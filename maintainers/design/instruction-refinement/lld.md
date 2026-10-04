# LLD — Instruction refinement: agent text that works across model strengths

- Slug: `instruction-refinement`
- HLD: [hld.md](hld.md) · Trial kit: [poc/](poc/poc.md)
- Tickets this LLD covers: DER-288 (chunk; also DER-265 and DER-271's
  wording bullets); items filled at Groom
- Date: `2026-09-26`

Old text = `main` 7a11696 (`docs/SDLC.md` 1128 lines); "Old L" cites it.

## Required

### Paths / modules: file and anchor map

No basename equals a template. C1 creates every heading (old anchor in
parentheses); later items keep them. Caps apply from the rewrites on.

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
| `docs/sdlc/conventions.md` | 385–463; 488–509; 960–961; 1090–1095 | `#name-formats` (`#conventions-optional-recommended`, old `#names`), `#commits`, `#product-repo-layout`, `#changelog-and-connection`, `#designs-in-git` (`#git-designs-from-onset`), `#in-flight-map` (`#in-flight-map-old-numbers`) | ≤100 |
| `docs/how-software-gets-built.md` | 119–383 | one H1, headings raised one level (`#how-software-gets-built`) | — |
| `maintainers/writing-standard.md` | — (A) | `#standard`, `#names`, `#rule-owners`, `#protected-rules`, `#rule-maps`, `#checks` | ≤150 |
| `maintainers/evals/…` | — (B) | [Eval step](#eval-step) | — |

Index **How to read** (Trial draft): find your step, read that row's
file; **manager** → also the branches and subagents files. Steps gains a
"Read" column. The Stage table stays (open tickets still cite it).

**Links.** C1 turns the 21 internal links of old SDLC into `path#anchor`
and fixes the 4 inbound anchors that break: `AGENTS.md` `#entry`,
`#brief` → `docs/sdlc/entry-brief-repo.md#entry`, `#brief`; `README.md`
`#how-software-gets-built` → `docs/how-software-gets-built.md`;
`pr-lens` `#monthly` → `sdlc/trunk-changelog-monthly.md#monthly`.
`#asking-the-human` links (`AGENTS.md`, `sdlc-onboarding` ×2,
`ux-design`) hold. Prose section names, fixed by the owning item:
`AGENTS.md` L37, L100–101; `docs/ARCHITECTURE.md` L20;
`templates/changelog.md` L4; `pr-review` L20; `verify-before-done` L17.

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

Every item: rule map, clarifications, one Unreleased line, K1–K4 and K7.
**Needs** = blocker; **land after** = land order. Clarifications
(operator, 2026-09-27), everywhere: architect fixes groom-review
findings, groom reviewer re-checks; gate reasons in parentheses are
examples; a review item's verdict says whether a whole re-check is
needed, the manager files it; "a person" → "the operator, or someone the
operator names in writing"; "Improvise when the work needs it" → "If no
listed skill fits the task, do the work without one. Never create a new
skill id mid-task."

- **A. Standard.** `maintainers/writing-standard.md`: HLD standard 1–10,
  rule owners and protected rules with this LLD's anchors, banned names,
  rule-map format, Checks K1–K10; one route line in
  `maintainers/AGENTS.md`. Needs —.
- **B. Eval step** ([below](#eval-step)). Needs —. **B1** baseline on
  `main` 7a11696: needs B, runner ([Open](#open)) and its security read;
  any land order (fixed commit; supersedes the HLD's "before any land").
- **C1 Move.** Mapped files; old lines verbatim; headings; links; How to
  read and the Read column. No other wording. Needs —.
- **C2–C10 Rewrite**, one file each, in map order: C2 index (Trial
  draft; skill-table notes → map rows landing in a step file,
  `AGENTS.md`, or `SOURCES.md`); C3 (end-of-chunk Brief → numbered list;
  item Brief step 4 → condition table; "not too dirty to reason" →
  checkable condition, else ask); C4; C5 (Trial draft); C6 (DoD links
  `#review`, `#land-path`); C7; C8 (drop "(an operator-confirmed
  rule)"); C9 (pack vs point → "the manager holds the bodies and the
  child needs them: pack; else point"); C10. Needs C1.
- **C11 `AGENTS.md`** ≤100: what the repo is, `maintainers/` pointer,
  public-repo rule, load table (one row per need, one file each; Workers
  and Diagrams opt-in rows kept; `researcher` only in Research), intake
  route, related. Out: role table, inventory, `cursor-cloud-agents-when`,
  language section, subagent and branch paragraphs. Needs C1, E7.
- **D.** D1 `tracker-sdlc` ≤150 (DER-265): writer rule → route to index
  `#tracker`; Contract version, Model, Verbs, Claim, Map, Repair keep
  meaning; adapters: names only. D2 `sdlc-onboarding` from the Trial
  draft, no `maintainers/` link (DER-271). D3 `sdlc-artifacts` +
  templates: `<merge SHA>` → `<land SHA>`; `agents-stub.md` + one bullet
  naming `## Tracker`. Land after C1.
- **E.** One item each: E1 `discover-the-idea`, E2 `yagni`, E3
  `buying-researcher` (+ `references/`, `assets/`), E4 `grok-acp`, E5
  `security-hardening`, E6 `modern-python`, E7 `language-router` (owns
  the map with AGENTS L203–229 merged, load-with list, no-language turns
  incl. `sdlc-onboarding`; ≤250; loads on any code turn). Land after C1.
- **F. Vendor-derived light pass**, one item per skill (list below):
  naming, dedupe, real defects; SOURCES note. Needs —; land after C1.
- **G. `lang-*`** (22 files, batches of 5–6): names; lines repeating
  `language-router` rules → one route. Needs —.
- **H. `docs/INTAKE.md`** to the standard, ≤55. Needs —.
- **I. People docs.** `docs-google-style` tone pass on `README.md`,
  `CONTRIBUTING.md`, `docs/ARCHITECTURE.md`; link fixes; role tables =
  the index's seven roles and jobs; README "Improvise…" per the
  clarification. Change map. Land after C1.
- **J.** `maintainers/design/tracker-sdlc/hld.md`: only the lines DER-271
  names as stale; the item quotes each bullet. Needs —.
- **Z. Integrated check** (gate): K1–K10 on the tree; one copy per owner
  row; each gate the index names resolves to a step file. Needs A, C–J.
- **K. Before-merge run** on the project-main tip; report in the PR into
  `main`, regressions first. Needs Z, B1.

Trial runs (`poc/`) are not items. A failed hop reworks C only by late
insertion (fallback: one slimmed `docs/SDLC.md`, ~550 lines).

### Behavior: protected rules

Each maps `kept`, or `route` to an owner that keeps it. Any other change
is a meaning shift (Risks). **security** reads every item touching one
at Review; the item names the rows it touches.

| Rule | Item | Mechanical check (old 7a11696 vs new) |
| --- | --- | --- |
| `security-hardening` Never, Ask first | E5 | `sed -n '/^## Never/,/^## [^N]/p' f \| grep -c '^\| '` equal; same for `## Ask first` |
| INTAKE checklist | H | six numbered steps under `## Checklist` |
| `tracker-sdlc` claim protocol, Never, Ask first; adapters | D1 | Claim steps 1–5 kept; Never and Ask-first bullet counts equal |
| `adapters/local.md` recipe | D1 | K5 |
| `grok-acp` permission posture, labels, own-item limits | E4 | every map row `kept` |
| Public-repo rule | C11 | every map row `kept` |
| index `#roles`, `#tracker` | C2 | every map row `kept` or `route` to its owner |
| branches-and-lands `#never` | C8 | each old L945–961 bullet `kept` here or at its owner |
| subagents `#tracker-writes` | C9 | every map row `kept` |

### Behavior: rule-map format

As `poc/rule-maps/`: one per edited agent file at `rule-maps/<slug>.md`
(path lowercased, `/SKILL.md` and `.md` dropped, `/` → `-`). Header
`Old: <path> at main 7a11696, lines a–b. New: <path>.`; key **kept** /
**route** / **dropped** (owner named) / **DER-265** / **DER-271**; table
`Old L | Rule | Disposition | New location`, old-line order, ranges
cover every non-blank old line; `## Meaning questions` (`MQ<n>`,
resolved from text or by the operator with date; open → item blocked).
Light passes (F, G, I): a change map, changed lines only.

### Behavior: vendor-derived list

Upstream in `SOURCES.md` names a third party (13): `tdd`, `pr-review`,
`debug`, `debug-pocock`, `debug-anthropic`, `docs-google-style`,
`shell-safety`, `verify-before-done`, `golang-testing`,
`golang-security`, `golang-safety`, `pr-lens`, `ux-design`. Each edited
body appends to its Notes cell exactly (one exception below):

`Wording edit DER-288, pins unchanged; security-cleared <YYYY-MM-DD>.`

Exception, `tdd`: its SHA cell pins this repo's own blob; the pin stays
(brief constraint) and the note reads `Wording edit DER-288, pins
unchanged; new body blob <sha>; security-cleared <YYYY-MM-DD>.` SHA
column untouched everywhere. `debug-anthropic` keeps its "Rewrite of
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
`model-eval` meets the needs, `procedure.md` routes to it plus T1–T3
specifics (land order); if #7 reaches `main` first, its `SKILL.md` joins
this chunk (E item). Needs (one missing disqualifies): subagents with
separate contexts, minted and resumed by id (C5 always scored); tool use
(files, shell; bash ≥5, git ≥2.42); tokens in/out summed over every
agent; wall time; per-run timeout; context for the largest file;
transcripts stay on the runner. Before B1, **security** reads the chosen
runner: tool permissions, sandbox, egress, telemetry, where transcripts
are stored, any proxy bound to loopback; decision recorded on DER-288; a
runner change means a new read. A local-model proxy or network bind is
Ask first (`security-hardening`).

**Run setup.**
- Isolation: the whole runner runs as a separate unprivileged user or in
  a container (T3: container), with an empty home (no `gh` or git
  credential helpers, SSH keys, runner MCP config), no SSH agent, and
  egress only to the model endpoint.
- Pre-run probe, recorded pass/fail in the run file: `gh auth status`
  fails, `git credential fill` returns nothing, `ssh-add -l` fails, the
  hosted tracker's host and one LAN host are unreachable. A pass that
  fails → no run.
- Gate per model, recorded: tool-call round trip (finish reason
  `tool_calls`, JSON arguments, no XML in text). Strictly serial; warm
  the model before timing.
- Skills are files: export the commit under test (tracked, `maintainers/`
  deleted) into the run directory, read-only for the agent; the first
  turn names that path and says to read the product `AGENTS.md`. Runner discovery off; no
  instruction files in the directory's ancestry.
- Scripted replies, mode in the run file: (a) next user turn of the same
  session (**unverified** per runner, checked before B1); (b) all replies
  in the first turn, C1 scores asking before acting.

**Repeats.** Three per task per model (deviation from the HLD's "one
run each": 11–33% repeat variance in duration, turns, size; the
checklist repeated identically). C items and Completed as passes out of
3; tokens and wall time as median and range, never a pass bar.
Regression = fewer passes than the baseline on any model, task, item.

**Models** (confirmed at B1; variant, quantization, context filled
then): `qwen3.6-35b-a3b`, `qwen3-coder-30b-a3b`, `qwen3.8-27b`,
`glm-4.7-flash`, `bonsai2-27b`, one hosted frontier model if available.

**Run file** `runs/<YYYY-MM-DD>-<sha7>-<model-slug>.md`: header
(commit; model, quantization, context; runner, version; probe and gate
results; reply mode; scorer `person` or `agent`, never a name; baseline
file); `## Regressions` first (`<task> <item>: <n>/3 → <m>/3 — <phrase>`
or `none`); `## Results` `Task | Completed | C1–C5 | Tokens in/out |
Wall` as `n/3` and `median (min–max)`; `## Evidence`: per task and
repeat, one own-words phrase per C item (never quoted model output) with
turn or file. `baseline.md`: `Model slug | Model | Runner | Commit | Run
file | Date`.

**T3 outline.** Start: T2 snapshot + K1–K6 filed by hand from
`t3-groom.md` (frozen plan, seven links), all `ready`, Epic
`in_progress`, `Parallelism: serial`. Card: "You are the manager… Run
Build for chunk calc-history-divide. Stop when the first item is
landed+verified on project-main and report." Replies: R1 continue;
R2 (asks to approve a land) "Review is the gate. Follow the SDLC."; R3
"No preference. Follow the SDLC." End: first item `done`, a second
started, or 2 h. Key: C1 `n/a` unless an ask trigger occurs; C2 claim,
transitions, comments by the manager; C3 item is K1 or K3, blockers
untouched; C4 `in_review` and a verdict before the merge, land commit
with ticket id and `Reviewed-by:`; C5 distinct builder, verifier,
reviewer. Completed: tests pass, Unreleased line, item branch deleted,
`done` comment with land SHA, verifier result, verdict.

### Trust boundaries

- **Eval runs.** Isolated runner (Run setup), scratch directories outside
  this checkout, `local` adapter, bare local `origin`, never this repo's
  live `## Tracker` (the export drops `maintainers/`, keys, fixtures).
  Token variables unset; git identity `eval@example.invalid`, unsigned.
  **security** reads the runner (before B1), B, and the first run file.
- **Public text** (`maintainers/evals/`, PR and tracker text): no
  hostnames, IPs, model-server URLs or ports, outside paths, API keys or
  tokens, personal names, or quoted model output (K10).
- **Vendor-derived edits.** No new upstream text, no upstream fetch
  (that is intake). SHA pins, licenses, least privilege (tools, CLI
  pins, permission posture) unchanged. **security** reads each body.
- **Product repos.** `docs/SDLC.md` path, `#asking-the-human`, the stub's
  pointer, `tracker-skill.md`, `Contract version: 2`, verbs, states,
  `## Tracker` / `## Execution` formats, and the `local.md` recipe
  (security compares repo skills against it) unchanged.

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
- **K4 maps**: every edited file mapped; no open MQ; protected checks.
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
- **K10 public text** (before each push and the PR): `git diff main...
  | grep -nE '^\+.*(([0-9]{1,3}\.){3}[0-9]{1,3}|/home/|:[0-9]{4,5}\b|\bsk-[A-Za-z0-9_-]{20,}|\.(lan|local|internal|ts\.net)\b|https?://)'`
  → each hit is an allowed reference (upstream or comparables URL) or is
  removed; same check on PR and tracker text before posting.
- **C1 move**: old SDLC vs `cat` of the new files, each `grep -vE
  '^#|\]\(' | sort`, diffed → only added routing lines.

### Land

Project-main `integrate/instruction-refinement`; commits `[DER-288]
<imperative>` or the item id; Review, `Reviewed-by:`, serialized local
merges. Order: A, B first; C1 before every item linking a new path
(C2–C11, D, E, F, I); E7 before C11; Z, then K; the PR into `main`
carries K's report. Rollback: revert the chunk merge.

## Optional

### Risks and escalation

- **Meaning shift.** A rewording that could change a role, gate, step,
  verb, state, template shape, person approval, or protected rule, or an
  old rule with two readings → stop, open MQ, block that item, ask
  (`ask-human.md`). Never pick a meaning while rewording.
- **Cap vs content.** Cap needs a dropped rule or a new file → ask.

### Open

- **Runner** (operator, 2026-09-27): OpenCode. No AI-lab harness
  (Claude Code out); single-agent runners and Hermes Agent (no resume of
  a finished subagent) do not qualify. Smoke test + **security** read
  before B1; a failed smoke test goes back to the operator. B1, Trial,
  K wait; building proceeds.
