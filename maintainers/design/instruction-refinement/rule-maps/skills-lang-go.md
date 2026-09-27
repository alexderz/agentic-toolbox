# Change map — `skills/lang-go/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-go/SKILL.md` at main 7a11696, lines 1–47.
New: [`skills/lang-go/SKILL.md`](../../../../skills/lang-go/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 47 lines old, 47 new.

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
| 17–18 | Load table header | kept verbatim, as the addendum table header | L19–20 |
| 19 | Default write or review of `*.go` → `golang-safety` | route: owner `skills/language-router/SKILL.md#map`, Go row ("`golang-safety` by default") (MQ2) | L17 |
| 20 | Adding tests → `golang-testing` | route: owner `#map`, Go row ("when writing tests") (MQ2) | L17 |
| 20 | Changing tests, tables, race, goleak → `golang-testing` | kept, as a Go-only addendum row; wording kept (MQ2) | L21 |
| 21 | Input, auth, SQL, files, subprocesses, crypto → `golang-security` | route: owner `#map`, Go row (same six signals) (MQ2) | L17 |
| 21 | HTTP → `golang-security` | kept, as a Go-only addendum row (MQ2) | L22 |
| 23 | "Then stop. Apply that skill." | kept verbatim | L24 |
| 23 | Pair process skills as they already say | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 47 | Never: `golang-safety` + `golang-testing` + `golang-security` in one turn | route: owner `skills/language-router/SKILL.md#iron-law`, in the L9 route line | L9 |

New line with no old line: L17 (route to the Go row and addendum lead-in).
Unchanged old lines 1–7, 10–12, 14–16 keep their line numbers; old L22
and L24–46 are new L23 and L25–47.

## Meaning questions

- **MQ1** — The old lines name four process skills, or defer to what
  each process skill says; the owner list names nine (a superset).
  Resolved from the text: neither old line excluded a skill, and
  `language-router` loads on every code turn (its description), so the
  owner list already governs every turn that loads this skill. The route
  adds no condition.
- **MQ2** — Old L17–21, the Load table, repeats the owner's Go row
  (`skills/language-router/SKILL.md#map`) and adds signals: `HTTP` →
  `golang-security`; changing tests, tables, race, goleak →
  `golang-testing`. Resolved by the operator 2026-09-27 (Q14): route +
  Go-only addendum. The repeated Go row routes to `#map` (L17); the
  extra signals stay as addendum rows (L21–22) with their old meaning.
