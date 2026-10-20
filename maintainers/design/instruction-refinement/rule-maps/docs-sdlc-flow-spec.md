# Rule map — `docs/sdlc/flow-spec.md`

Item: DER-421 (G2).

Old: `docs/sdlc/flow-spec.md` absent at main 7a11696.
New: [`docs/sdlc/flow-spec.md`](../../../../docs/sdlc/flow-spec.md), 186 lines.
New file. Layout, personas, prompt kinds, and placeholders stay in `docs/sdlc/bundle-spec.md`. Result fields stay in `docs/sdlc/stage-result.md`; this file does not restate their patterns.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | `flow.json` fields, node fields, and strict-reader code `flow.json` | new | flow.json, L9–46 |
| — | Exit shape, `@items`, `@done`, `extract` | new | Exits, L47–60 |
| — | Reserved `stop` and `operator` | new | Reserved exits, L61–71 |
| — | Driver-fixed exits for land, manager, repair, answer, and rehydrate | new | Driver-fixed exits, L72–89 |
| — | `json sdlc-env` block and `flow.env-block` | new | json sdlc-env, L90–103 |
| — | Chunk land, re-entry choices `env`, `spec`, `deny`, `defer` | new | Chunk land and re-entry, L104–118 |
| — | Candidate rules 1–10 extend the stage-result fields | new | Candidate rules, L119–145 |
| — | Bundle check B1–B14 and the six `gate.*` rows | new | Bundle check, L146–179 |
| — | Fixture phases. `phase` `bundle` checks `bundle/` for that code set only | new | Fixtures, L180–186 |

## Meaning questions

None.
