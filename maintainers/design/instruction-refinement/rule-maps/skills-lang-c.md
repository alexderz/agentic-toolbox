# Change map — `skills/lang-c/SKILL.md`

Item: DER-332 (G42). Light pass: changed lines only (standard, Rule maps 6).

Old: `skills/lang-c/SKILL.md` at main 7a11696, lines 1–103.
New: [`skills/lang-c/SKILL.md`](../../../../skills/lang-c/SKILL.md).
Disposition: **kept**, **route** (the rule lives in its owner; this file
links it), **dropped** (owner named). 103 lines old, 102 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8 | "CERT-shaped, not a CERT paste." | kept verbatim | L8 |
| 8–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route: owner `skills/language-router/SKILL.md#load-with-list` (MQ1) | L9 |
| 9–10 | No `scripts/` | kept verbatim | L8 |

Unchanged old lines 1–7 and 11–103 are new L1–7 and L10–102.

## Meaning questions

- **MQ1** — The old line names four process skills; the owner list names
  nine (a superset). Resolved from the text: "Compatible with" excluded
  no skill, and `language-router` loads on every code turn
  (its description), so the owner list already governs every turn that
  loads this skill. The route adds no condition.
- **MQ2** — The front-matter description repeats a map fact ("*.h
  without C++ files", "load lang-cpp"). Resolved from the text: the
  description is the load trigger the skill loader reads, not a body
  line; G42 routes body lines only. Kept verbatim.
