# HLD — Instruction refinement: agent text that works across model strengths

- Slug: `instruction-refinement`
- Track / chunk ids: skills-home process track; chunk DER-288 (also
  delivers DER-265 and DER-271's wording bullets)
- Brief: confirmed by the operator 2026-09-26 (on DER-288)
- Date: `2026-09-26`

## Required

- **Problem** — Agent text is long (`AGENTS.md` 245 lines, SDLC 1128,
  45 skills), duplicated (role table in 4 files, 7 or 8 roles; land,
  subagent, language and skill-list rules twice or more), mixed with
  people text, and leans on judgment ("not too dirty to reason"),
  synonyms (manager / parent / orchestrator) and nested conditions
  (item Brief step 4). Small local models (Qwen family) lose these.
- **Goals** — (1) One writing standard applied to every agent file in
  scope. (2) Each rule in one file; others route. (3) `docs/SDLC.md`
  becomes a short index; steps load on demand. (4) People text moves
  out, content unchanged. (5) A basic eval shows no regression vs `main`.
- **Non-goals** — Any process change (roles, gates, steps, tracker
  verbs, states, contract version, template shapes, branch and land
  rules, what the person approves). DER-271's process bullets.
  `packages/`, `knowledge/`, `maintainers/design/` (except DER-271's
  stale lines in `tracker-sdlc/hld.md`), CI (DER-267), single-model
  tuning, rewording people text; DER-286, DER-253, DER-266, DER-287.
- **Users / operators** — Agents on any model, from the local Qwen
  family (variant from the harness notes) to frontier; the maintainer,
  who reads eval reports and decides.
- **UX / stories** — `n/a`: no screen, no end-user journey; readers are
  agents and the maintainer; the people doc moves unchanged. Operator
  wrote `UX verification not required` (2026-09-26).
- **Comparables** — [comparables.md](comparables.md)

### Writing standard (checkable on the diff)

1. Procedures are numbered steps, one action each; a step for another
   actor starts with that role in bold.
2. Decisions are if/then or a condition → action table. Each condition
   is checkable from files, tracker state, or the person's written
   words. No "use judgment", "when appropriate", "not too X".
3. One name per thing, defined in one line at first use in its owner
   file: `manager` (never orchestrator / parent), `trunk` (never
   official copy), `project-main`, role and step names. Grep bans the
   synonyms in agent text.
4. No forward references inside a file.
5. One owner per rule (table below). Elsewhere, at most a one-line
   route naming the rule and linking the owner by path and anchor; a
   route adds no condition. No rule assembled from several sections.
6. Routing is one hop: every agent file is linked from its entry
   (`AGENTS.md`, SDLC index, or its `SKILL.md`); a routed file needs no
   second hop to finish a rule.
7. Most-violated rule first (Iron law stays first). Every "never" names
   the allowed action beside it.
8. Imperative sentences, one instruction each; no condition hidden in a
   parenthesis. No metaphor. No self-deleting or dated conditions.
9. Caps: `SKILL.md` ≤250; `tracker-sdlc` ≤150 (DER-265); SDLC index
   ≤200, step files ≤150; root `AGENTS.md` ≤100. Rewrites never grow.
10. Each item carries a **rule map**: every old rule → kept / merged
    into owner / route / dropped duplicate, with its new location. The
    reviewer checks the map, not only the prose.

### Rule owners

| Rule | Owner | Others route |
| --- | --- | --- |
| Roles; names manager, trunk, project-main | SDLC index | all |
| Only the manager writes the tracker | SDLC index (roles) | `tracker-sdlc`, `sdlc-artifacts` |
| When to ask the person | SDLC index `#asking-the-human` | skills |
| Ask message shape | template `ask-human.md` | SDLC (no inline copy) |
| Branches, project-main, land path | SDLC branches-and-lands | `AGENTS.md` L83–102 |
| Mint, resume, pack vs point, workers | SDLC subagents | `AGENTS.md`, `pr-review`, `verify-before-done` |
| Language map, load-with list, no-language turns | `language-router` | `AGENTS.md` (one row) |
| Skill inventory | `SOURCES.md` | `AGENTS.md` list, SDLC skill table dropped |
| Third-party intake | `docs/INTAKE.md` | `AGENTS.md`, `SOURCES.md` |
| Public-repo voice | root `AGENTS.md` | `maintainers/AGENTS.md` |

`researcher` stays only in the `AGENTS.md` Research row (not an SDLC
role); "no ninth role" → "use only the roles in the table". Empty
`cursor-cloud-agents-when` leaves `AGENTS.md`; its SOURCES row stays.

- **Shape** — **Layout: split `docs/SDLC.md` into an index plus step
  files.** Today every agent loads ~860 agent lines to act on one step;
  instruction density and near-duplicate text hurt small models most
  (comparables). `docs/SDLC.md` stays the entry path (product-repo
  stubs point at it) and keeps `#asking-the-human` (linked from
  `AGENTS.md` and two skills).

  | File | Holds | Lines |
  | --- | --- | --- |
  | `docs/SDLC.md` | How to read, names, roles, hierarchy + tracker rule, grain, asking the human, step → file table | ≤200 |
  | `docs/sdlc/entry-brief-repo.md` | Entry, Brief (chunk, item), Repo | ≤150 |
  | `docs/sdlc/plan-trial-spec.md` | Plan, Trial, Spec, Documentation | ≤150 |
  | `docs/sdlc/groom-step.md` | Groom, late insertion, incoming item | ≤150 |
  | `docs/sdlc/build-review.md` | Build, dispatch, DoD, Review | ≤150 |
  | `docs/sdlc/trunk-changelog-monthly.md` | Trunk, Changelog, Monthly | ≤80 |
  | `docs/sdlc/branches-and-lands.md` | Project-main, land path, branch names | ≤120 |
  | `docs/sdlc/subagents.md` | Subagents per item, spawn prompts, workers | ≤150 |
  | `docs/sdlc/conventions.md` | Product layout, changelog, commits, designs in git | ≤100 |

  Names provisional (LLD fixes them; no basename equal to a template).
  Index rule: find your step, read that one file; the manager also reads
  branches-and-lands and subagents. Rejected: one slimmed file (Trial
  fallback); one file per step (12 tiny files, more hops); a glossary.

  **People doc:** SDLC lines 119–384 ("How software gets built" through
  the examples) move to `docs/how-software-gets-built.md`: content
  byte-identical, plus one H1, headings raised one level. README link
  and the "no analogies outside" route point there.

  **Root `AGENTS.md`** keeps: what this repo is, public-repo rule, the
  load table (one row per need, one file each), intake route, related.

  **Hazards (LLD examples):** end-of-chunk Brief → numbered list; item
  Brief step 4 → condition table; pack vs point → "manager holds the
  bodies and the child needs them: pack; else point"; Stage map → no
  open ticket cites a Stage number: delete as it says; else ask.

  **Eval step** (this skills home's maintainer practice only). Rule in
  `maintainers/AGENTS.md` (when, who decides); procedure, fixtures and
  answer keys in `maintainers/evals/`; harness-agnostic (what to give
  the agent, not how to run it).
  - Tasks, one run each per model: T1 onboard a scratch repo (`local`
    adapter); T2 Groom a toy chunk (key holds the right blocker graph);
    T3 Build one of its items to land. Person replies are scripted.
  - Checklist per task (`pass`/`fail`/`n/a`): C1 asks the person where
    required; C2 only the manager writes the tracker; C3 blocker links
    match the key; C4 Review never skipped; C5 builder, verifier,
    reviewer distinct. Plus completed, tokens in/out, wall time (never
    decisive). Scorer: the person or a clean agent; evidence is a short
    phrase, never a quote.
  - Files: `maintainers/evals/runs/<YYYY-MM-DD>-<sha7>-<model-slug>.md`
    (commit, arm, model + variant + quantization, harness + version,
    scorer, a row per task); `maintainers/evals/baseline.md` (per
    model). No hostnames, paths, user names, transcripts.
  - Cadence: first run on `main`; each PR into `main` changing agent
    text gets a run, regressions listed first; a person decides; merged
    runs become the baseline; new daily-driver model → re-baseline.
- **Persistence** — Git: this directory, rewritten files,
  `maintainers/evals/`. Tracker: DER-288, items. Transcripts: harness.
- **Worker rules** — SDLC as today. The reviewer checks each diff
  against the standard and the rule map. **security** reads every
  edited vendor-derived body and the eval step. A change to a role,
  gate, step, verb, state, template shape, or person approval → stop,
  block that item, ask. An ambiguous old rule is a meaning decision →
  ask; never pick a meaning while rewording.
- **Open** — Harness details (models, quantization, how runs start):
  needed before Spec; Trial and the before-merge run wait on them.
  People doc path `docs/how-software-gets-built.md`: operator OK
  (2026-09-26).

## Optional

### Work areas (Groom may split into waves)

| Id | Area | Needs |
| --- | --- | --- |
| A | Standard + owner map → `maintainers/writing-standard.md`, routed from `maintainers/AGENTS.md` | — |
| B | Eval procedure, fixtures, keys, run format, `maintainers/AGENTS.md` rule | — |
| B1 | Baseline run on `main` (by hand) | B, harness; before any land |
| C | SDLC index + step files + people doc + `AGENTS.md` slim; drop "(an operator-confirmed rule)" | A |
| D | `tracker-sdlc` ≤150 (DER-265); `sdlc-onboarding` (replace `maintainers/` example pointer); `sdlc-artifacts` + templates ("land SHA" wording; agents-stub names `## Tracker`) | A |
| E | First-party: `discover-the-idea`, `yagni`, `buying-researcher`, `grok-acp`, `security-hardening`, `modern-python`, `language-router` (owns map; onboarding joins no-language turns) | A |
| F | Vendor-derived light pass (naming, dedupe, real defects): `tdd`, `pr-review`, `debug*`, `docs-google-style`, `verify-before-done`, `golang-*`, `pr-lens`, `ux-design`, `shell-safety`; SOURCES note each | A, **security** |
| G | `lang-*` naming + dedupe, no eval | A |
| H | `docs/INTAKE.md` | A |
| I | Tone pass `README.md`, `CONTRIBUTING.md`, `docs/ARCHITECTURE.md` + link fixes; role tables in `README.md` / `docs/ARCHITECTURE.md` corrected to the SDLC roles (operator, 2026-09-26) | C paths |
| J | Stale lines in `maintainers/design/tracker-sdlc/hld.md` | — |
| K | Before-merge run (rewrite arm), report in the PR into `main` | all, harness |

The LLD publishes the final file and anchor map, so D–I link to it and
need C only at land (land order, not a blocker). Vendor-derived = the
`SOURCES.md` Upstream names a third party, intent pins included.
`adapters/local.md` fenced recipe stays byte-identical (diff check).

### PoC questions (Trial: current text vs rewrite)

Rewrite `sdlc-onboarding` and Groom (index + step file) on a scratch
branch; run T1, T2 in both arms on the weakest and one frontier model.
(1) Does the weak model make the index → step-file hop? (2) Do passes
hold, tokens fall? (3) Does frontier hold? Evidence: `poc.md` here. Hop
fails → one slimmed `docs/SDLC.md` (~550 lines), decided before Spec.

### Trust boundaries (for Spec)

- Eval: local harness, scratch repos outside this repo, `local` adapter,
  no credentials; never here (this repo's `## Tracker` is a live hosted
  tracker). Results are public: the security read of B checks the
  format bars hostnames, paths, transcripts.
- Vendor-derived edits add no upstream text (not new intake); pins and
  least privilege unchanged; **security** reads each body.
- Product repos: `docs/SDLC.md` path and `#asking-the-human` stay;
  `templates/tracker-skill.md` keeps its shape (no contract bump).

### Risks

- Rewording shifts meaning → rule map, reviewer, eval. n=1 is noisy and
  the weak model may fail T2/T3 on both arms → report as is; the person
  may ask for a rerun. Tokens compare within one model.
- `README.md` / `docs/ARCHITECTURE.md` role tables disagree with the
  SDLC → fixed in area I (operator, 2026-09-26), content limited to the
  role tables.
