# Rule map — `skills/discover-the-idea/SKILL.md`

Item: DER-735 (A3).

Old: `skills/discover-the-idea/SKILL.md` at main c26f424, lines 1–135.
New: [`skills/discover-the-idea/SKILL.md`](../../../../skills/discover-the-idea/SKILL.md) (186 lines).
Key: **kept**, **route**, **replaced**, **dropped**, **new**. "Old L" is a line at main c26f424.

A0 retargeted two links (step agents, Roles). A row marked **kept** is the same rule. **security** reads this body at Review. Procedure: [A3](../lld.md#a3--brief-step-and-discover-the-idea).

Protected rows touched: none.

Operator clarifications (2026-09-27): the frontmatter `description` is metadata (Q16). "a person" and "Improvise" do not occur.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–2 | Front matter `name` | kept | L1–2 |
| 3 | Description: triggers, architect gatherer, do not implement | replaced (metadata, Q16): also the SDLC refiner, which runs its Refine section; architect gatherer and refiner | L3 |
| 4 | Closing front matter | kept | L4 |
| 6 | Title | kept | L6 |
| 8–10 | A messy thought becomes a brief the refiner critiques; no `scripts/` | kept | L8–10 |
| 12–16 | Role architect; gatherer ids route to `#step-agents`; no language skill on a gather-only turn | kept | L12–16 |
| 18 | Heading Iron law | kept | L18 |
| 20–21 | Do not write; do not decide; surface. The user owns decisions. You own facts. The session ends in a brief | replaced (A3 edit 2): do not write; surface. The user owns every "theirs" question (route to `#asking-the-human`). Settle a minor point and mark it `your call`. You own facts. The session ends in a brief | L20–23 |
| 23 | Heading Loop | kept | L25 |
| 25 | Step 0 heading | kept | L27 |
| 27–30 | A dump already in the thread is the dump | kept | L29–32 |
| 32–34 | The dump prompt, and nothing else | kept | L34–36 |
| 36 | Wait for the dump; no questions in that message | kept | L38 |
| 38 | Heading Reflect | kept | L40 |
| 40–41 | Restate the dump in the user's words and name what is still vague | kept | L42–43 |
| 42–43 | Ask the user to confirm the restatement before any question list | replaced (R72): in an SDLC chunk the restatement goes in the brief and the operator corrects it at touchpoint 1; outside, it rides with the first question round, or in the brief when no question is left. Never send it alone | L44–47 |
| 45 | Heading Environment | kept | L49 |
| 47 | Run after the dump; the environment may not be a repo | kept | L51 |
| 49–53 | Skip only when there is nothing to read; look up facts; never ask what a file already says | kept | L53–57 |
| 55 | Heading Options map | kept | L59 |
| 57–63 | Skip a personal decision with no market; research real options; cite a source | kept | L61–67 |
| 65 | Heading Question the frontier | kept | L69 |
| 67–68 | Design tree; frontier is questions whose prerequisites are settled | kept | L71–72 |
| 70–71 | Ask the whole frontier in one round, numbered, with a recommendation | replaced (R88, R100): sort into the three piles first. In an SDLC chunk, write each remaining "theirs" question as an ask and send no message, then write the brief; do not wait and run no further round. Outside, ask the remaining frontier in one round, numbered, with a recommendation | L74–84 |
| 73–81 | Question format block | kept | L86–94 |
| 83 | Wait for the answers | replaced (R88): outside the SDLC, do the research every answer needs while you wait; none left → end the turn | L96–97 |
| 84–85 | Recompute the frontier; a question that depends on one still open waits for the next round | kept, renumbered from step 3 to step 4. The LLD gives this sentence no new wording | L98–99 |
| 87–88 | Push back on vague words; propose a strawman | kept | L101–102 |
| 90–95 | Cap at four rounds; split a widening round 4; when the frontier is empty, one more round on out-of-scope and failure modes; stop when the next question cannot be answered by talking; mark those open; never invent an answer | replaced (A3 edit 5): the cap, the split, and the cannot-be-answered-by-talking stop stay. The extra out-of-scope round is dropped. Stop when the frontier holds no "theirs" question | L104–108 |
| 97 | Heading Brief, then stop | kept | L110 |
| 99 | Emit the brief in the outline | kept | L112 |
| 101–110 | Brief outline fields | replaced (A3 edit 6): Decided, Not yet specified, Out of scope, Later, riskiest assumptions, standing permissions, release permission, HLD review, guardrails, and the renamed Open line. Options map and Verify later stay | L114–130 |
| 112 | Keep the brief in chat; write a file only when the user asks | replaced (R54): in an SDLC chunk, write `brief.md` in the chunk's design folder and hand it to the refiner; otherwise the chat rule stays | L132–135 |
| 113 | Ask the user to confirm the brief | replaced (R54): outside the SDLC, ask; in the SDLC the **manager** sends it at touchpoint 1 after Refine. Route: [Chunk brief](../../../../skills/sdlc/references/entry-brief-repo.md#chunk-brief) | L136–138 |
| 114 | Stop. Hand the brief to the refiner only when the user says so | replaced (R54): stop. The SDLC hand-off is in the new step 2, not after a separate confirm | L139 |
| — | Refiner checklist: three buckets, defer don't delete, contradictions, riskiest assumptions, invented requirements, three-pile sort, `back to Gather` or `buildable` | new (R4, R91). Owner of the refiner job | L141–165 `## Refine` |
| 116 | Heading Ask first | kept | L167 |
| 118 | Ask first: any file | replaced (A3 edit 9): any file other than the brief, `rulings.md` and `asks.md` | L169 |
| 119 | Ask first: do not expand "this idea" into "rebuild the product" | kept | L170 |
| 120 | Ask first: do not call the refiner or a builder before the user confirms | replaced (A3 edit 10): do not call a builder before the operator confirms the brief. The refiner is no longer behind that confirm | L171 |
| 122 | Heading Never | kept | L173 |
| 124–126 | Never implement; never critique in the same turn; never recommend an unlooked-at tool | kept | L175–177 |
| 127 | Never name pantheon personas; use only the roles table | kept | L178 |
| 129 | Heading Red flags | kept | L180 |
| 131–135 | Red flags, including no language skill "in case we code next" | kept | L182–186 |

## Meaning questions

None open.

- Old L20–21 "do not decide" / "the user owns decisions" now reads: the user owns every "theirs" question, and a minor point is marked `your call`. That is A3 edit 2, not a second reading.
- Old L83 "wait" is the outside-SDLC wait. The SDLC branch of step 2 sends no message and runs no further round (R88, R100).
- Old L84–85 stays the recompute sentence, renumbered. The LLD does not rewrite it.
- Old L90–93's extra out-of-scope round is removed by A3 edit 5. The cap of four and the cannot-be-answered-by-talking stop stay.
