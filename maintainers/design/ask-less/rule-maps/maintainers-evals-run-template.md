# Rule map — `maintainers/evals/run-template.md`

Item: DER-731 (E1).

Old: `maintainers/evals/run-template.md` at main c26f424, lines 1–74.
New: [`maintainers/evals/run-template.md`](../../../evals/run-template.md).
Key: **kept**, **replaced**, **new**, as in the procedure map. "Old L"
is a line in the file at main c26f424.

Operator clarifications (2026-09-27): none of their subjects are in this file.

Protected rows touched: none.

The link to `t4-key.md#counts` resolves when E2 lands. Scheduled.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Title; copy once per model and commit; keep the sections from ## Run down | kept | intro |
| 5 | One file holds every repeat of T1–T3 | replaced: T1–T4 (E1 step 1) | intro |
| 6–11 | The file is public; what it must not contain; never quote model output | kept | intro |
| 13–24 | Run header fields | kept | ## Run |
| 26–30 | Regressions: one line per regression, or `none`, in the `<task> <item>` shape | kept | ## Regressions |
| — | T4 needed asks kept: `<n>` to `<m>` | new (E1 step 4) | ## Regressions |
| 32 | Results | kept | ## Results |
| 34 | C1–C5 and Completed as passes out of 3; a repeat scored `n/a` | replaced: C1–C6 (E1 step 2). The rest of the sentence stays | ## Results |
| 35–38 | A repeat scored `n/a` because the run ended early is a non-pass; `n/a` only where the card says so; C5 is never `n/a`; tokens and wall time are never a pass bar | kept | ## Results |
| 40–44 | Results table for T1–T3, columns through C5 | replaced: T1–T4 with a C6 column (E1 step 3) | ## Results |
| — | T4 counts table: unneeded asks, needed asks kept out of 4, guardrails added, guardrails disclosed, per repeat; rules in the T4 key | new (E1 step 3). The key link resolves when E2 lands | ## T4 counts |
| 46–47 | Evidence heading | kept | ## Evidence |
| 48 | One block per repeat, in order T1 r1 through T3 r3 | replaced: through T4 r3 (E1 step 5) | ## Evidence |
| 49–59 | Where a C line points; the T1 r1 block through C5 | kept | ## Evidence |
| — | C6: over-ask row ids used, or `none` | new (E1 step 5) | ## Evidence, after the C5 line |
| 60–74 | Replies used, deviations, tokens, and how each C item is scored | kept | ## Evidence; ## How each C item is scored |
| — | C6 is scored by Judging an ask | new (E1 step 6) | ## How each C item is scored |

## Meaning questions

None open.
