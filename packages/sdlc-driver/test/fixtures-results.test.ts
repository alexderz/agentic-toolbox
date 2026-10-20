// Every fixture under docs/sdlc/fixtures/results/ (item 1) is a test.
// The fixtures leave the invocation implicit; this test supplies it:
// ticket DER-529, run folder `<step in lower case>-1/` (`build-1/` for
// a bad step), and a run root that holds result.md and commands.json in
// that folder.

import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, mkdirSync, mkdtempSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import { STEPS, validateResult } from "../src/result.ts";

const dir = join(import.meta.dirname, "../../../docs/sdlc/fixtures/results");
const names = existsSync(dir) ? readdirSync(dir).filter((f) => f.endsWith(".json") && !f.endsWith(".expect.json")) : [];

if (names.length === 0) {
  test("docs/sdlc/fixtures/results", (t) => t.skip("no result fixtures yet: G1 has not landed docs/sdlc/fixtures/results/"));
}

const root = mkdtempSync(join(tmpdir(), "sdlc-fixture-run-"));
for (const folder of ["build-1", "spec-1", "brief-1", "other-stage"]) {
  mkdirSync(join(root, folder), { recursive: true });
  writeFileSync(join(root, folder, "result.md"), "x\n");
  writeFileSync(join(root, folder, "commands.json"), "[]\n");
}

for (const name of names) {
  test(`results/${name}`, () => {
    const bytes = readFileSync(join(dir, name));
    const expect = JSON.parse(readFileSync(join(dir, name.replace(/\.json$/, ".expect.json")), "utf8"));
    let step = "build";
    try {
      const s = JSON.parse(bytes.toString("utf8")).step;
      if ((STEPS as readonly string[]).includes(s)) step = s.toLowerCase();
    } catch {
      // unparsable fixtures keep the default folder
    }
    const v = validateResult(bytes, { ticket: "DER-529", runRoot: root, runFolder: `${step}-1/` }, name);
    const codes = [...new Set(v.issues.map((i) => i.code))].sort();
    assert.deepEqual({ valid: v.issues.length === 0, codes }, { valid: expect.valid, codes: [...expect.codes].sort() });
  });
}
