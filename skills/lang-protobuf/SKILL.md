---
name: lang-protobuf
description: use this when writing or reviewing *.proto files or generated stubs you are allowed to edit. generated code is usually not hand-edited. load with the host language when you also change application code.
---

# Protocol Buffers

No `scripts/`.
Process skills that may load with this one, and the host language skill beside it: `language-router` [Load-with list](../language-router/SKILL.md#load-with-list), [Algorithm](../language-router/SKILL.md#algorithm) step 6.

## Iron law

**Fields are forever. Reserve deleted numbers. Do not hand-edit
generated stubs.**

## Tooling / verify

Regenerate with the project's command (`buf generate`, `protoc`, etc.).
Diff only the intended schema change plus the expected generated files.

## Idioms a linter misses

- Add fields. Do not reuse field numbers.
- `reserved` numbers and names when removing.
- Use `optional` / presence as the proto edition in the repo already
  does.
- Keep packages stable. Compatibility is the API.
- Comments say why a field exists, not what the type is.

## Errors

- Unknown fields must survive a round-trip on old clients. Do not
  strip them in app code.

## Testing

- Old client + new field must parse.
- Golden encoded bytes for wire format if the repo has them.

## PR review

- No reused numbers.
- No type change of a shipped field.
- Generated files only from codegen.

## Security

- Treat decoded protobuf as untrusted input in the host language
  (size limits, required-meaning fields validated after parse).
- Do not embed secrets in proto comments committed to git.

## Always

- Additive changes. `reserved` on delete. Codegen, not hand edits.

## Ask first

- Renaming a shipped field.
- Changing a field type.
- Breaking package rename.

## Never

- Reusing a field number.
- Editing generated `*.pb.go` / `*_pb2.py` / `*.pb.ts` by hand.

## Red flags

- "I'll reuse field 3, nothing uses it"
- "I'll just tweak the generated stub"
