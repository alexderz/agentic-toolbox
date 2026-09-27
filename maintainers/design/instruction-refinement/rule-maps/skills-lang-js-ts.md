Old: skills/lang-js-ts/SKILL.md at main 7a11696, lines 1–111. New: skills/lang-js-ts/SKILL.md.

Light pass (`lang-*`, DER-333): change map, changed lines only. Not
vendor-derived (`SOURCES.md` Upstream: first-party); no `SOURCES.md`
change. Frontmatter `description` unchanged.

Key: **kept**, **route**, **dropped** (owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–11 | One skill for both; TS-strict default when `tsconfig.json` exists; JS = same rules minus the type checker; "No `scripts/`."; not a React/Next/Vue skill | **kept** (re-wrapped) | L8–10 |
| 9–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | **dropped** (owner `skills/language-router/SKILL.md#load-with-list`); **route**, one line, "may" kept (see MQ1) | L11 |
| 104 | Never: loading `lang-web-markup` instead of this skill for `.tsx` logic | **dropped** (owner `skills/language-router/SKILL.md#map`: "`*.tsx` loads `lang-js-ts`, not `lang-web-markup`, unless the change is primarily markup or CSS"); **route**, its own line | L12 |

Lines 111 → 111. Banned names: none in old or new.

## Meaning questions

- **MQ1** — The old line listed 4 skills that may load with this one;
  the owner `skills/language-router/SKILL.md#load-with-list` lists 9.
  Resolved from the text (2026-09-27): the route defers to the owner, and
  "may" keeps the old optionality. It adds no load and no requirement.
