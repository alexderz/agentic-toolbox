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
