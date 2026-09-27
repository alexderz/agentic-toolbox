# Change map — `skills/lang-protobuf/SKILL.md`

Item: DER-334 (G44). Light pass: changed lines only.

Old: `skills/lang-protobuf/SKILL.md` at main 7a11696, lines 1–73.
New: [`skills/lang-protobuf/SKILL.md`](../../../../skills/lang-protobuf/SKILL.md).
Key: **kept**, **route**, **dropped** (owner named), **DER-265**, **DER-271**.

Protected rows touched: none. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route (owner: `skills/language-router/SKILL.md#load-with-list`); no condition added (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |
| 9–10 | May be the second skill next to the host language | route (owner: `skills/language-router/SKILL.md#algorithm` step 6, "proto and hand-edited host code, load both"); same route line (MQ2) | L9 |
| 46–47 | PR review: a host language change loads the host skill as the other of the two | dropped, duplicate of old L9–10; owner `skills/language-router/SKILL.md#algorithm` step 6, routed at L9 (MQ2) | L9 |

All other lines are unchanged. The frontmatter description (old L3,
"load with the host language when you also change application code") is
trigger text and stays verbatim.

## Meaning questions

- **MQ1** — Old L8–9 lists four skills; the owner lists nine plus
  `shell-safety` for shell turns. Resolved from the text: "Compatible
  with" is not exclusive, and the owner's list applies to every
  language skill, so the route adds no condition.
- **MQ2** — The owner's step 5 loads one skill when one language owns
  ≥80% of the change, while old L46–47 says "if any" host change.
  Resolved from the text: step 6 names "proto and hand-edited host code"
  as a case of two first-class languages that loads both, so any
  hand-edited host code beside proto loads the host skill, as the old
  lines said. The anchor `#algorithm` is used because the Load-with
  list does not hold this rule.
