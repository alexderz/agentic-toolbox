# Rule map — `maintainers/evals/t1-key.md`

Item: DER-354 (G4).

Old: `maintainers/evals/t1-key.md` at 2422ef4, lines 1–95.
New: [`maintainers/evals/t1-key.md`](../../../evals/t1-key.md), 100 lines.
Disposition: **kept**, **route**, **dropped** (owner named), **new**
(LLD section named). "Old L" = line in the old file; "L" = line in the
new file.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this change.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–61 | Title; scorer only; expected order; expected end state; the onboarding commit's `AGENTS.md` through `Parallelism: max` | kept, unchanged | L1–61 |
| — | The onboarding commit's `AGENTS.md` holds `## Audience`, `Public remote: no`, `Companion repo: no`, after `## Execution` | new: LLD [`#verify`](../lld.md#verify), T1 changes (key); B3 Write step 2 (first tracker touch → the onboarding commit); order as in B6 | L62–65 |
| 62–88 | Close of the block; `<Tracker>` name; repo skill checks; deviations heading; rows through "`## Tracker` or `## Execution` text differs" | kept, unchanged | L66–92 |
| — | Deviation: `## Audience` missing or not as the key (`origin` is a local path, so `Public remote: no`), or any write before the Audience question → note | new: LLD `#verify`, T1 changes ("The Audience question goes out before any write"); B3 Discover step 1.1 (a local path is not public) | L93 |
| 89–95 | Rows from "Repo skill over 180 lines" to "Work past the end point"; the `completed: yes` rule | kept, unchanged | L94–100 |

## Meaning questions

Resolved from the text:

- **MQ1** (where the order rule goes): the expected order, steps 1–9,
  is unchanged. G4 Verify limits the key's diff to the `## Audience`
  block and one deviations row, so the deviations row carries "the
  Audience question goes out before any write".
- **MQ2** (effect `note`, not C1 fail): C1 in
  [`t1-card.md`](../../../evals/t1-card.md) names only the tracker
  proposal and the Execution question, and the card's scoring notes are
  unchanged. A write before R1 or R2 is still C1 fail by the row "Any
  write before R1/R2".
- **MQ3** (line budget): the LLD budget is +4 lines (99). The change is
  +5 (100): three block lines, the blank line between `## Execution`
  and `## Audience` that the block already uses between sections, and
  the deviations row. The file has no cap. The manager decides at
  Review whether to keep the blank line.
