# Rule map — `skills/sdlc/references/build-review.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/sdlc/references/build-review.md` at chunk base commit 80bfbd5, lines 1–126. New: `skills/sdlc/references/build-review.md` (143 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Unchanged rules in this range | kept | 1–4 |
| after 4 | (new) Build intro: the layering, linked to the write-up | changed (R7): one line plus link to `docs/agents-write-and-check-proofs.md`; the doc is not restated | 5–8 |
| 5–47 | Unchanged rules in this range | kept | 9–51 |
| 48–49 | DoD: "tests or verification evidence" | changed (R2): "the builder's proof bundle", routed to `proofs.md#proof-bundle` | 52–53 |
| 50–53 | Unchanged rules in this range | kept | 54–57 |
| 54–57 | The verifier checks deliverable tone against the style guide; not agent context | route: moved whole to Review step 6 (R4), owner the reviewer, citing the style-guide rule | — (after new 57) |
| 58 | Unchanged rules in this range | kept | 58 |
| 59–60 | Builder and verifier: one each per item | changed (R1, R3): one builder per item; it runs and re-runs every check; route to `proofs.md#builder-checks` | 59–62 |
| 61–106 | Unchanged rules in this range | kept | 63–108 |
| 107–108 | Review step 3: take the diff range; old step 4 heading (GR16) | changed (R2, R4): step 3 adds the manager passing the bundle privately to the authorized reviewer, never the transcript; new step 4 reads the bundle first, never re-runs, five fail conditions, then the diff; GR16 renumbered to step 5, text kept | 109–122 |
| 109–120 | Unchanged rules in this range | kept | 123–134 |
| 121 | Review step 5: approve only if step 4 failed nothing, plus yagni and security | changed (R4): new step 6 tone (moved from L54–56); step 7 approve only if steps 4–6 failed nothing; `yagni`, smell baseline and **security** text kept | 135–138 |
| 122–126 | Unchanged rules in this range | kept | 139–143 |

Protected rows touched: none

## Meaning questions

- MQ1 — Resolved: R4: evidence review is part of the existing Review gate.
- MQ2 — Resolved: R4: the reviewer checks deliverable tone against the same style standard.
- MQ3 — Resolved: R4: GR16 is renumbered, not weakened.
