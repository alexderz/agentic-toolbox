# Rule map — root `AGENTS.md`

Item: DER-308 (C11).

Old: `AGENTS.md` at main 7a11696, lines 1–245. New: [`AGENTS.md`](../../../../AGENTS.md).
Old = project-main 120d298 except old L45, whose links DER-298 (C1)
retargeted from `docs/SDLC.md#entry`, `#brief` to
`docs/sdlc/entry-brief-repo.md#entry`, `#brief`.
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line in the old file;
"L" in New location = line in the new file.

Protected rows (writing standard, Protected rules): public-repo rule,
old L16–32. Every row below is `kept`, unchanged, at the same line
numbers. Check: `diff <(git show 7a11696:AGENTS.md | sed -n 16,32p) <(sed -n 16,32p AGENTS.md)`
→ empty. **security** reads them at Review.

Operator clarifications (2026-09-27): "Improvise" (old L81) now lives in
its owner `docs/SDLC.md#roles`; "a person" (old L43 row name) → row
**Ask the operator**, linking the owner heading "Asking the operator".
The other clarifications have no subject in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–5 | Shared skills home, not an application repo; Claude Code arrives from `CLAUDE.md`; stay here, then load what it names | kept | L3–5 |
| 7–8 | Git is the source of truth; no skill bodies only on a mirror | kept | L7–8 |
| 10–14 | `maintainers/` holds build notes; toolbox users skip it; repo workers read `maintainers/AGENTS.md` next; its `## Tracker` governs | kept | L10–14 |
| 16 | Heading "Public repo"; anchor `#public-repo` (linked from `maintainers/AGENTS.md`) | kept, unchanged | L16 |
| 18 | Public, open-source repo | kept, unchanged | L18 |
| 20–27 | Deliverables: outside readers, professional voice, style guide; no names, attributions, private tracker URLs, hostnames, IPs, credentials, session leftovers; bare ticket ids fine | kept, unchanged | L20–27 |
| 28–30 | Agent context may be informal: civil, credential-free, not tone-reviewed | kept, unchanged | L28–30 |
| 31–32 | Commit messages, PR descriptions, tags are public and permanent | kept, unchanged | L31–32 |
| 34 | Heading "How to load" | kept | L34 |
| 36 | Do not paste skill or SDLC bodies into this file | kept | L36 |
| 36–38 | Read the named path, or pack it into a subagent prompt, "see Spawn prompts in the SDLC" | kept; prose section name fixed (LLD Links, L37) → link `docs/sdlc/subagents.md#spawn-prompts`; parenthesis → sentence (standard 8) | L36–38 |
| 40–41 | Load table header `What \| When \| How` | kept | L40–41 |
| 42 | SDLC row: any project, ticket, chunk, multi-agent run → read `docs/SDLC.md` before implementing | kept | L42 |
| 42 | SDLC row: "Owns named steps, grain, asking the human, project-main, subagents, pack vs point, land path, conventions" | dropped: description, not a rule (owner of the reading order: `docs/SDLC.md#how-to-read`, `#steps`) | — |
| 43 | Row "Need a person": any gate, waiver, blocker, unclear choice → Asking the human | kept as row **Ask the operator**, When unchanged; route (owner `docs/SDLC.md#asking-the-human`) | L44 |
| 43 | Stop; template `ask-human.md` parts; wait blocks this issue, others proceed; do not continue until they answer | dropped: duplicate (owner `docs/SDLC.md#asking-the-human` steps 1, 2, 6 and "While you wait"; shape: `skills/sdlc-artifacts/templates/ask-human.md`) | L44 route |
| 44 | Requirements: chunk Gather → read `discover-the-idea` | kept, as row **Requirements** (Gather) | L45 |
| 44 | Refine: load `yagni` on a **different** agent | kept, as row **Refine**, "as the refiner agent" (MQ4); the different-agent rule: owner `docs/sdlc/subagents.md#step-agents`, `docs/sdlc/entry-brief-repo.md#chunk-brief` | L46 |
| 44 | Loop is in the SDLC | dropped: duplicate (owner `docs/sdlc/entry-brief-repo.md#chunk-brief`) | — |
| 44 | No language skill on a gather- or refine-only turn | route (owner `skills/language-router/SKILL.md#no-language-turns`) | L56 |
| 45 | Incoming item: read Entry + Brief first | kept; Brief link narrowed to its item subsection `#item-brief` | L47 |
| 45 | Do not load `discover-the-idea` on an incoming item | kept | L47 |
| 45 | Do not implement yet; problem + fix vs removal, then align Plan/Spec | dropped: duplicate (owner `docs/sdlc/entry-brief-repo.md#entry` "Do not implement here", `#item-brief` steps 1–2; `docs/SDLC.md#grain` Item row) | — |
| 46 | Research: purchase, shortlist, market research → **researcher** persona reads `buying-researcher` when that ask is in play; not an SDLC step | kept; "when that ask is in play" = the When column; "Not an SDLC role or step" routes to `docs/SDLC.md#roles` (standard Rule owners; MQ2) | L48 |
| 47 | UX: **designer** reads `ux-design` | kept | L49 |
| 47 | Agent review vs requirements, no reviewer taste; then the human unless they waive | dropped: duplicate (owner `docs/sdlc/plan-trial-spec.md#ux`) | — |
| 48 | Artifacts: when; read `sdlc-artifacts`, copy the matching template | kept | L50 |
| 48 | Chunk brief stays `discover-the-idea`; incoming item `bug.md` / `task.md` | kept; "(problem + fix vs removal)" dropped: duplicate (owner `skills/sdlc-artifacts/SKILL.md` Map, Incoming item row) | L50 |
| 49 | Debug row: new ticket → Incoming item; in Build read `debug` default, alternatives, load one, then `tdd` + `verify-before-done`; troubleshooter may load `debug` at item Brief and must not implement | kept; "(not already in Build)" out of the parenthesis (standard 8) | L51 |
| 50 | Tracker row: read `tracker-sdlc`; product repo's own `## Tracker`; the skill loads the repo tracker skill or `sdlc-onboarding` | kept; When parenthesis → colon list | L52 |
| 51 | Docs row: read `docs-google-style` | kept | L53 |
| 51 | Human: what it is, how it works, how to use it; agent: locatable contracts | dropped: duplicate (owner `docs/sdlc/plan-trial-spec.md#documentation` table) | — |
| 52 | A skill: read `skills/<id>/SKILL.md` | kept | L54 |
| 52 | "Ids are listed below" | route (owner `SOURCES.md`, standard Rule owners "Skill inventory") | L55 |
| 53 | Language row: code turn; at most one language skill; table below, or `language-router` first if ambiguous; pointers do not count | route, one row (owner `skills/language-router/SKILL.md` `#iron-law`, `#map`); "at most one language skill per turn" named in the row with a link to `#iron-law`; "if ambiguous" → read the router on every code turn (MQ3) | L56 |
| 54 | Pins / intake: third-party content, or checking ownership → `SOURCES.md`, `docs/INTAKE.md` | kept, split one file each: ownership and pins → row **Skill ids**; third-party content → Intake section | L55, L65–66 |
| 55 | Knowledge: read `knowledge/README.md`, then the note | kept | L61 |
| 55 | Do not remint as a skill; live vendor docs win | dropped: duplicate (owner `knowledge/README.md` L3–6, L50) | — |
| 57–59 | Process skills that may load with the one language skill | route (owner `skills/language-router/SKILL.md#load-with-list` item 1) | L56 |
| 60 | `shell-safety` when the turn includes shell | route (owner `#load-with-list` item 2) | L56 |
| 60–62 | `discover-the-idea` gather-only, `buying-researcher` research-only: no language skill | route (owner `#no-language-turns`) | L56 |
| 64 | Skills live under `skills/<id>/` | kept, in row **A skill** | L54 |
| 64–65 | Knowledge lives under `knowledge/<domain>/<kind>/` | kept, in row **Knowledge** | L61 |
| 65–66 | No second process pack beside these ids | dropped: duplicate (owner `docs/INTAKE.md` checklist 1) | L65–66 route |
| 68 | Heading "Skills are tools, keyed by role" | dropped: section out (LLD C11) | — |
| 70–79 | Role table, including the `researcher` row | route (owner `docs/SDLC.md#roles`, the DER-299 index); wording differences resolve to the owner (MQ6); `researcher` only in row **Research** | L43, L48 |
| 81 | Pick the tool that matches the role | route (owner `docs/SDLC.md#roles` "Skills are tools, keyed by role") | L43 |
| 81 | "Improvise when the work needs it" | route (owner `docs/SDLC.md#roles`, replaced per operator clarification 2026-09-27) | L43 |
| 82 | Do not remint a skill that already has an id here | route (owner `docs/SDLC.md#roles`); see MQ1 | L43 |
| 84–86 | Per item: mint a clean builder and a clean verifier; resume them later; never reuse the builder as the verifier | route (owner `docs/sdlc/subagents.md#item-agents`) | L60 |
| 86–89 | On mint, pack or point; host default reads the skill files; resume is delta-only | route (owner `docs/sdlc/subagents.md#spawn-prompts`) | L60 |
| 91–93 | Branch items off project-main when it exists; land each merge-ready item there, serialized; land project-main on trunk | route (owner `docs/sdlc/branches-and-lands.md#branches`, `#project-main`; Trunk: `docs/sdlc/trunk-changelog-monthly.md#trunk`) | L59 |
| 93–95 | Incoming item, no live project-main: branch from trunk, Review vs trunk, local merge; do not invent a project-main | route (owner `#branches`; `docs/sdlc/build-review.md#review` diff range; `#land-path`) (MQ8) | L59 |
| 97–98 | No PRs; Review is an explicit gate; push for durability; manager orders local, serialized lands | route (owner `docs/sdlc/branches-and-lands.md#land-path`) | L59 |
| 98 | Groom writes a reviewed `groom.md`, then sets blockers through `tracker-sdlc` | dropped: duplicate (owner `docs/sdlc/groom-step.md#procedure`; reached from row **SDLC**) | — |
| 99 | Do not start or land an item with an open blocker unless the operator said so | route (owner `docs/sdlc/branches-and-lands.md#never`; `docs/sdlc/build-review.md#open-blockers`) (MQ7) | L59 |
| 100–101 | "Full rules: docs/SDLC.md (Groom, Build, Project-main, Subagents per work item, Spawn prompts)" | prose section names fixed (LLD Links, L100–101): replaced by rows linking each file | L42, L59–60 |
| 103 | Heading "Inventory" | dropped: section out (LLD C11) | — |
| 105 | Authoritative table: `SOURCES.md`; bundles: `README.md` | route: row **Skill ids** (owner `SOURCES.md`); bundles kept in Related | L55, L70 |
| 107 | Skill ids with `SKILL.md`; do not remint without a new **security** cut | ids: route (owner `SOURCES.md`); remint clause split by actor (MQ1): agents at work never remint, route to `docs/SDLC.md#roles`; a skill-body change is maintainer work through `docs/INTAKE.md` plus a new **security** cut | L55 |
| 109–127 | Process skill ids list | dropped: duplicate (owner `SOURCES.md` L12–33) | — |
| 129, 131 | Research, not SDLC: **researcher** loads `buying-researcher` when relevant | dropped: duplicate (owner row **Research**; `SOURCES.md` L17) | L48 |
| 133 | Workers: operator opt-in; load only when the operator picks that worker | kept, as row **Workers** | L57 |
| 135 | `grok-acp`: Grok Build over ACP as a builder | kept, row **Workers** When | L57 |
| 135 | Client is the package `packages/grok-acp/` | dropped: duplicate (owner `SOURCES.md` L18, L66) | — |
| 137–138 | Diagrams: operator opt-in; load only when the operator asks, such as a diagram in the PR into `main` | kept, as row **Diagrams** | L58 |
| 140 | `pr-lens`: PR Lens diagrams; local render + PR attach only | id kept in row **Diagrams**; scope dropped: duplicate (owner `SOURCES.md` L34, `skills/pr-lens/SKILL.md`) | L58 |
| 142 | Language pack; do not remint the Go / Python / Shell ids | dropped: duplicate (owner `skills/language-router/SKILL.md#iron-law`) | L56 route |
| 144–166 | `language-router`, pointers and `lang-*` ids | dropped: duplicate (owner `SOURCES.md` L35–57; pointers: `skills/language-router/SKILL.md#iron-law`, `#map`) | — |
| 168–169, 171 | First-party placeholder `cursor-cloud-agents-when`; no body claim until SHA and `SKILL.md` on `main` | dropped: duplicate (owner `SOURCES.md` L3–4, L19; `docs/INTAKE.md` Layout-only exception) | — |
| 173 | Load by id from this repo | kept, in row **A skill** | L54 |
| 175 | Heading "Language routing" | dropped: section out (LLD C11); owner `skills/language-router/SKILL.md` | — |
| 177–178 | At most one language skill; a second only for a mixed-language diff; never load the catalog | route (owner `skills/language-router/SKILL.md#iron-law`, DER-318 map); "at most one" named at L56 with the `#iron-law` link | L56 |
| 179–181 | Process skills that may load alongside | route (owner `#load-with-list`) | L56 |
| 182–187 | Onboarding, gather/refine-only, incoming-item Brief, UX-only, research-only turns load no language skill | route (owner `#no-language-turns`) | L56 |
| 187–188 | Load one of `debug` / `debug-pocock` / `debug-anthropic` | route (owner `#load-with-list` item 3); also kept in row **Debug** | L51, L56 |
| 190–191 | `language-router` first if the table is ambiguous, then the one skill it names | route; changed at E7 to every code turn (MQ3) | L56 |
| 193–195 | Pointer ids exist so every language has a file; not a load; they route | route (owner `#iron-law`, `#map`) | L56 |
| 197–220 | Language table | route (owner `#map`; merged at E7) | L56 |
| 222–223 | Stubs: no skill body, official docs only | route (owner `skills/language-router/SKILL.md#stubs`) | L56 |
| 225–226 | Frameworks are not language skills; do not invent one | route (owner `skills/language-router/SKILL.md#family-rules`) | L56 |
| 228 | Heading "Intake (security)" | kept | L63 |
| 230, 233 | Before any third-party content, complete **security** intake (`docs/INTAKE.md`) | kept, as one route (owner `docs/INTAKE.md`) | L65–66 |
| 232 | Pin the cherry-pick SHA in `SOURCES.md` | route (owner `docs/INTAKE.md` checklist 4) (MQ5) | L65–66 |
| 234–235 | No marketplace install, no auto-update, no scripts, no secrets | route (owner `docs/INTAKE.md` checklist 1, 2, 5, 6) | L65–66 |
| 237 | Empty SHA cells mean the body must not exist yet | route (owner `SOURCES.md` L3–4; `docs/INTAKE.md` checklist 4) | L55, L65–66 |
| 239 | Heading "Related" | kept | L68 |
| 241–245 | README, SDLC, Knowledge, License, Claude Code entry | kept; README label names its bundles (old L105) | L70–74 |

