Old: skills/lang-js-ts/SKILL.md at main 7a11696, lines 1–111. New: skills/lang-js-ts/SKILL.md.

Light pass (`lang-*`, DER-333): change map, changed lines only. Not
vendor-derived (`SOURCES.md` Upstream: first-party); no `SOURCES.md`
change. Frontmatter `description` unchanged.

Key: **kept**, **route**, **dropped** (owner named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–11 | One skill for both; TS-strict default when `tsconfig.json` exists; JS = same rules minus the type checker; "No `scripts/`."; not a React/Next/Vue skill | **kept** (re-wrapped) | L8–10 |
| 9–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | **dropped** (owner `skills/language-router/SKILL.md#load-with-list`); **route** | L11 |
| 104 | Never: loading `lang-web-markup` instead of this skill for `.tsx` logic | **dropped** (owner `skills/language-router/SKILL.md#map`: "`*.tsx` loads `lang-js-ts`, not `lang-web-markup`, unless the change is primarily markup or CSS"); **route**, same line as L9–10, no condition added | L11 |

Lines 111 → 110. Banned names: none in old or new.

## Meaning questions

None.
