# Change map — `skills/lang-docker/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-docker/SKILL.md` at main 7a11696, lines 1–86.
New: [`skills/lang-docker/SKILL.md`](../../../../skills/lang-docker/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 86 lines old, 85 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |
| 9–10 | Real `.sh` files still load `shell-safety` | route: owner `skills/language-router/SKILL.md#map` (the `*.sh` row) and `#load-with-list` item 2, in the L9 route line (MQ2) | L9 |

Unchanged old lines 1–7 and 11–86 are new L1–7 and L10–85.

## Meaning questions

- **MQ1** — The old line names four process skills; the owner list names
  nine (a superset). Resolved from the text: "Compatible with" excluded
  no skill, and `language-router` loads on every code turn
  (its description), so the owner list already governs every turn that
  loads this skill. The route adds no condition.
- **MQ2** — Old L9–10 states the `*.sh` → `shell-safety` map row.
  Resolved from the text: the owner's map row and load-with item 2 say
  the same; the route names the rule ("the skill for `.sh` files"). The
  front-matter description keeps its own `shell-safety` sentence
  verbatim (it is the load trigger, not a body line).
