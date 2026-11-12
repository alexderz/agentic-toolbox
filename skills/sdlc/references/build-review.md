# Build and Review

## Build

Open blocker: defined in [Tracker](../SKILL.md#tracker).

**manager**: before minting or resuming a **builder** on an item, claim
the item with the `tracker-sdlc` claim verb, under the builder's agent
label. The claim reads the blockers first.

Branch source for each item: see [Branches](branches-and-lands.md#branches).

### Open blockers

Do not land past an open blocker to "make progress". If any blocker is
open, **manager** resolves it or defers the item:

1. The blocker is an item in this chunk, not yet in Build → **resolve**
   it first: work that item, honoring *its* blockers, then return.
2. The blocker is an item in this chunk already in Build → leave it to
   its builder. This item waits. Pick an unblocked item.
3. Otherwise → **defer** the item. Pick an unblocked item. Do not start
   the deferred item. **manager** records the deferral on the ticket
   with `comment`. The deferred item stays filed; it is ready again when
   its blocker closes.
4. Step 3 deferred the item, and no unblocked item is left, in the chunk
   or for a lone item → escalate the blocker at the Item rung:
   [Escalation](../SKILL.md#escalation).

### Dispatch

Start every item `list-ready` returns for the Epic. For a lone incoming
item, start that item. Start them up to the `Parallelism:` ceiling in
the product repo's `## Execution`:

| `Parallelism:` in `## Execution` | Ceiling |
| --- | --- |
| `max` | None |
| `serial` | One item in Build at a time |
| `at most <N>`, where N is a positive integer | N items in Build at a time |
| No `## Execution`, or any other value | Run `sdlc-onboarding` Execution, which writes `Parallelism: max`. Use the `max` row now; do not wait for that commit to land. |

The ceiling never orders work; blockers do. The harness may run fewer
items: see [Writable worktree](subagents.md#writable-worktree).

### Definition of done

**DoD** (definition of done) includes: acceptance on the ticket; tests
or verification evidence; the [land path](branches-and-lands.md#land-path)
cites a ticket ID when the project uses tickets; a changelog line under
Unreleased; human and agent docs current for this item; no silent scope
leftover.

The verifier checks the tone and voice of deliverables against the
project's style guide; if the project names none, `docs-google-style`.
The verifier does not review agent context for tone.

Do not exit Build after one pass. Loop implement → test → fix until the
item meets DoD. Builder and verifier: one each per item, minted and
resumed per [Item agents](subagents.md#item-agents).

An item is merge-ready when it meets DoD and passes [Review](#review).
Land each merge-ready item, one land at a time, per
[Land path](branches-and-lands.md#land-path).

Notify only when work is **landed and verified**. Landed means on
project-main, or on trunk if trunk was the land target. Do not notify on
"pushed to an item branch" or on "LGTM" without evidence.

### Debug in Build

On an unexpected failure:

1. Load `debug` by default. `debug-pocock` and `debug-anthropic` are
   alternatives. Load only **one** of the three.
2. Load `tdd` for the cause.
3. Load `verify-before-done` to prove the fix.

Debug in Build is **not** a second Brief: find the root cause with
`debug` on the chosen fix. Do not re-open item Brief. Escalate at the
Item rung ([Escalation](../SKILL.md#escalation)) only when:

1. the failure shows the chosen fix was the wrong *kind* of change; or
2. this is the third failed fix of the same item, counted since the item's last escalation.

**builder**: to escalate, report it to the **manager** in your result,
with the need, the line forcing it, why it cannot be met, and what was
tried. Any other failure: [Mid-build returns](../SKILL.md#asking-the-human).

### Skills-home DoD

In this repo, any skill-body diff must match the pinned SHA in
[SOURCES.md](../../../SOURCES.md) for that id. If that SHA is empty, no
body may land. Worker PR intake: [Workers](intake.md#workers).
Workers do not bypass **security**: see [Roles](../SKILL.md#roles).

## Review

Review is an explicit gate, not a PR. A local merge does **not** skip
it. Review the item before it lands on project-main or trunk.

1. **manager**: when Review starts, transition the item to `in_review`
   with `tracker-sdlc`.
2. Get a **reviewer** that is not the builder: mint or resume it per
   [Item agents](subagents.md#item-agents).
3. Take the diff range versus project-main, or versus trunk if there is
   no project-main.
4. **reviewer**: fail the item when its diff does any of these (GR16). Skip a commit titled
   `[<ticket-id>] Record asks` that changes only the asks file only when a **manager** `comment`
   on the item's ticket names its SHA. Check every other commit that touches the asks file.
   1. touches the chunk's `brief.md`;
   2. adds an asks-file section whose `Status` is not `open`, or whose `Answer` is not empty;
   3. changes or removes the `Status`, `Answer`, `Choices` or `Recommendation` of an existing
      asks-file section;
   4. touches `## Autonomy` in an `AGENTS.md`, and the item's ticket has no **manager** `comment`
      citing the operator's instruction for that change. That comment names the ask id and its
      answer, or the date, in the manager's words.

   A needed `brief.md` or answer change → the **manager** or the **liaison** makes it on
   project-main, outside the item.
5. **reviewer**, with `pr-review` and `yagni` loaded: approve only if step 4 failed nothing, the
   item meets the ticket and the LLD, it ships no speculative generality (the `yagni` Iron law and
   Decide and log), **and** it passes the **security** gate: intake, SHA pins, and trust-boundary
   deltas.

Monthly is not the security gate: see [Monthly](trunk-changelog-monthly.md#monthly).
