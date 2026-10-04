# Change map — `skills/lang-cpp/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-cpp/SKILL.md` at main 7a11696, lines 1–101.
New: [`skills/lang-cpp/SKILL.md`](../../../../skills/lang-cpp/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 101 lines old, 101 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8 | "RAII and ownership, not a Core Guidelines dump." | kept verbatim | L8 |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |
| 94 | Never treat C++ as "C with classes" | kept verbatim | L94 |
| 94 | Parenthesis "(load `lang-c` for `.c` files)" | route: owner `skills/language-router/SKILL.md#map` (the `*.c` row and Family rules), in the L9 route line (MQ2) | L9 |

Unchanged old lines 1–7, 10–93 and 95–101 keep their line numbers.

## Meaning questions

- **MQ1** — The old line names four process skills; the owner list names
  nine (a superset). Resolved from the text: "Compatible with" excluded
  no skill, and `language-router` loads on every code turn
  (its description), so the owner list already governs every turn that
  loads this skill. The route adds no condition.
- **MQ2** — Old L94's parenthesis says to load `lang-c` for `.c` files;
  the owner's Family rules say that if any `.cpp` or `.hpp` file is in
  the change, load `lang-cpp` and never `lang-c` beside it. Resolved from
  the text: the parenthesis is a partial copy of the owner's map rule,
  and the owner governs; the "C with classes" ban itself is kept
  verbatim. Standard 8 also bars a condition in a parenthesis.
- **MQ3** — The front-matter description repeats a map fact ("load
  lang-c" for C-only changes). Resolved from the text: the description is
  the load trigger the skill loader reads, not a body line; G42 routes
  body lines only. Kept verbatim.