New lines with no old line, each a route the standard's Rule owners
list for `AGENTS.md`: L43 row **Roles** (`docs/SDLC.md#roles`); L52
"Only the **manager** writes" (`docs/SDLC.md#tracker`); L59 row
**Branches and lands** (`branches-and-lands.md`); L60 row **Subagents**
(`subagents.md`, pack vs point and workers).

## Meaning questions

Resolved by the operator:

- **MQ1** (old L107 vs old L82): resolved by operator 2026-09-27 (Q13):
  split by actor. L82 and its owner `docs/SDLC.md#roles` L20 say "Do not
  remint a skill that already has an id"; L107 says "do not remint
  without a new **security** cut". Ruling: agents doing a task never
  remint a skill (owner `docs/SDLC.md#roles`, unchanged); changing a
  skill body is maintainer work through `docs/INTAKE.md` plus a new
  **security** cut. Row **Skill ids** (L55) states both.

Resolved from the text:

- **MQ2** (old L46): "Not an SDLC role" is added as a route, not a new
  rule: the standard's Rule owners row gives `docs/SDLC.md#roles` the
  owner of "`researcher` is not an SDLC role; use only the roles in the
  table", with the Research row as the route.
- **MQ3** (old L53, L190–191): "`language-router` first if ambiguous"
  → read it on every code turn. The owner changed this at E7 (DER-318
  rule map MQ1, from the HLD, LLD E7 and the ticket Outcome); this
  file routes to the owner's rule.
