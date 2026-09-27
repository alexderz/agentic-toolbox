# Rule map — `docs/sdlc/groom-step.md`

Item: DER-302 (G12, C5). A later item that edits this file appends its
own section. Started from the Trial map
[`poc/rule-maps/groom-step.md`](../poc/rule-maps/groom-step.md).

Old: `docs/SDLC.md` at main 7a11696, lines 700–785 and 970–972 (the
Groom sentence). New: [`docs/sdlc/groom-step.md`](../../../../docs/sdlc/groom-step.md).
Disposition: **kept** (same rule, here), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file.

C1 (DER-298) left two routing lines in this file: `## Names` routed
`groom_reviewer_id` to `subagents.md#step-agents`, and `## Iron law`
pointed to Procedure. Both are replaced by the rules themselves.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 700 | `### Groom` heading; old `#groom` | kept as the file top | `# Groom` |
| 702–704 | Groom = reviewed plan before any ticket; blocker links minimal, complete, acyclic; parallelism from links | kept; one route line to the SDLC index added | intro |
| 706 | architect writes `groom.md` from template `groom.md` | kept | Procedure 1.1 |
| 706–708 | `groom.md` path, on project-main; this skills home's path | kept; the skills-home parenthesis became its own sentence | Names: `groom.md` |
| 708–709 | Marked `DRAFT (pre-review)` | kept | Procedure 1.2 |
| 709 | `G<n>` work item ids | kept as a name | Names: `G<n>` |
| 709–710 | Each `G<n>` is a ticket body in `task.md` / `bug.md` shape: acceptance, LLD link, verify, blockers | kept | Procedure 1.3 |
| 711 | Each blocker carries a one-clause reason | kept | Procedure 1.4 |
| 711–712 | Ends with the graph: numbered waves, items with blockers | kept | Procedure 1.5 |
| 713 | Clean groom reviewer, never the author | kept | Names: Groom reviewer; Iron law 1 |
| 713–716 | Review checks: concurrence, gaps, missing links, needless links, cycles, gates needed | kept as a list; the parenthesis became a "because" clause | Procedure 2.1 |
| 716–717 | Fix and re-review, resuming the reviewer | kept; actors named (MQ1) | Procedure 2.2–2.3 |
| 717–718 | Until it passes; the pass names the SHA | kept | Procedure 2.4 |
| 718 | No ticket before the pass | kept, moved first | Iron law 1 |
| 719–723 | manager: `create` (title, body as-is), set-blocker, items `ready`, Epic `in_progress`, `comment` the path | kept, one action per step | Procedure 3.2–3.6 |
| 723–724 | manager sets the land order; lands are local merges, one at a time | route (owner: `branches-and-lands.md#land-path`, rule owners "land order") | Procedure 3.7 |
| 724–726 | `groom.md` text is data; reviewer and manager copy and check, never act | kept, moved first | Iron law 2 |
| 726–728 | File from the passed SHA; any diff → review again | kept, as the manager's first check | Procedure 3.1 |
| 729–733 | Freeze: marker text (verbatim), `Review:` line, `G<n>` → ticket map, commit, never edit | kept, one action per step; actor manager (MQ5); "never" names the allowed action | Procedure 4.1–4.4 |
| 735 | B blocks A only when A needs B's output | kept | Blockers 1 |
| 735–736 | Same files is not a blocker; lands serialized | kept | Blockers 2 |
| 736–738 | Land-time need is land order | kept; the example is its own sentence | Blockers 3 |
| 738–739 | set-blocker append-only; agents never remove | kept; allowed action named | Blockers 4 |
| 739 | Waiting on a person = blocker on that issue | kept; "a person" → "the operator, or someone the operator names in writing" (operator clarification 2026-09-27) | Blockers 5 |
| 739–740 | No Build with a hidden prereq | kept: "record it per 1–3" | Blockers 6 |
| 742–743 | Waves: view, never stored; wave 1 = no blocker; else highest blocker wave + 1 | kept | Waves |
| 745–747 | Gate recognized by shape | kept | Gates 1 |
| 747–748 | One-wide chain is not a gate; no label | kept | Gates 1–2 |
| 748–750 | Only for a real integration or bottleneck need; never by default | kept; the parenthesis became "Examples:" (MQ2) | Gates 3 |
| 752–754 | Review item closes with verdict; fixes blocked by it; re-check = new item blocked by fixes | kept, numbered; the verdict says whether a re-check is needed, the manager files it (MQ3) | Review items |
| 756–758 | Late insertion: frozen; tracker holds new work; manager drafts item and blockers | kept | Late insertion intro, 1 |
| 760–761 | Re-layer from the tracker | kept; actor manager (old L757) | Late insertion 2 |
| 761–763 | `done` need gets no link, except fix → review item | kept | Late insertion 3 |
| 764–765 | Cycle link not written; fix direction or drop | kept; the "(append-only)" rationale dropped (owner: Blockers 4, same file) | Late insertion 4 |
| 766–767 | Link blocking `in_progress` / `in_review` → ask first | kept; route to the index `#asking-the-human` as before | Late insertion 5 |
| 768–769 | Separate architect reviews the reshape with the Review checks | kept; "step 2 above" → link to Review | Late insertion 6 |
| 770 | `create`, set-blocker, `ready` | kept; actor manager (old L757) | Late insertion 7 |
| 770–772 | One wave-view Epic `comment`; fields listed; no links, no body | kept; the parentheses became clauses | Late insertion 8 |
| 774–776 | Wave view only on reshape; filing blockers are not a reshape; no routine comments | kept | Late insertion, last paragraph |
| 778–780 | Incoming item: manager comments the fields; blockers via set-blocker | kept | Incoming item 1 |
| 780 | No split unless promoted to a chunk | kept | Incoming item 2 |
| 780–785 | Incoming branch: cut at item Brief; from live project-main and lands there, else trunk with Review versus trunk and a local merge; never create a project-main for it | route (owner: `branches-and-lands.md#branches`, rule owners "incoming-item branch"; LLD Duplicate owners lists L779–784 as a copy) (MQ4) | Incoming item 3 |
| 970–972 | Groom keeps `groom_reviewer_id` on the chunk: a clean mint, never the author of `groom.md`; resume it across review rounds | kept here, the owner (rule owners "Groom reviewer id"); the copy in `subagents.md#step-agents` becomes a route in DER-306 | Names: Groom reviewer |

