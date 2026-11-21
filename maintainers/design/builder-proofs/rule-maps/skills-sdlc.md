# Rule map — `skills/sdlc/SKILL.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/sdlc/SKILL.md` at chunk base commit 80bfbd5, lines 1–247. New: `skills/sdlc/SKILL.md` (248 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–32 | Unchanged rules in this range | kept | 1–32 |
| 33–34 | Step jobs list names the verifier | changed (R3): "verifier" dropped from the list | 33–34 |
| 35–40 | Unchanged rules in this range | kept | 35–40 |
| 41–42 | Roles table: builder "Implement and ship"; tester "…, verification evidence" | changed (R1, R2, R3): builder "Implement, run every check for its item, and ship with a proof bundle"; tester "Mechanical CI, hooks, cleanup" | 41–42 |
| 43–85 | Unchanged rules in this range | kept | 43–85 |
| 86–87 | Tracker step 3: builders, verifiers and reviewers never write | changed (R3): "verifiers" dropped; rule otherwise kept | 86–87 |
| 88–242 | Unchanged rules in this range | kept | 88–242 |
| after 242 | (new) Steps table row: Proofs | changed (R2, standard 6): entry link for the new owner file | 243 |
| 243–247 | Unchanged rules in this range | kept | 244–248 |

Protected rows touched: `#roles`, `#tracker` (C2): rows L33, L41, L86 changed under R1/R3 (MQ1, MQ2); every other line kept.

## Meaning questions

- MQ1 — Resolved: R1/R3: builders own item checks; testers own CI and hooks. No new role.
- MQ2 — Resolved: R3: only the manager writes to the tracker.
- MQ3 — Resolved: R5: the post-land check runs on the actual land SHA.
