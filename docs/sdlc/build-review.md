# Build and Review

## Build

Before minting or resuming a **builder** on an item, **manager** claims
it with the `tracker-sdlc` claim verb, under the builder's agent label
(claim reads the blockers first). An **open**
blocker is a blocker not in `done` or `canceled`.

### Open blockers

If any blocker is open:

1. **Resolve** it first when it is an item in this chunk (work that
   item, honoring *its* blockers, then return).
2. **Otherwise ask the human** (see [Asking the human](../SDLC.md#asking-the-human))
   whether to wait, drop the wait, or go ahead anyway. **manager**
   records the call on the ticket with `comment`.
3. If the operator is not available and the blocker cannot be resolved
   here: **defer** the item. Pick an unblocked one. Do not start it.

Do not land past an open blocker to “make progress.”

### Dispatch

**Dispatch.** Start every item `list-ready` returns for the Epic (a lone
incoming item: that item), up to the `Parallelism:` ceiling in the
product repo's `## Execution`: `max` (none), `serial` (one item in Build
at a time), or `at most <N>` (N a positive integer). The ceiling never
orders work; blockers do. The harness may run fewer ([Writable
worktree](subagents.md#writable-worktree)). No `## Execution`, or any other
value → run `sdlc-onboarding` Execution (ask); one at a time until the
operator answers.

**Do not exit Build after one pass.** Loop implement → test → fix
until the ticket Definition of Done is actually met. Use **one builder
subagent and one verifier subagent per work item** for that loop (see
[Subagents per work item](subagents.md#item-agents)).

Each item **branches off project-main** (or off trunk if there is no
project-main), not off a pile of sibling item branches. Items split from
an accepted Spec branch here; incoming items already have theirs from
item Brief. Independent
items may **build** in parallel. When an item is merge-ready (DoD +
Review), **land it on project-main** (or trunk) — do not stockpile
finished-but-unmerged branches for a batch integrate. Lands are one at
a time.

### Definition of done

DoD includes: acceptance on the ticket, tests/verification evidence,
land path cites a ticket ID when the project uses tickets, changelog
line under Unreleased, human + agent docs current for this item, no
silent scope leftover. The verifier checks the tone and voice of
deliverables against the project's style guide (default
`docs-google-style`); it does not review agent context for tone.

Notify only when work is **landed and verified**.

### Debug in Build

On unexpected failure, load **`debug`** (default). Alternatives
`debug-pocock` / `debug-anthropic` — load **one**. Then `tdd` for the
cause and `verify-before-done` to prove the fix. Notify
**landed+verified** on **project-main** (or trunk if that was the land
target) — not “pushed to an item branch” and not “LGTM without
evidence.”

This is **not** a second Brief. Root cause during Build is `debug` on
the chosen fix. Do not re-open item-Brief unless the failure shows the
chosen fix was the wrong *kind* of change (then escalate).

### Skills-home DoD

**Skill-home DoD (this repo):** any skill-body diff must match the pinned
SHA in [SOURCES.md](../../SOURCES.md) for that id. Empty SHA means no body
may land. Remote agent PRs into this repo still pass **security intake**.
Workers **do not bypass** intake, SHA pins, or security Spec/Review gates.

## Review

Review **before** the item lands on project-main (or trunk). When
Review starts, **manager** transitions the item to `in_review` with
`tracker-sdlc`. The
reviewer is **not** the builder who wrote the diff. Same-session
self-review does not count. Review is an explicit gate, not a PR; a
local merge does **not** skip it.

First review of this item: mint a **clean reviewer**. Later review rounds
on the same item (after fixes): **resume that reviewer**. Do not mint a
new reviewer each round, and do not feed it the builder’s transcript.

Reviewer approves only if the item meets the ticket + LLD **and** the
**security** gate (intake, SHA pins, trust-boundary deltas). Security at
land is a gate, not deferred to Monthly. Diff range is versus
**project-main** (or versus trunk if there is no project-main).
