# Rule map — `docs/sdlc/entry-brief-repo.md`

Item: DER-300 (G10, C3). A later item that edits this file appends its
own section.

Old: `docs/SDLC.md` at main 7a11696, lines 511–610 (moved verbatim by
C1, DER-298). New:
[`docs/sdlc/entry-brief-repo.md`](../../../../docs/sdlc/entry-brief-repo.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (owner named),
**DER-265**, **DER-271**. "Old L" = line in old `docs/SDLC.md`; "L" =
line in the new file. Protected rows touched: none (the route to
`branches-and-lands.md#never` links it; that file is unchanged).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 511 | Heading Entry | kept, anchor `#entry` | L3 |
| 513–514 | Classify: chunk (needs a person for taste, opinions, design talk) or item (mechanical, tactical, immediate) | kept as a condition → class table (standard 2); "a person" → "the operator, or someone the operator names in writing" (operator clarification 2026-09-27) | L5, L9–11 |
| 514–516 | Examples of item: broken build, unit failure, UI bug report until analysis shows it needs taste | kept, as "Examples:" | L12 |
| 518–519 | Unclear → a short look (reproduce? design choice?); still unclear → ask | kept, numbered if/then; "ask" links the owner of how to ask, index `#asking-the-human` | L14–17 |
| 519 | Do not implement here | kept; allowed action named: classify, or ask (standard 7) | L19 |
| 521–523 | Read-only: classify from what you were handed; no template, subagent, tracker write; classification line goes on the ticket at Brief | kept | L5–7 |
| — | Never use the item path to avoid talking to a person about a product change | route (owner: `branches-and-lands.md#never`), new line from the DER-298 review; "a person" per the clarification; allowed action named: ask them (standard 7) | L19–22 |
| 525 | Heading Brief | kept, anchor `#brief` | L23 |
| 527 | Before Plan | kept | L25 |
| — | Heading Chunk brief (C1) | kept, anchor `#chunk-brief` | L27 |
| 529–531 | Chunk Gather ↔ Refine; skip only when a confirmed brief exists; loop until the operator confirms a brief Refine did not send back; do not implement | kept; loop → numbered steps 1–4; allowed action named: write the brief | L29–30, L44–45 |
| 533–537 | Gather: load `discover-the-idea`; the skill owns interview, facts, options map, brief; read it or pack it into the gatherer prompt; do not copy or paraphrase its loop | kept, step 1; parenthesis → "or" (standard 8); allowed action named: link the skill | L32–37 |
| 539–542 | Refine: a different subagent from the gatherer; load `yagni`; question necessity; less stupid, simpler; first principles from the dump and facts, not a product template | kept, step 2 | L38–41 |
| 542–543 | Requirement dies or new fog → return to Gather with the delta (resume the gatherer) | kept, step 3; "fog" (metaphor, standard 8) → "unresolved point" (MQ3); parenthesis → own sentence | L42–43 |
| 545–547 | Mint a clean gatherer and refiner on the first pass; resume later; never one agent for both | route (owner: `subagents.md#step-agents`, which holds the whole rule since DER-306); plain route line | L48 |
| 547 | No language skill on a gather- or refine-only turn | route (owner: `language-router` `#never`, rule-owner row "no-language turns") | L49–50 |
| 549 | Plan from the confirmed brief, not a raw dump | kept; "never" with the allowed source | L52 |
| 551–552 | End of chunk Brief: cut project-main `integrate/<chunk-slug>` from trunk | kept as step 1 of a numbered list; source "from trunk" → route (owner: `branches-and-lands.md#branches`) | L54–57 |
| 552–554 | Setup check; fail → load `sdlc-onboarding`, which writes the tracker files first | kept, step 2 | L58–60 |
| 554–557 | Get the Epic (`backlog`): arrived as a ticket → use it; type differs → ask the operator to relabel; never duplicate; else **manager** files with `create` | kept, step 3 as if/then; "its type differs" → "its type is not Epic"; allowed action beside "never duplicate" | L61–65 |
| 557–562 | Onboarding ran → commit `[<epic-id>] Onboard tracker: <Tracker>` on an item branch cut from project-main; land on project-main as its own item through Review before Plan; own verifier, reviewer, security read; never a bare commit | kept, step 4.1–4.4, one action each | L66–72 |
| 563–564 | **manager** posts the Entry classification on the Epic with `comment` | kept, step 5 | L73–74 |
| — | Heading Item brief (C1) | kept, anchor `#item-brief` | L76 |
| 566–568 | Item (Task or Bug): always run unless `n/a — split from accepted Spec` (start at Build); a confirmed brief on the parent chunk does not skip item-Brief | kept; parenthesis → sentence; "parent chunk" → "the item's chunk"; "item-Brief" → "item Brief" (standard 3) | L78–81 |
| 570–571 | Step 0: cut `item/<ticket-id>-<slug>` (from the live project-main, else trunk) | kept, 0.1; source → route (owner: `branches-and-lands.md#branches`, item branch row) | L84–85 |
| 571–572 | Setup check; fail → `sdlc-onboarding` | kept, 0.2 | L86–87 |
| 572–573 | **manager** posts the Entry classification on the ticket | kept, 0.3 | L88–89 |
| 574–575 | Troubleshooter (architect hat) writes problem + proposed fix and out of scope | kept, 1.2; "architect hat" (metaphor) → "an agent in the architect role" | L95–96 |
| 575–577 | May load one of `debug` / `debug-pocock` / `debug-anthropic` through root cause / hypothesis only; not the fix phase, `tdd`, or land | kept, 1.3; allowed action named: stop there | L97–99 |
| 577–579 | The parent session may troubleshoot when already that item and not too dirty to reason; otherwise mint a clean troubleshooter | kept, 1.1 (moved first: who before what); "parent session" → "manager" (Names); "not too dirty to reason" → no other item's work and no builder, verifier or reviewer conversation (MQ1, resolved by operator 2026-09-27 (Q1)) | L91–94 |
| 580–582 | A different agent loads `yagni` only; competing fix that removes something (examples) | kept, step 2; the agent named **contrarian** (the `contrarian_id` name, rule-owner row); "different" = from the troubleshooter (MQ4); parenthesis → "Examples:" | L100–102 |
| 582–583 | Honor the existing HLD, or propose removing a part (an escalation) | kept, 2.1 | L103–104 |
| 583 | Never "delete the product" | kept, 2.2; allowed action named: remove at most a part | L105 |
| 583–584 | No honest removal path → `none — already smallest` | kept, 2.3, "honest" kept | L106 |
| 585–586 | The parent (not troubleshooter, not yagni agent) picks and records why | kept, step 3; "parent" → "manager" (Names) | L107–108 |
| 588–590 | Parent is the troubleshooter or yagni agent → mint a clean parent-pick (or ask); neither of those two chooses | kept, moved into step 3 (it decides who picks; no forward reference, standard 4); "parent-pick" → "a clean agent for the pick" (Names) | L108–109 |
| 587–588 | Ask the human if the two options look different to a user or either is a plan change | kept, step 4 condition table rows 1 and 3 (first match applies) | L110–116 |
| 590–594 | That wait blocks this issue unless AFK / headless / autonomous, then the parent may pick between two item fixes that honor the plan; other items proceed | route (owner: index `#asking-the-human`, AFK pick and wait-is-a-blocker), rows 2 and 3 (MQ5) | L115–116 |
| 596–597 | Store `contrarian_id` on the item; resume it for another round | route (owner: `subagents.md#step-agents`, which holds the whole rule since DER-306); plain route line | L118 |
| 597 | Do not add a ninth role | kept as "Use only the roles in Roles" (rule-owner replacement phrase), link index `#roles` | L118–119 |
| 599 | Heading Repo | kept, anchor `#repo` | L121 |
| 601 | Before Plan: the list below is set up for a chunk | kept as "make sure each exists; set up what is missing"; old L610's "confirm … do not reinvent" stays the item-only contrast | L123 |
| 603 | Repo or subdir exists (private as needed) | kept; "as needed" → private only when the operator says so (MQ2, resolved by operator 2026-09-27 (Q2)) | L125–126 |
| 604–606 | README / AGENTS stub so agents who need access are aware; layout: Conventions; stub template `agents-stub.md` | kept; layout link → `conventions.md#product-repo-layout` (old L413, inside the old Conventions section it linked; C1 had `#name-formats`); template path linked | L127–129 |
| 607 | **tester** watch if applicable | kept; "if applicable" → when the repo has CI or hooks (MQ2, resolved by operator 2026-09-27 (Q2)) | L130 |
| 608 | Designs live in git from onset | route (owner: `conventions.md#designs-in-git`) | L131–132 |
| 610 | Item: confirm the workspace exists; do not reinvent it | kept; allowed action named | L134 |

## Meaning questions

All resolved.

- **MQ1** (old L577–578), resolved by operator 2026-09-27 (Q1). "Not
  too dirty to reason" had no checkable form. Answer: the manager may be
  the troubleshooter only when it holds no other item's work and no
  builder, verifier or reviewer conversation. New L91–94 state it.
- **MQ2** (old L603, L607), resolved by operator 2026-09-27 (Q2).
  "(private as needed)" and "if applicable" had no checkable source.
  Answer: make the repo private only when the operator says so; add a
  **tester** watch when the repo has CI or hooks. New L125–126 and L130
  state it.
- **MQ3** (old L542), resolved from the text: "fog" is
  `discover-the-idea`'s word for what is still vague or unknown (its
  L34, L80); "unresolved point" keeps that sense.
- **MQ4** (old L580), resolved from the text: "a different agent" means
  different from the troubleshooter; `subagents.md#step-agents` says
  the troubleshooter and the contrarian must not be the same.
- **MQ5** (old L590–594), resolved from the text: the rule-owner table
  names index `#asking-the-human` the owner of the AFK pick; it also
  holds "waiting is a blocker on that issue; other items keep moving",
  so the route finishes the rule in one hop.
