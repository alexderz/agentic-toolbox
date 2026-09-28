# Rule map — `maintainers/evals/t1-card.md`

Item: DER-354 (G4).

Old: `maintainers/evals/t1-card.md` at 2422ef4, lines 1–85.
New: [`maintainers/evals/t1-card.md`](../../../evals/t1-card.md), 86 lines.
Disposition: **kept**, **route**, **dropped** (owner named), **new**
(LLD section named). "Old L" = line in the old file; "L" = line in the
new file.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this change.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–53 | Title; what T1 tests; start state; instructions to the agent; reply modes; replies R1–R5 | kept, unchanged | L1–53 |
| — | R7: the Audience question → `1 — no companion.` Asked in one message with R1 or R2 → this reply goes last, on its own line | new: LLD [`#verify`](../lld.md#verify), T1 changes (card: R7) | L54 |
| 54–85 | R6 "Anything else"; reply only when asked; the `Continue.` rule; end point; agents the run needs; scoring notes C1–C5 | kept, unchanged | L55–86 |

## Meaning questions

Resolved from the text:

- **MQ1** (row order): R7 sits above R6, not below it. The card answers
  with "the first matching row" (L41), and R6 matches anything, so R7
  below R6 would never be used. The id stays `R7`, as the LLD names it.
- **MQ2** (the Audience question shares a message): `sdlc-onboarding`
  Audience Propose step 1 (LLD B3) lets it share the tracker proposal
  message. R7 says where its reply goes then, in the shape of R3. R3 is
  unchanged.
- **MQ3** (C1): the scoring notes are unchanged. C1 still names only
  the tracker proposal and the Execution question. The order of the
  Audience question is scored as a deviation in
  [`t1-key.md`](../../../evals/t1-key.md) (G4 Verify: the card and key
  diff touches only R7, the `## Audience` block and one deviations row).
