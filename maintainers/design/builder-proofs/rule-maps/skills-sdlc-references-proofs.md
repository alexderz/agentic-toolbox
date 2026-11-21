# Rule map — `skills/sdlc/references/proofs.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: none (new file at chunk base commit 80bfbd5). New: `skills/sdlc/references/proofs.md`, lines 1–112 (cap 150).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | Names: check, raw output, proof bundle (a result, not a transcript), journey, midpoint, span test (start-to-mid, mid-to-end) | changed (new; R2, R6) | `## Names` |
| — | Builder checks: condition → check table, span tests, seen failing, raw outputs to the manager's scratch folder, fresh re-run per `verify-before-done`, bundle in the result; never weaken a check | changed (new; R1, R2) | `## Builder checks` |
| — | Sharing evidence: full bundle only for authorized review; public surfaces receive safe results and shareable references | changed (R2) | `## Sharing evidence` |
| — | Proof bundle: private review evidence in seven fields, `n/a` and why for an empty field | changed (new; R2, direct evidence) | `## Proof bundle` |
| — | Journeys: Spec and Groom identify coverage; builder adds missing end-to-end tests for touched behavior even if omitted | changed (new; R6) | `## Journeys` |
| — | After integration: post-land journey run by the landing builder; failure path; pre-Trunk full journey set by the last item’s builder, not a different item; public-safe summary at Trunk | changed (new; R5) | `## After integration` |

Protected rows touched: none

## Meaning questions

- MQ1 — Resolved: R6: missing coverage of changed behavior requires a test even if the ticket omitted it. No changed behavior needs no journey test.
- MQ2 — Resolved: R5: a post-land failure uses the existing fix and Review path.
