# Change map — `skills/lang-protobuf/SKILL.md`

Item: DER-334 (G44). Revised by DER-346 (G53): operator decision Q17,
2026-09-27. Light pass: changed lines only.

Old: `skills/lang-protobuf/SKILL.md` at main 7a11696, lines 1–73.
New: [`skills/lang-protobuf/SKILL.md`](../../../../skills/lang-protobuf/SKILL.md).
Key: **kept**, **route**, **dropped** (owner named), **DER-265**, **DER-271**.

Protected rows touched: none. Banned names: none in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 8–9 | Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening` | route (owner: `skills/language-router/SKILL.md#load-with-list`); no condition added (MQ1) | L9 |
| 9 | No `scripts/` | kept verbatim | L8 |
| 9–10 | May be the second skill next to the host language | route: "May be the second language skill", linking `#algorithm`; owner `skills/language-router/SKILL.md#algorithm` step 5 states the condition; the route adds none (MQ2) | L8 |
| 46–47 | PR review: a host language change, if any, loads the host skill as the other of the two | route: same owner and line as old L9–10; "if any" kept at the owner, step 5 (MQ2) | L8 |

All other lines are unchanged. The frontmatter description (old L3,
"load with the host language when you also change application code") is
trigger text and stays verbatim.

## Before and after, DER-346

"Before" is project-main 44d6842: the router plus this file's L8
condition. "After" is the router alone.

| Case | Before | After |
| --- | --- | --- |
| `*.proto` plus a small hand-edited Go handler, proto ≥80% | `lang-protobuf` and the Go skill (L8 "if any") | `lang-protobuf` and the Go skill (router step 5) |
| `*.proto` plus a large hand-edited Python change | `lang-protobuf` and `modern-python` | `lang-protobuf` and `modern-python` (router step 5) |
| `*.proto` plus regenerated stubs only | `lang-protobuf` only | `lang-protobuf` only |

## Meaning questions

- **MQ1** — Old L8–9 lists four skills; the owner lists nine plus
  `shell-safety` for shell turns. Resolved from the text: "Compatible
  with" is not exclusive, and the owner's list applies to every
  language skill, so the route adds no condition.
- **MQ2** — The router's Algorithm checks the ≥80% one-language rule
  before the two-language rule, so a small host edit beside proto could
  stop at one skill, while old L46–47 says "if any" host change.
  Resolved (DER-334 review, 2026-09-27): the old condition is kept in
  the text at L8 ("If any hand-edited host code changed too"); the link
  to `#algorithm` names no step number. **Revised by operator
  2026-09-27 (Q17):** the router owns the rule. Its step 5 loads both
  for proto plus any hand-edited host code and overrides the ≥80% rule.
  L8 is a route with no condition of its own.
