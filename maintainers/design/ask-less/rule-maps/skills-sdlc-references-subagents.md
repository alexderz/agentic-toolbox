# Rule map — `subagents.md` (A2, DER-734)

Old: `docs/sdlc/subagents.md` at main c26f424, lines 1–136. New: `skills/sdlc/references/subagents.md`.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–75 | Item agents, Fallback, Step agents | kept | same lines |
| — | (new) Step agents and item agents raise asks per Raising an ask and never message the operator | route (R85, L1) | end of `## Step agents`, L77–78 |
| 77–136 | Tracker writes (protected), Writable worktree, Spawn prompts, Workers | kept | L80–139 |

## Meaning questions

None. The protected `## Tracker writes` section is untouched (R85).

## Pack list (A4, DER-736)

Old: `docs/sdlc/subagents.md` at main c26f424, lines 101–108. New: `skills/sdlc/references/subagents.md`.
Item: DER-736 (G5, A4 of DER-712). Changed lines only; the A2 rows above cover the rest of the
file. Text: [opus-rebuild.md G5](../opus-rebuild.md#g5--yagni-subagents-pack-review-a4).

Key: **kept**, **route**, **dropped** with the owner named, **changed** with the brief, ruling or
LLD id that decides it.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 101 | First gatherer packed with `discover-the-idea` | **changed** (R147): also packs Asking the operator and Raising an ask | L104–106 |
| 101–102 | First refiner packed with `yagni` | **changed** (T3, R147): packs `discover-the-idea` to run its Refine section, and the same two rules; no `yagni` | L107 |
| 102–107 | Contrarian, designer, UX reviewer, architect, first builder, verifier packs | kept | L108–113 |
| 107–108 | Reviewer packed with `pr-review` plus the range | **changed** (R67): also packs `yagni` | L114 |

### Meaning questions (A4)

None.
