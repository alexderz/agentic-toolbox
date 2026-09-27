# Rule map — `docs/sdlc/conventions.md`

Item: DER-307 (C10).

Old: `docs/SDLC.md` at main 7a11696, lines 385–463, 488–509, 960–961,
1090–1095 (moved verbatim into `docs/sdlc/conventions.md` by C1, DER-298).
New: [`docs/sdlc/conventions.md`](../../../../docs/sdlc/conventions.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in old `docs/SDLC.md`; "L" = line
in the new file.

Protected row touched: branches-and-lands `#never` (old L960–961 is in
L945–961); kept here. **security** reads it at Review. Operator
clarifications (2026-09-27): none of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 385 | Heading "Conventions (optional, recommended)" | kept, as the file title (C1) | L1 |
| 387–389 | Follow these unless the repo has a rule; do not rename mid-chunk to match; consistency beats a prettier local scheme | kept; first two sentences verbatim; third → imperative "Prefer consistency … over a prettier local scheme" | L3–4 |
| 391 | Heading "Names" | kept as "Name formats" (C1 heading, anchor `#name-formats`) | L6 |
| 393–401 | Name-format table | kept; Role row "the names in this SDLC" → link `[Roles](../SDLC.md#roles)`; Step link kept (`../SDLC.md#steps`) | L8–16 |
| 403–405 | Cite the ticket ID on item branch, merge commit, changelog line when tickets are used; else omit the ID, keep the rest | kept, as if/then | L18–19 |
| 407–408 | Commits: imperative subject, one idea; `[ticket-id] subject` when tickets exist | kept, imperative + if/then; heading `#commits` (C1) | L21–24 |
| 410–411 | Cite the step name; old numbers only in the in-flight map | kept; moved into `#in-flight-map` so no forward reference (standard 4); "the in-flight map" → "this table" | L80 |
| 413–428 | Heading and product repo layout block | kept, block verbatim | L26–41 |
| 430–433 | `.agents/design/` is data, not loaded; only loaded file under `.agents/` is the tracker `SKILL.md` `## Tracker` names; no credentials, internal hostnames, private workspace URLs | kept; first two → imperative; the third sentence verbatim (MQ1) | L43–45 |
| 435–436 | Copy shapes from `sdlc-artifacts` templates; do not invent a second outline | kept; "Do not" → "Never" beside the allowed action | L47–48 |
| 438–440 | This skills home stays `skills/<id>/SKILL.md`, `SOURCES.md` and "this file"; build notes and design records under `maintainers/`; tests follow the language skill, not a second layout | kept; "this file" → "the SDLC (`SDLC.md`, `docs/sdlc/`)" (MQ2); rest → imperative | L48–51 |
| 442 | Heading "Changelog and connection" | kept (`#changelog-and-connection`) | L53 |
| 444–445 | `CHANGELOG.md` at repo root; newest first; sections Added, Changed, Fixed, Removed, skip empty | kept | L55–56 |
| 447–453 | Board, git and changelog agree; table | kept, table verbatim | L56–62 |
| 455 | Build land: one line under `## Unreleased` | kept, imperative | L64 |
| 456–458 | Changelog step: promote Unreleased into a dated chunk heading or the repo's version scheme; link tickets and the Trunk merge | kept; parenthesis → plain "or" (no condition added) | L65–67 |
| 460–462 | **manager** transitions the item `done` with `tracker-sdlc` when landed+verified on project-main, or on trunk if there was no project-main | route (owner: `docs/sdlc/branches-and-lands.md#land-path`: Land row "(or trunk)", Done row "After land + verify, **manager** transitions … `done` with `tracker-sdlc`"; `#never` "Landed means on project-main (or on trunk …)") | L68–69 |
| 462–463 | Do not mark the chunk shipped until Trunk | kept verbatim, "Trunk" linked to `trunk-changelog-monthly.md#trunk` (MQ3) | L69–70 |
| 488 | Heading "In-flight map (old numbers)" | kept as "In-flight map" (C1, `#in-flight-map`) | L78 |
| 490–492 | Keep an already-cited Stage number's meaning until the item lands; do not re-read a new heading as your step | kept | L81–83 |
| 494–507 | Stage table | kept verbatim (open tickets still cite Stage numbers; LLD "The Stage table stays") | L85–98 |
| 509 | Delete this table once tickets that still say those numbers have landed | kept, checkable form per manager clarification (2026-09-27, per HLD hazards "Stage map"): "Delete this table when no open ticket cites a Stage number; until then keep it." (MQ4) | L100 |
| 960–961 | Never teach old numbered ids in new tickets or skills; see the in-flight map | kept (protected `#never` row), in `#in-flight-map`; the "see" link dropped as a self-link; allowed action "Cite the step name" beside it | L80–81 |
| 1090 | Heading "Git designs from onset" | kept as "Designs in git" (C1, `#designs-in-git`); this file is the owner | L72 |
| 1092–1093 | HLD, LLD, PoC notes, decisions, changelogs and this SDLC land in git from Repo; paths link | kept; "land in **git** from Repo" → "Keep … in **git** from Repo on"; paths link → `#product-repo-layout` (MQ5) | L74–75 |
| 1094–1095 | A local or vendor mirror may follow; do not treat a mirror as an independent write path for designs | kept; "Do not" → "never" | L75–76 |

## Meaning questions

- **MQ1** — Old L432–433 "No credentials, internal hostnames, or private
  workspace URLs" can scope to `.agents/` files or to every layout file.
  Resolved from the text: the sentence stays verbatim in the same
  paragraph, so no reading is chosen.
- **MQ2** — Old L438 "this file": in old `docs/SDLC.md` it named the SDLC,
  which C1 split into the index and `docs/sdlc/`. After C1 it read as
  `conventions.md`. Resolved from the text: "the SDLC" with both paths
  restores the old meaning.
- **MQ3** — Routing old L460–463 must not drop "or on trunk" or the chunk
  rule. Resolved from the text: the land-path owner carries the trunk
  target (Land row, `#never`); the chunk sentence stays here verbatim.
- **MQ4** — Old L509 is a self-deleting condition (standard 8), and its
  trigger ("tickets … have landed") is not checkable as written.
  Resolved by manager clarification (2026-09-27, per HLD hazards: "Stage
  map → no open ticket cites a Stage number: delete as it says; else
  ask"): "Delete this table when no open ticket cites a Stage number;
  until then keep it." The table stays; only the trigger is made
  checkable.
- **MQ5** — Old L1093 linked the whole Conventions section; the paths it
  names are in the product repo layout. Resolved from the text: the link
  narrows to `#product-repo-layout`, same target content.
