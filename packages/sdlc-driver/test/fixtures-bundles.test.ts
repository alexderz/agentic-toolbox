// Every fixture under docs/sdlc/fixtures/bundles/ and flows/ (item 2) is a
// test. A bundle fixture `bundles/NAME/` is clean unless
// `bundles/NAME.expect.json` says otherwise. A flow fixture
// `flows/NAME.json` replaces flow.json in a copy of `bundles/minimal/`.
// Expect files are `{"valid": bool, "codes": [...]}`.

import { test } from "node:test";
import assert from "node:assert/strict";
import { cpSync, existsSync, lstatSync, mkdtempSync, readdirSync, readFileSync, symlinkSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { checkBundle } from "../src/check.ts";
import { formatIssue } from "../src/issue.ts";

const repo = join(import.meta.dirname, "../../..");
const fixtures = join(repo, "docs/sdlc/fixtures");
const bundles = join(fixtures, "bundles");
const flows = join(fixtures, "flows");
// Candidate rule 9 (the env block) is checked on a stage result, not by
// the bundle check; its fixtures belong to the env parser.
const NOT_BUNDLE_CHECK = ["flow.env-block"];

const expectOf = (file: string) => (existsSync(file) ? JSON.parse(readFileSync(file, "utf8")) : { valid: true, codes: [] });
const result = (dir: string) => {
  const issues = checkBundle(dir);
  return { valid: issues.length === 0, codes: [...new Set(issues.map((i) => i.code))].sort(), lines: issues.map(formatIssue) };
};

const bundleNames = existsSync(bundles) ? readdirSync(bundles).filter((n) => lstatSync(join(bundles, n))?.isDirectory()) : [];
if (bundleNames.length === 0) test("docs/sdlc/fixtures/bundles", (t) => t.skip("no bundle fixtures yet: G2 has not landed docs/sdlc/fixtures/bundles/"));
for (const name of bundleNames) {
  test(`bundles/${name}`, () => {
    const want = expectOf(join(bundles, `${name}.expect.json`));
    const got = result(join(bundles, name));
    assert.deepEqual({ valid: got.valid, codes: got.codes }, { valid: want.valid, codes: [...want.codes].sort() }, got.lines.join("\n"));
  });
}

const flowNames = existsSync(flows) ? readdirSync(flows).filter((n) => n.endsWith(".json") && !n.endsWith(".expect.json")) : [];
if (flowNames.length === 0) test("docs/sdlc/fixtures/flows", (t) => t.skip("no flow fixtures yet: G2 has not landed docs/sdlc/fixtures/flows/"));
else if (!existsSync(join(bundles, "minimal"))) test("docs/sdlc/fixtures/flows", (t) => t.skip("flow fixtures need docs/sdlc/fixtures/bundles/minimal/"));
else {
  for (const name of flowNames) {
    test(`flows/${name}`, (t) => {
      const want = expectOf(join(flows, name.replace(/\.json$/, ".expect.json")));
      if (want.codes.some((c: string) => NOT_BUNDLE_CHECK.includes(c))) return t.skip(`${want.codes.join(", ")} is not a bundle-check code`);
      const bytes = readFileSync(join(flows, name));
      let id = "minimal";
      try {
        const v = JSON.parse(bytes.toString("utf8")).id;
        if (typeof v === "string" && /^[a-z][a-z0-9-]{0,31}$/.test(v)) id = v;
      } catch {
        // an unparsable flow keeps the minimal bundle's id
      }
      const root = mkdtempSync(join(tmpdir(), "sdlc-flow-fixture-"));
      const dir = join(root, "bundles", id);
      cpSync(join(bundles, "minimal"), dir, { recursive: true });
      writeFileSync(join(dir, "flow.json"), bytes);
      symlinkSync(join(repo, "skills"), join(root, "skills"));
      cpSync(join(repo, "SOURCES.md"), join(root, "SOURCES.md"));
      const md = readFileSync(join(dir, "bundle.md"), "utf8");
      writeFileSync(join(dir, "bundle.md"), md.replace(/^# Bundle — .*$/m, `# Bundle — ${id}`));
      const got = result(dir);
      assert.deepEqual({ valid: got.valid, codes: got.codes }, { valid: want.valid, codes: [...want.codes].sort() }, got.lines.join("\n"));
    });
  }
}