- **MQ4** (old L44): "load `yagni` on a **different** agent" → row
  **Refine** "as the refiner agent". `docs/sdlc/subagents.md#step-agents`
  and `entry-brief-repo.md#chunk-brief` L33, L39–41 define the refiner
  as never the gatherer; same meaning.
- **MQ5** (old L230–235): old order "pin, then intake" vs the owner's
  checklist, where the pin is step 4, before the body lands. Both put
  the pin before the body; the owner's order stands.
- **MQ6** (old L70–79): the old role table differs in wording from
  `docs/SDLC.md#roles` (tester, security, manager, operator jobs;
  `researcher` row). The owner's table was mapped `kept` or `route` at
  DER-299 (protected, C2); this file routes to it.
- **MQ7** (old L99): "unless the operator said so" =
  `branches-and-lands.md#never` "without an operator call"; the
  resolve-first and defer steps live in `build-review.md#open-blockers`.
- **MQ8** (old L93–95): each part has an owner line —
  `branches-and-lands.md#branches` L9, L11–12 (trunk if none; no
  project-main for a lone incoming item), `build-review.md#review`
  L95–96 (diff vs trunk), `#land-path` L38 (local merge into trunk).

## DER-290: `ui-craft` load row

Old: `AGENTS.md` at project-main 88455d8, lines 1–74. New: lines 1–75
(cap 100). Changed rows only; every other line is unchanged (old L1–58 →
L1–58, old L59–74 → L60–75).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | Load row **UI craft**: a builder implementing or reviewing UI code reads `skills/ui-craft/SKILL.md`, beside `ux-design`, not in its place; upstream instead is operator opt-in, asked in the skill | new: this file owns "which skill loads when" (writing standard, Rule owners); the ask rule lives in `skills/ui-craft/SKILL.md` (route). Source: operator decisions 2026-09-27, [intake note](../../ui-craft-intake/intake.md) | L59 |

