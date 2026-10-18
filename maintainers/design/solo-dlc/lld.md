# LLD — solo-dlc: the SDLC on a harness without sub-agents

- Slug: `solo-dlc`
- HLD: [maintainers/design/solo-dlc/hld.md](hld.md) (agent review passed
  in round 4; operator acceptance pending). UX: [ux.md](ux.md); stories:
  [user-stories.md](user-stories.md); comparables:
  [comparables.md](comparables.md). Brief: DER-421 brief v3, confirmed
  2026-10-18.
- Tickets this LLD covers: DER-421 (chunk); brief items 1–8 (item 1 is
  DER-529; the others get ids at Groom)
- Date: `2026-10-18`
- Status: **draft, awaiting security review and operator acceptance.**
  Architect acceptance is this draft. Groom and Build start only after
  **security** and then the operator accept it
  ([Security gate](../../../docs/sdlc/plan-trial-spec.md#security-gate)).
- Spec entry gate: the offline `tracker-sdlc` setup check passed on
  2026-10-18 (`maintainers/AGENTS.md` `## Tracker` names
  `.agents/tracker/SKILL.md`; that file says `Contract: tracker-sdlc v2`).
- Trial: not run. Every fact the HLD marks for the Trial (T1–T6) has a
  chosen design and a fallback in
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
  a candidate: command stages, gate nodes, failed checks, invalid
  results after repair.
- **Pinned commit**: the skills-home commit recorded in `run.json`.
  The driver reads `flow.json`, personas, and packed skill bodies only
  from that commit, never from a working tree.

## Required

### Paths / modules

| Path | Item | What |
| --- | --- | --- |
| `docs/sdlc/stage-result.md` | 1 | Edited in place: v1 fields, rules, examples |
| `docs/sdlc/fixtures/results/` | 1 | Valid and invalid result fixtures, each with an `.expect.json` |
| `docs/sdlc/bundle-spec.md` | 2 | Owner: bundle layout, `bundle.md`, persona files, prompt kinds, placeholders. ≤150 lines |
| `docs/sdlc/flow-spec.md` | 2 | Owner: `flow.json`, exits, reserved exits, candidate rules, bundle check, error codes. ≤150 lines |
| `docs/sdlc/fixtures/flows/`, `docs/sdlc/fixtures/bundles/` | 2 | Flow and bundle fixtures with expected error codes |
| `docs/sdlc/bundle-runs.md` | 3 | Owner of every rule change in [HLD Rule changes](hld.md#rule-changes), plus run-root formats for agents. ≤150 lines |
| `bundles/sdlc/` | 3 | The SDLC bundle: `bundle.md`, `flow.json`, `personas/*.md` |
| `skills/test-failure-handler/SKILL.md` | 3 | New first-party skill, `SOURCES.md` row |
| `skills/tracker-sdlc/SKILL.md`, `adapters/local.md` | 3 | Same-item claim rule (protected rules: rule maps, **security** read) |
| One-line routes in `docs/SDLC.md`, `docs/sdlc/subagents.md`, `build-review.md`, `branches-and-lands.md`, `plan-trial-spec.md`, `stage-result.md`, `skills/debug/SKILL.md` | 3 | Each route names the rule and links `bundle-runs.md` |
| `packages/sdlc-driver/` | 5 | Core driver: TypeScript, Node built-ins only, no Pi dependency |
| `packages/pi-sdlc/` | 6 | Pi plugin: `/sdlc`, the Pi adapter, the detached driver entry, the worker extension, the smoke test |
| `skills/bundle-authoring/SKILL.md` | 4 | New skill |
| `packages/opencode-sdlc/` | 7 | OpenCode plugin, hosting the same core |
| `skills/sdlc-followed-mode/SKILL.md`, `skills/sdlc-kickoff/SKILL.md` | 8 | New skills |
| `CHANGELOG.md` | all | One line under `## Unreleased` per item |

Final skill ids, fixed here: `test-failure-handler`, `bundle-authoring`,
`sdlc-followed-mode`, `sdlc-kickoff`.

**Where bundles live.** In the skills home, at `bundles/<bundle-id>/`.
A run pins one skills-home commit; a product repo never carries a copy.
A third-party bundle is copied into `bundles/<id>/` only after
[INTAKE](../../../docs/INTAKE.md).

**Package layout.**

```text
packages/sdlc-driver/          # core; no runtime dependency; no Pi import
  package.json                 # private; "type": "module"; engines node >=22.18
  tsconfig.json                # strict; erasableSyntaxOnly; noEmit
  README.md
  src/
    index.ts                   # public API: prepare, run, checkBundle, validateResult
    cli.ts                     # `check BUNDLE_DIR [--at COMMIT]`, `validate RESULT --flow F --node N`
    json.ts                    # strict JSON reader (duplicate keys, nulls, trailing text)
    result.ts                  # stage-result v1 and candidate rules
    flow.ts  bundle.ts  check.ts   # flow types, bundle loader (git show at pinned commit), bundle check
    frontmatter.ts             # persona front matter subset parser
    runroot.ts                 # run.json, driver.json, index.jsonl, asks/, run folders, lock
    machine.ts                 # pure state machine: (state, event) -> (state, actions)
    stage.ts                   # stage pipeline: prompt, facts, snapshot, worker, validate, checks
    land.ts                    # land sub-machine, merge-tree classification
    prove.ts                   # command wrapper
    git.ts                     # git calls: hooks off, replace objects off, no force option
    snapshot.ts                # pre/post hashes, worktree and remote checks
    tracker/local.ts  tracker/linear.ts
    groom.ts                   # frozen groom.md parser
    prompts.ts  facts.ts  scan.ts  console.ts  labels.ts
    adapter.ts                 # HarnessAdapter interface
  test/                        # node:test; fixtures from docs/sdlc/fixtures; fake worker
packages/pi-sdlc/              # Pi plugin, a Pi package
  package.json                 # "pi": {"extensions": ["./extensions/sdlc.ts"]}
  extensions/sdlc.ts           # registers /sdlc and /sdlc-stop; input guard; widget
  src/pi-adapter.ts            # HarnessAdapter for Pi: argv, env, process groups
  src/driver-main.ts           # detached driver entry: core.run(RUN_ROOT, piAdapter)
  src/pi-types.ts              # hand-written minimal types for the Pi API used
  worker/sdlc-worker.ts        # worker extension; self-contained; NOT in the manifest
  test/                        # node:test with a fake `pi`
  smoke/                       # end-to-end smoke on real Pi; manual
packages/opencode-sdlc/        # item 7: HarnessAdapter for OpenCode
```

The worker extension is not listed in the Pi package manifest, so the
operator's own Pi session never loads it. `src/pi-types.ts` replaces a
dev dependency on the Pi package; the smoke test checks it against real
Pi.

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
| `ticket` | string | Matches `^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$`. The id the repo tracker skill returns, on any backend, including `local`. Chunk-scope stages use the Epic id. The harness fixes it from the invocation; a mismatch is a failure |
| `artifact` | string | One path relative to the run root. Segments match `[A-Za-z0-9._-]+`; no `.` or `..` segment, no leading `/`, no `\`. It names the result document or the output folder in the stage's own run folder; a folder ends with `/`. Absolute, outside the run root, outside the stage's run folder, or missing: failure |
| `evidence` | object | As today |
| `findings` | string | As today |

Rules added to the Rules section:

1. **Stage harness** fixes `schemaVersion`, `step`, `ticket`, and
   `evidence.kind` from the invocation.
2. A command stage's `choice` is set by the command wrapper: the node's
   `pass` exit when `exit_code` is `0`, else its `fail` exit.
3. `artifact` of a command stage names its `commands.json`.
4. Out of scope: the line now says the flow file and `choice` routing
   are in `docs/sdlc/flow-spec.md`.

Example:

```json
{"schemaVersion": 1, "step": "Build", "status": "pass", "choice": "review",
  "ticket": "DER-530", "artifact": "verifier-der-530/run-3/result.md",
  "evidence": {"kind": "model", "checks": ["dod: acceptance bullets 1-4 hold"]},
  "findings": ""}
```

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
  `## Modes` (`enforced`, `followed`, or both).
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
| `tools` | yes | Subset of Pi's built-in names `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`. With `readOnly: true`, no `edit` or `write` |
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
`{{stopRun}}`, `{{question}}`, `{{choices}}`, `{{answer}}`, `{{record}}`.
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
| `scope` | all | `chunk` or `item`. `land` is `item` |
| `persona` | `model` | A persona id with the same scope |
| `skills` | `model` | Optional. Packed the first time this persona runs this node |
| `outputs` | `model`, chunk | Optional. Repo-relative paths; `{design}` expands to `run.json` `repo.designDir` |
| `outputDirs` | `model`, chunk | Optional. Repo-relative folder prefixes ending `/`; every regular file the persona puts there is committed |
| `checks` | `model` | Optional. Required check names, `^[a-z][a-z0-9-]{0,31}$` |
| `commands` | `command` | `"groom"` (the item's proving commands) or an array of `scripts/<file>` paths |
| `gate` | `gate` | Tag: `brief`, `ux`, `plan`, `trial`, `mockup`, `spec`, or another `^[a-z][a-z0-9-]{0,15}$` word |
| `ask` | `gate` | The decision in one sentence, for the manager's `ask-human.md` draft |
| `builder`, `prove`, `verify`, `review` | `land` | Node ids: the builder model node, the proving `command` node, the verifier model node, and the Review node |
| `exits` | all | Array of exit objects |

Exit fields: `name` (`^[a-z][a-z0-9-]{0,31}$`, unique per node, never
`stop` or `operator`), `statuses` (non-empty subset of the four),
`to` (a node id, `@items`, or `@done`), and optional `say` (one line the
console prints when the exit is taken; placeholders allowed).

- `@items` ends the chunk phase and starts each planned item at
  `itemEntry`. Only chunk nodes may target it.
- `@done` ends the current scope: for an item, it is landed+verified;
  for the chunk, the run is complete once every item is done.
- `command` nodes have exactly two exits: one with `["pass"]`, one with
  `["fail"]`.
- Each `gate` exit has exactly one status, `pass` or `fail`.
- A `land` node has exactly one exit, `done`, with `["pass"]`, to
  `@done`.

**Reserved exits.** Every node has two exits that no flow lists:

| Exit | Worker may choose it with | Driver-authored results may also use it with | Route |
| --- | --- | --- | --- |
| `stop` | `blocked`, `needs_input` | `fail` | Resume the manager; it may `resume`, `defer`, or `escalate` |
| `operator` | `needs_input` | `fail` | Resume the manager; it may only `escalate` |

A worker candidate with `fail` and a reserved exit is invalid
(`flow.reserved-status`). Driver-authored `fail` results with `operator`
record failed checks and spent budgets.

**Land sub-stage exits.** Inside a `land` node, model and command
sub-stages use these fixed exits, owned by the flow spec, not the flow
file:

| Sub-stage | Exits |
| --- | --- |
| Builder: merge the tip, or fix after a land check | `ready` [`pass`] |
| Verifier: re-run, or post-land | `ok` [`pass`], `fix` [`fail`] |
| Proving commands on the item or on the integration merge | `ok` [`pass`], `fix` [`fail`] |

**Candidate rules.** A worker writes `candidate.json` with the
`sdlc_result` tool or with `sdlc_write`
([Worker extension](#worker-extension)).

1. `schemaVersion`, `step`, `ticket`, and `evidence.kind` may be
   omitted; when present they must equal the invocation's values
   (`flow.fixed-field`).
2. `choice` must be allowed for `status` by the node, or by the land
   sub-stage table (`flow.choice-not-allowed`).
3. `pass` with node `checks`: each name appears as the prefix
   `<name>: ` of one `evidence.checks` entry, followed by a finding or
   `n/a — <why>` (`flow.check-missing`).
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

Any rule failing makes the candidate invalid
([Stage pipeline](#stage-pipeline-model-node) step 6).

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
| B10 | A `land` node names existing nodes of the right kind: `prove` is an item `command` node with `commands: "groom"`; `verify` is a model node with job `verifier`; `review` has step `Review`, job `reviewer`, and `checks` holding `intake`, `sha-pins`, `trust-boundary` | `flow.land-ref`, `flow.review-checks` |
| B11 | Gate rows below hold on every path | `gate.*` |
| B12 | `bundle.md` headings; no symbolic links; size caps | `bundle.layout` |

Gate rows. The checker finds the nodes by kind, step, job, outputs, and
gate tag, so a flow cannot avoid a row by renaming nodes:

| Code | Any path from | Reaching | Must pass, in this order |
| --- | --- | --- | --- |
| `gate.comparables` | `entry` | The HLD node: chunk `model`, step Plan, an `outputs` path ending `/hld.md` | The comparables node: chunk `model`, step Plan, an `outputs` path ending `/comparables.md` |
| `gate.plan` | `entry` | The Spec node: `model`, step Spec, an `outputs` path ending `/lld.md` | The `gate` node tagged `plan` |
| `gate.spec` | `entry` | Any Groom node, or any item node | The Spec node, then the `model` node with step Spec and job `security`, then the `gate` node tagged `spec` |
| `gate.land` | Each `model` node with job `builder` | The `land` node | Its `prove`, `verify`, and `review` nodes |

A row whose target does not exist in the flow holds trivially. A row
whose target exists but whose required node does not is an error.

Algorithm: breadth-first search over pairs (node, k), where k counts the
required nodes passed in order; entering the k-th required node
increments k. Reaching the target with k below the number required is a
violation. The error names the exit used on the last edge into the
target, from the shortest counterexample path. The search is finite
because there are at most nodes × (required + 1) pairs. Stops and the
manager re-run the stopped node, so they add no flow edges. The land
node's internal re-runs reach Review only through its `prove`, `verify`,
and `review` nodes, which are flow edges.

### Behavior 3: the SDLC bundle (item 3)

#### SDLC flow

`bundles/sdlc/flow.json`, `entry: refine`, `itemEntry: build`,
`defaults.prove: []`. `{design}` is `run.json` `repo.designDir`.

| Node | Label | Step | Kind | Persona | Outputs / checks / tag | Exits |
| --- | --- | --- | --- | --- | --- | --- |
| `refine` | Brief | Brief | model | refiner | — | `brief` [pass] → `brief-gate`. Back to Gather: `operator` with `needs_input` |
| `brief-gate` | Brief | Brief | gate | — | tag `brief` | `confirmed` [pass] → `comparables`; `revise` [fail] → `refine` |
| `comparables` | Plan | Plan | model | architect | `{design}/comparables.md` | `hld` [pass] → `hld` |
| `hld` | Plan | Plan | model | architect | `{design}/hld.md` | `ux` [pass] → `ux` |
| `ux` | Plan | Plan | model | designer | `{design}/ux.md`, `{design}/user-stories.md` | `review` [pass] → `ux-review` |
| `ux-review` | Plan | Plan | model | ux-reviewer | — | `accept` [pass] → `ux-gate`; `fix` [fail] → `ux` |
| `ux-gate` | Plan | Plan | gate | — | tag `ux` | `accepted` [pass] → `plan-gate`; `waived` [pass] → `plan-gate`; `revise` [fail] → `ux` |
| `plan-gate` | Plan | Plan | gate | — | tag `plan` | `accept` [pass] → `trial-gate`; `revise` [fail] → `hld` |
| `trial-gate` | Trial | Trial | gate | — | tag `trial` | `trial` [pass] → `trial-done`, say `Trial kickoff prompt: {design}/hld.md#trial-kickoff-prompt`; `skip` [pass] → `spec` |
| `trial-done` | Trial | Trial | gate | — | tag `trial-done` | `done` [pass] → `spec`; `revise` [fail] → `hld` |
| `spec` | Spec | Spec | model | architect | `{design}/lld.md` | `mockups` [pass] → `mockups` |
| `mockups` | Spec | Spec | model | designer | `outputDirs` `{design}/mockups/` | `none` [pass] → `security`; `review` [pass] → `mockup-review` |
| `mockup-review` | Spec | Spec | model | ux-reviewer | — | `accept` [pass] → `mockup-gate`; `fix` [fail] → `mockups` |
| `mockup-gate` | Spec | Spec | gate | — | tag `mockup` | `accepted` [pass] → `security`; `revise` [fail] → `mockups` |
| `security` | Spec | Spec | model | security | checks `authz`, `secrets`, `egress`, `data-class`, `writers` | `accept` [pass] → `spec-gate`; `fix` [fail] → `spec` |
| `spec-gate` | Spec | Spec | gate | — | tag `spec` | `accept` [pass] → `groom`; `revise` [fail] → `spec` |
| `groom` | Groom | Groom | model | architect | `{design}/groom.md` | `review` [pass] → `groom-review` |
| `groom-review` | Groom | Groom | model | groom-reviewer | — | `file` [pass] → `file-tickets`; `fix` [fail] → `groom` |
| `file-tickets` | Groom | Groom | model | manager | `{design}/groom.md` (the frozen copy) | `items` [pass] → `@items` |
| `build` | Build | Build | model | builder | — | `prove` [pass, fail] → `prove` |
| `prove` | Build | Build | command | — | `commands: "groom"` | `verify` [pass] → `verify`; `fix` [fail] → `build` |
| `verify` | Verify | Build | model | verifier | checks `dod` | `review` [pass] → `review`; `fix` [fail] → `build` |
| `review` | Review | Review | model | reviewer | checks `intake`, `sha-pins`, `trust-boundary` | `land` [pass] → `land`; `fix` [fail] → `build` |
| `land` | Land | Build | land | — | builder `build`, prove `prove`, verify `verify`, review `review` | `done` [pass] → `@done` |

A builder `fail` still goes to the proving commands: the commands, not
the builder, decide whether the item goes back. The builder's own `fail`
is not a check sending the item back.

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
| `builder-<suffix>` | builder | item | no | all seven | `tdd`, `yagni`, `debug`, `docs-google-style`, plus the item's `skills` from `groom.md`; `test-failure-handler` on the first `test-failure` prompt | `mint`, `resume`, `test-failure`, `fix`, `merge-tip`, `handoff` |
| `verifier-<suffix>` | verifier | item | yes | read set | `verify-before-done`, `docs-google-style` | `mint`, `recheck`, `land-recheck`, `post-land` |
| `reviewer-<suffix>` | reviewer | item | yes | read set | `pr-review`, `security-hardening` | `mint`, `rereview` |

Every persona has `tracker: true`. The read set is
`read,bash,grep,find,ls`. The driver always adds the extension tools
`sdlc_write` and `sdlc_result`. Every persona may also receive `repair`
and `answer` prompts; those two are fixed by the driver, not the bundle.

`state.md` templates (the body section `## State template`):

| Persona | Template headings and lines |
| --- | --- |
| builder | `## Corrected errors` (`- <what broke> → <fix> (<run>)`), `## Open findings` (`- <id> <criticality> <one line> (<source>)`), `## Do not repeat` (`- <approach> — <why it failed>`), `## Next` (one line) |
| verifier | `## Ledger` (table: `Id`, `Criticality`, `Status`, `Issue`, `Raised`, `Fixed`), `## Nits` (recorded, not sent back), `## Last commands seen` (`- <prove run>: <status>`) |
| reviewer | `## Verdicts` (`- <run> <range> <verdict>`), `## Open review comments`, `## Security reads` (`intake`, `sha-pins`, `trust-boundary`, one line each) |
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
| `resume` | Later run of the same node | Only what changed |
| `test-failure` | Proving commands failed | Load `test-failure-handler`; open `{{log}}`; `{{repair}}` |
| `fix` | Verifier or reviewer sent the item back | Fix the open findings in the facts; do not move the ticket |
| `merge-tip` | Land step 1, tip moved | Merge `{{tip}}` into `{{branch}}` with a merge commit; never rebase; `blocked` if a conflict cannot be resolved |
| `handoff` | Replacement mint the operator approved | The short handoff: paths, decisions, open failures |
| `recheck`, `land-recheck` | Verifier re-check, before or inside land | Confirm committed issues; new issues only if breaking or critical |
| `post-land` | Land step 4 | Read `{{landResult}}` at `{{landSha}}`; `done` or back to `in_progress` |
| `rereview` | Review again | `{{range}}` and the open review comments only |
| `paperwork` | After the driver commits the HLD or LLD | Post `{{commentText}}` on `{{epic}}`; write nothing else |
| `stop` | Any stop | `{{stopKind}}`, `{{stopRun}}`, `{{question}}`, `{{choices}}` |
| `gate` | A gate node | Draft `ask-human.md` for `ask`; choices are the gate's exits |
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

The groom reviewer checks that the block agrees with the prose. At
freeze, the manager fills the `Tickets:` line as
`` `G1` = `DER-530`, `G2` = `DER-531` ``; the driver parses only that
line and the blocks.

#### `test-failure-handler`

A first-party skill, at most 60 lines. Steps: open the log at the path
in the prompt; find the first failure; load `debug` and find the root
cause; write a failing test when the cause is in code (`tdd`); fix;
commit; add one `## Corrected errors` line and, for an approach that
failed, one `## Do not repeat` line to `state.md`. Never edit the
proving commands or `groom.md`. Never move the ticket.

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
them. The contract version stays 2
([Open questions](#questions-for-the-operator), O4).

### Behavior 4: run root formats

All files are UTF-8. JSON files are written atomically: temporary file
in the same folder, `fsync`, `rename`. The driver refuses a run root
that is inside a git worktree, that is a symbolic link, or whose mode
grants any group or other permission; it creates the run root `0700`.

```text
RUN_ROOT/
  run.json             # kickoff writes; the operator confirms at the first /sdlc
  driver.json          # driver only
  index.jsonl          # driver only; one line per event (UX Q3)
  checklist.md         # kickoff
  plan/items.json      # driver, after ticket filing
  asks/ask-N.json      # driver: ask and answer, machine copy
  asks/ask-N.md        # driver: the same, for people
  driver/lock          # run-root lock
  driver/console.log   # every console line
  driver/snapshot.json # pre-stage hashes of the stage in flight
  driver/facts/<persona>--run-N.md   # facts passed to that run
  driver/worker-ext/sdlc-worker-<sha12>.ts
  repo.git/            # driver's bare clone of the product repo
  worktrees/integrate/ # integration worktree, detached at project-main
  worktrees/<suffix>/  # one item worktree
  gatherer/run-1/      # kickoff: brief.md, gather session copy
  <persona>/session.jsonl            # the persona's Pi session
  <persona>/run-N/     # see Run folder
  prove-<suffix>/run-N/  land-<suffix>/run-N/  commands/run-N/  operator/run-N/
```

`repo.git/` and the folder names keyed by suffix refine the HLD layout:
item worktrees and the integration worktree share one bare clone whose
git directory sits inside the hashed run root
([Post-stage checks](#post-stage-checks)). The driver's command folders
(`prove-`, `land-`, `commands`) and `operator/` (gate results) are not
personas and never write to the tracker.

#### `run.json`

```json
{
  "schemaVersion": 1,
  "chunk": {"slug": "solo-dlc", "epic": "DER-421"},
  "bundle": {"id": "sdlc", "home": "/abs/path/to/skills-home", "commit": "<40-hex>"},
  "repo": {"origin": "git@github.com:OWNER/REPO.git", "trunk": "main",
           "projectMain": "integrate/solo-dlc", "designDir": "maintainers/design/solo-dlc"},
  "tracker": {"backend": "local", "skill": ".agents/tracker/SKILL.md",
              "keyPattern": "^der-[a-z0-9]{4}$", "local": {"branch": "tickets"}},
  "mode": "enforced",
  "harness": {"name": "pi", "version": "0.73.1", "bin": "/abs/path/to/pi"},
  "models": {"default": {"model": "local/qwen-coder", "contextWindow": 131072, "paid": false}},
  "spending": null,
  "labels": {"mode": "plain"},
  "limits": {"repairs": 3, "invalidRepairs": 1},
  "env": {"scrub": ["LINEAR_API_KEY"]},
  "gather": {"sessions": ["gatherer/run-1/session.jsonl"]},
  "createdAt": "2026-10-18T07:00:00Z"
}
```

- `repo.origin` must carry no user info (`://user@` with a password, or
  a token) and no query string. SSH and plain HTTPS forms are allowed.
- `tracker.backend`: `local` or `linear`; any other value stops the
  kickoff ([Tracker reads](#tracker-reads-no-model)). `linear` adds
  `"linear": {"keyFile": "/abs/path", "team": "DER"}`, `"stateMap"`
  (status name → canonical state, copied from the repo skill's Mapping),
  and `"self"` (the Linear user id that agents share). The endpoint is
  fixed in code, not configurable.
- `harness.bin` is the absolute path of the `pi` executable; the
  optional `harness.node` is the Node binary for the detached driver.
- `models.<slot>.model` is the Pi `--model` value. A slot with
  `"paid": true` requires `spending` = `{"askId": "kickoff-1",
  "approvedAt": "<UTC>", "text": "<the operator's words>"}`.
- At the first `/sdlc`, and whenever its hash changes, the plugin shows
  a summary of `run.json` (bundle commit, repo, tracker, models,
  spending, labels) and records the operator's yes as `runJsonSha256`
  in `driver.json`. No yes, no run.

#### `driver.json`

```json
{
  "schemaVersion": 1,
  "runJsonSha256": "<hex>",
  "bundle": {"commit": "<40-hex>", "checkedAt": "<UTC>"},
  "worker": {"extension": "driver/worker-ext/sdlc-worker-1a2b3c4d5e6f.ts",
             "sha256": "<hex>", "harnessVersion": "0.73.1"},
  "chunk": {"node": "spec", "state": "active", "stop": null, "askId": null},
  "groom": {"path": "maintainers/design/solo-dlc/groom.md", "reviewedCommit": "<sha>",
            "frozenCommit": "<sha>", "commandsSha256": "<hex>"},
  "items": {
    "DER-530": {"state": "active", "node": "verify", "land": null,
                "repairs": 1, "sentBack": true, "fixPending": false,
                "lastPushed": "<sha>", "reviewBase": "<sha>",
                "stop": null, "askId": null}
  },
  "sessions": {"builder-der-530": {"path": "builder-der-530/session.jsonl",
               "state": "live", "packed": ["tdd", "yagni", "debug"]}},
  "runs": {"builder-der-530": 5, "prove-der-530": 4},
  "inFlight": null,
  "projectMainSeen": "<sha>",
  "nextAsk": 4,
  "updatedAt": "<UTC>"
}
```

| Field | Values and meaning |
| --- | --- |
| `chunk.state`, `items.*.state` | `pending` (not started), `active`, `waiting` (an ask is open: `askId`), `deferred` (the manager deferred it; retried at the next `/sdlc`), `done` |
| `chunk.node`, `items.*.node` | Current node id, or `@items` / `@done` |
| `items.*.land` | `null` outside the land node, else `{"phase", "p1", "p2", "cleanTree", "cleanCommit", "landCommit"}`; `phase` is one of the [Land](#land-sub-machine) rows |
| `repairs`, `sentBack`, `fixPending` | [Repair counter](#repair-counter) |
| `lastPushed` | Item branch tip the driver last pushed |
| `reviewBase` | Item `HEAD` at the last Review pass, or the clean merge commit after a row-1 classification |
| `stop` | `{"kind", "run", "operatorOnly"}` while the manager handles a stop |
| `sessions.*.state` | `live`, `lost` (stopped; ask open), `replaced` (minted again on the operator's answer; the old file is kept as `session.lost-<UTC>.jsonl`) |
| `sessions.*.packed` | Skill ids already in that session's transcript |
| `inFlight` | `{"run", "scope", "node", "kind", "pid", "startedAt"}` while a stage runs |

#### `index.jsonl`

One JSON object per line, appended with `O_APPEND`, at most 4 KiB:

```json
{"v": 1, "seq": 41, "at": "2026-10-18T09:12:03Z", "event": "end", "scope": "DER-530",
 "node": "verify", "step": "Build", "persona": "verifier-der-530",
 "run": "verifier-der-530/run-3", "session": "resumed", "status": "pass",
 "choice": "review", "artifact": "verifier-der-530/run-3/result.md"}
```

`event` is `start`, `end`, `stop`, `ask`, `answer`, `push`, `land`,
`interrupted`, or `found`. Resume never reads this file; it is history
for people ([ux.md](ux.md) Q3). If the operator rejects Q3, the driver
writes no `index.jsonl` and nothing else changes.

#### `plan/items.json`

```json
{"schemaVersion": 1,
 "groom": {"path": "maintainers/design/solo-dlc/groom.md", "reviewedCommit": "<sha>",
           "frozenCommit": "<sha>", "commandsSha256": "<hex>"},
 "items": [{"g": "G1", "ticket": "DER-530", "suffix": "der-530", "slug": "result-format",
            "branch": "item/der-530-result-format", "blockedBy": [],
            "skills": ["lang-js-ts"], "prove": ["npm --prefix packages/sdlc-driver test"],
            "proveSha256": "<hex>"}]}
```

Array order is plan order (G-number order). `blockedBy` holds ticket ids.
This file is a snapshot for people and for dispatch order; the driver
never reads proving commands from it.

#### `asks/`

`ask-N.json`:

```json
{"id": "ask-4", "kind": "operator-stop", "scope": "DER-532", "node": "build",
 "stopKind": "repair budget exhausted", "stoppedRun": "builder-der-532/run-9",
 "managerRun": "manager/run-6", "choices": [], "openedAt": "<UTC>",
 "message": "<ask-human.md text, verbatim>",
 "answer": null}
```

`kind` is `gate` (choices = the gate's exit names), `lost-session`
(choices `replace`, `defer`), `scan-hit` (choices `allow`, `revise`),
`pi-dir` (choices `allow`, `defer`), or `operator-stop` (free text). An answer is
`{"choice": "<one of choices or null>", "text": "<verbatim>", "at": "<UTC>"}`.
`ask-N.md` renders the same fields with the message and the answer
verbatim. Answers are recorded only by the plugin's `/sdlc` handler, in
the operator's interactive session, while no driver holds the lock
([Host shape](#host-shape-and-sdlc)).

#### Run folder

| File | Writer | Notes |
| --- | --- | --- |
| `meta.json` | driver | Node, scope, persona, `new` or `resumed`, prompt kind, `repairOf`, start and end times, the worker argv |
| `prompt.md` | driver | The prompt sent on stdin |
| `candidate.json` | worker | Through `sdlc_result` or `sdlc_write` |
| `result.json` | driver | The validated result, or a driver-authored one |
| `result.md` | worker | Prose |
| `state.md` | worker | Copied by the driver from the persona's previous run, or from the template, before the run starts |
| `ledger.json` | verifier | [Verifier ledger](#sdlc-personas-and-prompts) |
| `ask-human.md` | manager | On `escalate` |
| `out/` | worker | Files for the repo, at their repo-relative paths |
| `commands.json` | driver | Command stages: one entry per command: index, line, exit code, duration, log path |
| `logs/` | driver, extension | `worker.jsonl` (Pi's JSON stream), `worker.stderr`, `ext.json` (extension load marker), `prove-K.log` |
| `interrupted.json` | driver | Present when the run was interrupted; such a folder never gets `result.json` and is never reused |

#### Driver facts

The driver writes the facts as text, at most 16 KiB, passes them to the
worker in `SDLC_FACTS` with their SHA-256 in `SDLC_FACTS_SHA256`, and
keeps the same text in `driver/facts/<persona>--run-N.md`:

```text
Driver facts for builder-der-530/run-5 (DER-530, Build). Written by the driver.
- Repair: 2/3
- Open verifier issues:
  - V2 critical: retry stops after the first attempt
  - V4 breaking: CLI exits 0 on a missing run root
- Failing logs:
  - prove-der-530/run-4/logs/prove-2.log
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

1. **Kickoff** reads the tracker's key pattern and the longest id it
   allows. `local` ids (`<prefix>-xxxx`, at most 11 characters) and
   Linear keys fit `plain`. A pattern that allows ids longer than 23
   characters, or characters outside `[A-Za-z0-9-]`, sets `short`, and
   kickoff says so on the checklist.
2. **Driver**, when it writes `plan/items.json`, computes each suffix.
   In `plain` mode, an id that does not fit is a `fail`, `operator`
   stop that asks to switch to `short`; no item persona exists yet, so
   the switch is safe. In `short` mode, two items with the same suffix
   extend both hashes to 12 hex digits.
3. The suffix never changes after an item persona exists. Comments
   still carry the full ticket id.

### Behavior 5: core driver (item 5)

#### Adapter interface

The core knows no harness. A plugin passes a `HarnessAdapter`:

```ts
interface HarnessAdapter {
  name: string;                                   // "pi", "opencode", "test"
  checkVersion(pinned: string): Promise<string>;  // returns the actual version
  installWorkerExtension(runRoot: string): Promise<{path: string; sha256: string}>;
  sessionLooksValid(path: string): Promise<boolean>;
  runWorker(spec: WorkerSpec, signal: AbortSignal): Promise<WorkerExit>;
  ui: {line(text: string): void; notify(kind: "stop" | "ask" | "done", text: string): void};
}
interface WorkerSpec {
  persona: string; job: string; mint: boolean; sessionPath: string;
  runDir: string; promptPath: string; cwd: string; tools: string[];
  model: string; env: Record<string, string>; timeoutSec: number; logDir: string;
}
interface WorkerExit {
  exitCode: number | null; signal: string | null; timedOut: boolean;
  modelError: string | null;                      // adapter-specific: Pi stopReason error/aborted
}
```

The core API is `prepare(runRoot, adapter)` (lock check, validation,
the found report, pending asks) and `run(runRoot, adapter)` (the loop).
Recording an answer is `recordAnswer(runRoot, askId, choice, text)`;
it refuses while any driver holds the lock.

#### Start

1. Take `driver/lock`: create it with `O_EXCL`, holding
   `{"pid", "procStart", "startedAt"}`. If it exists and its pid is
   alive with the same process start time, exit with
   `another driver holds RUN_ROOT (pid N)`. Otherwise it is stale: print
   one line and take it.
2. Validate `run.json`; check `runJsonSha256`; check the harness version
   equals `run.json` `harness.version`, else stop with the two versions.
3. Fetch `repo.git`; run the bundle check at the pinned commit; any
   error stops the start with the error lines. On the first start,
   create `repo.git` (`git init --bare`, `origin` from `run.json`,
   fetch refspec `+refs/heads/*:refs/remotes/origin/*`) and
   `worktrees/integrate`, detached at the project-main tip.
4. Install the worker extension; if its hash differs from
   `driver.json`, print one line and record the new hash.
5. If `inFlight` is set, the previous driver died mid-stage: write
   `interrupted.json` in that run folder, run the
   [post-stage checks](#post-stage-checks) against
   `driver/snapshot.json`, clear `inFlight`, and append an
   `interrupted` event. A failed check is an `operator` stop.
6. Print the found report ([Console](#console-lines)); any `deferred`
   scope becomes `active`.
7. Enter the loop.

#### Loop

1. Pick the next runnable scope: the chunk, while its node is not
   `@items` or `@done` and its state is `active`; then items in plan
   order whose state is `pending` or `active` and whose `blockedBy`
   items are all `done`.
2. None runnable: print the summary (pending asks, deferred and waiting
   items), release the lock, and return.
3. An item that is `pending` becomes `active`: fetch, create its
   branch from the fetched project-main tip with
   `git worktree add -b <branch> worktrees/<suffix> <tip>`, push the
   branch without force, and set `lastPushed`.
4. Run the scope's current node ([Node routing](#node-routing)).
5. Repeat.

One stage runs at a time, model or command, across all scopes.

#### Stage pipeline: model node

1. **Run folder.** N = `runs[folder] + 1`. If `<folder>/run-N/` already
   exists and holds a `meta.json`, increment N again. An empty folder
   (kickoff's `refiner/run-1/`) is used as is.
2. **Session.** If `sessions[persona]` exists, this is a resume: the
   file must exist and `adapter.sessionLooksValid` must pass, else a
   `lost-session` stop. If it does not exist, this is a mint: the file
   must not exist, else an `operator` stop
   (`unexpected session file`).
3. **Files.** Copy `state.md` from the persona's previous run, or the
   template; write `prompt.md` ([Prompts](#prompts)); write the facts
   file; write `meta.json`.
4. **Snapshot.** Set `inFlight`, write `driver.json`, then take the
   pre-stage snapshot and write `driver/snapshot.json`.
5. **Worker.** Print the start line; call `adapter.runWorker`. After it
   returns, kill leftovers ([Pi adapter](#pi-adapter-and-worker-command-line)).
6. **Checks.** Run the [post-stage checks](#post-stage-checks) first,
   whatever the candidate holds. The first failure writes a
   driver-authored `fail` (`choice: operator`) naming the check, keeps
   `candidate.json`, and is an `operator` stop; no repair runs.
7. **Validate.** The candidate is invalid if it is missing, fails the
   strict reader, fails item 1 or the
   [candidate rules](#flowjson), `timedOut` is true, or `modelError` is
   set. Then:
   - First invalid run of this stage: write a driver-authored `fail`
     (`choice: stop`, findings: the error codes and messages) in this
     run folder, print `invalid result … repair 1/1`, and run a repair:
     a new run folder for the same persona, resumed, with the fixed
     `repair` prompt holding the errors. A repair does not count toward
     the [repair counter](#repair-counter).
   - Invalid repair run: driver-authored `fail`, `choice: stop`; keep
     both candidates; stop kind `invalid result after repair`.
8. **Result.** Write `result.json`: the candidate plus the fixed
   fields. If this was a mint and the session file now exists, record
   `sessions[persona]`; if the file does not exist (Pi writes it only
   after the first assistant message), the next run is a mint again.
9. **Builder push.** After a builder run with a valid result: check
   `lastPushed` is an ancestor of `HEAD`, push the item branch without
   force, and record `lastPushed`. Not an ancestor: `operator` stop
   (`pushed history rewritten`). A rejected push: `operator` stop with
   the redacted error.
10. **Records.** For a chunk node with `outputs` or `outputDirs` and a
    `pass`: [design-record commit](#design-record-commits).
11. **Record and route.** Clear `inFlight`, append `end` to
    `index.jsonl`, print the end line, and route by `choice`.

#### Stage pipeline: command node

1. Read the commands: for `"groom"`, from the frozen `groom.md` blob
   ([Proving commands](#proving-commands)); else the bundle's
   `scripts/` files at the pinned commit, copied into the run folder.
2. Run each command in order in the item worktree, stopping at the first
   non-zero exit. Each command runs as
   `bash --noprofile --norc -c <line>` in its own process group, with the
   worker environment minus every `SDLC_*` variable, a per-command
   timeout (`defaults.commandTimeoutSec`), and output to
   `logs/prove-K.log` (cap 50 MiB, then a truncation line).
3. Write `commands.json` and a driver-authored command result:
   `evidence.command` is the lines joined with ` && `, `exit_code` is the
   first non-zero code or `0`, timeout `124`, signal `128 + n`, launch
   failure `127`. `choice` is the node's `pass` or `fail` exit. On
   `fail`, `findings` names `proving command K of N`, the exit code, and
   the log path.
4. Run the post-stage checks for the worktree and the run root.
5. Route.

#### Node routing

| Scope at node | Result | Next |
| --- | --- | --- |
| `model` or `command` node | `choice` is a listed exit | `node = exit.to`; print `say` if any. `@items`: set the chunk node to `@items` and each planned item to `pending` at `itemEntry`. `@done`: the scope is done |
| any | `choice: stop` | Manager stop, all three manager exits allowed |
| any | `choice: operator` | Manager stop, `escalate` only |
| `gate` node | (reached) | Manager stop of kind `gate`, `escalate` only; ask kind `gate` |
| `land` node | (reached) | [Land sub-machine](#land-sub-machine) |
| `prove`, `verify`, or `review` node sends the item back (`fail` exit to the builder node) | — | [Repair counter](#repair-counter) first; third failed fix → `operator` stop instead of the builder |
| `file-tickets` `pass` | — | [Ticket filing](#ticket-filing) before `@items` |

#### Repair counter

Per item: `repairs` (never reset), `sentBack`, and `fixPending`.

| Event | Effect |
| --- | --- |
| A check sends the item back: proving commands `fail`, verifier `fail`, reviewer `fail`, a land re-run `fix` | If `fixPending`: `repairs += 1`. Then `fixPending = false`, `sentBack = true` |
| Proving commands on the integration merge are red ([Land](#land-sub-machine) L6) | `repairs += 1` once, whether or not `fixPending`; then `fixPending = false`, `sentBack = true` |
| A builder run starts while `sentBack` is true | `fixPending = true`, `sentBack = false` |
| A builder run starts for `merge-tip` | No change |
| `repairs` reaches 3 or more at an event | Do not resume the builder: `operator` stop, kind `repair budget exhausted` |
| An invalid-result repair | No change |

Console `repair N/3` on a send-back line: N = `repairs + 1`, the fix
attempt about to start. After the operator answers a budget stop and
the builder is resumed, each further failed fix stops again.

#### Land sub-machine

The item enters the land node after a Review `pass`. `T` is the fetched
project-main tip. `H` is the item `HEAD`.

| Row | State and condition | Action | Next |
| --- | --- | --- | --- |
| L1 | Enter, or after L3a or L4 | Fetch. If `T` is an ancestor of `H`, print `tip unchanged` | L5 |
| L1′ | `T` not an ancestor of `H` | Print `tip moved`; `p1 = H`, `p2 = T`; resume the builder with `merge-tip` | L2 |
| L2 | Builder merge run ends | `blocked` or `needs_input`: stop the item (manager), whatever `merge-tree` reports. `pass` (`ready`): push the item branch (pipeline step 9); require that `p1` and `p2` are ancestors of the new `H`, else `operator` stop | L3 |
| L3 | Classify | `git merge-tree --write-tree --no-messages p1 p2`. Exit `0` and its tree equals `H^{tree}`: print `tip merged clean`, set `cleanTree`, `cleanCommit = H`, `reviewBase = H` → L3a. Exit `1` (conflict) or a different tree: print `tip merged, tree differs from the clean merge` → L3b. Any other exit: `operator` stop | — |
| L3a | Clean (row 1, inside land) | Proving commands on the item worktree (`prove-<suffix>`, exits `ok`/`fix`); then the verifier with `land-recheck` (exits `ok`/`fix`). Both `ok` | L1 |
| L3a′ | A row-1 run returns `fix` | Repair counter (send-back event); resume the builder with `test-failure` or `fix`; then L3c | — |
| L3c | Builder returns from an edit after the clean check | `blocked` or `needs_input`: stop. Otherwise push, then re-run L3's check with the stored `p1` and `p2`, never the new `H`'s parents: tree of `H` equals `cleanTree` → L3a; else → L3b | — |
| L3b | Not clean (row 2) | Leave the land node: `node = land.prove`; the item then takes `prove` → `verify` → `review` → land | L1 on the next Review `pass` |
| L5 | Tip unchanged | In `worktrees/integrate`: detach at `T`, `git merge --no-ff --no-edit H` with message `[<ticket>] Land <branch>` and trailer `Reviewed-by: <reviewer-label> (<verdict>)`, where `<verdict>` is the last Review `status` | L6 |
| L6 | Merge exists | Proving commands on the merge (`land-<suffix>/run-N`, exits `ok`/`fix`) | L7 or L6r |
| L6r | Red | Reset the integration worktree to `T` (driver worktree only). Repair counter (land-red event); third failed fix → `operator` stop. Else resume the builder with `test-failure` and the log path; then `node = land.prove` (row 2 path) | — |
| L7 | Green | `git push origin HEAD:refs/heads/<projectMain>`, no force option | L8, L7m, or L7x |
| L7m | Rejected: `[rejected] … (fetch first)` or `(non-fast-forward)` | Reset the integration worktree to `T`; append a `push` event | L1 |
| L7x | Rejected for any other reason | Reset; write a command result in a new `land-<suffix>` run (`git push …`, its exit code, `fail`, redacted error, `choice: stop`); stop kind `blocked` to the manager. Never retry that push | — |
| L8 | Pushed | `landCommit = HEAD`; append `land`; resume the verifier with `post-land` (`{{landSha}}`, `{{landResult}}`) | L9 |
| L9 | Post-land verifier ends | `pass`: read the ticket; `done` → delete the remote item branch (`git push origin --delete <branch>`), remove the item worktree, take the land node's `done` exit, print `verified done`. Not `done` → tracker-state check failure, `operator` stop. Any non-`pass`: `operator` stop; the merge stays on project-main; branch and worktree stay; dependents stay blocked | — |

Rules this table encodes:

- The clean merge is always computed from the stored pre-merge parents
  `p1` (item tip before the builder's merge) and `p2` (the tip the
  builder merged).
- A merge commit whose tree differs from the clean tree always goes
  through Review, whatever the builder's result or prose says. The
  driver prints the merge line from its own classification.
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

1. Fetch; detach `worktrees/integrate` at the project-main tip.
2. For each output path: `out/<path>` must be a regular file (no
   symbolic link on the way), at most 2 MiB; copy it. For each
   `outputDirs` prefix, copy every regular file under it. Ignore any
   other file in `out/` and print one line naming it.
3. Scan the copied files ([Scan patterns](#scan-patterns)). A hit:
   replace `result.json` with a driver-authored `fail` naming file and
   line, ask kind `scan-hit`. `allow` commits as is and records the
   answer; `revise` resumes the persona with the hit list.
4. `git add -- <paths>`; commit `[<epic>] <Step>: <node id> from
   <run>`. Nothing staged: no commit, continue.
5. Push without force. Rejected because the tip moved: fetch, detach at
   the new tip, copy and commit again, push; at most 10 rounds, then a
   `blocked` stop. Any other rejection: `blocked` stop, no retry.
6. Record the commit SHA in `meta.json`. For `groom`, it becomes
   `groom.reviewedCommit` when the next `groom-review` passes.
7. For the HLD node and the Spec node: resume the architect in a new
   run folder with `paperwork` and `{{commentText}}` holding the comment
   fields plus `Record: <path>`. Its only exit is `posted` [`pass`].
   Any other status is a manager stop (`stop` exit semantics,
   kind `paperwork failed`). The original node's `choice` routes only
   after `posted`.

#### Scan patterns

Case-insensitive, per line, applied to every committed record:

- IPv4 addresses, except `192.0.2.0/24`, `198.51.100.0/24`,
  `203.0.113.0/24`, and `127.0.0.1`.
- Home and system paths: `/home/`, `/Users/`, `/root/`, `/var/lib/`,
  `C:\Users\`, and the literal run root path.
- Host suffixes `.lan`, `.local`, `.internal`, `.ts.net`, `.home.arpa`.
- URLs with user info (`://[^/\s]+@`).
- Credential shapes: `-----BEGIN [A-Z ]*PRIVATE KEY-----`,
  `sk-[A-Za-z0-9_-]{20,}`, `lin_api_[A-Za-z0-9]{20,}`, `ghp_`,
  `github_pat_`, `xox[abprs]-`, `AKIA[0-9A-Z]{16}`.

#### Post-stage checks

Every check named here is the `check` field of a failed-check result.

| Check | After | How |
| --- | --- | --- |
| `snapshot` | every stage | Walk `RUN_ROOT` without following symbolic links. Excluded: the current run folder, the current persona's session file, `worktrees/`, `driver/snapshot.json`, and everything under `repo.git/` except `config`, `hooks/`, and `info/`. Record path, type, mode, size, and SHA-256 (the target string for a link). A cache keyed by inode, size, and `ctime` skips rehashing unchanged files. Any difference is a failure |
| `worktrees` | every stage | For each worktree outside the writable set: `HEAD` and `git status --porcelain` equal before and after |
| `item-remote` | verifier and reviewer stages | `git ls-remote origin refs/heads/<branch>` equal before and after |
| `ancestry` | builder stages | `lastPushed` is an ancestor of `HEAD` (pipeline step 9) |
| `project-main` | every worker stage | Fetch; let `M0` be `projectMainSeen` and `M1` the new tip. For each active item, no commit in `git rev-list H ^M0` is also in `git rev-list M1 ^M0`. Then `projectMainSeen = M1` |
| `extension` | model stages | `logs/ext.json` exists and names this persona and facts hash |
| `tracker-state` | every worker stage | [Tracker-state check](#tracker-state-check) |

Every git call by the driver sets `GIT_CONFIG_COUNT` to disable hooks
(`core.hooksPath=/dev/null`), sets `GIT_NO_REPLACE_OBJECTS=1`, and has
no force option in its code path. The only branch deletion is L9.

#### Stops and the manager

| Stop kind (console words) | Trigger | Manager may | Ask kind |
| --- | --- | --- | --- |
| `blocked` | Worker `blocked` with `stop`; L2; L7x; design-record push | `resume`, `defer`, `escalate` | `operator-stop` |
| `needs input` | Worker `needs_input` with `stop` | `resume`, `defer`, `escalate` | `operator-stop` |
| `invalid result after repair` | Pipeline step 6 | `resume`, `defer`, `escalate` | `operator-stop` |
| `paperwork failed` | Design-record step 7 | `resume`, `defer`, `escalate` | `operator-stop` |
| `operator gate: <tag>` | A gate node | `escalate` | `gate` |
| `operator: <question>` | Worker chose `operator` | `escalate` | `operator-stop` |
| `repair budget exhausted` | Repair counter | `escalate` | `operator-stop` |
| `check failed: <check>` | Post-stage or tracker-state check, `unexpected session file`, `pushed history rewritten` | `escalate` | `operator-stop` |
| `scan hit` | Design-record step 3 | `escalate` | `scan-hit` |
| `session lost: <file>` | Pipeline step 2 | `escalate` | `lost-session` |
| `project Pi files: <path>` | `.pi/` in a worker cwd ([Pi adapter](#pi-adapter-and-worker-command-line)) | `escalate` | `pi-dir` |
| `post-land verify failed` | L9 | `escalate` | `operator-stop` |

1. The driver sets the scope's `stop`, prints the `STOP` line, and
   resumes `manager` with the `stop` prompt (or `gate`).
2. Manager exits: `resume` [`pass`], `defer` [`pass`], `escalate`
   [`needs_input`]. A `pass` needs one `evidence.checks` entry
   `source: <brief|plan|spec|tracker|gather> <path or run folder>`;
   the console prints it (SD-7).
3. `resume`: resume the stopped persona in a new run folder with the
   `answer` prompt; `{{answer}}` is the manager's `findings`, verbatim,
   fenced as data.
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
| `lost-session` | `replace` | Moves the old file to `session.lost-<UTC>.jsonl` if present, mints a new session with the `handoff` prompt (last `state.md`, facts, the answer) |
| `lost-session` | `defer` | Leaves the scope `waiting` |
| `scan-hit` | `allow` or `revise` | [Design-record commits](#design-record-commits) step 3 |
| `operator-stop` | Text | Resumes `manager` with `apply-answer`; exits `resume`, `defer`, `escalate` as in steps 3–5 |

An empty answer records nothing; the ask stays pending (never proceed
after silence).

#### Prompts

The driver builds `prompt.md` in this order:

1. The persona's `## Role` (mint only).
2. Packed skills not yet in `sessions[persona].packed`, each under
   `# Packed skill <id> — do not reload`, read from the pinned commit,
   or, for the repo tracker skill, from `origin/<projectMain>` at the
   last fetch.
3. The prompt kind's text with placeholders filled.
4. The run contract, fixed by the driver: the run folder; the files the
   worker may write; `state.md` limits; the allowed exits with their
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

| Stage | Expected state | Expected assignee: `local` / `linear` |
| --- | --- | --- |
| Builder, any pass | `in_progress` | `builder-<suffix>` / `self` |
| Verifier, before land | `in_progress` | `verifier-<suffix>` / `self` |
| Reviewer | `in_review` | `reviewer-<suffix>` / `self` |
| Verifier, post-land, `pass` | `done` | `verifier-<suffix>` / `self` |
| Verifier, post-land, not `pass` | `in_progress` | `verifier-<suffix>` / `self` |
| Chunk personas, except `file-tickets` | Epic state unchanged from before the stage | not checked |
| Manager, `file-tickets` | [Ticket filing](#ticket-filing) step 4 | not checked |
| Manager, stops | Unchanged from before the stop | not checked |

Anything else is `check failed: tracker-state`. The read happens after
the stage even when the result is invalid, so a builder that moved the
ticket to `done` is caught before any repair.

#### Tracker reads (no model)

The driver reads with built-in readers, one per backend. It runs no
command string from a repo file. A read that fails after three attempts
(2, 4, and 8 seconds apart) is `check failed: tracker-read` with a
redacted message. Every id is checked against `tracker.keyPattern`
before use.

**`local`.**

1. `git -C repo.git fetch origin +refs/heads/tickets:refs/remotes/origin/tickets`.
2. `git -C repo.git ls-tree refs/remotes/origin/tickets tickets/<id>.md`
   must show mode `100644`.
3. `git -C repo.git show refs/remotes/origin/tickets:tickets/<id>.md`;
   parse the front matter (`id`, `type`, `state`, `parent`,
   `blocked_by`, `assignee`) with the adapter's text format; reject a
   malformed list or an unknown state.

**`linear`.** Node's global `fetch`, `POST https://api.linear.app/graphql`
(fixed in code), header `Authorization: <key>` (a personal API key takes
no `Bearer` prefix), body:

```graphql
query($id: String!) { issue(id: $id) { identifier state { name type }
  assignee { id } parent { identifier }
  inverseRelations(first: 50) { nodes { type issue { identifier state { name } } } } } }
```

- `issue(id:)` accepts the human key such as `DER-530`.
- Blockers are the `inverseRelations` entries with `type` `blocks`.
- `state.name` maps through `run.json` `tracker.stateMap`; an unknown
  name is a read failure.
- A response with a non-2xx status, any `errors` entry, or a null
  `issue` is a failure; error codes are matched on both
  `extensions.code` and `extensions.type`.
- Timeout 15 seconds (`AbortSignal.timeout`). The driver never logs
  request headers.
- The key is read from `run.json` `tracker.linear.keyFile` at each read;
  the file must be a regular file owned by the operator with mode
  `0600`, outside the run root and every checkout. The key is never put
  in any environment, file, prompt, or log the driver writes.
- Budget: about two reads per stage, against Linear's published limit of
  2,500 requests per hour per user, shared by every key of that user.

Jira, Asana, and Trello have no built-in reader in this chunk: kickoff
stops with that reason.

#### Console lines

Fields are separated by two spaces. `<S>` is the ticket id, or the Epic
id for the chunk. `<L>` is the node `label`, padded to 7.

| Event | Line |
| --- | --- |
| Header | `<slug>  bundle <id>@<sha7>  mode enforced  root <RUN_ROOT>` |
| Found | `found  last finished  <S> <L> <run> <status>`; `found  interrupted  <run> (kept)`; `found  will resume  <personas>`; `found  next run  <run>`; `found  pending ask  ask-N  <S> <L>: <stop kind>` |
| Start | `<S> <L>  <persona>  new or resumed  <run>  started[  <note>]`; notes: `merge tip`, `fix`, `re-run`, `re-review`, `repair` |
| End | `<S> <L>  <status>  choice <choice>  artifact <path>[  <extra>]`; extra for Verify `ledger <fixed> fixed, <open> open, <nits> nit`, for Review `reads <packed skills>` |
| Command fail | `<S> <L>  fail  proving command K of N failed  log <path>  repair N/3` |
| Invalid | `<S> <L>  invalid result  <run>  repair 1/1` |
| Rejected choice | `<S> <L>  rejected choice <value>  allowed <exit> (<statuses>), …` |
| Land | `<S> Land  fetched  tip moved  builder merges the tip`; `<S> Land  pass  tip merged clean`; `<S> Land  pass  tip merged, tree differs from the clean merge`; `<S> Land  fetched  tip unchanged  merged  <projectMain>  pushed`; `<S> Land  verifier  resumed  <run>  verified  done` |
| Stop | `STOP   <S> <L>  <stop kind>  <run>` then `       resuming manager  <run>` |
| Manager answered | `       manager answered from <source>  <S> continues` |
| Ask | The full `ask-human.md` text between `--- ask-N ---` lines |
| Say | `<S> <L>  <say text>` |
| Summary | `idle  <n> pending asks  <n> waiting  <n> deferred  type /sdlc RUN_ROOT to continue` |

`driver/console.log` holds every line. No color carries meaning, and no
worker transcript goes to the console.

### Behavior 6: Pi plugin and worker extension (item 6)

#### Host shape and `/sdlc`

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
3. `core.prepare`: show validation errors, the `run.json` confirmation
   (`ctx.ui.confirm`) when needed, the found report, and each pending
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
| `--session <file>` | Mint when the file is absent, resume when present ([Stage pipeline](#stage-pipeline-model-node) step 2) |
| `--no-extensions` with one `--extension` | Discovery off; Pi still loads explicit `--extension` paths |
| `--no-skills --no-context-files` | No skill discovery; no `AGENTS.md` or `CLAUDE.md`; skills arrive packed |
| `--tools` | Allowlist for built-in and extension tools; read-only personas get no `write` or `edit` |
| `--model` | `provider/id[:thinking]` from the persona's slot |

- **cwd:** builder, verifier, reviewer: `worktrees/<suffix>`. Chunk
  personas: `worktrees/integrate`.
- **Project Pi files:** before each start, the driver refuses a cwd
  that contains `.pi/`, because Pi reads project settings,
  `.pi/SYSTEM.md`, and `.pi/APPEND_SYSTEM.md` from there. This is an
  `operator` stop with ask kind `pi-dir` (choices `allow`, `defer`). An
  `allow` is recorded in `driver.json` with the git tree hash of that
  `.pi/` folder and holds until the tree changes.
- **Environment:** the operator's environment, minus every `SDLC_*`
  variable, `PI_CODING_AGENT_SESSION_DIR`, and each name in
  `run.json` `env.scrub`; plus:

  | Variable | Value |
  | --- | --- |
  | `SDLC_RUN_DIR` | Absolute run folder |
  | `SDLC_RUN_REL` | Run folder relative to the run root |
  | `SDLC_PERSONA`, `SDLC_JOB`, `SDLC_TICKET`, `SDLC_STEP` | The invocation |
  | `SDLC_WRITABLE` | JSON array of absolute paths: the run folder, plus the item worktree for the builder |
  | `SDLC_EXITS` | JSON array of `{"name", "statuses"}`, reserved exits included as the worker may use them |
  | `SDLC_CHECKS`, `SDLC_OUTPUTS` | JSON arrays from the node |
  | `SDLC_FACTS`, `SDLC_FACTS_SHA256` | [Driver facts](#driver-facts) |
  | `PI_OFFLINE` | `1`: Pi skips its start-up network calls and version check |

- **Process:** spawned with `detached: true` so the worker leads its own
  process group; stdout to `logs/worker.jsonl`, stderr to
  `logs/worker.stderr`. On timeout or `/sdlc-stop`: `SIGTERM` to the
  group, 20 seconds, then `SIGKILL`.
- **Leftovers:** after the worker exits, the adapter sends `SIGTERM` to
  the group and, on Linux, to every process of the same user whose
  `/proc/<pid>/environ` holds this `SDLC_RUN_DIR`. A process that
  cleared its environment escapes: residual.
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
the snapshot covers it.

1. **Load.** Parse every `SDLC_*` variable; check `SDLC_FACTS_SHA256`.
   Any error throws, so Pi reports the extension as failed. On
   `session_start`, write `logs/ext.json`
   (`{"persona", "factsSha256", "version"}`) with `fs` directly. The
   driver treats a missing marker as an invalid stage.
2. **`tool_call` guard.** For `write` and `edit`: resolve `input.path`
   (a leading `~/` is the home folder; relative paths against the
   process cwd); resolve symbolic links on the deepest existing
   ancestor and on the target if it exists. Allow only a path inside a
   `SDLC_WRITABLE` entry, with no `.git` path component, and, inside the
   run folder, not `prompt.md`, `result.json`, `meta.json`,
   `commands.json`, `interrupted.json`, or `logs/`. Otherwise return
   `{block: true, reason}` naming the writable set. The whole handler
   sits in `try`; any error blocks. Pi also blocks the call when a
   `tool_call` handler throws.
3. **`sdlc_write`.** Parameters `{path, content}`. `path` is relative to
   the run folder and matches
   `^(candidate\.json|result\.md|state\.md|ledger\.json|ask-human\.md|(out|notes)/[A-Za-z0-9._/-]+)$`
   with no `.` or `..` segment. Parent folders are created one by one
   and checked to be real folders. The file opens with
   `O_WRONLY|O_CREAT|O_TRUNC|O_NOFOLLOW`, mode `0600`. Content at most
   1 MiB; `state.md` at most 60 lines and 6,000 characters, else an
   error that says to shorten it.
4. **`sdlc_result`.** Parameters `status`, `choice` (a TypeBox union of
   the names in `SDLC_EXITS`), `findings`, `artifact`, and the optional
   `checks`, `blocker`, `question`. It applies the shape rules of item 1
   and candidate rules 2, 3, and 5, returns the errors to the model in
   the same turn, and writes `candidate.json` only when they pass. The
   driver validates again; the tool is advisory. Its tests run the
   shared fixtures, so the two stay in step.
5. **`session_before_compact`.** Returns
   `{compaction: {summary, firstKeptEntryId, tokensBefore}}`, the last
   two from `event.preparation`. The summary:

   ```text
   # Compaction summary (worker extension)
   ## Persona
   <SDLC_PERSONA> (<SDLC_JOB>) for <SDLC_TICKET>, step <SDLC_STEP>.
   Current run folder: <SDLC_RUN_REL>. Write files only with sdlc_write;
   finish with sdlc_result.
   ## State (state.md, at most one page)
   <state.md, first 60 lines>
   ## Driver facts (written by the driver)
   <SDLC_FACTS, verbatim>
   ```

   A missing `state.md` is replaced by one line saying so. The handler
   never cancels a compaction.

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
their own shape.

| Persona | Calls, in order | Label |
| --- | --- | --- |
| Builder, every pass | At start: `claim` (steps 1–4, same-item rule). Before exit, whatever the outcome: `comment`. An open blocker in claim step 1 → result `blocked` with `evidence.blocker`; a collision → `needs_input`, `operator` | `builder-<suffix>` |
| Verifier, before land | `claim`; `comment` with the ledger verdict as `Status` | `verifier-<suffix>` |
| Reviewer, every pass | `claim`; claim step 5, then `transition` `in_review`; `comment` with the verdict as `Status` | `reviewer-<suffix>` |
| Verifier, post-land, `pass` | `claim`; `transition` `done`; `comment` plus `Land`, `Result`, `Review` | `verifier-<suffix>` |
| Verifier, post-land, not `pass` | `claim`; `transition` `in_progress`; `comment` | `verifier-<suffix>` |
| Refiner, architect, designer, ux-reviewer, security, groom-reviewer | `comment` on the Epic | — |
| Architect, `paperwork` | `comment` on the Epic plus `Record` | — |
| Manager, `file-tickets` | Groom File steps 2–6: `create` each item (title `G<n>: <title>`, body copied), `set-blocker` each planned blocker, `transition` each item `ready`, `transition` the Epic `in_progress`, `comment` the `groom.md` path on the Epic. Then the freeze edit in `out/` | `manager` |
| Manager, stops | `comment` on the stopped ticket or the Epic | `manager` |

**Shell recipes on Pi.** Pi workers have no MCP client, so every recipe
in the repo skill must run from `bash`. Kickoff fails its tracker line
when the repo skill names an MCP tool (`mcp__`). The `local` adapter's
recipes qualify. This repo's Linear skill uses MCP; see
[O5](#questions-for-the-operator).

### Behavior 8: later items (4, 7, 8)

- **Item 4, `bundle-authoring`.** Walks an author through the
  [bundle layout](#bundle-layout-and-bundlemd), persona files, and
  `flow.json`; ends by running `sdlc-driver check` until it exits `0`.
  It routes to `bundle-spec.md` and `flow-spec.md` and restates no rule.
- **Item 7, OpenCode plugin.** `packages/opencode-sdlc/` provides an
  OpenCode `HarnessAdapter` and a user command. Its worker shape is
  decided after the OpenCode server check named in the HLD, before item
  7 starts; this LLD fixes only that it hosts the same core and passes
  the same driver tests through the adapter contract.
- **Item 8, `sdlc-followed-mode`.** The same algorithm in prose: the
  loop, the stage pipeline without process isolation, the same run
  folders and `result.json`, the exit rule, and `followed, not enforced`
  on the first line, in every stage's prose, and in every stop. At each
  separate-agent step it prints this handoff block and stops (UX Q2,
  open):

  ```text
  followed, not enforced
  Persona: verifier-der-530 (new session; resume this session for its later passes)
  Run folder: RUN_ROOT/verifier-der-530/run-1/
  Prompt: RUN_ROOT/verifier-der-530/run-1/prompt.md
  Open a new session, paste the prompt file, and come back when result.json exists.
  ```

- **Item 8, `sdlc-kickoff`.** Runs the readiness checklist (tracker and
  onboarding, the shell-recipe check, the tracker read, project-main
  from trunk, the run root's parent, labels mode, models and the
  spending gate), Gather, the Epic, then writes `run.json`,
  `checklist.md`, `gatherer/run-1/` (brief and a copy of the Gather
  session), and an empty `refiner/run-1/`. It prints the run root and
  `/sdlc RUN_ROOT`.

### Trust boundaries

**Actors.** The operator (trusted; holds every gate); the driver and the
plugin (trusted code from the pinned commit and the installed package);
workers (untrusted model output with the operator's shell rights); the
manager (a worker); the kickoff session model (untrusted; writes
`run.json`); the tracker, git remote, and model provider (external).

| # | Boundary | What crosses | Control | Kind |
| --- | --- | --- | --- | --- |
| TB1 | Operator → driver | `/sdlc`, `/sdlc-stop`, answers | User commands only; refused without UI or inside a worker; answers recorded only in the interactive handler while no driver runs | Enforced; headless start blocked; a worker that fakes a terminal is residual |
| TB2 | Kickoff model → `run.json` | Paths, models, tracker, spending | Strict schema; the operator confirms a summary at the first `/sdlc` and on every change | Enforced |
| TB3 | Bundle → driver | Flow, personas, skills | Pinned commit read with `git show`; bundle check; third-party bundles through INTAKE | Enforced; a malicious intake-passed bundle is out of scope |
| TB4 | Driver → worker | Prompt, facts, env | Prompt built from driver state; model or operator text fenced as data; facts hash; extension copy hashed | Enforced and detected |
| TB5 | Worker → files | `write`, `edit`, `sdlc_write` | Allowlist, path guard (fail-closed), run-folder tool | Enforced |
| TB6 | Worker → files through `bash` | Any write | Snapshot, worktree, remote-tip, ancestry, project-main checks | Detected in the run root and worktrees; residual elsewhere |
| TB7 | Worker → result | `candidate.json` | Strict validation; only validated fields route; prose never routes | Enforced |
| TB8 | Worker → tracker | Every verb, full access | Tracker-state check on state and assignee | Detected for state; residual for comment text, other tickets, reverted changes |
| TB9 | Driver → tracker | One read per check | Built-in readers; fixed Linear endpoint; read-only key | Enforced |
| TB10 | Driver and workers → git remote | Pushes with the operator's credentials | Driver code has no force option; pushes only item branches and project-main; L9 is the only deletion | Enforced for the driver; worker pushes residual except the project-main check |
| TB11 | Worker → model provider | Prompt, repo content, tool output | Local model by default; a paid slot requires the spending record | Enforced at start |
| TB12 | Proving commands | Shell lines | Only from the frozen, reviewed `groom.md` blob and the pinned bundle; hash per run | Enforced |
| TB13 | Run root → git | Design records | Only declared outputs, regular files, scanned, operator decides hits | Enforced |

**Secrets.**

| Secret | Where it lives | Who reads it | Never in |
| --- | --- | --- | --- |
| Linear read key | `tracker.linear.keyFile`, `0600`, outside run root and checkouts | Driver only, per read | Environment, run root, prompts, facts, logs, console |
| Worker tracker credential | `local`: the operator's git credentials. `linear` on Pi: not designed in this chunk ([O5](#questions-for-the-operator)) | Workers | Run root files the driver writes |
| Git credentials | The operator's credential helper or SSH agent | Driver and workers | `run.json` (origin URL without user info) |
| Model credentials | Pi's own configuration | Pi | Run root files the driver writes |

A worker can still print a secret it can read into a log or `out/`:
logs stay in the run root (`0700`); `out/` is scanned before commit.

**Egress.** The tracker API (Linear: `api.linear.app` only), the git
remote, the model provider (local by default), and whatever a worker's
`bash` or a proving command reaches. Workers can read any file the
operator can and can reach the network through `bash`: with a local
model this is residual; with a paid reviewer it is the spending and
egress gate in `run.json`.

**Data class.** The run root holds prompts, transcripts, logs, and tool
output: operator-private, never committed or published. Tracker
comments are public: only the fields in
[Tracker calls](#behavior-7-tracker-calls-per-persona). A `local` tickets branch on
a public repo is public; kickoff warns before the first write.

**Who may write what.**

| Path | Driver | Builder | Other workers | Plugin |
| --- | --- | --- | --- | --- |
| Own current run folder (worker files) | — | yes | yes | — |
| Item worktree | merges, resets of its own worktrees | its own item | no (detected) | — |
| `worktrees/integrate`, project-main | commits, merges, pushes | no (detected) | no (detected) | — |
| `run.json` | no | no | no | no; kickoff writes it |
| `driver.json`, `index.jsonl`, `plan/`, `driver/`, other persona folders | yes | no (detected) | no (detected) | `driver.json` confirmation and `asks/` answers, while no driver runs |
| Tracker | read only | per table | per table | — |

**Residual risks.** Unchanged from the HLD's [Risks](hld.md#risks),
plus: a symbolic link swapped between the guard's check and the write;
ignored files written in a worktree that `git status --porcelain` does
not show; a worker that escapes the leftover sweep; and a worker that
tampers with `driver/snapshot.json` while the driver is down, which only
weakens the interrupted-stage check.

### Mockups

`n/a`: no graphical screen. The console, chat dialogs, and run-root
files are the interface; [Console lines](#console-lines) fixes their
text. UX acceptance of [ux.md](ux.md) by the operator is pending.

### Verify

**Per item.**

| Item | Unit | Fixture and integration | Proving commands (Groom writes the final lines) |
| --- | --- | --- | --- |
| 1 | — | `docs/sdlc/fixtures/results/` holds one fixture per error code and three valid examples | `K1` and `K7` from the [writing standard](../../writing-standard.md#checks); `ls docs/sdlc/fixtures/results/*.expect.json` |
| 2 | — | `docs/sdlc/fixtures/flows/` holds one fixture per bundle-check code, including each `gate.*` row's counterexample, and `fixtures/bundles/minimal/` | `K1`, `K7`; `wc -l docs/sdlc/bundle-spec.md docs/sdlc/flow-spec.md` ≤ 150 each |
| 3 | — | `bundles/sdlc/` follows the spec; rule maps | `K1`–`K4`, `K7`; once item 5 has landed, `node packages/sdlc-driver/src/cli.ts check bundles/sdlc` |
| 5 | `node:test` per module: strict reader, result and candidate rules, front matter, bundle check, labels, groom parser, facts, scan, console | Every fixture under `docs/sdlc/fixtures/`; driver tests with the fake worker against a temporary bare origin with a `local` tickets branch | `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check` (`tsc -p . && node --test`) |
| 6 | Argv and env builder; worker extension with a fake extension API: path guard (links, `..`, `.git`, `~`), `sdlc_write`, `sdlc_result` on the shared fixtures, compaction summary | Plugin and adapter against a fake `pi` that records argv and env | `npm --prefix packages/pi-sdlc ci && npm --prefix packages/pi-sdlc run check`; then the Pi checks below |
| 4 | — | Following the skill produces a bundle under `docs/sdlc/fixtures/bundles/authored/` that passes the check | `K1`, `K7`; `node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/authored` |
| 7 | Adapter unit tests | The item 5 driver suite through the OpenCode adapter with a fake server | Set at Groom after the server check |
| 8 | — | A followed-mode walk-through of `fixtures/bundles/minimal/` writes run folders whose results pass `sdlc-driver validate` | `K1`, `K7`; the validate lines |

**Fake worker** (item 5, `test/fake-worker.ts`). The test adapter starts
it as the worker process with the `WorkerSpec` in its environment. A
JSON script, keyed by persona and run number, lists its actions: write a
file through the same rules as `sdlc_write`, write a candidate, run git
commands in its worktree, run the `local` write recipe against the
fixture tickets branch, sleep, exit with a code, or misbehave: write
outside the writable set, edit `driver.json`, push project-main, rewrite
pushed history, move the ticket to `done`, skip the extension marker,
write no candidate, or hang. It records its argv and environment.

Driver scenarios, each a test:

1. Happy path through a two-item flow with a blocker; dispatch order.
2. Proving command failure, `repair N/3` lines, budget exhaustion on the
   third failed fix, and the land-red event counting once.
3. Invalid candidate, repair in a new run folder, valid; and invalid
   twice → manager stop.
4. Manager `resume`, `defer`, `escalate`; manager invalid → driver-written
   ask; operator-only stops reject `resume`.
5. Gate answer writes `operator/run-N/result.json` and routes.
6. Land: tip unchanged; tip moved → clean (row 1) → done; tip moved →
   conflict resolved (row 2) → Review; clean then a fix → Review with
   `reviewBase` at the clean commit; builder `blocked` on merge;
   push rejected by a concurrent push → L1; push rejected by a
   pre-receive hook → L7x; post-land verifier `fail`.
7. Each post-stage check fires on its misbehavior.
8. Crash: kill the driver mid-stage, restart, `interrupted.json`, found
   report, next run number.
9. Lost session → `lost-session` ask → `replace` mints with `handoff`.
10. Proving commands edited in the item worktree have no effect; a
    `groom.md` changed after review stops ticket filing.

**Pi checks** (item 6 acceptance, on the operator's machine with Pi
0.73.1 and one local model; manual, gated by `SDLC_PI_SMOKE=1`; they
spend no money). These run the Trial questions as tests; each failure
switches to its fallback in
[Trial-dependent decisions](#trial-dependent-decisions):

- P1 (T1): `/sdlc` on a fixture run root starts the detached driver, the
  widget shows lines, and the `input` guard holds while it runs.
- P2 (T2): `pi -p "/sdlc RUN_ROOT"` refuses.
- P3 (T3): three resumed passes keep context; a missing session file is
  a `session lost` stop.
- P4 (T4): with a high `reserveTokens` in an isolated
  `PI_CODING_AGENT_DIR`, compaction fires in `-p` mode and the summary
  holds `state.md` and the facts; removing a fact from `state.md` does
  not remove it from the next summary.
- P5 (T5): ten runs of a fixed task; count valid candidates first time
  and after one repair.
- P6 (T6): `write`/`edit` absent for read-only personas; the guard
  blocks writes outside, through a symbolic link, and when the handler
  throws; `sdlc_write` stays in the run folder.
- P7 end-to-end: `smoke/run.sh` builds a fixture product repo (one small
  Node function, a `local` tickets branch, a frozen `groom.md` with two
  items, one blocking the other), seeds a run root at `@items`, and runs
  `src/driver-main.ts` with `bundles/sdlc`. Pass: both items `done` on
  the tickets branch, in order; two land commits on the fixture
  project-main with `Reviewed-by` trailers; every `result.json` passes
  `sdlc-driver validate`; `meta.json` argv shows the flags above; no
  check failed.

**Definition of done**, every item: acceptance on its ticket; the item's
proving commands green; docs current (package READMEs for 5 to 7); one
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

| Trial | Chosen design | Confirmed in 0.73.1 source | Fallback if disproved |
| --- | --- | --- | --- |
| T1 TUI during a long handler | Detached driver; the handler returns at once; widget and notify show lines; `input` guard | Handlers can spawn children; `setWidget`, `notify`, and `input` events exist. Not confirmed: that the widget timer and `notify` render after the handler returns | Lines only in `driver/console.log`; the handler prints `tail -f RUN_ROOT/driver/console.log`. If T1 instead shows the TUI stays usable during an awaited handler and the operator accepts UX Q1's console reply, item 6 may run `core.run` in process with the same adapter, and record answers from `ctx.ui` while it runs |
| T2 Headless `/sdlc` | Refused: the handler requires `ctx.hasUI` | Yes: `hasUI` is false in `-p` and JSON modes; `pi -p "/cmd"` does reach the handler | None needed |
| T3 `--session` resume | One session file per persona, resumed with `--session`; existence and header check first | Missing file → new session at that path; written after the first assistant message | Keep each item persona's Pi process alive in `--mode rpc` with the same session file, one prompt per pass; idle processes make no model call, so one large-model session still runs at a time |
| T4 Extension under `--no-extensions`; `session_before_compact` in `-p` | `--no-extensions --extension <file>`; custom summary from the hook | Explicit `-e` loads under `-ne`; the hook is fired from the mode-independent session core (read, not run) | Extension not loaded: run workers with an isolated `PI_CODING_AGENT_DIR` whose `settings.json` lists only the worker extension, keeping the `.pi/` refusal. Hook not fired in `-p`: try `--mode rpc` (fallback T3); if it never fires headless, disable auto-compaction in the isolated settings and stop with an `operator` stop when the session nears `contextWindow - reserveTokens`, so the operator can approve a `handoff` mint built from the same summary text |
| T5 Result validity | `sdlc_result` tool with exits as an enum and in-turn errors, plus one driver repair | — (needs the local model) | Below 8 of 10 valid after one repair: ask the operator for another local model or a provider mode that enforces the tool schema; the brief's one-repair limit stays |
| T6 Write controls | `--tools` allowlist, fail-closed path guard, `sdlc_write` | Yes for all three APIs | `--tools` ignored: the path guard alone limits `write` and `edit` to the writable set. Guard ineffective: detection only, reported to **security** as residual. Extension tools missing: read-only personas write their files with `bash` in the run folder; detection covers the rest |

### Clarifications of the HLD made here

1. The merge-tree re-check keeps the pre-merge parents `p1` and `p2`
   (L3, L3c).
2. A non-`pass` result from the architect's paperwork pass is an
   explicit manager stop, `paperwork failed`.
3. A merge commit whose tree differs from the clean tree always needs
   Review, whatever the builder's result says.
4. The tracker-state read uses built-in readers per backend, not a
   command string from the repo skill; the repo skill's Mapping supplies
   state names.
5. Ticket filing ends with items `ready` and the Epic `in_progress`, per
   [Groom File](../../../docs/sdlc/groom-step.md#3-file) steps 4–5; the
   HLD table says `backlog` ([O3](#questions-for-the-operator)).
6. A push the driver cannot retry is recorded as a command `fail`,
   because the result contract forbids `blocked` for a command; the
   stop kind is still `blocked`.
7. Reserved exits accept `fail` only on driver-authored results.
8. Invalid-result repairs get their own run folder; the invalid run's
   `result.json` is a driver-authored `fail`.
9. Pi's JSON mode exits `0` on a model error (the HLD's exit-1 fact
   holds for text mode); the driver reads `stopReason` from the stream.
10. Prompts go on stdin; worktrees and driver folders use the label
    suffix; `repo.git/` is added to the run root.
11. Pi workers have no MCP client, so repo tracker recipes must run from
    `bash`.

### Groom split (proposal)

| G | Item | Blocked by | Reason |
| --- | --- | --- | --- |
| G1 | Result format (DER-529) | — | — |
| G2 | Bundle and flow spec, fixtures | G1 | Candidate and `choice` rules extend item 1's fields |
| G3 | SDLC bundle, `test-failure-handler`, tracker wiring, `bundle-runs.md` | G2 | Written in the spec's format |
| G5 | Core driver | G1, G2 | Implements both specs; its tests read their fixtures |
| G6 | Pi plugin, worker extension, Pi checks | G3, G5 | Hosts the core; the smoke runs `bundles/sdlc` |
| G4 | `bundle-authoring` | G6 | Brief: after the Pi path works |
| G7 | OpenCode plugin | G6 | Brief: after the Pi path works |
| G8 | `sdlc-followed-mode`, `sdlc-kickoff` | G6 | Brief: after the Pi path works |

Waves: 1: G1; 2: G2; 3: G3, G5; 4: G6; 5: G4, G7, G8. No gate items.
Item 5 is the largest for a 100k-token builder. Groom may split it into
G5a (strict reader, result and candidate rules, front matter, bundle
check; ← G1, G2), G5b (run root, state machine, stage pipeline, stops,
fake worker; ← G5a), and G5c (git, land, proving commands, snapshot,
tracker readers, scan; ← G5b), with G6 ← G3, G5c.

### Questions for security

| # | Question | Recommendation |
| --- | --- | --- |
| S1 | Linear read key: storage and scope | A dedicated personal API key with the **Read** permission only, limited to the one team; in a `0600` file outside every checkout and run root, path in `run.json`; read per request, never in any environment or file the driver writes; rotate on suspicion |
| S2 | Worker tracker credentials when Linear backs a Pi run | Defer: this chunk proves Pi on `local`. When designed, a second key limited to Write, Create issues, and Create comments on the one team, in the worker environment only |
| S3 | `bash` is not path-guarded; workers read any file and reach the network | Accept as residual with the detection checks (the HLD's non-goal). Note Pi's example sandbox extension (bubblewrap) as a later option after intake |
| S4 | Driver bare clone in the run root, hooks off for driver git, `.pi/` refusal in worker cwd | Accept |
| S5 | Same-item claim rule in `tracker-sdlc` and the `local` recipe (protected rules) | Read at Review with the rule maps; keep contract v2 with the kickoff check |
| S6 | Design-record scan patterns, and the operator's `allow` on a hit | Accept the list; `allow` stays an operator answer recorded in `asks/` |
| S7 | Proving commands inherit the operator's environment minus `SDLC_*` and `env.scrub` | Accept; kickoff's default `env.scrub` lists tracker key variables |
| S8 | Dev dependency on a pinned `typescript` for type checking in items 5 and 6 | Allow one exact-pinned dev dependency with a lockfile, through INTAKE; no runtime dependency |
| S9 | Pinned bundle commit | Require that the commit is reachable from the skills home's trunk or from this chunk's project-main; else the operator confirms it at the first `/sdlc` |

### Questions for the operator

| # | Question | Recommendation |
| --- | --- | --- |
| O1 | Run a Trial before Build? | No separate Trial. This LLD keeps every Pi fact behind the adapter and the worker extension, so a fallback changes item 6, not item 5's shape; item 6 runs T1–T6 as P1–P6 first |
| O2 | UX Q1–Q3 | Accept the recommended defaults this LLD assumes: replies at the next `/sdlc` (Q1); the handoff block in [Behavior 8](#behavior-8-later-items-4-7-8) (Q2); `index.jsonl` (Q3) |
| O3 | Ticket filing end state: Groom says `ready` and Epic `in_progress`; the HLD table says `backlog` | Follow Groom; the HLD row gets a clarification |
| O4 | Same-item claim rule: bump `tracker-sdlc` to contract v3, or keep v2 and have kickoff check the repo skill | Keep v2; kickoff checks for the same-item sentence and stops without it. A bump would mark every repo skill out of date for a rule that only bundle runs use |
| O5 | This repo's Linear skill uses MCP, which Pi workers lack | Prove Pi on the `local` adapter in this chunk; add shell recipes for Linear later as a new item after S2 |
| O6 | Pi version: 0.73.1 (checked here, now deprecated) or `@earendil-works/pi-coding-agent` 1.x | Pin 0.73.1 for this chunk; the driver checks the version at start; move to 1.x as a later item that reruns P1–P7 |
| O7 | Skill ids `test-failure-handler`, `bundle-authoring`, `sdlc-followed-mode`, `sdlc-kickoff` | Accept |
| O8 | Item 5 split into G5a–G5c | Let Groom split it |

### Rollout / rollback

The chunk adds new files and routes; existing runs that use sub-agents
are unaffected except by the same-item claim rule, which applies only
inside bundle runs. Rollback is reverting the items' land commits on
project-main before Trunk; run roots are outside git and need no
cleanup.
