# Rule map — `maintainers/evals/t1-card.md`

## DER-748 — Current rule map

Old: `maintainers/evals/t1-card.md` at 0abd4db9e5053da6b0e5ad2ef4dfa338561fc985, lines 1–87. New: [maintainers/evals/t1-card.md](../../../evals/t1-card.md).
Item: DER-748. This map records the scoring correction in `1e9b8a2a315594a7e1c948b6f1aa75dd41f9e2e0`.
Authority: [LLD A6](../lld.md#a6--onboarding), as overridden by
[overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6): Tracker Write
waits for the proposal reply; Execution Write runs now and goes in the
onboarding commit at a first tracker touch. See the existing
[onboarding map](skills-sdlc-onboarding.md), rows for old L38–40.

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.
New locations below refer to the current eval card; historical locations below
refer only to the DER-731 result.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–81 | Title, start state, instructions, all replies R1–R7, end point, required agents, scoring heading and table header | kept | L1–81 |
| 82 | C1: tracker proposal before Tracker and Execution writes, repo skill, bootstrap and Epic; no write before R1, R3 carrying R1; no progress on silence | **changed** (DER-748; overlay G7 edit 3; MQ1): only Tracker-area writes wait for R1; proposal shape, R3 handling and silence rule kept. Execution needs no answer, may be written before R1, and is committed in the onboarding commit | L82 |
| 83–87 | C2 manager-only tracker writes; C3 not applicable; C4 reviewer pass and land trailer; C5 distinct author/verifier/reviewer and non-author security read; C6 no over-ask row | kept | L83–87 |

## DER-731 — Historical provenance

This section preserves the original map, not the current C1 gate. DER-748's
map above supersedes its broad pre-reply write restriction.

Old: `maintainers/evals/t1-card.md` at main c26f424, lines 1–85. New: `maintainers/evals/t1-card.md`.
Item: DER-731 (E1 of DER-712). Edits: [LLD E1](../lld.md#e1--eval-text) as overridden by
[overlay G11](../opus-rebuild.md#g11--eval-text-e1).

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–45 | Title, start state, instructions, reply-mode rules | kept | L1–45 |
| 47–48 | Reply table header | changed (R26): `C6` column added | L47–48 |
| 49–53 | Rows R1–R5 | changed (R26, R172): marks R1 `needed`, R2–R5 `over-ask` | L49–53 |
| — | Row R7, touchpoint 1 items other than the tracker proposal, `needed` | changed (R180; overlay G11 item 9): added before R6 | L54 |
| 54 | Row R6, anything else | changed (R26): mark `over-ask` | L55 |
| 56–75 | Reply only when asked; end point; agents the run needs | kept | L57–76 |
| 77 | Scoring heading C1–C5 | changed (R26): C1–C6 | L78 |
| 79–80 | Scoring table header | kept | L80–81 |
| 81 | C1: proposal and Execution question before any write; waits for R1/R2 | changed (A6, R14, R69, R180; overlay G11 item 10): the proposal only; no write before R1's reply, R3 carrying it | L82 |
| 82–85 | C2–C5 | kept | L83–86 |
| — | C6: no `over-ask` row used | changed (R26): added | L87 |

## Meaning questions

DER-731: none recorded.

- **MQ1 (DER-748), resolved:** Does the pre-R1 gate cover Execution?
  No. [Overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6), lines
  637–642, separates the Tracker reply gate from immediate Execution Write
  and retains the first-touch onboarding commit. Early Execution remains
  uncommitted until that commit; this is not permission for a standalone
  early Execution commit or an early Tracker-area write. The unchanged
  review, security, branch and C6 requirements still apply; no new gate is
  added. [LLD A6](../lld.md#a6--onboarding) supplies the retained branch
  and Execution Write rules.
