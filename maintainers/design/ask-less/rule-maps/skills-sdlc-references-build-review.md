# Rule map — `skills/sdlc/references/build-review.md`

Item: DER-736 (A4 of DER-712).

Old: `docs/sdlc/build-review.md` at main c26f424, lines 1–102.
New: [`skills/sdlc/references/build-review.md`](../../../../skills/sdlc/references/build-review.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line at c26f424.
"New L" = line in the new file (110 lines).

A0 rewrote links only (already on this branch). This item replaces
Review step 4 and adds Review step 5. Open blockers, Dispatch, and
Debug in Build stay as they are; A5 edits those.

Protected rows touched: none. The notify-only rule stays in this file
at `#definition-of-done` (kept). Operator clarifications (2026-09-27):
none of their subjects occur in the edited lines.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–65 | Build: open blocker defined, claim before a builder, branch source, open blockers, dispatch, definition of done, notify only when landed and verified | kept; A0 links | L3–65 |
| 67–78 | Debug in Build: one of the three debug skills, then `tdd`, then `verify-before-done`; not a second Brief | kept | L67–78 |
| 80–85 | Skills-home DoD: skill-body diff matches the pinned SHA; workers do not bypass **security** | kept; A0 links | L80–85 |
| 87–97 | Review is a gate. Step 1: **manager** moves the item to `in_review`. Step 2: reviewer is not the builder. Step 3: diff range versus project-main, or trunk | kept | L87–97 |
| 98–100 | **reviewer** approves only if the item meets the ticket and the LLD and passes the **security** gate (intake, SHA pins, trust-boundary deltas) | kept, and the reviewer loads `pr-review` and `yagni` and fails speculative generality (R67) | L98–101 |
| — | Fail an item diff that touches the chunk's `brief.md`; adds an asks-file section whose `Status` is not `open` or whose `Answer` is not empty; changes an existing `Status`, `Answer`, `Choices`, or `Recommendation`; or touches `## Autonomy` in an `AGENTS.md` when the ticket has no **manager** `comment` citing the operator's instruction (GR16) | new | L102–108 |
| 102 | Monthly is not the security gate | **route** kept. Owner: `trunk-changelog-monthly.md#monthly` | L110 |

## Meaning questions

None. Review steps 4 and 5 are the accepted A4 text (R67, GR16).
