# Rule map — `skills/sdlc/references/subagents.md`

Item: DER-734 (A2 of DER-712).

Old: `docs/sdlc/subagents.md` at main c26f424, lines 1–136.
New: [`skills/sdlc/references/subagents.md`](../../../../skills/sdlc/references/subagents.md).

Disposition key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. "Old L" is a line at c26f424. A0 moved the file and rewrote
links. This map records A2. The insert is a blank line plus two lines after
old L75, so later lines move down by three. 136 lines become 139 (cap 150).

Protected row: `#tracker-writes` (old L77–81). Every row **kept**. The
insert is under `## Step agents`, not in that section (R85). Operator
clarifications (2026-09-27): none of their subjects occur in this edit.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3 | Item agents heading | kept | L3 |
| 5–16 | Work item, mint, contrarian, clean, resume | kept | L5–16 |
| 18–20 | The manager keeps `builder_id` and `verifier_id`. Review adds `reviewer_id`. The three are different agents | kept | L18–20 |
| 22–26 | First pass and later pass for builder, verifier, and reviewer | kept | L22–26 |
| 28–29 | One pair per item, including when a manager spawns in parallel | kept | L28–29 |
| 31–42 | Never: self-gate, shared transcript, reuse across items, remint while resumable, manager as contrarian, builder, or verifier | kept | L31–42 |
| 44–49 | Fallback: resume failure, or a transcript the harness cannot load, mints a clean agent of the same role with a short handoff | kept | L44–49 |
| 51–52 | Never pass the other role's transcript. Never rotate roles to save context | kept | L51–52 |
| 54–70 | Step agents: gatherer and refiner, designer and UX reviewer, groom reviewer, contrarian and troubleshooter | kept | L54–70 |
| 72–75 | Item grain: fewer agents for a no-screen incoming item. Add security when a trust boundary moves | kept | L72–75 |
| — | Step agents and item agents raise asks as `liaison.md#raising-an-ask` says, and never message the operator | route (owner `skills/sdlc/references/liaison.md#raising-an-ask`, L1). Adds no condition. Inserted after old L75 (R85) | after the item-grain paragraph |
| 77–81 | Only the manager writes the tracker. Builder, verifier, and reviewer prompts carry no tracker-writing instructions | kept (protected `#tracker-writes`). A0 rewrote the Tracker link on old L79. This item does not change the section | `#tracker-writes` |
| 83–88 | On a host that pins one writable worktree, other items write to scratch or run one after another | kept | same section |
| 90–94 | Pack when the manager holds the bodies and the child needs them. Otherwise point | kept | `#spawn-prompts` |
| 96–99 | Pack and Point prompt table | kept. A0 rewrote the language-router link on old L99 | same table |
| 101–108 | Typical pack mints | kept | same paragraph |
| 110–112 | Resume is delta-only. Pack a new slice, not the whole set | kept | same paragraph |
| 114–122 | Never: load a catalog to pack it, pack unused skills, pack and also tell the child to read it, or point with no ids | kept | same list |
| 124–130 | Workers table | kept | `#workers` |
| 132–133 | The architect adversarial-reviews tools when the work needs it. Other role jobs route to the index | kept. A0 rewrote the Roles link on old L133 | same paragraph |
| 135–136 | Workers do not bypass security. Worker PR intake routes to intake | kept. A0 rewrote both links | same lines |

## Meaning questions

None open. The new line is a route. The protected section is unchanged
by this item. No open MQ.
