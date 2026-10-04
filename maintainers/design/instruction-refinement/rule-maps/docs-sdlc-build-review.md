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

Line counts: old section 83 lines (L787–868 and L1088; 68 non-blank).
New file 102 lines: +19. Of these, +12 are the C1 H1 and five H3
anchor headings with their blank lines, which the LLD file map
requires. The other +7 make rules checkable: the Dispatch
`Parallelism:` condition table, if/then open-blocker steps, numbered
Debug and Review steps with their actors, and "open blocker" defined
on its own line before use. Every other paragraph is the same length
as the old text or shorter (MQ3).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 787 | `### Build` heading | kept as H2 (C1) | L3 `#build` |
| 789–791 | Before minting or resuming a builder, **manager** claims the item with the `tracker-sdlc` claim verb under the builder's agent label; claim reads blockers first | kept; parenthesis → own sentence | L7–9 |
| 791–792 | Open blocker = blocker not in `done` or `canceled` | kept; moved first so the name is defined before use | L5 |
| 794 | "If any blocker is open:" | kept | L15–16 |
| 796–797 | Blocker is an item in this chunk → resolve it first, honoring its blockers, then return | kept; condition → if/then | L18–19 |
| 798–800 | Otherwise ask whether to wait, drop the wait, or go ahead; **manager** records the call with `comment` | kept; "the human" → "the operator" (heading of the owner section; index Roles: operator = human in the loop); link text follows the owner heading | L20–22 |
| 801–802 | Operator not available and blocker not resolvable here → defer; pick an unblocked item; do not start the deferred item | kept; "Do not start it" → "the deferred item" (MQ1) | L23–25 |
| 804 | Do not land past an open blocker to "make progress" | kept; placed first in the section (standard 7), allowed actions named beside it | L15–16 |
| 806–807 | Dispatch: start every item `list-ready` returns for the Epic; lone incoming item: that item | kept, meaning exact; parenthesis → sentence | L29–30 |
| 807–809 | Up to the `Parallelism:` ceiling in `## Execution`: `max` none, `serial` one in Build at a time, `at most <N>` N positive integer | kept, meaning exact; values → condition table; `at most <N>` row states the ceiling N | L30–37 |
| 809–810 | Ceiling never orders work; blockers do | kept | L40 |
| 810–811 | Harness may run fewer (Writable worktree) | kept; link target fixed to `subagents.md#writable-worktree` in C1 | L40–41 |
| 811–813 | No `## Execution` or other value → run `sdlc-onboarding` Execution (ask); one at a time until the operator answers | kept, meaning exact; table row | L38 |
| 815–816 | Do not exit Build after one pass; loop implement → test → fix until DoD is met | kept; moved below the DoD list so DoD is defined before use (standard 4) | L55–56 |
| 816–818 | One builder and one verifier subagent per work item | route (owner: `subagents.md#item-agents`) | L56–57 |
| 820–823 | Each item branches off project-main, else trunk, never off sibling item branches; Spec-split items branch at Build, incoming items at item Brief | route (owner: `branches-and-lands.md#branches`, table row "item branch", and `#never` first bullet) | L11 |
| 823–824 | Independent items may build in parallel | dropped (owner: Dispatch in this file, L29–38; `branches-and-lands.md#project-main` "Builds may run in parallel") | — |
| 824–825 | Merge-ready = DoD + Review | kept; parenthesis → sentence, links `#review` | L59 |
| 825–827 | Land each merge-ready item on project-main or trunk; do not stockpile for a batch integrate; lands one at a time | route (owner: `branches-and-lands.md#land-path`; no-stockpile also held at `#project-main` and `#never`) | L60–61 |
| 829–831 | DoD includes: acceptance on the ticket, tests/verification evidence, land path cites a ticket ID when the project uses tickets, changelog line under Unreleased, human + agent docs current, no silent scope leftover | kept; one sentence; "land path" links `branches-and-lands.md#land-path` | L45–49 |
| 832–834 | Verifier checks tone and voice of deliverables against the project's style guide (default `docs-google-style`); not agent context | kept; "(default …)" → "; if the project names none, `docs-google-style`" | L51–53 |
| 836–838 | On unexpected failure: load `debug` (default) or one of `debug-pocock` / `debug-anthropic`; then `tdd` for the cause, `verify-before-done` to prove the fix | kept; numbered steps | L69–74 |
| 838–841 | Notify landed+verified on project-main, or trunk if that was the land target; not "pushed to an item branch", not "LGTM without evidence" | dropped here, moved into the owner copy in `#definition-of-done` (writing-standard Rule owners) | L63–65 |
| 843–845 | Not a second Brief; root cause in Build is `debug` on the chosen fix; do not re-open item Brief unless the fix was the wrong kind of change (then escalate) | kept; "(then escalate)" → "; then escalate" (MQ2) | L76–78 |
| 847–849 | Skills home: skill-body diff must match the pinned SHA in `SOURCES.md`; empty SHA → no body lands; remote agent PRs still pass security intake | kept | L82–85 |
| 850 | Workers do not bypass intake, SHA pins, security Spec/Review gates | route (owner: `docs/SDLC.md#roles`); intake and SHA pins stay in L82–85 | L85 |
| 852 | `### Review` heading | kept as H2 (C1) | L87 `#review` |
| 854 | Review before the item lands on project-main (or trunk) | kept | L90 |
| 854–856 | When Review starts, **manager** transitions the item to `in_review` with `tracker-sdlc` | kept; step 1 | L92–93 |
| 856–858 | Reviewer is not the builder; same-session self-review does not count | route (owner: `subagents.md#item-agents`: reviewer "Never the builder", clean mint, Never "reviewer-reviews its own work") | L94–95 |
| 858–859 | Review is an explicit gate, not a PR; a local merge does not skip it | kept; placed first (standard 7) | L89–90 |
| 861–863 | First review: mint a clean reviewer; later rounds: resume it; no new reviewer per round; no builder transcript | route (owner: `subagents.md#item-agents` table row "reviewer" and Never) | L94–95 |
| 865–866 | Reviewer approves only if ticket + LLD **and** security gate (intake, SHA pins, trust-boundary deltas) | kept; actor **reviewer**; parenthesis → colon list (it defines the gate's scope, not examples) | L98–100 |
| 866–867 | Security at land is a gate | dropped here (owner: this file, Review step 4, which makes the security gate a condition of approval before land) | L98–100 |
| 867 | Not deferred to Monthly | route (owner: `trunk-changelog-monthly.md#monthly`) | L102 |
| 867–868 | Diff range versus project-main, or trunk if there is no project-main | kept; step 3 | L96–97 |
| 1088 | Notify only when work is landed and verified | kept; this file is the owner (`#definition-of-done`) | L63 |

Link from DoD to `#review` (L59): Review is a step named and linked in
the SDLC index Steps table, which How to read sends every reader through
first, so the name is defined before this file; the link is the one the
ticket requires, not a forward definition.

Operator clarifications (2026-09-27): none applies to these lines (no
groom-review fix, gate-reason parenthesis, review-item verdict, "a
person" or "Improvise" text).

## Meaning questions

All resolved.

- **MQ1** (old L802) "Pick an unblocked one. Do not start it.": "it"
  is the deferred item, the only item the rule stops; the unblocked item
  is picked in order to be started. New text names "the deferred
  item". Resolved from the text.
- **MQ2** (old L844–845) "unless … wrong kind of change (then
  escalate)": the new text keeps the same structure (exception to "do
  not re-open item Brief", action escalate) and picks no further
  reading; only the parenthesis became a clause. Resolved from the text.
- **MQ3** (whole file) Growth of the rewrite over the old text:
  resolved by operator 2026-09-27 (Q6). Growth is measured against the
  old SDLC section; growth up to the cap is allowed only where it makes
  rules checkable; the line target is a goal, not a blocker (Q10). Old
  83 lines, new 102; the growth is itemized under the header.

## DER-344 (G51)

Wording fixes from the integrated check DER-339. Changed lines only.
Old = project-main 44d6842; "Old L" = line there; "L" = line in the new
file. No rule changes meaning.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 5 | Open-blocker definition → route "Open blocker: defined in Tracker", linking `../SDLC.md#tracker` | F5: owner `docs/SDLC.md#tracker` (L79–81) states "a blocker not in `done` or `canceled`" | L5 |
| 84–85 | "Remote agent PRs into this repo still pass **security** intake." → route "Worker PR intake: Workers", linking `../INTAKE.md#workers`; the Roles route is kept | F5: owner `docs/INTAKE.md#workers` states the remote-agent PR security clear and the pinned-SHA match | L84–85 |
