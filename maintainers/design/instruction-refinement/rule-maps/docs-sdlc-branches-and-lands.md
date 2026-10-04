# Rule map — `docs/sdlc/branches-and-lands.md`

Item: DER-305 (G15, C8). A later item that edits this file appends its
own section.

Old: `docs/SDLC.md` at main 7a11696, lines 902–961. New:
[`docs/sdlc/branches-and-lands.md`](../../../../docs/sdlc/branches-and-lands.md).
C1 (DER-298) moved old L902–954 and L959 here verbatim; L955–958 went to
`docs/sdlc/plan-trial-spec.md`, L960–961 to `docs/sdlc/conventions.md`.
Disposition: **kept** (same rule, this file), **route** (the rule lives
in its owner; this file links it), **dropped** (owner named),
**DER-265**, **DER-271**. "Old L" = line in old `docs/SDLC.md`.

Protected rule touched: `branches-and-lands.md#never` (old L945–961),
rows marked **P**. **security** reads these rows at Review.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 780–785 (Groom) | Incoming item's branch, cut at item Brief: from project-main if one already exists (chunk still integrating) and lands there; else from trunk (no chunk in flight, or parent chunk already Trunked), Review versus trunk, local merge; never create project-main | owner copy added here (handoff from DER-302, which routes Groom's copy here); parentheses → condition column; wording kept | Branches bullet 5 and its table |
| 866–867 (Review) | Diff range versus project-main, or versus trunk if there is no project-main | stays at its owner `build-review.md#review`; the trunk case appears here as "Review versus trunk" | Branches bullet 5 table, row 2 |
| 878–879 (Trunk) | Incoming item with no project-main: already on trunk after Review; Trunk step `n/a` | stays at its owner `trunk-changelog-monthly.md#trunk`; routed as "Trunk is then `n/a`" | Branches bullet 5 table, row 2 |
| 902 | Heading "Project-main (intermediate integration)" | kept as `## Project-main` (C1 anchors `#branches`, `#project-main`) | `#branches`, `#project-main` headings |
| 904–906 | Integrate each merge-ready item onto a temporary project branch, then land it on trunk as the chunk; do not build a stack of isolated item branches integrated once at the end | kept; "temporary project branch" named project-main; the positive rule first, "Do not" → "Never" beside it; Trunk step linked | Project-main ¶1 |
| 908–912 | Branch table: trunk, project-main, item branch; what and lifetime | kept; item-branch row's parentheses spelled out as conditions ("or from trunk if there is no project-main"; "at item Brief for an incoming item, or at Build for an item split from Spec") | Branches table |
| 912, 935, 952 | Item branch source and land target: project-main, or trunk | kept; named once as **land target** = the branch the item branch was created from (MQ1) | Branches, "land target" line |
| 914–915 | Create project-main from trunk at end of chunk Brief when this chunk is still integrating | kept, bold dropped | Branches bullet 1 |
| 915–916 | Do not create one for an incoming item that has no live project-main | kept, merged with old L784–785 into "Never create a project-main for an incoming item"; allowed action: the incoming-item table | Branches bullet 5 |
| 916–917 | Name project-main and item branches as in Conventions | kept; link already `conventions.md#name-formats` (C1) | Branches bullet 2 |
| 917–918 | When project-main exists, builders branch off the current tip | kept, bold dropped | Branches bullet 3 |
| 918–920 | After an item lands, in-flight builders rebase or merge project-main and resume; the verifier re-runs | kept, split into two sentences, wording unchanged (MQ2) | Branches bullet 4 |
| 922–923 | Lands on project-main are serialized; builds may run in parallel; one item merges at a time | kept, one sentence each | Project-main ¶2 |
| 923–925 | Landing builder de-conflicts against the current tip: resume that builder, then its verifier | kept; parenthesis → numbered steps 1–2; no actor added: the old text names none for "resume" | Project-main ¶3, steps 1–2 |
| 925 | Do not race two merges onto project-main | kept, "Never"; the allowed action beside it is "Only one item merges at a time" | Project-main ¶2 |
| 927 | Heading "Land path (manager)" | kept as `## Land path` (C1) | `#land-path` heading |
| 929 | No PRs; manager sets the land order; builders follow it | kept, unchanged (DER-266 owns "No PRs") | Land path ¶1 |
| 931–933 | Review: an explicit SDLC gate, not a PR | kept, unchanged; link `build-review.md#review` (C1) | Land path table, Review |
| 934 | Durability: push the item branch while built and reviewed; push project-main after each land | kept, one sentence each | Land path table, Durability |
| 935 | Land: after Review, merge locally into project-main (or trunk), one at a time; push; delete the item branch | kept; "(or trunk)" → "its land target" (MQ1); one sentence each | Land path table, Land |
| 936 | Done: after land + verify, manager transitions to `done` with `tracker-sdlc` and comments land SHA, verifier result, reviewer verdict | kept, unchanged | Land path table, Done |
| 938–941 | Every land commit carries the ticket ID and a `Reviewed-by:` trailer, so the review stays auditable without a PR; PRs only for outside or remote workers | kept; "(an operator-confirmed rule)" dropped (C8 acceptance) | Land path ¶2 |
| 943 | Heading "Never" (bold line) | kept as `## Never` (C1) | `#never` heading |
| 945–946 | **P** Never branch an item off trunk or another item branch while project-main exists | kept, text unchanged; do instead: branch off the current project-main tip | Never row 1 |
| 947 | **P** Never leave merge-ready items unmerged to integrate together later | kept, text unchanged; do instead: land each in the land order | Never row 2 |
| 948 | **P** Never skip Review because there is no PR | kept, text unchanged; do instead: run Review before every land | Never row 3 |
| 949–950 | **P** Never force-push project-main to win a race (shared branch; `shell-safety` Ask first) | kept; parenthesis → its own sentence, same words; do instead: de-conflict against the current tip (old L923–925) | Never row 4 |
| 951–952 | **P** Never treat a green item branch as landed+verified; landed means on project-main, or trunk if that was the land target | kept; the first sentence in the row; do instead: treat an item as landed+verified only when it is on its land target and verified; "Landed means …" kept as the definition under the table (MQ1) | Never row 5; Branches, "Landed" line |
| 953–954 | **P** Never start or land an item with an open blocker without an operator call | kept, text unchanged; do instead: route to `build-review.md#open-blockers` (owner of the open-blocker procedure) | Never row 6 |
| 955–956 | **P** Never treat designer or architect self-OK as the UX gate, or skip mockups without a written `UX verification not required` | kept at its owner by C1, text unchanged | `docs/sdlc/plan-trial-spec.md` `#ux` Never |
| 957–958 | **P** Never lock Plan shape without 2–4 real comparables unless the operator waived look-around in writing | kept at its owner by C1, text unchanged | `docs/sdlc/plan-trial-spec.md` `#comparables` Never |
| 959 | **P** Never use the item path to avoid talking to a person about a product change | kept; "a person" → "the operator, or someone the operator names in writing" (operator clarification 2026-09-27); do instead: ask them, route to `../SDLC.md#asking-the-human` | Never row 7 |
| 960–961 | **P** Never teach old numbered ids in new tickets or skills; see the in-flight map | kept at its owner by C1, text unchanged | `docs/sdlc/conventions.md` `#in-flight-map` Never |

