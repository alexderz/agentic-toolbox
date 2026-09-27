# Rule map — `docs/sdlc/subagents.md`

Item: DER-306 (G16, C9). A later item that edits this file appends its
own section.

Old: `docs/SDLC.md` at main 7a11696, lines 963–1087; plus the Brief
step-agent copies L545–547 and L596–597, whose owner is this file
(DER-300 routes them here). New:
[`docs/sdlc/subagents.md`](../../../../docs/sdlc/subagents.md).
C1 (DER-298) moved old L963–1087 here verbatim and added the headings
`## Step agents`, `## Item agents`, `## Fallback`, `## Tracker writes`,
`## Writable worktree`; old L1088 went to
`docs/sdlc/build-review.md#definition-of-done`.
Disposition: **kept** (same rule, this file), **route** (the rule lives
in its owner; this file links it), **dropped** (owner named),
**DER-265**, **DER-271**. "Old L" = line in old `docs/SDLC.md`.

Protected rule touched: `subagents.md#tracker-writes` (old L1025–1027),
rows marked **P**. **security** reads these rows at Review.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 545–546 | Mint a clean gatherer and a clean refiner on a chunk's first pass; resume those ids on later rounds; never the same agent for both | kept here as owner (copy in `entry-brief-repo.md#chunk-brief` → route, DER-300); "Never the same agent for both" → "Never use the same agent for both" | Step agents, Chunk Brief |
| 547 | No language skill on a gather- or refine-only turn | not moved; stays in `entry-brief-repo.md#chunk-brief` (DER-300) | — |
| 596–597 | Store `contrarian_id` (the yagni agent) on the item; resume it if the debate has another round | kept here as owner (copy in `entry-brief-repo.md#item-brief` → route, DER-300); "the debate has another round" → "the fix-vs-removal choice gets another round" (the debate is item Brief steps 1–3: troubleshooter's fix vs the contrarian's removal) | Step agents, Incoming item Brief |
| 597 | Do not add a ninth role | not moved; roles owner `docs/SDLC.md#roles` (DER-300, C2) | — |
| 963 | Heading "Subagents per work item" | kept as `## Item agents` and `## Step agents` (C1 anchors `#item-agents`, `#step-agents`); Item agents placed first so Clean and Resume are defined before Step agents uses them (standard 4) | `#item-agents`, `#step-agents` |
| 965–967 | Chunk Brief keeps `gatherer_id`, `refiner_id` on the chunk; not the same agent; resume across Gather ↔ Refine; see Brief | kept; merged with old L545–546 into one bullet; link `entry-brief-repo.md#brief` (C1) | Step agents, Chunk Brief |
| 967–969 | Plan–Spec keeps `designer_id`, `ux_reviewer_id` on the chunk; not each other, not the architect; resume across UX and mockup rounds | kept; the parenthesis → a sentence | Step agents, Plan–Spec |
| 969–970 | UX reviewer checks requirements only, not taste; the human sees it after the two agree | route (owner: `docs/sdlc/plan-trial-spec.md#ux`, which holds the loop "against the written requirements … not the reviewer's taste" and "then the operator accepts") | Step agents, Plan–Spec, last sentence |
| 970–972 | Groom keeps `groom_reviewer_id` on the chunk: clean mint, never the author of `groom.md`; resume across review rounds | route (owner: `docs/sdlc/groom-step.md#names`, per the writing standard's Rule owners; DER-302 carries the text there) | Step agents, Groom |
| 974 | Incoming item Brief keeps `contrarian_id` (yagni agent) | kept; one name, **contrarian** (matches the id and DER-300), defined in Item agents before its first use (old L1006) as "the agent that loads `yagni` at item Brief" (`entry-brief-repo.md#item-brief` step 2); "yagni agent" replaced everywhere | Item agents, **Contrarian**; Step agents, Incoming item Brief |
| 975 | The troubleshooter may be the parent | route (owner: `entry-brief-repo.md#item-brief` step 1, which holds the troubleshooter and the condition under which the manager session may do that work) | Step agents, Incoming item Brief |
| 975–976 | Troubleshooter and contrarian differ; neither is the item's builder, verifier, or reviewer | kept; "yagni agent" → "contrarian" | Step agents, Incoming item Brief |
| 978–979 | Work item = one Task, Bug, or outside/remote PR; one implementable unit | kept, as a name line | Item agents, **Work item** |
| — | Mint = start a new subagent | new name line (standard 3); the word is used unchanged from old L985–987, L1008, L1036 | Item agents, **Mint** |
| 979–981 | Orchestrator (manager session, parent agent, or workflow) keeps `builder_id`, `verifier_id`; Review adds `reviewer_id`; the three are not the same agent | kept; "orchestrator (manager session, parent agent, or workflow)" → "the manager, a session or a workflow" (banned names; MQ1) | Item agents ¶1 |
| 983–987 | Role table: builder, verifier, reviewer; first pass mint clean, later passes resume | kept, unchanged | Item agents table |
| 989–990 | Clean = empty transcript except the crafted task; do not seed with another role's chat | kept, as a name line; "Do not" → "Never" | Item agents, **Clean** |
| 991 | Do not use the orchestrator as the builder or verifier | kept; merged with old L1006 into one Never bullet (same actor, same roles) | Item agents, Never 5 |
| 993–996 | Resume = continue that subagent by id; it already read the item; send delta; do not re-paste spec, tree, logs | kept, as a name line; the allowed action first, then "Never re-paste" | Item agents, **Resume** |
| 998 | "Never" label | kept | Item agents, Never |
| 1000 | Builder verifies or reviews its own work as the only gate | kept; allowed action beside it: the verifier and the reviewer are other agents (old L981) | Item agents, Never 1 |
| 1001 | Verifier or reviewer gets the builder's transcript as memory | kept; allowed action: mint them clean (old L989–990) | Item agents, Never 2 |
| 1002–1003 | An item's builder, verifier, reviewer reused on a different item | kept; allowed action: mint clean agents for that item | Item agents, Never 3 |
| 1004–1005 | New builder or verifier minted each Build loop while the previous is resumable | kept; allowed action: resume it | Item agents, Never 4 |
| 1006 | Parent is the yagni agent, builder, or verifier of that item | kept; "Parent" → "manager" (MQ1), "yagni agent" → "contrarian"; allowed action: mint a clean subagent for the role | Item agents, Never 5 |
| 1008–1011 | Fallback: resume fails (expired, quota, host error) → mint a clean agent of the same role, replace the id, short handoff (paths, decisions, open failures), not the other role's transcript | kept; condition → action table, one action per step; the dash clause → its own Never sentence with the allowed action | Fallback row 1; Fallback last ¶ |
| 1013–1015 | Overflow: resumed transcript too large to be useful → replace that role's agent the same way; do not rotate roles to save context | kept; condition wording unchanged (Note N1); "Do not" → "Never" with the allowed action | Fallback row 2; Fallback last ¶ |
| 1017–1018 | Orchestrators that spawn in parallel mint one pair per item, not per loop; independent items get independent pairs | kept; "Orchestrators" → "A manager" (banned name); moved to Item agents | Item agents ¶ after the table |
| 1020–1023 | Item grain: no gatherer, designer, UX reviewer for a no-screen incoming item; yagni agent at Brief; builder, verifier, reviewer as usual; security if a trust boundary moves | kept; moved to Step agents; "yagni agent" → "contrarian"; the fragment "Security if a trust boundary moves" → "Add **security** if a trust boundary moves" (actor and condition unchanged) | Step agents, last ¶ |
| 1025–1026 | **P** Only the orchestrator writes to the tracker (see Hierarchy) | kept; "orchestrator" → "**manager**" (banned name); the old link, now `../SDLC.md#tracker` (C1), makes the line the route to the owner `docs/SDLC.md#tracker` | Tracker writes, L1 |
| 1026–1027 | **P** Builder, verifier, reviewer prompts carry no tracker-writing instructions; those roles report | kept, unchanged | Tracker writes, L2–3 |
| 1029–1032 | Writable worktree: some hosts pin it to the orchestrator's worktree; then one item worktree writable; other builders write to scratch for the orchestrator to commit, or items run in sequence | kept; "orchestrator" → "manager"; one sentence split in two | Writable worktree |
| 1034 | Heading "Spawn prompts (pack vs point)" | kept as `## Spawn prompts` (C1) | `#spawn-prompts` |
| 1036–1037 | On each mint the manager picks the cheaper prompt; no default is always right | kept, reworded per LLD C9: the manager picks the mode by "the manager holds the bodies and the child needs them → Pack; else → Point"; "cheaper" and "no default" are replaced by that rule (MQ2) | Spawn prompts ¶1 |
| 1039–1042 | Mode table: Pack, Point; prompt; what the child does; at most one language-family skill | kept, unchanged (curly quotes straightened) | Spawn prompts table |
| 1044–1045 | Pack when the parent has the bodies, the child uses most of them, and a re-read costs more than inlining | kept, reworded per LLD C9 as the Pack condition (MQ2) | Spawn prompts ¶1 |
| 1046–1053 | Typical pack mints and their skills; builder gets no `tracker-sdlc`, no tracker writes; UX reviewer review loop only | kept; parentheses → clauses; "item yagni-agent" → "contrarian" | Spawn prompts, Typical pack mints |
| 1055–1057 | Point when several skills or servers might apply, the parent lacks the bodies, or a thin slice matters | kept, reworded per LLD C9 as "else → Point" (MQ2) | Spawn prompts ¶1 |
| 1057 | Do not load a catalog into the parent just to pack it | kept; "parent" → "manager" (MQ1); allowed action: point instead | Spawn prompts, Never 1 |
| 1059–1061 | Resume is delta-only; no re-pack; a new skill or tool → pack that slice or name it | kept; "If … required" → "→" | Spawn prompts, Resume ¶ |
| 1063 | "Never" label | kept | Spawn prompts, Never |
| 1065–1066 | Never pack the language catalog, every MCP server, or other roles' skills "just in case" | kept; allowed action: pack only what the child needs | Spawn prompts, Never 2 |
| 1067 | Never pack a skill and also tell the child to read it | kept; allowed action: tell it not to reload (old L1041) | Spawn prompts, Never 3 |
| 1068–1069 | Never point at "load whatever you need" when the parent knows the ids | kept; "parent" → "manager" (MQ1); allowed action: name those ids | Spawn prompts, Never 4 |
| 1071 | Heading "Workers" | kept | `#workers` |
| 1073–1077 | Workers table: remote agent, local CLI (`grok-acp` when the operator picks it), local mirror | kept, unchanged | Workers table |
| 1079–1080 | **architect** adversarial-reviews other agents' tools when the work needs it | kept, unchanged (Note N1) | Workers ¶1 |
| 1080–1082 | **tester** owns CI/hooks; **security** owns Spec trust-boundary and Review gates and skill intake; **manager** after-acts the board, does not bless before ship | route (owner: `docs/SDLC.md#roles`; its Roles table holds each job) | Workers ¶1, last sentence |
| 1084 | Workers do not bypass security | route (owner: `docs/SDLC.md#roles`) | Workers ¶2 |
| 1084–1086 | A remote or local agent PR into this skills home still needs intake and SHA-pin match; worker choice is not an exemption | route (owner: `docs/INTAKE.md`: its intro says workers, local CLIs included, do not bypass intake; `#workers` holds the security clear, "not an exemption", and the pinned-SHA match) | Workers ¶2 |

Acceptance notes:

- Tracker-writer copy: old L1025–1026, now the route line above
  (kept and routed). The builder pack line "no tracker writes" (old
  L1051) is pack content for that mint and stays.
- Security copies: old L1080–1086 → routes.
- Landed+verified copy: none in this file since C1; old L1088 sits in
  the owner `docs/sdlc/build-review.md#definition-of-done`.
- Land order: this file routes the groom reviewer to
  `groom-step.md#names`, whose text DER-302 adds. Land DER-302 before
  or with this item; until then `groom-step.md#names` routes back here.

## Meaning questions

All resolved.

- **MQ1** (old L979, L991, L1006, L1017, L1044, L1056–1057,
  L1069), resolved from the text: "parent", "parent agent" and
  "orchestrator" name the manager. Old L979 lists the parent agent as a
  form of the orchestrator, and old L1036 writes "the orchestrator
  (**manager**)"; the writing standard's Names table maps these to
  `manager`. "Or workflow" is kept as "a session or a workflow".
- **MQ2** (old L1036–1037, L1044–1045, L1055–1057), resolved by the
  accepted LLD, work area C9: pack vs point → "the manager holds the
  bodies and the child needs them: pack; else point".
- **MQ3** (old L970–972), resolved by the writing standard's Rule
  owners: the groom reviewer id is owned by `groom-step.md#names`;
  this file keeps a one-line route.

Notes, not MQs (one reading each; wording kept):

- **N1** Old L1013 "too large to be useful" and old L1079 "when the
  work needs it" are not checkable conditions (standard 2). Each has one
  reading. A checkable threshold would change the rule, so the wording
  stays; the operator may set one later.
