# Rule map — `docs/SDLC.md` (SDLC index)

Item: DER-299 (C2). A later item that edits this file appends its own
section.

Old: `docs/SDLC.md` at main 7a11696, lines 1–118, 465–487, 1097–1128.
New: [`docs/SDLC.md`](../../../../docs/SDLC.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line in the old file;
"L" in New location = line in the new file. Source draft:
[`poc/rewrite/docs/SDLC.md`](../poc/rewrite/docs/SDLC.md) and its map
[`poc/rule-maps/sdlc-index.md`](../poc/rule-maps/sdlc-index.md).

Protected rows (writing standard, Protected rules): SDLC index `#roles`
(old L9–25) and `#tracker` (old L76–98). Each maps `kept` or `route`
below. **security** reads them at Review.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–7 | Purpose; git holds artifacts; tracker is the board; cite ticket ids | kept; "Software is the common case; the same steps apply to" → one list | intro, L3–6 |
| — | Reading order | kept from the DER-298 move (no old line) | How to read, L8–14 |
| 9 | Heading Roles | kept; anchor `#roles` unchanged | L16 |
| 11 | Skills are tools, keyed by role | kept | Roles, L18 |
| 11 | "Improvise when the work needs it" | kept; replaced per operator clarification 2026-09-27 (MQ6) | Roles, L18–19 |
| 12 | Do not remint a skill that already has an id "here" | kept; "here" dropped: the skill table is gone and its ids are the `SOURCES.md` ids (MQ7) | Roles, L19–20; ids route L37–38 |
| — (old L597, Brief) | Do not add a ninth role | kept as "Use only these roles", plus the step-jobs line (MQ1); old L597 itself belongs to C3 (see note 1) | Roles, L20–22 |
| 14–15 | Role table header | kept | L24–25 |
| 16–20 | architect, designer, builder, tester, security rows | kept, unchanged; gate reasons in parentheses are examples (clarification 2026-09-27) | L26–30 |
| 21 | manager row; "Sole tracker writer" | kept; "Sole tracker writer" → "The only tracker writer" | L31 |
| 22 | operator row; "Human in the loop" | kept; → "The person in the loop" | L32 |
| 24–25 | Workers act as builder or tester; do not bypass security | kept, unchanged (owner of "Workers do not bypass security") | L34–35 |
| 27 | Heading "Asking the human" | kept; renamed "Asking the operator"; anchor `#asking-the-human` kept by an explicit `<a id>` (K9) | L104–106 |
| 29 | "When a person must decide" | kept; → "the operator, or someone the operator names in writing" (MQ5) | Asking intro, L108–109 |
| 29–30 | Stop and say so; do not hide the ask in a status dump | kept | Asking 1, L111 |
| 30 | Do not keep going as if they said yes | kept | Asking 6, L120 |
| 30–32 | No project words unless defined in everyday language | kept | Asking 3, L115–116 |
| 34 | Use the shape of template `ask-human.md` | route (owner: `skills/sdlc-artifacts/templates/ask-human.md`); "Fill every part" | Asking 2, L112–114 |
| 36–56 | Inline copy of the ask message shape | dropped: duplicate (owner: template `ask-human.md`, same parts) | Asking 2, L112–114 |
| 58–59 | Show the recommendation and why; say if there is no good default | kept | Asking 4, L117 |
| 59–60 | One question per message; several → number them, recommend a set | kept | Asking 5, L118–119 |
| 62–65 | When an ask is required (list) | kept, list verbatim | L122–125 |
| 67–68 | Never: "Please advise.", "LGTM?", "UX verification not required?" unexplained; proceeding after silence | kept; allowed action named beside each Never (standard 7) | L127–129 |
| 70–71 | Waiting on a person is a blocker on that issue; others move; do not freeze the chunk | kept; "Waiting on a person" → "The wait" (the person is the one asked, L108–109) | While you wait, L133–134 |
| 71–73 | AFK / headless / autonomous → "the parent" may pick between two item fixes honoring the plan | kept; "parent" → manager (banned name) | L135–137 |
| 73–74 | Never change Plan or Spec shape; blocked until "a person" answers | kept; → "the operator, or someone the operator names in writing" (MQ5) | L137–139 |
| 76 | Heading "Hierarchy (issue tracker)" | kept as "Tracker"; anchor `#tracker` from the DER-298 move unchanged | L60 |
| 78–82 | Hierarchy table | kept; "Work item" → "Item" (one name, Names L51) | L62–66 |
| 84–86 | Every tracker read and write goes through `tracker-sdlc` and the repo's tracker skill | kept | Tracker 1, L68–70 |
| 86–88 | Six canonical states; `done` = landed+verified, an Epic when on trunk | kept; "Canonical states" → "States" | L77–78 |
| 88–89 | Blocked is not a state; blocked while it has open blockers | kept; adds the open-blocker definition from old L791–792 (see note 2) | L78–80 |
| 91–92 | Only the orchestrator (manager) writes: create, claim, release, set-blocker, comment, every transition | kept; "orchestrator (manager)" → manager (banned name) | Tracker 2, L71–72 |
| 92–94 | Builders, verifiers, reviewers never write; they report, the manager writes | kept; "orchestrator" → manager | Tracker 3, L73–74 |
| 96 | After-act manager with the operator's timezone | kept (after-act: MQ3) | Tracker 4, L75 |
| 96–97 | The board is the tracker; git holds the files | kept once, in the intro | intro, L4–5 |
| 97–98 | Designs live in git from onset; not only on a local mirror | route (owner: `docs/sdlc/conventions.md#designs-in-git`) | L82–83 |
| 100 | Heading "Grain (how you enter)" | kept as "Grain"; anchor `#grain` from the DER-298 move unchanged | L85 |
| 102 | Board layer is the grain; no fourth issue type | kept | L87 |
| 104–105 | Grain table header "Needs a person for taste / design talk?" | kept; → "the operator, or someone the operator names in writing" (MQ5) | L89–90 |
| 106–108 | Grain table rows | kept; "—" → ":" | L91–93 |
| 110 | Entry (first step) classifies or asks; does not fix | kept; parenthesis → apposition (standard 8) | L95 |
| 112–113 | UI defect stays an item until "what should this screen be?"; then chunk or promote | kept | L96–97 |
| 115–116 | Split-from-Spec work is an item in Build; do not re-run item Brief | kept | L98–99 |
| 116–117 | Build finds a shape change → escalate (ask, block that issue, siblings proceed) | kept; parenthesis → list; "ask" routes to Asking the operator | L100–102 |
| — | Names: roles, trunk, project-main, chunk, item, landed+verified, step names; name formats | new names list (owner per standard Rule owners); each from old text: trunk L872–874, L910; project-main L911; chunk and item L513–515 ("a person": MQ5); landed+verified L951–952 (MQ4); step names L472–483; formats route to `conventions.md#name-formats` (DER-298 line) | Names, L41–58 |
| 465 | Heading Steps | kept; anchor `#steps` | L141 |
| 467–468 | Same names at every grain; headings and tickets use the name | kept | L143–145 |
| 470–471 | Step table header | kept; Read column from the DER-298 move | L148–149 |
| 472–480 | Entry … Review rows | kept; links and Read column from the DER-298 move; trailing periods and bold dropped; Plan/Spec add "the HLD" / "the LLD" | L150–158 |
| 481 | Trunk row: "Land project-main on the official copy" | kept; "the official copy" → trunk (banned name) | L159 |
| 482–483 | Changelog, Monthly rows | kept | L160–161 |
| — | Manager rows; Conventions row | kept from the DER-298 move; Conventions row: "old Stage numbers" moves to its own row | L162–164 |
| — | Old Stage numbers | route (owner: `docs/sdlc/conventions.md#in-flight-map`, the Stage table, kept there) | L165 |
| 485–486 | HLD and LLD are artifact names; steps are Plan and Spec | kept | Steps intro, L145–146 |
| 1097 | Heading "Skill table" | dropped: the table is gone (LLD C2); rows below name each note's home | — |
| 1099 | Ids and ownership: `SOURCES.md` | route (owner: `SOURCES.md`) | Roles, L37–38 |
| 1099 | Empty SHA = no body yet | route (owner: `SOURCES.md` L3–4, "Empty SHA cells mean no body may land") | Roles, L37–38 |
| 1100 | No marketplace install; no auto-update; see INTAKE | route (owner: `docs/INTAKE.md` L14, L32–33; also `SOURCES.md` L8) | Roles, L38–39 |
| 1102–1103 | Skill table header; Role column | route: which skill loads when → root `AGENTS.md` load table (standard Rule owners) | Roles, L37 |
| 1104 | `tracker-sdlc`: manager writes, architect reads; contract for all tracker reads and writes; loads the repo's tracker skill | kept here: all reads and writes (Tracker 1), manager the only writer (Tracker 2); also `AGENTS.md` L50, `SOURCES.md` L12 | L68–72 |
| 1105 | `sdlc-onboarding`: first tracker touch and Spec gate failure; proposes, writes `## Tracker`, `## Execution` on confirm | route (homes: `entry-brief-repo.md` L46–47, L67–68; `plan-trial-spec.md#spec` L57–58; `build-review.md#dispatch` L32; `SOURCES.md` L13) | — |
| 1106 | `cursor-cloud-agents-when`: empty dir until a first-party body | route (homes: `SOURCES.md` L19, empty SHA; `AGENTS.md` L168–171) | — |
| 1107 | `discover-the-idea`: chunk Brief Gather; load, do not paste; not on an incoming item | route (homes: `entry-brief-repo.md#chunk-brief` L27–31; `SOURCES.md` L14; `AGENTS.md` L44–45) | — |
| 1108 | `ux-design`: stories and UX at Plan; mockups at Spec if a screen; operator gate | route (homes: `plan-trial-spec.md#ux`, `#mockups`) | — |
| 1109 | `sdlc-artifacts`: templates; do not paste the SDLC into them | route (homes: `SOURCES.md` L15; `conventions.md#product-repo-layout` L53–54) | — |
| 1110 | `tdd`: fail-first | route (home: `SOURCES.md` `tdd` row; note missing there → handoff to the F item for `tdd`; also `build-review.md#debug-in-build` L63) | — |
| 1111 | `debug`: default; load on failure and on incoming-item Brief; alternatives | route (homes: `build-review.md#debug-in-build` L62–63; `entry-brief-repo.md#item-brief` L71–72; `SOURCES.md` L22) | — |
| 1112 | `docs-google-style`: human how-tos and agent-facing contracts after Spec | route (home: `plan-trial-spec.md#documentation`) | — |
| 1113 | `pr-review`: reviewer ≠ builder; receive-review on the builder; Standards vs Spec | route (homes: `build-review.md#review`; `SOURCES.md` L21) | — |
| 1114 | `security-hardening`: Always / Ask first / Never | route (home: `SOURCES.md` L26) | — |
| 1115 | `shell-safety`: classify before a command runs | route (home: `SOURCES.md` `shell-safety` row; note missing there → handoff to the F item for `shell-safety`; when to load: `AGENTS.md` L60) | — |
| 1116 | `verify-before-done`: Build; notify landed+verified; resume the verifier | route (homes: `build-review.md#definition-of-done`, `#debug-in-build` L64–67; `subagents.md#item-agents`) | — |
| 1117 | `grok-acp`: operator opt-in worker, Grok Build over ACP as the builder; label = `builder_id`; mint packs, resume delta-only; never verifier or reviewer of its own item | route (homes: `subagents.md#workers`; `SOURCES.md` grok-acp row, label and own-item notes added by this item) | — |
| 1118 | `pr-lens`: operator opt-in; local render + `gh --attach`; no canvas, no `analyze`; CLI pinned | route (home: `SOURCES.md` L34; `AGENTS.md` L137–140) | — |
| 1119 | `yagni`: smallest change for this Task; Brief Refine (chunk), removal alternative (item) | route (homes: `entry-brief-repo.md#chunk-brief` L33, `#item-brief` L76; `SOURCES.md` yagni row, "Smallest change that meets this Task" added by this item) | — |
| 1120 | `modern-python`: uv / ruff / ty / pytest | route (home: `SOURCES.md` L30) | — |
| 1121–1123 | `golang-testing`, `golang-safety`, `golang-security`: test shape; nil/slice/numeric traps; exploitable issues | route (home: `AGENTS.md` L199 language table, which moves to `language-router` at E7) | — |
| 1124 | `language-router`: pick at most one language-family skill | route (homes: `AGENTS.md` L53, L177; `SOURCES.md` L35) | — |
| 1125 | `lang-*`: pointers or language guides | route (homes: `AGENTS.md` L142–166, L193–195; `SOURCES.md` L36–57) | — |
| 1127 | Pin SHAs in `SOURCES.md` | route (owner: `SOURCES.md` L3; `docs/INTAKE.md` step 4) | Roles, L37–38 |
| 1127–1128 | **security** intake before any vendor content; see INTAKE | route (owner: `docs/INTAKE.md`) | Roles, L38–39 |

Notes:

1. The standard's Rule owners row gives "use only the roles in the
   table" to the root `AGENTS.md` Research row. This file carries it
   beside the role table, as the Trial draft does. C11 routes the
   `AGENTS.md` line here, or the standard's owner row is corrected.
2. The open-blocker definition (old L791–792) now lives in `#tracker`.
   Its copy in `docs/sdlc/build-review.md#build` L7–8 becomes a route at
   C6. The Names definitions have copies in `entry-brief-repo.md#entry`
   (chunk, item), `trunk-changelog-monthly.md#trunk` (trunk) and
   `branches-and-lands.md#branches` (trunk, project-main); C3, C7 and C8
   route them to `#names`.
3. `SOURCES.md` is not agent text; this item adds two Notes phrases
   (grok-acp, yagni rows) so each skill-table note has a home. Rows
   whose Notes an F item owns (`tdd`, `shell-safety`) are handed off.

## Meaning questions

Resolved from the current text:

- **MQ1** (old L597): the HLD's rule owners decide "use only the roles in
  the table"; step jobs are agents acting in those roles.
- **MQ2** (old L62): the write-up is the brief (old L152, L298, L304).
- **MQ3** (old L96): after-act = record on the board after the fact
  (old L460).
- **MQ4** (Names): landed+verified as defined at old L460–461 and
  L951–952.
- **MQ7** (old L12): "an id here" meant the skill table, whose ids are
  the `SOURCES.md` ids (old L1099); the rule does not change.
- **MQ8** (old L1104): "architect (reads)" narrows nothing: old L84
  sends every read, by any role, through `tracker-sdlc` (Tracker 1).

Resolved by the operator:

- **MQ5** (old L29, L70–74, L104, L513), operator clarification
  2026-09-27: "a person" means the operator, or someone the operator
  names in writing. Applied at those places only.
- **MQ6** (old L11), operator clarification 2026-09-27: "Improvise when
  the work needs it" → "If no listed skill fits the task, do the work
  without one. Never create a new skill id mid-task."

No open MQ.
