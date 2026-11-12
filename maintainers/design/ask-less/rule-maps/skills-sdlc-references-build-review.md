# Rule map — `skills/sdlc/references/build-review.md`

## Build (DER-737, G6 / A5)

Old: `docs/sdlc/build-review.md` at main c26f424, lines 1–86. New:
`skills/sdlc/references/build-review.md`.

Item: DER-737 (G6 of DER-712; source item A5). Exact text:
[G6](../opus-rebuild.md#g6--build-blockers-dispatch-debug-a5). "Old L"
is a line at c26f424; "New L" is a line in the new file. A0 moved the
file and rewrote its paths only (DER-730); this map ignores those path
rewrites. Key: **kept**, **route**, **dropped** with the owner named,
**changed** with the brief, ruling or LLD id that decides it.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–11 | Title, `## Build`, open blocker defined in Tracker, **manager** claims before minting a builder, branch source | kept | L1–11 |
| 13 | `### Open blockers` heading | kept | L13 |
| 15–16 | Never land past an open blocker; resolve, ask or defer | **changed** (R66, R148): the ask is gone; **manager** is the actor; resolve or defer | L15–16 |
| 18–19 | In-chunk blocker → resolve it first, honoring its blockers | kept for an in-chunk blocker not yet in Build; clarified (R148, of R66) | L18–19 |
| — | In-chunk blocker already in Build → leave it to its builder; pick an unblocked item | **changed** (R148): new clause, a clarification of R66 | L20–21 |
| 20–22 | Otherwise ask the operator whether to wait, drop the wait or go ahead; **manager** records the call with `comment` | **changed** (R66): no ask; the item is deferred; **manager** records the deferral with `comment` | L22–24 |
| 23–25 | Operator unavailable and blocker unresolvable → defer; pick an unblocked item; do not start the deferred item | **changed** (R66): defer applies to every out-of-chunk blocker; the deferred item stays filed and is ready again when its blocker closes (R148) | L22–25 |
| — | No unblocked item left, in the chunk or for a lone item → escalate the blocker at the Item rung | **changed** (R66, R148): new step; the lone-item clause is a clarification of R66; route to index `#escalation` | L26–28 |
| 27–37 | `### Dispatch`; start every ready item up to the `Parallelism:` ceiling; table rows `max`, `serial`, `at most <N>` | kept | L30–40 |
| 38 | No or invalid `## Execution` → onboarding asks the operator; one item at a time until answered | **changed** (R14, R69, R149): onboarding writes `Parallelism: max`; use the `max` row now, without waiting for that commit | L41 |
| 40–41 | Ceiling never orders work; harness may run fewer | kept | L43–44 |
| 43–65 | `### Definition of done`; verifier tone check; loop until DoD; merge-ready and land; notify only when landed and verified | kept | L46–68 |
| 67–74 | `### Debug in Build`; load one `debug` variant, `tdd`, `verify-before-done` | kept | L70–77 |
| 76–77 | Debug in Build is not a second Brief: root cause with `debug` on the chosen fix; do not re-open item Brief | kept | L79–80 |
| 77–78 | Wrong *kind* of change → escalate | **changed** (R150, R122): escalate at the Item rung, route to index `#escalation` | L80–83 |
| — | Third failed fix of the same item, counted since the item's last escalation → escalate at the Item rung | **changed** (R150, R122; trigger from R93): new route in Build | L84 |
| — | **builder** reports the escalation to the **manager** with the need, the line, why it cannot be met, what was tried; any other failure → Mid-build returns | **changed** (R150): route to index `#escalation` and `#asking-the-human` | L86–88 |
| 80–85 | `### Skills-home DoD`; SHA pin; worker intake; workers do not bypass **security** | kept | L90–95 |

Old L87–102 (`## Review`) is outside this item: G5 (A4) maps the Review
edit in its own section of this file.

### Meaning questions

None. Each changed row cites the overlay text and the ruling that
decides it.

## Review (DER-736, G5 / A4)

Old: `docs/sdlc/build-review.md` at main c26f424, lines 98–100. New: `skills/sdlc/references/build-review.md`.
Item: DER-736 (G5, A4 of DER-712). Changed lines only: Review step 4. G6 maps its own Build edits.
Text: [opus-rebuild.md G5](../opus-rebuild.md#g5--yagni-subagents-pack-review-a4).

Key: **kept**, **route**, **dropped** with the owner named, **changed** with the brief, ruling or
LLD id that decides it.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | GR16: the reviewer fails a diff that touches `brief.md`, adds a non-open or answered asks-file section, changes or removes an existing `Status`, `Answer`, `Choices` or `Recommendation`, or touches `## Autonomy` without a manager `comment`; skips only a `Record asks` commit whose SHA a manager `comment` names | **changed** (GR16, R114, R141, R142, R185): new step 4, run first | Review step 4 |
| 98–100 | Reviewer approves only if the item meets the ticket and the LLD and passes the security gate | **changed** (R67, R141): step 5; loads `pr-review` and `yagni`; also needs step 4 to fail nothing and no speculative generality (the `yagni` Iron law and Decide and log) | Review step 5 |

### Meaning questions

None.
