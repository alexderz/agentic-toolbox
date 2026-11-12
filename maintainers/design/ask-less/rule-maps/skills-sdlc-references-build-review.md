# Rule map — `skills/sdlc/references/build-review.md`

Item: DER-737 (A5 of DER-712).

Old: `docs/sdlc/build-review.md` at main c26f424, lines 1–102.
New: [`skills/sdlc/references/build-review.md`](../../../../skills/sdlc/references/build-review.md).

A0 moved this file and rewrote paths only. Those path rewrites stay.
This map's dispositions are A5's. "Old L" is a line at c26f424. "New L"
is a line after A5. Review steps 4–5 are G5's and are unchanged here.

Key: **kept** (same rule), **route** (the rule lives in its owner; this
file links it in one line), **dropped** (owner named), **replaced**
(the accepted LLD changes the rule; the ruling is named).

Line count: 102 before A5, 102 after. Open blockers 11 lines → 10.
Debug in Build 3 lines → 4. The Dispatch row stays one line. Cap for
this file is ≤150.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | `# Build and Review` | kept | L1 |
| 3 | `## Build` | kept | L3 `#build` |
| 5 | Open blocker: defined in Tracker | kept | L5 |
| 7–9 | **manager** claims the item with the `tracker-sdlc` claim verb before minting or resuming a **builder**; the claim reads the blockers first | kept | L7–9 |
| 11 | Branch source for each item | route (owner: `branches-and-lands.md#branches`) | L11 |
| 13 | `### Open blockers` | kept | L13 `#open-blockers` |
| 15–16 | Do not land past an open blocker to "make progress". If any blocker is open, resolve it, ask, or defer | replaced (R66): the allowed actions are resolve or defer. The ask is removed | L15–16 |
| 18–19 | Blocker is an item in this chunk → resolve it first, honoring its blockers, then return | kept; if/then → condition → action | L18–19 |
| 20–22 | Otherwise ask the operator whether to wait, drop the wait, or go ahead; **manager** records the call with `comment` | replaced (R66): otherwise defer; **manager** records the deferral with `comment` | L20–22 |
| 23–25 | Operator not available and the blocker cannot be resolved here → defer; pick an unblocked item; do not start the deferred item | replaced (R66): defer applies to every out-of-chunk blocker, not only when the operator is unavailable. Pick an unblocked item and do not start the deferred item stay in step 2. No unblocked item left → escalate, route to `#escalation` | L20–22 (defer clauses); L23–24 (escalate) |
| 27 | `### Dispatch` | kept | L26 `#dispatch` |
| 29–31 | Start every item `list-ready` returns for the Epic; a lone incoming item starts that item; up to the `Parallelism:` ceiling in `## Execution` | kept | L28–30 |
| 33–37 | Ceiling table: `max` none, `serial` one, `at most <N>` N | kept | L32–36 |
| 38 | No `## Execution`, or any other value → run `sdlc-onboarding` Execution, which asks the operator; one item at a time until the operator answers | replaced (R14): Execution writes `Parallelism: max`; then use the `max` row. The write's owner is `skills/sdlc-onboarding/SKILL.md` Execution (A6). This cell states that result and adds no second procedure | L37 |
| 40–41 | The ceiling never orders work; blockers do. The harness may run fewer (Writable worktree) | kept | L39–40 |
| 43 | `### Definition of done` | kept | L42 `#definition-of-done` |
| 45–49 | DoD includes acceptance, tests or verification evidence, a ticket ID on the land path when the project uses tickets, a changelog line under Unreleased, current human and agent docs, no silent scope leftover | kept | L44–48 |
| 51–53 | Verifier checks tone and voice of deliverables against the project's style guide, or `docs-google-style` when the project names none; not agent context | kept | L50–52 |
| 55–57 | Do not exit Build after one pass; loop until DoD. One builder and one verifier per item | kept; the mint and resume clause routes to `subagents.md#item-agents` | L54–56 |
| 59 | Merge-ready = DoD + Review | kept | L58 |
| 60–61 | Land each merge-ready item, one land at a time | route (owner: `branches-and-lands.md#land-path`) | L59–60 |
| 63–65 | Notify only when work is landed and verified | kept; this file is the owner | L62–64 |
| 67 | `### Debug in Build` | kept | L66 `#debug-in-build` |
| 69–74 | On an unexpected failure, load one of `debug`, `debug-pocock`, `debug-anthropic`; then `tdd`; then `verify-before-done` | kept | L68–73 |
| 76–78 | Debug in Build is not a second Brief; find the root cause with `debug` on the chosen fix. Do not re-open item Brief unless the failure shows the chosen fix was the wrong kind of change; then escalate | kept; "then escalate" → "then escalate one rung", route to `#escalation` (W3, W4). No other return is added | L75–78 |
| 80 | `### Skills-home DoD` | kept | L80 `#skills-home-dod` |
| 82–85 | A skill-body diff matches the pinned SHA in `SOURCES.md`; an empty SHA means no body lands. Worker PR intake routes to intake Workers. Workers do not bypass **security** | kept; the security clause routes to `SKILL.md#roles` | L82–85 |
| 87 | `## Review` | kept | L87 `#review` |
| 89–90 | Review is an explicit gate, not a PR. A local merge does not skip it. Review before the item lands on project-main or trunk | kept | L89–90 |
| 92–93 | **manager** transitions the item to `in_review` when Review starts | kept | L92–93 |
| 94–95 | Reviewer is not the builder; mint or resume per Item agents | route (owner: `subagents.md#item-agents`) | L94–95 |
| 96–97 | Diff range versus project-main, or versus trunk if there is no project-main | kept | L96–97 |
| 98–100 | **reviewer** approves only if the item meets the ticket and the LLD and passes the **security** gate | kept. G5 (A4) edits Review steps 4–5; this item does not | L98–100 |
| 102 | Monthly is not the security gate | route (owner: `trunk-changelog-monthly.md#monthly`) | L102 |

Operator clarifications (2026-09-27): none of those four changes these
lines. Frontmatter is absent from this file.

`#escalation` is an anchor A1 adds in `skills/sdlc/SKILL.md`. This item
links it, as A5 writes. The anchor check for that link is at G15.

## Meaning questions

All resolved. None open.

- **MQ1** (old L20–22). The old step asked the operator whether to
  wait, drop the wait, or go ahead. The new step defers and records the
  deferral. That removes an ask. Resolved from the accepted A5 text and
  R66 (2026-11-11): an out-of-chunk blocker defers the item; it
  escalates only when no unblocked item is left.
- **MQ2** (old L23–25). The old step deferred only when the operator
  was unavailable and the blocker could not be resolved here. The new
  step 2 defers every out-of-chunk blocker, and step 3 escalates when
  the chunk has no unblocked item. Resolved from the same A5 text and
  R66. The "pick an unblocked item; do not start the deferred item"
  clauses stay.
- **MQ3** (old L38). The old row asked the operator and ran one item at
  a time until the answer. The new row writes `Parallelism: max` and
  uses the `max` row. Resolved from the accepted A5 text and R14
  (operator, 2026-11-11, GR9 removed): Parallelism defaults to `max`
  with no question. A6 owns the write. This row does not restate that
  procedure.
- **MQ4** (old L78). "Then escalate" did not name a rung. The new text
  says one rung and links Escalation. Resolved from the accepted A5
  text: one rung, and the ladder is the owner. No second reading
  remains in this file.

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
