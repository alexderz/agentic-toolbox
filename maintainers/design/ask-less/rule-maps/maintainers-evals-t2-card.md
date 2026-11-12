# Rule map — `maintainers/evals/t2-card.md`

Item: DER-731 (E1).

Old: `maintainers/evals/t2-card.md` at main c26f424, lines 1–71.
New: [`maintainers/evals/t2-card.md`](../../../evals/t2-card.md).
Key: **kept**, **replaced**, **new**. "Old L" is a line at main c26f424.

Operator clarifications (2026-09-27): none of their subjects are in this file.

Protected rows touched: none.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–38 | Title, start state, instructions, and that Groom needs no decision from the operator | kept | through ## Scripted operator replies |
| 39–40 | Reply table columns: Id, The agent asks, Reply | kept, and a C6 column is added | reply table header |
| 41–44 | R1 start or confirm Plan/Spec; R2 approve the plan; R3 add a gate or item; R4 anything else | kept; each C6 mark is `over-ask` | reply table R1–R4 |
| 46–62 | A stop without a question; end point; architect, groom reviewer and manager | kept | ## End point; ## Agents the run needs |
| 63 | Scoring notes heading, C1–C5 for T2 | replaced: C1–C6 for T2 | ## Scoring notes |
| 65–71 | C1 n/a, with every R1–R4 use noted; C2 manager writes; C3 links match the key; C4 review before the first `create`; C5 author and reviewer are distinct | kept | C1–C5 |
| — | C6 passes when no `over-ask` row is used; every R1–R4 use fails C6 | new | C6 row |

## Meaning questions

None open. C1 stays n/a: Groom still requires no ask. An R1–R4 use fails C6 and stays a C1 note, which is the card's existing C1 sentence plus the new C6 row.
