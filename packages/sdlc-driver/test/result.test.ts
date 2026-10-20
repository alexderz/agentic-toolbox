import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, symlinkSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { validateCandidate, validateResult, type Invocation } from "../src/result.ts";

const base = {
  schemaVersion: 1, step: "Build", status: "pass", choice: "review", ticket: "der-a530",
  artifact: "builder-a530/run-1/result.md",
  evidence: { kind: "model", checks: ["dod: acceptance holds"] }, findings: "",
};
const text = (patch: Record<string, unknown>, drop: string[] = []) => {
  const o: Record<string, unknown> = { ...base, ...patch };
  for (const k of drop) delete o[k];
  return JSON.stringify(o);
};
const codes = (input: string, inv: Invocation = {}) => validateResult(input, inv).issues.map((i) => i.code).sort();

test("a v1 result with no invocation checks patterns only", () => {
  assert.deepEqual(codes(text({})), []);
});

test("every top-level field is required", () => {
  assert.deepEqual(codes(text({}, ["ticket"])), ["result.ticket-pattern"]);
  assert.deepEqual(codes(text({}, ["schemaVersion"])), ["result.schema-version"]);
  assert.deepEqual(codes(text({ schemaVersion: 1.5 })), ["result.schema-version"]);
});

test("the artifact path rules", () => {
  for (const a of ["/abs/x", "a/./b", "a\\b", "a//b", "", "a b"]) {
    assert.deepEqual(codes(text({ artifact: a })), ["result.artifact-path"], a);
  }
});

test("the invocation fixes step, ticket, and kind", () => {
  const inv: Invocation = { step: "Build", ticket: "der-a530", kind: "command" };
  assert.deepEqual(codes(text({ ticket: "der-b1" }), { ticket: "der-a530" }), ["result.ticket-mismatch"]);
  assert.deepEqual(codes(text({ step: "Spec" }), { step: "Build" }), ["result.step"]);
  assert.deepEqual(codes(text({}), inv), ["result.evidence-kind"]);
});

test("artifact must lie in the run folder and exist", () => {
  const root = mkdtempSync(join(tmpdir(), "sdlc-result-"));
  mkdirSync(join(root, "builder-a530/run-1/out"), { recursive: true });
  writeFileSync(join(root, "builder-a530/run-1/result.md"), "x");
  const inv: Invocation = { runRoot: root, runFolder: "builder-a530/run-1/" };
  assert.deepEqual(codes(text({}), inv), []);
  assert.deepEqual(codes(text({ artifact: "builder-a530/run-1/out/" }), inv), []);
  assert.deepEqual(codes(text({ artifact: "builder-a530/run-1/absent.md" }), inv), ["result.artifact-missing"]);
  assert.deepEqual(codes(text({ artifact: "builder-a530/run-1/out" }), inv), ["result.artifact-missing"]);
  assert.deepEqual(codes(text({ artifact: "builder-a530/run-2/result.md" }), inv), ["result.artifact-outside-run"]);
  symlinkSync("result.md", join(root, "builder-a530/run-1/link.md"));
  assert.deepEqual(codes(text({ artifact: "builder-a530/run-1/link.md" }), inv), ["result.artifact-missing"]);
});

test("evidence fields by condition", () => {
  assert.deepEqual(codes(text({ evidence: { kind: "model", checks: ["a\nb"] } })), ["result.evidence-missing"]);
  assert.deepEqual(codes(text({ evidence: { kind: "model", checks: ["x"], foo: 1 } })), ["result.unknown-key"]);
  assert.deepEqual(codes(text({ status: "blocked", findings: "x", evidence: { kind: "model" } })), ["result.evidence-missing"]);
  assert.deepEqual(codes(text({ status: "blocked", findings: "x", evidence: { kind: "model", blocker: "ABC-1" } })), []);
  assert.deepEqual(
    codes(text({ status: "fail", findings: "x", evidence: { kind: "command", command: "npm test", exit_code: 1.0 } }).replace('"exit_code":1', '"exit_code":1.0')),
    ["result.evidence-missing"],
  );
  assert.deepEqual(
    codes(text({ status: "fail", findings: "", evidence: { kind: "command", command: "npm test", exit_code: 0 } })),
    ["result.command-disagreement", "result.findings-empty"],
  );
});

