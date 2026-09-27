# Rule map — `docs/SDLC.md` (index)

Old: `docs/SDLC.md` at main 7a11696, lines 1–118, 465–486, 1097–1128
(the parts the index takes over). Every other old section stays, in the
trial, unchanged in `docs/sdlc/not-yet-split.md` and is routed from the
Steps table. New: [`../rewrite/docs/SDLC.md`](../rewrite/docs/SDLC.md).
Dispositions as in [sdlc-onboarding.md](sdlc-onboarding.md).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 3–7 | Purpose; git holds artifacts; tracker is the board; cite ticket ids | kept | intro |
| — | Reading order | new routing (no rule) | How to read |
| 11–12 | Skills are tools keyed by role; improvise; do not remint | kept ("improvise when the work needs it" stays a judgment: MQ6) | Roles, intro |
| 14–22 | Role table (7 roles) | kept; manager row: "Sole tracker writer" → "The only tracker writer"; operator: "Human in the loop" → "The person in the loop" | Roles table |
| 23–24 | Workers act as builder/tester; do not bypass security | kept | Roles, after table |
| 597 (Brief) | "Do not add a ninth role" | generalized per HLD L78–79: "Use only these roles", plus one line that step jobs (gatherer, refiner, troubleshooter, verifier, reviewer, groom reviewer) are agents acting in these roles; old line stays in not-yet-split in the trial (MQ1 resolved) | Roles, intro |
| 29–32 | Ask: stop and say so; no hidden ask; do not proceed as if yes; define project words | kept, numbered | Asking 1, 3, 6 |
| 34–56 | Inline copy of the ask message shape | dropped: duplicate (owner: template `ask-human.md`) | Asking 2 |
| 58–60 | Show recommendation and why; say if none; one question per message; numbered sets | kept | Asking 4–5 |
| 62–65 | When an ask is required (list) | kept verbatim | Asking, "An ask is required for" |
| 67–68 | Never: "Please advise", "LGTM?", "UX verification not required?" unexplained; proceeding after silence | kept; allowed action named | Asking, Never paragraph |
| 70–74 | Wait = blocker on that issue; others move; no freeze; AFK → parent may pick between two item fixes honoring the plan; never change Plan/Spec shape | kept; "parent" → manager; "a person" → operator (MQ5) | Asking, "While you wait" |
| — | Heading "Asking the human" | renamed "Asking the operator"; anchor `#asking-the-human` kept by an explicit id (linked from `AGENTS.md` and two skills) | Asking heading |
| 78–82 | Hierarchy table | kept; "Work item" → "Item" | Tracker table |
| 84–90 | All tracker I/O via `tracker-sdlc` + repo skill; six states; `done` meanings; blocked is not a state | kept | Tracker 1, States |
| 791–792 (Build) | Open blocker = not `done` / `canceled` | kept as a definition (owner: here; Build routes in area C) | Tracker, States |
| 91–95 | Only the orchestrator (manager) writes; verbs; builders/verifiers/reviewers report | kept; "orchestrator (manager)" → manager | Tracker 2–3 |
| 96 | After-act manager with operator's timezone | kept | Tracker 4 |
| 96–99 | Board is tracker, git holds files; designs in git from onset | dropped: duplicate (owner: Git designs from onset, old L1090–1095) | Steps, Layout row |
| 102 | Board layer is the grain; no fourth issue type | kept | Grain |
| 104–108 | Grain table | kept | Grain table |
| 110–111 | Entry classifies or asks; does not fix | kept | Grain bullets |
| 113–114 | UI defect stays an item until "what should this screen be?" | kept | Grain bullets |
| 116–118 | Split-from-Spec work is an item in Build; no item Brief; shape change → escalate, block, siblings proceed | kept | Grain bullets |
| — | Definitions of trunk, project-main, chunk, item, landed+verified | new names section; each from old text: trunk L872–874, L910; project-main L911; chunk/item L513–515; landed+verified L951–952 | Names |
| 119–384 | "How software gets built" (people text) | moves unchanged to `docs/how-software-gets-built.md` (area C); in the trial it stays in not-yet-split | — |
| 467–469 | Same names at every grain; headings and tickets use names | kept | Steps intro |
| 471–484 | Step table | kept; third column routes to a file or section; Trunk row "the official copy" → trunk (one name); Plan/Spec rows add "the" | Steps table |
| 486–487 | HLD/LLD are artifact names; steps are Plan and Spec | kept | Steps intro |
| 1097–1128 | Skill table (roles and notes per skill) | route: which skill → root `AGENTS.md`; ids and pins → `SOURCES.md` (per HLD owners); the per-skill notes are checked into their step files in area C | Roles, last line |

## Meaning questions

Resolved from the current text (coordinator review, 2026-09-26):

- **MQ1** (old L597): HLD L78–79 decides: "use only the roles in the
  table"; step jobs are agents acting in those roles.
- **MQ2** (old L62): the write-up is the brief (SDLC L152, L298, L304).
- **MQ3** (old L96): after-act = record on the board after the fact
  (SDLC L460).
- **MQ4** (Names): landed+verified as defined at SDLC L460–461 and
  L951–952.

Open for the operator:

- **MQ5** (old L29, L70–74): "a person must decide", "until a person
  answers". The draft says the operator throughout (one name per
  thing). Can a person other than the operator answer these asks?
  Same question as onboarding MQ4.
- **MQ6** (old L11): "Improvise when the work needs it" is a judgment
  call with no checkable condition. Kept verbatim; can the operator
  state when improvising is allowed (for example: no skill id fits the
  task), or should it stay open-ended?
