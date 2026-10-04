# Change map — `skills/lang-go/SKILL.md`

Item: DER-332 (G42). Revised by DER-346 (G53): operator decision Q18,
2026-09-27. Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-go/SKILL.md` at main 7a11696, lines 1–47.
New: [`skills/lang-go/SKILL.md`](../../../../skills/lang-go/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 47 lines old, 42 new.

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
| 17–18 | Load table header | dropped: the table is gone; owner `skills/language-router/SKILL.md#map` (MQ2) | L17 |
| 19 | Default write or review of `*.go` → `golang-safety` | route: owner `skills/language-router/SKILL.md#map`, Go row ("`golang-safety` by default") (MQ2) | L17 |
| 20 | Adding tests → `golang-testing` | route: owner `#map`, Go row ("writing or changing tests") (MQ2) | L17 |
| 20 | Changing tests, tables, race, goleak → `golang-testing` | route: moved into the owner `#map`, Go row ("writing or changing tests or test tables, or when the change touches races or `goleak`"); before, only an agent that read this optional pointer saw it (MQ2) | L17 |
| 21 | Input, auth, SQL, files, subprocesses, crypto → `golang-security` | route: owner `#map`, Go row (same six signals) (MQ2) | L17 |
| 21 | HTTP → `golang-security` | route: moved into the owner `#map`, Go row ("input, auth, HTTP, …"); before, only an agent that read this optional pointer saw it (MQ2) | L17 |
| 23 | "Then stop. Apply that skill." | kept verbatim | L19 |
| 23 | Pair process skills as they already say | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 47 | Never: `golang-safety` + `golang-testing` + `golang-security` in one turn | route: owner `skills/language-router/SKILL.md#iron-law`, in the L9 route line | L9 |

New line with no old line: L17 (route to the Go row). Unchanged old
lines 1–7, 10–12, 14–16 keep their line numbers; old L22 and L24–46 are
new L18 and L20–42.

## Before and after, DER-346

"Before" is project-main 44d6842: the router Go row, plus this file's
addendum only when the agent read this optional pointer. "After" is the
router Go row alone, which every code turn reads.

| Case | Before | After |
| --- | --- | --- |
| Edit an existing table test | `golang-testing` if the agent read `lang-go`; the router row alone named only "writing tests" | `golang-testing` (Go row) |
| Add `goleak.VerifyTestMain` or fix a race | `golang-testing` if the agent read `lang-go`; the router row alone named only "writing tests" | `golang-testing` (Go row) |
| Change an HTTP handler | `golang-security` if the agent read `lang-go`; the router row alone did not name HTTP | `golang-security` (Go row) |
| Plain `*.go` change, no test, no listed signal | `golang-safety` (Go row) | `golang-safety` (Go row) |

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
  Go-only addendum. **Revised by operator 2026-09-27 (Q18):** the
  router's Go row owns every signal; this file keeps only the route at
  L17, and the addendum table is removed. This file is an optional
  pointer, so before DER-346 the signals reached an agent only when it
  read `lang-go`. They now sit in the router row, which every code turn
  reads; the operator chose this. Each signal loads the skill the
  addendum named; see the before-and-after table. Overlapping signals,
  such as HTTP with tests, predate this item: backlog DER-347.
