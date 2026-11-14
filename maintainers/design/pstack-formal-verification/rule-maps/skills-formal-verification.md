# Change map (light pass) — `skills/formal-verification/SKILL.md`

Item: DER-774. Vendor-derived skill: SOURCES Upstream names cursor/plugins pstack, so this is a
light-pass change map per `maintainers/writing-standard.md` Rule maps step 6. The file is
**added** (new skill id); this map says where each upstream section went.

Old: upstream `pstack/skills/create-formal-verification-skill/SKILL.md` (C, 43 lines) and
`pstack/skills/maintain-formal-verification-skill/SKILL.md` (M, 58 lines) at
3dbd22ff12742fb28c9700b9760baa29ed41dc13. New:
[`skills/formal-verification/SKILL.md`](../../../../skills/formal-verification/SKILL.md) (250 lines).

Key: **kept** (same behavior, new words), **adapted** (changed by a manager ruling, named),
**dropped** (reason), **added** (source).

| Upstream L | Content | Disposition | New location |
| --- | --- | --- | --- |
| C1–5, M1–5 | Frontmatter; slash-command triggers; `disable-model-invocation` | adapted: one toolbox `description` ("use this when …"); slash commands and the invocation flag dropped (routing is the `AGENTS.md` row, ruling 3) | frontmatter |
| C9 | Test vs verification; reader-cold verify skill; trust without the language | kept | intro; Write the verify skill lead |
| — | Attribution line | added (ruling 5) | L8 |
| — | Names: property, verification, check, verify target, verify skill, coverage record, sync commit, broken variant | added (writing standard 3) | Names |
| — | Actors: architect at Spec, builder, verifier | added (ruling 3); the architect records target, property and tool in the LLD or ticket | Actors |
| C13 | Answer from the code; ask only what you cannot observe; start at a named area | adapted: ask per Asking the operator (ruling 4) | Toolbox policies 1; Choose the target 1 |
| C15 | Promise where a break harms users and tests rarely reach; strongest, not easiest | kept, as numbered steps; "find the implicit state machines" list added from the post (ruling 1) | Choose the target 2–5 |
| C19 | Tool choice: TLA+ default for order; code verifier per input; generated-input tests when none; proof when no bound; prefer installable; say why | kept, as a first-match table | Choose the tool |
| C23–29 | Seven quality bars | kept | Quality bar 1–7; Findings stay findings is also the Iron law (most-violated rule first) |
| C25 | "do not change product code unless the user asks" | adapted: product code only inside the item's scope (ruling 4) | Toolbox policies 2 |
| C33 | Verify skill contents: frontmatter, touch test, run, bug vs model error, intended changes, coverage, sync commit rule, real names | kept | Write the verify skill 1–6 |
| C35 | TLA+ results read with `/statechart`, by name, no commands copied | adapted: the toolbox `statechart` id | Write the verify skill 7 |
| — | Where the verify skill lives; one per subsystem | added (ruling 4; ruling 1 "one skill per subsystem") | Toolbox policies 4–5 |
| — | Tool install is a product dependency decision in the LLD or ticket | added (ruling 4) | Toolbox policies 3 |
| C39 | Prove on a scratch break; restore; fix the skill, not the break | kept | Build and prove the check 3–5; Prove the verify skill 1–4 |
| C43 | Hand-off contents; second target only if close; point to maintain | kept; second target as its own subsystem (ruling 1); "point to maintain" becomes the Maintain section | Hand off 1–7 |
| M9 | Stale pass is the dangerous case; maintain covers changes that skipped the verify skill | kept | Maintain lead |
| M13–19 | Outcomes in sync / updated / bug / blocked; updated and bug together | kept, as a table | Outcomes |
| M24 | Edit only the verification; no product edits; never weaken | adapted: product code per Toolbox policies 2 (ruling 4); never-weaken is the Iron law | Outcomes tail; Iron law |
| M28–44 | Six-step pass, with the four change classes | kept; the classes as a condition → action table | Pass 1–6 |
| M48–58 | Report contents; drift vs bug; stale pass; separate change | kept; "change of its own" as "commit of its own" | Report |

Guardrails added beyond ruling 4: none. The Actors split follows ruling 3's routing; it adds no
approval or question.

## Meaning questions

None open. Toolbox policies 3 reads ruling 4 as: install only a tool the LLD or ticket names;
otherwise hand the choice off for recording. That is the ruling's "recorded in that repo's LLD
or ticket, not a silent install", with no new approver.
