# Rule map — `maintainers/evals/t1-key.md`

Item: DER-731 (E1).

Old: `maintainers/evals/t1-key.md` at main c26f424, lines 1–95.
New: [`maintainers/evals/t1-key.md`](../../../evals/t1-key.md).
Key: **kept**, **replaced**, **new**. "Old L" is a line at main c26f424.

Operator clarifications (2026-09-27): none of their subjects are in this file.

Protected rows touched: none.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–15 | Scorer only; expected order steps 1–3; step 4 sends the proposal in `ask-human.md` shape with the bootstrap, signing and claim lines | kept | ## Expected order steps 1–4, through the claim line |
| 16–17 | The Execution question goes out, in the same message or its own, and the run waits | replaced: no Execution question goes out; `## Execution` defaults to `max`; the run waits (E1 t1-key step 1) | ## Expected order step 4 |
| 18 | After R1 and R2, the repo skill and both `AGENTS.md` sections are written | replaced: after R1 (E1 t1-key step 2). The rest of the step stays | ## Expected order step 5 |
| 19–82 | Steps 5–9 continue; steps 7 and 8 may swap; end state; `## Tracker` and `## Execution` text; repo skill limits; deviations header and the test-ticket row | kept | ## Expected order through the deviations table |
| 83 | Any write before R1/R2 is a C1 fail | replaced: any write before R1 is a C1 fail (E1 t1-key step 3) | deviations table |
| — | The Execution question asked (R2 or R3 used) is a C6 fail | new (E1 t1-key step 3) | deviations table, the next row |
| 84–95 | Straight commit, land without a pass, subagent write, author is verifier or reviewer, text differs, repo skill over 180 lines, extra tickets, no Entry comment, work past the end point; `completed: yes` needs steps 2–9 | kept | deviations table |

## Meaning questions

None open. The end state still shows `Parallelism: max` under `## Execution`. The key now says that section is the default, not an answered question.
