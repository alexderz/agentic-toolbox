// Every bundle and flow fixture is one case. A flow fixture is a
// directory: `expect.json` names the phase and the exact code set.
// `bundle` checks `bundle/`. `candidate` requires that bundle to pass,
// then checks `candidate.json` against the node whose exit is `choice`.
// `env-block` checks the one block in `block.md`. Nothing is skipped.

import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, lstatSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { checkBundle } from "../src/check.ts";
import { readFlow } from "../src/flow.ts";
import { formatIssue } from "../src/issue.ts";
import { envSectionError, validateResult, type Exit } from "../src/result.ts";

const repo = join(import.meta.dirname, "../../..");
const fixtures = join(repo, "docs/sdlc/fixtures");
const bundles = join(fixtures, "bundles");
const flows = join(fixtures, "flows");

interface Expect {
  valid: boolean;
  codes: string[];
  phase?: string;
}

const codesOf = (issues: { code: string }[]) => [...new Set(issues.map((i) => i.code))].sort();
const loadExpect = (file: string): Expect => JSON.parse(readFileSync(file, "utf8")) as Expect;

const bundleNames = readdirSync(bundles).filter((n) => lstatSync(join(bundles, n))?.isDirectory() === true).sort();
const flowNames = readdirSync(flows).filter((n) => lstatSync(join(flows, n))?.isDirectory() === true).sort();

test("bundle and flow fixtures are the landed set", () => {
  assert.deepEqual(bundleNames, ["minimal"]);
  assert.equal(flowNames.length, 32);
  assert.equal(flowNames.some((n) => !existsSync(join(flows, n, "expect.json"))), false);
});

for (const name of bundleNames) {
  test(`bundles/${name}`, () => {
    const want = loadExpect(join(bundles, `${name}.expect.json`));
    const issues = checkBundle(join(bundles, name));
    assert.deepEqual(
      { valid: issues.length === 0, codes: codesOf(issues) },
      { valid: want.valid, codes: [...want.codes].sort() },
      issues.map(formatIssue).join("\n"),
    );
  });
}

function flowCase(name: string): { valid: boolean; codes: string[]; lines: string[] } {
  const root = join(flows, name);
  const want = loadExpect(join(root, "expect.json"));
  if (want.phase === "bundle") {
    const issues = checkBundle(join(root, "bundle"));
    return { valid: issues.length === 0, codes: codesOf(issues), lines: issues.map(formatIssue) };
  }
  if (want.phase === "env-block") {
    const why = envSectionError(readFileSync(join(root, "block.md"), "utf8"));
    const codes = why === undefined ? [] : ["flow.env-block"];
    return { valid: codes.length === 0, codes, lines: why === undefined ? [] : [why] };
  }
  if (want.phase === "candidate") {
    const bundleIssues = checkBundle(join(root, "bundle"));
    if (bundleIssues.length > 0) {
      return { valid: false, codes: codesOf(bundleIssues), lines: ["bundle did not pass", ...bundleIssues.map(formatIssue)] };
    }
    const file = join(root, "candidate.json");
    const bytes = readFileSync(file);
    const choice = JSON.parse(bytes.toString("utf8")).choice;
    const flowFile = join(root, "bundle/flow.json");
    const read = readFlow(readFileSync(flowFile), flowFile);
    if (!read.flow) return { valid: false, codes: codesOf(read.issues), lines: read.issues.map(formatIssue) };
    const node = read.flow.nodes.find((n) => n.exits.some((e) => e.name === choice));
    if (!node) return { valid: false, codes: ["fixture"], lines: [`no node has exit ${String(choice)}`] };
    const kind = node.kind === "command" ? "command" : node.kind === "land" ? undefined : "model";
    const exits: Exit[] = node.exits.map((e) => ({ name: e.name, statuses: e.statuses, ...(e.checks ? { checks: e.checks } : {}) }));
    const v = validateResult(bytes, {
      step: node.step,
      ...(kind ? { kind } : {}),
      exits,
      checks: node.checks ?? [],
    }, file);
    return { valid: v.issues.length === 0, codes: codesOf(v.issues), lines: v.issues.map(formatIssue) };
  }
  return { valid: false, codes: ["fixture"], lines: [`unknown phase ${String(want.phase)}`] };
}

for (const name of flowNames) {
  test(`flows/${name}`, () => {
    const want = loadExpect(join(flows, name, "expect.json"));
    const got = flowCase(name);
    assert.deepEqual(
      { valid: got.valid, codes: got.codes },
      { valid: want.valid, codes: [...want.codes].sort() },
      got.lines.join("\n"),
    );
  });
}
