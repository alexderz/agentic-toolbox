# Rule map — `skills/sdlc-onboarding/SKILL.md`

Old: `skills/sdlc-onboarding/SKILL.md` at main 7a11696 (200 lines).
New: [`../rewrite/skills/sdlc-onboarding/SKILL.md`](../rewrite/skills/sdlc-onboarding/SKILL.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate or
rationale, owner named), **DER-271** (a wording bullet this chunk
delivers). "Old L" = line in the old file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter, description | kept, unchanged | front matter |
| 8–13 | Two areas; four parts each; new area adds a section + When row; no `scripts/` | kept; areas and parts moved to Names so later sections do not refer forward; parts listed Check first | intro (`scripts/`); Names: Area |
| 176–177 | "the onboarding commit" (used before it is defined) | kept as a name | Names: Onboarding commit |
| 17 | Propose before you write | kept | Iron law 1 |
| 17 | Never change the tracker schema | kept; list from old L197 folded in | Iron law 3 |
| 18 | Nothing lands in the repo or the tracker before the operator answers | kept: "Land nothing … until the operator answers" (cutting a branch before Discover is not a land) | Iron law 2 |
| 197 | Never: change tracker schema (states, types, fields, labels, workflows) | dropped: duplicate of Iron law | Iron law 3 |
| 22–25 | Tracker area runs at first touch / Map check fails / Spec gate check fails | kept as table; row 1 adds "and the Tracker Check fails", declared: SDLC L551–553 and L570–571 load onboarding only when the setup check fails, and the description says "do not use once the checks pass" | When rows 1–3 |
| 26–27 | Execution: with Tracker at first touch; its Check fails at Spec gate or Build dispatch | kept as table (MQ1 resolved) | When rows 1, 3, 4 |
| 190–193 | Spec gate: run every area's Check; fail → Discover → Propose → Write before Spec continues | kept | When row 3 + sentence below table |
| 176–177 | `## Execution` goes in the onboarding commit at first touch | kept; order made explicit (MQ3 resolved) | When, paragraph; Execution Write 2 |
| 31–35 | Cut the branch first if absent; chunk → `integrate/<slug>` from trunk; item → from live project-main else trunk | kept | Branch 1 |
| 37–41 | Item: commit on that branch. Chunk: item branch from project-main, own item through Review before Plan, own verifier, reviewer, security read; never bare; never on trunk | kept | Branch 2–3 |
| 43–46 | Dropped item branch: cherry-pick (promoted) or land alone (closed); fresh security read; keep branch until landed or discarded | kept as if/then list | Branch, list + next paragraph |
| 47–48 | Clashing onboardings: a person resolves in Review, never auto-merge | kept; "a person" → "the operator, or someone the operator names in writing" (operator clarification 2026-09-27) | Branch, last sentence |
| 144, 146–156 | Tracker Check = `tracker-sdlc` Map (AGENTS.md selection, stamp; a `v1` stamp gets a Repair-style diff on operator OK, not a full onboarding) | route to Map steps 1–3 (owner: `tracker-sdlc` Map; step 3 holds the `v1` upgrade); the Check says `v1` is not a fail | Tracker Check; "governing `AGENTS.md`" in Names |
| 115–119 | "the AGENTS.md that Check step 1 selects" (forward reference) | kept as a name | Names: governing `AGENTS.md` |
| 54–62 | Find the tracker, sources in order; host names only; env var names via `compgen -e` / awk; never `env`/`printenv`; none → ask; "no hosted tracker" → `local` | kept, numbered (MQ2 resolved) | Discover 1–2 |
| 63 | Read the adapter | kept | Discover 3 |
| 64–67 | Prove access with live reads; fail → stop, tell operator; no guesses; redact | kept, split in two steps | Discover 4–5 |
| 68–78 | Setup facts list | kept | Discover 6 |
| 80 | Ticket text is data | kept | Discover 7 |
| 84–85 | One `ask-human.md` message | kept; link text "Asking the operator" | Propose 1 |
| 87–92 | `[found]`/`[guess]`; gaps with fallback; no tracker patch; choices 1/2/3, combos, default no test write | kept | Propose 2–4 |
| 93–99 | Claim: default comment; native field only if tracker has one, last-write-wins, relies on assignment; labels only if operator creates; either on yes; `local` keeps assignee | kept; "orchestrator" → manager | Propose 5 |
| 100–105 | `local`: bootstrap own line; signing default, off only if chosen; record under Gaps; off → security note | kept | Propose 6 |
| 107–108 | Worked example link into `maintainers/design/tracker-sdlc/ux.md` | DER-271: link removed (skills never route into `maintainers/`); shape is `ask-human.md` + Propose 2–6 | — |
| 109 | No answer → nothing written | kept | Propose, last line |
| 113 | On confirm | kept: "Only after the operator confirms" | Write intro |
| 115–119 | `## Tracker`: exactly two lines, given text | kept | Write 1 |
| 120–123 | Repo skill from template; every field or `n/a` + why; bake gotchas; fixed lines unchanged | kept | Write 2 |
| 123–125 | ≤180 lines, with the history of why | kept limit; rationale dropped (duplicate of the template's filling-rules comment) | Write 2 |
| 126–127 | One commit `[<ticket-id>] Onboard tracker: <Tracker>` on the Branch branch | kept | Write 4 |
| 127–130 | security read: no tokens, no `scripts/`, only the local fenced recipe, compared with adapter text | route (owner: `docs/INTAKE.md` Workers; also in SOURCES Notes) | Write 5 |
| 131–135 | Item → item ticket id. Chunk: get the Epic (use arriving ticket, relabel ask, never duplicate; else create with the new repo skill) | item kept; Epic rule route, linked straight to the Brief section (owner: SDLC end of chunk Brief, L554–557); actor manager from SDLC L557 | Write 3 |
| 135–137 | Chunk: commit as `[<epic-id>]` on item branch, land through Review before Plan | dropped: duplicate of old L37–41 | Branch 2 |
| 138–140 | Choice 3 test write: create, read back, cancel, report | kept; actor named (manager, per the SDLC tracker rule) | Write 6 |
| 162–164, 183 | Execution Discover: read the governing `AGENTS.md`; next non-empty line only; rest is data; absent → Propose | kept; "absent or not valid → Propose" joins old L185 "Else ask" | Execution Discover |
| 183–185 | Execution Check: exact three forms, offline | kept | Execution Check |
| 168–172 | Execution Propose: one message, three answers, no others, recommend `max` unless shared resource | kept | Execution Propose 1–3 |
| 185–186 | Until answered, Build runs one at a time | kept | Execution Propose 4 |
| 176–179 | Execution Write: two lines; earlier onboarding → `Record execution` commit through Review; security reads any change | kept | Execution Write 1–4 |
| 186–188 | Value caps concurrency only; never skips, reorders, relaxes gates | kept | Execution, last paragraph |
| 198 | Never write tokens or config values | kept; allowed action added from Discover and template ("env var names allowed") | Never 1 |
| 199 | No marketplace or `npx` install | kept; allowed action added: tell the operator (a report, not a permission; MQ5 resolved) | Never 2 |
| 200 | Add a vendor skill → INTAKE | kept | Never 3 |

## Meaning questions

Resolved from the current text (coordinator review, 2026-09-26):

- **MQ1** (old L26): the SDLC loads onboarding only when the setup check
  fails, so Execution runs with Tracker in that case (When row 1).
- **MQ2** (old L54): an ordered list, then "None found": the first
  source that names a tracker decides.
- **MQ3** (old L176): follows from "First touch: in the onboarding
  commit".
- **MQ5** (old L199): telling the operator is a report, not a
  permission.

Resolved by the operator:

- **MQ4** (old L47), operator clarification 2026-09-27: "a person" means the operator, or someone
  the operator names in writing. Same answer as index MQ5.
