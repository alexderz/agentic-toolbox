# Rule map — result fixtures

Old: `docs/sdlc/fixtures/results/README.md` absent at main 7a11696.
New: [`docs/sdlc/fixtures/results/README.md`](../../../../docs/sdlc/fixtures/results/README.md), 9 lines.
These fixtures are result-only. Each `NAME.context.json` is invocation context (`ticket`, `runFolder`, `files`), not a second result.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | `NAME.json`, `NAME.context.json`, and `NAME.expect.json` are read together | new | Opening |
| — | Artifact checks run path, then run folder, then existence; a parse failure stops later checks | new | Last sentence |

## Meaning questions

None.