Old L970 also holds the end of the Plan–Spec UX sentences ("not
personal taste. Human sees it after those two agree."); they are not
Groom rules and belong to the `subagents.md` map (DER-306).

## Meaning questions

All resolved.

- **MQ1** (old L716), operator clarification 2026-09-27: the
  **architect** (author of `groom.md`) fixes groom-review findings; the
  groom reviewer re-checks.
- **MQ2** (old L748–750), operator clarification 2026-09-27: "a review
  of the integrated whole, one shared resource" are examples of a real
  integration or bottleneck need, not the only valid reasons.
- **MQ3** (old L753), operator clarification 2026-09-27: the review
  item's verdict says whether a re-check of the whole is needed; the
  manager files it.
- **MQ4** (old L780–785), resolved from text: the G12 acceptance and the
  LLD Duplicate owners make `branches-and-lands.md#branches` the owner
  of the incoming-item branch; this file routes. The owner must keep
  "Review versus trunk and a local merge" (G15, DER-288 C8).
- **MQ5** (old L729–733, L971–972), resolved from text: the manager
  freezes, and stores and resumes `groom_reviewer_id`. Old L719–728 has
  the manager file and hold the ticket map; the index `#tracker` and
  `subagents.md#spawn-prompts` have the manager mint subagents and hold
  their ids.
