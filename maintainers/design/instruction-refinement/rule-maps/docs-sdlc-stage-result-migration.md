# DER-529: in-flight stage-result migration

Old: `docs/sdlc/stage-result-migration.md` absent at 7a11696 and 4a342db.
New: `docs/sdlc/stage-result-migration.md`. This is a new procedure
requested after approval of the stage-result contract.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | Preserve the active item, step, evidence, and current invocations | new, requested | Prepare at a safe boundary |
| — | Reload a pinned instruction revision and replace stale prompts | new, requested | Adopt the contract |
| — | Verify harness capability and validate the next actual invocation | route to existing result contract; new migration check | Check the next invocation |
| — | Preserve history, avoid invented results, and record adoption idempotently | new, requested | Preserve history and close the migration |

## Meaning questions

The operator requested a migration step for sessions already in the
SDLC. The procedure is not a new stage and implements neither session
resume nor a driver. Harness unavailability blocks affected dispatch;
legacy outputs are not retroactively represented as new-schema results.
Role permissions, gate rules, and the approved schema remain unchanged.
No open meaning questions.
