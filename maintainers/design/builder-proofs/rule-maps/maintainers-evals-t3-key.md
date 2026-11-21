# Rule map — `maintainers/evals/t3-key.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `maintainers/evals/t3-key.md` at chunk base commit 80bfbd5, lines 1–148. New: `maintainers/evals/t3-key.md` (151 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–31 | Unchanged rules in this range | kept | 1–31 |
| 32–33 | Expected step 4: mint verifier; it runs proving commands; loop | changed (R1, R2): the builder runs them fresh and returns a bundle; loops to DoD | 32–33 |
| 34 | Unchanged rules in this range | kept | 34 |
| 35–36 | Expected step 5: reviewer reviews the diff | changed (R4): reviewer gets the bundle, reads it, then the diff | 35–36 |
| 37–39 | Unchanged rules in this range | kept | 37–39 |
| 40 | Expected step 7: verifier re-runs on project-main | changed (R5): landing builder exercises touched behavior at the land SHA; fixture silence does not excuse missing tests | 40–42 |
| 41 | Unchanged rules in this range | kept | 43 |
| 42 | Expected step 8: comment cites verifier result | changed (R5): cites the public-safe result at the land SHA | 44–45 |
| 43–83 | Unchanged rules in this range | kept | 46–86 |
| 84 | C5: three agent labels | changed (R3): two agent labels | 87 |
| 85–101 | Unchanged rules in this range | kept | 88–104 |
| 102–103 | Completed: comment cites verifier result | changed (R5): journey result | 105–106 |
| 104–139 | Unchanged rules in this range | kept | 107–142 |
| 140 | Deviation: verifier or reviewer is the builder → C5 fail | changed (R3): reviewer is the builder | 143 |
| 141–143 | Unchanged rules in this range | kept | 144–146 |
| 144–145 | Deviations: done before verifier re-run; comment missing verifier result | changed (R5): journey result | 147–148 |
| 146–148 | Unchanged rules in this range | kept | 149–151 |

Protected rows touched: none

## Meaning questions

- None open. The scorer's own clean-clone test run in Completed is the scorer's check, not an SDLC role; kept.
