import { test } from "node:test";
import assert from "node:assert/strict";
import { parseFrontmatter } from "../src/frontmatter.ts";

test("reads the YAML subset up to the first # line", () => {
  const r = parseFrontmatter("schemaVersion: 1\nid: builder\nreadOnly: false\ntools: [read, bash]\nskills: []\n\n## Role\nx\n");
  assert.deepEqual(r, {
    ok: true,
    fields: { schemaVersion: 1, id: "builder", readOnly: false, tools: ["read", "bash"], skills: [] },
    body: "## Role\nx\n",
  });
});

test("rejects quotes, nesting, comments, duplicates, and a --- fence", () => {
  for (const fm of [
    "id: 'x'", "id: x # c", "a:\n  b: 1", "id: x\nid: y", "list: [a, [b]]", "id: x y", "id:x", "&a: 1", "list: [a,]", "---\nid: x\n---",
  ]) {
    assert.equal(parseFrontmatter(`${fm}\n## Role\n`).ok, false, fm);
  }
});
