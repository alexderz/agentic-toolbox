# Rule map — `skills/sdlc/references/subagents.md`

Item: DER-736 (A4 of DER-712).

Old: `docs/sdlc/subagents.md` at main c26f424, lines 1–136.
New: [`skills/sdlc/references/subagents.md`](../../../../skills/sdlc/references/subagents.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line at c26f424.

A0 rewrote links only (already on this branch). This item edits two
phrases in the pack list (old L101–108). No other rule changes.

Protected rule touched: `#tracker-writes` (old L77–81). The row is
**kept**. **security** reads protected rows at Review.

Operator clarifications (2026-09-27): none of their subjects occur in
the edited phrases.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–42 | Item agents: work item, mint, contrarian, clean, resume; the two ids; the role table; one pair per item; the five Never bullets | kept | L3–42 |
| 44–52 | Fallback: resume failure and a transcript that will not load; never pass the other role's transcript; never rotate roles | kept | L44–52 |
| 54–75 | Step agents: chunk brief, plan–spec, groom, incoming item brief, item grain | kept | L54–75 |
| 77–81 | Tracker writes (P): only the **manager** writes; builder, verifier, and reviewer prompts carry no tracker-writing instructions | kept; A0 link `../SDLC.md#tracker` → `../SKILL.md#tracker` | L77–81 `#tracker-writes` |
| 83–88 | Writable worktree: one writable item worktree, or scratch, or one item after another | kept | L83–88 |
| 90–99 | Spawn prompts: pack when the child needs the bodies, else point; the mode table | kept; A0 link on the Point row | L90–99 |
| 101 | First gatherer packs `discover-the-idea` | kept | L101 |
| 102 | First refiner packs `yagni` | pack id `yagni` → `discover-the-idea` (A4). The contrarian on this line still packs `yagni` (kept) | L102 |
| 103–106 | Designer, UX reviewer, architect, and first builder packs. The builder still packs `yagni` with the language skill, `tdd`, and `debug` | kept | L103–106 |
| 107–108 | Verifier packs `verify-before-done` plus the proving commands. Reviewer packs `pr-review` plus the range vs project-main | verifier kept. Reviewer also packs `yagni` (A4): `pr-review` and `yagni` plus the range | L107–108 |
| 110–122 | Resume is delta-only. Four Never bullets on what a pack includes | kept | L110–122 |
| 124–136 | Workers table; architect reviews tools when the work needs it; workers do not bypass **security** | kept; A0 links | L124–136 |

## Meaning questions

None. The two pack-list phrases are the accepted A4 edits. The refiner
no longer packs `yagni`. The reviewer packs `pr-review` and `yagni`.
