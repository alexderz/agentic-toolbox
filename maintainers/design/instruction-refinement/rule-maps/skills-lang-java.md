Old: skills/lang-java/SKILL.md at main 7a11696, lines 1–98. New: skills/lang-java/SKILL.md.

Light pass (`lang-*`, DER-333): change map, changed lines only. Not
vendor-derived (`SOURCES.md` Upstream: first-party); no `SOURCES.md`
change. Frontmatter `description` unchanged.

Key: **kept**, **route**, **dropped** (owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–10 | "Language guide. No Spring / Jakarta religion." and "No `scripts/`." | **kept** | L8 |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | **dropped** (owner `skills/language-router/SKILL.md#load-with-list`); **route**, one line, "may" kept (see MQ1) | L9 |

Lines 98 → 97. Banned names: none in old or new.

## Meaning questions

- **MQ1** — The old line listed 4 skills that may load with this one;
  the owner `skills/language-router/SKILL.md#load-with-list` lists 9.
  Resolved from the text (2026-09-27): the route defers to the owner, and
  "may" keeps the old optionality. It adds no load and no requirement.
