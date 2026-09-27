Old: skills/pr-review/SKILL.md at main 7a11696, lines 1–121. New: skills/pr-review/SKILL.md.

Light pass (vendor-derived): change map, changed lines only. Unlisted
old lines are unchanged. Key: **kept**, **route**, **dropped** (owner
named).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 15–19 | Reviewer is not the builder; mint a clean reviewer with crafted inputs; resume it on later rounds; no new reviewer each round; never the builder's transcript | route → `docs/sdlc/subagents.md#item-agents`; crafted inputs stay in Always step 2 | L18–19 |
| 19–21 | "See docs/SDLC.md (Project-main, Subagents per work item)": prose section names of the pre-split SDLC | kept, links fixed to `docs/sdlc/build-review.md#review` and `docs/sdlc/branches-and-lands.md#project-main`; Subagents per work item is the route above | L15–17 |
| 26–28 | Iron law tail: first review is a clean reviewer with crafted inputs, never the builder's chat history; later reviews resume that reviewer | route → `docs/sdlc/subagents.md#item-agents`, via the L18–19 route; Iron law first line kept | L18–19; L23 |
| 45 | Act: Critical/Important before merge | kept; "merge" → "land", the SDLC name for the gate | L40 |

`SOURCES.md` L21 (`pr-review` row): Notes cell appends `Wording edit
DER-288, pins unchanged; security-cleared 2026-09-27.` Upstream, SHA
and License cells unchanged.

## Meaning questions

None. Out of scope, not changed: the Roles row gives **architect**
"Requesting a clean reviewer"; the owner, `subagents.md#item-agents`,
gives the item-agent ids to the manager session. Changing a role is a
meaning shift, so this pass leaves it.

## DER-344 (G51)

Wording fixes from the integrated check DER-339. Changed lines only.
Old = project-main 44d6842; "Old L" = line there; "L" = line in the new
file. No rule changes meaning.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 34–35 | "send the new range and what changed — do not re-paste the spec" → "with the new range:" + route [Item agents](../../../../docs/sdlc/subagents.md#item-agents) | F5: owner `subagents.md#item-agents` states resume `reviewer_id`, send what changed, never re-paste the spec | L34–35 |

SOURCES row unchanged.
