# Change map — `skills/lang-python/SKILL.md`

Item: DER-334 (G44). Light pass: changed lines only.

Old: `skills/lang-python/SKILL.md` at main 7a11696, lines 1–43.
New: [`skills/lang-python/SKILL.md`](../../../../skills/lang-python/SKILL.md).
Key: **kept**, **route**, **dropped** (owner named), **DER-265**, **DER-271**.

Protected rows touched: none. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–9 | This id routes; load `modern-python`; do not remint uv/ruff/ty/pytest advice | kept verbatim (the pointer's job, per `language-router` `#map`) | L8–9 |
| 9–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route (owner: `skills/language-router/SKILL.md#load-with-list`); no condition added (MQ1) | L10 |
| 10 | No `scripts/`; `modern-python` is first-party MIT | kept verbatim | L9 |
| 16–18 | "Load": `modern-python` only, then stop | dropped, duplicate of old L8; owner `skills/language-router/SKILL.md#map` (Python row: `modern-python`), routed at L10 (MQ2) | L10 |

All other lines are unchanged. Old L14 (Iron law) and old L41, L43
(Never) stay: they bar a second Python guide in this pack, which the
item's two named rules (load-with list, one language skill) do not cover.

## Meaning questions

- **MQ1** — Old L9–10 lists four skills; the owner lists nine plus
  `shell-safety` for shell turns. Resolved from the text: "Compatible
  with" is not exclusive, and the owner's list applies to every
  language skill, so the route adds no condition. Same resolution as
  `skills-modern-python.md` old L12–13.
- **MQ2** — "Then stop" could mean stop routing or stop reading.
  Resolved from the text: the owner's Algorithm step 7 says "Read the
  chosen `SKILL.md`. Stop routing.", and old L8 still says "Load
  `modern-python`", so the load and the single skill stay; the next
  section ("Combined verify (after modern-python)") shows reading goes on.
