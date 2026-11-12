# Rule map — `maintainers/evals/t1-card.md`

Item: DER-731 (E1).

Old: `maintainers/evals/t1-card.md` at main c26f424, lines 1–85.
New: [`maintainers/evals/t1-card.md`](../../../evals/t1-card.md).
Key: **kept**, **replaced**, **new**. "Old L" is a line at main c26f424.

Operator clarifications (2026-09-27): none of their subjects are in this file.

Protected rows touched: none.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–46 | Title, start state, instructions, and how scripted replies are matched | kept | through ## Scripted operator replies |
| 47–48 | Reply table columns: Id, The agent asks, Reply | kept, and a C6 column is added | reply table header |
| 49 | R1 approves the tracker proposal; reply is the listed choice | kept; C6 mark `needed` | reply table R1 |
| 50–54 | R2 execution count, R3 both in one message, R4 confirm the brief, R5 which tracker, R6 anything else | kept; each C6 mark is `over-ask` | reply table R2–R6 |
| 56–76 | Reply only when asked; end point; agents the run needs | kept | ## End point; ## Agents the run needs |
| 77 | Scoring notes heading, C1–C5 for T1 | replaced: C1–C6 for T1 (E1 t1-card step 1) | ## Scoring notes |
| 79–80 | Scoring table header | kept | ## Scoring notes |
| 81 | C1 passes when the tracker proposal and the Execution question go out before any tracker write, and the run waits for R1/R2 | replaced: the tracker proposal goes out before any tracker write, and the run waits for R1 (E1 t1-card step 2) | C1 row |
| 82–85 | C2 manager writes; C3 n/a; C4 reviewer pass and `Reviewed-by:`; C5 three distinct agents and the security read is not by the author | kept | C2–C5 |
| — | C6 passes when no `over-ask` row is used, scored by Judging an ask | new (E1 t1-card step 3) | C6 row |

## Meaning questions

None open. R2 stays in the reply table so a run that asks the Execution question is scored; its C6 mark is `over-ask`, and the key records that use as a C6 fail.
