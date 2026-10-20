import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { checkBundle } from "../src/check.ts";
import { formatIssue } from "../src/issue.ts";
import { codes, editFile, editFlow, exit, node, toolbox } from "./helpers.ts";

const broken = (f: (dir: string) => void, opts = {}) => {
  const { dir } = toolbox();
  f(dir);
  return codes(dir, opts);
};
const lines = (dir: string) => checkBundle(dir).map((i) => formatIssue(i).slice(dir.length + 1));

test("the ok fixture bundle is clean", () => {
  const { dir } = toolbox();
  assert.deepEqual(checkBundle(dir).map(formatIssue), []);
});

test("B1: strict reader and field tables", () => {
  assert.deepEqual(broken((d) => editFile(d, "flow.json", (t) => `${t} x`)), ["flow.json"]);
  assert.deepEqual(broken((d) => editFile(d, "flow.json", (t) => t.replace('"label": "Plan"', '"label": "Plan", "label": "P"'))), ["flow.json"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "plan").persona = "architect"))), ["flow.field"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "plan").label = "plan"))), ["flow.field"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (f.entry = "build"))), ["flow.field"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => delete f.itemEntry)), ["flow.field", "flow.unreachable"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (f.id = "other"))), ["flow.field"]);
});

test("B2: targets resolve; @items only from chunk; item never to chunk; unique ids", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "plan", "approve").to = "nowhere"))), ["flow.target", "flow.unreachable"]);
  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "verify", "fix").to = "spec"))).includes("flow.target"));
  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "verify", "fix").to = "@items"))).includes("flow.target"));
  assert.ok(broken((d) => editFlow(d, (f) => (node(f, "groom").id = "build"))).includes("flow.target"));
});

test("B3: reachability and dead ends", () => {
  assert.deepEqual(
    broken((d) => editFlow(d, (f) => f.nodes.push({ id: "extra", label: "Extra", step: "Build", kind: "model", scope: "chunk", persona: "architect", exits: [] }))),
    ["flow.dead-end", "flow.unreachable"],
  );
});

test("B4: command, gate, and land exit shapes", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => node(f, "prove").exits.pop())), ["flow.exit-shape"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "spec-gate", "reject").statuses = ["fail", "blocked"]))), ["flow.exit-shape"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "land", "done").name = "landed"))), ["flow.exit-shape"]);
  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "land", "done").to = "build"))).includes("flow.exit-shape"));
});

test("B5: reserved exit names are never listed", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => node(f, "spec").exits.push({ name: "stop", statuses: ["blocked"], to: "spec" }))), ["flow.reserved-listed"]);
});

test("B6: persona exists, scope matches, prompt kinds exist", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").persona = "ghost"))), ["flow.persona"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").persona = "builder"))), ["flow.persona"]);
  assert.deepEqual(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("## Prompt: merge-tip", "## Prompt: merge-later"))), ["persona.prompt-missing"]);
  assert.deepEqual(broken((d) => editFile(d, "personas/env-builder.md", (t) => t.replace("## Prompt: node-env-build", "## Prompt: node-other"))), ["persona.prompt-missing"]);
});

test("B7: front matter, read-only rule, tools, placeholders, body", () => {
  assert.deepEqual(broken((d) => editFile(d, "personas/security.md", (t) => t.replace("readOnly: true", "readOnly: false"))), ["persona.read-only"]);
  assert.deepEqual(broken((d) => editFile(d, "personas/security.md", (t) => t.replace("tools: [read,", "tools: [edit, read,"))), ["persona.tools"]);
  assert.deepEqual(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("tools: [read,", "tools: [shell, read,"))), ["persona.tools"]);
  assert.deepEqual(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("Exits: {{exits}}", "Exits: {{exitz}}"))), ["persona.placeholder"]);
  assert.ok(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("job: builder", "job: 'builder'"))).includes("persona.frontmatter"));
  assert.ok(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("id: builder", "id: builder-x"))).includes("persona.frontmatter"));
  assert.deepEqual(broken((d) => editFile(d, "personas/builder.md", (t) => t.replace("## Next", "## Next\n" + "- line\n".repeat(60)))), ["persona.body"]);
});

test("B8: skills resolve, have a SOURCES row or live in the bundle, and match ## Required skills", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "build").skills = ["ok-notes", "ghost"]))), ["bundle.skill"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "build").skills = ["ok-notes", "unlisted"]))), ["bundle.skill"]);
  assert.deepEqual(broken((d) => editFile(d, "bundle.md", (t) => t.replace("- `yagni`\n", ""))), ["bundle.skill"]);
});

test("B9: outputs and outputDirs are normalized repo-relative paths", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").outputs = ["../groom.md"]))), ["flow.output-path"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").outputDirs = ["docs/notes"]))), ["flow.output-path"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").outputDirs = ["docs/notes/"]))), []);
});

