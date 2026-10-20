import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdirSync, mkdtempSync, symlinkSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { editFlow, exit, run, toolbox } from "./helpers.ts";

test("check: clean exits 0 and prints nothing", () => {
  const { dir } = toolbox();
  assert.deepEqual(run(["check", dir]), { status: 0, out: "", err: "" });
});

test("check: one error per line in the flow-spec format, exit 1", () => {
  const { root } = toolbox();
  editFlow(join(root, "bundles/ok"), (f) => (exit(f, "plan", "approve").name = "stop"));
  const r = run(["check", "bundles/ok"], root);
  assert.equal(r.status, 1);
  assert.equal(r.out, "bundles/ok/flow.json: node plan exit stop: flow.reserved-listed: stop is reserved and never listed\n");
  writeFileSync(join(root, "bundles/ok/extra.md"), "x");
  assert.match(run(["check", "bundles/ok"], root).out, /^bundles\/ok\/extra\.md: -: bundle\.layout: not an allowed top-level entry$/m);
});

test("check: usage errors exit 2", () => {
  assert.equal(run([]).status, 2);
  assert.equal(run(["check"]).status, 2);
  assert.equal(run(["check", "a", "--at"]).status, 2);
  assert.equal(run(["validate", "r.json", "--flow", "f.json"]).status, 2);
});

const gitc = (cwd: string, ...args: string[]) => {
  const r = spawnSync("git", ["-c", "user.name=t", "-c", "user.email=t@t.invalid", "-c", "core.hooksPath=/dev/null", ...args], { cwd });
  assert.equal(r.status, 0, r.stderr.toString("utf8"));
};

test("check --at reads the commit, not the working tree", () => {
  const { root, dir } = toolbox();
  gitc(root, "init", "-q");
  gitc(root, "add", "-A");
  gitc(root, "commit", "-q", "-m", "ok");
  editFlow(dir, (f) => (exit(f, "plan", "approve").to = "nowhere"));
  assert.equal(run(["check", dir]).status, 1);
  assert.deepEqual(run(["check", dir, "--at", "HEAD"]), { status: 0, out: "", err: "" });
  symlinkSync("lint.sh", join(dir, "scripts/link.sh"));
  gitc(root, "add", "-A");
  gitc(root, "commit", "-q", "-m", "link");
  const r = run(["check", dir, "--at", "HEAD"]);
  assert.equal(r.status, 1);
  assert.match(r.out, /scripts\/link\.sh: -: bundle\.layout: symbolic link/);
  assert.equal(run(["check", dir, "--at", "no-such-ref"]).status, 2);
});

function runRoot(): { root: string; flow: string } {
  const { dir } = toolbox();
  const root = mkdtempSync(join(tmpdir(), "sdlc-run-"));
  mkdirSync(join(root, "reviewer-a530/run-1"), { recursive: true });
  writeFileSync(join(root, "reviewer-a530/run-1/result.md"), "ok\n");
  return { root, flow: join(dir, "flow.json") };
}

const review = (choice: string, checks: string[]) =>
  JSON.stringify({
    schemaVersion: 1, step: "Review", status: "pass", choice, ticket: "der-a530",
    artifact: "reviewer-a530/run-1/result.md", evidence: { kind: "model", checks }, findings: "",
  });

test("validate: a result that holds for the node exits 0", () => {
  const { root, flow } = runRoot();
  const file = join(root, "reviewer-a530/run-1/result.json");
  writeFileSync(file, review("approve", ["intake: none", "sha-pins: pinned", "trust-boundary: unchanged"]));
  assert.deepEqual(run(["validate", file, "--flow", flow, "--node", "review"]), { status: 0, out: "", err: "" });
});

