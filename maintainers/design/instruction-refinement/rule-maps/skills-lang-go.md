# Change map — `skills/lang-go/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-go/SKILL.md` at main 7a11696, lines 1–47.
New: [`skills/lang-go/SKILL.md`](../../../../skills/lang-go/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 47 lines old, 46 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8 | "**This id routes.** Do not remint Go advice." | kept verbatim | L8 |
| 8 | Load **one** existing Go skill | route: owner `skills/language-router/SKILL.md#iron-law` (at most one language skill; the Go row says "One of") | L9 |
| 9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |
| 13 | Iron law: pick one Go skill; never load all three | route: owner `skills/language-router/SKILL.md#iron-law`, in the L9 route line | L9 |
| 13 | Iron law: never write a parallel Go guide | kept verbatim, first (standard 7) | L13 |
| 23 | "Then stop. Apply that skill." | kept verbatim | L23 |
| 23 | Pair process skills as they already say | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 47 | Never: `golang-safety` + `golang-testing` + `golang-security` in one turn | route: owner `skills/language-router/SKILL.md#iron-law`, in the L9 route line | L9 |

Unchanged old lines 1–7, 10–12, 14–22 and 24–46 keep their line numbers.
Old L17–21 (the Load table) is kept verbatim pending MQ2.

## Meaning questions

- **MQ1** — The old lines name four process skills, or defer to what
  each process skill says; the owner list names nine (a superset).
  Resolved from the text: neither old line excluded a skill, and
  `language-router` loads on every code turn (its description), so the
  owner list already governs every turn that loads this skill. The route
  adds no condition.
- **MQ2** — **Open.** Old L17–21, the Load table, repeats the owner's Go
  row (`skills/language-router/SKILL.md#map`) with extra signals: `HTTP`
  → `golang-security`; "tables, race, goleak" → `golang-testing`. Two
  readings: (a) a duplicate of the Go row (HTTP is input; race and
  goleak are tests), so the table becomes a route to `#map`; (b) Go
  pointer content the owner allows ("it routes to the language skill in
  its row", router L80–81), so it stays. Kept verbatim; the route line
  does not link `#map`. Operator to pick (a) or (b); under (a) the table
  and "Then stop. Apply that skill." become one link to `#map`, and the
  route line adds it.
