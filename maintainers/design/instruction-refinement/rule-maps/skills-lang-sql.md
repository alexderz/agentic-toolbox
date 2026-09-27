# Change map — `skills/lang-sql/SKILL.md`

Item: DER-335 (G, light pass).

Old: `skills/lang-sql/SKILL.md` at main 7a11696, lines 1–94.
New: [`skills/lang-sql/SKILL.md`](../../../../skills/lang-sql/SKILL.md).
Light pass: this map lists changed lines only; every other line is
unchanged. 94 lines old, 93 new.

Names: no banned name in old or new. SQL advice (Iron law through Red
flags): unchanged. Frontmatter `description`: unchanged (see MQ1).

| Old L | Change | Kind | Reason |
| --- | --- | --- | --- |
| 8–10 | "Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`, and the host language skill." → one route line (new L9): "Process skills that **may** load with this one: [load-with list](…#load-with-list). SQL beside its host language: [Algorithm](…#algorithm)."; "Parameterize or do not ship." and "No `scripts/`." kept on new L8 | dedupe | The process skills are the load-with list, owned by [`language-router#load-with-list`](../../../../skills/language-router/SKILL.md#load-with-list); when SQL and its host language both load is owned by [`language-router#algorithm`](../../../../skills/language-router/SKILL.md#algorithm); the route adds no condition |

## Meaning questions

- **MQ1** — The frontmatter `description` says "load with the host
  language skill when the query lives in application code", a repeat of
  the `language-router` Algorithm. Resolved by the operator 2026-09-27
  (Q16): descriptions are metadata, kept.
- **MQ2** — Old L8–9 named four process skills; the owner's load-with
  list names nine. Resolved from the text: the owner holds the rule
  (standard 5, writing-standard `#rule-owners` "Language map, load-with
  list"), so the route follows the owner's list, and "**may**" keeps
  each one optional.