DER-290 meaning questions: none. One row added; no existing rule changes.

## DER-351: every message to the operator routes to Asking

Old: `AGENTS.md` at project-main 63f6b72, lines 1–75. New: lines 1–75
(cap 100; K2: no growth). Changed rows only; every other line is
unchanged.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 44 | Row **Ask the operator**: any gate, waiver, blocker, or unclear choice → read Asking the operator | kept, edited in place; renamed **Message the operator**; When widened to any message to the operator: an ask (the same four triggers), a status, or a report; route unchanged (owner `docs/SDLC.md#asking-the-human`, whose opening line holds the ticket ID-plus-slug rule). Source: operator rule 2026-09-27; DER-351 review | L44 |

DER-351 meaning questions: none. The ask triggers are unchanged; the row
adds status and report messages, which reach only the owner's opening
line (the numbered ask steps still apply to a decision).
## DER-352: `ui-craft` row routes to the ask

Old: `AGENTS.md` at project-main 63f6b72, lines 1–75. New: lines 1–75
(cap 100). Changed row only; every other line is unchanged.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 59 | Load row **UI craft**: read `skills/ui-craft/SKILL.md` beside `ux-design`, not in its place; "Upstream instead is operator opt-in, once per product repo: the skill's ask" | Load rule **kept**. The option clause → **route**: "Which version, or none:" linked to the skill's `#which-version-ask-once-per-product-repo`, the owner of the three answers. The row no longer lists options, so a new answer cannot drift from it | L59 |

DER-352 meaning questions: none. The row adds no condition (standard 5);
upstream opt-in and its risk text stay in the owner's ask and Never.
