# Rule map — `docs/sdlc/build-review.md`

Item: DER-303 (C6).

Old: `docs/SDLC.md` at main 7a11696, lines 787–868 and 1088.
New: [`docs/sdlc/build-review.md`](../../../../docs/sdlc/build-review.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives
in its owner; this file links it in one line), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line in old
`docs/SDLC.md`; "New L" = line in the new file. C1 (DER-298) moved these
lines verbatim and added the H3 headings `Open blockers`, `Dispatch`,
`Definition of done`, `Debug in Build`, `Skills-home DoD`; all anchors
(`#build`, `#open-blockers`, `#dispatch`, `#definition-of-done`,
`#debug-in-build`, `#skills-home-dod`, `#review`) are kept.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 787 | `### Build` heading | kept as H2 (C1) | L3 `#build` |
| 789–791 | Before minting or resuming a builder, **manager** claims the item with the `tracker-sdlc` claim verb under the builder's agent label; claim reads blockers first | kept; parenthesis → own sentence | L7–9 |
| 791–792 | Open blocker = blocker not in `done` or `canceled` | kept; moved first so the name is defined before use | L5 |
| 794 | "If any blocker is open:" | kept | L15–16 |
| 796–797 | Blocker is an item in this chunk → resolve it first, honoring its blockers, then return | kept; condition → if/then | L18–19 |
| 798–800 | Otherwise ask whether to wait, drop the wait, or go ahead; **manager** records the call with `comment` | kept; "the human" → "the operator" (heading of the owner section; index Roles: operator = human in the loop); link text follows the owner heading | L20–23 |
| 801–802 | Operator not available and blocker not resolvable here → defer; pick an unblocked item; do not start the deferred item | kept; "Do not start it" → "the deferred item" (MQ1) | L24–26 |
| 804 | Do not land past an open blocker to "make progress" | kept; placed first in the section (standard 7), allowed actions named beside it | L15–16 |
| 806–807 | Dispatch: start every item `list-ready` returns for the Epic; lone incoming item: that item | kept, meaning exact; parenthesis → sentence | L30–31 |
| 807–809 | Up to the `Parallelism:` ceiling in `## Execution`: `max` none, `serial` one in Build at a time, `at most <N>` N positive integer | kept, meaning exact; values → condition table; `at most <N>` row states the ceiling N | L31–38 |
| 809–810 | Ceiling never orders work; blockers do | kept | L41 |
| 810–811 | Harness may run fewer (Writable worktree) | kept; link target fixed to `subagents.md#writable-worktree` in C1 | L41–42 |
| 811–813 | No `## Execution` or other value → run `sdlc-onboarding` Execution (ask); one at a time until the operator answers | kept, meaning exact; table row | L39 |
| 815–816 | Do not exit Build after one pass; loop implement → test → fix until DoD is met | kept; moved below the DoD list so DoD is defined before use (standard 4) | L61–62 |
| 816–818 | One builder and one verifier subagent per work item | route (owner: `subagents.md#item-agents`) | L62–63 |
| 820–823 | Each item branches off project-main, else trunk, never off sibling item branches; Spec-split items branch at Build, incoming items at item Brief | route (owner: `branches-and-lands.md#branches`, table row "item branch", and `#never` first bullet) | L11 |
| 823–824 | Independent items may build in parallel | dropped (owner: Dispatch in this file, L30–39; `branches-and-lands.md#project-main` "Builds may run in parallel") | — |
| 824–825 | Merge-ready = DoD + Review | kept; parenthesis → sentence, links `#review` | L65–66 |
| 825–827 | Land each merge-ready item on project-main or trunk; do not stockpile for a batch integrate; lands one at a time | route (owner: `branches-and-lands.md#land-path`; no-stockpile also held at `#project-main` and `#never`) | L66–67 |
| 829–831 | DoD includes: acceptance on the ticket, tests/verification evidence, land path cites a ticket ID when the project uses tickets, changelog line under Unreleased, human + agent docs current, no silent scope leftover | kept; list; "land path" links `branches-and-lands.md#land-path` | L46–54 |
| 832–834 | Verifier checks tone and voice of deliverables against the project's style guide (default `docs-google-style`); not agent context | kept; "(default …)" → "If the project names none, use …" | L56–59 |
| 836–838 | On unexpected failure: load `debug` (default) or one of `debug-pocock` / `debug-anthropic`; then `tdd` for the cause, `verify-before-done` to prove the fix | kept; numbered steps | L75–80 |
| 838–841 | Notify landed+verified on project-main, or trunk if that was the land target; not "pushed to an item branch", not "LGTM without evidence" | dropped here, moved into the owner copy in `#definition-of-done` (writing-standard Rule owners) | L69–71 |
| 843–845 | Not a second Brief; root cause in Build is `debug` on the chosen fix; do not re-open item Brief unless the fix was the wrong kind of change (then escalate) | kept; "(then escalate)" → "; in that case, escalate" (MQ2) | L82–85 |
| 847–849 | Skills home: skill-body diff must match the pinned SHA in `SOURCES.md`; empty SHA → no body lands; remote agent PRs still pass security intake | kept; list | L89–94 |
| 850 | Workers do not bypass intake, SHA pins, security Spec/Review gates | route (owner: `docs/SDLC.md#roles`); intake and SHA pins stay in L89–94 | L96 |
| 852 | `### Review` heading | kept as H2 (C1) | L98 `#review` |
| 854 | Review before the item lands on project-main (or trunk) | kept | L101 |
| 854–856 | When Review starts, **manager** transitions the item to `in_review` with `tracker-sdlc` | kept; step 1 | L103–104 |
| 856–858 | Reviewer is not the builder; same-session self-review does not count | route (owner: `subagents.md#item-agents`: reviewer "Never the builder", clean mint, Never "reviewer-reviews its own work") | L105–106 |
| 858–859 | Review is an explicit gate, not a PR; a local merge does not skip it | kept; placed first (standard 7) | L100–101 |
| 861–863 | First review: mint a clean reviewer; later rounds: resume it; no new reviewer per round; no builder transcript | route (owner: `subagents.md#item-agents` table row "reviewer" and Never) | L105–106 |
| 865–866 | Reviewer approves only if ticket + LLD **and** security gate (intake, SHA pins, trust-boundary deltas) | kept; actor **reviewer**; parenthesis → colon list (it defines the gate's scope, not examples) | L109–111 |
| 866–867 | Security at land is a gate | kept | L113 |
| 867 | Not deferred to Monthly | route (owner: `trunk-changelog-monthly.md#monthly`) | L113–114 |
| 867–868 | Diff range versus project-main, or trunk if there is no project-main | kept; step 3 | L107–108 |
| 1088 | Notify only when work is landed and verified | kept; this file is the owner (`#definition-of-done`) | L69 |

Link from DoD to `#review` (L66): Review is a step named and linked in
the SDLC index Steps table, which How to read sends every reader through
first, so the name is defined before this file; the link is the one the
ticket requires, not a forward definition.

Operator clarifications (2026-09-27): none applies to these lines (no
groom-review fix, gate-reason parenthesis, review-item verdict, "a
person" or "Improvise" text).

## Meaning questions

All resolved from the text.

- **MQ1** (old L802) "Pick an unblocked one. Do not start it.": "it"
  is the deferred item, the only item the rule stops; the unblocked item
  is picked in order to be started. New text names "the deferred item".
- **MQ2** (old L844–845) "unless … wrong kind of change (then
  escalate)": the new text keeps the same structure (exception to "do
  not re-open item Brief", action escalate) and picks no further
  reading; only the parenthesis became a clause.
