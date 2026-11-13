# Rule map — `maintainers/evals/t1-key.md`

## DER-748 — Current rule map

Old: `maintainers/evals/t1-key.md` at 0abd4db9e5053da6b0e5ad2ef4dfa338561fc985, lines 1–96. New: [maintainers/evals/t1-key.md](../../../evals/t1-key.md).
Item: DER-748. This map records the scoring correction in `1e9b8a2a315594a7e1c948b6f1aa75dd41f9e2e0`.
Authority: [LLD A6](../lld.md#a6--onboarding), as overridden by
[overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6): Tracker Write
waits for the proposal reply; Execution Write runs now and goes in the
onboarding commit at a first tracker touch. See the existing
[onboarding map](skills-sdlc-onboarding.md), rows for old L38–40.

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.
New locations below refer to the current eval key; historical locations below
refer only to the DER-731 result.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–17 | Title, scorer-only notice, expected steps 1–4, tracker proposal and wait; no Execution question, default `max` | kept | L1–17 |
| 18–20 | Step 5: repo skill and both AGENTS sections written after R1, not yet committed; manager bootstraps tickets and creates Epic | **changed** (DER-748; overlay G7 edit 3; MQ1): repo skill and Tracker still wait for R1; Execution may already be written before R1, explicitly uncommitted; manager bootstrap and Epic creation kept | L18–21 |
| 21–23 | Step 6: one onboarding commit on an item branch from project-main, holding AGENTS and the repo skill | kept | L22–24 |
| 24–53 | Verification, security read, review, land, Entry comment, stop before Plan; interleaving; origin, Epic and comment end state | kept | L25–54 |
| 54–65 | Onboarding commit's AGENTS contains both Tracker and Execution with `Parallelism: max`; rest of stub unchanged | kept | L55–66 |
| 66–82 | Repo skill end state; deviations heading and header; test-ticket deviation | kept | L67–83 |
| 83 | Any write before R1 fails C1 | **changed** (DER-748; overlay G7 edit 3; MQ1): only Tracker-area writes (`## Tracker`, repo skill, tickets, Epic) before R1 fail C1 | L84 |
| 84–96 | Execution question fails C6; item branch, reviewer pass, manager-only writes and distinct-agent checks; remaining deviations and completion rule | kept | L85–97 |

## DER-731 — Historical provenance

This section preserves the original map, not the current write order or
line numbers. DER-748's map above supersedes its after-R1 Execution order
and broad "Any write" deviation.

Old: `maintainers/evals/t1-key.md` at main c26f424, lines 1–95. New: `maintainers/evals/t1-key.md`.
Item: DER-731 (E1 of DER-712). Edits: [LLD E1](../lld.md#e1--eval-text) as overridden by
[overlay G11](../opus-rebuild.md#g11--eval-text-e1).

Key: **kept**; **route**; **dropped** with the owner named; **changed** with its deciding id.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–15 | Title; expected order steps 1–4 up to the claim line | kept | L1–15 |
| 16–17 | The Execution question goes out | changed (A6, R14, R69): no Execution question; `## Execution` defaults to `max` | L16–17 |
| 18 | After R1 and R2: writes | changed (R14, R69): after R1 | L18 |
| 19–82 | Steps 5–9, end state, Deviations table head and the test-ticket row | kept | L19–82 |
| 83 | Any write before R1/R2 → C1 fail | changed (R14, R69): before R1; row "The Execution question asked (R2 or R3 used) → C6 fail" added (R26) | L83–84 |
| 84–95 | Other deviations; Completed rule | kept | L85–96 |

## Meaning questions

DER-731: none recorded.

- **MQ1 (DER-748), resolved:** Does step 5 require Execution to wait for
  R1, and does any early write fail C1? No.
  [Overlay G7 edit 3](../opus-rebuild.md#g7--onboarding-a6), lines 637–642,
  separates the Tracker reply gate from immediate Execution Write and
  retains the first-touch onboarding commit. Step 5 now permits early
  uncommitted Execution; step 6 and the end state still require it in the
  onboarding commit, not a standalone early commit. Tracker writes still
  wait for R1; the item branch, Review, security and C6 requirements are
  unchanged. [LLD A6](../lld.md#a6--onboarding) supplies the retained
  branch and Execution Write rules. No new gate is added.
