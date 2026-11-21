# Rule map — `skills/sdlc/references/branches-and-lands.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/sdlc/references/branches-and-lands.md` at chunk base commit 80bfbd5, lines 1–69. New: `skills/sdlc/references/branches-and-lands.md` (72 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–19 | Unchanged rules in this range | kept | 1–19 |
| 20 | After a land, in-flight builders rebase or merge and resume; the verifier re-runs | changed (R1, R3): each builder re-runs its checks fresh before claiming done | 20 |
| 21–38 | Unchanged rules in this range | kept | 21–38 |
| 39 | De-conflict before a land | changed (R5): use the actual land target | 39 |
| 40–41 | Unchanged rules in this range | kept | 40–41 |
| 42 | De-conflict step 2: resume its verifier | changed (R1, R5): step 2 the builder re-runs its checks on the de-conflicted head; step 3 after the land it runs touched journeys at the land SHA on the land target; routes to `proofs.md` | 42–45 |
| 43–52 | Unchanged rules in this range | kept | 46–55 |
| 53 | Done row: comment cites land SHA, verifier result, reviewer verdict | changed (R5): cites land SHA, the landing builder's journey result at the land SHA on the land target, reviewer verdict | 56 |
| 54–69 | Unchanged rules in this range | kept | 57–72 |

Protected rows touched: `#never` (C8): untouched; every bullet kept.

## Meaning questions

- MQ1 — Resolved: R5: the landing builder verifies affected journeys at the land SHA on either target.
