# Change map — `skills/lang-web-markup/SKILL.md`

Item: DER-335 (G, light pass).

Old: `skills/lang-web-markup/SKILL.md` at main 7a11696, lines 1–78.
New: [`skills/lang-web-markup/SKILL.md`](../../../../skills/lang-web-markup/SKILL.md).
Light pass: this map lists changed lines only; every other line is
unchanged. 78 lines old, 77 new.

Names: no banned name in old or new. HTML / CSS advice (Iron law through
Red flags): unchanged. Frontmatter `description`: unchanged (see MQ1).

| Old L | Change | Kind | Reason |
| --- | --- | --- | --- |
| 8–10 | "Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`." and "May be the second skill next to `lang-js-ts`. Cap is still 2." → one route line (new L9): "Process skills that **may** load with this one: `[load-with list](…#load-with-list)`. When a second language skill may load: `[iron law](…#iron-law)`, `[Algorithm](…#algorithm)`."; "One skill for markup and style." and "No `scripts/`." kept on new L8 | dedupe | The process skills are the load-with list ([`language-router#load-with-list`](../../../../skills/language-router/SKILL.md#load-with-list)); when a second language skill may load is owned by the router [iron law](../../../../skills/language-router/SKILL.md#iron-law) and [Algorithm](../../../../skills/language-router/SKILL.md#algorithm); "Cap is still 2" is not stated by the owner and is dropped into the route; the route adds no condition |

## Meaning questions

- **MQ1** — The frontmatter `description` says "load lang-js-ts first;
  this may be the second skill", a repeat of the router map note on
  `*.tsx`. Resolved by the operator 2026-09-27 (Q16): descriptions are
  metadata, kept.
- **MQ2** — Old L10 "May be the second skill next to `lang-js-ts`. Cap
  is still 2." carried no condition; the owner allows a second language
  skill only when the diff is mixed-language (iron law) and names TSX
  with a stylesheet (Algorithm). Resolved from the text: the owner holds
  the rule (standard 5), so the route follows the owner's condition.
- **MQ3** — Old L8–9 named four process skills; the owner's load-with
  list names nine. Resolved from the text: the route follows the owner's
  list, and "**may**" keeps each one optional.
