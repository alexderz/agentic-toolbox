import { test } from "node:test";
import assert from "node:assert/strict";
import { JsonFloat, readStrictJson } from "../src/json.ts";

test("reads nested values", () => {
  const r = readStrictJson('{"a": [1, "x\\u00e9", true, {"b": false}], "c": -0}');
  assert.deepEqual(r, { ok: true, value: { a: [1, "xé", true, { b: false }], c: -0 } });
});

test("a fraction or exponent is a JsonFloat, not an integer", () => {
  const r = readStrictJson('{"a": 1.0, "b": 1e2}');
  assert.ok(r.ok);
  const v = r.value as Record<string, unknown>;
  assert.ok(v.a instanceof JsonFloat);
  assert.equal((v.b as JsonFloat).value, 100);
});

test("rejects a duplicate key at any depth", () => {
  const r = readStrictJson('{"a": {"b": 1, "b": 2}}');
  assert.deepEqual(r.ok ? undefined : r.error.kind, "duplicate-key");
});

test("rejects a null anywhere", () => {
  const r = readStrictJson('{"a": [null]}');
  assert.deepEqual(r.ok ? undefined : r.error.kind, "null");
});

test("rejects trailing text", () => {
  const r = readStrictJson('{"a": 1} x');
  assert.deepEqual(r.ok ? undefined : r.error.kind, "trailing-text");
});

test("accepts trailing whitespace", () => {
  assert.ok(readStrictJson('{"a": 1}\n').ok);
});

test("rejects a syntax error, a BOM, and invalid UTF-8", () => {
  for (const text of ['{"a": 1,}', "﻿{}", "{'a': 1}", ""]) {
    const r = readStrictJson(text);
    assert.equal(r.ok ? undefined : r.error.kind, "syntax", text);
  }
  const bad = readStrictJson(new Uint8Array([0x7b, 0xff, 0x7d]));
  assert.equal(bad.ok ? undefined : bad.error.kind, "syntax");
});

test("rejects a control character inside a string", () => {
  const r = readStrictJson('{"a": "x\ny"}');
  assert.equal(r.ok ? undefined : r.error.kind, "syntax");
});