const exits = [
  { name: "review", statuses: ["pass"] },
  { name: "retry", statuses: ["fail"] },
];

test("with a flow, choice must be an exit allowed for the status", () => {
  assert.deepEqual(codes(text({}), { exits }), []);
  assert.deepEqual(codes(text({ choice: "retry" }), { exits }), ["flow.choice-not-allowed"]);
  const stop = text({ choice: "stop", status: "needs_input", evidence: { kind: "model", question: "q?" } });
  assert.deepEqual(codes(stop, { exits }), []);
  assert.deepEqual(codes(stop, { exits, reserved: [] }), ["flow.choice-not-allowed"]);
  const failOp = text({ choice: "operator", status: "fail", findings: "check failed", evidence: { kind: "model" } });
  assert.deepEqual(codes(failOp, { exits }), ["flow.reserved-status"]);
  assert.deepEqual(codes(failOp, { exits, driverAuthored: true }), []);
});

test("required checks need a finding; n/a counts only for node checks", () => {
  const ev = (checks: string[]) => text({ evidence: { kind: "model", checks } });
  const inv: Invocation = { exits: [{ name: "review", statuses: ["pass"], checks: ["sha-pins"] }], checks: ["dod"] };
  assert.deepEqual(codes(ev(["dod: holds", "sha-pins: all pinned"]), inv), []);
  assert.deepEqual(codes(ev(["dod: n/a — docs only", "sha-pins: ok"]), inv), []);
  assert.deepEqual(codes(ev(["dod: holds", "sha-pins: n/a — none"]), inv), ["flow.check-missing"]);
  assert.deepEqual(codes(ev(["dod:", "sha-pins: ok"]), inv), ["flow.check-missing"]);
});

function runFolder(): string {
  const dir = mkdtempSync(join(tmpdir(), "sdlc-cand-"));
  writeFileSync(join(dir, "state.md"), "## Next\nbuild\n");
  writeFileSync(join(dir, "result.md"), "done\n");
  return dir;
}

test("a candidate may omit fixed fields; present ones must match", () => {
  const dir = runFolder();
  const inv = { step: "Build", ticket: "der-a530", kind: "model" as const, runFolderAbs: dir };
  const r = validateCandidate(text({}, ["schemaVersion", "step", "ticket"]), inv);
  assert.deepEqual(r.issues, []);
  assert.equal(r.result?.ticket, "der-a530");
  assert.equal(r.result?.schemaVersion, 1);
  const bad = validateCandidate(text({ ticket: "der-b1" }), inv);
  assert.deepEqual(bad.issues.map((i) => i.code), ["flow.fixed-field"]);
  const kind = validateCandidate(text({ evidence: { checks: ["x"] } }), inv);
  assert.deepEqual(kind.issues.map((i) => i.code), []);
});

