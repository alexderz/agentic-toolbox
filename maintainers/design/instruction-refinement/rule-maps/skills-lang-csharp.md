# Change map — `skills/lang-csharp/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-csharp/SKILL.md` at main 7a11696, lines 1–95.
New: [`skills/lang-csharp/SKILL.md`](../../../../skills/lang-csharp/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 95 lines old, 95 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8 | "Language guide." | kept verbatim | L8 |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |

Unchanged old lines 1–7 and 10–95 keep their line numbers.

## Meaning questions

- **MQ1** — The old line names four process skills; the owner list names
  nine (a superset). Resolved from the text: "Compatible with" excluded
  no skill, and `language-router` loads on every code turn
  (its description), so the owner list already governs every turn that
  loads this skill. The route adds no condition.
