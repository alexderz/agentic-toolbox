# Rule map — `skills/yagni/SKILL.md`

Item: DER-736 (A4 of DER-712).

Old: `skills/yagni/SKILL.md` at main c26f424, lines 1–41.
New: [`skills/yagni/SKILL.md`](../../../../skills/yagni/SKILL.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line at c26f424.
"New L" = line in the new file.

The new file is the LLD block, 40 lines. A0 had rewritten two links
only; this item replaces the body. **security** reads this body at
Review.

The LLD locates Ask first at old L21–27. The second-toolkit bullet is
old L28. A line number is a locator only; that bullet is mapped below
with the abstraction and flag bullets.

Protected rows touched: none. Operator clarifications (2026-09-27):
frontmatter `description` is metadata, not a second copy of a rule
(Q16). None of the other clarifications occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–2 | Front matter `name` | kept | L1–2 |
| 3 | Description: when to use the skill | kept, plus the users (builder, item contrarian, reviewer) and "do not use on a chunk brief" (A4). Metadata (Q16) | L3 |
| 4 | Front matter close | kept | L4 |
| 6 | Title "YAGNI" | kept | L6 |
| 8 | The ask; speculative generality; use restraint; smallest change for this ask; compatible with `tdd` and `verify-before-done`; this skill has no `scripts/` | kept verbatim | L8 |
| 10–12 | Iron law: do not ship speculative generality; if the ask does not need it, leave it out | kept verbatim | L10–12 |
| 14 | Heading "Always" | kept | L14 |
| 16–19 | One focused PR; delete or skip dead paths and keep one path; reuse an installed skill id; keep `AGENTS.md` thin | kept verbatim | L16–19 |
| — | `yagni` for safety: add no guardrail that no rule and no operator asked for, unless it protects a one-way door; a control a **security** rule or finding requires is a rule, not a guardrail | new (R81); routes the ask/ruling shape to `skills/sdlc/SKILL.md#asking-the-human` | L20 |
| 21 | Heading "Ask first" | dropped as an ask heading (accepted A4). Replaced by Decide and log | L22 |
| 23 | Ask the operator before the bullets | **dropped** as an ask (accepted A4). Owner of when to ask: `skills/sdlc/SKILL.md#asking-the-human`. The new lead says act and log a ruling | L24 |
| 25 | New abstraction for later reuse, no second caller | not an ask; Decide and log, stricter: leave it out (A4) | L26 |
| 26 | New config flag or feature toggle with no current consumer | not an ask; Decide and log, stricter: leave it out (A4) | L26 |
| 27 | Expanding a skill past ~250 lines | not an ask; past its line cap → split it into a second file (R45). The cap number stays the writing standard | L27 |
| 27 | Adding `scripts/` to a skill dir | **route**: never in a first-party skill (intake: ship first-party files without `scripts/`); a vendor helper only through [intake](../../../../skills/sdlc/references/intake.md) checklist step 2 (R82) | L27 |
| 28 | Second toolkit that overlaps an installed skill id | not an ask; Decide and log, stricter: leave it out; reuse the installed id (A4) | L26 |
| 30 | Heading "Never" | kept | L29 |
| 32 | Never remint a MERGED skill body without a new **security** cut; get the cut first | kept verbatim | L31 |
| 33 | Never add marketplace installers or auto-update upstream; take third-party content through intake | kept; link text `INTAKE.md` → `intake`. A0 already moved the path | L32 |
| 34 | Never add just-in-case helpers for personal finance, mail, password stores, or extra hosts; leave them out | kept verbatim | L33 |
| 36 | Red flags: if the plan says one of these, stop, shrink the change, ship the ask | kept verbatim | L35 |
| 38–41 | Four red-flag phrases | kept verbatim | L37–40 |

## Meaning questions

None. Ask first becomes Decide and log as the accepted LLD states
(A4, R45, R82, R81). Old L8 "this skill has no `scripts/`" stays the
statement about this skill. The general `scripts/` rule is the route
on old L27.
