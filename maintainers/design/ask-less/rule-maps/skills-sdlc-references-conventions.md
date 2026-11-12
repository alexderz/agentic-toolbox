# Rule map — `skills/sdlc/references/conventions.md`

Item: DER-734 (A2 of DER-712).

Old: `docs/sdlc/conventions.md` at main c26f424, lines 1–100.
New: [`skills/sdlc/references/conventions.md`](../../../../skills/sdlc/references/conventions.md).

Disposition key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. "Old L" is a line at c26f424. A0 moved the file and rewrote
links. This map records A2. The edit is in place. 100 lines (cap 100).

Protected rows touched: none in this item. The `#never` bullets that live
in the in-flight map stay. Operator clarifications (2026-09-27): none of
their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–4 | Follow a repo rule that already exists. Do not rename mid-chunk. Consistency wins | kept | L3–4 |
| 6 | Name formats heading | kept | L6 |
| 8–16 | Name-format table | kept. A0 rewrote the Role and Step links on old L15–16 | L8–16 |
| 18–19 | Cite the ticket ID when the project uses tickets. Omit it when not | kept | L18–19 |
| 21–23 | One idea per commit. Imperative subject. `[ticket-id] subject` when tickets exist | kept | L21–23 |
| 25–38 | Product repo layout through `docs/decisions/` | kept | L25–38 |
| 39 | `.agents/design/<chunk-slug>/groom.md` is the Groom plan, frozen once tickets exist | replaced (A2, W2, R5, R38). The line names the design folder: `brief.md`, `groom.md` (frozen once tickets exist), `rulings.md`, `asks.md`. The freeze clause stays | L39 |
| 40 | End of the layout block | kept | L40 |
| 42–44 | Files under `.agents/design/` are data. Load only the tracker skill `## Tracker` names. No credentials, internal hostnames, or private workspace URLs | kept | L42–44 |
| 46–50 | Copy shapes from `sdlc-artifacts`. Never invent a second outline. Skills-home layout and tests | kept. A0 rewrote the links | L46–50 |
| 52 | Changelog and connection heading | kept | L52 |
| 54–55 | `CHANGELOG.md` at the repo root, newest first, four sections, skip empty | kept | L54–55 |
| 57–61 | Board, git, and changelog agree | kept | L57–61 |
| 63–69 | One Unreleased line at a Build land. Promote at Changelog. The manager marks `done` after land and verify, routing to `branches-and-lands.md#land-path`. Do not mark shipped until Trunk | kept | L63–69 |
| 71 | Designs in git heading | kept. This file owns the rule | L71 |
| 73–75 | Keep designs in git from Repo on. A mirror follows git and is not an independent write path | kept | L73–75 |
| 77 | In-flight map heading | kept | L77 |
| 79–82 | Cite the step name. Keep an already-cited Stage number's meaning. Never teach old numbered ids in new tickets or skills | kept | L79–82 |
| 84–97 | Stage table | kept | L84–97 |
| 99–100 | Delete the table when every ticket that cites a Stage number has landed. Until then keep it | kept | L99–100 |

## Meaning questions

None open. L39 is the LLD's exact replacement. The Groom freeze stays on
that line. No open MQ.