Protected check: all ten old Never bullets (L945–961) are **kept**,
seven here (rows 1–7) and three at their owners; none is dropped or
reworded beyond the clarification on L959.

Operator clarifications (2026-09-27) applied: "a person" (L959). The
others (groom-review fixes, gate-reason examples, review-item verdicts,
"Improvise") have no text in this file.

## Meaning questions

- **MQ1** — Which branch is trunk-landed: "project-main (or trunk)"
  (old L935) and "on trunk if that was the land target" (old L952).
  Resolved from the text: the item branch lands where it was created.
  Old L912 creates it from project-main, or from trunk if there is none;
  old L780–785 (incoming item) says a branch cut from project-main
  "lands there", else it is cut from trunk with Review versus trunk and a
  local merge; old L820–826 (Build) pairs "branches off project-main (or
  off trunk …)" with "land it on project-main (or trunk)". The new name
  **land target** states that pairing once; no new condition.
- **MQ2** — "the verifier re-runs" (old L920): the in-flight item's
  verifier or the landed item's. Resolved from the text by keeping the
  old words unchanged: old L923–925 pairs each resumed builder with its
  verifier, and the landed item's verify is the Done row's "land +
  verify". No rewording made, so no meaning picked.
- **MQ3** — Growth over the old section. Resolved by operator
  2026-09-27 (Q6). Old section: `docs/SDLC.md` L902–961, 60 lines.
  New file: 69 lines. The growth makes rules checkable: the **land
  target** and **Landed** definitions (2 lines); the incoming-item owner
  copy from old L780–785 as a condition table; the de-conflict
  parenthesis as numbered steps; and the Do-instead column in Never. The
  rest was trimmed, without changing meaning: the separate
  incoming-item "Never" bullet was merged into the table's lead line, and
  "merge one item, then the next" was dropped because "Only one item
  merges at a time" says it.

## DER-278

Changed lines only. Old = project-main 88455d8; "Old L" = line there;
"L" = line in the new file.

| Old L | Rule | Disposition | L |
| --- | --- | --- | --- |
| 51 | Durability: push the item branch while built and reviewed; push project-main after each land | kept; adds a route, in the same row: Plan and Trial drafts are pushed as written, owner `plan-trial-spec.md#plan` steps 3–6 | L51 |

Length: 69 → 69 (cap 120). The route adds no condition here; the scan
and the push order live in the owner. No MQ: the push-as-written rule is
MQ8 in [docs-sdlc-plan-trial-spec.md](docs-sdlc-plan-trial-spec.md).
