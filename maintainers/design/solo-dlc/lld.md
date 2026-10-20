# LLD — solo-dlc: the SDLC on a harness without sub-agents

- Slug: `solo-dlc`
- HLD: [maintainers/design/solo-dlc/hld.md](hld.md) (agent review passed
  in round 4; accepted by the operator at 021f81d, 2026-10-19). UX: [ux.md](ux.md); stories:
  [user-stories.md](user-stories.md); comparables:
  [comparables.md](comparables.md). Brief: DER-421 brief v3, confirmed
  2026-10-18.
- Tickets this LLD covers: DER-421 (chunk); brief items 1–8 (item 1 is
  DER-529; the others get ids at Groom)
- Date: `2026-10-18`; fix round 1 after the security and adversarial
  reviews of 34e1278; cleanup round 2 after the security and LLD
  re-reviews of de7c438 passed, applying their recommendations, same day;
  fix round 4 adds the [driver-file ledger](#driver-file-ledger);
  the OpenCode-first revision makes OpenCode the first harness
  (clarification 16); the run-state revision, 2026-10-19, applies the
  operator's decisions A–D (clarifications 19–25), and its fix round
  applies the independent review of f0f389e; the toolbox-copy revision,
  2026-10-19, applies the operator's decisions on a pinned toolbox copy
  in the run root (clarification 26), with the reviews of ed91909,
  ed16411, and 0047da2
- Status: **Spec accepted by the operator at 021f81d, 2026-10-19**, with
  O12, O13, O17 (residual accepted in writing), O18, and O20 as
  recommended. The security re-review of de7c438 passed. The
  toolbox-copy revision follows that acceptance: it changes TB2, TB3,
  and TB15, adds residual item 7 and operator item 5 (O22, accepted),
  and opens O21. **Security** re-reads
  those rows and the operator accepts the revision before Groom
  ([Security gate](../../../docs/sdlc/plan-trial-spec.md#security-gate)).
- Spec entry gate: the offline `tracker-sdlc` setup check passed on
  2026-10-18 (`maintainers/AGENTS.md` `## Tracker` names
  `.agents/tracker/SKILL.md`; that file says `Contract: tracker-sdlc v2`).
- Trial: not run; the operator accepted O1, no separate Trial
  (2026-10-18). OpenCode facts read in 1.19.3 source, and the OpenCode
  Trial checks O-T1–O-T10 with their fallbacks, are in
  [opencode-server.md](opencode-server.md). Every Pi fact the HLD marks
  for the Trial (T1–T6) has a chosen design and a fallback in
  [Trial-dependent decisions](#trial-dependent-decisions). Facts read
  from Pi's published 0.73.1 source are cited in
  [Pi facts](#pi-facts-checked-in-0731-source).

Words used here as in the HLD: **run root** (`RUN_ROOT`), **run folder**
(`<persona>/run-N/`), **persona folder**, **node**, **exit**, **stop**,
**driver**, **worker**. New words:

- **Suffix**: the lowercased, label-safe form of an item's ticket id
  ([Labels](#labels)). Item personas, worktrees, and driver folders use
  it: `builder-<suffix>`.
- **Candidate**: `candidate.json`, the result a worker proposes. The
  driver validates it and writes `result.json`.
- **Driver-authored result**: a `result.json` the driver writes without
  a valid candidate: command stages (as the command wrapper), gate
  nodes, failed checks on model stages, and invalid results.
- **Driver-fixed exits**: exits that the flow spec, not a flow file,
  defines for stages the driver adds inside or around nodes: land
  sub-stages, paperwork, and manager stages
  ([Driver-fixed exits](#driver-fixed-exits)).
- **Toolbox**: this skills home. A run reads it only from the toolbox
  copy; nothing from it is copied into a product repo.
- **Toolbox copy**: `RUN_ROOT/toolbox.git`, a bare copy of `run.json`
  `bundle.remote`'s trunk and tags, as the operator typed it at Run prep ([Toolbox copy](#toolbox-copy)).
- **Pinned commit**: the toolbox commit recorded in `run.json`
  `bundle.commit`, with the optional tag `bundle.tag`. The driver reads
  `flow.json`, personas, scripts, and packed skill bodies only from the
  toolbox copy's object store at that commit, each object checked by
  hash.
- **Run prep**: stage 0, a short interactive session that asks the
  setup questions, runs the readiness checks, and prepares the run
  root. Its session is discarded ([Behavior 8](#behavior-8-run-prep-and-later-items-0-4-8)).
- **Durability level**: `pushed`, `local`, or `plain`; how the run
  state survives ([Durable run state](#durable-run-state)).
- **State branch**: `sdlc/run/<chunk-slug>`, the driver-owned orphan
  branch in the product repo that holds the durable run state.
- **Compiled file**: `RUN_ROOT/compiled/<persona>.md`, one per persona: role, packed skills, and repo facts
  ([Compiled files](#compiled-files)).
- **Rehydrate**: start a fresh session for a persona whose session
  file is missing, from its compiled file, `state.md`, and driver facts.
- **Env-prep**: the chunk-scope nodes that build and prove the build
  and test environment after Spec is accepted
  ([Build-environment gate](#build-environment-gate)).

## Required

### Paths / modules

| Path | Item | What |
| --- | --- | --- |
| `skills/sdlc-kickoff/SKILL.md` | 0 | New skill, first in the build order: Run prep, Gather wrap-up, and restore modes ([Behavior 8](#behavior-8-run-prep-and-later-items-0-4-8)). ≤250 lines |
| `docs/sdlc/run-state.md` | 0 | New owner of the formats that Run prep, the plugin, and workers read: the run-root layout with its **D** marks, `run.json`, `machine.json`, `asks/`, the run folder, labels, the durability levels, the state branch and `sdlc-state.json`, persist, lease, restore and drill, the toolbox copy (remote rule, pin, repin), compiled files, rehydrate, session backup. Rules only, one or two lines each; examples stay in this LLD and `docs/sdlc/fixtures/run-root/`. ≤250 lines: a new `docs/sdlc/` file over standard 9's 150, an operator ask ([O13](#questions-for-the-operator)) |
| `docs/sdlc/stage-result.md` | 1 | Edited in place: v1 fields, rules, examples; stays ≤150 lines per the [line budget](#line-budget-for-stage-resultmd) |
| `docs/sdlc/fixtures/results/` | 1 | Valid and invalid result fixtures, each with an `.expect.json` |
| `docs/sdlc/bundle-spec.md` | 2 | Owner: bundle layout, `bundle.md`, persona files, prompt kinds, placeholders. ≤150 lines |
| `docs/sdlc/flow-spec.md` | 2 | Owner: `flow.json`, exits, reserved exits, driver-fixed exits and route, candidate rules, bundle check, chunk land and re-entry, the `json sdlc-env` block, error codes. ≤200 lines, over standard 9's 150 ([O13](#questions-for-the-operator)) |
| `docs/sdlc/fixtures/flows/`, `docs/sdlc/fixtures/bundles/` | 2 | Flow and bundle fixtures with expected error codes |
| `docs/INTAKE.md` | 2 | New `## Script records` section: one line per bundle script **security** cleared ([Bundle layout](#bundle-layout-and-bundlemd)) |
| `docs/sdlc/bundle-runs.md` | 3 | Owner of every rule change in [HLD Rule changes](hld.md#rule-changes); routes run-root formats to `run-state.md`. ≤150 lines |
| `bundles/sdlc/` | 3 | The SDLC bundle: `bundle.md`, `flow.json`, `personas/*.md` |
| `skills/test-failure-handler/SKILL.md` | 3 | New first-party skill, `SOURCES.md` row |
| `skills/tracker-sdlc/SKILL.md`, `adapters/local.md` | 3 | Same-item claim rule (protected rules: rule maps, **security** read) |
| One-line routes in `docs/SDLC.md`, `docs/sdlc/subagents.md`, `build-review.md`, `branches-and-lands.md`, `plan-trial-spec.md`, `stage-result.md`, `skills/debug/SKILL.md` | 3 | Each route names the rule and links `bundle-runs.md` |
| `packages/sdlc-driver/` | 5 | Core driver: TypeScript, Node built-ins only, no harness dependency. `README.md` owns the driver-only formats, which only the driver writes and reads: `driver.json`, `driver/state.json`, `driver/ledger.json`, `index.jsonl`, `plan/items.json`. ≤200 lines; the types in `runroot.ts` and `state.ts` are the schema |
| `maintainers/design/solo-dlc/opencode-server.md` | Spec | OpenCode server note: the facts read in 1.19.3 and the Trial checks O-T1–O-T10. Exists; item 7 is groomed from it |
| `packages/opencode-sdlc/` | 7 | First harness. OpenCode plugin: the TUI `/sdlc` command, the operator-session input guard, the OpenCode adapter, the detached driver entry, the worker plugin, the smoke test |
| `packages/pi-sdlc/` | 6 | Second harness. Pi plugin: `/sdlc`, the Pi adapter, the detached driver entry, the worker extension, the smoke test |
| `skills/bundle-authoring/SKILL.md` | 4 | New skill |
| `skills/sdlc-followed-mode/SKILL.md` | 8 | New skill |
| `CHANGELOG.md` | all | One line under `## Unreleased` per item |

Final skill ids, fixed here: `test-failure-handler`, `bundle-authoring`,
`sdlc-followed-mode`, `sdlc-kickoff`.

**Where bundles live.** In the toolbox, at `bundles/<bundle-id>/`. A
run pins one toolbox commit and reads it from the
[toolbox copy](#toolbox-copy) in the run root; a product repo never
carries a copy of a bundle, persona, skill, or compiled file. Run prep
and every [Start](#start) (step 2) check the copy and the pin; a new pin is `/sdlc-repin` between stages
([Repin](#repin-the-toolbox)).
A third-party bundle enters `bundles/<id>/` only after
[INTAKE](../../../docs/INTAKE.md).

**Package layout.**

```text
packages/sdlc-driver/          # core; no runtime dependency; no harness import
  package.json                 # private; "type": "module"; engines node >=22.18
  tsconfig.json                # strict; erasableSyntaxOnly; noEmit
  README.md
  src/
    index.ts                   # public API: prepare, run, checkBundle, validateResult, repin
    cli.ts                     # `check BUNDLE_DIR [--at COMMIT]`, `validate RESULT --flow F --node N`,
                               # and the Run prep steps: `readiness`, `toolbox`, `state-init`, `status`,
                               # `persist`, `restore`, `drill` (Behavior 8)
    state.ts                   # durable run state: mirror, scan, commit, push, lease, restore, drill
    toolbox.ts                 # toolbox copy: remote rule, bare clone, config check, object reads
    compiled.ts                # compiled files: render from the copy, source hash, file hash
    env.ts                     # `json sdlc-env` parser, env command stages, dependency pre-steps
    backup.ts                  # optional session backup and restore
    json.ts                    # strict JSON reader (duplicate keys, nulls, trailing text)
    result.ts                  # stage-result v1 and candidate rules
    flow.ts  bundle.ts  check.ts   # flow types, bundle loader (toolbox copy at the pin), bundle check
    frontmatter.ts             # persona front matter subset parser
    runroot.ts                 # run.json, driver.json, index.jsonl, asks/, run folders, lock
    machine.ts                 # pure state machine: (state, event) -> (state, actions)
    stage.ts                   # stage pipeline: prompt, facts, snapshot, worker, validate, checks
    land.ts                    # land sub-machine, merge-tree classification
    prove.ts                   # command wrapper
    git.ts                     # git calls: hooks and fsmonitor off, replace objects off, no force option; copy rules
    snapshot.ts                # pre/post hashes, driver-file ledger, worktree, refs, and tickets checks
    tracker.ts                 # the repo skill's local read recipe, as fixed git argv
    groom.ts                   # frozen groom.md parser
    prompts.ts  facts.ts  scan.ts  console.ts  labels.ts
    adapter.ts                 # HarnessAdapter interface
  test/                        # node:test; fixtures from docs/sdlc/fixtures; fake worker
packages/opencode-sdlc/        # item 7, first harness: OpenCode plugin package
  package.json                 # private; "exports": {"./tui": "./src/tui.ts", "./server": "./src/server.ts"}
  src/tui.ts                   # TUI plugin: /sdlc, /sdlc-stop, and /sdlc-repin palette commands, dialogs, toasts
  src/server.ts                # operator-session server plugin: input guard (chat.message)
  src/opencode-adapter.ts      # HarnessAdapter for OpenCode: argv, env, worker config, process groups
  src/worker-config.ts         # builds OPENCODE_CONFIG_CONTENT for one stage
  src/driver-main.ts           # detached driver entry: core.run(RUN_ROOT, opencodeAdapter)
  src/cli.ts                   # O-T7 fallback only: the /sdlc steps on a terminal
  src/opencode-types.ts        # hand-written minimal types for the plugin API used
  worker/sdlc-worker.ts        # worker plugin; self-contained; loaded only by the worker config
  test/                        # node:test with a fake `opencode`
  smoke/                       # end-to-end smoke on real OpenCode; manual
packages/pi-sdlc/              # item 6, second harness: Pi plugin, a Pi package
  package.json                 # "pi": {"extensions": ["./extensions/sdlc.ts"]}
  extensions/sdlc.ts           # registers /sdlc, /sdlc-stop, and /sdlc-repin; input guard; widget
  src/pi-adapter.ts            # HarnessAdapter for Pi: argv, env, process groups
  src/driver-main.ts           # detached driver entry: core.run(RUN_ROOT, piAdapter)
  src/pi-types.ts              # hand-written minimal types for the Pi API used
  worker/sdlc-worker.ts        # worker extension; self-contained; NOT in the manifest
  test/                        # node:test with a fake `pi`
  smoke/                       # end-to-end smoke on real Pi; manual
```

Neither worker file is listed where the operator's own session loads
plugins: the OpenCode worker plugin is not in the package `exports`,
and the Pi worker extension is not in the Pi package manifest. Only
the worker's own config or `--extension` flag names the hashed copy.
`src/opencode-types.ts` and `src/pi-types.ts` replace dev dependencies
on `@opencode-ai/plugin` and the Pi package; each smoke test checks its
types against the real harness.

### Behavior 1: stage result v1 (item 1)

Item 1 edits `docs/sdlc/stage-result.md` in place. The file stays the
owner of the result format; the flow rules that need a flow live in
`flow-spec.md`.

Top-level fields (all required; unknown keys and nulls stay failures):

| Field | Type | Rule |
| --- | --- | --- |
| `schemaVersion` | integer | Exactly `1`. Not `"1"`, not `1.0` |
| `step` | string | As today |
| `status` | string | As today |
| `choice` | string | Matches `^[a-z][a-z0-9-]{0,31}$`. With a flow: an exit of the stage's node whose status list holds `status`, or a reserved exit allowed for that status ([Behavior 2](#behavior-2-bundle-and-flow-spec-item-2)). Without a flow, the reader checks the pattern only |
| `ticket` | string | Matches `^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$`. The id the repo tracker skill returns, on any backend, including `local`. Chunk-scope stages use the Epic id. The harness fills it from the invocation when it is omitted. A present value that differs is a failure: the harness rejects the result and never overwrites the value |
| `artifact` | string | One path relative to the run root. Segments match `[A-Za-z0-9._-]+`; no `.` or `..` segment, no leading `/`, no `\`. It names the result document or the output folder in the stage's own run folder; a folder ends with `/`. Absolute, outside the run root, outside the stage's run folder, or missing: failure |
| `evidence` | object | As today |
| `findings` | string | As today |

Rules added to the Rules section:

1. **Stage harness** fills `schemaVersion`, `step`, `ticket`, and
   `evidence.kind` from the invocation when they are omitted, and
   rejects any of them that mismatches the invocation (rule 4 of the
   current Rules list, extended).
2. A command stage's `choice` is set by the command wrapper: the node's
   `pass` exit when `exit_code` is `0`, else its `fail` exit. Its
   `artifact` names its `commands.json` (new rule 5).
3. Out of scope: the line now says the flow file and `choice` routing
   are in `docs/sdlc/flow-spec.md`.

Example:

```json
{"schemaVersion": 1, "step": "Build", "status": "pass", "choice": "review",
  "ticket": "der-a530", "artifact": "verifier-der-a530/run-3/result.md",
  "evidence": {"kind": "model", "checks": ["dod: acceptance bullets 1-4 hold"]},
  "findings": ""}
```

#### Line budget for `stage-result.md`

K1 caps every `docs/sdlc/` file at 150 lines, and the file has 150
today. It did not exist at 7a11696, so K2 (never grow) does not apply,
but standard 9 says a cap that needs a new file is an operator ask. Item
1 therefore adds no file and fits the cap by these exact edits, line
numbers as at 34e1278:

| Lines today | Edit | Net |
| --- | --- | --- |
| L37 | "The four top-level fields are required" → "Every top-level field is required" | 0 |
| L40–45 table | Add four rows: `schemaVersion`, `choice`, `ticket`, `artifact`, with the rules above | +4 |
| L77–78 | Rule 4 rewritten as rule 1 above, still two lines | 0 |
| after L78 | New rule 5, two lines | +2 |
| L101–146 | Cut the four `###` example headings L103, L118, L126, L135 and their blank lines L104, L119, L127, L136: −8. Each of the five examples gains one line for the new fields: +5. Fold the lone closing brace onto the line before it in the model `pass` (L115, −1) and `blocked` (L132, −1) examples. In the `needs_input` example, join L140 (`"kind": "model",`) onto L139 and fold the closing braces L142 and L144 onto the lines before them (−3). Together: −5 | −8 |
| L149–150 | Out-of-scope sentence reworded, still two lines | 0 |

Result: 148 lines. Item 3's one-line route to `bundle-runs.md` makes it
149. Both pass K1. Item 1's proving commands include
`test "$(wc -l < docs/sdlc/stage-result.md)" -le 150`.

Fixtures: one file per rule, named for the error code it proves
(`result.choice-pattern.json`, `result.artifact-escape.json`, …), each
with `NAME.expect.json`: `{"valid": false, "codes": ["result.artifact-path"]}`.
Error codes: `result.not-object`, `result.trailing-text`,
`result.duplicate-key`, `result.unknown-key`, `result.null`,
`result.schema-version`, `result.step`, `result.status`,
`result.choice-pattern`, `result.ticket-pattern`, `result.ticket-mismatch`,
`result.artifact-path`, `result.artifact-outside-run`,
`result.artifact-missing`, `result.evidence-kind`,
`result.evidence-missing`, `result.evidence-extra`,
`result.command-disagreement`, `result.findings-empty`. Flow-aware codes
live in `flow-spec.md`.

### Behavior 2: bundle and flow spec (item 2)

#### Bundle layout and `bundle.md`

```text
bundles/<bundle-id>/
  bundle.md                    # required
  flow.json                    # required
  personas/<persona-id>.md     # one per persona the flow names
  skills/<skill-id>/SKILL.md   # optional; skills owned only by this bundle
  scripts/                     # optional; run only by command nodes
```

- `<bundle-id>` matches `^[a-z][a-z0-9-]{0,31}$` and equals
  `flow.json` `id`.
- No symbolic links, no other top-level entries, no file over 256 KiB.
- `bundle.md` has these headings, in order: `# Bundle — <id>`,
  `## What it is`, `## Flow summary` (entry node, item entry node, one
  line per node: id, step, kind, persona), `## Required skills` (one
  bullet per skill id), `## Personas` (one bullet per persona id),
  `## Modes` (`enforced`, `followed`, or both). A bundle with
  `scripts/` adds `## Scripts`: one bullet per file,
  `` `scripts/<file>` sha256 `<hex>` intake `<record>` ``, where
  `<record>` names the [INTAKE](../../../docs/INTAKE.md) record under
  which **security** cleared that exact file. First-party scripts clear
  INTAKE too. The bundle check fails a script whose hash differs or
  that has no bullet (`bundle.script-intake`).
- **Script records.** A `<record>` matches `^[a-z0-9][a-z0-9-]{0,39}$`
  and names one line under `## Script records` in `docs/INTAKE.md`:
  `` `<record>` `bundles/<bundle-id>/scripts/<file>` sha256 `<hex>` ``.
  **security** writes that line when it clears the file. For a bundle
  commit outside reviewed history ([`run.json`](#runjson)), the
  driver's start-time bundle check also reads `docs/INTAKE.md` with
  `git -C <home> show <ref>:docs/INTAKE.md` at each derived reviewed
  ref, and fails a script unless one of them holds a line with its
  record, path, and hash (`bundle.script-intake`). A record that exists
  only in the bundle commit, or in any commit that is not an ancestor
  of a derived reviewed ref, does not count. A bundle commit inside
  reviewed history needs only the bullet.
- `## Required skills` equals the union of every persona's and node's
  `skills`. Each id resolves to `skills/<id>/SKILL.md` in the skills
  home at the pinned commit, with a `SOURCES.md` row, or to the bundle's
  own `skills/<id>/SKILL.md`.

#### Persona files

`personas/<id>.md` is front matter, then a body. The front matter is a
YAML subset, parsed without a YAML library: one `key: value` per line;
a value is `true`, `false`, a non-negative integer, a bare word matching
`^[A-Za-z0-9._/-]+$`, or a flow list `[a, b]` of bare words. No quotes,
nesting, anchors, or comments. Anything else is `persona.frontmatter`.

| Key | Required | Rule |
| --- | --- | --- |
| `schemaVersion` | yes | `1` |
| `id` | yes | Equals the file stem. Chunk scope: `^[a-z][a-z0-9-]{0,31}$`. Item scope: `^[a-z][a-z0-9-]{0,7}$`, so `<id>-<suffix>` fits a label ([Labels](#labels)) |
| `job` | yes | One of `refiner`, `architect`, `designer`, `ux-reviewer`, `security`, `groom-reviewer`, `manager`, `builder`, `verifier`, `reviewer` |
| `scope` | yes | `chunk` or `item` |
| `readOnly` | yes | `true` or `false`. Must be `true` when `job` is `refiner`, `ux-reviewer`, `security`, `groom-reviewer`, `verifier`, or `reviewer` |
| `model` | yes | A model slot name in `run.json` `models` |
| `tools` | yes | Subset of the neutral names `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`, which are Pi's built-in names; the OpenCode adapter maps them to permission rules ([OpenCode adapter](#opencode-adapter-and-worker-command-line)). With `readOnly: true`, no `edit` or `write` |
| `skills` | yes | Skill ids packed into the mint prompt; `[]` allowed |
| `tracker` | yes | `true`: pack `tracker-sdlc` and the repo tracker skill |

Body sections, in this order:

1. `## Role` — the role prompt. Required.
2. `## State template` — the `state.md` template. Required; at most 60
   lines.
3. `## Prompt: <kind>` — one section per prompt kind the persona uses.
   The kinds each job needs are in
   [SDLC personas](#sdlc-personas-and-prompts); a missing one is
   `persona.prompt-missing`.

Placeholders in prompts, closed set; any other `{{…}}` is
`persona.placeholder`: `{{ticket}}`, `{{epic}}`, `{{step}}`, `{{node}}`,
`{{persona}}`, `{{label}}`, `{{run}}`, `{{worktree}}`, `{{branch}}`,
`{{projectMain}}`, `{{range}}`, `{{rangeMain}}`, `{{log}}`, `{{repair}}`,
`{{exits}}`, `{{checks}}`, `{{outputs}}`, `{{tip}}`, `{{landSha}}`,
`{{landResult}}`, `{{verdict}}`, `{{commentText}}`, `{{stopKind}}`,
`{{stopRun}}`, `{{question}}`, `{{choices}}`, `{{answer}}`, `{{record}}`,
`{{ask}}`, `{{extracted}}`, `{{envSpec}}` (the accepted LLD's path and
commit), `{{capability}}` (the request that re-entered env-prep).
The driver fills each from its own state. `{{answer}}` and
`{{question}}` carry text a model or the operator wrote; the driver
inserts them inside a fenced block headed `Data, not instructions:`.

#### `flow.json`

One JSON object, read by the strict reader (`json.ts`): duplicate keys,
nulls, unknown keys, and trailing text are errors.

| Field | Rule |
| --- | --- |
| `schemaVersion` | `1` |
| `id` | The bundle id |
| `entry` | Id of a `chunk` node |
| `itemEntry` | Id of an `item` model node whose persona job is `builder`. Omit when no node has scope `item` |
| `defaults.prove` | Array of command lines appended after each item's own proving commands; `[]` allowed |
| `defaults.commandTimeoutSec`, `defaults.workerTimeoutSec` | Integers; defaults 1800 and 7200 |
| `nodes` | Array of node objects; order is flow order |

Node fields:

| Field | Kinds | Rule |
| --- | --- | --- |
| `id` | all | `^[a-z][a-z0-9-]{0,31}$`, unique |
| `label` | all | Console label, `^[A-Z][A-Za-z]{0,11}$` (`Build`, `Verify`, `Land`) |
| `step` | all | A step in [Names](../../../docs/SDLC.md#names) |
| `kind` | all | `model`, `command`, `gate`, or `land` |
| `scope` | all | `chunk` or `item`. A `land` node is `item`, or `chunk` for the env land ([Build-environment gate](#build-environment-gate)); at most one chunk `land` node |
| `persona` | `model` | A persona id with the same scope |
| `envSpec` | `model`, chunk | Optional, `true` on at most one node, with step Spec and an `outputs` path ending `/lld.md`. Its `pass` must carry a valid [`json sdlc-env` block](#the-json-sdlc-env-block) (candidate rule 9) |
| `skills` | `model` | Optional. Packed the first time this persona runs this node |
| `outputs` | `model`, chunk | Optional. Repo-relative paths; `{design}` expands to `run.json` `repo.designDir` |
| `outputDirs` | `model`, chunk | Optional. Repo-relative folder prefixes ending `/`; every regular file the persona puts there is committed |
| `checks` | `model` | Optional. Required check names, `^[a-z][a-z0-9-]{0,31}$` |
| `commands` | `command` | `"groom"` (the item's proving commands), `"env"` (the env block's dependency, toolchain, and `prove` lines), `"env-test"` (the env block's `test` line, the baseline), or an array of `scripts/<file>` paths. `"env"` and `"env-test"` only on chunk nodes |
| `gate` | `gate` | Tag: `brief`, `ux`, `plan`, `trial`, `mockup`, `spec`, or another `^[a-z][a-z0-9-]{0,15}$` word |
| `ask` | `gate` | The ask text for the manager's `ask-human.md` draft: the decision, the committed files that hold its facts and the recommendation, and what to quote from them. The `gate` prompt passes it as `{{ask}}` |
| `builder`, `prove`, `verify`, `review` | `land` | Node ids of the land node's scope: the builder model node, the proving `command` node, the verifier model node, and the Review node |
| `exits` | all | Array of exit objects |

Exit fields: `name` (`^[a-z][a-z0-9-]{0,31}$`, unique per node, never
`stop` or `operator`), `statuses` (non-empty subset of the four),
`to` (a node id, `@items`, or `@done`), and these optional fields:

- `say`: one line the console prints when the exit is taken;
  placeholders allowed.
- `checks`: check names required when a candidate takes this exit, in
  addition to the node's `checks`. For these names, `n/a` is not a
  finding (`flow.check-missing`).
- `extract` (`gate` nodes only): `{"from": "<repo path>", "heading":
  "<heading text>", "to": "<file name>"}`. When the exit is taken, the
  driver fetches, copies the section under that `##` heading of `from`
  at the project-main tip into the gate result's run folder as `to`, and
  sets `{{extracted}}` to its absolute path for `say`. `from` may use
  `{design}`. A missing file or heading is `check failed: extract`, an
  `operator` stop.

Targets and exit shapes:

- `@items` ends the chunk phase and starts each planned item at
  `itemEntry`. Only chunk nodes may target it.
- `@done` ends the current scope: for an item, it is landed+verified;
  for the chunk, the run is complete once every item is done.
- `command` nodes have exactly two exits: one with `["pass"]`, one with
  `["fail"]`.
- Each `gate` exit has exactly one status, `pass` or `fail`.
- A `land` node has exactly one exit, `done`, with `["pass"]`: an item
  land to `@done`, the chunk land to a chunk node.

**Reserved exits.** Every node has two exits that no flow lists:

| Exit | Worker may choose it with | Driver-authored results may also use it with | Route |
| --- | --- | --- | --- |
| `stop` | `blocked`, `needs_input` | `fail` | Resume the manager; it may `resume`, `defer`, or `escalate` |
| `operator` | `needs_input` | `fail` | Resume the manager; it may only `escalate` |

A worker candidate with `fail` and a reserved exit is invalid
(`flow.reserved-status`). Driver-authored `fail` results with `operator`
record failed checks on model stages.

#### Driver-fixed exits

These stages take their exits from this table, owned by the flow spec,
not from the flow file. They have the same status as node exits: a
candidate's `choice` must be in the row for its stage, and the reserved
exits apply as above unless the row says otherwise.

| Stage | Prompt kinds | Exits |
| --- | --- | --- |
| Land builder, merging the tip | `merge-tip` | `ready` [`pass`] |
| Land builder, fixing after a land check | `test-failure`, `fix` | `ready` [`pass`, `fail`] |
| Land verifier, re-run or post-land | `land-recheck`, `post-land` | `ok` [`pass`], `fix` [`fail`] |
| Land proving commands, on the item or on the integration merge | — | `ok` [`pass`], `fix` [`fail`] |
| Architect paperwork | `paperwork` | `posted` [`pass`]. Reserved exit: `stop` only |
| Manager | `stop`, `gate`, `apply-answer` | `resume` [`pass`], `defer` [`pass`], `escalate` [`needs_input`]. For an `operator` stop or a gate: `escalate` only. Reserved exits are not offered |
| Invalid-result repair | `repair` | The exits of the stage it repairs |
| Answer | `answer` | The exits of the stopped node or stage |
| Rehydrated session | `rehydrate`, wrapping the prompt kind the stage would have sent | The exits of that stage ([Sessions and rehydrate](#sessions-and-rehydrate)) |

**Driver-fixed route.** While `chunk.reentry` is set, the chunk `land`
node's `done` goes to `@items`, not to its flow `to`
([Build-environment gate](#build-environment-gate), re-entry). The flow
spec states this override; the bundle check adds no edge for it.

**Candidate rules.** A worker writes `candidate.json` with the
`sdlc_result` tool or with `sdlc_write`
([Worker plugin (OpenCode)](#worker-plugin-opencode),
[Worker extension](#worker-extension) for Pi).

1. `schemaVersion`, `step`, `ticket`, and `evidence.kind` may be
   omitted; when present they must equal the invocation's values
   (`flow.fixed-field`). The driver rejects a mismatch and never
   overwrites the field.
2. `choice` must be allowed for `status` by the node, or by the
   [driver-fixed exits](#driver-fixed-exits) row for the stage
   (`flow.choice-not-allowed`).
3. `pass` with node `checks`, or with exit `checks` on the chosen exit:
   each name appears as the prefix `<name>: ` of one `evidence.checks`
   entry, followed by a finding. For node checks, `n/a — <why>` is also
   a finding (`flow.check-missing`).
4. `pass` with node `outputs`: each path exists as a regular file at
   `out/<path>` in the run folder; no symbolic link anywhere under
   `out/` (`flow.output-missing`, `flow.output-symlink`).
5. `artifact` follows item 1 and lies in this run folder.
6. `state.md` exists, has at most 60 lines and 6,000 characters
   (`flow.state-size`).
7. A builder run with status `pass` or `fail` leaves no uncommitted
   change in its worktree (`flow.uncommitted`).
8. The verifier's `ledger.json` exists and is valid
   ([Verifier ledger](#sdlc-personas-and-prompts)) (`flow.ledger`).
9. `pass` on an `envSpec` node: `out/<lld path>` has one
   `## Build environment` section holding exactly one valid
   [`json sdlc-env` block](#the-json-sdlc-env-block) (`flow.env-block`).
10. An `env-capability: <one line>` entry in `evidence.checks` is
    allowed only with `needs_input` and `choice: operator`
    (`flow.env-capability`); it makes the stop kind `env capability`
    ([Stops](#stops-and-the-manager)).

Any rule failing makes the candidate invalid
([Stage pipeline](#stage-pipeline) step 7).

**Results by source.** `evidence.kind` is fixed by who produces the
result:

| Result | `evidence.kind` | Evidence and findings |
| --- | --- | --- |
| Model stage, including land model sub-stages, paperwork, and manager stages | `model` | `pass` needs `checks`. Paperwork: `comment: <comment id the recipe printed>`. Manager `resume` or `defer`: `source: …` ([Stops](#stops-and-the-manager)) |
| Command stage, including land proving commands and an L7x push record | `command` | `command`, `exit_code`; `findings` per item 1 |
| Gate result, written from the operator's answer | `model` | `pass`: `checks` = `["operator-answer: asks/ask-N"]`. `findings` = the answer verbatim; an empty answer records nothing, so a `fail` always has findings |
| Failed check or invalid result on a model stage | `model` | `fail`; `findings` names the check, or the error codes |
| Failed check on a command stage | `command` | The wrapper result is kept unchanged; the failed check goes in `check.json` in the run folder |

A gate result uses `model` because the stage-result contract has two
kinds and the decision is not a command's exit code.

#### Bundle check

`sdlc-driver check BUNDLE_DIR [--at COMMIT]` reads the bundle at
`COMMIT` (default: the working tree, for authors). The driver runs the
same check at the pinned commit before every run. Output is one error
per line, `<file>: node <id> exit <name>: <code>: <message>`, or
`<file>: <field>: <code>: <message>` when no node applies; exit `0` when
clean, `1` on any error.

| # | Rule | Code |
| --- | --- | --- |
| B1 | `flow.json` passes the strict reader and the field tables | `flow.json`, `flow.field` |
| B2 | Node ids unique; every `to` resolves; `@items` only from chunk nodes; item nodes never target chunk nodes | `flow.target` |
| B3 | Every node reachable from `entry` (item nodes through `@items`); every node has an exit | `flow.unreachable`, `flow.dead-end` |
| B4 | Kind-specific exit shapes (command, gate, land) | `flow.exit-shape` |
| B5 | Reserved names `stop` and `operator` never listed | `flow.reserved-listed` |
| B6 | Each `model` node's persona exists, its scope matches, and its prompt kinds exist | `flow.persona`, `persona.prompt-missing` |
| B7 | Persona front matter, read-only rule, tool names, placeholders | `persona.*` |
| B8 | Every skill id resolves and has a `SOURCES.md` row or lives in the bundle; `## Required skills` matches | `bundle.skill` |
| B9 | `outputs` and `outputDirs` are normalized repo-relative paths | `flow.output-path` |
| B10 | A `land` node names existing nodes of its own scope and the right kind: `prove` is a `command` node with `commands: "groom"` (item land) or `"env"` (chunk land); `verify` is a model node with job `verifier`; `review` has step `Review`, job `reviewer`, and `checks` holding `intake`, `sha-pins`, `trust-boundary` | `flow.land-ref`, `flow.review-checks` |
| B11 | Gate rows below hold on every path | `gate.*` |
| B12 | `bundle.md` headings; no symbolic links; size caps; every `scripts/` file listed with its hash and intake record; outside reviewed history, that record and hash present in `docs/INTAKE.md` at a derived reviewed ref ([Script records](#bundle-layout-and-bundlemd)) | `bundle.layout`, `bundle.script-intake` |
| B13 | `extract` only on `gate` exits; `from` is a normalized repo-relative path; `to` matches `^[a-z0-9-]{1,40}\.md$` | `flow.extract` |
| B14 | `envSpec` on at most one Spec node with an `lld.md` output; `commands: "env"` or `"env-test"`, or a chunk `land` node, only when that node exists | `flow.env` |

Gate rows. The checker finds the nodes by kind, step, job, outputs, and
gate tag, so a flow cannot avoid a row by renaming nodes:

| Code | Any path from | Reaching | Must pass, in this order |
| --- | --- | --- | --- |
| `gate.comparables` | `entry` | The HLD node: chunk `model`, step Plan, an `outputs` path ending `/hld.md` | The comparables node: chunk `model`, step Plan, an `outputs` path ending `/comparables.md` |
| `gate.plan` | `entry` | The Spec node: `model`, step Spec, an `outputs` path ending `/lld.md` | The `gate` node tagged `plan` |
| `gate.trial` | `entry` | The Spec node, as in `gate.plan` | The `gate` node tagged `trial` |
| `gate.spec` | `entry` | Any Groom node, any item node, or any chunk node with a builder persona or a `"env"` or `"env-test"` command | The Spec node, then the `model` node with step Spec and job `security`, then the `gate` node tagged `spec` |
| `gate.env` | `entry` | Any Groom node, or any item node | The `gate` node tagged `env`, then the chunk `land` node |
| `gate.land` | Each `model` node with job `builder` | The `land` node of its scope | Its `prove`, `verify`, and `review` nodes |

A row whose target does not exist in the flow holds trivially. A row
whose target exists but whose required node does not is an error.

Algorithm: breadth-first search over pairs (node, k), where k counts the
required nodes passed in order; entering the k-th required node
increments k. Reaching the target with k below the number required is a
violation. The error names the exit used on the last edge into the
target, from the shortest counterexample path. The search is finite
because there are at most nodes × (required + 1) pairs. Stops and the
manager re-run the stopped node, so they add no flow edges. An env
re-entry ([Build-environment gate](#build-environment-gate)) is not a
flow edge either: it enters only the chunk builder node or the Spec
node, after every item already passed `gate.spec` and `gate.env`, and
from there follows flow edges back through the `env` gate and the chunk
land before any item runs again. The land
node's internal re-runs reach Review only through its `prove`, `verify`,
and `review` nodes, which are flow edges.

### Behavior 3: the SDLC bundle (item 3)

#### SDLC flow

`bundles/sdlc/flow.json`, `entry: refine`, `itemEntry: build`,
`defaults.prove: []`. `{design}` is `run.json` `repo.designDir`.

| Node | Label | Step | Kind | Persona | Outputs / checks / tag | Exits |
| --- | --- | --- | --- | --- | --- | --- |
| `refine` | Brief | Brief | model | refiner | — | `brief` [pass] → `brief-gate`. Back to Gather: `operator` with `needs_input` |
| `brief-gate` | Brief | Brief | gate | — | tag `brief`; ask: "Confirm the brief as the refiner left it, or say what to revise. Quote the refiner's proposed cuts and open points from its last `result.md`." | `confirmed` [pass] → `comparables`; `revise` [fail] → `refine` |
| `comparables` | Plan | Plan | model | architect | `{design}/comparables.md` | `hld` [pass] → `hld` |
| `hld` | Plan | Plan | model | architect | `{design}/hld.md`; checks `test-env` | `ux` [pass] → `ux` |
| `ux` | Plan | Plan | model | designer | `{design}/ux.md`, `{design}/user-stories.md` | `review` [pass] → `ux-review` |
| `ux-review` | Plan | Plan | model | ux-reviewer | — | `accept` [pass] → `ux-gate`; `fix` [fail] → `ux` |
| `ux-gate` | Plan | Plan | gate | — | tag `ux`; ask: "Accept `{design}/ux.md` and `{design}/user-stories.md`, waive the UX review in writing, or say what to revise. Quote the UX reviewer's verdict and open findings, and each open UX question with the designer's recommendation." | `accepted` [pass] → `plan-gate`; `waived` [pass] → `plan-gate`; `revise` [fail] → `ux` |
| `plan-gate` | Plan | Plan | gate | — | tag `plan`; ask: "Accept `{design}/hld.md`, or say what to revise. Quote each item under its `## Open` heading with the HLD's default or recommendation, and summarize its test harness and environment section: each dependency and integration the build needs." | `accept` [pass] → `trial-gate`; `revise` [fail] → `hld` |
| `trial-gate` | Trial | Trial | gate | — | tag `trial`; ask: "Run a Trial before Spec? Quote each unconfirmed fact and the recommendation from the `## Trial question` section of `{design}/hld.md`. On yes, the driver writes the Trial kickoff prompt to a file and prints its path." | `trial` [pass] → `trial-done`, extract `{design}/hld.md` heading `Trial kickoff prompt` to `trial-kickoff.md`, say `Trial kickoff prompt written: {{extracted}}`; `skip` [pass] → `spec` |
| `trial-done` | Trial | Trial | gate | — | tag `trial-done`; ask: "Is the Trial done, with each verdict recorded under `{design}/poc/`? Quote each verdict and any HLD change the Trial report recommends." | `done` [pass] → `spec`; `revise` [fail] → `hld` |
| `spec` | Spec | Spec | model | architect | `{design}/lld.md`; `envSpec` | `mockups` [pass] → `mockups` |
| `mockups` | Spec | Spec | model | designer | `outputDirs` `{design}/mockups/` | `none` [pass] → `security`, exit check `no-screen`; `review` [pass] → `mockup-review` |
| `mockup-review` | Spec | Spec | model | ux-reviewer | — | `accept` [pass] → `mockup-gate`; `fix` [fail] → `mockups` |
| `mockup-gate` | Spec | Spec | gate | — | tag `mockup`; ask: "Accept the mockups under `{design}/mockups/`, or say what to revise. Quote the UX reviewer's verdict and open findings." | `accepted` [pass] → `security`; `revise` [fail] → `mockups` |
| `security` | Spec | Spec | model | security | checks `authz`, `secrets`, `egress`, `data-class`, `writers`, `env-commands` | `accept` [pass] → `spec-gate`; `fix` [fail] → `spec` |
| `spec-gate` | Spec | Spec | gate | — | tag `spec`; ask: "Accept `{design}/lld.md`, and accept in writing each residual its trust-boundary section lists under operator must accept; or say what to revise. Quote security's findings with severities, each open operator question with the LLD's recommendation, and the build-environment block's dependencies and `passEnv` names." | `accept` [pass] → `env-prep`; `revise` [fail] → `spec` |
| `env-prep` | Env | Build | model | env-builder | — | `prove` [pass, fail] → `env-prove`; `respec` [needs_input] → `respec-gate` |
| `respec-gate` | Env | Spec | gate | — | tag `respec`; ask: "The env-builder says the LLD's build environment cannot be built as written. Route back to Spec for an LLD change, or tell the env-builder how to go on. Quote its reasons from its last `result.md`." | `spec` [pass] → `spec`; `retry` [fail] → `env-prep` |
| `env-prove` | Env | Build | command | — | `commands: "env"` | `baseline` [pass] → `env-baseline`; `fix` [fail] → `env-prep` |
| `env-baseline` | Env | Build | command | — | `commands: "env-test"` | `green` [pass] → `env-verify`; `known` [fail] → `env-verify` |
| `env-verify` | Env | Build | model | env-verifier | checks `env-proof`, `baseline` | `review` [pass] → `env-review`; `fix` [fail] → `env-prep` |
| `env-review` | Env | Review | model | env-reviewer | checks `intake`, `sha-pins`, `trust-boundary`, `env-harness` | `gate` [pass] → `env-gate`; `fix` [fail] → `env-prep` |
| `env-gate` | Env | Build | gate | — | tag `env`; ask: "Accept the build and test environment, send it back to the env-builder, or route back to Spec for an LLD change. Quote the env-verifier's `env-proof` and `baseline` findings, the baseline status with any pre-existing failures, and the env-reviewer's verdict." | `accept` [pass] → `env-land`; `revise` [fail] → `env-prep`; `spec` [fail] → `spec` |
| `env-land` | Env | Build | land | — | builder `env-prep`, prove `env-prove`, verify `env-verify`, review `env-review` | `done` [pass] → `groom`; `@items` during a re-entry ([driver-fixed route](#driver-fixed-exits)) |
| `groom` | Groom | Groom | model | architect | `{design}/groom.md` | `review` [pass] → `groom-review` |
| `groom-review` | Groom | Groom | model | groom-reviewer | — | `file` [pass] → `file-tickets`; `fix` [fail] → `groom` |
| `file-tickets` | Groom | Groom | model | manager | `{design}/groom.md` (the frozen copy) | `items` [pass] → `@items` |
| `build` | Build | Build | model | builder | — | `prove` [pass, fail] → `prove` |
| `prove` | Build | Build | command | — | `commands: "groom"` | `verify` [pass] → `verify`; `fix` [fail] → `build` |
| `verify` | Verify | Build | model | verifier | checks `dod` | `review` [pass] → `review`; `fix` [fail] → `build` |
| `review` | Review | Review | model | reviewer | checks `intake`, `sha-pins`, `trust-boundary`, `env-harness` | `land` [pass] → `land`; `fix` [fail] → `build` |
| `land` | Land | Build | land | — | builder `build`, prove `prove`, verify `verify`, review `review` | `done` [pass] → `@done` |

A builder `fail` still goes to the proving commands: the commands, not
the builder, decide whether the item goes back. The builder's own `fail`
is not a check sending the item back.

- **`mockups` `none`** needs the exit check `no-screen: <reason>`, a
  written reason that the change has no screen; `n/a` does not count.
  A designer without such a reason takes `review`, or asks for the
  operator's waiver with the `operator` exit; the waiver is then the
  recorded answer in `asks/`.
- **`trial-gate`** carries SD-9: the ask names the HLD's unconfirmed
  facts and its recommendation, `trial` writes `trial-kickoff.md` into
  the gate result's run folder (`operator/run-N/`) and prints its path,
  and `skip` continues to Spec. `gate.plan` and `gate.trial` together
  keep the run from reaching Spec without both answers.
- **Env nodes** (`env-prep` to `env-land`) are the
  [build-environment gate](#build-environment-gate). `env-baseline`
  takes `known` on a red baseline and still goes to the env-verifier,
  which records the pre-existing failures; the env-builder is not sent
  back for them. `gate.env` keeps Groom and every item behind the
  `env` gate and the env land.
- **`env-harness`** on both Review nodes: the change adds no test
  harness, service, dependency start, or toolchain outside the accepted
  `json sdlc-env` block, or the finding names it.

#### SDLC personas and prompts

| Persona (folder) | Job | Scope | Read-only | Tools | Packed skills | Prompt kinds |
| --- | --- | --- | --- | --- | --- | --- |
| `refiner` | refiner | chunk | yes | `read,bash,grep,find,ls` | `yagni` | `mint`, `resume` |
| `architect` | architect | chunk | no | all seven | `sdlc-artifacts`, `docs-google-style`; node `spec` adds `security-hardening` | `mint`, `resume`, `node-comparables`, `node-hld`, `node-spec`, `node-groom`, `paperwork` |
| `designer` | designer | chunk | no | all seven | `ux-design`, `sdlc-artifacts` | `mint`, `resume`, `node-mockups` |
| `ux-reviewer` | ux-reviewer | chunk | yes | read set | `ux-design` | `mint`, `resume` |
| `security` | security | chunk | yes | read set | `security-hardening` | `mint`, `resume` |
| `groom-reviewer` | groom-reviewer | chunk | yes | read set | `sdlc-artifacts` | `mint`, `resume` |
| `manager` | manager | chunk | no | all seven | `sdlc-artifacts` | `mint`, `stop`, `gate`, `apply-answer`, `node-file-tickets` |
| `env-builder` | builder | chunk | no | all seven | `tdd`, `yagni`, `debug`, `docs-google-style`, `security-hardening`; `test-failure-handler` on the first `test-failure` prompt | `node-env-prep`, `resume`, `test-failure`, `fix`, `merge-tip` |
| `env-verifier` | verifier | chunk | yes | read set | `verify-before-done` | `mint`, `recheck`, `land-recheck` |
| `env-reviewer` | reviewer | chunk | yes | read set | `pr-review`, `security-hardening` | `mint`, `rereview` |
| `builder-<suffix>` | builder | item | no | all seven | `tdd`, `yagni`, `debug`, `docs-google-style`, plus the item's `skills` from `groom.md`; `test-failure-handler` on the first `test-failure` prompt | `mint`, `resume`, `test-failure`, `fix`, `merge-tip` |
| `verifier-<suffix>` | verifier | item | yes | read set | `verify-before-done`, `docs-google-style` | `mint`, `recheck`, `land-recheck`, `post-land` |
| `reviewer-<suffix>` | reviewer | item | yes | read set | `pr-review`, `security-hardening` | `mint`, `rereview` |

Every persona has `tracker: true`. The read set is
`read,bash,grep,find,ls`. The driver always adds the extension tools
`sdlc_write` and `sdlc_result`. Every persona may also receive `repair`,
`answer`, and `rehydrate` prompts; those three are fixed by the driver,
not the bundle. The packed skills of a persona's `skills` front matter
are in its [compiled file](#compiled-files); the others in this column are
packed per stage.

**Why a separate `env-builder`.** The architect wrote the LLD's
environment section; proving it with the same session would grade its
own design, and would give a design persona write access to a code
worktree. The env work is build work (TDD, debugging, failing logs), so
it gets a builder-job persona with its own session, and its own
verifier and reviewer, as an item does.

**Harness rule** (every builder, verifier, and reviewer prompt, and
`test-failure-handler`): use only the test harness, dependencies, and
toolchain of the accepted `json sdlc-env` block; never install, start,
or write a new one. A change that needs one ends with `needs_input`,
`choice: operator`, and an `env-capability: <one line>` check
(candidate rule 10).

`state.md` templates (the body section `## State template`):

| Persona | Template headings and lines |
| --- | --- |
| builder, env-builder | `## Corrected errors` (`- <what broke> → <fix> (<run>)`), `## Open findings` (`- <id> <criticality> <one line> (<source>)`), `## Do not repeat` (`- <approach> — <why it failed>`), `## Next` (one line) |
| verifier, env-verifier | `## Ledger` (table: `Id`, `Criticality`, `Status`, `Issue`, `Raised`, `Fixed`), `## Nits` (recorded, not sent back), `## Last commands seen` (`- <prove run>: <status>`) |
| reviewer, env-reviewer | `## Verdicts` (`- <run> <range> <verdict>`), `## Open review comments`, `## Security reads` (`intake`, `sha-pins`, `trust-boundary`, one line each) |
| architect | `## Node`, `## Decisions`, `## Open`, `## Outputs written` |
| refiner | `## Brief version`, `## Cuts proposed`, `## Open` |
| designer, ux-reviewer | `## Work`, `## Findings` (`- <id> open or fixed <one line>`), `## Open` |
| security | `## Boundaries read`, `## Findings` (`- <id> <severity> open or fixed <one line>`), `## Open` |
| groom-reviewer | `## Reviewed commit`, `## Findings`, `## Open` |
| manager | `## Stops handled` (`- <ask or stop> <decision> <source>`), `## Pending asks`, `## Parked` |

**Verifier ledger.** Each verifier run writes `ledger.json`: an array of
`{"id": "V<n>", "criticality": "breaking"|"critical"|"major"|"minor"|"nit",
"status": "open"|"fixed", "summary": "<one line, at most 200 characters>",
"raised": "<run>", "fixed": "<run>"|""}`. Ids are stable across runs; a
run never deletes an entry. A re-check may add an entry only with
criticality `breaking` or `critical`, unless it is the verifier's first
run on the item. `nit` entries are never `open` in facts sent to the
builder. A verifier `pass` requires no `open` entry above `nit`.

**Prompt kinds**, all written in the persona file:

| Kind | Sent when | Must tell the worker |
| --- | --- | --- |
| `mint` / `node-<id>` | First run of the persona, or first run of that node | The role, the node's task, `{{outputs}}`, `{{exits}}`, `{{checks}}` |
| `node-hld` | The HLD node | Also: a required `## Test harness and environment` section: each dependency to run (for example a database engine, a single-node Kafka, or an existing platform such as AD, with the operator's integration instructions from the brief or an ask), build tools and toolchains, and the test harness; checks `test-env` |
| `node-spec` | The Spec node | Also: a required `## Build environment` section with one [`json sdlc-env` block](#the-json-sdlc-env-block): each dependency's setup (clone, configure, auth by variable name only), start, ready, reset, and stop lines, the toolchain version lines, the proving lines, and the repo test command; the driver rejects a `pass` without it (candidate rule 9) |
| `node-env-prep` | First env-prep run, or a re-entry | Build the harness and environment that `{{envSpec}}` defines, nothing more; commit harness code on `{{branch}}`; do not edit the LLD; `respec` with reasons when the section cannot be built as written; on a re-entry, `{{capability}}` |
| `resume` | Later run of the same node | Only what changed |
| `test-failure` | Proving commands failed | Load `test-failure-handler`; open `{{log}}`; `{{repair}}` |
| `fix` | Verifier or reviewer sent the item back | Fix the open findings in the facts; do not move the ticket |
| `merge-tip` | Land step 1, tip moved | Merge `{{tip}}` into `{{branch}}` with a merge commit; never rebase; `blocked` if a conflict cannot be resolved |
| `recheck`, `land-recheck` | Verifier re-check, before or inside land | Confirm committed issues; new issues only if breaking or critical. The env-verifier also checks every env block line has evidence (`env-proof`) and records pre-existing baseline failures in `baseline.json` (`baseline`) |
| `post-land` | Land step 4 | Read `{{landResult}}` at `{{landSha}}`; `done` or back to `in_progress` |
| `rereview` | Review again | `{{range}}` and the open review comments only |
| `paperwork` | After the driver commits the HLD or LLD | Post `{{commentText}}` on `{{epic}}`; write nothing else; finish with `posted` |
| `stop` | Any stop | `{{stopKind}}`, `{{stopRun}}`, `{{question}}`, `{{choices}}` |
| `gate` | A gate node | Draft `ask-human.md` from `{{ask}}`: quote what it names from the committed files in `worktrees/integrate`, and give the recommendation; choices are the gate's exits |
| `apply-answer` | The operator answered a non-gate ask | Turn `{{answer}}` into `resume` or `defer` |

#### `groom.md` items for bundle runs

Each `### G<n>: <title>` section of `groom.md` holds exactly one fenced
block with the info string `json sdlc-item`:

````text
```json sdlc-item
{"slug": "result-format", "blockedBy": [], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver test"]}
```
````

- `slug`: `^[a-z0-9][a-z0-9-]{0,39}$`; the item branch is
  `item/<suffix>-<slug>`.
- `blockedBy`: G ids in this file.
- `skills`: extra packed skill ids for the builder, at most one language
  skill ([language-router](../../../skills/language-router/SKILL.md#iron-law)).
- `prove`: non-empty array of command lines, each at most 1,000
  characters, no newline.

The groom reviewer checks that the block agrees with the prose, and
that every `prove` line uses only the harness and dependencies of the
accepted `json sdlc-env` block and allows for the recorded baseline
failures; Groom runs after the env land, so both are known. At
freeze, the manager fills the `Tickets:` line as
`` `G1` = `der-a530`, `G2` = `der-a531` ``; the driver parses only that
line and the blocks.

#### `test-failure-handler`

A first-party skill, at most 60 lines. Steps: open the log at the path
in the prompt; find the first failure; load `debug` and find the root
cause; write a failing test when the cause is in code (`tdd`); fix;
commit; add one `## Corrected errors` line and, for an approach that
failed, one `## Do not repeat` line to `state.md`. Never edit the
proving commands, `groom.md`, or the LLD's env block. Never add a
harness (the [harness rule](#sdlc-personas-and-prompts)). Never move the
ticket.

#### Tracker wiring and `bundle-runs.md`

Item 3 writes `docs/sdlc/bundle-runs.md` as the owner of every row in
[HLD Rule changes](hld.md#rule-changes) and adds a one-line route from
each current owner. Two of them change protected rules:

1. `skills/tracker-sdlc/SKILL.md` Claim, steps 1 and 4: in a bundle
   run, a marker or assignee whose label is `builder-`, `verifier-`, or
   `reviewer-` followed by the claiming persona's own suffix counts as
   the same item. This route adds no other condition.
2. `skills/tracker-sdlc/adapters/local.md`, `change: claim`: the
   assignee test accepts the same three labels with the same suffix.
   The change is one condition in that function; nothing else in the
   recipe changes.

Each edited agent file gets a rule map per the
[writing standard](../../writing-standard.md#rule-maps). Repo tracker
skills copied from the old recipe are upgraded with a Repair-style diff,
committed only on the operator's OK; this repo's own skill is one of
them. The contract version stays 2 (security ruling S5): K6's
`Contract version: 2` count stays 1.

**Claim-condition diff at Review (S5).** **security** runs K5's extract
of `skills/tracker-sdlc/adapters/local.md` at 7a11696 and at the item
tip and diffs the two. The diff must be exactly one changed line: the
assignee test in `change: claim` (`[[ -z $a || $a == "$AGENT" ]]`),
widened by the same-suffix condition and nothing else. Any other
changed line fails Review. The rule map records this as the one
expected K5 difference.

### Behavior 4: run root formats

All files are UTF-8. JSON files are written atomically: temporary file
in the same folder, `fsync`, `rename`. The driver refuses a run root
that is inside a git worktree, that is a symbolic link, or whose mode
grants any group or other permission; it creates the run root `0700`.

The run root has a durable part and a local part. At the `pushed` and
`local` [durability levels](#durable-run-state), the driver mirrors the
durable part (marked **D** below) into the state branch after each
stage. The local part is never committed: volatile, large, or
secret-bearing, or regenerated from the toolbox copy. Unmarked entries
are local, including everything under `driver/`, `repo.git/`,
`toolbox.git/`, `compiled/`, and `worktrees/`.

```text
RUN_ROOT/
  run.json             # D; Run prep writes; the operator confirms at the first /sdlc
  machine.json         # local; Run prep writes: harness paths, host id, backup folder
  driver.json          # D; driver only
  index.jsonl          # D; driver only; one line per event (UX Q3)
  checklist.md         # D; Run prep
  plan/items.json      # D; driver, after ticket filing
  asks/ask-N.json      # D; driver: ask and answer, machine copy
  asks/ask-N.md        # D; driver: the same, for people
  compiled/<persona>.md # local; driver: compiled files, regenerated from the pin
  toolbox.git/         # local; the toolbox copy: trunk and tags, bare
  env-data/            # local; the env commands' data folder (SDLC_ENV_DIR); outside the snapshot walk
  driver/lock          # run-root lock
  driver/console.log   # every console line
  driver/snapshot.json # pre-stage hashes of the stage in flight
  driver/ledger.json   # hash of each driver file at its last driver write
  driver/state.json    # tip record: seq, tip, genesis, pushedTip, restore; never mirrored
  driver/driver.stderr # the detached driver's stdout and stderr
  driver/facts/<persona>--run-N.md   # facts passed to that run
  driver/worker-ext/sdlc-worker-<sha12>.ts
  driver/worker-config/<persona>--run-N.json   # OpenCode: the worker config passed to that run
  driver/opencode/xdg-config/        # OpenCode: the workers' XDG_CONFIG_HOME; holds only an empty opencode/, mode 0500
  repo.git/            # driver's bare clone of the product repo
  worktrees/integrate/ # integration worktree, detached at project-main
  worktrees/<suffix>/  # one item worktree
  worktrees/env/       # the env-builder's worktree, on env/<chunk-slug>-<pass>
  worktrees/state/     # the state branch's worktree; the driver only (pushed, local)
  gatherer/run-1/      # Gather: brief.md (D); the Gather session copy (local)
  <persona>/opencode.db              # local; OpenCode: the persona's session database, with its -wal and -shm files
  <persona>/session.jsonl            # local; Pi: the persona's session file
  <persona>/run-N/     # see Run folder; D files listed there
  prove-<suffix>/run-N/  land-<suffix>/run-N/  land-env/run-N/  commands/run-N/  operator/run-N/
```

`repo.git/` and the folder names keyed by suffix refine the HLD layout:
item worktrees, the env worktree, the state worktree, and the
integration worktree share one bare clone whose
git directory sits inside the hashed run root
([Post-stage checks](#post-stage-checks)). The driver's command folders
(`prove-`, `land-`, `commands`) and `operator/` (gate results) are not
personas and never write to the tracker. Chunk command nodes
(`env-prove`, `env-baseline`) use `commands/`; the env land uses
`land-env/`.

#### Toolbox copy

`RUN_ROOT/toolbox.git` is a bare copy of `run.json` `bundle.remote`
that holds only its trunk and tags.
The driver reads every bundle, persona, skill, and script file, and
`docs/INTAKE.md`, from its object store at the pin, never from a
working tree. It is local, never mirrored, and rebuilt from the
confirmed remote at the pin while that remote holds the pin. Nothing
from it is copied into the product repo.

**Remote.** `bundle.remote` is an `https://host/path` URL or an SSH
URL, `ssh://host/path` or the scp form `[user@]host:path`. The host
must not start with `-`, and the URL holds no whitespace or control
character. Anything else is refused at Run prep and at every check of
the copy: a `<transport>::` prefix (`ext::`, `fd::`), `file://`, a
local path, user info with a password or token, or a query string. No
model proposes it. Run prep asks the operator to type it in full, with
no default or prefill, before anything is cloned or fetched; the skill
passes the typed text to `toolbox --remote`, which requires it to equal
`run.json` `bundle.remote` and records it as `driver.json`
`bundleRemote`. A `run.json` whose `bundle.remote` later differs from
`bundleRemote` is `check failed: toolbox`: a repin moves only the
commit, and another remote is another run. A restore asks for it again
from the genesis note ([Durable run state](#durable-run-state)).

**Trunk.** `run.json` `bundle.trunk` names the reviewed branch, `main`
unless the operator names another at Run prep; it passes
`git check-ref-format --branch` and does not start with `-`. The
reviewed ref is `refs/heads/<bundle.trunk>`, fetched by that name. The
remote's `HEAD` is never read, so a remote whose `HEAD` names another
branch changes nothing. The trunk is fixed for the run, like the remote.

**Genesis note.** At `pushed` and `local`, Run prep prints the only
copy, from driver state, in the turn that runs `state-init`:
`keep off this machine: genesis <40-hex>  toolbox <bundle.remote>  trunk <bundle.trunk>; a restore asks for all three`.
`plain` has no state branch and no note.

**Driver git in the copy.** Every driver git call there is
`git --git-dir=RUN_ROOT/toolbox.git --no-pager` with
`-c core.fsmonitor= -c core.hooksPath=/dev/null -c core.commitGraph=false`
`-c core.multiPackIndex=false -c fetch.writeCommitGraph=false -c gc.auto=0`
`-c maintenance.auto=false`,
`GIT_ALLOW_PROTOCOL=https:ssh`, `GIT_CONFIG_NOSYSTEM=1`,
`GIT_NO_REPLACE_OBJECTS=1`, `GIT_CONFIG_GLOBAL=driver/gitconfig`, and
no other `GIT_*` variable from the operator's environment.
`driver/gitconfig` is a local
[driver file](#driver-file-ledger), never mirrored, that `toolbox`
writes with only the operator's `credential.*` and `core.sshCommand`
values. `GIT_ALLOW_PROTOCOL` already refuses `ext::`, `fd::`, and
`file://`; `-c protocol.ext.allow=never -c protocol.file.allow=never`
stay as a second layer, so removing one layer opens nothing. Git runs
in the copy only for `init`, `config`, fetch, `rev-parse <tag>^{commit}`,
and `merge-base --is-ancestor`, never to read file bytes. The driver
needs git 2.32 or newer (`GIT_CONFIG_GLOBAL`); readiness R7 and every
Start refuse an older one.

`sdlc-driver toolbox RUN_ROOT --remote <typed> [--rebuild]` runs only
while no driver holds the lock: at Run prep, in the drill, and at a
restore, each after the operator typed the remote. `--rebuild` first
removes an existing copy, without running git in it, after a
`check failed: toolbox`:

1. Check that `--remote` passes the remote rule and equals `run.json`
   `bundle.remote` and, when set, `driver.json` `bundleRemote`; write
   `driver/gitconfig`. Then, as driver git:
   `git init --bare --template= --initial-branch=<trunk> toolbox.git`,
   `config remote.origin.url <remote>`, and the check's step 3 fetch.
2. Record `bundleRemote`, and in `driver.json` `toolbox` the SHA-256 of
   `toolbox.git/config` and `toolbox.git/HEAD`. `bundle.commit` must
   exist, a set `bundle.tag` must resolve to it, and the check's step 5
   must pass on it; else `check failed: toolbox`. Its ancestry is shown
   at the first `/sdlc` summary ([`run.json`](#runjson)).
3. Compile each [compiled file](#compiled-files) that `driver.json`
   `compiled` lists (`state-init` records the chunk personas' later).

**Check** (`toolbox`), at every [Start](#start) step 2, at the
[`run.json` summary](#runjson), and at [repin](#repin-the-toolbox)
step 1, in this order. Steps 1 and 2 read files only; no git command
runs in the copy before they pass, on any path, the finish of a pending
repin included:

1. `toolbox.git` is a folder, not a link; `config` and `HEAD` have the
   SHA-256s in `driver.json` `toolbox`, and `HEAD` is one line
   `ref: refs/heads/<name>`; none of these exists: `commondir`,
   `shallow`, `info/attributes`, `info/grafts`, `objects/info/alternates`,
   `objects/info/http-alternates`, `objects/info/commit-graph`,
   `objects/info/commit-graphs/`, `objects/pack/multi-pack-index`,
   `refs/replace/`, or a `packed-refs` line under `refs/replace/`.
2. `remote.origin.url` in that config equals `driver.json`
   `bundleRemote` and passes the remote rule.
3. `run.json` `bundle.remote` equals `bundleRemote`, and `HEAD` names
   `refs/heads/<bundle.trunk>`. Fetch
   `origin +refs/heads/<trunk>:refs/heads/<trunk> +refs/tags/*:refs/tags/*`.
   A failed fetch or a missing trunk ref fails here, naming it; it is
   never "not an ancestor".
4. `bundle.commit` is an ancestor of the fetched `refs/heads/<trunk>`,
   or equals the `to` of a `driver.json` `bundle.history` entry with
   `typed: true`. Record the fetched tip as `bundle.trunkTip`. At the
   summary, a pin that passes neither takes the typed-SHA path instead
   of failing.
5. Read every file the driver will use at `bundle.commit` (the bundle,
   personas, scripts, packed skills, `docs/INTAKE.md`) with the object
   hash checks of Reads, and run the bundle check on those bytes.

A failure is `check failed: toolbox`, naming the step, an `operator`
stop; the operator runs `toolbox --rebuild`, or retries once the remote
is reachable. A fetch writes refs and objects, never `config` or
`HEAD`, so their recorded hashes never change after `toolbox`. A pin
moved or a commit added while the driver is down therefore fails step
4 at the next Start, however consistent `driver.json` and the ledger
are.

**Reads.** The driver reads toolbox objects in its own process, never
with `git cat-file` or another git command, so no commit-graph,
replace ref, graft, or alternate can change what it reads. It finds each
object as a loose file or through a pack's `.idx`, reads those bytes on
one open file descriptor, inflates them (deltas resolve only inside the
same pack), and hashes `<type> <size>\0<bytes>` against the id; a
mismatch is `check failed: toolbox`. It walks from the pin's commit
down the trees to each blob. The bundle check, the INTAKE script-hash
checks, the skill packing, and the [command body](#command-body) use
only those bytes; a tree entry of type `160000` (a gitlink) under a
read path fails the bundle check. The driver loads the bundle and
personas into memory at check step 5 and rereads them only at the next
Start or repin.

The [`snapshot`](#post-stage-checks) walk covers `compiled/` like the
rest of the run root. Under `toolbox.git/` it records every path's
type, mode, and size, and hashes only `config`, `HEAD`, `packed-refs`,
and the files under `refs/`, every time, with no stat cache: a `bash`
write that adds, removes, or resizes a file there, or moves a ref,
fails the stage. Object files are not hashed per stage: a rewritten
object fails its next read, and a new commit matters only as a pin,
which check step 4 tests on the fetched trunk. The general SDLC's
version, DER-570, now follows this layout.

#### `run.json`

```json
{
  "schemaVersion": 1,
  "chunk": {"slug": "solo-dlc", "epic": "der-e421"},
  "bundle": {"id": "sdlc", "remote": "git@github.com:OWNER/agentic-toolbox.git",
             "trunk": "main", "tag": "v0.9.0", "commit": "<40-hex>"},
  "repo": {"origin": "git@github.com:OWNER/REPO.git", "trunk": "main",
           "projectMain": "integrate/solo-dlc", "designDir": "maintainers/design/solo-dlc",
           "test": "npm test"},
  "tracker": {"backend": "local", "skill": ".agents/tracker/SKILL.md",
              "keyPattern": "^der-[a-z0-9]{4}$", "local": {"branch": "tickets"}},
  "mode": "enforced",
  "state": {"level": "pushed", "branch": "sdlc/run/solo-dlc"},
  "harness": {"name": "opencode", "package": "opencode-ai", "version": "1.19.3",
              "plugin": {"name": "opencode-sdlc", "version": "0.1.0"},
              "integrity": {"opencode-ai": "sha512-<base64>", "opencode-linux-x64": "sha512-<base64>"},
              "treeSha256": "<hex>",
              "providers": {"local": {"npm": "@ai-sdk/openai-compatible",
                                      "models": {"qwen-coder": {"limit": {"context": 131072, "output": 16384}}}}}},
  "models": {"default": {"model": "local/qwen-coder", "contextWindow": 131072, "paid": false}},
  "spending": null,
  "labels": {"mode": "plain"},
  "limits": {"repairs": 3, "invalidRepairs": 1},
  "env": {"scrubExtra": []},
  "createdAt": "2026-10-18T07:00:00Z"
}
```

- `repo.origin` and `bundle.remote` must carry no user info (`://user@`
  with a password, or a token) and no query string. SSH and plain HTTPS
  forms are allowed; `bundle.remote` follows the stricter
  [remote rule](#toolbox-copy).
- `bundle.commit` is the pin; `bundle.tag` is the tag the operator
  chose, or `null` for a bare commit. `bundle.remote` is the URL the
  operator typed at Run prep, and `bundle.trunk` the reviewed branch,
  default `main`; both are fixed for the run
  ([Toolbox copy](#toolbox-copy)).
- `tracker.backend`: driven runs support `local` only in this chunk
  (security ruling S1). Run prep refuses any other backend, and `/sdlc`
  refuses to start a run root whose `run.json` names one, with the line
  `tracker backend <name> is not supported for driven runs yet; use local`.
  Linear for driven runs, both the driver's reads and the workers'
  writes, is the later item G9 with its own security gate
  ([Groom split](#groom-split-proposal), O5).
- `harness.name` is `opencode` (item 7, the first harness) or `pi`
  (item 6). The executable and Node paths are machine-local, in
  [`machine.json`](#machinejson).
- `repo.test`: the repo's test command as Run prep found it, or `null`
  for a repo without one yet. After the env land, the accepted env
  block's `test` line replaces it in the compiled files
  ([Compiled files](#compiled-files)).
- `state.level`: `pushed` (default), `local`, or `plain`;
  `state.branch`: `sdlc/run/<chunk-slug>`
  ([Durable run state](#durable-run-state)). A `plain` run has no
  branch.
- **Portable.** `run.json` holds no absolute path, host name, address,
  or credential, so it can be mirrored to the state branch and read on
  another machine. Run prep refuses to write one that fails the
  [scan patterns](#scan-patterns).
- **Harness pin.** `harness.package` and `harness.version` name the
  release: OpenCode `opencode-ai` 1.19.3, as read in
  [opencode-server.md](opencode-server.md); Pi
  `@mariozechner/pi-coding-agent` 0.73.1 or
  `@earendil-works/pi-coding-agent` 1.x (O6). Run prep installs that
  version with npm, which checks each package's registry
  `dist.integrity`, and records them in `harness.integrity` by package
  name (OpenCode: `opencode-ai` and the platform package whose binary
  its `postinstall` copies). `harness.treeSha256` is the SHA-256 of a
  compiled harness binary, as OpenCode's, else of the sorted
  `<path> <sha256>` lines of every regular file in the installed
  package folder, `node_modules/` included; [Start](#start) checks it,
  since an installed package keeps no tarball. Another machine of the
  same platform finds the same hash; another platform is a re-pin that
  the restore summary shows.
- `harness.providers` (OpenCode only): the `provider` entries that the
  model slots name, copied by Run prep from the operator's resolved
  OpenCode config, without `options`, which are machine-local
  (`machine.json` `harness.providerOptions`). Run prep refuses an entry
  whose `options` hold `apiKey` or any header value; credentials stay in OpenCode's own
  store (Model credentials in [Trust boundaries](#trust-boundaries)).
  It also refuses an entry whose `npm` package is not one the pinned
  binary bundles, so no provider package is downloaded at run time.
  Each model's `limit.context` equals the slot's `contextWindow`.
  Compaction reads `limit.input` in place of `limit.context` when the
  entry sets it ([note](opencode-server.md#worker-plugin-hooks)), so a
  set `limit.input` must not exceed `contextWindow`.
- `models.<slot>.model` is the harness `--model` value,
  `provider/model` for both harnesses. A slot with
  `"paid": true` requires `spending` = `{"askId": "prep-1",
  "approvedAt": "<UTC>", "text": "<the operator's words>"}`.
- `env.scrubExtra`: variable names added to the fixed denylist in
  [Environment scrub](#environment-scrub). It can only add names.
- `harness.plugin`: the installed sdlc plugin package and its version,
  which must equal `packages/<name>/package.json` at the pinned commit
  (R5; Start step 2; a repin to a commit with another version waits
  for the operator to install it).
- At the first `/sdlc`, and whenever either hash changes, the plugin shows
  a summary of `run.json` and `machine.json` (bundle remote, tag, and
  commit, repo, tracker, durability level, harness and plugin pins and
  paths, OpenCode providers, models, spending, labels, `env.scrubExtra`,
  backup folder) and
  records the operator's yes as `runJsonSha256` and `machineJsonSha256`
  in `driver.json`. No yes, no run. The summary shows `bundle.remote`
  and `bundle.trunk` and never asks for them: the operator typed the
  remote at Run prep, and neither can change
  ([Toolbox copy](#toolbox-copy)). It runs the toolbox check first, so
  its ancestry result is on a trunk fetched for this summary.
- **Bundle commit outside reviewed history (S9, N2, N4).** The driver
  uses one reviewed ref in the [toolbox copy](#toolbox-copy):
  `refs/heads/<bundle.trunk>` at the confirmed remote, as fetched by the
  latest toolbox check; the remote's `HEAD` is never read. A
  commit only on the toolbox's own project-main takes the typed-SHA
  path. A missing trunk ref stops the start, naming it, and is never
  "not an ancestor". The summary shows the full 40-hex commit and its
  `merge-base --is-ancestor <commit> refs/heads/<trunk>` result. On a
  commit that is not an ancestor, it also shows the SHA-256 of every file under the
  bundle's `scripts/` and `personas/` at that commit and each script's
  intake record; a script whose record and hash are not in
  `docs/INTAKE.md` at the derived ref first fails the bundle check
  (`bundle.script-intake`, [Script records](#bundle-layout-and-bundlemd)).
  The confirmation is then `ctx.ui.input`: the answer must equal the
  full SHA, else no run; the yes records the pin in `bundle.history`
  with `typed: true`. A restore takes this path for any pin other
  than the genesis commit's ([Durable run state](#durable-run-state)).

#### `machine.json`

Machine-local settings, mode `0600`, never mirrored. Run prep writes it,
and writes a new one at a restore on another machine.

```json
{"schemaVersion": 1,
 "hostId": "<32-hex, random per run root and machine>",
 "harness": {"bin": "/abs/path/to/opencode", "node": "/abs/path/to/node",
             "providerOptions": {"local": {"baseURL": "<local model endpoint>"}}},
 "backup": {"dir": null},
 "gather": {"sessions": ["gatherer/run-1/session.jsonl"]},
 "createdAt": "<UTC>"}
```

- `harness.bin`: the `opencode` or `pi` executable. `harness.node`: the
  Node binary for the detached driver; required for OpenCode, whose TUI
  runs on its own compiled runtime, and for Pi's compiled binary;
  optional for Pi on Node.
- `harness.providerOptions`: the `options` of each `run.json`
  `harness.providers` entry, with the same refusals; the worker config
  merges them.
- `backup.dir`: `null`, or an absolute folder outside every git
  worktree, not a symbolic link, mode `0700`, for the optional
  [session backup](#sessions-and-rehydrate).
- `hostId`: names this machine in the state branch's lease without a
  host name.
- `gather.sessions`: run-root-relative paths of the Gather session
  copies, local like the copies. A restored run has none, and the
  manager reads the brief alone.

#### `driver.json`

```json
{
  "schemaVersion": 1,
  "runJsonSha256": "<hex>",
  "machineJsonSha256": "<hex>",
  "bundleRemote": "git@github.com:OWNER/agentic-toolbox.git",
  "toolbox": {"config": "<sha256>", "head": "<sha256>"},
  "bundle": {"commit": "<40-hex>", "trunkTip": "<40-hex>", "checkedAt": "<UTC>",
             "history": [{"from": null, "to": "<40-hex>", "tag": "v0.9.0", "typed": false, "at": "<UTC>"},
                         {"from": "<40-hex>", "to": "<40-hex>", "tag": "v0.9.1", "typed": false, "at": "<UTC>"}]},
  "repinPending": null,
  "worker": {"extension": "driver/worker-ext/sdlc-worker-1a2b3c4d5e6f.ts",
             "sha256": "<hex>", "harnessVersion": "1.19.3"},
  "compiled": {"architect": "<sha256>", "builder-der-a530": "<sha256>"},
  "chunk": {"node": "spec", "state": "active", "stop": null, "askId": null,
            "pendingRoute": null, "unposted": null, "reentry": null,
            "land": null, "landReentry": false, "repairs": 0, "sentBack": false,
            "fixPending": false, "lastPushed": null, "reviewBase": null},
  "env": {"lld": "maintainers/design/solo-dlc/lld.md", "specCommit": "<sha>",
          "commandsSha256": "<hex>", "pass": 1, "branch": "env/solo-dlc-1",
          "landCommit": null, "baseline": null, "test": null},
  "groom": {"path": "maintainers/design/solo-dlc/groom.md", "recordCommit": "<sha>",
            "reviewedCommit": "<sha>", "frozenCommit": "<sha>", "commandsSha256": "<hex>"},
  "items": {
    "der-a530": {"state": "active", "node": "verify", "land": null, "landReentry": false,
                 "repairs": 1, "sentBack": true, "fixPending": false,
                 "lastPushed": "<sha>", "reviewBase": "<sha>",
                 "stop": null, "askId": null}
  },
  "sessions": {"builder-der-a530": {"path": "builder-der-a530/opencode.db", "id": "ses_<id>",
               "state": "live", "packed": ["tdd", "yagni", "debug"], "compiled": "<sha256>",
               "rehydratePending": false, "backup": null}},
  "runs": {"builder-der-a530": 5, "prove-der-a530": 4},
  "unmirrored": ["builder-der-a530/run-3"],
  "inFlight": null,
  "projectMainSeen": "<sha>",
  "lands": ["<sha>"],
  "nextAsk": 4,
  "updatedAt": "<UTC>"
}
```

| Field | Values and meaning |
| --- | --- |
| `chunk.state`, `items.*.state` | `pending` (not started), `active`, `waiting` (an ask is open: `askId`), `deferred` (the manager deferred it; retried at the next `/sdlc`), `done` |
| `chunk.node`, `items.*.node` | Current node id, or `@items` / `@done` |
| `chunk.pendingRoute` | `null`, or `{"node", "choice", "run", "record", "commit"}` from the end of an HLD or Spec stage whose design record was committed until its paperwork stage returns `posted`: the node and `choice` to route, the node's run, the record path, and the pushed commit ([Design-record commits](#design-record-commits) step 7) |
| `chunk.unposted` | `null`, or `{"node", "record", "commit"}`: a design record an interrupted HLD or Spec run pushed before its stage ended ([Start](#start) step 5). Cleared when [Stage pipeline](#stage-pipeline) step 11 sets `chunk.pendingRoute` |
| `items.*.land`, `chunk.land` | `null` outside the land node, else `{"phase", "p1", "p2", "cleanTree", "cleanCommit", "landCommit"}`; `phase` is one of the [Land](#land-sub-machine) rows. `chunk.land` is the env land |
| `items.*.landReentry`, `chunk.landReentry` | `true` from L3b or L6r until the scope next enters the land node at L1; selects the console label ([Land](#land-sub-machine)) |
| `repairs`, `sentBack`, `fixPending` | [Repair counter](#repair-counter), per item and, for env-prep, on `chunk` |
| `lastPushed` | Item or env branch tip the driver last pushed |
| `chunk.reentry` | `null`, or `{"from", "node", "askId"}` while an env re-entry runs: the stopped item, `env-prep` or `spec`, and the ask ([Build-environment gate](#build-environment-gate)) |
| `env` | The accepted env block: the LLD path, the `specCommit` that the `spec` gate accepted, `commandsSha256`, the env pass number and branch, the env land commit, the baseline `{"run", "status"}` (`green` or `known`), and the accepted `test` line |
| `unmirrored` | Run folders whose worker-written files the state branch never gets: a failed post-stage check or an interrupted run ([Persist](#durable-run-state) step 2). Rehydrate and a restore use the latest mirrored `state.md` |
| `compiled` | SHA-256 of each persona's current [compiled file](#compiled-files) |
| `repinPending` | `null`, or `{"old", "new", "tag", "typed", "compiled", "runJsonSha256"}` while a [repin](#repin-the-toolbox) writes `run.json`: the new pin, whether its SHA was typed, the new compiled hashes, and the new `run.json` hash; the next Start finishes or clears it from these alone |
| `bundleRemote` | The toolbox remote the operator typed at Run prep, written by `toolbox`; fixed for the run |
| `toolbox` | `{"config", "head"}`: the SHA-256 of the [toolbox copy](#toolbox-copy)'s `config` and of its `HEAD`, written only by `toolbox` |
| `bundle.trunkTip` | The trunk tip the latest [toolbox check](#toolbox-copy) fetched |
| `bundle.history` | The first pin (`from` `null`, at the first `/sdlc` summary) and every [repin](#repin-the-toolbox), oldest first, with the tag or `null`; `typed` is `true` when the operator typed the full SHA back |
| `reviewBase` | Item `HEAD` at the last Review pass, or the clean merge commit after a row-1 classification |
| `stop` | `{"kind", "run", "operatorOnly", "resumeWith"}` while the manager handles a stop. `resumeWith` is `{"persona", "prompt", "log"}`: who the driver resumes, and with which prompt kind, when the answer is `resume` |
| `sessions.*.state` | `live`, `lost` (stopped; ask open), `rehydrated` (a fresh session from the compiled file, `state.md`, and facts), `replaced` (minted again on the operator's answer; the old file is kept with `.lost-<UTC>` appended to its name; OpenCode: the database and its `-wal` and `-shm` files) |
| `sessions.*.packed` | Skill ids already in that session's transcript: the compiled file's skills at the mint or rehydrate, plus every skill packed since |
| `sessions.*.compiled` | The compiled file hash the session last received; a different `compiled` entry sends the changed parts at the next prompt ([Compiled files](#compiled-files)) |
| `sessions.*.rehydratePending` | `true` from a rehydrate until that persona's next valid result |
| `sessions.*.backup` | `null`, or `{"sha256", "at"}` of the last [session backup](#sessions-and-rehydrate) |
| `sessions.*.path`, `sessions.*.id` | The persona's session file: the OpenCode database or the Pi `session.jsonl`. `id`: the OpenCode session id the adapter read at the mint; `null` for Pi, whose file is the session |
| `groom.recordCommit` | The last `groom.md` commit the driver pushed ([Design-record commits](#design-record-commits) step 6) |
| `inFlight` | `{"run", "scope", "node", "kind", "prompt", "repairOf", "invalidRepairs", "recordCommit", "pid", "startedAt"}` while a stage runs. `kind` is `model` or `command`. `invalidRepairs` is `1` on an invalid-result repair stage, else `0`; `repairOf` names the run it repairs. `recordCommit` is `null` until [Design-record commits](#design-record-commits) step 5 sets it, before each push, to the commit that push sends; it is the only value the [pushed record exception](#start) trusts |
| `projectMainSeen` | The project-main tip the driver last fetched outside a worker stage or last pushed ([Post-stage checks](#post-stage-checks)) |
| `lands` | Every land merge commit the driver pushed (L8), kept after the item is done |

#### `index.jsonl`

One JSON object per line, appended with `O_APPEND`, at most 4 KiB:

```json
{"v": 1, "seq": 41, "at": "2026-10-18T09:12:03Z", "event": "end", "scope": "der-a530",
 "node": "verify", "step": "Build", "persona": "verifier-der-a530",
 "run": "verifier-der-a530/run-3", "session": "resumed", "status": "pass",
 "choice": "review", "artifact": "verifier-der-a530/run-3/result.md"}
```

`event` is `start`, `end`, `stop`, `ask`, `answer`, `push`, `land`,
`interrupted`, `found`, `rehydrate`, `restore`, or `repin`. Resume never reads this file; it is history
for people ([ux.md](ux.md) Q3). If the operator rejects Q3, the driver
writes no `index.jsonl` and nothing else changes.

#### `plan/items.json`

```json
{"schemaVersion": 1,
 "groom": {"path": "maintainers/design/solo-dlc/groom.md", "reviewedCommit": "<sha>",
           "frozenCommit": "<sha>", "commandsSha256": "<hex>"},
 "items": [{"g": "G1", "ticket": "der-a530", "suffix": "der-a530", "slug": "result-format",
            "branch": "item/der-a530-result-format", "blockedBy": [],
            "skills": ["lang-js-ts"], "prove": ["npm --prefix packages/sdlc-driver test"],
            "proveSha256": "<hex>"}]}
```

Array order is plan order (G-number order). `blockedBy` holds ticket ids.
This file is a snapshot for people and for dispatch order; the driver
never reads proving commands from it.

#### `asks/`

`ask-N.json`:

```json
{"id": "ask-4", "kind": "operator-stop", "scope": "der-a532", "node": "build",
 "stopKind": "repair budget exhausted", "stoppedRun": "builder-der-a532/run-9",
 "managerRun": "manager/run-6", "choices": [], "openedAt": "<UTC>",
 "message": "<ask-human.md text, verbatim>",
 "answer": null}
```

`kind` is `gate` (choices = the gate's exit names), `lost-session`
(choices `replace`, `defer`), `scan-hit` (choices `allow`, `revise`),
`scan-secret` (choices `revise`, `defer`; never `allow`), `pi-dir` or
`opencode-dir` (choices `allow`, `defer`), `env-capability` (choices
`env`, `spec`, `deny`, `defer`), `state-scan` (choices `allow`,
`exclude`, `defer`), `state-secret` (choices `exclude`, `defer`; never
`allow`; neither offers `exclude` for `run.json`, `driver.json`, or
`plan/items.json`), `state-push` (choices `retry`, `local`, `defer`), or
`operator-stop` (free text). An answer is
`{"choice": "<one of choices or null>", "text": "<verbatim>", "at": "<UTC>"}`.
`ask-N.md` renders the same fields with the message and the answer
verbatim. Answers are recorded only by the plugin's `/sdlc` handler, in
the operator's interactive session, while no driver holds the lock
([OpenCode host shape](#opencode-host-shape-and-sdlc),
[Pi host shape](#pi-host-shape-and-sdlc)).

#### Run folder

**D** marks the files the state branch mirrors
([Durable run state](#durable-run-state)); the others stay local.

| File | Writer | Notes |
| --- | --- | --- |
| `meta.json` | driver | Local. Node, scope, persona, `new` or `resumed`, prompt kind, `repairOf`, start and end times, the worker argv; `recordCommit`, a copy for people of `inFlight.recordCommit` ([Design-record commits](#design-record-commits) step 5). A worker can write this file through `bash`, so no driver step reads `recordCommit` from it |
| `prompt.md` | driver | Local. The prompt sent on stdin |
| `candidate.json` | worker | Local. Through `sdlc_result` or `sdlc_write` |
| `result.json` | driver | D. The validated result, or a driver-authored one |
| `result.md` | worker | D. Prose; paths relative to the run root or the repo, never absolute (the run contract says so) |
| `state.md` | worker | D. Copied by the driver from the persona's previous run, or from the template, before the run starts |
| `ledger.json`, `baseline.json` | verifier | D. [Verifier ledger](#sdlc-personas-and-prompts) |
| `ask-human.md` | manager | D. On `escalate` |
| `out/` | worker | D. Files for the repo, at their repo-relative paths |
| `commands.json`, `env-evidence.json` | driver | D. Command stages: one entry per command: index, line, exit code, duration, log path (local; absent after a restore). `env-evidence.json` (env command stages): each toolchain line with its output after each `passEnv` value is replaced by `<passEnv NAME>`, then cut to the first 200 characters, each dependency step, and the baseline status |
| `check.json` | driver | D. Command stages only: the post-stage check that failed, when one did |
| `<extract>.md` | driver | D. Gate results only: the section an exit's `extract` copied, such as `trial-kickoff.md` |
| `logs/` | driver, extension | Local. `worker.jsonl` (the harness's JSON stream: `opencode run --format json` or Pi's `--mode json`), `worker.stderr`, `ext.json` (extension or worker-plugin load marker; missing → `check failed: extension`), `prove-K.log` |
| `interrupted.json` | driver | D. Present when the run was interrupted; such a folder never gets `result.json`, is never reused, and is listed in `unmirrored`. Holds `recordCommit`, for people, when the pushed record exception's pushed case applied ([Start](#start) step 5) |

#### Driver facts

The driver writes the facts as text, at most 16 KiB, passes them to the
worker in `SDLC_FACTS` with their SHA-256 in `SDLC_FACTS_SHA256`, and
keeps the same text in `driver/facts/<persona>--run-N.md`:

```text
Driver facts for builder-der-a530/run-5 (der-a530, Build). Written by the driver.
- Repair: 2/3
- Open verifier issues:
  - V2 critical: retry stops after the first attempt
  - V4 breaking: CLI exits 0 on a missing run root
- Failing logs:
  - prove-der-a530/run-4/logs/prove-2.log
```

- Issues come from the item verifier's latest `ledger.json`: entries
  with status `open` and criticality above `nit`, at most 30.
- The driver removes control characters, joins whitespace, and cuts each
  summary to 200 characters.
- Logs are paths relative to the run root, never log text.
- Personas other than the builder get the first line only.

#### Labels

Labels match `^[a-z0-9][a-z0-9-]{0,31}$`. An item persona's label and
folder are `<persona-id>-<suffix>`; the longest SDLC persona id is
`reviewer` and `verifier`, so the suffix may be at most 23 characters.

`run.json` `labels.mode` decides the suffix:

| Mode | Suffix |
| --- | --- |
| `plain` | The ticket id lowercased. Valid only if it matches `^[a-z0-9][a-z0-9-]{0,22}$` |
| `short` | The ticket id lowercased, every character outside `[a-z0-9-]` replaced with `-`, cut to 12 characters, then `-` and the first 8 hex digits of the SHA-256 of the ticket id: at most 21 characters |

1. **Run prep** reads the tracker's key pattern and the longest id it
   allows. `local` ids (`<prefix>-xxxx`, at most 11 characters) fit
   `plain`. A pattern that allows ids longer than 23
   characters, or characters outside `[A-Za-z0-9-]`, sets `short`, and
   Run prep says so on the checklist.
2. **Driver**, when it writes `plan/items.json`, computes each suffix.
   In `plain` mode, an id that does not fit is a `fail`, `operator`
   stop that asks to switch to `short`; no item persona exists yet, so
   the switch is safe. In `short` mode, two items with the same suffix
   extend both hashes to 12 hex digits.
3. The suffix never changes after an item persona exists. Comments
   still carry the full ticket id.

#### Durable run state

`run.json` `state.level`. This table and the public-repo rule are the
one definition; the HLD, UX, and stories link here.

| Level | Where the **D** files live | Survives | Drill source |
| --- | --- | --- | --- |
| `pushed` (default) | The state branch, committed in `worktrees/state/`, pushed to `origin` at every persist | Loss of the machine | `origin` |
| `local` | The state branch in `repo.git`, never pushed | A damaged run-root file | `repo.git` |
| `plain` | The run root only | Crashes on this machine | None (`n/a`) |

**Public repo.** The state branch is then public (brief, prose,
`state.md`, verbatim answers). Run prep says so before the first push
and offers the three levels with no default, a deliberate departure
from decision B's default ([O12](#questions-for-the-operator)).

**State branch** `sdlc/run/<chunk-slug>`: orphan, never merged, never
named by the land path, never deleted by the driver; at `@done` the
console names it as the operator's ([O15](#questions-for-the-operator)).
Its tree is the **D** files at their run-root paths plus
`sdlc-state.json`: `schemaVersion`, `seq`, `prev`, `level`, `event`,
`run`, `pin` (`{"commit", "trunkTip", "typed"}` from `driver.json`
`bundle`), `lease` (`{"holder", "since"}`, `pushed` only), `files`
(the hash ledger: SHA-256 of every other file), `excluded`
(`[{"path", "askId"}]`), `skipped` (`[{"path", "bytes", "sha256"}]`).
The tip record `driver/state.json` (`seq`, `tip`, `genesis`,
`pushedTip`, `restore`) is a local [driver file](#driver-file-ledger),
never mirrored, since a commit cannot hold its own hash; `state-init`,
restore, and drill set it from the branch `HEAD`.

**Persist** at: `state-init`; the end of Gather (`sdlc-driver persist`);
each stage start, after pipeline step 4 sets `inFlight`, before the
snapshot; each stage end on every finish path, after the end line and
the session backup; each driver push to project-main outside a stage
(L8); Start step 7. Holding the lock, in `worktrees/state/`:

1. `HEAD` equals `tip` and the worktree is clean; else
   `check failed: state`, an `operator` stop. One exception, a kill
   between step 4's commit and its tip-record write: when the worktree
   is clean, `HEAD`'s only parent is `tip`, its `sdlc-state.json` has
   `prev` equal to `tip` and `seq` one above the record's, and its
   ledger matches its tree, the driver adopts `HEAD` as `tip` (and `seq`)
   and goes on.
2. Copy each **D** file whose hash differs from the tip's ledger; never
   delete one. A run folder's worker-written files (`result.md`,
   `state.md`, `ledger.json`, `baseline.json`, `ask-human.md`, `out/`)
   only once it has `result.json` and is not in `driver.json`
   `unmirrored`. A file over 256 KiB or not NUL-free UTF-8 goes to
   `skipped`. The tip's `excluded` and `skipped` lists carry over: an
   `excluded` path is never copied or scanned again; a `skipped` path is
   checked again only when its SHA-256 differs from its entry, then
   copied if it now fits, else its entry updated. An entry whose path no
   longer exists is dropped. Neither list is compared with the ledger,
   so an unchanged listed file never makes a persist.
3. [Scan](#scan-patterns) each copied file, every class and the
   `passEnv` values, with the run root and every `machine.json` path as
   `path` patterns. A hit: no commit, a driver-written ask naming
   `<file>:<line> <class>`, and no stage until the answer. Credential:
   `state scan hit: credential`, ask `state-secret` (`exclude`, `defer`).
   Other: `state scan hit`, ask `state-scan` (`allow`, `exclude`,
   `defer`). `exclude` keeps the path local and lists it; it is never
   offered for `run.json`, `driver.json`, or `plan/items.json`.
4. Write `sdlc-state.json` (`seq` + 1, `prev`, ledger); commit, hooks
   off, as `sdlc-driver <sdlc-driver@sdlc.invalid>`, message
   `[<epic>] state <seq>: <event> <run>`; write the tip record.
5. `pushed`: push without force; exit `0` sets `pushedTip`. Else fetch:
   a tip other than `pushedTip` is `state lease lost` (exit; only a
   restore continues); otherwise `state push failed`, ask `state-push`
   (`retry`, `local`, `defer`; `local` is a confirmed `run.json` change).

**Lease.** `lease.holder` is `machine.json` `hostId`. Every
[Start](#start) fetches the branch: tip = `pushedTip` with this holder
goes on; a local tip ahead is pushed first; anything else is
`state lease lost`; a failed fetch is `state lease unknown`, ask
`state-push`, never a skipped check. Only a restore moves the lease.

**Restore.** The [`restore` mode](#item-0-sdlc-kickoff-run-prep-gather-restore)
writes a new `machine.json`, then
`sdlc-driver restore RUN_ROOT [--from <url or path>]` (default `origin`):

1. `RUN_ROOT` absent or empty, created `0700`; `repo.git` and
   `worktrees/integrate/` as at a first Start; fetch; `worktrees/state/`
   at the branch tip.
2. Walk `prev` to the first commit: each `sdlc-state.json` passes the
   strict reader, the ledger matches the tree exactly, `seq` falls by
   one. A failure refuses, naming commit and path. Commits by another
   identity than the driver's are listed: the identity is forgeable.
3. **Named commits.** Each set `groom.reviewedCommit`,
   `groom.frozenCommit`, `groom.recordCommit`, `env.specCommit`,
   `env.landCommit`, `chunk.pendingRoute.commit`,
   `chunk.unposted.commit`, `lands` entry, and `projectMainSeen` is an
   ancestor of the fetched `origin/<projectMain>`; else
   `check failed: state-commits`, naming the field. `inFlight.recordCommit` is exempt: in the not-pushed case it is
   on no ref, and the [pushed record exception](#start) accepts it only
   as project-main's or `worktrees/integrate`'s exact tip. Item and env
   branch tips (`lastPushed`, `reviewBase`, `env.branch`) are outside the
   test: anyone with branch push can move them, and Start step 3 checks
   each remote tip equals `lastPushed`. [Start](#start) step 3 repeats
   this test after its fetch.
4. Copy the files in, create the driver ledger, write the tip record
   with `restore: {"tip", "confirmed": false}`.
The first `/sdlc` first asks, from the [genesis note](#toolbox-copy)
kept off this machine, the first 12 hex digits of the genesis commit,
the full toolbox remote, and the trunk. The typed remote must pass the
remote rule and equal the restored `run.json` `bundle.remote` and
`driver.json` `bundleRemote`, and the trunk `bundle.trunk`. Only then it
runs `toolbox --remote <typed>`, so no network call goes to
a remote the operator has not typed: the copy is cloned at the restored
pin, and each compiled file's SHA-256 must equal the restored
`driver.json` `compiled`; else `check failed: toolbox` or `compiled`.

It then shows the restore summary: tip, `seq`, genesis
commit, last event, `inFlight`, lease, the listed commits, each named
commit with subject, author, and ancestry, the full
[`run.json` summary](#runjson) under its reviewed-refs and typed-SHA
rules, `bundle.tag` and the pin with the trunk ref's ancestry in the
new copy, the genesis commit's own pin, and
a diff stat, from objects read as in [Reads](#toolbox-copy), from that
pin to the restored one over
`bundles/<id>`, `skills/`, and `docs/INTAKE.md`, the harness and plugin pins with this
machine's tree hash, the `excluded` and `skipped` paths, and
every remote ref that differs from `projectMainSeen`, `lastPushed`, or
`lands`. The operator then types the first 12 hex digits of the tip
([O20](#questions-for-the-operator), [O22](#questions-for-the-operator)).
A pin other than the genesis commit's needs its full SHA typed back, as
for a commit outside reviewed history, whatever its ancestry: the
genesis is anchored by the note, a later pin only by the state branch.
Anything else, no run.
Only then the driver records `runJsonSha256` and `machineJsonSha256`,
writes `interrupted.json` with `"restored": true` for an in-flight run
(the typed confirmation stands in for Start step 5's checks), persists
as lease holder, and starts. Local files that mirrored ones name (Gather
copies, logs) and the `excluded` and `skipped` paths are absent after a
restore; readers treat them so, and the next persist drops their
entries ([Persist](#durable-run-state) step 2).

**Drill.** Run prep's last step at `pushed` and `local`:
`sdlc-driver drill RUN_ROOT` restores the branch from its drill source
into a temporary `0700` folder `<tmp>` with no lease and no push, and a
copy of `machine.json` with `hostId` new and `backup.dir` `null`; the
driver refuses any drill write outside `<tmp>`. It runs
`toolbox --remote` there with the remote the operator typed at Run prep
(`driver.json` `bundleRemote`, never a model's text), then the toolbox
check, and fails when the temporary copy's `config` or `HEAD` SHA-256
differs from the source `driver.json` `toolbox`. It then compares
`sdlc-driver status` of both roots, ignoring the lease, the tip record's
`restore` and `pushedTip`, the run-root path, `bundle.trunkTip` and
`checkedAt`, and the `excluded` and `skipped` paths, which stay local by design; then
each file the tip's ledger lists, and each compiled hash with
`driver.json` `compiled`. Pass: `restore drill: done`; else the
line names the difference and Run prep prints no Gather line. The
folder is removed either way.

#### Compiled files

One file per persona, `compiled/<persona>.md`: local, a
[driver file](#driver-file-ledger), never committed or mirrored. The
driver compiles it from the [toolbox copy](#toolbox-copy) at the pin and
the `run.json` repo facts: the chunk personas' files at `state-init`,
each item persona's when it writes `plan/items.json`, and every file
again after a [repin](#repin-the-toolbox) and after the env land. Each
write is a temporary file, `fsync`, and `rename`, and only these writes
change `driver.json` `compiled`.

```text
<!-- sdlc-compiled pin=<40-hex> sources=<sha256> -->
# Compiled: <persona> (<job>, <scope>), bundle <id>@<sha12>
## Role
<the persona's ## Role>
## Repo facts
- Repo <origin>; trunk <trunk>; project-main <projectMain>; design folder <designDir>
- Tracker <backend>; Epic <epic>; key pattern <keyPattern>[; ticket <ticket>; branch <branch>]
- Test command: <env.test, else repo.test, else "none yet; env-prep sets it">
- Environment: <after the env land: each dependency and the env block's prove lines; else "not built yet">
## Packed skill <id> — do not reload
<the skill body at the pinned commit>
```

- It packs the persona's front-matter `skills` and, for an item
  builder, the item's `groom.md` `skills`. What changes per stage (the
  repo tracker skill, packed per prompt from project-main; node skills;
  `test-failure-handler`; the run folder; the facts) stays in the prompt
  kinds and the run contract.
- `sources` is the SHA-256 of the sorted `<path> <sha256>` lines of the
  persona file and each packed skill file at the pin, plus one line
  for the repo-facts block. The file holds no absolute path, so it
  compiles the same on every machine; `driver.json` `compiled` keeps
  each file's SHA-256, so the state branch records the pin and the
  hashes, never the file.
- At [Start](#start) step 3, a missing file that has a `compiled`
  entry, or one whose `pin` or `sources` differs from the values the
  copy gives now, is compiled again, and the result must equal its
  `compiled` entry. Any other difference, or a file with no entry, is
  `check failed: compiled`, an `operator` stop; an edited file fails
  the ledger check first, which passes only a missing one. A file is a pure
  function of the pin and `run.json`, so a kill during any compile
  leaves nothing to finish: the next Start compiles again.
- Only a mint's `prompt.md` names the file, in its first line, by
  absolute path:
  `Read RUN_ROOT/compiled/<persona>.md first: your role, packed skills, and repo facts.`
  `sessions.*.packed` starts as the file's skill ids
  and `sessions.*.compiled` as its hash. When the persona's `compiled`
  entry later differs, the next prompt carries a `# Compiled update`
  block: the changed repo facts, and each changed skill under
  `# Packed skill <id> — replaces the earlier copy`.
- A [rehydrate](#sessions-and-rehydrate) starts from the current file:
  `packed` restarts as its skill ids and `sessions.*.compiled` as its
  hash, so no update block follows. A recompile with an unchanged hash,
  as after a restore, changes no session.
- A resumed session, one restored from backup on another machine
  included, never reads the file again: its transcript already holds
  the contents, and changes reach it as `# Compiled update` blocks.
- The worker reads the file through its read tool. It is in the run
  root, which OpenCode's `external_directory` allow list already names;
  every persona can read every compiled file, which holds only
  read-only facts and skill text, and the path guard refuses writes
  there, as everywhere outside the writable set.

### Behavior 5: core driver (item 5)

#### Adapter interface

The core knows no harness. A plugin passes a `HarnessAdapter`:

```ts
interface HarnessAdapter {
  name: string;                                   // "opencode", "pi", "test"
  checkVersion(pinned: string): Promise<string>;  // returns the actual version
  installWorkerExtension(runRoot: string): Promise<{path: string; sha256: string}>;
  sessionLooksValid(session: SessionRef, cwd: string): Promise<boolean>;
  missingModels(models: string[]): Promise<string[]>; // no model call: OpenCode `models`, Pi `--list-models`
  preflight(spec: WorkerSpec): Promise<Preflight>; // before each spawn; no model call
  runWorker(spec: WorkerSpec, signal: AbortSignal): Promise<WorkerExit>;
  ui: {line(text: string): void; notify(kind: "stop" | "ask" | "done", text: string): void};
}
interface SessionRef { path: string; id: string | null }  // id: OpenCode session id; null for Pi
interface WorkerSpec {
  persona: string; job: string; mint: boolean; session: SessionRef;
  runDir: string; promptPath: string; cwd: string; tools: string[];
  model: string; env: Record<string, string>; timeoutSec: number; logDir: string;
}
interface WorkerExit {
  exitCode: number | null; signal: string | null; timedOut: boolean;
  modelError: string | null;   // OpenCode: exit 1 or an `error` line; Pi: stopReason error/aborted
  sessionId: string | null;    // OpenCode: the id from the first stream line; Pi: null
  sessionMissing: boolean;     // OpenCode: `Session not found` on a resume
}
type Preflight =
  | {ok: true}
  | {stop: "harness-dir"; askKind: "pi-dir" | "opencode-dir"; path: string; treeHash: string}
  | {check: "harness-config"; detail: string};
```

`preflight` returns `harness-dir` for a folder the adapter refuses
until the operator allows it (Pi: `.pi/` in the cwd; OpenCode:
`~/.opencode/` or `/etc/opencode/`), and `harness-config` when the
harness would load configuration the driver did not write. The
[stage pipeline](#stage-pipeline) step 5 turns them into stops.
`sessionMissing` makes the stage a `session lost` stop, like a present
but invalid file at pipeline step 2.

The core API is `prepare(runRoot, adapter)` (lock check, validation,
the found report, pending asks) and `run(runRoot, adapter)` (the loop).
Recording an answer is `recordAnswer(runRoot, askId, choice, text)`;
it refuses while any driver holds the lock.

#### Start

1. Take `driver/lock`: create it with `O_EXCL`, holding
   `{"pid", "procStart", "startedAt"}`. If it exists and its pid is
   alive with the same process start time, exit with
   `another driver holds RUN_ROOT (pid N)`. Otherwise it is stale: print
   one line and take it. Taking a stale lock replaces its
   [ledger](#driver-file-ledger) entry without comparing it first.
2. Run the ledger check ([Driver-file ledger](#driver-file-ledger)
   point 6) before reading `driver.json`; a mismatch stops the start.
   Run the [toolbox check](#toolbox-copy)'s steps 1 and 2, which read
   files only. Finish a pending [repin](#repin-the-toolbox) from
   `driver.json` and `run.json` alone. Validate `run.json`; check
   `runJsonSha256`. Refuse a
   `tracker.backend` other than `local` with the line in
   [`run.json`](#runjson). Check the harness version equals
   `harness.version` and the installed tree's hash equals
   `harness.treeSha256`, hashing every file in full, and the installed
   plugin's version equals `harness.plugin`; else stop and print both
   values of each. A stat cache of the tree (path, inode, size, `mtime`,
   `ctime`, SHA-256), `driver/harness-tree.json`, a driver file written
   only here, lets the [stage pipeline](#stage-pipeline) re-check the
   hash before each spawn: it walks the whole tree, hashes each added or
   stat-changed file, counts removed ones, and reuses a cached hash only
   when path and stat match.

   Then the start preflight, the cheap subset of Run prep's
   [readiness checks](#behavior-8-run-prep-and-later-items-0-4-8), with
   no model call and no push: check `machineJsonSha256`; refuse a run
   root that is a symbolic link or grants group or other permission; git
   is 2.32 or newer; the [toolbox check](#toolbox-copy)'s steps 3–5
   pass: the trunk fetch, the pin on it or typed, and the hash-checked
   reads (a start never clones; the operator runs `sdlc-driver toolbox
   RUN_ROOT --remote <typed> --rebuild`); `adapter.missingModels` is empty for every model slot; a set
   `backup.dir` passes its `machine.json` rules, else one warning line;
   `gatherer/run-1/brief.md` exists, else the line
   `no brief yet: finish Gather first` and no run; one warning line per `passEnv` variable whose value is
   shorter than 6 characters, which the scan cannot match. While the
   tip record's `restore.confirmed` is `false`, the start waits for the
   restore confirmation.
3. On the first start, before any fetch, when `repo.git` does not
   exist: `git init --bare --initial-branch=empty repo.git`; set
   `origin` from `run.json` with no force option and fetch refspec
   `+refs/heads/*:refs/remotes/origin/*`; then
   `git -C repo.git worktree add --orphan -b integrate-empty <RUN_ROOT>/worktrees/integrate`.
   The driver requires `git worktree add --orphan`. The bare clone and
   the integration worktree both exist before any fetch. Then, on every
   start including the first: fetch `repo.git`. On that first start
   only, `git -C worktrees/integrate switch --detach refs/remotes/origin/<projectMain>`.
   If `refs/heads/integrate-empty` still exists,
   `git -C repo.git update-ref -d refs/heads/integrate-empty`. Then
   compile each missing or stale [compiled file](#compiled-files) and
   check every one against `compiled`.

   Run prep's `state-init` runs this first-start part, because the
   state worktree needs `repo.git`. After the fetch, on every start: run
   the restore's named-commits test
   ([Durable run state](#durable-run-state) restore step 3) against the
   fetched `origin/<projectMain>`; at
   `pushed`, apply the [lease](#durable-run-state) rule to the fetched
   state branch; at `pushed` and `local`, check `worktrees/state/` as
   persist step 1 does. Recreate a missing item or env worktree at
   `lastPushed`, after checking that the remote branch tip equals it; a
   difference is an `operator` stop. Report each live session whose file is missing as
   `will restore from backup` or `will rehydrate`
   ([Sessions and rehydrate](#sessions-and-rehydrate)).
4. Install the worker extension; if its hash differs from
   `driver.json`, print one line and record the new hash.
5. If `inFlight` is set, the previous driver died mid-stage: write
   `interrupted.json` in that run folder, run the
   [post-stage checks](#post-stage-checks) for its stage kind against
   `driver/snapshot.json` and, for driver files, the ledger, clear
   `inFlight`, add the run folder to `unmirrored`, and append an
   `interrupted` event. A failed check is an `operator` stop. Otherwise
   the next run of that scope and node uses the interrupted record's
   `prompt`, `repairOf`, and `invalidRepairs`, so an interrupted repair
   is not granted a second repair. An interrupted paperwork stage is
   replayed from `chunk.pendingRoute`
   ([Design-record commits](#design-record-commits) step 7).

   **Pushed record exception.** An interrupted HLD or Spec stage (not
   its paperwork) may have committed, and pushed, its design record
   before it died. Let `C` be `inFlight.recordCommit` in `driver.json`,
   as read after step 2's ledger check passed
   ([Design-record commits](#design-record-commits) step 5), and `S`
   the snapshot's project-main tip. The exception never reads
   `meta.json` or any other file in the run folder: a worker can write
   those through `bash`, and the snapshot excludes them. When `C` is
   `null`, every check runs unchanged. When `C` is set, the `refs` and
   `worktrees` checks allow exactly one of two differences:

   - **Pushed.** `refs/heads/<projectMain>` now points at `C`,
     `git merge-base --is-ancestor S C` succeeds, and
     `worktrees/integrate` has `HEAD` equal to `C` and the same
     `git status --porcelain` as before. Write `recordCommit: C` into
     `interrupted.json`, and, in the `driver.json` write that clears
     `inFlight`, set `projectMainSeen` to `C` and `chunk.unposted` to
     the node, the record path, and `C`. The node then runs again;
     [Stage pipeline](#stage-pipeline) step 11 turns `chunk.unposted`
     into `chunk.pendingRoute` so that paperwork runs for `C`.
   - **Not pushed.** Every remote ref equals the snapshot, and
     `worktrees/integrate` has `HEAD` equal to `C` and the same
     `git status --porcelain` as before: the driver died after
     recording `C` and before its push reached the remote. `C` is on no
     ref. Set nothing else; the node runs again as after any
     interruption, and design-record step 1 detaches
     `worktrees/integrate` at the fetched tip, so the re-run commits
     its own record.

   Every other ref and every other worktree must still be equal, and
   every other check runs unchanged; any other difference is an
   `operator` stop, whatever any run folder holds.
6. Print the found report ([Console](#console-lines)); any `deferred`
   scope becomes `active`.
7. Persist when a **D** file differs from the tip's ledger (recorded
   answers, a repin, a restore), not counting the worker-written files
   of folders in `unmirrored`, `excluded` paths, or `skipped` paths
   whose SHA-256 equals their entry, which persist never copies; then
   enter the loop.

#### Repin the toolbox

`/sdlc-repin` is a plugin command, like `/sdlc`, and runs only while no
driver holds the lock: between stages, never inside one. It takes the
lock for its own run. OpenCode asks for the run root and the new tag or
commit in dialogs; Pi takes `/sdlc-repin RUN_ROOT TAG_OR_COMMIT`. It
moves only the commit; `bundle.remote` stays the confirmed one. Every
step reads the [toolbox copy](#toolbox-copy)'s object store; nothing is
checked out.

1. The [toolbox check](#toolbox-copy) passes at the old pin; its step
   3 fetches the trunk and tags, and `config` and `HEAD` keep their
   recorded hashes. Resolve the new tag or commit to a 40-hex commit `N`.
2. Read `flow.json`, the personas, the scripts, the packed skills, and
   `docs/INTAKE.md` at `N` with the object hash checks of
   [Reads](#toolbox-copy); run the bundle check on those bytes; refuse
   when a scope's current node is gone from the new flow, a persona
   with a session changes its job or scope, or the plugin version
   differs from `harness.plugin` (the operator installs it first).
   Compute every compiled file at `N` in memory.
3. Show `N` in full, the diff stat from `<old>` to `N` over
   `bundles/<id>`, `skills/`, and `docs/INTAKE.md`, and the full diff of
   `flow.json` and the personas, from the objects step 2 checked. The
   [reviewed-refs rule](#runjson) applies as for a new run, on the
   just-fetched trunk ref: a commit that is not an ancestor needs the
   full SHA typed back. The yes confirms exactly `N`.
   A failure, a refusal, or a no changes nothing but the fetched refs
   and objects.
4. On the yes, `core.repin`: write `driver.json` `repinPending` =
   `{"old", "new": N, "tag", "typed", "compiled", "runJsonSha256"}`,
   with step 2's compiled hashes and the hash of the new `run.json`;
   write `run.json` with the new `bundle.commit` and `bundle.tag`; in
   one `driver.json` write, record `runJsonSha256`, append
   `bundle.history`, set `compiled` from `repinPending`, and clear it;
   write the compiled files; append a `repin` event and persist. Each
   live session gets the changed parts at its next prompt.

**A kill** in step 4 leaves one of three cases. Start step 2 settles it
after the toolbox check's steps 1 and 2 and before it validates
`run.json`, reading only `driver.json` and `run.json`, so it runs no git
and reads no object:

- `repinPending` set and `run.json` `bundle.commit` is `old`: clear the
  marker; print `repin interrupted; still at <old7>`.
- `repinPending` set and `run.json` names `new` with the marker's
  `runJsonSha256`: do step 4's combined `driver.json` write from the
  marker.
- `repinPending` clear: nothing to finish; Start step 3 compiles each
  file whose `pin` differs from `bundle.commit`, and each must equal its
  `compiled` entry.

Any other `run.json` with the marker set is `check failed: toolbox`.
`repinPending` is the only repin marker: each `driver.json` write is
already atomic through the [ledger](#driver-file-ledger)'s two phases,
and `run.json` is not a driver file, so the ledger alone cannot tell
which pin `run.json` holds.

#### Loop

1. Pick the next runnable scope: the chunk, while its node is not
   `@items` or `@done` and its state is `active`; then items in plan
   order whose state is `pending` or `active` and whose `blockedBy`
   items are all `done`.
2. None runnable: print the summary (pending asks, deferred and waiting
   items), release the lock, and return.
3. An item that is `pending` becomes `active`: fetch, set
   `projectMainSeen` to the fetched tip, create its branch from that tip
   with `git worktree add -b <branch> worktrees/<suffix> <tip>`, push
   the branch without force, and set `lastPushed`.
4. Run the scope's current node ([Node routing](#node-routing)). For
   the chunk with `chunk.pendingRoute` set, run the architect's
   paperwork stage instead
   ([Design-record commits](#design-record-commits) step 7). The chunk
   at `env-prep` creates the env branch first
   ([Build-environment gate](#build-environment-gate) point 2).
5. After the stage finishes, by any path: back up the stage persona's
   session file when `backup.dir` is set
   ([Sessions and rehydrate](#sessions-and-rehydrate)), then persist
   ([Durable run state](#durable-run-state)) unless `state.level` is
   `plain`.
6. Repeat.

One stage runs at a time, model or command, across all scopes. A chunk
in an env re-entry is runnable before every item, so items wait for the
new environment.

#### Stage pipeline

Every stage runs these steps: model nodes, command nodes, land
sub-stages, paperwork, manager stages, and repairs. Steps marked
*(model)* run only for model stages; command stages skip them and the
worker-only checks.

1. **Run folder.** N = `runs[folder] + 1`. If `<folder>/run-N/` already
   exists and holds a `meta.json`, increment N again. An empty folder
   (Run prep's `refiner/run-1/`) is used as is.
2. *(model)* **Session.** If `sessions[persona]` exists, this is a
   resume: a present file must pass `adapter.sessionLooksValid`, else a
   `lost-session` stop; a missing file is restored from its backup or
   rehydrated ([Sessions and rehydrate](#sessions-and-rehydrate)). If
   it does not exist, this is a mint: the file must not exist, else an
   `operator` stop (`unexpected session file`).
3. **Files.** *(model)* Copy `state.md` from the persona's previous run,
   or the template; write `prompt.md` ([Prompts](#prompts)); write the
   facts file. Every stage: write `meta.json`.
4. **Snapshot.** Set `inFlight` (with `kind`, `prompt`, `repairOf`,
   `invalidRepairs`, and `recordCommit: null`), write `driver.json`,
   persist at `pushed` and `local` (the in-flight marker), then take the pre-stage
   snapshot that the [post-stage checks](#post-stage-checks) for this
   stage kind need, and write `driver/snapshot.json`.
5. **Run.** Print the start line, except a proving-command stage
   while `items.*.land` or `landReentry` is set, which prints none
   ([console mapping](#land-sub-machine)). Model: re-check
   `harness.treeSha256` from the stat cache ([Start](#start) step 2);
   a mismatch finishes the stage as a failed check
   (`check failed: harness`, step 6) without spawning. Then call
   `adapter.preflight`: `harness-config` finishes the stage the same
   way (`check failed: harness-config`) without spawning;
   `harness-dir` is an `operator` stop with its ask kind, unless
   `driver.json` records an `allow` for that path and tree hash. Then
   re-hash the persona's [compiled file](#compiled-files) against its
   `compiled` entry, mint or resume; a difference finishes the stage
   the same way (`check failed: compiled`) without
   spawning. Then call `adapter.runWorker`;
   after it returns, kill leftovers
   ([OpenCode adapter](#opencode-adapter-and-worker-command-line),
   [Pi adapter](#pi-adapter-and-worker-command-line)). Command: run
   the [command body](#command-body).
6. **Checks.** Run the post-stage checks for this stage kind, whatever
   the candidate or command result holds, `snapshot` first
   ([Driver-file ledger](#driver-file-ledger) point 5). The first failure finishes
   this stage and does not enter steps 7–11: on a model stage, write a
   driver-authored `fail` (`choice: operator`) naming the check and
   keep `candidate.json`; on a command stage, keep the wrapper result
   and write `check.json`. Then add the run folder to `unmirrored`,
   clear `inFlight`, append `end`, print
   the end line, and take an `operator` stop, kind
   `check failed: <check>`. No repair runs.
   A command stage whose checks pass clears `inFlight`, appends
   `end`, prints the end line unless the console mapping omits it, and
   routes by the command result's `choice`, unless
   `items.*.land` is set: then the
   [land sub-machine](#land-sub-machine) consumes the result and the
   flow route does not. It does not run steps 7–11. When the command
   result is `fail` and the checks passed, a proving-command stage
   with `items.*.land` or `landReentry` set prints the command-fail
   line instead of the end line.
7. *(model)* **Validate.** The candidate is invalid if it is missing,
   fails the strict reader, fails item 1 or the
   [candidate rules](#flowjson), `timedOut` is true, or `modelError` is
   set.
   - Valid: go to step 8.
   - Invalid and `inFlight.invalidRepairs` is `0`: write a
     driver-authored `fail` (`choice: stop`, findings: the error codes
     and messages) in this run folder, print
     `invalid result … repair 1/1`, clear `inFlight`, append `end`, and
     print the end line. Then start the repair: a new stage for the
     same persona, resumed, with the fixed `repair` prompt holding the
     errors, `invalidRepairs: 1`, and `repairOf` naming this run. A
     repair does not count toward the
     [repair counter](#repair-counter). Steps 8–11 do not run.
   - Invalid and `inFlight.invalidRepairs` is `1`: write a
     driver-authored `fail` (`choice: stop`); keep both candidates;
     clear `inFlight`, append `end`, and print the end line. Stop kind
     `invalid result after repair` points at this step, with
     `resumeWith` the same persona and the `answer` prompt. Steps 8–11
     do not run.

   Steps 8–11 run only after a valid candidate.
8. *(model)* **Result.** Write `result.json`: the candidate, with each
   omitted fixed field filled from the invocation. If this was a mint
   and the session file now exists, record `sessions[persona]`, with
   `WorkerExit.sessionId` as `id` for OpenCode; if the file does not
   exist (Pi writes it only after the first assistant message), or
   OpenCode reported no id, the next run is a mint again. A rehydrate
   counts as a mint here, and a valid result clears
   `sessions[persona].rehydratePending`.
9. *(model)* **Builder push.** After a builder run: check `lastPushed`
   is an ancestor of `HEAD`, push the item branch without force, and
   record `lastPushed`. Not an ancestor: finish this stage (clear
   `inFlight`, append `end`, print the end line) and take an
   `operator` stop (`pushed history rewritten`); do not continue. A
   rejected push: the same finish, `operator` stop, with the redacted
   error.
10. *(model)* **Records.** For a chunk node with `outputs` or
    `outputDirs` and a `pass`, except a paperwork stage:
    [design-record commit](#design-record-commits). A stop inside that
    procedure finishes this stage the same way and does not continue.
    Paperwork never runs inside this step: it is a later stage of its
    own (step 11).
11. **Record and route.** Clear `inFlight`, append `end` to
    `index.jsonl`, print the end line, and route by `choice`, with
    these exceptions:
    - The HLD or Spec node after step 10's design-record commit: in the
      same `driver.json` write that clears `inFlight`, set
      `chunk.pendingRoute` to this node, `choice`, run, record path,
      and pushed commit, and clear `chunk.unposted`. Do not route; the
      next stage is the architect's paperwork
      ([Design-record commits](#design-record-commits) step 7).
    - The HLD or Spec node after a `pass` whose step 10 staged nothing,
      while `chunk.unposted.node` is this node: the record is already
      on project-main from an interrupted run ([Start](#start) step 5).
      In the same write, set `chunk.pendingRoute` to this node,
      `choice`, run, and `chunk.unposted.record` and
      `chunk.unposted.commit`, and clear `chunk.unposted`. Do not route;
      paperwork runs next. A re-run that does not `pass` routes as
      usual and leaves `chunk.unposted` set for the node's next `pass`.
    - A paperwork stage that returns `posted`: in one `driver.json`
      write, clear `inFlight` and `chunk.pendingRoute` and route by
      `pendingRoute.choice` from `pendingRoute.node`.
    - A manager stage routes by [Stops](#stops-and-the-manager).
    - While `items.*.land` is set, the land sub-machine consumes the
      result and this step does not take the flow route.

#### Sessions and rehydrate

A harness session file is never committed. When a resume finds the
persona's session file missing, for example after a restore on another
machine, the driver does not stop:

1. **Backup.** If `sessions[persona].backup` is set and `backup.dir`
   holds that persona's backup with the same SHA-256, restore the file
   and check it with `adapter.sessionLooksValid`. Pass: resume as usual.
   An OpenCode session stores its `--dir`, so a backup restored under
   another run-root path may fail the check; then go to point 2.
2. **Rehydrate.** Otherwise mint a new session with the `rehydrate`
   prompt, set `state: rehydrated` and `rehydratePending: true`, append
   a `rehydrate` event, and say `rehydrated` in the start line. The
   stage's exits are those of the prompt kind it wraps.

The driver-fixed `rehydrate` prompt: the line that names the persona's
[compiled file](#compiled-files); the line `Rehydrated session: your earlier
session is gone; your memory is the state.md below, the driver facts,
and the run folders listed`; the persona's latest mirrored `state.md`;
its last three run folders' paths and, for a verifier, its latest
`ledger.json`; then the wrapped prompt kind, the run contract, and the
facts. `sessions[persona].packed` restarts from the compiled file.

The driver still stops where a fresh session would be unsafe:

| Case | Why it stops | Stop |
| --- | --- | --- |
| The file exists but fails `sessionLooksValid`, or OpenCode reports `Session not found` for an existing database | The file is damaged or is not the persona's own session; it is kept for the operator, never overwritten | `session lost: <file>`, ask kind `lost-session` |
| The file is missing again while `rehydratePending` is `true` | A second loss before one valid result would loop | `session lost: <file>` |
| A mint finds a file already there | Unchanged: `unexpected session file` | `check failed`, `operator` |

**Session backup** (optional, best effort). When `machine.json`
`backup.dir` is set, at each stage end, before the end persist, the driver compresses
that stage persona's session file with Node `zlib` (OpenCode: the
database with its `-wal` and `-shm` files, after the worker's process
group is gone) to `<backup.dir>/<chunk-slug>/<persona>.gz` through a
temporary name and a rename, and records its SHA-256 in
`sessions[persona].backup`, which the state branch mirrors. A failure
prints one line and never stops the run. A backup holds a transcript:
operator-private, outside every repo.

#### Command body

1. Read the commands: for `"groom"`, from the frozen `groom.md` blob
   ([Proving commands](#proving-commands)); for `"env"` and
   `"env-test"`, from the accepted env block
   ([Build-environment gate](#build-environment-gate) point 3); else the
   bundle's `scripts/` files at the pin, read from the
   [toolbox copy](#toolbox-copy) with the object hash checks, and those
   bytes copied into the run folder. For `"groom"` and land L6, first run the dependency
   pre-steps (same section, point 8).
2. Run each command in order in the stage's worktree (the item or env
   worktree, or `worktrees/integrate` for land L6), stopping at the
   first non-zero exit. Each command runs as
   `bash --noprofile --norc -c <line>` in its own process group, with the
   environment from [Environment scrub](#environment-scrub), a
   per-command timeout (`defaults.commandTimeoutSec`), and output to
   `logs/prove-K.log` (cap 50 MiB, then a truncation line).
3. Write `commands.json` and the command result:
   `evidence.command` is the lines joined with ` && `, `exit_code` is the
   first non-zero code or `0`, timeout `124`, signal `128 + n`, launch
   failure `127`. `choice` is the node's `pass` or `fail` exit. On
   `fail`, `findings` names `proving command K of N`, the exit code, and
   the log path.

#### Environment scrub

Workers and proving commands start with the operator's environment
minus:

- every `SDLC_*` and `OPENCODE_*` variable (the adapter then sets the
  worker's own), and `PI_CODING_AGENT_SESSION_DIR`;
- the fixed denylist: `LINEAR_API_KEY`, `LIN_API_KEY`, `GH_TOKEN`,
  `GITHUB_TOKEN`, `NPM_TOKEN`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`,
  every name matching `AWS_*`, and every name ending in `_KEY`,
  `_TOKEN`, or `_SECRET`;
- each name in `run.json` `env.scrubExtra`.

Command stages, and only they, keep each name the accepted env block
lists in `passEnv` ([The `json sdlc-env` block](#the-json-sdlc-env-block)),
even a denylisted one; the operator accepts that list at the `spec`
gate. Workers never get them.

This is hygiene, not a boundary. A worker or a proving command can still
read any credential file the operator can read and can use the
operator's git credential helper or SSH agent. The harness reads model
credentials from its own store: OpenCode from `auth.json` in its data
folder, which the worker environment leaves at the operator's default;
Pi from its configuration. A model slot whose key comes
from a scrubbed variable cannot start, and Run prep's model line
checks each slot's key source and stops with that reason. Proving lines
come only from the frozen `groom.md` blob, the accepted env block, and
the pinned bundle's `defaults.prove` ([Proving commands](#proving-commands)).

#### Node routing

| Scope at node | Result | Next |
| --- | --- | --- |
| `model` or `command` node | `choice` is a listed exit | `node = exit.to`; print `say` if any. `@items`: set the chunk node to `@items` and each planned item to `pending` at `itemEntry`. `@done`: the scope is done |
| any | `choice: stop` | Manager stop, all three manager exits allowed |
| any | `choice: operator` | Manager stop, `escalate` only |
| `gate` node | (reached) | Manager stop of kind `gate`, `escalate` only; ask kind `gate` |
| `land` node | (reached) | [Land sub-machine](#land-sub-machine) |
| `prove`, `verify`, or `review` node of a land node sends the scope back (`fail` exit to the builder node) | — | [Repair counter](#repair-counter) first; third failed fix → `operator` stop instead of the builder |
| `file-tickets` `pass` | — | [Ticket filing](#ticket-filing) before `@items` |
| `spec` gate `pass` | — | Record the accepted env block ([Build-environment gate](#build-environment-gate) point 1) |
| Chunk `land` node `done` while `chunk.reentry` is set | — | `@items`, not the exit's target; resume the stopped item (point 9 there) |

#### Repair counter

Per item, and on `chunk` for env-prep: `repairs` (never reset),
`sentBack`, and `fixPending`. For env-prep, read `env-prove`,
`env-verify`, `env-review`, and `env-builder` for `prove`, `verify`,
`review`, and `builder-<suffix>` below. `env-baseline` never sends the
scope back.

| Event | Effect |
| --- | --- |
| Send-back: the `prove` node `fail`, the `verify` node `fail`, the `review` node `fail`, or a row-1 re-run `fix` ([Land](#land-sub-machine) L3a′) | If `fixPending`: `repairs += 1`. Then `fixPending = false`, `sentBack = true` |
| Land-red: proving commands on the integration merge return `fix` ([Land](#land-sub-machine) L6r only) | `repairs += 1` once, whether or not `fixPending`; then `fixPending = false`, `sentBack = true`. The counter matches this land-red row only, never the L6 green path |
| A builder run starts while `sentBack` is true | `fixPending = true`, `sentBack = false` |
| A builder run starts for `merge-tip` | No change |
| `repairs` is 3 or more after an event | Do not resume the builder: `operator` stop, kind `repair budget exhausted`, with `resumeWith` = `builder-<suffix>` and the prompt kind the send-back would have sent: `test-failure` with the failing log path after a proving-command `fail` or land-red, else `fix` |
| An invalid-result repair | No change |

Console `repair N/3` on a send-back line: N = `repairs + 1`, the fix
attempt about to start. When the answer to a budget stop is `resume`,
the driver resumes `builder-<suffix>` with the prompt kind in
`resumeWith`, the answer appended as the `answer` block. That run starts
with `sentBack` true, so each further failed fix stops again.

#### Land sub-machine

The item enters the land node after a Review `pass`. `T` is the fetched
project-main tip. `H` is the item `HEAD`. The env land runs the same
rows on the `chunk` fields and the env branch, with the changes in
[Build-environment gate](#build-environment-gate) point 6.

| Row | State and condition | Action | Next |
| --- | --- | --- | --- |
| L1 | Enter, or after L3a or L7m | Fetch; set `projectMainSeen = T`; clear `landReentry`. If `T` is an ancestor of `H`, print `tip unchanged` | L5 |
| L1′ | `T` not an ancestor of `H` | Print `tip moved`; `p1 = H`, `p2 = T`; resume the builder with `merge-tip` | L2 |
| L2 | Builder merge run ends | `blocked` or `needs_input`: stop the item (manager), whatever `merge-tree` reports. `pass` (`ready`): push the item branch (pipeline step 9); require that `p1` and `p2` are ancestors of the new `H`, else `operator` stop | L3 |
| L3 | Classify | `git merge-tree --write-tree --no-messages p1 p2`. Exit `0` and its tree equals `H^{tree}`: the builder's end line is `tip merged clean`; set `cleanTree`, `cleanCommit = H`, `reviewBase = H` → L3a. Exit `1` (conflict), or exit `0` with a different tree: the builder's end line is `tip merged, conflicts resolved` → L3b. Any other exit: `operator` stop | — |
| L3a | Clean (row 1, inside land) | Proving commands on the item worktree (`prove-<suffix>`, exits `ok`/`fix`); then the verifier with `land-recheck` (exits `ok`/`fix`). Both `ok` | L1 |
| L3a′ | A row-1 run returns `fix` | Repair counter (send-back event); resume the builder with `test-failure` or `fix`; then L3c | — |
| L3c | Builder returns from an edit after the clean check | `blocked` or `needs_input`: stop. Otherwise push, then re-run L3's check with the stored `p1` and `p2`, never the new `H`'s parents: tree of `H` equals `cleanTree` → L3a; else → L3b | — |
| L3b | Not clean (row 2) | Set `landReentry`. Leave the land node: `node = land.prove`; the item then takes `prove` → `verify` → `review` → land | L1 on the next Review `pass` |
| L5 | Tip unchanged | In `worktrees/integrate`: detach at `T`, `git merge --no-ff --no-edit H` with message `[<ticket>] Land <branch>` and trailer `Reviewed-by: <reviewer-label> (<verdict>)`, where `<verdict>` is the last Review `status` | L6 |
| L6 | Merge exists | Proving commands on the merge (`land-<suffix>/run-N`, exits `ok`/`fix`) | L7 or L6r |
| L6r | Red (`fix`) | Reset the integration worktree to `T` (driver worktree only). Repair counter: the land-red event only; third failed fix → `operator` stop. Else set `landReentry`, resume the builder with `test-failure` and the log path; then `node = land.prove` (row 2 path) | — |
| L7 | Green (`ok`) | `git push origin HEAD:refs/heads/<projectMain>`, no force option. Exit `0` → L8. Non-zero: fetch, let `T′` be the fetched project-main tip, and decide only from git state, never from push output | L8, L7m, or L7x |
| L7m | Push failed, `T′ ≠ T`, and `git merge-base --is-ancestor T T′` succeeds: the tip moved | Reset the integration worktree to `T′`; append a `push` event | L1 |
| L7x | Push failed, and the tip did not move as in L7m | Reset; write a command result in a new `land-<suffix>` run (`git push …`, its exit code, `fail`, redacted error, `choice: stop`); stop kind `blocked` to the manager. Never retry that push | — |
| L8 | Pushed | `landCommit = HEAD`; append it to `lands`; set `projectMainSeen = landCommit`, both before L9 starts; append `land`; resume the verifier with `post-land` (`{{landSha}}`, `{{landResult}}`) | L9 |
| L9 | Post-land verifier ends | `pass`: read the ticket; `done` → delete the remote item branch (`git push origin --delete <branch>`), remove the item worktree, take the land node's `done` exit, print `verified done`. Not `done` → tracker-state check failure, `operator` stop. Any non-`pass`: `operator` stop; the merge stays on project-main; branch and worktree stay; dependents stay blocked | — |

Rules this table encodes:

- The clean merge is always computed from the stored pre-merge parents
  `p1` (item tip before the builder's merge) and `p2` (the tip the
  builder merged).
- A merge commit whose tree differs from the clean tree always goes
  through Review, whatever the builder's result or prose says.
- **Console mapping (SD-28).** The driver prints the builder's end line
  from its own classification, never from the builder's prose, using
  the story's two phrases:

  | Driver classification | Builder end line | Lines that follow |
  | --- | --- | --- |
  | L3 row 1: no conflict, tree equals the clean merge | `tip merged clean` | Verifier re-run; no reviewer line while the tree stays clean. The L3a proving commands print no line unless they fail, as in [ux.md](ux.md)'s SD-28 sample |
  | L3 row 2: conflict, or any other tree | `tip merged, conflicts resolved` | Verifier re-run, then reviewer re-run, then the merge line |
  | L3c after a fix: tree differs from `cleanTree` | The fix run's normal end line | Verifier re-run, then reviewer re-run with the range from `reviewBase` (the clean merge commit) |
  | L2 `blocked` or `needs_input` | None | `STOP` line of kind `blocked` or `needs input`; no merge line |

  While `landReentry` is set, the item's lines use the label `Land`
  and the start notes `fix`, `re-run`, and `re-review`. A
  proving-command stage inside the land node (`items.*.land` set: L3a
  and L6) or while `landReentry` is set prints no start line and no
  end line. When that command fails it prints the command-fail line
  and nothing else. A green L6 run is reported by the
  `tip unchanged  merged  <projectMain>  pushed` line. The persona
  lines are then the builder end line, the verifier (`re-run`), and
  the reviewer (`re-review`): builder → verifier → reviewer, as the
  story says. `index.jsonl` and
  `result.json` keep the real node and step.
- A failed push is classified by fetch and `git merge-base
  --is-ancestor`, never by parsing push output. The design-record push
  uses the same rule ([Design-record commits](#design-record-commits)
  step 5); a failed item-branch push is an `operator` stop whatever the
  output says (pipeline step 9).
- No path retries the same merge or the same push.
- An interrupt waits for a running `git merge`, `git commit`, or
  `git push` to finish, so no merge is left half done (SD-12).

#### Proving commands

1. After [ticket filing](#ticket-filing), the driver records
   `groom.frozenCommit` and `commandsSha256`: the SHA-256 of the
   canonical JSON `[["G1", [line, …]], …]` of every item's `prove`
   lines plus `defaults.prove`.
2. Before every command run it reads `groom.md` with
   `GIT_NO_REPLACE_OBJECTS=1 git -C repo.git cat-file blob
   <frozenCommit>:<path>`, parses the item's block, appends
   `defaults.prove` from the pinned bundle, and compares the item's hash
   with `proveSha256`. A mismatch is a `fail`, `operator` stop.
3. It reads commands from no other copy.

#### Build-environment gate

Once per chunk, after the `spec` gate and before Groom, the env nodes
build and prove the environment the accepted LLD defines
([SDLC flow](#sdlc-flow)); why Groom comes after is in the
[HLD](hld.md#build-environment-gate).

1. **Accepted env block.** The Spec design-record commit (step 6) sets
   `env.specCommit`. At the `spec` gate's `pass` the driver reads
   `lld.md` there with `GIT_NO_REPLACE_OBJECTS=1 git -C repo.git
   cat-file blob`, checks the commit is an ancestor of
   `origin/<projectMain>`, parses the block, and records
   `env.commandsSha256` of its canonical JSON; a failure is
   `check failed: env-block`, an `operator` stop.
2. **Env branch.** Entering `env-prep` with no env worktree, the driver
   fetches, creates `env/<chunk-slug>-<env.pass>` from the project-main
   tip in `worktrees/env/`, pushes it without force, and sets
   `chunk.lastPushed`. The env-builder writes its run folder and
   `worktrees/env/`; pipeline step 9 applies.
3. **Env command stages.** Each run re-reads the block at
   `env.specCommit` and compares the hash (mismatch: `fail`, `operator`
   stop), then runs in `worktrees/env` (`worktrees/integrate` at L6):
   `toolchain`; per dependency `setup`, `start`, `ready` (every 5
   seconds until `0` or `defaults.commandTimeoutSec`), `reset`; then
   `prove`, under the [command body](#command-body) with
   `SDLC_ENV_DIR=RUN_ROOT/env-data/` and the `passEnv` names kept, and
   writes `env-evidence.json`.
4. **Baseline.** `"env-test"` runs each `reset`, then `test`: exit `0`
   is `green`, else `known`; both reach the env-verifier, whose
   `baseline.json` (`{"status", "failing", "log"}`) and `baseline` check
   name every failure and any the env branch caused (a `fix`).
   `env.baseline` records run and status; later failures of those tests
   are not blamed on a builder, and verifiers get the path as a fact.
5. **Verify, review, gate.** As for an item: `env-proof` needs evidence
   per block line; the env-reviewer takes the range with the three
   security reads and `env-harness`; send-backs count on the chunk's
   [repair counter](#repair-counter). The `env` gate follows that agent
   gate: `accept` lands, `revise` sends the env-builder the answer,
   `spec` re-enters Spec. No agent-only acceptance.
6. **Env land.** [Land](#land-sub-machine) L1–L7 on the `chunk` fields,
   with `worktrees/env`, the env branch, `env-prove` (L3a, L6), the
   env-verifier's `land-recheck`, merge message
   `[<epic>] Land <env branch>`, trailer
   `Reviewed-by: env-reviewer (<verdict>)`. In place of L8–L9: set
   `env.landCommit`, append it to `lands`, persist, delete the remote
   env branch (the only remote deletion besides L9), remove
   `worktrees/env/`, set `env.test`, render the
   [compiled files](#compiled-files) again, and take `done`. A branch with no
   commit beyond its base skips L5; its tip becomes `env.landCommit`.
7. **Dependencies during Build.** Before every `"groom"` proving stage
   and L6, per dependency: `ready`, else `start` then `ready`; then
   `reset`. A failure is a driver-authored command `fail`,
   `choice: operator`, stop kind `environment not ready: <dep>`, not a
   send-back and not counted. At `@done` the driver runs every `stop`
   line; `/sdlc-stop` leaves dependencies running.
8. **Re-entry.** A builder, verifier, or reviewer that needs a missing
   capability stops with `env-capability:` (candidate rule 10): stop
   kind `env capability`, `escalate` only, ask `env-capability`:

   | Choice | When | Driver then |
   | --- | --- | --- |
   | `env` | The capability is inside the accepted block | Sets `chunk.reentry`, the chunk node to `env-prep` with the request as `{{capability}}`, and `env.pass` + 1 |
   | `spec` | It needs an LLD change | Sets `chunk.reentry` and the chunk node to `spec`; the run passes `security`, the `spec` gate, and env-prep again |
   | `deny` | Work with the accepted environment | Resumes the stopped persona with the answer |
   | `defer` | Not now | Leaves the item `waiting` |

   The chunk then runs before every item. Its land's `done` goes to
   `@items` ([driver-fixed route](#driver-fixed-exits)); the driver
   clears `reentry` and resumes the stopped persona with the `answer`
   prompt naming `env.landCommit`. Frozen proving commands do not
   change; new or changed items are
   [O16](#questions-for-the-operator).

#### The `json sdlc-env` block

The LLD's `## Build environment` section holds exactly one fenced block
with the info string `json sdlc-env`, read by the strict reader:

```json
{"schemaVersion": 1,
 "toolchain": ["node --version", "docker --version"],
 "deps": [{"name": "postgres",
           "setup": ["docker pull postgres@sha256:<hex>"],
           "start": ["docker run -d --name sdlc-pg postgres@sha256:<hex>"],
           "ready": ["docker exec sdlc-pg pg_isready"],
           "reset": ["docker exec sdlc-pg psql -U postgres -c 'drop schema public cascade; create schema public'"],
           "stop": ["docker rm -f sdlc-pg"]}],
 "passEnv": ["AD_BIND_DN", "AD_BIND_PASSWORD"],
 "prove": ["npm run test:integration -- --grep env-smoke"],
 "test": "npm test"}
```

| Field | Rule |
| --- | --- |
| `toolchain` | Command lines that print versions; their output goes to `env-evidence.json` |
| `deps` | Array; `name` matches `^[a-z][a-z0-9-]{0,31}$`, unique. `setup` (clone, configure, auth through `passEnv` names only), `start`, `ready`, `reset`, `stop`: arrays of command lines, each may be empty; `ready` is non-empty when `start` is |
| `passEnv` | Variable names, `^[A-Z][A-Z0-9_]{0,63}$`: credentials and endpoints of an existing platform, such as AD, that command stages keep ([Environment scrub](#environment-scrub)). The operator's integration instructions in the HLD say where each value comes from |
| `prove` | Non-empty: the proving lines that show the environment works |
| `test` | One line: the repo's test command, run as the baseline and named in the compiled files |

Every command line is at most 1,000 characters with no newline, as in
`groom.md`. No line holds a credential, host name, address, or absolute
path; the design-record scan of `lld.md` enforces it, and a value the
environment needs comes through `passEnv`.

#### Ticket filing

After `file-tickets` passes and its frozen `groom.md` is committed:

1. Parse the frozen file at the driver's commit: the `Tickets:` line and
   every `json sdlc-item` block. Missing or malformed: `fail`,
   `operator` stop.
2. Parse the same blocks at `groom.reviewedCommit`, the driver's last
   commit of `groom.md` before the groom reviewer's `pass`. Any
   difference in `prove`, `blockedBy`, `skills`, or `slug` is a `fail`,
   `operator` stop: the file changed after review.
3. Check the graph is acyclic and every `blockedBy` id exists.
4. Read every ticket ([Tracker reads](#tracker-reads-no-model)): it
   exists, its parent is the Epic, its state is `ready`, and its
   blockers include the planned ones. Read the Epic: `in_progress`.
5. Compute suffixes ([Labels](#labels)); write `plan/items.json`; set
   the chunk node to `@items`.

#### Design-record commits

For a chunk `model` node with `outputs` or `outputDirs`, after a valid
`pass` and passing checks:

1. Fetch; set `projectMainSeen` to the fetched tip; detach
   `worktrees/integrate` at it.
2. For each output path: `out/<path>` must be a regular file (no
   symbolic link on the way), at most 2 MiB; copy it. For each
   `outputDirs` prefix, copy every regular file under it. Ignore any
   other file in `out/` and print one line naming it.
3. Scan the copied files ([Scan patterns](#scan-patterns)). On any hit,
   replace `result.json` with a driver-authored `fail` naming each hit
   as `<file>:<line> <class>`, never the line text, and stop. The
   driver writes the ask itself from those fields and does not resume
   the manager, so no drafted text can quote the hit.
   - Any hit of class `credential`: stop kind `scan hit: credential`,
     ask kind `scan-secret`, choices `revise` and `defer`. No answer
     commits the file as is.
   - Only other classes: stop kind `scan hit`, ask kind `scan-hit`,
     choices `allow` and `revise`. `allow` commits as is; the answer in
     `asks/` is the recorded allowance.
   - `revise` resumes the persona with the `answer` prompt listing the
     hits as `<file>:<line> <class>`.
4. `git add -- <paths>`; commit `[<epic>] <Step>: <node id> from
   <run>`. Nothing staged: no commit, continue.
5. Before each push, set `inFlight.recordCommit` to the commit's SHA
   through the [ledger](#driver-file-ledger)'s two-phase write, and push
   only after it returns: the only value a restart trusts to tell the
   driver's push from any other ([Start](#start) step 5). The write
   follows the `snapshot` check (pipeline step 6), so ledger point 5
   holds and a worker edit fails the next ledger check. Copy the SHA into
   `meta.json` as `recordCommit`, for people; no step reads that copy.
   Push without force. Exit `0`: set `projectMainSeen` to it. Non-zero:
   fetch; if the tip moved as in [Land](#land-sub-machine) L7m, detach
   at the new tip, copy, commit, record, and push again, at most 10
   rounds, then a `blocked` stop; otherwise a `blocked` stop, no retry.
6. The `driver.json` write after exit `0` also sets, for `groom`,
   `groom.recordCommit` (which becomes `groom.reviewedCommit` when the
   next `groom-review` passes), and for the `envSpec` node,
   `env.specCommit`.
7. For the HLD node and the Spec node, paperwork is a separate stage
   that starts only after the parent stage has finished: `inFlight`
   cleared, `end` appended, and `chunk.pendingRoute` persisted
   ([Stage pipeline](#stage-pipeline) step 11). While
   `chunk.pendingRoute` is set, the chunk's next stage is always the
   paperwork stage: resume the architect in a new run folder with
   `paperwork` and `{{commentText}}` holding the comment fields plus
   `Record: <pendingRoute.record>`. Its exits are the
   [driver-fixed](#driver-fixed-exits) `posted` [`pass`], plus the
   reserved `stop`; its `pass` evidence is `comment: <comment id>`. A
   `stop` is a manager stop of kind `paperwork failed`; `resume` runs
   paperwork again with the answer, and `defer` leaves
   `pendingRoute` set for the next `/sdlc`. The parent node's `choice`
   routes only after `posted`.

   **Crash replay.** `driver.json` holds the parent's end and the
   pending route in one atomic write, so a restart sees one of three
   states:

   - (a) The parent is still `inFlight`: [Start](#start) step 5 marks
     it interrupted and applies the pushed record exception on
     `C = inFlight.recordCommit`. Nothing committed: `C` is `null`, the
     node runs again. Committed but `C` not yet in `driver.json` (Start
     promotes a ledger `next` only when the file holds it, ledger point
     2): `worktrees/integrate` sits at an unnamed commit, so `worktrees`
     fails, an `operator` stop. `C` written, push not on the remote: the
     not-pushed case; the node commits its own record again. Pushed: the
     pushed case; the re-run stages nothing unless it changes the file
     (then its record replaces `C`), and pipeline step 11 sets
     `pendingRoute` from `C`. Any other change, such as project-main at
     a commit `C` does not name, is an `operator` stop, whatever
     `meta.json` says.
   - (b) `pendingRoute` is set and a paperwork stage is `inFlight`:
     Start step 5 marks that run interrupted and runs its post-stage
     checks with no exception. Only when they pass does the loop run
     paperwork again in a new run folder; a failed check is an
     `operator` stop. A comment the interrupted run already posted
     stays; the replay posts its own, with its own `Run:` line, so the
     Epic can show two paperwork comments for one record.
   - (c) `pendingRoute` is set and nothing is `inFlight`: the loop runs
     paperwork.

   Paperwork never re-commits the record, and once `pendingRoute` is
   set the parent node does not run again for that record.

#### Scan patterns

Per line, applied to every committed record and to every ticket or
comment file the [tickets check](#tickets-content-check) sees added or
modified, in full, front matter included. Each pattern has a class:

| Class | Patterns | Operator may `allow` |
| --- | --- | --- |
| `credential` | `-----BEGIN [A-Z ]*PRIVATE KEY-----`; and, each starting at a word boundary, `lin_api_[A-Za-z0-9]{20,}`, `ghp_[A-Za-z0-9]{20,}`, `github_pat_[A-Za-z0-9_]{20,}`, `AKIA[0-9A-Z]{16}`, `xox[abprs]-[A-Za-z0-9-]{10,}`, `sk-[A-Za-z0-9_-]{20,}`; URLs with a password (`://[^/\s:@]+:[^/\s@]+@`). Case-sensitive | No: revise only |
| `ip` | IPv4 addresses, except `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, and `127.0.0.1` | Yes |
| `path` | `/home/`, `/Users/`, `/root/`, `/var/lib/`, `C:\Users\`, and the literal run root path; case-insensitive | Yes |
| `host` | Host suffixes `.lan`, `.local`, `.internal`, `.ts.net`, `.home.arpa`; case-insensitive | Yes |
| `userinfo` | URLs with a user name and no password (`://[^/\s:@]+@`) | Yes |

The credential prefixes require a body of the stated length so that
words such as `disk-based` do not match `sk-`. Console lines, asks,
prompts, and tracker text name a hit by file, line, and class only.

**`passEnv` values.** Every scan here (design records, tickets, state
commits) also matches, as class `credential`, the literal value of each
accepted `passEnv` variable set in the driver's environment, when it has
at least 6 characters. Command stages write those values into no
mirrored file: `env-evidence.json` excerpts replace each with
`<passEnv NAME>`, and full output stays in local logs. A shorter value
is not matched; Start warns ([Start](#start) step 2).

#### Post-stage checks

Every check named here is the `check` field of a failed-check result.
"Worker stage" means a model stage. The pre-stage snapshot (pipeline
step 4) records what each check compares.

| Check | After | How |
| --- | --- | --- |
| `snapshot` | every stage | Walk `RUN_ROOT` without following symbolic links. Excluded: the current run folder, the current persona's session file (OpenCode: `opencode.db` and its `-wal` and `-shm` files), `worktrees/`, `env-data/` (a running dependency writes there), `driver/snapshot.json`, `driver/driver.stderr`, and everything under `repo.git/` except `config`, `hooks/`, and `info/`. Record path, type, mode, size, and SHA-256 (the target string for a link). A [driver file](#driver-file-ledger) is compared with its ledger entry, and `driver/ledger.json` with the driver's last ledger write; every other path is compared with the pre-stage snapshot. A cache keyed by inode, size, and `ctime` skips rehashing unchanged files, except under `toolbox.git/`, which the [toolbox copy](#toolbox-copy) rule covers. Any difference is a failure |
| `worktrees` | every stage | For each worktree outside the stage's writable set, `worktrees/state/` always among them: `HEAD` and `git status --porcelain` equal before and after. A command stage's writable set is its run folder and the worktree it runs in. At restart only, an interrupted HLD or Spec stage's `worktrees/integrate` may sit at its `inFlight.recordCommit` in `driver.json`, never a value from the run folder ([Start](#start) step 5) |
| `refs` | every stage | `git ls-remote origin` before and after: every ref name and tip equal, except `refs/heads/tickets`, which the `tickets` check owns, and the state branch, which must equal the tip record's `pushedTip` after the stage whatever the snapshot holds (the stage-start persist moves it before the snapshot). A ref added, deleted, or moved fails, whoever moved it. At restart only, an interrupted HLD or Spec stage's project-main may have fast-forwarded to its `inFlight.recordCommit` in `driver.json` ([Start](#start) step 5) |
| `tickets` | every stage | [Tickets content check](#tickets-content-check) |
| `ancestry` | builder stages | `lastPushed` is an ancestor of `HEAD` (pipeline step 9) |
| `project-main` | every worker stage | Fetch; let `M0` be `projectMainSeen` and `M1` the fetched tip. For each active item with `HEAD` `H`, no commit in `git rev-list H ^M0 ^<each commit in lands>` is also in `git rev-list M1 ^M0`. Then `projectMainSeen = M1` |
| `extension` | worker stages | `logs/ext.json` exists and names this persona and facts hash; for OpenCode it also names the persona's agent, the agent the worker plugin saw in `chat.message`. Missing or wrong: `check failed: extension`, an `operator` stop with no repair, because the stage ran without the path guard and the compaction hook, or under another agent's permissions |
| `tracker-state` | worker stages | [Tracker-state check](#tracker-state-check) |

**`projectMainSeen`.** The driver also sets it to the tip it fetches at
loop step 3, land L1, and design-record step 1, and to the commit it
pushes at L8 and design-record step 5. So `M0` is always a tip the
driver saw outside a worker stage, a land merge never counts against
the item it lands, and an item branched from or merged with a newer tip
does not fail. The `refs` check catches any project-main move during a
worker stage; this check also covers commits that reach project-main
between stages.

#### Driver-file ledger

The driver itself changes some files in the `snapshot` walk during a
stage and across a restart: the start line, `projectMainSeen`, the lock,
the stat cache. Compared with the pre-stage snapshot, they would fail
every stage. They are compared with the driver's own record instead.

**Driver files** are `driver.json`, `index.jsonl`, and every file under
`plan/`, `asks/`, `compiled/`, and `driver/`, except `driver/snapshot.json`,
`driver/ledger.json`, and `driver/driver.stderr`. Only the driver and
the plugin write them ([Who may write what](#trust-boundaries)). Every
other path in the walk, such as `run.json`, other persona folders, and
other personas' sessions, only a worker could change during a stage; it
is compared with the pre-stage snapshot.

1. **One write path.** The driver and the plugin change a driver file
   only through one core function, which keeps `driver/ledger.json`:

   ```json
   {"schemaVersion": 1,
    "files": {
      "driver.json": {"type": "file", "mode": "0600", "size": 1834, "sha256": "<hex>", "next": null},
      "driver/console.log": {"type": "file", "mode": "0600", "size": 90211, "sha256": "<hex>", "next": null}},
    "updatedAt": "<UTC>"}
   ```

   The plugin writes only through `core.prepare` and
   `core.recordAnswer` (`runJsonSha256`, answers in `asks/`), so it uses
   the same function. Removing a file (the lock at release) removes its
   entry. Run prep's `toolbox` creates an empty ledger before it writes
   any driver file.
2. **Two phases.** Before a write, the function sets the entry's `next`
   to the `{size, sha256}` the file will have and writes the ledger;
   then it writes the file; then it moves `next` into the entry and
   writes the ledger again. Ledger writes are atomic
   ([Behavior 4](#behavior-4-run-root-formats)). A file that equals the
   entry or its `next` passes, so a kill at any point leaves files that
   pass. At Start, the driver promotes `next` when the file equals it
   and clears it otherwise.
3. **Hashes from the driver's bytes.** A replaced file's hash is the
   SHA-256 of the bytes the driver wrote. `index.jsonl` and
   `driver/console.log` are append-only: each line is one `write` call
   with `O_APPEND`, and the new hash comes from a running SHA-256 the
   driver holds for the file (Node `Hash.copy()`), never from reading
   the file back. A worker's edit, truncation, or extra line therefore
   stays a mismatch after the driver's next append. At Start, the
   ledger check's read of each append-only file seeds its running hash.
4. **The comparison.** The `snapshot` check compares each driver file
   with its entry: type, mode, size, and SHA-256, or the entry's `next`
   (point 2). A driver file with no entry, or an entry with no file,
   fails. The pre-stage snapshot's records of driver files are ignored.
   `driver/ledger.json` itself must equal the bytes of the driver's last
   ledger write, which the driver holds in memory.
5. **No replace before the check.** From the worker spawn (pipeline
   step 5) until `snapshot` has run (step 6), the driver only appends to
   driver files and replaces none. `snapshot` runs first in step 6,
   before `project-main` writes `projectMainSeen`. A worker's edit of a
   replaced file such as `driver.json` is therefore still on disk when
   the check runs; the driver's later rewrite cannot hide it.
6. **Across a restart.** `driver/ledger.json` persists the hashes. The
   ledger check is point 4 without the in-memory comparison: the ledger
   on disk is read as found. `core.prepare` runs it before the plugin
   reads or writes `driver.json` or records an answer, and
   [Start](#start) step 2 runs it again before the driver reads
   `driver.json`; only `driver/lock`, replaced at Start step 1 when
   stale, is written before it. A mismatch refuses the run root with
   `driver file changed outside the driver: <path>` and both hashes, as
   a harness mismatch stops a start; the operator restores the file or
   starts a new run root. At Start step 5, every change since the
   interrupted stage's snapshot that the driver or plugin made (the
   start line, `projectMainSeen`, the lock, the stat cache, the
   extension copy, the found report's lines, recorded answers) matches
   the ledger, and only worker-set paths are compared with
   `driver/snapshot.json`. Start step 5's pushed record exception reads
   `inFlight.recordCommit` only from a `driver.json` that passed this
   check, so a worker edit of that value refuses the run root before
   the exception is evaluated. Trusting the ledger as found is a
   [residual](#trust-boundaries).

#### Tickets content check

The `local` tickets branch is public on a public repo. After every
stage, including every worker stage, the driver diffs `origin/tickets`
against the pre-stage tip `P`, and the `refs` check diffs every other
ref. The only allowed paths are `tickets/<id>.md` for this stage's
ticket and that ticket's `comments/`, and a comment body must equal
the driver's comment template. Any other ref or path is
`check failed` and an operator stop. `file-tickets` is the only
exception, and only for the rows marked below.

1. Fetch `tickets`; let `Q` be the new tip. `P` is the pre-stage tip.
   `Q = P`: pass.
2. `git merge-base --is-ancestor P Q` must succeed.
3. For each commit in `git rev-list --reverse P..Q`: exactly one parent;
   message exactly `[<id>] <verb>` with `<verb>` one of `create`,
   `claim`, `transition`, `comment`, `set-blocker`; author name, author
   email, committer name, and committer email
   (`git log -1 --format=%an%x00%ae%x00%cn%x00%ce <c>`) equal the
   driver-set identity for this stage, below; and every entry of
   `git diff-tree -r --no-renames --name-status <c>^ <c>` is allowed by
   the table below, mode `100644`.
4. Scan every added or modified file at `Q` in full, front matter
   included, with the [scan patterns](#scan-patterns). Any hit fails;
   the operator cannot `allow` it here. One exception: a non-credential
   hit on a `file-tickets` body line that copies a `groom.md` line the
   operator allowed at that file's design-record scan (the recorded
   `scan-hit` answer in `asks/` names that file and line) does not
   fail.
5. For `file-tickets`, the filing rules below hold over the whole
   range.
6. Anything else is `check failed: tickets`, an `operator` stop that
   names the commit and path, or the file, line, and class of a scan
   hit, never the text.

`<id>` is the stage's `ticket`: the item for an item stage and for a
manager stage about an item; otherwise the Epic. `<label>` is the
persona label
([Tracker calls](#behavior-7-tracker-calls-per-persona)).

**Driver-set identity.** The adapter sets `GIT_AUTHOR_NAME` and
`GIT_COMMITTER_NAME` to `<label>`, and `GIT_AUTHOR_EMAIL` and
`GIT_COMMITTER_EMAIL` to `<label>@sdlc.invalid`, in every worker's
environment ([OpenCode adapter](#opencode-adapter-and-worker-command-line),
[Pi adapter](#pi-adapter-and-worker-command-line)). Git
gives these variables precedence over `user.name` and `user.email`, so
the `local` recipe's commits carry them, and so do a builder's item
commits. A tickets commit with any other value fails, whoever made
it.

**Front-matter values.** `<state>` is one of `backlog`, `ready`,
`in_progress`, `in_review`, `done`, `canceled`. `<UTC>` matches
`^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}Z$`,
the `local` recipe's `now` format.

| Entry | Allowed when |
| --- | --- |
| `M tickets/<id>.md` | Only the front-matter lines `state:`, `assignee:`, and `updated:` differ from the parent; every other line is byte-equal. `state` is a `<state>`; `assignee` equals `<label>` or is unchanged from the parent; `updated` is a `<UTC>` |
| `A comments/<id>/<TS>-<label>.md` | At most one per stage. `<TS>` matches `^[0-9]{8}T[0-9]{6}Z$`. The body equals the driver's [comment template](#behavior-7-tracker-calls-per-persona) for this stage, with `Status` one of the four statuses and only the optional lines that row allows, with the driver's values |
| `file-tickets` only: `A tickets/<new>.md` | `<new>` matches `tracker.keyPattern`. The front matter has exactly these keys, each once, in this order: `id`, `type`, `title`, `state`, `parent`, `blocked_by`, `labels`, `assignee`, `created`, `updated`, `links`. `id` is `<new>`; `type: task`; `title` is `G<n>: <title>`, byte-equal to a groom item's heading text; `state: backlog`; `parent` is the Epic; `blocked_by` is `[]` or a list of planned ticket ids; `labels: []`; `assignee` empty; `created` and `updated` are the same `<UTC>`; `links: []`. The body, every line after the closing `---`, equals that item's section of the reviewed `groom.md` (filing rule 1, below) |
| `file-tickets` only: `M tickets/<new>.md`, `M tickets/<epic>.md` | As the first row, with `blocked_by` also allowed to gain planned ids, and `assignee` unchanged |

**Filing rules** (`file-tickets` only):

1. **Reviewed, scanned body.** The section source is `groom.md` at
   `groom.reviewedCommit`: a commit the driver made, whose copy passed
   the [scan](#scan-patterns) at design-record step 3, and which
   `git merge-base --is-ancestor <reviewedCommit> origin/<projectMain>`
   shows is already on project-main at the check. Otherwise the check
   fails. The section is the lines after its `### G<n>: <title>`
   heading up to the next `##` or `###` heading, with leading and
   trailing blank lines dropped.
2. **One ticket per groom item.** Each `A tickets/<new>.md` in the range
   matches exactly one groom item by title, and no groom item gets two.
3. **No duplicate filing.** No `A` is allowed for a groom item that
   already has a ticket at `P` whose `parent` is the Epic and whose
   `title` starts with `G<n>: `. A re-run of `file-tickets` after an
   interrupted one reuses that ticket; the manager's prompt says so.

Other people share the tickets branch and project-main. A write to
another ticket, or any other ref move, during a stage also stops the
run; the operator's answer decides, and the stop text names the ref or
path so the operator can tell a colleague's write from a worker's.

Every git call by the driver sets `GIT_CONFIG_COUNT` to disable hooks
(`core.hooksPath=/dev/null`) and the file system monitor
(`core.fsmonitor=`), sets `GIT_NO_REPLACE_OBJECTS=1`, and has
no force option in its code path. Calls in the toolbox copy add the
[copy rules](#toolbox-copy): the protocol limits, no system config,
and `driver/gitconfig` as the global config. The only deletions of a remote
branch are L9's item branch and the env land's env branch
([Build-environment gate](#build-environment-gate) point 6). The first-start
local ref `integrate-empty` is removed with `git update-ref -d` after
the detach, only if that ref still exists, and it is never pushed.

#### Stops and the manager

| Stop kind (console words) | Trigger | Manager may | Ask kind |
| --- | --- | --- | --- |
| `blocked` | Worker `blocked` with `stop`; L2; L7x; design-record push | `resume`, `defer`, `escalate` | `operator-stop` |
| `needs input` | Worker `needs_input` with `stop` | `resume`, `defer`, `escalate` | `operator-stop` |
| `invalid result after repair` | Pipeline step 7 | `resume`, `defer`, `escalate` | `operator-stop` |
| `paperwork failed` | Design-record step 7 | `resume`, `defer`, `escalate` | `operator-stop` |
| `operator gate: <tag>` | A gate node | `escalate` | `gate` |
| `operator: <question>` | Worker chose `operator` | `escalate` | `operator-stop` |
| `env capability: <line>` | Worker chose `operator` with an `env-capability:` check (candidate rule 10) | `escalate` | `env-capability` |
| `environment not ready: <dep>` | Dependency pre-steps of a proving stage ([Build-environment gate](#build-environment-gate) point 7) | `escalate` | `operator-stop` |
| `repair budget exhausted` | Repair counter | `escalate` | `operator-stop` |
| `check failed: <check>` | A post-stage check (`snapshot`, `worktrees`, `refs`, `tickets`, `ancestry`, `project-main`, `extension`, `tracker-state`, `tracker-read`), the pre-spawn `harness` re-check, the pre-spawn `harness-config` preflight, `extract`, `unexpected session file`, `pushed history rewritten`, and the run-state checks `state`, `state-commits`, `toolbox`, `compiled`, `env-block` | `escalate` | `operator-stop` |
| `scan hit` | Design-record step 3, no credential hit | Not resumed: the driver writes the ask | `scan-hit` |
| `scan hit: credential` | Design-record step 3, a credential hit | Not resumed: the driver writes the ask | `scan-secret` |
| `state scan hit` | Persist step 3, no credential hit | Not resumed: the driver writes the ask and returns | `state-scan` |
| `state scan hit: credential` | Persist step 3, a credential hit | Not resumed: the driver writes the ask and returns | `state-secret` |
| `state push failed` | Persist step 5, the remote tip unchanged | Not resumed: the driver writes the ask and returns | `state-push` |
| `state lease lost` | Start, or persist step 5 with a moved remote tip | None: the driver exits; only a restore continues | — |
| `state lease unknown` | Start cannot fetch the state branch at `pushed` | Not resumed: the driver writes the ask and returns | `state-push` |
| `session lost: <file>` | A present session file fails its check, `WorkerExit.sessionMissing`, or a second loss while `rehydratePending` ([Sessions and rehydrate](#sessions-and-rehydrate)) | `escalate` | `lost-session` |
| `OpenCode config folder: <path>` | `~/.opencode/` or `/etc/opencode/` exists ([OpenCode adapter](#opencode-adapter-and-worker-command-line)) | `escalate` | `opencode-dir` |
| `project Pi files: <path>` | `.pi/` in a worker cwd ([Pi adapter](#pi-adapter-and-worker-command-line)) | `escalate` | `pi-dir` |
| `post-land verify failed` | L9 | `escalate` | `operator-stop` |

1. The driver sets the scope's `stop`, with `resumeWith` defaulting to
   the stopped persona and the `answer` prompt (the budget stop names
   the builder and its pending prompt kind; see
   [Repair counter](#repair-counter)), prints the `STOP` line, and
   resumes `manager` with the `stop` prompt (or `gate`). Scan and state
   stops skip the manager, as their rows say.
2. Manager exits are the [driver-fixed](#driver-fixed-exits) `resume`
   [`pass`], `defer` [`pass`], `escalate` [`needs_input`]. A `pass`
   needs one `evidence.checks` entry
   `source: <brief|plan|spec|tracker|gather> <path or run folder>`;
   the console prints it (SD-7).
3. `resume`: resume `resumeWith.persona` in a new run folder with
   `resumeWith.prompt`, followed by the `answer` block; `{{answer}}` is
   the manager's `findings`, verbatim, fenced as data.
4. `defer`: state `deferred`; other scopes continue; the next `/sdlc`
   start makes it `active` again and re-runs the stop.
5. `escalate`: the manager wrote `ask-human.md`. The driver writes
   `asks/ask-N.json` and `.md`, prints the full message, sets the
   scope to `waiting`, and continues with other runnable scopes.
6. The manager's own result is invalid after its repair, or it chooses
   an exit not offered: the driver writes the ask itself from the stop
   fields (no manager text) and continues as in step 5.
7. The manager never gets a manager stop.

**Answers** (at the next `/sdlc`, before any stage):

| Ask kind | Answer | Driver then |
| --- | --- | --- |
| `gate` | A gate exit + text | Writes the gate node's result in `operator/run-N/`: `status` = that exit's status, `choice` = the exit, `findings` = the text verbatim, `evidence.checks` = `["operator-answer: asks/ask-N"]` for `pass`. Routes |
| `lost-session` | `replace` | Renames the old file, if present, with `.lost-<UTC>` appended (OpenCode: with its `-wal` and `-shm`), mints a new session with the `rehydrate` prompt and the answer |
| `lost-session` | `defer` | Leaves the scope `waiting` |
| `scan-hit` | `allow` or `revise` | [Design-record commits](#design-record-commits) step 3 |
| `scan-secret` | `revise` or `defer` | `revise`: as for `scan-hit`. `defer`: leaves the scope `waiting`. There is no `allow` |
| `operator-stop` | Text | Resumes `manager` with `apply-answer`; exits `resume`, `defer`, `escalate` as in steps 3–5 |
| `env-capability` | `env`, `spec`, `deny`, or `defer`, + text | [Build-environment gate](#build-environment-gate) point 8 |
| `state-scan` | `allow`, `exclude`, or `defer` | [Persist](#durable-run-state) step 3; `defer` leaves the run stopped |
| `state-secret` | `exclude` or `defer` | The same; there is no `allow` |
| `state-push` | `retry`, `local`, or `defer` | Persist step 5; for `state lease unknown`, `retry` fetches again and `local` lowers the level |

An empty answer records nothing; the ask stays pending (never proceed
after silence).

#### Prompts

The driver builds `prompt.md` in this order:

1. On a mint, the line that names the persona's
   [compiled file](#compiled-files); on a rehydrate, the
   [`rehydrate`](#sessions-and-rehydrate) header block, which starts
   with that line; on a resume whose `compiled` entry changed, the
   `# Compiled update` block.
2. Packed skills not yet in `sessions[persona].packed`, each under
   `# Packed skill <id> — do not reload`, read from the pinned commit,
   or, for the repo tracker skill, from `origin/<projectMain>` at the
   last fetch.
3. The prompt kind's text with placeholders filled.
4. The run contract, fixed by the driver: the run folder; the files the
   worker may write; paths in prose relative to the run root or the
   repo; `state.md` limits; the allowed exits with their
   statuses; the required checks and outputs; the tracker steps from
   [Tracker calls](#behavior-7-tracker-calls-per-persona) with the exact comment
   text; "Finish with `sdlc_result`."
5. The facts.

Range placeholders: `{{rangeMain}}` is `origin/<projectMain>...HEAD`,
the diff versus project-main. `{{range}}` is `<reviewBase>..HEAD`, or
`{{rangeMain}}` when `reviewBase` is unset; after a row-1
classification `reviewBase` is the clean merge commit, so a later
re-review starts there (SD-28).

A prompt over a quarter of the persona's `contextWindow`, estimated at
four characters per token, prints a warning line.

#### Tracker-state check

After each worker stage the driver reads the ticket (or the Epic) and
compares:

| Stage | Expected state | Expected assignee |
| --- | --- | --- |
| Builder, any pass | `in_progress` | `builder-<suffix>` |
| Verifier, before land | `in_progress` | `verifier-<suffix>` |
| Reviewer | `in_review` | `reviewer-<suffix>` |
| Verifier, post-land, `pass` | `done` | `verifier-<suffix>` |
| Verifier, post-land, not `pass` | `in_progress` | `verifier-<suffix>` |
| Chunk personas, except `file-tickets` | Epic state unchanged from before the stage | not checked |
| Manager, `file-tickets` | [Ticket filing](#ticket-filing) step 4 | not checked |
| Manager, stops | Unchanged from before the stop | not checked |

Anything else is `check failed: tracker-state`. The read happens after
the stage even when the result is invalid, so a builder that moved the
ticket to `done` is caught before any repair.

#### Tracker reads (no model)

As the HLD says, the driver reads ticket state with the repo tracker
skill's `read` recipe, run as a command with no model. In this chunk
only the `local` backend has such a recipe, and it is a git read
([local adapter Reads](../../../skills/tracker-sdlc/adapters/local.md#reads)).
Run prep's checklist requires the repo skill to carry that recipe and
stops without it. The driver runs the recipe's git calls as fixed argv
in `repo.git`, so no shell string from a repo file runs:

1. `git -C repo.git fetch origin +refs/heads/tickets:refs/remotes/origin/tickets`.
2. `git -C repo.git ls-tree refs/remotes/origin/tickets tickets/<id>.md`
   must show mode `100644`.
3. `git -C repo.git show refs/remotes/origin/tickets:tickets/<id>.md`;
   parse the front matter (`id`, `type`, `state`, `parent`,
   `blocked_by`, `assignee`) with the adapter's text format; reject a
   malformed list or an unknown state.

Every id is checked against `tracker.keyPattern` before use. A read
that fails after three attempts (2, 4, and 8 seconds apart) is
`check failed: tracker-read` with a redacted message. Any backend other
than `local` is refused at Run prep and at `/sdlc` start
([`run.json`](#runjson)); Linear for driven runs is G9.

#### Console lines

Fields are separated by two spaces. `<S>` is the ticket id, or the Epic
id for the chunk. `<L>` is the node `label`, padded to 7.

| Event | Line |
| --- | --- |
| Header | `<slug>  bundle <id>@<sha7>  mode enforced  state <level>  root <RUN_ROOT>` |
| Found | `found  last finished  <S> <L> <run> <status>`; `found  interrupted  <run> (kept)`; `found  will resume  <personas>`; `found  will rehydrate  <personas>`; `found  will restore from backup  <personas>`; `found  next run  <run>`; `found  pending ask  ask-N  <S> <L>: <stop kind>`; `found  state  <level>  seq <n>  <tip7>  lease ok` |
| Start | `<S> <L>  <persona>  new, resumed, or rehydrated  <run>  started[  <note>]`; notes: `merge tip`, `fix`, `re-run`, `re-review`, `repair` |
| End | `<S> <L>  <status>  choice <choice>  artifact <path>[  <extra>]`; extra for Verify `ledger <fixed> fixed, <open> open, <nits> nit`, for Review `reads <packed skills>` |
| Command fail | `<S> <L>  fail  proving command K of N failed  log <path>  repair N/3` |
| Invalid | `<S> <L>  invalid result  <run>  repair 1/1` |
| Rejected choice | `<S> <L>  rejected choice <value>  allowed <exit> (<statuses>), …` |
| Land | `<S> Land  fetched  tip moved  builder merges the tip`; `<S> Land  pass  tip merged clean  artifact <path>`; `<S> Land  pass  tip merged, conflicts resolved  artifact <path>` ([console mapping](#land-sub-machine)); `<S> Land  fetched  tip unchanged  merged  <projectMain>  pushed`; `<S> Land  verifier  resumed  <run>  verified  done` |
| Stop | `STOP   <S> <L>  <stop kind>  <run>` then `       resuming manager  <run>`; scan stops instead name each hit as `<file>:<line> <class>` and print the driver-written ask |
| Manager answered | `       manager answered from <source>  <S> continues` |
| Ask | The full `ask-human.md` text between `--- ask-N ---` lines |
| Say | `<S> <L>  <say text>` |
| State | Only on a problem: `STATE  <stop kind>  <file>:<line> <class>` or `STATE  lease lost  remote <tip7>, expected <tip7>`; and at `@done`: `done  state branch <branch> is yours to keep or delete` |
| Toolbox | `STOP   <S> <L>  check failed: toolbox  <step>` then `       sdlc-driver toolbox RUN_ROOT --remote <remote from your note> --rebuild`; the step names the file, the commit, or the two remotes; `check failed: compiled  <persona>`; at a cleared interrupted repin, `repin interrupted; still at <old7>` |
| Summary | OpenCode: `idle  <n> pending asks  <n> waiting  <n> deferred  pick /sdlc, then enter RUN_ROOT to continue`; Pi: `idle  <n> pending asks  <n> waiting  <n> deferred  type /sdlc RUN_ROOT to continue` |

`driver/console.log` holds every line. No color carries meaning, and no
worker transcript goes to the console.

### Behavior 6: harness plugins (item 7 OpenCode first, item 6 Pi second)

Both plugins host the same core through the
[adapter interface](#adapter-interface). Item 7, OpenCode, is built and
proven first, because the operator's first tests run in OpenCode
([clarification](#clarifications-of-the-hld-made-here) 16). Item 6, Pi,
follows. The OpenCode facts, read in 1.19.3 source, and the Trial
checks O-T1–O-T10 with their fallbacks are in
[opencode-server.md](opencode-server.md); this section fixes the design.

#### OpenCode host shape and `/sdlc`

**Chosen: a detached driver process**, the shape the HLD
[Trial question](hld.md#trial-question) assumes without a Trial. It
depends on O-T7; the fallback is in
[opencode-server.md](opencode-server.md#trial-checks).

`src/tui.ts`, a TUI plugin with default export `{id: "sdlc", tui}`,
registers two palette commands with `api.keymap.registerLayer`, each
with a `slashName`, and no tool. Picking a command from the
autocomplete or the palette runs it in the TUI process with no model
turn. Neither takes an argument, so each asks for the run root.

`/sdlc`:

1. Refuse when `SDLC_RUN_DIR` is set (a worker process), or when the
   TUI's own argv holds `--port`, `--hostname`, or `--mdns`: with those
   flags the TUI opens a server listener that a worker's `bash` could
   use to drive the TUI.
2. Ask for `RUN_ROOT` with `api.ui.DialogPrompt`, prefilled with the
   last run root from `api.kv`, and resolve it to an absolute path. If
   a live driver holds the lock: show its status and pending asks in
   `api.ui.DialogAlert`, say that answers are recorded when it is idle
   or after `/sdlc-stop`, and return.
3. `core.prepare`: show validation errors in `DialogAlert`; the
   `run.json` and `machine.json` confirmation in `DialogConfirm`, or in
   `DialogPrompt` when the answer must equal the full bundle SHA; an
   unconfirmed [restore](#durable-run-state) summary in `DialogPrompt`,
   whose answer must equal the state tip's first 12 hex digits; the found report;
   and each pending ask in full. For each ask, `DialogSelect` offers its
   choices plus `not now`, then `DialogPrompt` takes the text;
   `core.recordAnswer` stores it.
4. Append the run root to `roots.json` in the plugin's state folder,
   `$XDG_STATE_HOME/opencode-sdlc/`, for the input guard in step 6.
5. Spawn `harness.node src/driver-main.ts RUN_ROOT` with `detached:
   true` (a new session and process group), stdin closed, stdout and
   stderr to `driver/driver.stderr`, and `unref()`. The TUI runs inside
   the compiled `opencode` binary, so `process.execPath` is not Node.
6. Start a two-second timer that calls `api.ui.toast` for each new
   `STOP`, ask, or `done` line of `driver/console.log` and shows its
   last 12 lines in the `sidebar_content` slot (`api.slots.register`).
   If O-T7 shows the slot cannot render plain text, the toasts stay and
   `/sdlc` shows the `tail -f RUN_ROOT/driver/console.log` line.

**Input guard.** `src/server.ts`, a server plugin in the operator's own
OpenCode, throws in `chat.message` when a text part starts with
`/sdlc`, and for any prompt while the lock of a run root in
`roots.json` is held by a live process. The throw fails the prompt
before OpenCode saves the message or calls a model, and its text
reads `driver running: one large-model session at a time` or
`pick /sdlc from the command list`. No server command named `sdlc`
exists, because a server command always runs a model turn. Depends on
O-T8; the fallback is in the note and is operator question
[O11](#questions-for-the-operator).

`/sdlc-stop` asks for the run root, then sends `SIGTERM` to the lock
holder after checking its process start time. The driver then kills
the worker's process group, waits for any git critical section, writes
`interrupted.json`, releases the lock, and exits (SD-12).

Item 7's README gives the install lines: the package folder path in the
`plugin` list of the operator's `tui.json` and `opencode.json`. OpenCode
loads each entry by kind from the package `exports`, and loads
TypeScript directly. The README checks the lines on 1.19.3.

#### OpenCode adapter and worker command line

```text
<harness.bin> run --format json [--session <sessions[persona].id>]
  --agent <label> --model <run.json models[slot].model>
  --title "<label> run-N" --dir <cwd>
  < RUN_ROOT/<persona>/run-N/prompt.md
```

| Part | Why |
| --- | --- |
| `run --format json`, no positional message | Headless, one process, no TCP listener; the prompt arrives on stdin, which `opencode run` joins into the message |
| `--session <id>` | Absent on a mint, which creates a root session with no parent and an empty transcript; present on a resume. A missing id exits `1` with `Session not found` |
| `--agent <label>` | The per-stage agent in the worker config, holding the persona's permission rules |
| `--title` | A set title skips OpenCode's title model call |
| `--model`, `--dir` | The slot's `provider/model`; the persona's cwd |

- **cwd:** builder, verifier, reviewer: `worktrees/<suffix>`. Chunk
  personas: `worktrees/integrate`.
- **Worker config:** `src/worker-config.ts` builds it per stage, keeps
  it in `driver/worker-config/<persona>--run-N.json` (a
  [driver file](#driver-file-ledger)), and passes the same text in
  `OPENCODE_CONFIG_CONTENT`. It holds the keys the note's
  [Chosen shape](opencode-server.md#chosen-shape) lists, the providers
  from `run.json` `harness.providers` with their `options` from
  `machine.json`, and one agent named for the
  persona label with the permission rules of the note's
  [Tools per persona](opencode-server.md#tools-per-persona), built from
  the persona's `tools` and `readOnly`. The `external_directory` allow
  list names the run root, which holds the
  [compiled files](#compiled-files), and the system temporary folder.
- **Preflight** (`adapter.preflight`), before each spawn, with no model
  call:
  1. `~/.opencode/` or `/etc/opencode/` exists: OpenCode reads both
     whatever the environment says. If either holds a `tool/` or
     `tools/` folder, return `harness-config` naming it, whatever the
     operator has allowed: OpenCode imports every `*.js` and `*.ts`
     file there as a tool, and `debug config` does not list those
     tools, so step 2 cannot see them. Otherwise return `harness-dir`
     with ask kind `opencode-dir` and the SHA-256 of the sorted
     `<path> <sha256>` list of the folder's files. An `allow` holds
     until that hash changes.
  2. Run `<harness.bin> debug config` with the worker's environment and
     cwd. Its `plugin`, `agent`, `permission`, `mcp`, `instructions`,
     `command`, and `provider` must equal the worker config's, apart
     from OpenCode's built-in agents. Any other entry returns
     `harness-config`, naming the key. This catches the layers the
     environment cannot switch off: remote and organization config tied
     to the operator's OpenCode login.
- **Environment:** the scrubbed environment of
  [Environment scrub](#environment-scrub); plus:

  | Variable | Value |
  | --- | --- |
  | `SDLC_RUN_DIR` | Absolute run folder |
  | `SDLC_RUN_REL` | Run folder relative to the run root |
  | `SDLC_PERSONA`, `SDLC_JOB`, `SDLC_TICKET`, `SDLC_STEP` | The invocation |
  | `SDLC_WRITABLE` | JSON array of absolute paths: the run folder, plus the item worktree for an item builder or `worktrees/env/` for the env-builder |
  | `SDLC_EXITS` | JSON array of `{"name", "statuses"}`, reserved exits included as the worker may use them |
  | `SDLC_CHECKS`, `SDLC_OUTPUTS` | JSON arrays from the node |
  | `SDLC_FACTS`, `SDLC_FACTS_SHA256` | [Driver facts](#driver-facts) |
  | `GIT_AUTHOR_NAME`, `GIT_COMMITTER_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_EMAIL` | `<label>`, `<label>`, `<label>@sdlc.invalid`, `<label>@sdlc.invalid`: the [driver-set identity](#tickets-content-check) |
  | `OPENCODE_DB` | `RUN_ROOT/<persona>/opencode.db` |
  | `OPENCODE_CONFIG_CONTENT` | The worker config |
  | `XDG_CONFIG_HOME` | `RUN_ROOT/driver/opencode/xdg-config`, holding one empty `opencode/` folder; the driver creates both at each start and sets `opencode/` to mode `0500`, because OpenCode creates that folder at start-up and fails if it cannot |
  | `SDLC_XDG_CONFIG_HOME` | The operator's `XDG_CONFIG_HOME`, empty when unset; the worker plugin restores it for `bash` |
  | `OPENCODE_DISABLE_PROJECT_CONFIG`, `OPENCODE_DISABLE_CLAUDE_CODE`, `OPENCODE_DISABLE_AUTOUPDATE`, `OPENCODE_DISABLE_MODELS_FETCH`, `OPENCODE_DISABLE_LSP_DOWNLOAD` | `1` ([note](opencode-server.md#chosen-shape)) |

  With project config off, the product repo's `opencode.json`,
  `.opencode/`, `AGENTS.md`, and `CLAUDE.md` do not load, so the cwd
  needs no refusal like Pi's `.pi/`.
- **Process:** spawned with `detached: true` so the worker leads its own
  process group; stdout to `logs/worker.jsonl`, stderr to
  `logs/worker.stderr`. On timeout or `/sdlc-stop`: `SIGTERM` to the
  group, 20 seconds, then `SIGKILL`.
- **Leftovers:** after the worker exits, the adapter sends `SIGTERM` to
  the group and, on Linux, to every process of the same user whose
  `/proc/<pid>/environ` holds this `SDLC_RUN_DIR`. A process that
  cleared its environment escapes: residual.
- **Outcome:** exit `1`, or an `error` line in `worker.jsonl`, sets
  `modelError`. `Session not found` on a resume sets `sessionMissing`.
  The first line's `sessionID` is `sessionId`. A stream with no line
  means the worker never started.
- **`sessionLooksValid`:** the database file exists, starts with the
  SQLite header, and `<harness.bin> session list --format json`, run
  with the persona's `OPENCODE_DB` and cwd, lists exactly
  `sessions[persona].id`.

#### Worker plugin (OpenCode)

`worker/sdlc-worker.ts`: one file, imported only from Node built-ins.
Tool args are plain JSON Schema, so it needs no `zod`. The driver copies
it into `driver/worker-ext/` at each start, and the worker config names
that copy by `file://` URL, so the `snapshot` check covers it through
the [driver-file ledger](#driver-file-ledger).

1. **Load.** Parse every `SDLC_*` variable; check `SDLC_FACTS_SHA256`.
   Any error throws; OpenCode then logs and skips the plugin, so the
   marker is missing. At init, write `logs/ext.json`
   (`{"persona", "factsSha256", "version"}`) with `fs` directly; on the
   first `chat.message`, add `"agent"` from the hook input. A missing
   or wrong marker has one outcome: the post-stage `extension` check
   fails, an `operator` stop with no repair.
2. **`tool.execute.before` guard.** For `write` and `edit`, take
   `args.filePath`; for `apply_patch`, every path on a `*** Add File:`,
   `*** Update File:`, `*** Delete File:`, or `*** Move to:` line of
   `args.patchText`. Resolve each path: a leading `~/` is the home
   folder; a relative path is against the process cwd. Resolve
   symbolic links on the deepest existing ancestor and on the target if
   it exists. Allow only a path inside an `SDLC_WRITABLE` entry, with no
   `.git` path component, and, inside the run folder, not `prompt.md`,
   `result.json`, `meta.json`, `commands.json`, `interrupted.json`, or
   `logs/`. Otherwise throw an error that names the writable set; the
   throw rejects the tool call. The whole handler sits in `try`; any
   error throws.
3. **`sdlc_write`.** Parameters `{path, content}`. `path` is relative to
   the run folder and matches
   `^(candidate\.json|result\.md|state\.md|ledger\.json|baseline\.json|ask-human\.md|out/[A-Za-z0-9._/-]+)$`
   with no `.` or `..` segment. Parent folders are created one by one
   and checked to be real folders. The file opens with
   `O_WRONLY|O_CREAT|O_TRUNC|O_NOFOLLOW`, mode `0600`. Content at most
   1 MiB; `state.md` at most 60 lines and 6,000 characters, else an
   error that says to shorten it. The tool checks the types of its own
   args, because OpenCode does not validate JSON Schema args.
4. **`sdlc_result`.** Parameters `status` (enum of the four statuses),
   `choice` (enum of the names in `SDLC_EXITS`), `findings`,
   `artifact`, `checks` (array of strings), `blocker`, and `question`.
   OpenCode makes every JSON Schema property required, so an unused
   `checks` is `[]` and an unused `blocker` or `question` is `""`. It
   applies the shape rules of item 1 and candidate rules 2, 3, and 5,
   returns the errors to the model in the same turn, and writes
   `candidate.json` only when they pass. The driver validates again;
   the tool is advisory. Its tests run the shared fixtures, so the two
   stay in step.
5. **Compaction summary.** The deterministic summary is:

   ```text
   # Compaction summary (sdlc worker, not a model)
   ## Persona
   <SDLC_PERSONA> (<SDLC_JOB>) for <SDLC_TICKET>, step <SDLC_STEP>.
   Current run folder: <SDLC_RUN_REL>. Write files only with sdlc_write;
   finish with sdlc_result.
   ## State (state.md, at most one page)
   <state.md, first 60 lines>
   ## Driver facts (written by the driver)
   <SDLC_FACTS, verbatim>
   ```

   A missing `state.md` is replaced by one line saying so.
   `experimental.session.compacting` sets `output.prompt` to an
   instruction to return that text verbatim.
   `experimental.chat.messages.transform` replaces the text of every
   `summary: true` message with it on each model request, so the model
   sees the deterministic summary whatever the compaction agent wrote.
   `experimental.chat.system.transform` appends the driver-facts block
   to every request's system prompt. No handler cancels a compaction.
6. **`shell.env`.** Sets `output.env.XDG_CONFIG_HOME` to
   `SDLC_XDG_CONFIG_HOME`, so `bash` and `git` see the operator's
   setting. The hook's return value is ignored, so it returns nothing.
   If O-T3 fails, the adapter sets `GIT_CONFIG_GLOBAL` instead
   ([note](opencode-server.md#trial-checks)).

The plugin registers no command and reads no file outside the run
folder except its own load-time constants.

#### Pi host shape and `/sdlc`

Item 6, the second harness, blocked by item 7; its Pi version is O6.

**Chosen: a detached driver process** (HLD
[Trial question](hld.md#trial-question): without a Trial result, Spec
assumes the detached shape). `Trial-dependent` (T1); the fallback is
under [Trial-dependent decisions](#trial-dependent-decisions).

`extensions/sdlc.ts` registers two user commands and no tool:

`/sdlc RUN_ROOT`:

1. Refuse when `ctx.hasUI` is false (Pi sets it false in `-p` and JSON
   modes), so no headless start, or when `SDLC_RUN_DIR` is set (a
   worker process).
2. Resolve `RUN_ROOT` to an absolute path. If a live driver holds the
   lock: show its status and pending asks, say that answers are
   recorded when it is idle or after `/sdlc-stop`, and return.
3. `core.prepare`: show validation errors, the `run.json` and
   `machine.json` confirmation (`ctx.ui.confirm`) when needed, an
   unconfirmed restore summary (`ctx.ui.input`, the state tip's first
   12 hex digits), the found report, and each pending
   ask in full (`ctx.ui.custom` text view). For each ask, `ctx.ui.select`
   offers its choices plus `not now`, then `ctx.ui.input` takes the text;
   `core.recordAnswer` stores it.
4. Spawn `process.execPath src/driver-main.ts RUN_ROOT` with
   `detached: true` (a new session and process group), stdin closed,
   stdout and stderr to `driver/driver.stderr`, and `unref()`.
5. Start a two-second timer that shows the last 12 lines of
   `driver/console.log` with `ctx.ui.setWidget("sdlc", lines)` and
   calls `ctx.ui.notify` for each new `STOP` or ask line.
6. Register an `input` handler that returns `{action: "handled"}` for
   any non-slash input while this run root's lock is held, and notifies
   `driver running: one large-model session at a time`.

`/sdlc-stop RUN_ROOT`: sends `SIGTERM` to the lock holder after
checking its process start time. The driver then kills the worker's
process group, waits for any git critical section, writes
`interrupted.json`, releases the lock, and exits (SD-12).

The plugin is installed from the checkout by local path, not into a
`node_modules` folder, because Node does not strip TypeScript types
under `node_modules`. Item 6's README gives the one supported install
line and checks it on 0.73.1. The detached entry runs on
`process.execPath` when Pi runs on Node; under Pi's compiled binary it
uses `run.json` `harness.node`.

#### Pi adapter and worker command line

```text
<harness.bin> --print --mode json
  --session RUN_ROOT/<persona>/session.jsonl
  --no-extensions --extension RUN_ROOT/driver/worker-ext/sdlc-worker-<sha12>.ts
  --no-skills --no-context-files
  --tools <persona tools>,sdlc_write,sdlc_result
  --model <run.json models[slot].model>
  < RUN_ROOT/<persona>/run-N/prompt.md
```

| Part | Why |
| --- | --- |
| `--print --mode json`, no positional message | Headless; the prompt arrives on stdin, which Pi joins into the first message, so there is no argv size limit and no shell quoting |
| `--session <file>` | Mint when the file is absent, resume when present ([Stage pipeline](#stage-pipeline) step 2) |
| `--no-extensions` with one `--extension` | Discovery off; Pi still loads explicit `--extension` paths |
| `--no-skills --no-context-files` | No skill discovery; no `AGENTS.md` or `CLAUDE.md`; skills arrive packed |
| `--tools` | Allowlist for built-in and extension tools; read-only personas get no `write` or `edit` |
| `--model` | `provider/id[:thinking]` from the persona's slot |

- **cwd:** as in the [OpenCode adapter](#opencode-adapter-and-worker-command-line).
- **Project Pi files:** in `adapter.preflight`, before each start, the driver refuses a cwd
  that contains `.pi/`, because Pi reads project settings,
  `.pi/SYSTEM.md`, and `.pi/APPEND_SYSTEM.md` from there. This is an
  `operator` stop with ask kind `pi-dir` (choices `allow`, `defer`). An
  `allow` is recorded in `driver.json` with the git tree hash of that
  `.pi/` folder and holds until the tree changes.
- **Environment:** the scrubbed environment of
  [Environment scrub](#environment-scrub); the `SDLC_*` and `GIT_*`
  rows of the [OpenCode table](#opencode-adapter-and-worker-command-line),
  with the same values; plus `PI_OFFLINE=1`: Pi skips its start-up
  network calls and version check. No `OPENCODE_*` variable is set.

- **Process, leftovers:** as in the
  [OpenCode adapter](#opencode-adapter-and-worker-command-line).
- **Outcome:** Pi's JSON mode exits `0` even when the model call fails.
  The adapter reads the last `agent_end` event in `worker.jsonl`; when
  the last assistant message's `stopReason` is `error` or `aborted`,
  `modelError` is set. A stream without the session header line means
  the worker never started.
- **`sessionLooksValid`:** the file's first line parses as JSON with
  `"type": "session"`.

#### Worker extension

`worker/sdlc-worker.ts`: one file, imported only from Node built-ins and
`@sinclair/typebox` (Pi's extension loader aliases it for any loaded
file). The driver copies it into `driver/worker-ext/` at each start, so
the `snapshot` check covers it through the
[driver-file ledger](#driver-file-ledger).

1. **Load.** Parse every `SDLC_*` variable; check `SDLC_FACTS_SHA256`.
   Any error throws, so Pi reports the extension as failed. On
   `session_start`, write `logs/ext.json`
   (`{"persona", "factsSha256", "version"}`) with `fs` directly. A
   missing or wrong marker has one outcome: the post-stage `extension`
   check fails, an `operator` stop with no repair.
2. **`tool_call` guard.** For `write` and `edit`, apply the path rules
   of the [OpenCode guard](#worker-plugin-opencode) point 2 to
   `input.path`. A path they refuse returns `{block: true, reason}`
   naming the writable set. The whole handler sits in `try`; any error
   blocks. Pi also blocks the call when a `tool_call` handler throws.
3. **`sdlc_write`.** As the OpenCode plugin's point 3, with TypeBox
   parameters, which Pi validates.
4. **`sdlc_result`.** As the OpenCode plugin's point 4, with `choice` a
   TypeBox union of the names in `SDLC_EXITS`, and `checks`, `blocker`,
   and `question` optional.
5. **`session_before_compact`.** Returns
   `{compaction: {summary, firstKeptEntryId, tokensBefore}}`, the last
   two from `event.preparation`. The summary is the deterministic
   summary of the OpenCode plugin's point 5, which Pi stores as the
   compaction itself, so no model writes it. The handler never cancels
   a compaction.

The extension registers no command and reads no file outside the run
folder except its own load-time constants.

#### Pi facts checked in 0.73.1 source

Read from the published package, without installing or running it.
`U` = `https://unpkg.com/@mariozechner/pi-coding-agent@0.73.1`.

| Fact | Source |
| --- | --- |
| `-ne`/`--no-extensions` disables discovery; explicit `-e` paths still load | `U/dist/cli/args.js`; `U/dist/core/resource-loader.js` |
| `-t`/`--tools` is an allowlist over built-in, extension, and custom tools; built-ins are `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls` | `U/dist/cli/args.js`; `U/dist/core/sdk.js`; `U/dist/core/agent-session.js` |
| `-nc` is `--no-context-files` (`AGENTS.md`, `CLAUDE.md`); `-ns` is `--no-skills` | `U/dist/cli/args.js` |
| Non-TTY stdin is read and joined into the first message | `U/dist/main.js`; `U/dist/cli/initial-message.js` |
| JSON mode: first line is the session header, then one event per line, ending with `agent_end`; exit code `0` without a `stopReason` check | `U/dist/modes/print-mode.js`; `U/docs/json.md` |
| A missing `--session` file is created at that path; it is written only after the first assistant message; header `{"type": "session", "version": 3}` | `U/dist/core/session-manager.js` |
| `tool_call` returns `{block: true, reason}`; a throwing handler blocks the tool | `U/docs/extensions.md`; `U/dist/core/extensions/runner.js` |
| `session_before_compact` payload `{preparation, branchEntries, customInstructions?, signal}`; return `{cancel}` or `{compaction: {summary, firstKeptEntryId, tokensBefore}}` | `U/dist/core/extensions/types.d.ts`; `U/dist/core/agent-session.js` |
| Compaction triggers when `contextTokens > contextWindow - reserveTokens`; defaults `reserveTokens` 16384, `keepRecentTokens` 20000; project `.pi/settings.json` overrides global | `U/dist/core/compaction/compaction.js`; `U/docs/settings.md` |
| `ctx.hasUI` is false in `-p` and JSON modes, where `select` and `input` return `undefined` | `U/docs/extensions.md`; `U/dist/core/extensions/runner.js` |
| `pi -p "/cmd"` runs an extension command; piped stdin in front of it stops the match | `U/dist/core/agent-session.js` |
| `ctx.ui` has `select`, `confirm`, `input`, `notify`, `setWidget`, `custom`; an `input` event can return `{action: "handled"}` | `U/dist/core/extensions/types.d.ts` |
| Extensions load in process through jiti with aliases for `@sinclair/typebox` | `U/dist/core/extensions/loader.js` |
| `--offline` or `PI_OFFLINE=1` also sets `PI_SKIP_VERSION_CHECK=1` | `U/dist/main.js` |
| No built-in `bash` restriction; extensions run with full user rights | `U/README.md` |
| 0.73.1 is the last release under this name; the registry marks it deprecated in favor of `@earendil-works/pi-coding-agent` | `https://registry.npmjs.org/@mariozechner/pi-coding-agent` |

### Behavior 7: tracker calls per persona

Every write goes through `tracker-sdlc` and the packed repo skill. The
driver fills `{{commentText}}`; the worker posts it verbatim:

```text
Ticket: <ticket id, or the Epic id>
Status: <status of this run's result>
Run: <persona>/run-N/
```

Optional lines, in this order, only where the table says: `Record:
<repo-relative path>`, `Land: <sha>`, `Result: <post-land command
status>`, `Review: <reviewer-label> (<verdict>)`. Claim markers keep
their own shape; on `local` the marker is the `assignee` line, not a
comment. The [tickets check](#tickets-content-check) accepts a comment
body only if it equals this template, so a worker that adds or
changes a line stops the run.

| Persona | Calls, in order | Label |
| --- | --- | --- |
| Builder, every pass | At start: `claim` (steps 1–4, same-item rule). Before exit, whatever the outcome: `comment`. An open blocker in claim step 1 → result `blocked` with `evidence.blocker`; a collision → `needs_input`, `operator` | `builder-<suffix>` |
| Verifier, before land | `claim`; `comment` with the ledger verdict as `Status` | `verifier-<suffix>` |
| Reviewer, every pass | `claim`; claim step 5, then `transition` `in_review`; `comment` with the verdict as `Status` | `reviewer-<suffix>` |
| Verifier, post-land, `pass` | `claim`; `transition` `done`; `comment` plus `Land`, `Result`, `Review` | `verifier-<suffix>` |
| Verifier, post-land, not `pass` | `claim`; `transition` `in_progress`; `comment` | `verifier-<suffix>` |
| Refiner, architect, designer, ux-reviewer, security, groom-reviewer, env-builder, env-verifier, env-reviewer | `comment` on the Epic; no claim | The persona folder name, such as `architect` |
| Architect, `paperwork` | `comment` on the Epic plus `Record` | `architect` |
| Manager, `file-tickets` | Groom File steps 2–6: `create` each item (title `G<n>: <title>`, body copied from its `### G<n>` section), `set-blocker` each planned blocker, `transition` each item `ready`, `transition` the Epic `in_progress`, `comment` on the Epic plus `Record: <groom.md path>`. Then the freeze edit in `out/` | `manager` |
| Manager, stops | `comment` on the stopped ticket or the Epic | `manager` |

**Backend and shell recipes.** Driven runs use the `local` adapter only
in this chunk; Run prep and `/sdlc` refuse any other backend
([`run.json`](#runjson)). Workers have no MCP server: Pi has no MCP
client, and the OpenCode worker config lists none. So every recipe
in the repo skill must run from `bash`; the `local` recipes do. This
repo's Linear skill uses MCP, so Linear for driven runs needs shell
recipes, a no-model read recipe, and its own security gate: G9
([O5](#questions-for-the-operator)).

### Behavior 8: Run prep and later items (0, 4, 8)

#### Item 0, `sdlc-kickoff`: Run prep, Gather, restore

One skill with three modes, each run by the operator in a normal
interactive session. None starts the driver or a worker.

**Run prep** (`prep`), stage 0. It asks the setup questions of
[SD-1](user-stories.md#sd-1-prepare-the-run-before-gather), never a
product question, each with its default except the first: the toolbox
remote, which the operator types in full with no default or prefill,
and which must pass the [remote rule](#toolbox-copy), before anything
is cloned or fetched; its trunk, default `main`; the pin at its newest
release tag, else the trunk tip; the run root
`$XDG_STATE_HOME/sdlc/<chunk-slug>/`; the [level](#durable-run-state);
no backup folder. The tracker answer is required, `local` only for
driven runs, with the [ux.md](ux.md) J2 warning; a paid model slot
needs the spending answer.

It then shows the readiness checklist, one line per check, each `done`,
`to do`, `deferred`, or `n/a`. The checklist is a preview: nothing is
written, cut, or pushed until the operator replies; then R2's cut and
push and R10 run.

| # | Check | How |
| --- | --- | --- |
| R1 | Tracker | Onboarding; `local` backend; the repo skill's shell recipes and no-model `read` recipe ([Tracker reads](#tracker-reads-no-model)) |
| R2 | Branches | Trunk exists; project-main exists or, after the reply, is cut from trunk and pushed |
| R3 | Push permission | `git push --dry-run` of project-main to itself, which authenticates without moving a ref; at `pushed`, `state-init`'s first push also proves branch creation |
| R4 | Branch protection and CI | CI config at the project-main tip: `present` or `absent`, for the HLD's environment section. Protection on project-main and trunk through `gh api` when `gh` is logged in for that host, else `unknown`, which the operator confirms. A rule that blocks the driver's direct, non-force push to project-main is `to do` |
| R5 | Harness and plugin | Harness installed at the pinned version; `integrity`; `treeSha256`; OpenCode `harness.providers`; the installed plugin's version equals `harness.plugin` ([`run.json`](#runjson)) |
| R6 | Models | `adapter.missingModels` is empty for every slot; each slot's key source is not a scrubbed variable; a paid slot has its spending record |
| R7 | Toolbox | Git 2.32 or newer; `toolbox --remote` fetches only the remote the operator typed into `toolbox.git`; the toolbox check's byte steps and the bundle check pass at the pin ([Toolbox copy](#toolbox-copy)) |
| R8 | Run root | Parent outside every git worktree, not a symbolic link; the root is created `0700` |
| R9 | Labels | The `labels.mode` that the key pattern needs ([Labels](#labels)) |
| R10 | State | The level; at `pushed` and `local`, `state-init` and `drill` pass |

R1–R4 are the skill's own git, `gh`, and tracker steps; R7 starts with
`sdlc-driver toolbox`; R5–R9 are `sdlc-driver readiness`; R10 is
`state-init` then `drill`. After the
reply, Run prep files the Epic through `tracker-sdlc`; writes
`run.json`, `machine.json`, `checklist.md`, and empty `refiner/run-1/`
and `gatherer/run-1/`; and runs:

| Command | Does |
| --- | --- |
| `sdlc-driver toolbox RUN_ROOT --remote <typed> [--rebuild]` | The [toolbox copy](#toolbox-copy): remote rule against the typed remote, bare trunk copy, config and `HEAD` hashes, pin, compile; `--rebuild` replaces a damaged copy |
| `sdlc-driver readiness RUN_ROOT` | R5–R9 with no question, one checklist line each |
| `sdlc-driver state-init RUN_ROOT` | Start step 3's first-start part; the state branch's first commit, pushed at `pushed`; the tip record; the chunk personas' [compiled files](#compiled-files) |
| `sdlc-driver drill RUN_ROOT` | The [restore drill](#durable-run-state) |
| `sdlc-driver persist RUN_ROOT` | One [persist](#durable-run-state), holding the lock; Gather's last step |
| `sdlc-driver status RUN_ROOT` | The found report, read-only, without the lock |

`state-init`, `persist`, and `restore` refuse when `SDLC_RUN_DIR` is set
or a driver holds the lock. In the turn that runs `state-init`, Run
prep prints the only [genesis note](#toolbox-copy), with the typed
remote and the trunk. It prints the Gather line, `next: Gather; open a new session and load
sdlc-kickoff in gather mode for RUN_ROOT`. The session is discarded;
its decisions live in `run.json`, `machine.json`, and `checklist.md`.

**Gather** (`gather`), after Run prep, in a new session (why after:
[HLD](hld.md#run-prep-and-gather)). It runs `discover-the-idea` on the
operator's brain dump, ends with a brief the operator confirms in
words, writes `gatherer/run-1/brief.md`, copies the Gather session file
next to it and lists the copy in `machine.json` `gather.sessions`, runs
`sdlc-driver persist`, and prints the run root and the start line: in
OpenCode, "pick `/sdlc`, then enter RUN_ROOT"; in Pi, `/sdlc RUN_ROOT`.

**Restore** (`restore`), on a machine without the run root. It asks the
machine-local questions (harness paths, run-root location, backup
folder), runs R5, R6, and R8, runs `sdlc-driver restore`, and prints the
start line; the first `/sdlc` takes the typed remote and trunk,
re-clones the toolbox at the pin (R7), and shows the restore summary
([Durable run state](#durable-run-state)).

**Build order.** Item 0 lands first and fixes the procedure, the checks,
and the formats in `docs/sdlc/run-state.md`. R1–R4 work from the skill
as soon as it lands. `readiness`, `state-init`, `drill`, `persist`,
`status`, `restore`, `toolbox`, and compiling are `sdlc-driver` subcommands
that item 5 builds against those formats; until then the skill names
them as not available yet. Item 5's tests run the skill's command
sequence on a fixture repo ([O14](#questions-for-the-operator)).

#### Items 4 and 8

Both items start after the first harness, OpenCode (item 7), works.

- **Item 4, `bundle-authoring`.** Walks an author through the
  [bundle layout](#bundle-layout-and-bundlemd), persona files, and
  `flow.json`; ends by running `sdlc-driver check` until it exits `0`.
  It routes to `bundle-spec.md` and `flow-spec.md` and restates no rule.
- **Item 8, `sdlc-followed-mode`.** The same algorithm in prose: the
  loop, the stage pipeline without process isolation, the same run
  folders and `result.json`, the exit rule, and `followed, not enforced`
  on the first line, in every stage's prose, and in every stop. At each
  separate-agent step it prints this handoff block and stops (UX Q2,
  open):

  ```text
  followed, not enforced
  Persona: verifier-der-a530 (new session; resume this session for its later passes)
  Run folder: RUN_ROOT/verifier-der-a530/run-1/
  Prompt: RUN_ROOT/verifier-der-a530/run-1/prompt.md
  Open a new session, paste the prompt file, and come back when result.json exists.
  ```

  A mint's `prompt.md` starts with the line that names the persona's
  [compiled file](#compiled-files), so the new session needs one read.
  Followed mode has no driver to persist, so its runs are `plain`;
  Run prep offers only that level for a followed run.

### Trust boundaries

**Actors.** The operator (trusted; holds every gate); the driver and the
plugin (trusted code from the pinned commit and the installed package);
workers (untrusted model output with the operator's shell rights); the
manager (a worker); the Run prep, Gather, and restore session models
(untrusted; write `run.json`, `machine.json`, and the brief); the
env commands (shell lines from the accepted LLD); the tracker, git
remote, and model provider (external).

| # | Boundary | What crosses | Control | Kind |
| --- | --- | --- | --- | --- |
| TB1 | Operator → driver | `/sdlc`, `/sdlc-stop`, `/sdlc-repin`, answers, the restore confirmation | User commands only, never a tool; refused inside a worker. OpenCode: the commands exist only in the TUI plugin, so no headless path starts the driver; refused when the TUI has a server listener; a server command named `sdlc` never exists. Pi: refused without UI. Answers recorded only in the interactive handler while no driver runs | Enforced; headless start blocked; a worker that fakes a terminal is residual |
| TB1a | Operator's session → model while a driver runs | The operator's own prompts | OpenCode: the server plugin's `chat.message` throw while a lock is held and for typed `/sdlc` text (O-T8). Pi: the `input` handler | Enforced if O-T8 holds; else notify only, operator question [O11](#questions-for-the-operator) |
| TB2 | Run prep model → `run.json`, `machine.json` | Paths, models, tracker, spending, harness pin, durability level, backup folder | Strict schema; `local` backend only; `run.json` scanned as portable; the operator confirms a summary of both files at the first `/sdlc` and on every change; `bundle.remote` only `https://`, `ssh://`, or scp form, and never proposed or decided by the model: the operator types it in full at Run prep before any clone or fetch, it is recorded in `driver.json` `bundleRemote` and the off-machine genesis note, checked against the copy's `remote.origin.url` at every start and repin, and fixed for the run; the reviewed ref is `refs/heads/<bundle.trunk>` at that remote (default `main`, fixed for the run), fetched by name, never the remote's `HEAD`; a bundle commit not on it needs the full SHA typed back, with `scripts/` and persona hashes shown and each script's INTAKE record found at the reviewed ref | Enforced; the ref is as of this start's or repin's fetch, and anyone who can push the toolbox trunk at the confirmed remote can put a commit on it (operator item 5) |
| TB3 | Bundle → driver | Flow, personas, skills, scripts | Read only from the object store of the [toolbox copy](#toolbox-copy), a bare clone in the run root, each object checked by hash as read, never a working tree; its `config` and `HEAD` byte-checked, and commit-graph, replace, graft, alternates, and shallow files refused, before any git command, its remote confirmed; driver git there with fsmonitor, hooks, and commit-graph off, no system config, a driver-written global config, https or ssh only, and never used to read bytes; never copied into the product repo; at every start the trunk is fetched and the pin must be on it or a typed SHA in the history; a new pin only through `/sdlc-repin` between stages, all its checks on the fetched objects, with the diff shown and the bundle check passed; compiled files are driver files, re-hashed right before each spawn; bundle check; every `scripts/` file listed with its hash and INTAKE record; third-party bundles through INTAKE | Enforced; a malicious intake-passed bundle is out of scope; a same-uid process while the driver runs is residual (item 7) |
| TB3a | Harness → driver | The OpenCode binary or the Pi package the workers run | `harness.version` and `harness.treeSha256` checked at every start, and the tree hash re-checked from a stat cache before each worker spawn; npm checked `integrity` of each package at install. OpenCode: self-update off in the worker config and environment; provider packages only from those bundled in the binary | Enforced at start and at each spawn; `harness.node` is not hashed (residual) |
| TB3b | Operator's harness config → worker | OpenCode: plugins, tools, agents, MCP servers, instructions, remote and organization config. Pi: `.pi/` project files | OpenCode: `XDG_CONFIG_HOME` pointed at an empty unwritable folder, project config off, `~/.opencode/` and `/etc/opencode/` refused until allowed, a `tool/` or `tools/` folder in either refused even after an allow, and `debug config` compared with the worker config before every spawn. Pi: `--no-extensions`, `--no-skills`, `-nc`, and the `.pi/` refusal | Enforced before each spawn (OpenCode: O-T2); config that changes between the compare and the spawn is residual |
| TB4 | Driver → worker | Prompt, facts, env, OpenCode worker config | Prompt built from driver state; model or operator text fenced as data; facts hash; extension or worker-plugin copy hashed; worker config kept as a driver file; fixed environment denylist | Enforced and detected; the denylist is hygiene, not a boundary |
| TB5 | Worker → files | `write`, `edit`, OpenCode `apply_patch`, `sdlc_write` | Allowlist (OpenCode: permission rules; Pi: `--tools`), path guard (fail-closed), run-folder tool. OpenCode adds its own `external_directory` rules, so a write outside the run root and the temporary folder is refused before the guard runs | Enforced (OpenCode: O-T4); the guard's check-then-write race is an accepted residual |
| TB6 | Worker → files through `bash` | Any write | Snapshot (driver files against the driver-file ledger), worktree, refs, ancestry, project-main checks | Detected in the run root and worktrees; residual elsewhere (operator accepts in writing) |
| TB7 | Worker → result | `candidate.json` | Strict validation; only validated fields route; prose never routes | Enforced |
| TB8 | Worker → tracker | Every verb, full access to the `tickets` branch | Tracker-state check on state and assignee; tickets content check on every commit (driver-set author and committer), path, front-matter key and value, comment body, and filed ticket body, plus a scan of every touched file | Detected after the stage; the write is public before the check runs (operator accepts in writing) |
| TB9 | Driver → tracker | One read per check | The repo skill's `local` read recipe as fixed git argv; ids checked against the key pattern | Enforced |
| TB10 | Driver and workers → git remote | Pushes with the operator's credentials | Driver code has no force option; pushes only item branches, the env branch, project-main, and the state branch; L9 and the env land are the only remote deletions; moved tips decided by `merge-base --is-ancestor`; the `refs` check compares every remote ref around every stage | Enforced for the driver; worker pushes detected after the stage, public before it (operator accepts in writing) |
| TB11 | Worker → model provider | Prompt, repo content, tool output | Local model by default; a paid slot requires the spending record | Enforced at start |
| TB12 | Proving commands | Shell lines | Only from the frozen, reviewed `groom.md` blob, the accepted env block, and the pinned bundle; hash per run | Enforced |
| TB13 | Run root → project-main | Design records | Only declared outputs, regular files, scanned; the operator may allow a non-credential hit; a credential hit is revise-only | Enforced |
| TB14 | Driver → state branch | The **D** files: results, prose, `state.md`, asks with verbatim answers, plan, brief, env evidence | Only the mirror set, never sessions, logs, prompts, `machine.json`, or the tip record; only checked run folders' worker files; text files up to 256 KiB; scanned before every commit, `passEnv` values included, credential hits never committed; driver-set identity; fast-forward push without force; the lease; the operator picks the level, warned on a public repo | Enforced for the driver. At `pushed` the mirror set is on the remote, public on a public repo |
| TB15 | State branch → driver, at restore | The whole durable state | Hash ledger and `prev` chain verified; every commit the state names for proving, env, and land must be on the fetched project-main, the toolbox copy is cloned only after the operator types the remote, and its compiled hashes must equal the restored ones; the summary shows each commit with its ancestry, and the diff from the genesis commit's pin to the restored one; commits by another identity listed; the operator types, from their own off-machine note, the genesis commit and the full toolbox remote, which must equal the restored one, then the tip; a pin other than the genesis pin needs its full SHA typed back whatever its ancestry; the lease moves only then | A wholly foreign or rewritten chain, or another toolbox remote, is refused. A consistent forged continuation that names commits planted on project-main can choose the proving and env commands the restored run executes (operator item 4); one that names another pin on the confirmed remote is caught only by the operator's reading of the diff before typing its SHA (operator item 5) |
| TB16 | Env block → command stages | Dependency, toolchain, `prove`, and `test` lines; `passEnv` names | Only from the LLD at `env.specCommit`, which **security** reviewed (`env-commands`) and the operator accepted with its `passEnv` list at the `spec` gate; hash per run; `passEnv` values reach command stages only | Enforced; the commands run with the operator's rights, like proving commands |
| TB17 | Driver → session backup folder | Compressed session files: transcripts | Only when the operator sets `backup.dir`; folder outside every git worktree, not a link, `0700`; hash in the state; best effort | Enforced at write; the folder's privacy is the operator's |
| TB18 | Worker → env worktree, dependencies | Harness code; running services | The env-builder writes only its run folder and `worktrees/env/`; harness code reaches project-main only through env-prove, env-verify, env-review, the `env` gate, and the env land; services write `env-data/` or outside the run root | Enforced and detected as for item work; service writes outside the run root are residual (operator accepts in writing, item 1) |

**Secrets.**

| Secret | Where it lives | Who reads it | Never in |
| --- | --- | --- | --- |
| Worker tracker credential | `local`: the operator's git credentials. No other backend in this chunk; Linear is G9 | Workers | Run root files the driver writes |
| Git credentials | The operator's credential helper or SSH agent | Driver and workers | `run.json` (origin URL without user info) |
| Model credentials | The harness's own store: OpenCode's `auth.json` in its data folder; Pi's configuration | The harness | Run root files the driver writes; the scrubbed environment; `run.json` `harness.providers` and `machine.json` `providerOptions`, which Run prep refuses with an `apiKey` or header |
| Integration credentials (`passEnv`) | The operator's environment when the driver starts | Command stages only | Workers' environment; the LLD and every mirrored file (replaced in `env-evidence.json`, matched by every scan when 6 or more characters); the state branch. Local logs may hold them |

The driver holds no tracker key in this chunk. A worker can still print
a secret it can read into a log, `out/`, or prose: logs stay in the run
root (`0700`) and are never mirrored; `out/` is scanned before commit,
and a credential-shaped hit there can only be revised; prose and
`state.md` are scanned before every state commit, and a
credential-shaped hit there is excluded or deferred, never committed.

**Egress.** The git remote (which also carries the `local` tickets
branch and, at `pushed`, the state branch), the session backup folder
when set, the model provider (local by default), and whatever a
worker's `bash` or a proving command reaches. Workers can read any file
the operator can and can reach the network through `bash`. With a paid
reviewer this is also the spending and egress gate in `run.json`.

**Data class.** The run root's local part (prompts, transcripts, logs,
tool output) is operator-private, never committed or published; so are
session backups, outside every repo, and the logs and long tool output
OpenCode workers write under the operator's OpenCode data folder,
outside the run root's `0700`. The **D** files are operator-private at
`plain` and `local`, and at `pushed` readable by everyone who can read
the repo (TB14, [public repo](#durable-run-state)). Tracker comments are
public: only the template in
[Tracker calls](#behavior-7-tracker-calls-per-persona), enforced after
the fact by the [tickets check](#tickets-content-check); a `local`
tickets branch on a public repo is public, and Run prep warns first.

**Who may write what.**

| Path | Driver | Builder | Other workers | Plugin |
| --- | --- | --- | --- | --- |
| Own current run folder (worker files) | — | yes | yes | — |
| Item worktree | merges, resets of its own worktrees | its own item | no (detected) | — |
| `worktrees/env` | merges, resets | the env-builder only | no (detected) | — |
| `worktrees/integrate`, project-main | commits, merges, pushes | no (detected) | no (detected) | — |
| `worktrees/state`, state branch | commits, pushes | no (detected) | no (detected) | — |
| `run.json` | no | no | no | `bundle.commit` at a repin, the level at a `state-push` `local` answer, both through `core`; Run prep writes the rest |
| `machine.json` | no | no | no | no; Run prep writes it |
| `driver.json`, `index.jsonl`, `plan/`, `compiled/`, `driver/`, other persona folders | yes | no (detected) | no (detected) | `driver.json` confirmation, the restore confirmation, and `asks/` answers, while no driver runs, through the [ledger](#driver-file-ledger) |
| `env-data/` | env command stages, unchecked | no | no | — |
| `toolbox.git/` | `toolbox`, and the fetch at Start and at a repin; never inside a stage | no (detected) | no (detected) | a repin through `core` |
| Tracker | read only | per table | per table | — |

**What a restart trusts.** `bash` can rewrite any file in the current
run folder undetected, `meta.json` included, so no restart check reads
it. The pushed record exception reads only `inFlight.recordCommit`,
which the ledger protects; a worker push that `driver.json` does not
name is an `operator` stop ([Verify](#verify) scenario 18).

**Residual risks.** The HLD's [Risks](hld.md#risks), as narrowed
here: tracker comment text and writes to other tickets are now detected
by the tickets check, and worker pushes by the `refs` check, both after
the stage.

**Toolbox-copy revision, for security's re-read:** TB2, TB3, and TB15
as changed in their rows above; residual item 7; operator item 5
([O22](#questions-for-the-operator), accepted): the remote typed at Run
prep and its rule, the fixed trunk, the hardened copy git, the trunk
fetch and pin re-check at every Start, in-process object-hash reads,
the object-store repin and its three crash cases, and the drill.

**Run-state revision, accepted with the Spec at 021f81d:** TB2, TB10, TB12, TB13,
and S7 as changed in their rows above; TB14–TB18; operator item 4; the
[Run state](#security-rulings-review-of-34e1278-n1n4-from-the-re-review-of-de7c438)
ruling row.

**New with OpenCode first, for security's re-read** (none changes
O9's accepted residuals): worker copies of logs and long tool output in
the operator's OpenCode data folder (Data class); config that changes
between the pre-spawn `debug config` compare and the spawn (TB3b); the
`~/.opencode/` and `/etc/opencode/` refusal and its `allow`, which never
covers a `tool/` or `tools/` folder, since those tools escape the
compare; a worker's `bash` starting another `opencode` against the
operator's config, as with `pi` (unchanged HLD risk); if O-T8 fails, the
operator's session can call a model while a worker runs (TB1a,
[O11](#questions-for-the-operator)); if O-T1 fails, its fallback's
per-stage loopback listener, reachable from `bash` with the server's
password, which **security** rules on before item 7 uses it.

**Accepted by security** (review of 34e1278):

1. S4: the driver's bare clone in the run root, hooks off for driver
   git, and the `.pi/` refusal in a worker cwd.
2. S8: one exact-pinned `typescript` dev dependency with a lockfile,
   through INTAKE, for items 5 and 6; no runtime dependency.
3. Path-guard race: a symbolic link swapped between the guard's check
   and the write.
4. Followed mode: an agent keeps the gates, including one session per
   persona; no program detects a deviation.
5. Smaller residuals: ignored files that `git status --porcelain` does
   not show; a worker that escapes the leftover sweep; a process that,
   while the driver is down or after killing it, rewrites
   `driver/snapshot.json`, or `driver/ledger.json` with the driver files
   it lists. Each weakens only the interrupted-stage check and the next
   [ledger check](#driver-file-ledger), which read both files as found;
   a ledger rewritten with `driver.json` can also forge
   `inFlight.recordCommit` and pass a worker push under the pushed record
   exception (covered by operator item 1). An escaped leftover's edit of
   a driver file the driver replaces before the next check is lost
   unreported, harmlessly: driver files are read only at a start, after
   the ledger check. `driver/driver.stderr` (never read) is unchecked;
   `driver/lock` is replaced before the ledger check.
6. N4 (re-review of de7c438, low): the reviewed-ref ancestry test and
   INTAKE lookup use the toolbox copy's trunk ref, as of the last
   Start's or repin's fetch; `harness.treeSha256`'s per-spawn re-check
   re-hashes added and stat-changed files and notices removed ones, so a
   change keeping inode, size, `mtime`, and `ctime` waits for the next
   start's full hash; `harness.node` is not hashed.
7. Toolbox copy: the driver trusts the `git` binary, the operator's
   `credential.*` and `core.sshCommand` values it copies into
   `driver/gitconfig`, and SHA-1 object ids, with git's collision
   detection. Run prep, the drill, and a restore fetch only a remote
   the operator typed. Start re-fetches the trunk and re-checks the
   pin, so a pin moved while the driver is down fails; a typed pin is a
   `driver.json` record, so forging one needs a ledger rewrite (item
   5, covered by operator item 1). A same-uid process while the driver
   runs stays residual: between the byte check and a git call it can
   edit `config` or add an alternates file, and between the fetch and the
   ancestry test it can move the trunk ref; a changed object still
   fails its read. A compiled file swapped between the pre-spawn re-hash and the
   worker's read reaches the worker; the post-stage `snapshot` stops the
   run.

**Operator must accept in writing** (at the `spec` gate; the answer is
recorded verbatim in `asks/`):

1. **Local writes through `bash`.** A worker or a proving command can
   write any file the operator can write. Writes outside the run root
   and the worktrees go undetected.
2. **Network egress through `bash`.** A worker or a proving command can
   read any file the operator can read, including credential files
   that the environment scrub does not cover, and send it anywhere the
   machine can reach. The scrub is hygiene, not a boundary.
3. **Detection after publication.** Workers hold the operator's git
   credentials. A push to another ref, or a non-template ticket or
   comment, is public on the remote before the post-stage check stops
   the run; the check limits how long it goes unnoticed, not whether it
   is published.
4. **The state branch is writable by workers** (run-state revision;
   **accepted in writing by the operator, 2026-10-19**,
   [O17](#questions-for-the-operator); O9's 2026-10-18
   acceptance predates it). Workers and anyone who can push the repo
   can push the state branch, as they can push project-main. During a
   stage the `refs` check and the lease catch it. After the driver
   stops, a push that keeps the hash chain and the genesis commit, and
   names commits on project-main, passes the restore checks: if the
   pusher can also put a `groom.md` or `lld.md` commit on project-main,
   that state can choose the proving and env commands the restored run
   executes with the operator's rights. Only the operator's reading of
   the restore summary, which shows every named commit with its author
   and every commit by another identity, catches it.
5. **The bundle pin follows the toolbox trunk** (review of ed91909;
   **accepted in writing by the operator, 2026-10-19**, with branch
   protection on the toolbox `main`; [O22](#questions-for-the-operator)). The toolbox remote itself
   is fixed: the operator types it at Run prep and at a
   restore, from the off-machine genesis note. But the reviewed ref is
   that remote's trunk, `refs/heads/<bundle.trunk>`, so anyone who can push it, workers included
   when the toolbox is the product repo (as for this chunk), can put a
   commit there that a Run prep or repin takes without a typed SHA,
   whose `scripts/` the driver runs; a Run prep's first pin, an
   ancestor of trunk, is taken on the summary alone. Branch protection
   removes the planted-commit half only while workers' credentials
   cannot bypass it. At a restore, a forged state can
   name any pin on that remote; a pin other than the genesis pin needs
   its full SHA typed back after the diff from the genesis pin is
   shown, so only the operator's reading of that diff catches it.
   O17 accepted item 4 for proving and env commands only.

### Mockups

`none`. No-screen reason: this chunk has no graphical screen. The
console, chat dialogs, and run-root files are the interface; [Console lines](#console-lines) fixes their
text. The operator accepted [ux.md](ux.md) at 021f81d, 2026-10-19.

### Verify

**Per item.**

| Item | Unit | Fixture and integration | Proving commands (Groom writes the final lines) |
| --- | --- | --- | --- |
| 0 | — | A walk-through of the skill's R1–R4 lines on a fixture repo with a bare origin; after item 5 lands, item 5's Run prep test covers R5–R10 | `K1`, `K7`; `test "$(wc -l < skills/sdlc-kickoff/SKILL.md)" -le 250`; `test "$(wc -l < docs/sdlc/run-state.md)" -le 250` |
| 1 | — | `docs/sdlc/fixtures/results/` holds one fixture per error code and three valid examples | `K1` and `K7` from the [writing standard](../../writing-standard.md#checks); `test "$(wc -l < docs/sdlc/stage-result.md)" -le 150`; `ls docs/sdlc/fixtures/results/*.expect.json` |
| 2 | — | `docs/sdlc/fixtures/flows/` holds one fixture per bundle-check code, including each `gate.*` row's counterexample (`gate.trial` and `gate.env` among them), exit `checks`, `extract`, a chunk land, `envSpec`, a valid and an invalid `json sdlc-env` block, and a script without an intake bullet, and `fixtures/bundles/minimal/` | `K1`, `K7`; `wc -l docs/sdlc/bundle-spec.md docs/sdlc/flow-spec.md`: ≤ 150 and ≤ 200 |
| 3 | — | `bundles/sdlc/` follows the spec; rule maps; the S5 claim-condition diff | `K1`–`K7`; `test "$(wc -l < docs/sdlc/bundle-runs.md)" -le 150`; `node packages/sdlc-driver/src/cli.ts check bundles/sdlc`, which needs G5's bundle check on project-main, hence the land order in [Groom split](#groom-split-proposal) |
| 5 | `node:test` per module: strict reader, result and candidate rules, front matter, bundle check, labels, groom parser, facts, scan, console | Every fixture under `docs/sdlc/fixtures/`; driver tests with the fake worker against a temporary bare origin with a `local` tickets branch | `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check` (`tsc -p . && node --test`); `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200` |
| 7 | Argv, env, and worker-config builder (permission rules per persona; read-only personas get no edit tool); preflight; worker plugin with a fake plugin API: path guard for `write`, `edit`, and `apply_patch` (links, `..`, `.git`, `~`), `sdlc_write`, `sdlc_result` on the shared fixtures, the three compaction hooks, `shell.env` | The item 5 driver suite through the OpenCode adapter against a fake `opencode` that records argv, env, and the worker config | `npm --prefix packages/opencode-sdlc ci && npm --prefix packages/opencode-sdlc run check`; acceptance runs the OpenCode checks below, O-T1–O-T10 first |
| 6 | Argv and env builder; worker extension with a fake extension API: path guard (links, `..`, `.git`, `~`), `sdlc_write`, `sdlc_result` on the shared fixtures, compaction summary | Plugin and adapter against a fake `pi` that records argv and env | `npm --prefix packages/pi-sdlc ci && npm --prefix packages/pi-sdlc run check`; acceptance runs the Pi checks below first |
| 4 | — | Following the skill produces a bundle under `docs/sdlc/fixtures/bundles/authored/` that passes the check | `K1`, `K7`; `node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/authored` |
| 8 | — | A followed-mode walk-through of `fixtures/bundles/minimal/` writes run folders whose results pass `sdlc-driver validate` | `K1`, `K7`; the validate lines |

**Fake worker** (item 5, `test/fake-worker.ts`). The test adapter starts
it as the worker process with the `WorkerSpec` in its environment. A
JSON script, keyed by persona and run number, lists its actions: write a
file through the same rules as `sdlc_write`, write a candidate, run git
commands in its worktree, run the `local` write recipe against the
fixture tickets branch, sleep, exit with a code, or misbehave: write
outside the writable set, edit `driver.json`, push project-main, push
another branch, rewrite pushed history, move the ticket to `done`, post
a comment that differs from the template, edit another ticket or a
ticket body, skip the extension marker, write no candidate, or hang. It
records its argv and environment.

Driver scenarios, each a test:

1. Happy path through a two-item flow with a blocker; dispatch order;
   both items reach `done`, so the `project-main` check passes after
   each land (L8 sets `projectMainSeen`; `lands` is excluded).
2. Proving command failure, `repair N/3` lines, budget exhaustion on the
   third failed fix, and the land-red event counting exactly once.
   Resuming a budget stop resumes `builder-<suffix>` with the pending
   `test-failure` or `fix` prompt, and the next failed fix stops again.
3. Invalid candidate, repair in a new run folder, valid; the invalid
   run does not enter steps 8–11 (no push, no design-record commit).
   Invalid twice → `invalid result after repair` at step 7; a driver
   killed during the repair run restarts with `invalidRepairs: 1` and
   stops on the next invalid result.
4. Manager `resume`, `defer`, `escalate`; manager invalid → driver-written
   ask; operator-only stops reject `resume`.
5. Gate answer writes `operator/run-N/result.json` with
   `evidence.kind: model` and routes; `trial-gate` `trial` writes
   `trial-kickoff.md` and prints its path; a missing heading stops.
   Paperwork `posted` passes candidate rule 2.
6. Land: tip unchanged; tip moved → clean (row 1, `tip merged clean`) →
   done; tip moved → conflict or a different tree (row 2, `tip merged,
   conflicts resolved`) → verifier, then reviewer, all labelled `Land`,
   with a green prove printing no line; clean then a fix → Review with
   `reviewBase` at the clean commit; builder `blocked` on merge; push
   rejected by a concurrent push → L1; push rejected by a pre-receive
   hook with the tip unchanged → L7x, whatever the hook prints;
   post-land verifier `fail`.
7. Each post-stage check fires on its misbehavior, including `refs`,
   `tickets` (comment text, other ticket, ticket body, commit message),
   and `extension` (no marker → `check failed: extension`, no repair).
   A command stage gets the same run folder, `inFlight`, and snapshot,
   and skips the worker-only checks.
8. Crash: kill the driver mid-stage, model and command, restart,
   `interrupted.json`, found report, next run number.
9. Missing session file → rehydrate: the start line says `rehydrated`,
   `prompt.md` names the compiled file and holds the latest `state.md` and the
   pending prompt kind; a second loss before a valid result →
   `lost-session` ask → `replace` mints with `rehydrate`. A present but
   damaged file → `lost-session` at once. With `backup.dir` set, a
   matching backup is restored and resumed; a backup with another hash
   is ignored and the persona rehydrates.
10. Proving commands edited in the item worktree have no effect; a
    `groom.md` changed after review stops ticket filing.
11. First start creates `repo.git` and `worktrees/integrate` before any
    fetch; a `run.json` with `backend: linear` is refused at start; a
    changed harness tree hash stops the start.
12. A design record with a credential-shaped line → `scan-secret`, no
    `allow`; the console and ask name file, line, and class, never the
    text. A path hit → `scan-hit`, `allow` commits.
13. A proving command and a worker see none of the denylisted
    variables.
14. A bundle commit outside the toolbox trunk shows the full SHA, the
    ancestor result, and the `scripts/` and persona hashes; the answer
    must equal that SHA. A script that has not cleared INTAKE stops the
    start first, including a script whose record exists only in the
    bundle commit's own `docs/INTAKE.md`.
15. Tickets check (N1): a `state` outside the enum, an `assignee` set
    to another label, a malformed `updated`, a commit with another
    author or committer, a credential-shaped line in ticket front
    matter, and, for `file-tickets`, an extra key, a second ticket for
    one groom item, a re-filed item, and a body that differs from the
    reviewed section each fail.
16. Paperwork: the HLD stage ends (`end` appended, `inFlight` cleared,
    `chunk.pendingRoute` set) before paperwork starts; killing the
    driver during paperwork replays it in a new run folder and routes
    by the stored `choice` after `posted`.
17. A worker whose harness tree changed after start fails the pre-spawn
    `harness` re-check without spawning: once for an edited file, once
    for an added file, and once for a removed file.
18. Crash after a design-record push: a hook kills the driver after the
    Spec push returns `0`, before pipeline step 11. The restart passes
    `snapshot` against the ledger although the driver changed
    `driver.json`, `index.jsonl`, `driver/console.log`, `driver/lock`,
    and `driver/harness-tree.json` after the snapshot; passes `refs` and
    `worktrees` under the pushed case; writes `recordCommit` into
    `interrupted.json`; sets `chunk.unposted`; re-runs Spec, which stages
    nothing; sets `pendingRoute`; runs paperwork; routes after `posted`.
    A re-run `stop` leaves `chunk.unposted` for the next `pass`. Each
    stops with `check failed`: project-main at another commit;
    project-main at `C` with another ref moved; `worktrees/integrate`
    elsewhere or dirty; a kill before the ledger write of `C` starts, or
    between its `next` write and file write. A kill between file write
    and promotion, or after the write and before the push, takes the
    not-pushed case and the re-run commits its own record. **Worker
    push:** a Spec worker's `bash` pushes a descendant of the snapshot
    tip, leaves `worktrees/integrate` clean there, writes the SHA into
    `meta.json`, and kills the driver: the ledger passes, `C` is `null`,
    `meta.json` is not read, and `worktrees` or `refs` stops the start;
    Spec does not re-run. The same attack that also writes `C` into
    `driver.json` fails the ledger check first
    (`driver file changed outside the driver: driver.json`).
19. Driver-file ledger: in one stage the driver appends the start line
    and `project-main` writes `projectMainSeen`, and `snapshot` passes.
    A worker that edits `driver.json` (an `items.*.repairs` value) fails
    `snapshot` naming `driver.json`, although `project-main` rewrites the
    file after that check; so does a worker that appends a line to
    `driver/console.log`, truncates `index.jsonl`, adds a file under
    `asks/`, or edits the copy under `driver/worker-ext/`. A worker that
    edits `driver.json` and then kills the driver: `/sdlc` refuses the
    run root with `driver file changed outside the driver: driver.json`
    and records no answer. A kill between the ledger's `next` write and
    the file write, and one between the file write and the promotion,
    each restart with the ledger check passing. An answer that `/sdlc`
    records while no driver runs passes the next start.
20. Durable state at `pushed`, against a temporary bare origin: a commit
    and push at each stage start (with `inFlight`) and end; only **D**
    files in the tree; `sdlc-state.json` lists each file's hash; a
    `result.md` with a run-root path → `state-scan`, `exclude` keeps it
    local and lists it; a credential-shaped `state.md` line →
    `state-secret` with no `allow`; a `run.json` or `driver.json` hit
    offers no `exclude`; an `env-evidence.json` excerpt and a
    `result.md` line holding a 6-character `passEnv` value → the value
    is replaced in the first and is a `credential` hit in the second; a
    300 KiB or binary `out/` file → `skipped`; a failed-check run's
    `state.md` and `out/` are not mirrored, and an interrupted run's
    neither; an unchanged `excluded` or `skipped` file makes no persist
    at the next Start, and a `skipped` file cut below 256 KiB is
    mirrored at the next persist; a worker push to the state branch → `check failed: refs`;
    a second driver on another run root that pushed first →
    `state lease lost`, and the first exits; an unreachable origin at
    Start → `state lease unknown`.
21. Restore and drill: `drill` passes right after `state-init` and
    after a stage end, and `driver/state.json` is in no state commit;
    the first persist after a restore passes its step 1; restoring into
    a new root and typing the genesis and tip resumes at the same node
    with every item worktree recreated at `lastPushed`; a state tree with
    an edited file, a missing file, or a broken `prev` chain is refused;
    a `groom.frozenCommit` or `env.specCommit` not on project-main →
    `check failed: state-commits`, at restore and at Start; a commit by
    another identity is listed; a wrong genesis or tip starts nothing;
    the summary shows the `run.json` summary and `runJsonSha256` is
    recorded only after the answer; `local` restores from `repo.git`;
    `plain` skips the drill. Gather's `persist` puts the brief on the
    branch before the first `/sdlc`. A kill between a state commit and
    its tip-record write → the next Start adopts `HEAD` and persists; a
    `HEAD` whose parent or `seq` does not match → `check failed: state`.
    A restore re-clones `bundle.remote` at the pin only after the typed
    remote and compiles files with the restored hashes; a remote without
    the pin → `check failed: toolbox`; a typed remote that differs from
    the restored one, or a restored `bundle.remote` of `ext::`,
    `file://`, or a local path, starts nothing and clones nothing; a
    restored pin other than the genesis pin needs its full SHA typed
    after the diff is shown. The drill writes nothing outside `<tmp>`,
    also when it fails.
22. Toolbox copy and compiled files: compiled files are identical
    across two run roots and name no absolute path; a deleted compiled
    file is compiled again at Start with the same hash; a mint prompt
    names the absolute path; a repin that changes a skill sends
    `# Compiled update` to the live session once. A `bash` write under
    `toolbox.git/` or `compiled/` during a stage fails that stage's
    `snapshot` check. While the driver is down: an edited compiled file
    → the ledger check; `core.fsmonitor` or `url.*.insteadOf` added to
    `toolbox.git/config`, an edited `HEAD`, or an `alternates` or
    `info/attributes` file → `check failed: toolbox`, and the fsmonitor
    command never runs; a replaced loose object file → `toolbox` at the
    read; a `run.json` `bundle.remote` other than `bundleRemote` →
    `toolbox`; a compiled file swapped after Start, before a spawn →
    that stage does not spawn. While the driver is down, a commit added
    to the copy and named by `run.json` `bundle.commit`, with
    `driver.json` and the ledger rewritten to agree → `toolbox` at the
    next Start's step 4, before any script runs; a `commit-graph`,
    `multi-pack-index`, `shallow`, `info/grafts`, or `refs/replace/`
    file → `toolbox` at step 1, before any git command; an unreachable
    toolbox remote at Start → `toolbox` naming the fetch. A remote whose
    `HEAD` names another branch → the copy holds only
    `refs/heads/<bundle.trunk>`. Run prep runs no git against a toolbox
    remote before the operator types it, and refuses an `ext::`, `fd::`,
    `file://`, local-path, or `-`-leading-host `bundle.remote`, and git
    older than 2.32. The drill fails when its copy's `config` or `HEAD`
    hash differs from `driver.json` `toolbox`. No toolbox read runs
    `git cat-file`.
23. Env-prep on a fixture LLD with one fake dependency: env branch,
    `env-prove` runs toolchain, `setup`, `start`, `ready`, `reset`, then
    `prove`; a red baseline takes `known` and reaches the env-verifier;
    an env-verify `fix` counts on the chunk's repair counter; `env`
    gate `accept` lands with a `Reviewed-by` trailer, deletes the env
    branch, and re-renders compiled files with the `test` line; Groom
    starts only then. An edited block after the gate → `fail`,
    `operator` stop. A `passEnv` variable reaches the command stage and
    no worker.
24. Re-entry: a builder's `env-capability:` stop → `env-capability` ask;
    `env` re-enters `env-prep` while the item waits, the env land
    returns to `@items`, and the builder resumes with the land commit;
    `spec` re-runs Spec, security, and the `spec` gate first; a
    dependency whose `ready` fails before an item's proving commands →
    `environment not ready`, no repair counted.
25. `/sdlc-repin`: refused while a driver runs; refused when a current
    node is gone from the new flow, when the new commit fails the bundle
    check, or when a typed SHA does not match, each leaving `run.json`,
    `driver.json`, and the compiled files at the old pin; otherwise it
    fetches, shows the diff from the checked objects, `bundle.history`
    grows with the tag, the compiled files are compiled again, and the
    next start uses the new pin. A kill in step 4, in each of the three
    cases: `repinPending` set and `run.json` at the old pin → the next
    Start clears the marker and prints `repin interrupted`; set and
    `run.json` at the new pin → the next Start does the combined
    `driver.json` write and compiles the new files; already clear → the
    next Start compiles each file whose `pin` differs and each matches
    `compiled`. In every case no git command runs in the copy before
    the toolbox check's steps 1 and 2.

**OpenCode checks** (item 7 acceptance, run first, on the operator's
machine with OpenCode 1.19.3 and one local model; manual, gated by
`SDLC_OPENCODE_SMOKE=1`; they spend no money). Item 7 runs
O-T1–O-T10 from [opencode-server.md](opencode-server.md#trial-checks)
as its first acceptance tests, before any other; each failure switches
to the fallback in that table, and any fallback that names **security**
or the operator waits for that answer. Then:

- O-E2E end-to-end: `smoke/run.sh` builds a fixture product repo (one
  small Node function, a `local` tickets branch, a frozen `groom.md`
  with two items, one blocking the other), seeds a run root at
  `@items`, and runs `src/driver-main.ts` with `bundles/sdlc` under the
  OpenCode adapter. Pass: both items `done` on the tickets branch, in
  order; two land commits on the fixture project-main with
  `Reviewed-by` trailers; every `result.json` passes
  `sdlc-driver validate`; `meta.json` argv shows the `opencode run`
  flags above; each `driver/worker-config/` file holds the persona's
  permission rules; no check failed.

**Pi checks** (item 6 acceptance, after item 7 lands, on the
operator's machine with Pi at the O6 version and one local model;
manual, gated by `SDLC_PI_SMOKE=1`; they spend no money). These run the
Trial questions as tests; each failure switches to its fallback in
[Trial-dependent decisions](#trial-dependent-decisions):

- P1 (T1): `/sdlc` on a fixture run root starts the detached driver, the
  widget shows lines, and the `input` guard holds while it runs.
- P2 (T2): `pi -p "/sdlc RUN_ROOT"` refuses.
- P3 (T3): three resumed passes keep context; a missing session file
  rehydrates (scenario 9), and a damaged one is a `session lost` stop.
- P4 (T4): with a high `reserveTokens` in an isolated
  `PI_CODING_AGENT_DIR`, compaction fires in `-p` mode and the summary
  holds `state.md` and the facts; removing a fact from `state.md` does
  not remove it from the next summary.
- P5 (T5): ten runs of a fixed task; count valid candidates first time
  and after one repair.
- P6 (T6): `write`/`edit` absent for read-only personas; the guard
  blocks writes outside, through a symbolic link, and when the handler
  throws; `sdlc_write` stays in the run folder.
- P7 end-to-end: O-E2E's fixture and pass conditions under the Pi
  adapter, with `meta.json` argv showing the Pi flags above instead of
  the worker-config condition.

**Definition of done**, every item: acceptance on its ticket; the item's
proving commands green; docs current (package READMEs for 5, 7, and 6); one
`CHANGELOG.md` line; rule maps for every edited agent file.

### Land

- project-main: `integrate/solo-dlc`. Land path as in the HLD
  [Chunk record](hld.md#chunk-record): local merge after explicit
  Review, one land at a time, no internal PRs, no force-push.
- Every land commit cites its ticket id and carries
  `Reviewed-by: <reviewer-label> (<verdict>)`. Every `CHANGELOG.md` line
  cites the ticket id and the land SHA.
- This chunk is built with the current SDLC (manager and sub-agents),
  not by the driver it builds.

## Optional

### Trial-dependent decisions

OpenCode, item 7, the first harness: the checks O-T1–O-T10, each with
its chosen design and fallback, are in
[opencode-server.md](opencode-server.md#trial-checks). Pi, item 6, the
second harness, read at 0.73.1:

| Trial | Chosen design | Confirmed in 0.73.1 source | Fallback if disproved |
| --- | --- | --- | --- |
| T1 TUI during a long handler | Detached driver; the handler returns at once; widget and notify show lines; `input` guard | Handlers can spawn children; `setWidget`, `notify`, and `input` events exist. Not confirmed: that the widget timer and `notify` render after the handler returns | Lines only in `driver/console.log`; the handler prints `tail -f RUN_ROOT/driver/console.log`. If T1 instead shows the TUI stays usable during an awaited handler and the operator accepts UX Q1's console reply, item 6 may run `core.run` in process with the same adapter, and record answers from `ctx.ui` while it runs |
| T2 Headless `/sdlc` | Refused: the handler requires `ctx.hasUI` | Yes: `hasUI` is false in `-p` and JSON modes; `pi -p "/cmd"` does reach the handler | None needed |
| T3 `--session` resume | One session file per persona, resumed with `--session`; existence and header check first | Missing file → new session at that path; written after the first assistant message | Keep each item persona's Pi process alive in `--mode rpc` with the same session file, one prompt per pass; idle processes make no model call, so one large-model session still runs at a time |
| T4 Extension under `--no-extensions`; `session_before_compact` in `-p` | `--no-extensions --extension <file>`; custom summary from the hook | Explicit `-e` loads under `-ne`; the hook is fired from the mode-independent session core (read, not run) | Extension not loaded: run workers with an isolated `PI_CODING_AGENT_DIR` whose `settings.json` lists only the worker extension, keeping the `.pi/` refusal. Hook not fired in `-p`: try `--mode rpc` (fallback T3); if it never fires headless, disable auto-compaction in the isolated settings and stop with an `operator` stop when the session nears `contextWindow - reserveTokens`, so the operator can approve a `rehydrate` mint, which carries the same `state.md` and facts |
| T5 Result validity | `sdlc_result` tool with exits as an enum and in-turn errors, plus one driver repair | — (needs the local model) | Below 8 of 10 valid after one repair: ask the operator for another local model or a provider mode that enforces the tool schema; the brief's one-repair limit stays |
| T6 Write controls | `--tools` allowlist, fail-closed path guard, `sdlc_write` | Yes for all three APIs | `--tools` ignored: the path guard alone limits `write` and `edit` to the writable set. Guard ineffective: detection only, reported to **security** as residual. Extension tools missing: read-only personas write their files with `bash` in the run folder; detection covers the rest |

### Clarifications of the HLD made here

1. The merge-tree re-check keeps the pre-merge parents `p1` and `p2`
   (L3, L3c).
2. A `stop` from the architect's paperwork pass is an explicit manager
   stop, `paperwork failed`; its only other exit is the driver-fixed
   `posted`.
3. A merge commit whose tree differs from the clean tree always needs
   Review, whatever the builder's result says.
4. Ticket filing ends with items `ready` and the Epic `in_progress`, per
   [Groom File](../../../docs/sdlc/groom-step.md#3-file) steps 4–5; the
   HLD table says `backlog` ([O3](#questions-for-the-operator)).
5. A push the driver cannot retry is recorded as a command `fail`,
   because the result contract forbids `blocked` for a command; the
   stop kind is still `blocked`.
6. Reserved exits accept `fail` only on driver-authored results.
7. Invalid-result repairs get their own run folder; the invalid run's
   `result.json` is a driver-authored `fail`.
8. Pi's JSON mode exits `0` on a model error (the HLD's exit-1 fact
   holds for text mode); the driver reads `stopReason` from the stream.
9. Prompts go on stdin; worktrees and driver folders use the label
   suffix; `repo.git/` is added to the run root.
10. Workers have no MCP server, so repo tracker recipes must run from
    `bash`: Pi has no MCP client, and the OpenCode worker config lists
    no MCP server.
11. Driven runs support only the `local` backend in this chunk (security
    ruling S1): the HLD's own rule, since only `local` has a no-model
    `read` recipe. The draft clarification on built-in readers is
    withdrawn; the HLD's read-command sentence stands.
12. The HLD's per-item remote-tip compare for the verifier and reviewer
    becomes the `refs` check on every remote ref after every stage, and
    tracker comment text moves from residual to detected by the tickets
    content check (security ruling S3).
13. Scan stops are written by the driver, not drafted by the manager,
    so no ask can quote the hit.
14. Gate results use `evidence.kind: model`, the closer of the
    contract's two kinds.
15. Item 3 (G3) waits for item 5 (G5, or G5a after a split) and lands
    after it. The HLD [Items](hld.md#items) table blocks item 3 on
    item 2 only and runs 3 and 5 in one wave; G3's proving commands run
    G5's bundle check on `bundles/sdlc`, so that check must be on
    project-main first ([Groom split](#groom-split-proposal)).
16. **Harness order: OpenCode first, Pi second** (the operator's
    decision, 2026-10-18). This replaces the Pi-first order in the brief
    and in the HLD (Goals 3, [Items](hld.md#items),
    [Trial question](hld.md#trial-question), and [Open](hld.md#open)'s
    OpenCode server item, now answered by
    [opencode-server.md](opencode-server.md)). Item 7 ← items 3 and 5;
    item 6 ← item 7; items 4 and 8 follow the OpenCode path. Goal 1, Pi
    on one local model, is met at item 6. Where the HLD names a Pi
    mechanism, the OpenCode counterpart in
    [Behavior 6](#behavior-6-harness-plugins-item-7-opencode-first-item-6-pi-second)
    applies to item 7. OpenCode stores a model-written compaction
    summary; the worker plugin replaces it in every request, so "Driver
    facts reach the compaction summary unaltered" holds for what the
    model reads, not for the stored message.
17. G9, Linear for driven runs, is new: the HLD has no such item. It
    comes from security ruling S1 and carries S1 and S2, with its own
    LLD addendum and **security** gate.
18. The OpenCode `/sdlc` takes the run root in a dialog, not as an
    argument, because an OpenCode slash command from a plugin takes no
    argument; the HLD's "the operator runs `/sdlc RUN_ROOT`" becomes
    "picks `/sdlc`, then enters RUN_ROOT" in OpenCode
    ([O10](#questions-for-the-operator)).

Clarifications 19–25 apply the operator's decisions of 2026-10-19 for a
solo operator who runs one harness session at a time.

19. **Run prep first (A).** The one kickoff session becomes a discarded
    Run prep (stage 0) and a kept Gather after it; `sdlc-kickoff` moves
    to item 0 ([Behavior 8](#item-0-sdlc-kickoff-run-prep-gather-restore)).
20. **Toolbox beside the repo (A; toolbox copy 2026-10-19).** No bundle
    or compiled file in a product repo; `/sdlc-repin` is a user
    command, so HLD Goal 4 holds.
21. **Compiled files (A; toolbox copy 2026-10-19).** The mint prompt
    names the [compiled file](#compiled-files) by path; the state keeps
    only hashes.
22. **Durable run state (B).** The run root "is not committed or
    published" no longer holds at `local` and `pushed`
    ([Durable run state](#durable-run-state)); `run.json` splits off
    `machine.json`. The public-repo rule departs from B's default (O12).
23. **Sessions (C).** A missing file is restored or rehydrated without a
    stop; an unloadable one still stops; `rehydrate` replaces `handoff`
    ([Sessions and rehydrate](#sessions-and-rehydrate)).
24. **Build-environment gate (D).** New nodes under existing steps and
    jobs, so the HLD non-goal holds; the general SDLC gets it as
    DER-565 ([Build-environment gate](#build-environment-gate)).
25. **Harness rule (D).** A need beyond the accepted environment is the
    `env capability` stop, never a new harness in the Build loop.
26. **Toolbox copy in the run root (operator, 2026-10-19).** Replaces
    "the driver reads the toolbox checkout at `machine.json` `toolbox`
    with `git show`": each run clones the toolbox remote bare into
    `RUN_ROOT/toolbox.git` and reads it only from the object store at
    the pin; compiled files are `RUN_ROOT/compiled/` driver files
    ([Toolbox copy](#toolbox-copy)). The operator types the remote at
    Run prep and keeps it in the genesis note, and the reviewed ref is
    only that remote's trunk, `refs/heads/<bundle.trunk>`, so a bundle commit only on the toolbox's own
    project-main needs the typed SHA. An earlier draft that put the
    copy in an ignored `.sdlc/` in the operator checkout was dropped
    after the review of ed16411. The general SDLC version, DER-570,
    follows this layout.

### Groom split (proposal)

| G | Item | Blocked by | Reason |
| --- | --- | --- | --- |
| G0 | `sdlc-kickoff` (Run prep, Gather, restore modes) and `docs/sdlc/run-state.md` | — | First in the build order (decision A). Fixes the formats item 5 builds against; R1–R4 work from the skill at once ([O14](#questions-for-the-operator)) |
| G1 | Result format (DER-529) | — | — |
| G2 | Bundle and flow spec, fixtures | G1 | Candidate and `choice` rules extend item 1's fields |
| G5 | Core driver | G1, G2 | Implements both specs; its tests read their fixtures |
| G3 | SDLC bundle (with the env nodes and the `env-builder`, `env-verifier`, `env-reviewer` personas), `test-failure-handler`, tracker wiring, `bundle-runs.md` | G2, G5 | Written in the spec's format. Land order: G5 lands before G3, because G3's proving commands run G5's bundle check on `bundles/sdlc`. Differs from the HLD: [clarification](#clarifications-of-the-hld-made-here) 15 |
| G7 | OpenCode plugin (with `/sdlc-repin` and the restore confirmation), worker plugin, OpenCode checks (O-T1–O-T10 first, then O-E2E) | G3, G5 | First harness: the operator's first tests run in OpenCode. Hosts the core; the smoke runs `bundles/sdlc`. Order: [clarification](#clarifications-of-the-hld-made-here) 16 |
| G6 | Pi plugin, worker extension, Pi checks (P1–P7) | G7 | Second harness. Blocked by G7 so it reuses G7's adapter tests, fake-harness pattern, and smoke fixture, and items stay one at a time. Pi version: O6 |
| G4 | `bundle-authoring` | G7 | After the first harness works |
| G8 | `sdlc-followed-mode` | G7 | After the first harness works |
| G9 | Linear for driven runs: a no-model read recipe for the driver and shell write recipes for workers. Not groomed in this pass: it needs its own LLD addendum and its own **security** gate | G7 | Security ruling S1; carries S1 and S2 (below). Not an HLD item: [clarification](#clarifications-of-the-hld-made-here) 17 |

Waves: 1: G0, G1; 2: G2; 3: G5; 4: G3; 5: G7; 6: G6, G4, G8. G9 is
groomed later, after its own LLD addendum. No gate items. Item 5 is
the largest for a 100k-token builder. Groom may split it into G5a
(strict reader, result and candidate rules, front matter, bundle check;
← G1, G2), G5b (run root, state machine, stage pipeline, stops, fake
worker; ← G5a), and G5c (git, land, proving commands, snapshot, refs
and tickets checks, tracker read, scan; ← G5b). The run-state revision
adds G5d (durable state, lease, restore and drill, `status`, the toolbox copy and compiled files,
rehydrate, session backup, start preflight, repin; ← G5b) and G5e (env
block, env command stages, dependency pre-steps, chunk land, re-entry;
← G5c). With the split, G3 ← G2, G5a (land order G5a before G3), so G3
can build beside G5b–G5e, and G7 ← G3, G5d, G5e; G6 stays ← G7.

**G9 carries** from the security review of 34e1278: S1, the Linear read
key, with the constraints **security** set (the key file's content must
match the `lin_api_` format; the key path and its parents are no
symbolic link; the `run.json` confirmation shows the path; a same-uid
process reading the key is residual); and S2, worker tracker
credentials for Linear on each harness.

### Security rulings (review of 34e1278; N1–N4 from the re-review of de7c438)

| # | Topic | Ruling | Where it lands |
| --- | --- | --- | --- |
| S1 | Linear read key | Out of this chunk; driven runs are `local` only; Linear is G9 with its own gate | [`run.json`](#runjson), [Tracker reads](#tracker-reads-no-model), G9 |
| S2 | Worker Linear credentials | Moves to G9 with S1 | G9 |
| S3 | Public `tickets` content; `bash` not path-guarded | `refs` and tickets content checks after every stage; local writes and egress through `bash` are operator-accepted residuals | [Post-stage checks](#post-stage-checks), [Trust boundaries](#trust-boundaries) |
| S4 | Bare clone in the run root, hooks off, `.pi/` refusal | Accepted | Trust boundaries |
| S5 | Same-item claim rule (protected rules) | Diff the claim condition against `adapters/local.md` at Review; contract stays v2 | [Tracker wiring](#tracker-wiring-and-bundle-runsmd) |
| S6 | Scan patterns and `allow` | Credential-shaped hits are revise-only; other hits may be allowed, recorded in `asks/`; text never shown | [Scan patterns](#scan-patterns) |
| S7 | Environment of workers and proving commands | Fixed denylist; hygiene, not a boundary; proving lines only from the frozen blob and pinned defaults | [Environment scrub](#environment-scrub) |
| S8 | Pinned `typescript` dev dependency | Accepted | Trust boundaries |
| S9 | Bundle commit outside reviewed history | Full SHA, ancestor results, `scripts/` and persona hashes shown; the SHA typed back; `scripts/` clear INTAKE | [`run.json`](#runjson), [Bundle layout](#bundle-layout-and-bundlemd) |
| N1 | Tickets content (re-review of de7c438) | State enum, assignee, strict `updated`, exact key set for filed tickets, one ticket per groom item, no re-filing, whole-file scan, filed body equals the reviewed and scanned section on project-main, driver-set author and committer | [Tickets content check](#tickets-content-check) |
| N2 | Reviewed refs | Derived by the driver, never read from `run.json`; any other ref named forces the typed SHA | [`run.json`](#runjson) |
| N3 | INTAKE record for an unreviewed bundle commit | Record and hash must be in `docs/INTAKE.md` at a derived reviewed ref; one inside the bundle commit does not count | [Bundle layout](#bundle-layout-and-bundlemd) |
| N4 | Low residuals | Local refs, no fetch; `treeSha256` re-checked per spawn from a stat cache; `harness.node` not hashed | [Trust boundaries](#trust-boundaries) |
| Run state | Changes from the run-state revision, 2026-10-19 | S7 widened for `passEnv` (command stages only; values scanned); TB10 adds the env and state branches and the env branch deletion; TB13's "run root never published" no longer holds at `pushed`; TB12 adds the env block; TB14–TB18 are new; operator item 4 is a new residual. All await **security**'s re-read | [Trust boundaries](#trust-boundaries) |
| Harness pin | Harness supply chain | npm `integrity` recorded at install; `treeSha256` (binary hash, or package-tree hash) recorded in `run.json` and checked at every start. Ruled for Pi; OpenCode 1.19.3 (binary hash; integrity of `opencode-ai` and its platform package; self-update off) follows the same ruling and awaits **security**'s re-read. Pi 0.73.1 or 1.x is O6 | [`run.json`](#runjson), [Start](#start) |

### Questions for the operator

| # | Question | Recommendation |
| --- | --- | --- |
| O1 | Run a Trial before Build? | **Accepted by the operator, 2026-10-18: no separate Trial.** Every harness fact sits behind the adapter and the worker plugin or extension, so a fallback changes item 7 or item 6, not item 5's shape. Item 7 runs O-T1–O-T10 first; item 6 runs T1–T6 as P1–P6 first |
| O2 | UX Q1–Q3 | Accept the recommended defaults this LLD assumes: replies at the next `/sdlc` (Q1); the handoff block in [Behavior 8](#items-4-and-8) (Q2); `index.jsonl` (Q3) |
| O3 | Ticket filing end state: Groom says `ready` and Epic `in_progress`; the HLD table says `backlog` | Follow Groom; the HLD row gets a clarification |
| O4 | Same-item claim rule: contract v2 or v3 | Settled by security ruling S5: v2, with Run prep checking the repo skill for the same-item sentence. No answer needed |
| O5 | Linear for driven runs | Driven runs use `local` only in this chunk. Linear, driver reads and worker writes, becomes G9, blocked by G7, with its own LLD addendum and security gate; it carries S1 and S2. Accept |
| O6 | **Open; gates only G6, the second harness.** Pi version: `@mariozechner/pi-coding-agent` 0.73.1 (every Pi fact here was read in it; the registry marks it deprecated) or `@earendil-works/pi-coding-agent` 1.x (the maintained line; facts not yet checked). G7 pins OpenCode 1.19.3 and does not wait for this answer | Pin 0.73.1 for G6. Record npm `integrity` at install and `treeSha256` in `run.json`; check `treeSha256` at every start. The Pi facts table and the T1–T6 fallbacks were read at 0.73.1. Moving to 1.x is a later item that re-reads the facts table at 1.x and reruns P1–P7. If the operator picks 1.x now, G6's first task is that re-read; nothing else in this LLD names the package |
| O7 | Skill ids `test-failure-handler`, `bundle-authoring`, `sdlc-followed-mode`, `sdlc-kickoff`. **Changed 2026-10-19:** `sdlc-kickoff` is item 0 with three modes (Run prep, Gather, restore) | Accept; the id stays, so no route changes |
| O8 | Item 5 split into G5a–G5c. **Changed 2026-10-19:** G5d and G5e added | Let Groom split it; with the split, G3 waits only for G5a |
| O9 | Operator items 1–3 under "Operator must accept in writing" in [Trust boundaries](#trust-boundaries) | **Accepted in writing by the operator, 2026-10-18: "Risks are acceptable."** That answer covers items 1–3 only; item 4 was accepted in writing as [O17](#questions-for-the-operator), 2026-10-19. The three residuals do not depend on the harness, and OpenCode first adds none to them; its new items are listed for **security** under Trust boundaries. Removing them needs a sandbox for `bash` and network, which the HLD lists as a non-goal |
| O10 | In OpenCode, `/sdlc` takes the run root in a dialog instead of as an argument ([clarification](#clarifications-of-the-hld-made-here) 18); Gather prints the run root and "pick `/sdlc`, then enter RUN_ROOT" ([item 0](#item-0-sdlc-kickoff-run-prep-gather-restore)), and the OpenCode [Summary console line](#console-lines) ends `pick /sdlc, then enter RUN_ROOT to continue`. Pi keeps the typed `/sdlc RUN_ROOT` in both. **Changed 2026-10-19:** Gather, after Run prep, prints the start line | Accept. A plugin slash command in OpenCode 1.19.3 takes no argument, and typed `/sdlc RUN_ROOT` would reach the model; the dialog keeps the start model-free |
| O11 | If O-T8 fails, OpenCode cannot stop the operator's own prompt while a worker runs: one large-model session at a time becomes the operator's discipline in that session, with a toast and the console warning | Accept that fallback for item 7 only, decided now so item 7 does not stop on it. A second session costs speed or memory on the local model; it does not skip a gate or a check. Item 6 keeps Pi's enforced `input` guard |
| O12 | Durability on a public repo: at `pushed` the state branch, with the brief, prose, and verbatim answers, is public. **A deviation from decision B**, whose default is `pushed` everywhere | **Accepted by the operator, 2026-10-19, as recommended.** Confirm the deviation: no default on a public repo; Run prep warns and the operator picks `pushed`, `local`, or `plain`. A separate private remote for the state branch is a later item; it would need a second credential and a second `refs` baseline |
| O13 | Standard 9 exceptions: the new `docs/sdlc/run-state.md` at ≤250 lines, and `docs/sdlc/flow-spec.md` at ≤200 for the env block, chunk land, and re-entry. Driver-only formats go to `packages/sdlc-driver/README.md` (≤200) instead | **Accepted by the operator, 2026-10-19, as recommended.** Accept both. The run-state rules take about 200 lines even at one or two lines each; `bundle-runs.md` keeps the rule changes within 150. The alternative, two new `docs/sdlc/` files of ≤150 (formats and state), adds a file and a route for no reader |
| O14 | Item 0 lands first, but `readiness`, `state-init`, `drill`, `persist`, `status`, `restore`, and compiling need item 5's code | Accept: item 0 fixes the procedure and formats as items 1 and 2 fix theirs; R1–R4 work from the skill at once; R5–R10 and the full Run prep are tested in item 5 |
| O15 | Who removes the state branch, and when | The operator, after project-main lands on trunk; the driver never deletes it and says so at `@done`. Keep an archive tag only when audit needs it |
| O16 | An env re-entry whose LLD change needs new or changed items, whose proving commands are frozen | Out of scope for this chunk: the `env-capability` ask offers `defer`, and the operator amends Groom by hand or opens a new chunk. A driven Groom amendment is a later item |
| O17 | **Accepted in writing by the operator, 2026-10-19 (residual accepted).** Accept in writing operator item 4: anyone who can push the repo, workers included, can write a consistent forged state that, with a commit planted on project-main, chooses the proving and env commands a restored run executes; the restore checks narrow it to project-main commits and the operator's reading of the summary | Accept. Per-branch credentials are not generally available (as for the tracker); branch protection on project-main, where the host offers it, removes the planted-commit half. The alternative, a separate state remote, is O12's later item. **Scope, 2026-10-19 (review of ed91909):** this acceptance covers proving and env commands; the bundle pin, which the pinned-clone revision moved to the toolbox remote, is [O22](#questions-for-the-operator) |
| O18 | The `env` gate: operator acceptance after the agent gate (env-verifier and env-reviewer), or the operator alone | **Accepted by the operator, 2026-10-19, as recommended.** Agent gate, then operator acceptance, as designed: the agents check evidence line by line and the security reads; the operator accepts what every later check will trust |
| O19 | `passEnv` values reach command stages only, so a builder cannot run integration tests that need them in its own worktree | Accept: builders run unit tests and the dependencies the env started; the proving commands run the integration tests. Giving builders the values would widen what a worker's `bash` can send |
| O20 | The genesis anchor: a restore needs the genesis state commit from the operator's own note, kept off the machine | **Accepted by the operator, 2026-10-19, as recommended.** Accept: Run prep prints it once, with the toolbox remote the operator typed there and the trunk, which the note now also holds (reviews of ed91909 and 0047da2). A lost note blocks a restore; the operator then reads the genesis from an independent clone they trust, and the restore summary shows it for comparison. Without the anchor a wholly foreign state branch would pass on trust-on-first-use |
| O21 | **Open.** Each run has its own run root, and with it its own bare product clone (`repo.git`), worktrees, toolbox copy, compiled files, and state branch `sdlc/run/<chunk-slug>`; nothing of a run sits in the operator's checkout. Two runs share only the product remote (project-main differs per chunk; the `tickets` branch is shared), the operator's model capacity, and the operator. How many runs may be active at once? | (a) **One run per chunk slug, chunks in parallel.** A second run root for a slug whose state branch exists is refused at `state-init`. Pro: no new mechanism; the lease and the state branch already key on the slug; parallel chunks cost only disk. Con: two drivers push the shared `tickets` branch, so one can see a rejected fast-forward (never a force); two local-model workers contend. (b) **One active driver per machine**, through a lock under `$XDG_STATE_HOME/sdlc/`. Pro: matches one operator and one local model. Con: a new lock outside every run root, and an idle chunk blocks another. (c) **No rule.** Pro: nothing to build. Con: two run roots on one slug race on the state branch until the lease stops one. **Recommend (a)**: the run root already isolates everything local; the shared remote is what a solo operator already has across chunks, and O11 covers model contention in the operator's own session |
| O22 | **Accepted in writing by the operator, 2026-10-19; branch protection is on for the toolbox `main`.** Accept in writing operator item 5: the toolbox remote is fixed by the operator's typed URL and off-machine note, but anyone who can push its trunk, workers included when the toolbox is the product repo, can put a commit on the reviewed ref; and at a restore a forged state can name another pin on that remote, which the operator must read as a diff from the genesis pin before typing its full SHA; a Run prep's first pin on trunk is taken on the summary alone | Accept, with branch protection on the toolbox trunk. The reviewed ref is `refs/heads/<bundle.trunk>`, `main` unless Run prep's operator names another, which then needs the same protection; the remote's `HEAD` is never read, and every Start re-fetches that ref and re-checks the pin on it (review of 0047da2). Protection removes the planted-commit half as it does for O17 while workers' credentials cannot bypass it. The alternatives, typing the full SHA at every Run prep and repin, or a toolbox remote workers cannot push, cost a 40-hex entry per pin or a second credential for a residual the diff already shows |

### Rollout / rollback

The chunk adds new files and routes; existing runs that use sub-agents
are unaffected except by the same-item claim rule, which applies only
inside bundle runs. Rollback is reverting the items' land commits on
project-main before Trunk; run roots are outside git and need no
cleanup. State branches never reach project-main or trunk; the operator
removes them ([O15](#questions-for-the-operator)).
