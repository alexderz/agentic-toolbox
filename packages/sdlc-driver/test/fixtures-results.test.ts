// Every result fixture is one case. `NAME.json` is the body,
// `NAME.context.json` is the invocation (ticket, run folder, files),
// and `NAME.expect.json` is the exact code set. Context files are not
// results. Nothing is skipped.

import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdirSync, mkdtempSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { tmpdir } from "node:os";
import { validateResult } from "../src/result.ts";

const dir = join(import.meta.dirname, "../../../docs/sdlc/fixtures/results");
const names = readdirSync(dir)
  .filter((f) => f.endsWith(".json") && !f.endsWith(".expect.json") && !f.endsWith(".context.json"))
  .sort();

test("result fixtures cover every landed body", () => {
  assert.equal(names.length, 22);
});

for (const name of names) {
  test(`results/${name}`, () => {
    const bytes = readFileSync(join(dir, name));
    const expect = JSON.parse(readFileSync(join(dir, name.replace(/\.json$/, ".expect.json")), "utf8")) as { valid: boolean; codes: string[] };
    const context = JSON.parse(readFileSync(join(dir, name.replace(/\.json$/, ".context.json")), "utf8")) as {
      ticket: string;
      runFolder: string;
      files: string[];
    };
    const root = mkdtempSync(join(tmpdir(), "sdlc-fixture-run-"));
    for (const rel of context.files) {
      const path = join(root, rel);
      if (rel.endsWith("/")) mkdirSync(path, { recursive: true });
      else {
        mkdirSync(dirname(path), { recursive: true });
        writeFileSync(path, "x\n");
      }
    }
    const v = validateResult(bytes, { ticket: context.ticket, runRoot: root, runFolder: context.runFolder }, name);
    const codes = [...new Set(v.issues.map((i) => i.code))].sort();
    assert.deepEqual({ valid: v.issues.length === 0, codes }, { valid: expect.valid, codes: [...expect.codes].sort() });
  });
}
