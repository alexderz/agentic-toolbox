# Change map — `skills/lang-rust/SKILL.md`

Item: DER-334 (G44). Light pass: changed lines only.

Old: `skills/lang-rust/SKILL.md` at main 7a11696, lines 1–113.
New: [`skills/lang-rust/SKILL.md`](../../../../skills/lang-rust/SKILL.md).
Key: **kept**, **route**, **dropped** (owner named), **DER-265**, **DER-271**.

Protected rows touched: none. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–9 | Language guide; distills what agents get wrong; not a paste of the Microsoft guidelines or a 200-rule dump | kept verbatim | L8–9 |
| 9–10 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route (owner: `skills/language-router/SKILL.md#load-with-list`); one route line, no condition added (MQ1) | L10 |
| 10 | No `scripts/` | kept verbatim | L9 |

All other lines are unchanged. Old L105 (never paste the Microsoft
guidelines file) stays: it names a Rust source, which the item's two
named rules (load-with list, one language skill) do not cover.

## Meaning questions

- **MQ1** — Old L9–10 lists four skills; the owner lists nine plus
  `shell-safety` for shell turns. Resolved from the text: "Compatible
  with" is not exclusive, and the owner's list applies to every
  language skill, so the route adds no condition. Same resolution as
  `skills-modern-python.md` old L12–13.