test("candidate run-folder rules: outputs, symlinks, state size, env-capability", () => {
  const dir = runFolder();
  const inv = { runFolderAbs: dir, outputs: ["{design}/lld.md"], designDir: "docs/design" };
  assert.deepEqual(validateCandidate(text({}), inv).issues.map((i) => i.code), ["flow.output-missing"]);
  mkdirSync(join(dir, "out/docs/design"), { recursive: true });
  writeFileSync(join(dir, "out/docs/design/lld.md"), "# LLD\n");
  assert.deepEqual(validateCandidate(text({}), inv).issues, []);
  symlinkSync("/etc/passwd", join(dir, "out/x"));
  assert.deepEqual(validateCandidate(text({}), inv).issues.map((i) => i.code), ["flow.output-symlink"]);

  const d2 = runFolder();
  writeFileSync(join(d2, "state.md"), "x\n".repeat(61));
  assert.deepEqual(validateCandidate(text({}), { runFolderAbs: d2 }).issues.map((i) => i.code), ["flow.state-size"]);
  writeFileSync(join(d2, "state.md"), "x".repeat(6001));
  assert.deepEqual(validateCandidate(text({}), { runFolderAbs: d2 }).issues.map((i) => i.code), ["flow.state-size"]);

  const d3 = runFolder();
  const cap = (status: string, choice: string, more: Record<string, unknown>) =>
    validateCandidate(text({ status, choice, evidence: { kind: "model", checks: ["env-capability: needs postgres"], ...more } }), { runFolderAbs: d3 }).issues.map((i) => i.code);
  // Candidate rule 10 needs `checks` on needs_input, which item 1 calls
  // evidence-extra; only env-capability entries are allowed there.
  assert.deepEqual(cap("needs_input", "operator", { question: "add postgres?" }), []);
  assert.deepEqual(cap("needs_input", "stop", { question: "add postgres?" }), ["flow.env-capability"]);
  assert.deepEqual(cap("pass", "review", {}), ["flow.env-capability"]);
});

test("candidate rules 7 to 9: clean worktree, ledger, env block", () => {
  const dir = runFolder();
  const wt = mkdtempSync(join(tmpdir(), "sdlc-wt-"));
  const gitc = (...args: string[]) => {
    const r = spawnSync("git", ["-c", "user.name=t", "-c", "user.email=t@t.invalid", "-c", "core.hooksPath=/dev/null", ...args], { cwd: wt });
    assert.equal(r.status, 0, r.stderr?.toString());
  };
  gitc("init", "-q");
  writeFileSync(join(wt, "a.txt"), "a\n");
  gitc("add", "a.txt");
  gitc("commit", "-q", "-m", "a");
  const dirty = validateCandidate(text({}), { runFolderAbs: dir, builder: true, worktree: wt });
  assert.deepEqual(dirty.issues.map((i) => i.code), []);
  writeFileSync(join(wt, "b.txt"), "b\n");
  assert.deepEqual(validateCandidate(text({}), { runFolderAbs: dir, builder: true, worktree: wt }).issues.map((i) => i.code), ["flow.uncommitted"]);

  const vdir = runFolder();
  const ledger = [{ id: "V1", criticality: "major", status: "open", summary: "gap", raised: "run-1", fixed: "" }];
  writeFileSync(join(vdir, "ledger.json"), JSON.stringify(ledger));
  const fail = text({ status: "fail", findings: "gap", evidence: { kind: "model" } });
  assert.deepEqual(validateCandidate(fail, { runFolderAbs: vdir, verifier: true }).issues.map((i) => i.code), []);
  assert.deepEqual(validateCandidate(text({}), { runFolderAbs: vdir, verifier: true }).issues.map((i) => i.code), ["flow.ledger"]);
  const row = ledger[0]!;
  row.status = "fixed";
  row.fixed = "run-2";
  writeFileSync(join(vdir, "ledger.json"), JSON.stringify(ledger));
  assert.deepEqual(validateCandidate(text({}), { runFolderAbs: vdir, verifier: true }).issues.map((i) => i.code), []);

  const edir = runFolder();
  const lld = join(edir, "out/docs/lld.md");
  mkdirSync(join(edir, "out/docs"), { recursive: true });
  const block = {
    schemaVersion: 1, toolchain: ["node --version"], deps: [], passEnv: ["AD_BIND_DN"],
    prove: ["npm test"], test: "npm test",
  };
  writeFileSync(lld, `# LLD\n\n## Build environment\n\n\`\`\`json sdlc-env\n${JSON.stringify(block)}\n\`\`\`\n`);
  const einv = { runFolderAbs: edir, envSpec: true, outputs: ["{design}/lld.md"], designDir: "docs" };
  assert.deepEqual(validateCandidate(text({}), einv).issues.map((i) => i.code), []);
  writeFileSync(lld, `# LLD\n\n## Other\n\nno block\n`);
  assert.deepEqual(validateCandidate(text({}), einv).issues.map((i) => i.code), ["flow.env-block"]);
});
