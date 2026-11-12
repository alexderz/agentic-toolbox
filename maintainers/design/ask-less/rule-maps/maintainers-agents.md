# Rule map — `maintainers/AGENTS.md`

Item: DER-740 (A8 of DER-712). A later item that edits this file appends
its own section.

Old: `maintainers/AGENTS.md` at main c26f424, lines 1–50.
New: [`maintainers/AGENTS.md`](../../../AGENTS.md).
Disposition: **kept** (same rule, same place or A0 path only), **route**
(the rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" is a line at main
c26f424. A0 rewrote paths only; those rows stay **kept**.

Protected rows touched: none. `## Evals` rules 1–5 are unchanged text
(R59): T1–T3 stay the merge rule.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–5 | Entry point for work on this repo; toolbox users stop at the root `AGENTS.md` | kept | L3–5 |
| 7 | Read the root `AGENTS.md` and the SDLC first | kept; path only (A0): `docs/SDLC.md` → `skills/sdlc/SKILL.md` | L7 |
| 8 | This file adds only what is specific to building this repository | kept | L8 |
| 9 | Write agent text to the writing standard | kept; route to `maintainers/writing-standard.md#standard` | L9 |
| 11–12 | Tracker skill path in `## Tracker` is relative to this directory | kept | L11–12 |
| 14, 16 | `## Tracker`: Linear, tracker-sdlc v2 | kept | L14, L16 |
| 18, 20 | `## Execution`: `Parallelism: max` | kept | L18, L20 |
| 22 | `## Evals` heading | kept | L22 |
| 24–25 | Agent text paths that an eval run covers | replaced (A8): `AGENTS.md`, `skills/` (the SDLC is `skills/sdlc/`). A0 had rewritten the docs paths into skill paths; those paths sit inside `skills/` | L24 |
| 27–30 | Evals rule 1: a PR into `main` that changes agent text gets T1–T3 before merge | kept (R59) | L26–29 |
| 31–32 | Evals rule 2: one run file per model; regressions first | kept (R59) | L30–31 |
| 33–34 | Evals rule 3: the operator decides merge, fix, or rerun | kept (R59) | L32–33 |
| 35 | Evals rule 4: after the merge, that run becomes the baseline row | kept (R59) | L34 |
| 36–37 | Evals rule 5: a new daily-driver model runs T1–T3 on `main` first | kept (R59) | L35–36 |
| 39 | Where notes go | kept | L38 |
| 41–43 | Design records live in `maintainers/design/<chunk>/` | kept | L40–42 |
| 44 | Planning notes live in `maintainers/` | kept | L43 |
| 45–47 | Notes here are agent context under the root public-repo rule | kept; route to root `AGENTS.md#public-repo` | L44–46 |
| 48–50 | Skills, human-facing docs, and packages never link into `maintainers/` | kept | L47–49 |

## Meaning questions

None. The only wording change is the `## Evals` agent-text line, and
that line is the accepted LLD's exact text. Rules 1–5 are byte-identical
to c26f424.
