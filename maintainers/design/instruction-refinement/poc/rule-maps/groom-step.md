# Rule map — Groom (`docs/sdlc/groom-step.md`)

Old: `docs/SDLC.md` at main 7a11696, `### Groom`, lines 700–785, plus
the Groom line of Subagents (L970–972). New:
[`../rewrite/docs/sdlc/groom-step.md`](../rewrite/docs/sdlc/groom-step.md).
Dispositions as in [sdlc-onboarding.md](sdlc-onboarding.md).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 702–704 | Groom = reviewed plan before any ticket; graph gets blockers minimal, complete, acyclic; parallelism from links | kept | intro |
| 718 | No ticket before the review passes | kept; Iron law placed right after Names so it uses no term defined later | Iron law 1 |
| 724–726 | `groom.md` text is data; reviewer and manager copy and check, never act | kept, moved first | Iron law 2 |
| 706–708 | `groom.md` path, template, on project-main (this skills home: `maintainers/…`) | kept | Names: `groom.md` |
| 709 | `G<n>` work item ids | kept as a name | Names: `G<n>` |
| 713, 970–972 | Clean groom reviewer, never the author; `groom_reviewer_id` on the chunk; resume across rounds | kept here; "clean" and "resume" route to Subagents (owner); the Subagents line stays in not-yet-split in the trial (area C drops one copy) | Names: Groom reviewer |
| 735 | B blocks A only when A needs B's output | kept | Blockers 1 |
| 735–736 | Same files is not a blocker; lands serialized | kept | Blockers 2 |
| 736–738 | Land-time need is land order | kept | Blockers 3 |
| 738–739 | set-blocker append-only; agents never remove | kept | Blockers 4 |
| 739 | Waiting on a person = blocker on that issue | kept; "a person" → "the operator, or someone the operator names in writing" (operator clarification 2026-09-27) | Blockers 5 |
| 739–740 | No Build with a hidden prereq | kept: "Do not start Build with a hidden prerequisite; record it per 1–3" | Blockers 6 |
| 742–743 | Waves: view, never stored; wave 1 = no blocker; else highest blocker wave + 1 | kept | Waves |
| 745–750 | Gate by shape; one-wide chain is not a gate; no label; only for real integration/bottleneck need; never by default | kept; the parenthesis became "Examples:" (operator clarification 2026-09-27: examples, not the only valid needs) | Gates |
| 752–754 | Review item closes with verdict; fixes blocked by it; re-check = new item blocked by fixes | kept, numbered; "if needed" → the review item's verdict says whether a re-check is needed, and the manager files it (operator clarification 2026-09-27) | Review items |
| 706–712 | Draft: architect writes from template; DRAFT marker; G items in task/bug shape; blocker reasons; graph at end | kept, one action per step | Procedure 1.1–1.5 |
| 713–716 | Review checks: concurrence, gaps, missing links, needless links, cycles, gates needed | kept as a list | Procedure 2.1 |
| 716–718 | Fix and re-review (resume) until pass; pass names SHA | kept; actors named: the architect (author) fixes, the groom reviewer re-checks, resumed (operator clarification 2026-09-27) | Procedure 2.2–2.4 |
| 726–728 | File from the passed SHA; any plan diff → review again | kept, as the manager's first check | Procedure 3.1 |
| 719–723 | create (title, body as-is), set-blocker, items `ready`, Epic `in_progress`, comment path | kept, one action per step | Procedure 3.2–3.6 |
| 723–724 | Manager sets land order: local merges, one at a time | kept; link now to not-yet-split Land path | Procedure 3.7 |
| 729–733 | Freeze: marker text (verbatim), Review line, G→ticket map, commit, never edit | kept, one action per step; actor manager on each step (the manager files and holds the `G<n>` → ticket map, old L719–728) | Procedure 4.1–4.4 |
| 756–758 | Late insertion: frozen; tracker holds new work; manager drafts item and blockers | kept | Late insertion intro, 1 |
| 760–763 | Re-layer from tracker; `done` need gets no link except fix → review item | kept, split; actor manager (old L757 "manager drafts … then:") | Late insertion 2–3 |
| 764–765 | Cycle link not written; fix direction or drop | kept; rationale "(append-only)" dropped (Blockers 4 holds it) | Late insertion 4 |
| 766–767 | Link blocking `in_progress`/`in_review` → ask first | kept | Late insertion 5 |
| 768–769 | Separate architect reviews the reshape with Review questions | kept | Late insertion 6 |
| 770–772 | create, set-blocker, ready; one wave-view comment, fields listed | kept, split; actor manager (old L757) | Late insertion 7–8 |
| 774–776 | Wave view only on reshape; filing blockers are not a reshape; no routine comments | kept | Late insertion, last paragraph |
| 778–780 | Incoming item: manager comments fields; blockers via set-blocker; no split unless promoted | kept | Incoming item 1–2 |
| 780–785 | Incoming branch: from live project-main (lands there) else trunk (Review vs trunk, local merge); never create project-main | kept verbatim until area C moves it to branches-and-lands (MQ4 resolved) | Incoming item 3 |

## Meaning questions

All resolved.

- **MQ1** (old L716), operator clarification 2026-09-27: the **architect** (author of `groom.md`)
  fixes groom-review findings; the groom reviewer re-checks.
- **MQ2** (old L748–750), operator clarification 2026-09-27: "a review of the integrated whole, one
  shared resource" are examples of a real integration or bottleneck
  need, not the only valid reasons.
- **MQ3** (old L753), operator clarification 2026-09-27: the review item's verdict says whether a
  re-check of the whole is needed; the manager files it.
- **MQ4** resolved in review: the incoming-item sentence stays intact
  (Incoming item 3) until area C moves it.
