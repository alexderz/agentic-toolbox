# LLD — Instruction refinement: agent text that works across model strengths

- Slug: `instruction-refinement`
- HLD: [hld.md](hld.md) · Trial kit: [poc/](poc/poc.md)
- Tickets this LLD covers: DER-288 (chunk; also DER-265 and DER-271's
  wording bullets); items filled at Groom
- Date: `2026-09-26`

Old text = `main` 7a11696 (`docs/SDLC.md` 1128 lines); "Old L" cites it.

## Required

### Paths / modules: file and anchor map

Final names; no basename equals a template. C1 creates every heading
below (old anchor in parentheses); later items keep them. Caps apply
from the rewrite items on.

| File | Old L (moved in C1) | Anchors, H2 unless noted (old) | Cap |
| --- | --- | --- | --- |
| `docs/SDLC.md` (index) | 1–118 minus people text; 465–487; 1097–1128 (skill table, gone at C2) | `#how-to-read`, `#roles`, `#names`, `#tracker` (`#hierarchy-issue-tracker`), `#grain` (`#grain-how-you-enter`), `#asking-the-human` (kept: explicit `<a id>`, heading "Asking the operator"), `#steps` | ≤200 |
| `docs/sdlc/entry-brief-repo.md` | 511–610 | `#entry`, `#brief`, `#chunk-brief` (H3), `#item-brief` (H3), `#repo` | ≤150 |
| `docs/sdlc/plan-trial-spec.md` | 612–698; 955–958 | `#plan`, `#comparables` (H3), `#ux` (H3), `#trial`, `#spec`, `#mockups` (H3), `#security-gate` (H3), `#documentation` (`#documentation-after-spec`) | ≤150 |
| `docs/sdlc/groom-step.md` | 700–785; 970–972 | `#names`, `#iron-law`, `#blockers`, `#waves`, `#gates`, `#review-items`, `#procedure`, `#late-insertion`, `#incoming-item`; old `#groom` = file top | ≤150 |
| `docs/sdlc/build-review.md` | 787–868; 1088 | `#build`, H3 `#open-blockers`, `#dispatch`, `#definition-of-done`, `#debug-in-build`, `#skills-home-dod`; `#review` | ≤150 |
| `docs/sdlc/trunk-changelog-monthly.md` | 870–900 | `#trunk`, `#changelog`, `#monthly` | ≤80 |
| `docs/sdlc/branches-and-lands.md` | 902–954; 959 | `#branches`, `#project-main` (`#project-main-intermediate-integration`), `#land-path` (`#land-path-manager`), `#never` | ≤120 |
| `docs/sdlc/subagents.md` | 963–1087 | `#step-agents`, `#item-agents` (`#subagents-per-work-item`), `#fallback`, `#tracker-writes`, `#writable-worktree`, `#spawn-prompts` (`#spawn-prompts-pack-vs-point`), `#workers` | ≤150 |
| `docs/sdlc/conventions.md` | 385–463; 488–509; 960–961; 1090–1095 | `#name-formats` (`#conventions-optional-recommended`, old `#names`), `#commits`, `#product-repo-layout`, `#changelog-and-connection`, `#designs-in-git` (`#git-designs-from-onset`), `#in-flight-map` (`#in-flight-map-old-numbers`; until C10) | ≤100 |
| `docs/how-software-gets-built.md` | 119–383 | one H1, headings raised one level (`#how-software-gets-built`) | — |
| `maintainers/writing-standard.md` | — (A) | `#standard`, `#names`, `#rule-owners`, `#rule-maps`, `#checks` | ≤150 |
| `maintainers/evals/…` | — (B) | [Eval step](#eval-step) | — |

Index **How to read** (Trial draft): find your step in Steps, read that
row's file; **manager** → also `branches-and-lands.md`, `subagents.md`.
Steps gains a "Read" column and rows for the last three step files.

**Links.** C1 turns the 21 internal links of old SDLC into `path#anchor`
and updates the 4 inbound anchors that break:

| File | Old | New |
| --- | --- | --- |
| `AGENTS.md` | `docs/SDLC.md#entry` | `docs/sdlc/entry-brief-repo.md#entry` |
| `AGENTS.md` | `docs/SDLC.md#brief` | `docs/sdlc/entry-brief-repo.md#brief` |
| `README.md` | `docs/SDLC.md#how-software-gets-built` | `docs/how-software-gets-built.md` |
| `skills/pr-lens/SKILL.md` | `SDLC.md#monthly` | `sdlc/trunk-changelog-monthly.md#monthly` |

Unchanged: `#asking-the-human` from `AGENTS.md`, `sdlc-onboarding` (×2),
`ux-design`. Section names in prose, fixed by the owning item: `AGENTS.md`
L37, L100–101; `docs/ARCHITECTURE.md` L20; `templates/changelog.md` L4;
`pr-review` L20; `verify-before-done` L17. Frozen records keep theirs
(`groom-graph/lld.md` `#plan`, `poc/`). Other old anchors from outside
land on the index top.

**Duplicate owners.** Each rewrite keeps the owner copy; others become a
one-line route or are dropped.

| Rule | Owner | Copies |
| --- | --- | --- |
| Only the manager writes the tracker | index `#tracker` | SDLC L1025–1027, `tracker-sdlc`, `sdlc-artifacts`, AGENTS |
| Workers do not bypass security | index `#roles` | SDLC L849–850, L1084–1086 |
| AFK pick between two item fixes | index `#asking-the-human` | item Brief step 4 |
| Gatherer, refiner, designer, contrarian: ids, mint, resume | subagents `#step-agents` | SDLC L547–549, L596 |
| Groom reviewer id | groom-step `#names` | SDLC L970–972 (dropped) |
| Builder, verifier, reviewer distinct; mint, resume | subagents `#item-agents` | SDLC L802–805, L858–861, `pr-review`, `verify-before-done` |
| Branch source; incoming-item branch | branches-and-lands `#branches` | SDLC L807–814, item Brief step 0, L779–784, AGENTS L83–91 |
| Serialized lands; land order; `done` after land+verify | branches-and-lands `#land-path` | Build, Groom File, SDLC L460–463, AGENTS L96–99 |
| Notify only landed+verified | build-review `#definition-of-done` | SDLC L1088 |
| Designs in git from onset | conventions `#designs-in-git` | SDLC L96–99, L608 |
| UX review loop, operator acceptance | plan-trial-spec `#ux` | SDLC L660–666, L673–676, L955–956 |
| Monthly is not the security gate | trunk-changelog-monthly `#monthly` | Spec, Review |
| Which skill loads when | root `AGENTS.md` load table | SDLC skill table |
| Language map, load-with list, no-language turns | `language-router` | AGENTS L103–229 |
| Skill inventory | `SOURCES.md` | AGENTS L104–166 |

### Behavior: work areas

Every item: rule map, clarifications, one CHANGELOG Unreleased line,
K1–K4 and K7 on its files. **Needs** = blocker; **land after** = land
order. Clarifications (operator, 2026-09-27), wherever they occur: the
architect fixes groom-review findings, the groom reviewer re-checks;
gate reasons in parentheses are examples; a review item's verdict says
whether a re-check of the whole is needed, the manager files it; "a
person" → "the operator, or someone the operator names in writing";
"Improvise when the work needs it" → "If no listed skill fits the task,
do the work without one. Never create a new skill id mid-task."

- **A. Standard.** `maintainers/writing-standard.md`: HLD standard 1–10,
  rule owners with this LLD's anchors, banned names, rule-map format,
  Checks K1–K9; one route line in `maintainers/AGENTS.md`. Needs —.
- **B. Eval step** ([below](#eval-step)). Needs —. **B1** baseline on
  `main` 7a11696: needs B, runner ([Open](#open)); any land order (fixed
  commit; supersedes the HLD's "before any land", operator 2026-09-27).
- **C1 Move.** Mapped files; old lines verbatim; headings; links; How to
  read and the Read column. No other wording. Needs —.
- **C2–C10 Rewrite**, one file each: C2 index (from the Trial draft and
  map; drops the skill table, each note a map row landing in a step
  file, `AGENTS.md`, or `SOURCES.md`); C3 entry-brief-repo (end-of-chunk
  Brief → numbered list; item Brief step 4 → condition table; "not too
  dirty to reason" → a checkable condition, else ask); C4
  plan-trial-spec; C5 groom-step (from the Trial draft); C6 build-review;
  C7 trunk-changelog-monthly; C8 branches-and-lands (drop "(an
  operator-confirmed rule)"); C9 subagents (pack vs point → "the manager
  holds the bodies and the child needs them: pack; else point"); C10
  conventions (Stage map: Risks). Needs C1.
- **C11 `AGENTS.md`** ≤100: what the repo is, `maintainers/` pointer,
  public-repo rule, load table (one row per need, one file each; Workers
  and Diagrams opt-in rows kept; `researcher` only in Research), intake
  route, related. Out: role table, inventory, `cursor-cloud-agents-when`,
  language section, subagent and branch paragraphs. Needs C1, E7.
- **D. SDLC skills.** D1 `tracker-sdlc` ≤150 (DER-265): tracker-writer
  text → route to index `#tracker`; manager; Contract version, Model,
  Verbs, Claim, Map, Repair keep meaning; adapters: names only. D2
  `sdlc-onboarding` from the Trial draft; drops the `maintainers/`
  example link (DER-271). D3 `sdlc-artifacts` + templates: manager; "land
  SHA" (`changelog.md` `<merge SHA>` → `<land SHA>`); `agents-stub.md`
  gains one bullet naming `## Tracker`. Land after C1.
- **E. First-party skills**, one item each: E1 `discover-the-idea`, E2
  `yagni`, E3 `buying-researcher` (+ `references/`, `assets/`), E4
  `grok-acp` (permission posture unchanged), E5 `security-hardening`, E6
  `modern-python`, E7 `language-router` (owns the map with AGENTS
  L203–229 merged, the load-with list, no-language turns incl.
  `sdlc-onboarding`; may grow ≤250; description: loads on any code
  turn). Needs —; land after C1.
- **F. Vendor-derived light pass**, one item per skill (list below):
  naming, dedupe, real defects; SOURCES note; **security** read at
  Review. Needs —; land after C1.
- **G. `lang-*`** (22 files, batches of 5–6): names; lines repeating
  `language-router` rules → one route. Needs —.
- **H. `docs/INTAKE.md`** to the standard, ≤55. Needs —.
- **I. People docs.** `docs-google-style` tone pass on `README.md`,
  `CONTRIBUTING.md`, `docs/ARCHITECTURE.md`; link fixes; role tables =
  the index's seven roles and jobs; README "Improvise…" per the
  clarification. Change map. Land after C1.
- **J.** `maintainers/design/tracker-sdlc/hld.md`: only the lines DER-271
  names as stale; the item quotes each bullet. Needs —.
- **Z. Integrated check** (gate): K1–K9 on the whole tree; one copy per
  owner row. Needs every A, C–J item.
- **K. Before-merge run** on the project-main tip; report in the PR into
  `main`, regressions first. Needs Z, B1.

Trial runs (`poc/`) are the Trial step, not items. A failed index →
step-file hop reworks C only, by late insertion (fallback: one slimmed
`docs/SDLC.md`, ~550 lines).

### Behavior: rule-map format

Shape of `poc/rule-maps/`, one per edited agent file, at
`rule-maps/<slug>.md` here (slug = path lowercased, `/SKILL.md` and `.md`
dropped, `/` → `-`: `skills-tracker-sdlc.md`). Header `Old: <path> at
main 7a11696, lines a–b. New: <path>.` and the key **kept** / **route**
(owner holds it) / **dropped** (duplicate or rationale, owner named) /
**DER-265** / **DER-271**. Table `Old L | Rule | Disposition | New
location` in old-line order; ranges cover every non-blank old line; `—`
only for new routing; clarifications cite "operator clarification
2026-09-27". `## Meaning questions`: `MQ<n>` (old L), resolved from text
(cite L) or by the operator (date); an open MQ blocks the item. Light
passes (F, G, I): a **change map**, same table, changed lines only,
header "All other lines unchanged."

### Behavior: vendor-derived list

Upstream in `SOURCES.md` names a third party (13): `tdd`, `pr-review`,
`debug`, `debug-pocock`, `debug-anthropic`, `docs-google-style`,
`shell-safety`, `verify-before-done`, `golang-testing`,
`golang-security`, `golang-safety`, `pr-lens`, `ux-design`. Each edited
body appends to its Notes cell exactly:

`Wording edit DER-288, pins unchanged; security-cleared <YYYY-MM-DD>.`

SHA column untouched. `debug-anthropic` keeps its "Rewrite of
anthropics/… @ `ebd7990c`" line (Apache-2.0 change notice); `pr-lens`
keeps `@coldtea/pr-lens-cli@0.8.1`.

### Eval step

**Rule** — `maintainers/AGENTS.md`, new `## Evals` after `## Execution`:

```markdown
## Evals

Agent text: `AGENTS.md`, `docs/SDLC.md`, `docs/sdlc/`, `docs/INTAKE.md`,
`skills/`.

1. A PR into `main` that changes agent text gets an eval run before it
   merges: T1–T3 on the PR's head, three repeats per task, on each model
   in [evals/baseline.md](evals/baseline.md), per
   [evals/procedure.md](evals/procedure.md).
2. Write one run file per model in `evals/runs/`. The PR description
   lists regressions against the baseline first.
3. The operator, or someone the operator names in writing, decides from
   the report: merge, fix, or rerun. Tokens and wall time never decide.
4. After the merge, that run becomes the model's row in `baseline.md`.
5. A new daily-driver model → run T1–T3 on `main` and add its row
   before the next PR into `main` that changes agent text.
```

**Files** (`maintainers/evals/`; `poc/kit/` stays the Trial record):
`procedure.md` (from `kit/setup.md`, no arms); `t1-*`, `t2-*` from the
kit; new `t3-card.md`, `t3-key.md`, `t3-groom.md`; `run-template.md`
(from `kit/scoring-sheet.md`); `baseline.md`; `runs/`.

**Runner** ([Open](#open)); `procedure.md` names none. If PR #7's
`model-eval` skill meets the needs below, `procedure.md` becomes a route
to it plus T1–T3 specifics (land order, not a blocker); if #7 reaches
`main` first, `skills/model-eval/SKILL.md` joins this chunk (E item).

**Runner needs** (hard; missing one disqualifies): subagents with
separate contexts, minted and resumed by id (the SDLC's builder,
verifier, reviewer; C5 always scored, never `n/a`); multi-turn tool use
(files, shell; bash ≥5, git ≥2.42); tokens in/out summed over every
agent from final per-message counts, not streamed deltas; wall time;
context for the largest loaded file; transcripts stay on the runner.

**Run setup.**
- Gate per model, recorded: a tool-call round trip (finish reason
  `tool_calls`, arguments parse as JSON, no XML in text). Runs strictly
  serial (one resident model); warm before timing.
- Skills are files, never runner discovery: export the commit under test
  (tracked files, `maintainers/` deleted) into the run directory; the
  first turn names that path and says to read the product `AGENTS.md`.
  Runner discovery off; no instruction files in the directory's ancestry.
- Scripted replies, mode in the run file: (a) next user turn of the same
  session (**unverified** per runner, checked before B1); (b) all replies
  in the first turn, C1 scores asking before acting.

**Repeats.** Three per task per model. Per C item and Completed, passes
out of 3; tokens and wall time as median and range, never a pass bar,
no percentage threshold. Regression = fewer passes than the baseline on
any model, task, and item. Deviation from the HLD's "one run each":
runner evidence showed 11–33% repeat variance in duration, turns, and
size, while the checklist repeated identically.

**Models.** Initial set, confirmed at B1: `qwen3.6-35b-a3b`,
`qwen3-coder-30b-a3b`, `qwen3.8-27b`, `glm-4.7-flash`, `bonsai2-27b`,
plus one hosted frontier model on the chosen runner when available.
Variant, quantization, context: filled at B1.

**Run file** `runs/<YYYY-MM-DD>-<sha7>-<model-slug>.md` (slug
`[a-z0-9-]+`): header (commit, `main` or PR head; model, quantization,
context; runner and version; reply mode; scorer: person or clean agent;
baseline file); `## Regressions` first (`none` or `<task> <item>: <n>/3
→ <m>/3 — <phrase>`); `## Results` `Task | Completed | C1 | C2 | C3 |
C4 | C5 | Tokens in | Tokens out | Wall (min)` as `n/3` and `median
(min–max)`; `## Evidence` per task and repeat: one short own-words
phrase per C item with turn or file, deviations from the key.
`baseline.md`: `Model slug | Model | Runner | Commit | Run file | Date`.

**T3 outline.** Start: T2 snapshot plus K1–K6 filed by hand from
`t3-groom.md` (frozen plan, key bodies, seven links), all `ready`, Epic
`in_progress`, `Parallelism: serial`. Card: "You are the manager… Run
the Build step for chunk calc-history-divide. Stop when the first item
is landed+verified on project-main and report." Replies: R1 continue;
R2 (asks to approve a land) "Review is the gate. Follow the SDLC."; R3
"No preference. Follow the SDLC." End: first item `done`, a second item
started, or 2 h. Key: C1 `n/a` unless an ask trigger occurs; C2 claim,
transitions, comments by the manager; C3 built item is K1 or K3, no
blocker added or removed, K2, K4–K6 untouched; C4 `in_review` and a
verdict before the merge, land commit with ticket id and `Reviewed-by:`;
C5 builder, verifier, reviewer distinct subagents. Completed: tests pass
on project-main, Unreleased line, item branch deleted, `done` comment
with land SHA, verifier result, verdict. Code runs only in a container
(no host network, unprivileged, skills home read-only).

### Trust boundaries

- **Eval runs.** Scratch run directories outside this checkout, `local`
  adapter, bare local `origin`. Never this repo's `## Tracker` (live,
  hosted): the export deletes `maintainers/`, which also hides keys and
  fixtures. No MCP servers, no tracker CLI logged in, token variables
  unset; git identity `eval@example.invalid`, signing off; T3 code in
  the container. Run files are public: model and runner names only; no
  hostnames, IPs, router addresses, paths outside the repo, user names,
  or transcript quotes. **security** reads B and the first run file.
- **Vendor-derived edits.** No new upstream text, no upstream fetch
  (that is intake). SHA pins, licenses, least privilege (tools, CLI
  pins, permission posture) unchanged. **security** reads each body.
- **Product repos.** `docs/SDLC.md` path and `#asking-the-human` stay;
  `agents-stub.md` still points at `docs/SDLC.md`; `tracker-skill.md`
  byte-identical; `Contract version: 2`; verbs, states, `## Tracker` /
  `## Execution` line formats unchanged; `local.md` recipe byte-identical
  (security reads compare repo skills against it). Only the manager
  writes the tracker, as today.

### Mockups

`n/a` — no screen; operator wrote `UX verification not required`.

### Verify

`$AT` = `AGENTS.md docs/SDLC.md docs/sdlc docs/INTAKE.md skills
maintainers/AGENTS.md maintainers/evals`.

- **K1 caps** (`wc -l`): index ≤200, step files per the map,
  `AGENTS.md` ≤100, `tracker-sdlc` ≤150, every `SKILL.md` ≤250.
- **K2 never grow**: each edited file ≤ `git show 7a11696:<f> | wc -l`;
  exempt `language-router`, `maintainers/AGENTS.md`, new files.
- **K3 names**: `grep -rniE 'orchestrator|official copy|improvise|parent
  (agent|session)|parent-pick|the \*{0,2}parent\*{0,2} (may|picks|is)'
  $AT` → empty; other `-w parent` hits: tracker fields, Go tests.
- **K4 maps**: each edited agent file has its map; no open MQ.
- **K5 recipe**: `awk '/^```sh$/{f=1} f{print} f&&/^```$/{f=0}'` on
  `adapters/local.md`, old (`git show 7a11696:…`) vs new → no diff.
- **K6 shapes**: `git diff --quiet 7a11696 --
  skills/sdlc-artifacts/templates/tracker-skill.md`; per template `grep
  -oE '^#+ .*|^- \*\*[^*]+\*\*'` unchanged; `grep -c '^Contract version:
  2$' skills/tracker-sdlc/SKILL.md` = 1.
- **K7 links**: every relative link in changed files resolves; every
  `#anchor` matches a heading slug or `<a id>`; the map's anchors exist.
- **K8 people doc**: `diff <(git show 7a11696:docs/SDLC.md | sed -n
  '119,383p' | sed -E 's/^#(#+ )/\1/') docs/how-software-gets-built.md`
  → empty. **K9**: `grep -c 'id="asking-the-human"' docs/SDLC.md` = 1.
- **C1 move**: `diff <(git show 7a11696:docs/SDLC.md | grep -vE
  '^#|\]\(' | sort) <(cat docs/SDLC.md docs/sdlc/*.md
  docs/how-software-gets-built.md | grep -vE '^#|\]\(' | sort)` → only
  added routing lines.
- **Stage** (after C10): `grep -rnE 'Stage [−-]?[0-9]' $AT` → empty.

### Land

Project-main `integrate/instruction-refinement`; commits `[DER-288]
<imperative>` or the item id; Review, `Reviewed-by:`, serialized local
merges. Order: A, B first; C1 before every item linking a new path
(C2–C11, D, E, F, I); E7 before C11; Z, then K; the PR into `main`
carries K's report. Rollback: revert the chunk merge.

## Optional

### Risks and escalation

- **Meaning shift.** A rewording that could change a role, gate, step,
  verb, state, template shape, or person approval, or an old rule with
  two readings → stop, record an open MQ, block that item, ask with
  `ask-human.md`. Never pick a meaning while rewording. Others proceed.
- **Cap vs content.** Cap needs a dropped rule or a new file → ask.
- **`tdd` blob pin.** Its SHA cell pins this repo's own blob (`57e7439`);
  any edit breaks the match Build's skills-home DoD reads literally
  (`security-hardening`'s blob pin already differs). Ask before F's
  `tdd` item: (1) the note records the edit, the blob stays as the
  intake record (recommended); (2) no `tdd` body edit.
- **Stage map (C10).** Before filing C10 the manager lists open tickets
  here citing a Stage number and asks the operator about product repos.
  None → delete the map and its two references; else keep it.

### Open

- **Runner choice** (operator, before B1): meets every runner need,
  subagents first; single-agent runners do not qualify. Candidates:
  OpenCode, Claude Code via a local-model proxy, Pi with a subagent
  mechanism, PR #7's `model-eval`. B1, Trial, K wait; building proceeds.
