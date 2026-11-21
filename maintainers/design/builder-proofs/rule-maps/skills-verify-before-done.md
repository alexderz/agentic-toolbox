# Change map (light pass) — `skills/verify-before-done/SKILL.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/verify-before-done/SKILL.md` at chunk base commit 80bfbd5, lines 1–77. New: `skills/verify-before-done/SKILL.md` (78 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–12 | Unchanged rules in this range | kept | 1–12 |
| 13–14 | Proving command always re-run; verifier mint, resume, never the builder | changed (R1): re-run by the builder; this is the builder's gate; route to `proofs.md#builder-checks` | 13–15 |
| 15–38 | Unchanged rules in this range | kept | 16–39 |
| 39 | Never: trusting agent success without VCS/diff or independent run | changed (R1, R2): "without VCS/diff or direct evidence (raw output, workspace path, CI link)" | 40 |
| 40–61 | Unchanged rules in this range | kept | 41–62 |
| 62 | Roles: tester owns CI evidence and the verifier subagent | changed (R3): tester owns CI that produces evidence | 63 |
| 63–77 | Unchanged rules in this range | kept | 64–78 |

Protected rows touched: none

## Meaning questions

- None open. The Iron law, Gate and Claim → evidence table are unchanged; the Never row requires direct evidence (R2).