test("validate: ticket context and reserved fail follow authorship", () => {
  const { root, flow } = runRoot();
  const file = join(root, "reviewer-a530/run-1/result.json");
  const body = (choice: string, status: string, ticket = "der-a530") => JSON.stringify({
    schemaVersion: 1, step: "Review", status, choice, ticket,
    artifact: "reviewer-a530/run-1/result.md",
    evidence: status === "pass" ? { kind: "model", checks: ["intake: none", "sha-pins: pinned", "trust-boundary: unchanged"] } : { kind: "model" },
    findings: status === "fail" || status === "blocked" ? "check failed" : "",
  });
  writeFileSync(file, body("approve", "pass"));
  assert.equal(run(["validate", file, "--flow", flow, "--node", "review", "--ticket", "der-a530"]).status, 0);
  const wrong = run(["validate", file, "--flow", flow, "--node", "review", "--ticket", "der-other"]);
  assert.equal(wrong.status, 1);
  assert.match(wrong.out, /result\.ticket-mismatch/);
  writeFileSync(file, body("operator", "fail"));
  const worker = run(["validate", file, "--flow", flow, "--node", "review"]);
  assert.equal(worker.status, 1);
  assert.match(worker.out, /flow\.reserved-status/);
  assert.equal(run(["validate", file, "--flow", flow, "--node", "review", "--authored", "driver"]).status, 0);
  writeFileSync(file, body("stop", "fail"));
  assert.match(run(["validate", file, "--flow", flow, "--node", "review"]).out, /flow\.reserved-status/);
  assert.equal(run(["validate", file, "--flow", flow, "--node", "review", "--authored", "driver"]).status, 0);
  assert.equal(run(["validate", file, "--flow", flow, "--node", "review", "--authored", "guest"]).status, 2);
});

test("validate: flow-aware errors, one per line, exit 1", () => {
  const { root, flow } = runRoot();
  const file = join(root, "reviewer-a530/run-1/result.json");
  writeFileSync(file, review("approve", ["intake: none", "sha-pins: n/a — none", "trust-boundary: unchanged"]));
  const r = run(["validate", file, "--flow", flow, "--node", "review"]);
  assert.equal(r.status, 1);
  assert.equal(r.out, `${file}: evidence.checks: flow.check-missing: no finding for exit check sha-pins\n`);
  writeFileSync(file, review("land", ["intake: a", "sha-pins: b", "trust-boundary: c"]));
  assert.match(run(["validate", file, "--flow", flow, "--node", "review"]).out, /flow\.choice-not-allowed/);
  writeFileSync(file, review("approve", ["intake: a", "sha-pins: b", "trust-boundary: c"]).replace('"Review"', '"Build"'));
  assert.match(run(["validate", file, "--flow", flow, "--node", "review"]).out, /: step: result\.step: /);
  assert.equal(run(["validate", file, "--flow", flow, "--node", "ghost"]).status, 2);
});

// The fixed manager invocation is outside flow.nodes. Its original node is
// explicit so a result cannot choose its own stage or bypass a human gate.
function managerFixture() {
  const root = mkdtempSync(join(tmpdir(), "sdlc-manager-"));
  const folder = join(root, "manager/run-1");
  mkdirSync(folder, { recursive: true });
  writeFileSync(join(folder, "result.md"), "Operator decision required.\n");
  const file = join(folder, "result.json");
  const flow = join(import.meta.dirname, "../../../docs/sdlc/fixtures/bundles/minimal/flow.json");
  const result = { schemaVersion: 1, step: "Brief", status: "needs_input", choice: "escalate", ticket: "der-a530",
    artifact: "manager/run-1/result.md", evidence: { kind: "model", question: "Accept this brief?" }, findings: "Operator decision required." };
  return { file, flow, result };
}

test("validate: fixed manager gate escalation requires original-node context", () => {
  const { file, flow, result } = managerFixture();
  writeFileSync(file, JSON.stringify(result));
  const args = ["validate", file, "--flow", flow, "--node", "manager"];
  assert.equal(run(args).status, 2);
  assert.equal(run([...args, "--for-node", "ghost"]).status, 2);
  assert.deepEqual(run([...args, "--for-node", "ask"]), { status: 0, out: "", err: "" });
  writeFileSync(file, JSON.stringify({ ...result, step: "Build" }));
  assert.match(run([...args, "--for-node", "ask"]).out, /result.step/);
  writeFileSync(file, JSON.stringify({ ...result, choice: "resume", status: "pass", evidence: { kind: "model", checks: ["source: gather brief.md"] } }));
  assert.match(run([...args, "--for-node", "ask"]).out, /flow.choice-not-allowed/);
});

test("validate: fixed manager resume needs a recognized source finding", () => {
  const { file, flow, result } = managerFixture();
  const pass = { ...result, status: "pass", choice: "resume", evidence: { kind: "model", checks: ["source: gather brief.md"] } };
  const args = ["validate", file, "--flow", flow, "--node", "manager", "--for-node", "refine"];
  writeFileSync(file, JSON.stringify(pass));
  assert.equal(run(args).status, 0);
  writeFileSync(file, JSON.stringify({ ...pass, evidence: { kind: "model", checks: ["source: guess nowhere"] } }));
  assert.match(run(args).out, /flow.check-missing/);
  assert.equal(run(["validate", file, "--flow", flow, "--node", "refine", "--for-node", "refine"]).status, 2);
});
