Old: skills/lang-makefile/SKILL.md at main 7a11696, lines 1–71. New: skills/lang-makefile/SKILL.md.

Light pass (`lang-*`, DER-333): change map, changed lines only. Not
vendor-derived (`SOURCES.md` Upstream: first-party); no `SOURCES.md`
change. Frontmatter `description` unchanged.

Key: **kept**, **route**, **dropped** (owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | **dropped** (owner `skills/language-router/SKILL.md#load-with-list`); **route**, one line, "may" kept (see MQ2) | L9 |
| 9–10 | "No `scripts/`." and "The language being built still loads its own skill." | **kept**, wording unchanged (see MQ1) | L8 |

Lines 71 → 70. Banned names: none in old or new.

## Meaning questions

- **MQ1** — Old L9–10 "The language being built still loads its own
  skill." Two readings: (a) when the turn also edits the built code, that
  code's language skill loads too; (b) the built language's skill always
  loads beside `lang-makefile`. Reading (b) could clash with the
  `language-router` Iron law (at most one language skill; a second only
  for a mixed-language diff). Resolved from the text (2026-09-27): kept
  word for word, not routed. It is Make-specific guidance, the router
  has no Make rule to route to, and the description ("do not use instead
  of the language skill for the code the Makefile builds") supports
  reading (a), which fits the router's mixed-language exception.
  Reopen for the operator if the manager reads it as (b).
- **MQ2** — The old line listed 4 skills that may load with this one;
  the owner `skills/language-router/SKILL.md#load-with-list` lists 9.
  Resolved from the text (2026-09-27): the route defers to the owner, and
  "may" keeps the old optionality. It adds no load and no requirement.