test("B10: land references and review checks", () => {
  assert.ok(broken((d) => editFlow(d, (f) => (node(f, "land").prove = "env-prove"))).includes("flow.land-ref"));
  assert.ok(broken((d) => editFlow(d, (f) => (node(f, "land").verify = "review"))).includes("flow.land-ref"));
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "review").checks = ["intake", "sha-pins"]))), ["flow.review-checks"]);
  assert.ok(broken((d) => editFlow(d, (f) => (node(f, "env-prove").commands = "groom"))).includes("flow.land-ref"));
});

test("B11: each gate row's counterexample names the last exit into the target", () => {
  const { dir } = toolbox();
  editFlow(dir, (f) => (exit(f, "plan", "approve").to = "spec"));
  assert.ok(lines(dir).includes("flow.json: node plan exit approve: gate.trial: reaches spec without passing the gate tagged trial"), lines(dir).join("\n"));

  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "security", "cleared").to = "env-build"))).includes("gate.spec"));
  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "env-review", "approve").to = "env-land"))).includes("gate.env"));
  assert.ok(broken((d) => editFlow(d, (f) => (exit(f, "verify", "ok").to = "land"))).includes("gate.land"));
  // A loop back to the builder after review still reaches land only through review.
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "review", "changes").to = "verify"))), []);
  const hld = { id: "hld", label: "Hld", step: "Plan", kind: "model", scope: "chunk", persona: "architect", outputs: ["{design}/hld.md"], exits: [{ name: "written", statuses: ["pass"], to: "plan" }] };
  assert.deepEqual(broken((d) => editFlow(d, (f) => (f.nodes.unshift(hld), (f.entry = "hld")))), ["gate.comparables"]);
  const comparables = { ...hld, id: "comparables", label: "Comp", outputs: ["{design}/comparables.md"], exits: [{ name: "written", statuses: ["pass"], to: "hld" }] };
  assert.deepEqual(broken((d) => editFlow(d, (f) => (f.nodes.unshift(comparables, hld), (f.entry = "comparables")))), []);
  assert.ok(broken((d) => editFlow(d, (f) => (f.entry = "spec"))).includes("gate.plan"));
});

test("B12: layout, links, sizes, headings, script intake", () => {
  assert.deepEqual(broken((d) => writeFileSync(join(d, "notes.txt"), "x")), ["bundle.layout"]);
  assert.deepEqual(broken((d) => symlinkSync("lint.sh", join(d, "scripts/link.sh"))), ["bundle.layout"]);
  assert.deepEqual(broken((d) => writeFileSync(join(d, "skills/ok-notes/big.md"), "x".repeat(256 * 1024 + 1))), ["bundle.layout"]);
  assert.deepEqual(broken((d) => editFile(d, "bundle.md", (t) => t.replace("## Modes", "## Mode"))), ["bundle.layout"]);
  assert.deepEqual(broken((d) => editFile(d, "bundle.md", (t) => t.replace("- `security`\n", ""))), ["bundle.layout"]);
  assert.deepEqual(broken((d) => editFile(d, "scripts/lint.sh", (t) => `${t}# changed\n`)), ["bundle.script-intake"]);
  assert.deepEqual(broken((d) => writeFileSync(join(d, "scripts/new.sh"), "exit 0\n")), ["bundle.script-intake"]);
  assert.deepEqual(broken(() => {}, { intake: "# Intake\n\n## Script records\n\n" }), ["bundle.script-intake"]);
  const { dir } = toolbox();
  const sha = /sha256 `([0-9a-f]{64})`/.exec(readFileSync(join(dir, "bundle.md"), "utf8"))![1];
  const intake = `## Script records\n\n- \`ok-lint\` \`bundles/ok/scripts/lint.sh\` sha256 \`${sha}\`\n`;
  assert.deepEqual(codes(dir, { intake }), []);
});

test("B13: extract only on gate exits, with normalized paths", () => {
  const x = { from: "{design}/hld.md", heading: "Trial kickoff", to: "kickoff.md" };
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "spec", "written").extract = x))), ["flow.extract"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "trial", "approve").extract = { ...x, to: "Kick.md" }))), ["flow.extract"]);
  assert.deepEqual(broken((d) => editFlow(d, (f) => (exit(f, "trial", "approve").extract = { ...x, from: "/etc/x" }))), ["flow.extract"]);
});

test("B14: envSpec once, on a Spec node with an lld.md output; env commands need it", () => {
  assert.deepEqual(broken((d) => editFlow(d, (f) => (node(f, "groom").envSpec = true))), ["flow.env"]);
  assert.ok(broken((d) => editFlow(d, (f) => delete node(f, "spec").envSpec)).includes("flow.env"));
});

test("a missing flow.json or bundle.md is a layout error", () => {
  assert.deepEqual(broken((d) => rmSync(join(d, "flow.json"))), ["bundle.layout"]);
  assert.ok(broken((d) => rmSync(join(d, "bundle.md"))).includes("bundle.layout"));
});
