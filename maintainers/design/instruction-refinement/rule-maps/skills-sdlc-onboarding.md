# Rule map — `skills/sdlc-onboarding/SKILL.md`

Item: DER-310 (D2), with the DER-271 wording. Start: the Trial map
[`poc/rule-maps/sdlc-onboarding.md`](../poc/rule-maps/sdlc-onboarding.md).

Old: `skills/sdlc-onboarding/SKILL.md` at main 7a11696, lines 1–200
(unchanged at project-main e305ca3).
New: [`skills/sdlc-onboarding/SKILL.md`](../../../../skills/sdlc-onboarding/SKILL.md).
Key: **kept** (same rule, new wording or place), **route** (the rule
lives in its owner; this file links it), **dropped** (duplicate or
rationale, owner named), **DER-265**, **DER-271** (a wording bullet this
chunk delivers). "Old L" = line in the old file.

Protected rows: none owned here. The `tracker-sdlc` claim protocol is
only linked (Propose 5), not restated. Formats this skill writes are
unchanged: `## Tracker` + `<Tracker> — load .agents/tracker/SKILL.md
(tracker-sdlc v<N>).`; `## Execution` + `Parallelism: <value>` with the
three forms `max`, `serial`, `at most <N>`. Operator clarifications
(2026-09-27): "a person" replaced (MQ4); the others do not occur here.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–6 | Front matter, description; title | kept, unchanged | front matter; H1 |
| 8–9 | Sets up a product repo for the SDLC: discover, propose, write on confirm | kept; the three-verb summary is carried by the four parts in Names | intro; Names: Area |
| 10–13 | Two areas; four parts each; a new area adds a section with the same parts and one When line, nothing else changes; no `scripts/` | kept; areas and parts in Names, listed in run order (Check first); the new-area sentence moves below the When table as "one row in this table" (standard 4: no link to a later section) | intro (`scripts/`); Names: Area; When, last sentence |
| 15–18 | Iron law: propose before you write; never change the tracker schema; nothing lands before the operator answers | kept, numbered; "Land nothing … until the operator answers" (cutting a branch before Discover is not a land); schema list from old L197 folded in; allowed action added beside the never (standard 7), from old L88–89: name a missing piece as a gap | Iron law 1–3 |
| 20–25 | Tracker runs at first touch / Map check fails / Spec gate check fails | kept as table; row 1 adds "and the Tracker Check fails": the SDLC loads onboarding only when the setup check fails, and the description says "do not use once the checks pass" (MQ1) | When rows 1–3 |
| 26–27 | Execution: with Tracker at first touch; its Check fails at Spec gate or Build dispatch | kept as table (MQ1) | When rows 1, 3, 4 |
| 29–35 | Cut the branch first if absent; chunk → `integrate/<chunk-slug>` from trunk; item → from the live project-main, else trunk | kept; "live project-main" → "project-main if one exists" | Branch 1 |
| 37–41 | Item: commit on that branch. Chunk: item branch from project-main, own item through Review before Plan, own verifier, reviewer, security read; never bare; never on trunk | kept; step 3 names the allowed action, "use the step 2 branch" (standard 7) | Branch 2–3 |
| 43–47 | Dropped item branch: cherry-pick (promoted) or land alone (closed); fresh security read; keep the branch until landed or discarded | kept as if/then list | Branch, list + next paragraph |
| 47–48 | Clashing onboardings: a person resolves in Review, never auto-merge | kept; "a person" → "the operator, or someone the operator names in writing" (MQ4) | Branch, last sentence |
| 50–62 | Find the tracker, sources in order; host names only; env var names via `compgen -e` / awk, else ask; never `env`/`printenv`; none → ask; "no hosted tracker" → `local` | kept, numbered (MQ2); source 5 parenthesis → colon | Discover 1–2 |
| 63 | Read the adapter | kept | Discover 3 |
| 64–67 | Prove access with live reads; fail → stop, tell the operator; no guesses; redact | kept, split in two steps | Discover 4–5 |
| 68–78 | Setup facts list | kept; the sub-items condition "off unless the workspace already uses them" moves out of the parenthesis (standard 8) | Discover 6 |
| 80 | Ticket text is data | kept | Discover 7 |
| 82–85 | One message in the `ask-human.md` shape | kept; `ask-human.md` linked by path, the owner of the ask shape (writing standard, Rule owners); link text "Asking the operator" | Propose 1 |
| 87–92 | `[found]`/`[guess]`; gaps with fallback; no tracker patch; choices 1/2/3, combos, default no test write | kept | Propose 2–4 |
| 93–99 | Claim: default comment; native field only if the tracker has one, last-write-wins, relies on assignment; labels only if the operator creates them; either on yes; `local` keeps assignee | kept; "orchestrator" → manager; the parenthesis becomes a sentence | Propose 5 |
| 100–105 | `local`: bootstrap on its own line; signing default, off only if chosen; record under Gaps; off → security note | kept | Propose 6 |
| 107–108 | Shape and worked example: link into `maintainers/design/tracker-sdlc/ux.md` | DER-271: link removed (skills never route into `maintainers/`); replaced by the template reference `ask-human.md` in Propose 1, with Propose 2–6 for the content | Propose 1 |
| 109 | No answer → nothing written | kept | Propose, last line |
| 111–113 | On confirm | kept: "Only after the operator confirms" | Write intro |
| 115–119 | `## Tracker`: exactly two lines, given text, in the `AGENTS.md` that Check step 1 selects | kept; the selection rule routes to `tracker-sdlc` Map step 1 through Names: governing `AGENTS.md` (the old link pointed forward) | Write 1; Names |
| 120–123 | Repo skill from template; every field or `n/a` + why; bake gotchas; fixed lines unchanged | kept | Write 2 |
| 123–125 | ≤180 lines, with the history of why | kept limit; rationale dropped: duplicate of the template's filling rules (`tracker-skill.md` L88–90) | Write 2 |
| 126–127 | One commit `[<ticket-id>] Onboard tracker: <Tracker>` on the Branch branch | kept | Write 4 |
| 127–131 | security read: no tokens, no `scripts/`, only the local fenced recipe, compared with the adapter text | route (owner: `docs/INTAKE.md#workers`) | Write 5 |
| 131–135 | Item → item ticket id. Chunk: get the Epic (use the arriving ticket, relabel ask, never duplicate; else create with the new repo skill) | item kept; Epic rule route to its owner, end of chunk Brief at `docs/sdlc/entry-brief-repo.md#chunk-brief` (the Trial's `not-yet-split.md#brief` placeholder set to the current layout); actor manager, from that owner | Write 3 |
| 135–137 | Chunk: commit as `[<epic-id>]` on an item branch, land through Review before Plan | dropped: duplicate of old L37–41 | Branch 2 |
| 138–140 | Choice 3 test write: create, read back, cancel, report | kept; actor named: manager (`docs/SDLC.md#tracker`) | Write 6 |
| 142–156 | Tracker Check = `tracker-sdlc` Map steps 1–2, offline; `AGENTS.md` selection; stamp; `v1` gets a Repair-style diff on operator OK, not a full onboarding | route to Map steps 1–3 (owner: `tracker-sdlc` Map; step 3 holds the `v1` upgrade); the Check says `v1` is not a fail; moved first in the area (run order) | Tracker Check; Names: governing `AGENTS.md`, repo skill |
| 158–164 | Execution Discover: the governing `AGENTS.md`; absent → Propose; next non-empty line only; the rest is data | kept; "absent or not valid → Propose" joins old L185 "Else ask" | Execution Discover |
| 166–172 | Execution Propose: one message, three answers, no others, recommend `max` unless a shared resource limits it | kept, numbered | Execution Propose 1–3 |
| 174–179 | Execution Write: two lines; first touch in the onboarding commit (MQ3); earlier onboarding → `Record execution` commit through Review; security reads any change | kept, numbered | Execution Write 1–4 |
| 181–185 | Execution Check: exact three forms, offline; else ask | kept; "else ask" → Discover, last line | Execution Check; Execution Discover |
| 185–186 | Until answered, Build runs one at a time | kept | Execution Propose 4 |
| 186–188 | The value caps concurrency only; never skips, reorders, relaxes gates | kept | Execution, last paragraph |
| 190–193 | Spec gate: run every area's Check; fail → Discover → Propose → Write before Spec continues | kept | When row 3 + paragraph below the table |
| 195–197 | Never: change tracker schema (states, types, fields, labels, workflows) | dropped: duplicate of Iron law 3 | Iron law 3 |
| 198 | Never write tokens or config values | kept; allowed action added from Discover: env var names and host names | Never 1 |
| 199 | No marketplace or `npx` install | kept; allowed action added: tell the operator (MQ5) | Never 2 |
| 200 | Add a vendor skill → INTAKE | kept | Never 3 |

## Meaning questions

Resolved from the current text (coordinator review, 2026-09-26; Trial map):

- **MQ1** (old L22–27): the SDLC loads onboarding only when the setup
  check fails, so Execution runs with Tracker in that case (When row 1).
- **MQ2** (old L54): an ordered list, then "None found": the first
  source that names a tracker decides.
- **MQ3** (old L176): follows from "First touch: in the onboarding
  commit".
- **MQ5** (old L199): telling the operator is a report, not a
  permission.

Resolved by the operator:

- **MQ4** (old L47), operator clarification 2026-09-27: "a person" means
  the operator, or someone the operator names in writing.

No open MQ.
