# Build and Review

## Build

An **open blocker** is a blocker not in `done` or `canceled`.

**manager**: before minting or resuming a **builder** on an item, claim
the item with the `tracker-sdlc` claim verb, under the builder's agent
label. The claim reads the blockers first.

Branch source for each item: see [Branches](branches-and-lands.md#branches).

### Open blockers

Do not land past an open blocker to "make progress". If any blocker is
open, resolve it, ask, or defer the item:

1. If the blocker is an item in this chunk, **resolve** it first: work
   that item, honoring *its* blockers, then return.
2. Otherwise, ask the operator ([Asking the operator](../SDLC.md#asking-the-human))
   whether to wait, drop the wait, or go ahead anyway. **manager**
   records the call on the ticket with `comment`.
3. If the operator is not available and the blocker cannot be resolved
   here, **defer** the item. Pick an unblocked item. Do not start the
   deferred item.

### Dispatch

Start every item `list-ready` returns for the Epic. For a lone incoming
item, start that item. Start them up to the `Parallelism:` ceiling in
the product repo's `## Execution`:

| `Parallelism:` in `## Execution` | Ceiling |
| --- | --- |
| `max` | None |
| `serial` | One item in Build at a time |
| `at most <N>`, where N is a positive integer | N items in Build at a time |
| No `## Execution`, or any other value | Run `sdlc-onboarding` Execution, which asks the operator. Run one item at a time until the operator answers. |

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
`debug` on the chosen fix. Do not re-open item Brief unless the failure
shows the chosen fix was the wrong *kind* of change; then escalate.

### Skills-home DoD

In this repo, any skill-body diff must match the pinned SHA in
[SOURCES.md](../../SOURCES.md) for that id. If that SHA is empty, no
body may land. Remote agent PRs into this repo still pass **security**
intake. Workers do not bypass **security**: see [Roles](../SDLC.md#roles).

## Review

Review is an explicit gate, not a PR. A local merge does **not** skip
it. Review the item before it lands on project-main or trunk.

1. **manager**: when Review starts, transition the item to `in_review`
   with `tracker-sdlc`.
2. Get a **reviewer** that is not the builder: mint or resume it per
   [Item agents](subagents.md#item-agents).
3. Take the diff range versus project-main, or versus trunk if there is
   no project-main.
4. **reviewer**: approve only if the item meets the ticket and the LLD
   **and** passes the **security** gate: intake, SHA pins, and
   trust-boundary deltas.

Monthly is not the security gate: see [Monthly](trunk-changelog-monthly.md#monthly).
