# LLD — solo-dlc: the SDLC on a harness without sub-agents

- Slug: `solo-dlc`
- HLD: [maintainers/design/solo-dlc/hld.md](hld.md) (agent review passed
  in round 4; operator acceptance pending). UX: [ux.md](ux.md); stories:
  [user-stories.md](user-stories.md); comparables:
  [comparables.md](comparables.md). Brief: DER-421 brief v3, confirmed
  2026-10-18.
- Tickets this LLD covers: DER-421 (chunk); brief items 1–8 (item 1 is
  DER-529; the others get ids at Groom)
- Date: `2026-10-18`; fix round 1 after the security and adversarial
  reviews of 34e1278; cleanup round 2 after the security and LLD
  re-reviews of de7c438 passed, applying their recommendations, same day
- Status: **draft, awaiting operator acceptance.** The security
  re-review of de7c438 passed. Architect acceptance is this draft.
  Groom and Build start only after **security** and then the operator accept it
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
  a valid candidate: command stages (as the command wrapper), gate
  nodes, failed checks on model stages, and invalid results.
- **Driver-fixed exits**: exits that the flow spec, not a flow file,
  defines for stages the driver adds inside or around nodes: land
  sub-stages, paperwork, and manager stages
  ([Driver-fixed exits](#driver-fixed-exits)).
- **Pinned commit**: the skills-home commit recorded in `run.json`.
  The driver reads `flow.json`, personas, and packed skill bodies only
  from that commit, never from a working tree.

## Required

### Paths / modules

| Path | Item | What |
| --- | --- | --- |
| `docs/sdlc/stage-result.md` | 1 | Edited in place: v1 fields, rules, examples; stays ≤150 lines per the [line budget](#line-budget-for-stage-resultmd) |
| `docs/sdlc/fixtures/results/` | 1 | Valid and invalid result fixtures, each with an `.expect.json` |
| `docs/sdlc/bundle-spec.md` | 2 | Owner: bundle layout, `bundle.md`, persona files, prompt kinds, placeholders. ≤150 lines |
| `docs/sdlc/flow-spec.md` | 2 | Owner: `flow.json`, exits, reserved exits, candidate rules, bundle check, error codes. ≤150 lines |
| `docs/sdlc/fixtures/flows/`, `docs/sdlc/fixtures/bundles/` | 2 | Flow and bundle fixtures with expected error codes |
| `docs/INTAKE.md` | 2 | New `## Script records` section: one line per bundle script **security** cleared ([Bundle layout](#bundle-layout-and-bundlemd)) |
| `docs/sdlc/bundle-runs.md` | 3 | Owner of every rule change in [HLD Rule changes](hld.md#rule-changes), plus run-root formats for agents. ≤150 lines |
| `bundles/sdlc/` | 3 | The SDLC bundle: `bundle.md`, `flow.json`, `personas/*.md` |
| `skills/test-failure-handler/SKILL.md` | 3 | New first-party skill, `SOURCES.md` row |
| `skills/tracker-sdlc/SKILL.md`, `adapters/local.md` | 3 | Same-item claim rule (protected rules: rule maps, **security** read) |
| One-line routes in `docs/SDLC.md`, `docs/sdlc/subagents.md`, `build-review.md`, `branches-and-lands.md`, `plan-trial-spec.md`, `stage-result.md`, `skills/debug/SKILL.md` | 3 | Each route names the rule and links `bundle-runs.md` |
| `packages/sdlc-driver/` | 5 | Core driver: TypeScript, Node built-ins only, no Pi dependency |
| `packages/pi-sdlc/` | 6 | Pi plugin: `/sdlc`, the Pi adapter, the detached driver entry, the worker extension, the smoke test |
| `skills/bundle-authoring/SKILL.md` | 4 | New skill |
| `maintainers/design/solo-dlc/opencode-server.md` | 7 | One-page OpenCode server note; G7's first deliverable ([Groom split](#groom-split-proposal)) |
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
    snapshot.ts                # pre/post hashes, worktree, refs, and tickets checks
    tracker.ts                 # the repo skill's local read recipe, as fixed git argv
    groom.ts                   # frozen groom.md parser
    prompts.ts  facts.ts  scan.ts  console.ts  labels.ts  env.ts
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
`{{stopRun}}`, `{{question}}`, `{{choices}}`, `{{answer}}`, `{{record}}`,
`{{ask}}`, `{{extracted}}`.
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
| `ask` | `gate` | The ask text for the manager's `ask-human.md` draft: the decision, the committed files that hold its facts and the recommendation, and what to quote from them. The `gate` prompt passes it as `{{ask}}` |
| `builder`, `prove`, `verify`, `review` | `land` | Node ids: the builder model node, the proving `command` node, the verifier model node, and the Review node |
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
- A `land` node has exactly one exit, `done`, with `["pass"]`, to
  `@done`.

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
| Answer or replacement | `answer`, `handoff` | The exits of the stopped node or stage |

**Candidate rules.** A worker writes `candidate.json` with the
`sdlc_result` tool or with `sdlc_write`
([Worker extension](#worker-extension)).

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
| B10 | A `land` node names existing nodes of the right kind: `prove` is an item `command` node with `commands: "groom"`; `verify` is a model node with job `verifier`; `review` has step `Review`, job `reviewer`, and `checks` holding `intake`, `sha-pins`, `trust-boundary` | `flow.land-ref`, `flow.review-checks` |
| B11 | Gate rows below hold on every path | `gate.*` |
| B12 | `bundle.md` headings; no symbolic links; size caps; every `scripts/` file listed with its hash and intake record; outside reviewed history, that record and hash present in `docs/INTAKE.md` at a derived reviewed ref ([Script records](#bundle-layout-and-bundlemd)) | `bundle.layout`, `bundle.script-intake` |
| B13 | `extract` only on `gate` exits; `from` is a normalized repo-relative path; `to` matches `^[a-z0-9-]{1,40}\.md$` | `flow.extract` |

Gate rows. The checker finds the nodes by kind, step, job, outputs, and
gate tag, so a flow cannot avoid a row by renaming nodes:

| Code | Any path from | Reaching | Must pass, in this order |
| --- | --- | --- | --- |
| `gate.comparables` | `entry` | The HLD node: chunk `model`, step Plan, an `outputs` path ending `/hld.md` | The comparables node: chunk `model`, step Plan, an `outputs` path ending `/comparables.md` |
| `gate.plan` | `entry` | The Spec node: `model`, step Spec, an `outputs` path ending `/lld.md` | The `gate` node tagged `plan` |
| `gate.trial` | `entry` | The Spec node, as in `gate.plan` | The `gate` node tagged `trial` |
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
| `brief-gate` | Brief | Brief | gate | — | tag `brief`; ask: "Confirm the brief as the refiner left it, or say what to revise. Quote the refiner's proposed cuts and open points from its last `result.md`." | `confirmed` [pass] → `comparables`; `revise` [fail] → `refine` |
| `comparables` | Plan | Plan | model | architect | `{design}/comparables.md` | `hld` [pass] → `hld` |
| `hld` | Plan | Plan | model | architect | `{design}/hld.md` | `ux` [pass] → `ux` |
| `ux` | Plan | Plan | model | designer | `{design}/ux.md`, `{design}/user-stories.md` | `review` [pass] → `ux-review` |
| `ux-review` | Plan | Plan | model | ux-reviewer | — | `accept` [pass] → `ux-gate`; `fix` [fail] → `ux` |
| `ux-gate` | Plan | Plan | gate | — | tag `ux`; ask: "Accept `{design}/ux.md` and `{design}/user-stories.md`, waive the UX review in writing, or say what to revise. Quote the UX reviewer's verdict and open findings, and each open UX question with the designer's recommendation." | `accepted` [pass] → `plan-gate`; `waived` [pass] → `plan-gate`; `revise` [fail] → `ux` |
| `plan-gate` | Plan | Plan | gate | — | tag `plan`; ask: "Accept `{design}/hld.md`, or say what to revise. Quote each item under its `## Open` heading with the HLD's default or recommendation." | `accept` [pass] → `trial-gate`; `revise` [fail] → `hld` |
| `trial-gate` | Trial | Trial | gate | — | tag `trial`; ask: "Run a Trial before Spec? Quote each unconfirmed fact and the recommendation from the `## Trial question` section of `{design}/hld.md`. On yes, the driver writes the Trial kickoff prompt to a file and prints its path." | `trial` [pass] → `trial-done`, extract `{design}/hld.md` heading `Trial kickoff prompt` to `trial-kickoff.md`, say `Trial kickoff prompt written: {{extracted}}`; `skip` [pass] → `spec` |
| `trial-done` | Trial | Trial | gate | — | tag `trial-done`; ask: "Is the Trial done, with each verdict recorded under `{design}/poc/`? Quote each verdict and any HLD change the Trial report recommends." | `done` [pass] → `spec`; `revise` [fail] → `hld` |
| `spec` | Spec | Spec | model | architect | `{design}/lld.md` | `mockups` [pass] → `mockups` |
| `mockups` | Spec | Spec | model | designer | `outputDirs` `{design}/mockups/` | `none` [pass] → `security`, exit check `no-screen`; `review` [pass] → `mockup-review` |
| `mockup-review` | Spec | Spec | model | ux-reviewer | — | `accept` [pass] → `mockup-gate`; `fix` [fail] → `mockups` |
| `mockup-gate` | Spec | Spec | gate | — | tag `mockup`; ask: "Accept the mockups under `{design}/mockups/`, or say what to revise. Quote the UX reviewer's verdict and open findings." | `accepted` [pass] → `security`; `revise` [fail] → `mockups` |
| `security` | Spec | Spec | model | security | checks `authz`, `secrets`, `egress`, `data-class`, `writers` | `accept` [pass] → `spec-gate`; `fix` [fail] → `spec` |
| `spec-gate` | Spec | Spec | gate | — | tag `spec`; ask: "Accept `{design}/lld.md`, and accept in writing each residual its trust-boundary section lists under operator must accept; or say what to revise. Quote security's findings with severities, and each open operator question with the LLD's recommendation." | `accept` [pass] → `groom`; `revise` [fail] → `spec` |
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

The groom reviewer checks that the block agrees with the prose. At
freeze, the manager fills the `Tickets:` line as
`` `G1` = `der-a530`, `G2` = `der-a531` ``; the driver parses only that
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
  "chunk": {"slug": "solo-dlc", "epic": "der-e421"},
  "bundle": {"id": "sdlc", "home": "/abs/path/to/skills-home", "commit": "<40-hex>"},
  "repo": {"origin": "git@github.com:OWNER/REPO.git", "trunk": "main",
           "projectMain": "integrate/solo-dlc", "designDir": "maintainers/design/solo-dlc"},
  "tracker": {"backend": "local", "skill": ".agents/tracker/SKILL.md",
              "keyPattern": "^der-[a-z0-9]{4}$", "local": {"branch": "tickets"}},
  "mode": "enforced",
  "harness": {"name": "pi", "package": "@mariozechner/pi-coding-agent", "version": "0.73.1",
              "bin": "/abs/path/to/pi", "integrity": "sha512-<base64>",
              "treeSha256": "<hex>"},
  "models": {"default": {"model": "local/qwen-coder", "contextWindow": 131072, "paid": false}},
  "spending": null,
  "labels": {"mode": "plain"},
  "limits": {"repairs": 3, "invalidRepairs": 1},
  "env": {"scrubExtra": []},
  "gather": {"sessions": ["gatherer/run-1/session.jsonl"]},
  "createdAt": "2026-10-18T07:00:00Z"
}
```

- `repo.origin` must carry no user info (`://user@` with a password, or
  a token) and no query string. SSH and plain HTTPS forms are allowed.
- `tracker.backend`: driven runs support `local` only in this chunk
  (security ruling S1). Kickoff refuses any other backend, and `/sdlc`
  refuses to start a run root whose `run.json` names one, with the line
  `tracker backend <name> is not supported for driven runs yet; use local`.
  Linear for driven runs, both the driver's reads and the workers'
  writes, is the later item G9 with its own security gate
  ([Groom split](#groom-split-proposal), O5).
- `harness.bin` is the absolute path of the `pi` executable; the
  optional `harness.node` is the Node binary for the detached driver.
- **Harness pin.** `harness.package` and `harness.version` name the Pi
  release; the text supports both `@mariozechner/pi-coding-agent`
  0.73.1 and `@earendil-works/pi-coding-agent` 1.x, and the operator
  picks one (O6). Kickoff installs that exact version with npm, which
  checks the registry's `dist.integrity` while it installs, and records
  that value as `harness.integrity`. Kickoff then records
  `harness.treeSha256`: when `harness.bin` is a compiled binary, the
  SHA-256 of that file; otherwise the SHA-256 of the sorted list of
  `<path> <sha256>` lines for every regular file under the installed
  package folder, its `node_modules/` included. An installed package
  keeps no tarball to re-check `integrity` against, so the
  [Start](#start) check uses `treeSha256`.
- `models.<slot>.model` is the Pi `--model` value. A slot with
  `"paid": true` requires `spending` = `{"askId": "kickoff-1",
  "approvedAt": "<UTC>", "text": "<the operator's words>"}`.
- `env.scrubExtra`: variable names added to the fixed denylist in
  [Environment scrub](#environment-scrub). It can only add names.
- At the first `/sdlc`, and whenever its hash changes, the plugin shows
  a summary of `run.json` (bundle commit, repo, tracker, harness pin,
  models, spending, labels) and records the operator's yes as
  `runJsonSha256` in `driver.json`. No yes, no run.
- **Bundle commit outside reviewed history (S9, N2, N4).** The driver
  derives the reviewed refs itself and never reads them from
  `run.json`. They are two refs in the skills home:
  `origin/<trunk>`, where `<trunk>` is the branch that
  `git -C <home> symbolic-ref refs/remotes/origin/HEAD` names, and
  `origin/<projectMain>`, with `run.json` `repo.projectMain`, used only
  when that ref exists in the skills home (this chunk's does). The
  driver does not fetch the skills home, so these are the operator's
  local remote-tracking refs as last fetched (a residual:
  [Trust boundaries](#trust-boundaries)). A missing `origin/HEAD` or
  `origin/<trunk>` stops the start and names the ref; the driver
  never treats a missing ref as "not an ancestor," and an absent
  `origin/<projectMain>` is shown as `absent`. The
  summary shows the full 40-hex bundle commit and, for each derived
  ref, the result of
  `git -C <home> merge-base --is-ancestor <commit> <ref>`. When the
  commit is an ancestor of neither ref, the summary also shows the
  SHA-256 of every file under the bundle's `scripts/` and `personas/`
  at that commit, and each script's intake record. A script whose
  record and hash are not in `docs/INTAKE.md` at a derived ref fails
  the bundle check (`bundle.script-intake`,
  [Script records](#bundle-layout-and-bundlemd)) before that question.
  The confirmation is then `ctx.ui.input`, not `confirm`: the
  operator's answer must equal the full SHA, else no run.
- **Other refs force the typed SHA.** `bundle.reviewedRefs` is
  optional and never used for the ancestry test. When it is present
  and lists any ref other than the two derived refs, the driver takes
  the typed-SHA path above, even when the commit is an ancestor of a
  derived ref, and the summary names the extra refs.

#### `driver.json`

```json
{
  "schemaVersion": 1,
  "runJsonSha256": "<hex>",
  "bundle": {"commit": "<40-hex>", "checkedAt": "<UTC>"},
  "worker": {"extension": "driver/worker-ext/sdlc-worker-1a2b3c4d5e6f.ts",
             "sha256": "<hex>", "harnessVersion": "0.73.1"},
  "chunk": {"node": "spec", "state": "active", "stop": null, "askId": null,
            "pendingRoute": null, "unposted": null},
  "groom": {"path": "maintainers/design/solo-dlc/groom.md", "reviewedCommit": "<sha>",
            "frozenCommit": "<sha>", "commandsSha256": "<hex>"},
  "items": {
    "der-a530": {"state": "active", "node": "verify", "land": null, "landReentry": false,
                 "repairs": 1, "sentBack": true, "fixPending": false,
                 "lastPushed": "<sha>", "reviewBase": "<sha>",
                 "stop": null, "askId": null}
  },
  "sessions": {"builder-der-a530": {"path": "builder-der-a530/session.jsonl",
               "state": "live", "packed": ["tdd", "yagni", "debug"]}},
  "runs": {"builder-der-a530": 5, "prove-der-a530": 4},
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
| `items.*.land` | `null` outside the land node, else `{"phase", "p1", "p2", "cleanTree", "cleanCommit", "landCommit"}`; `phase` is one of the [Land](#land-sub-machine) rows |
| `items.*.landReentry` | `true` from L3b or L6r until the item next enters the land node at L1; selects the console label ([Land](#land-sub-machine)) |
| `repairs`, `sentBack`, `fixPending` | [Repair counter](#repair-counter) |
| `lastPushed` | Item branch tip the driver last pushed |
| `reviewBase` | Item `HEAD` at the last Review pass, or the clean merge commit after a row-1 classification |
| `stop` | `{"kind", "run", "operatorOnly", "resumeWith"}` while the manager handles a stop. `resumeWith` is `{"persona", "prompt", "log"}`: who the driver resumes, and with which prompt kind, when the answer is `resume` |
| `sessions.*.state` | `live`, `lost` (stopped; ask open), `replaced` (minted again on the operator's answer; the old file is kept as `session.lost-<UTC>.jsonl`) |
| `sessions.*.packed` | Skill ids already in that session's transcript |
| `inFlight` | `{"run", "scope", "node", "kind", "prompt", "repairOf", "invalidRepairs", "pid", "startedAt"}` while a stage runs. `kind` is `model` or `command`. `invalidRepairs` is `1` on an invalid-result repair stage, else `0`; `repairOf` names the run it repairs |
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
`interrupted`, or `found`. Resume never reads this file; it is history
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
`scan-secret` (choices `revise`, `defer`; never `allow`), `pi-dir`
(choices `allow`, `defer`), or `operator-stop` (free text). An answer is
`{"choice": "<one of choices or null>", "text": "<verbatim>", "at": "<UTC>"}`.
`ask-N.md` renders the same fields with the message and the answer
verbatim. Answers are recorded only by the plugin's `/sdlc` handler, in
the operator's interactive session, while no driver holds the lock
([Host shape](#host-shape-and-sdlc)).

#### Run folder

| File | Writer | Notes |
| --- | --- | --- |
| `meta.json` | driver | Node, scope, persona, `new` or `resumed`, prompt kind, `repairOf`, start and end times, the worker argv; `recordCommit`, the design-record commit, written before its push ([Design-record commits](#design-record-commits) step 5) |
| `prompt.md` | driver | The prompt sent on stdin |
| `candidate.json` | worker | Through `sdlc_result` or `sdlc_write` |
| `result.json` | driver | The validated result, or a driver-authored one |
| `result.md` | worker | Prose |
| `state.md` | worker | Copied by the driver from the persona's previous run, or from the template, before the run starts |
| `ledger.json` | verifier | [Verifier ledger](#sdlc-personas-and-prompts) |
| `ask-human.md` | manager | On `escalate` |
| `out/` | worker | Files for the repo, at their repo-relative paths |
| `commands.json` | driver | Command stages: one entry per command: index, line, exit code, duration, log path |
| `check.json` | driver | Command stages only: the post-stage check that failed, when one did |
| `<extract>.md` | driver | Gate results only: the section an exit's `extract` copied, such as `trial-kickoff.md` |
| `logs/` | driver, extension | `worker.jsonl` (Pi's JSON stream), `worker.stderr`, `ext.json` (extension load marker; missing → `check failed: extension`), `prove-K.log` |
| `interrupted.json` | driver | Present when the run was interrupted; such a folder never gets `result.json` and is never reused. Holds `recordCommit` when the pushed record exception applied ([Start](#start) step 5) |

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

1. **Kickoff** reads the tracker's key pattern and the longest id it
   allows. `local` ids (`<prefix>-xxxx`, at most 11 characters) fit
   `plain`. A pattern that allows ids longer than 23
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
2. Validate `run.json`; check `runJsonSha256`. Refuse a
   `tracker.backend` other than `local` with the line in
   [`run.json`](#runjson). Check the harness version equals
   `harness.version` and the installed tree's hash equals
   `harness.treeSha256`, hashing every file in full; else stop and
   print both values of each. The driver keeps a stat cache of the
   tree (path, inode, size, `mtime`, `ctime`, SHA-256) in
   `driver/harness-tree.json`, written only here, so the
   [stage pipeline](#stage-pipeline) can re-check the hash
   before each worker spawn, in memory. The re-check walks the whole
   tree again: it hashes every file that is not in the cache (an added
   file) or whose stat differs, counts every cached file that is gone
   (a removed file), and reuses the cached hash only for a file whose
   path and stat both match. The `snapshot` check covers the cache file
   like any driver file.
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
   `git -C repo.git update-ref -d refs/heads/integrate-empty`. Then run
   the bundle check at the pinned commit; any error stops the start
   with the error lines.
4. Install the worker extension; if its hash differs from
   `driver.json`, print one line and record the new hash.
5. If `inFlight` is set, the previous driver died mid-stage: write
   `interrupted.json` in that run folder, run the
   [post-stage checks](#post-stage-checks) for its stage kind against
   `driver/snapshot.json`, clear `inFlight`, and append an
   `interrupted` event. A failed check is an `operator` stop. Otherwise
   the next run of that scope and node uses the interrupted record's
   `prompt`, `repairOf`, and `invalidRepairs`, so an interrupted repair
   is not granted a second repair. An interrupted paperwork stage is
   replayed from `chunk.pendingRoute`
   ([Design-record commits](#design-record-commits) step 7).

   **Pushed record exception.** An interrupted HLD or Spec stage (not
   its paperwork) may have pushed its design record before it died.
   Let `C` be `recordCommit` in the interrupted run's `meta.json`
   ([Design-record commits](#design-record-commits) step 5) and `S` the
   snapshot's project-main tip. When `C` is set, the `refs` and
   `worktrees` checks allow exactly one difference:
   `refs/heads/<projectMain>` now points at `C` and
   `git merge-base --is-ancestor S C` succeeds, and
   `worktrees/integrate` has `HEAD` equal to `C` and the same
   `git status --porcelain` as before. Every other ref and every other
   worktree must still be equal, and every other check runs unchanged;
   any other difference is an `operator` stop. When the exception
   applies, write `recordCommit: C` into `interrupted.json`, and, in the
   `driver.json` write that clears `inFlight`, set `projectMainSeen` to
   `C` and `chunk.unposted` to the node, the record path, and `C`. The
   node then runs again; [Stage pipeline](#stage-pipeline) step 11 turns
   `chunk.unposted` into `chunk.pendingRoute` so that paperwork runs for
   `C`.
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
3. An item that is `pending` becomes `active`: fetch, set
   `projectMainSeen` to the fetched tip, create its branch from that tip
   with `git worktree add -b <branch> worktrees/<suffix> <tip>`, push
   the branch without force, and set `lastPushed`.
4. Run the scope's current node ([Node routing](#node-routing)). For
   the chunk with `chunk.pendingRoute` set, run the architect's
   paperwork stage instead
   ([Design-record commits](#design-record-commits) step 7).
5. Repeat.

One stage runs at a time, model or command, across all scopes.

#### Stage pipeline

Every stage runs these steps: model nodes, command nodes, land
sub-stages, paperwork, manager stages, and repairs. Steps marked
*(model)* run only for model stages; command stages skip them and the
worker-only checks.

1. **Run folder.** N = `runs[folder] + 1`. If `<folder>/run-N/` already
   exists and holds a `meta.json`, increment N again. An empty folder
   (kickoff's `refiner/run-1/`) is used as is.
2. *(model)* **Session.** If `sessions[persona]` exists, this is a
   resume: the file must exist and `adapter.sessionLooksValid` must
   pass, else a `lost-session` stop. If it does not exist, this is a
   mint: the file must not exist, else an `operator` stop
   (`unexpected session file`).
3. **Files.** *(model)* Copy `state.md` from the persona's previous run,
   or the template; write `prompt.md` ([Prompts](#prompts)); write the
   facts file. Every stage: write `meta.json`.
4. **Snapshot.** Set `inFlight` (with `kind`, `prompt`, `repairOf`, and
   `invalidRepairs`), write `driver.json`, then take the pre-stage
   snapshot that the [post-stage checks](#post-stage-checks) for this
   stage kind need, and write `driver/snapshot.json`.
5. **Run.** Print the start line, except a proving-command stage
   while `items.*.land` or `landReentry` is set, which prints none
   ([console mapping](#land-sub-machine)). Model: re-check
   `harness.treeSha256` from the stat cache ([Start](#start) step 2);
   a mismatch finishes the stage as a failed check
   (`check failed: harness`, step 6) without spawning. Then call
   `adapter.runWorker`;
   after it returns, kill leftovers
   ([Pi adapter](#pi-adapter-and-worker-command-line)). Command: run
   the [command body](#command-body).
6. **Checks.** Run the post-stage checks for this stage kind, whatever
   the candidate or command result holds. The first failure finishes
   this stage and does not enter steps 7–11: on a model stage, write a
   driver-authored `fail` (`choice: operator`) naming the check and
   keep `candidate.json`; on a command stage, keep the wrapper result
   and write `check.json`. Then clear `inFlight`, append `end`, print
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
   and the session file now exists, record `sessions[persona]`; if the
   file does not exist (Pi writes it only after the first assistant
   message), the next run is a mint again.
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

#### Command body

1. Read the commands: for `"groom"`, from the frozen `groom.md` blob
   ([Proving commands](#proving-commands)); else the bundle's
   `scripts/` files at the pinned commit, copied into the run folder.
2. Run each command in order in the stage's worktree (the item
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

- every `SDLC_*` variable (the adapter then sets the worker's own),
  and `PI_CODING_AGENT_SESSION_DIR`;
- the fixed denylist: `LINEAR_API_KEY`, `LIN_API_KEY`, `GH_TOKEN`,
  `GITHUB_TOKEN`, `NPM_TOKEN`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`,
  every name matching `AWS_*`, and every name ending in `_KEY`,
  `_TOKEN`, or `_SECRET`;
- each name in `run.json` `env.scrubExtra`.

This is hygiene, not a boundary. A worker or a proving command can still
read any credential file the operator can read and can use the
operator's git credential helper or SSH agent. Pi reads model
credentials from its own configuration; a model slot whose key comes
from a scrubbed variable cannot start, and the kickoff's model line
checks each slot's key source and stops with that reason. Proving lines
come only from the frozen `groom.md` blob and the pinned bundle's
`defaults.prove` ([Proving commands](#proving-commands)).

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
project-main tip. `H` is the item `HEAD`.

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
5. Before each push, write the commit's SHA as `recordCommit` in this
   run's `meta.json` (atomic write), so that a restart can tell the
   driver's own push from any other
   ([Start](#start) step 5, pushed record exception). Push without
   force. Exit `0`: set `projectMainSeen` to the pushed commit.
   Non-zero: fetch; if the tip moved as in [Land](#land-sub-machine)
   L7m, detach at the new tip, copy and commit again, record the new
   SHA the same way, and push, at most 10 rounds, then a `blocked`
   stop. Otherwise a `blocked` stop, no retry.
6. `recordCommit` in `meta.json` is the pushed commit. For `groom`, it
   becomes `groom.reviewedCommit` when the next `groom-review` passes.
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
     it interrupted and runs its post-stage checks. If nothing was
     pushed, the checks run as for any stage and the node runs again.
     If project-main is at the run's `recordCommit` `C`, the checks pass
     only under Start step 5's pushed record exception; the node then
     runs again, step 4 stages nothing unless the re-run changes the
     file, and [Stage pipeline](#stage-pipeline) step 11 sets
     `pendingRoute` from `C`, so paperwork runs. A re-run that changes
     the file commits its own record, which replaces `C`. Any other
     change is an `operator` stop and the node does not run again; that
     includes a crash after step 4's commit and before its push, which
     leaves the integration worktree at an unpushed commit.
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

#### Post-stage checks

Every check named here is the `check` field of a failed-check result.
"Worker stage" means a model stage. The pre-stage snapshot (pipeline
step 4) records what each check compares.

| Check | After | How |
| --- | --- | --- |
| `snapshot` | every stage | Walk `RUN_ROOT` without following symbolic links. Excluded: the current run folder, the current persona's session file, `worktrees/`, `driver/snapshot.json`, and everything under `repo.git/` except `config`, `hooks/`, and `info/`. Record path, type, mode, size, and SHA-256 (the target string for a link). A cache keyed by inode, size, and `ctime` skips rehashing unchanged files. Any difference is a failure |
| `worktrees` | every stage | For each worktree outside the stage's writable set: `HEAD` and `git status --porcelain` equal before and after. A command stage's writable set is its run folder and the worktree it runs in. At restart only, an interrupted HLD or Spec stage's `worktrees/integrate` may sit at its `recordCommit` ([Start](#start) step 5) |
| `refs` | every stage | `git ls-remote origin` before and after: every ref name and tip equal, except `refs/heads/tickets`, which the `tickets` check owns. A ref added, deleted, or moved fails, whoever moved it. At restart only, an interrupted HLD or Spec stage's project-main may have fast-forwarded to its `recordCommit` ([Start](#start) step 5) |
| `tickets` | every stage | [Tickets content check](#tickets-content-check) |
| `ancestry` | builder stages | `lastPushed` is an ancestor of `HEAD` (pipeline step 9) |
| `project-main` | every worker stage | Fetch; let `M0` be `projectMainSeen` and `M1` the fetched tip. For each active item with `HEAD` `H`, no commit in `git rev-list H ^M0 ^<each commit in lands>` is also in `git rev-list M1 ^M0`. Then `projectMainSeen = M1` |
| `extension` | worker stages | `logs/ext.json` exists and names this persona and facts hash. Missing or wrong: `check failed: extension`, an `operator` stop with no repair, because the stage ran without the path guard and the compaction hook |
| `tracker-state` | worker stages | [Tracker-state check](#tracker-state-check) |

**`projectMainSeen`.** The driver also sets it to the tip it fetches at
loop step 3, land L1, and design-record step 1, and to the commit it
pushes at L8 and design-record step 5. So `M0` is always a tip the
driver saw outside a worker stage, a land merge never counts against
the item it lands, and an item branched from or merged with a newer tip
does not fail. The `refs` check catches any project-main move during a
worker stage; this check also covers commits that reach project-main
between stages.

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
environment ([Pi adapter](#pi-adapter-and-worker-command-line)). Git
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
(`core.hooksPath=/dev/null`), sets `GIT_NO_REPLACE_OBJECTS=1`, and has
no force option in its code path. The only deletion of a remote product branch is L9. The first-start
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
| `repair budget exhausted` | Repair counter | `escalate` | `operator-stop` |
| `check failed: <check>` | A post-stage check (`snapshot`, `worktrees`, `refs`, `tickets`, `ancestry`, `project-main`, `extension`, `tracker-state`, `tracker-read`), the pre-spawn `harness` re-check, `extract`, `unexpected session file`, `pushed history rewritten` | `escalate` | `operator-stop` |
| `scan hit` | Design-record step 3, no credential hit | Not resumed: the driver writes the ask | `scan-hit` |
| `scan hit: credential` | Design-record step 3, a credential hit | Not resumed: the driver writes the ask | `scan-secret` |
| `session lost: <file>` | Pipeline step 2 | `escalate` | `lost-session` |
| `project Pi files: <path>` | `.pi/` in a worker cwd ([Pi adapter](#pi-adapter-and-worker-command-line)) | `escalate` | `pi-dir` |
| `post-land verify failed` | L9 | `escalate` | `operator-stop` |

1. The driver sets the scope's `stop`, with `resumeWith` defaulting to
   the stopped persona and the `answer` prompt (the budget stop names
   the builder and its pending prompt kind; see
   [Repair counter](#repair-counter)), prints the `STOP` line, and
   resumes `manager` with the `stop` prompt (or `gate`). Scan stops
   skip the manager, as their rows say.
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
| `lost-session` | `replace` | Moves the old file to `session.lost-<UTC>.jsonl` if present, mints a new session with the `handoff` prompt (last `state.md`, facts, the answer) |
| `lost-session` | `defer` | Leaves the scope `waiting` |
| `scan-hit` | `allow` or `revise` | [Design-record commits](#design-record-commits) step 3 |
| `scan-secret` | `revise` or `defer` | `revise`: as for `scan-hit`. `defer`: leaves the scope `waiting`. There is no `allow` |
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
Kickoff's checklist requires the repo skill to carry that recipe and
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
than `local` is refused at kickoff and at `/sdlc` start
([`run.json`](#runjson)); Linear for driven runs is G9.

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
| Land | `<S> Land  fetched  tip moved  builder merges the tip`; `<S> Land  pass  tip merged clean  artifact <path>`; `<S> Land  pass  tip merged, conflicts resolved  artifact <path>` ([console mapping](#land-sub-machine)); `<S> Land  fetched  tip unchanged  merged  <projectMain>  pushed`; `<S> Land  verifier  resumed  <run>  verified  done` |
| Stop | `STOP   <S> <L>  <stop kind>  <run>` then `       resuming manager  <run>`; scan stops instead name each hit as `<file>:<line> <class>` and print the driver-written ask |
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
| `--session <file>` | Mint when the file is absent, resume when present ([Stage pipeline](#stage-pipeline) step 2) |
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
- **Environment:** the scrubbed environment of
  [Environment scrub](#environment-scrub); plus:

  | Variable | Value |
  | --- | --- |
  | `SDLC_RUN_DIR` | Absolute run folder |
  | `SDLC_RUN_REL` | Run folder relative to the run root |
  | `SDLC_PERSONA`, `SDLC_JOB`, `SDLC_TICKET`, `SDLC_STEP` | The invocation |
  | `SDLC_WRITABLE` | JSON array of absolute paths: the run folder, plus the item worktree for the builder |
  | `SDLC_EXITS` | JSON array of `{"name", "statuses"}`, reserved exits included as the worker may use them |
  | `SDLC_CHECKS`, `SDLC_OUTPUTS` | JSON arrays from the node |
  | `SDLC_FACTS`, `SDLC_FACTS_SHA256` | [Driver facts](#driver-facts) |
  | `GIT_AUTHOR_NAME`, `GIT_COMMITTER_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_EMAIL` | `<label>`, `<label>`, `<label>@sdlc.invalid`, `<label>@sdlc.invalid`: the [driver-set identity](#tickets-content-check) |
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
   (`{"persona", "factsSha256", "version"}`) with `fs` directly. A
   missing or wrong marker has one outcome: the post-stage `extension`
   check fails, an `operator` stop with no repair.
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
   `^(candidate\.json|result\.md|state\.md|ledger\.json|ask-human\.md|out/[A-Za-z0-9._/-]+)$`
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
| Refiner, architect, designer, ux-reviewer, security, groom-reviewer | `comment` on the Epic | The persona folder name, such as `architect` |
| Architect, `paperwork` | `comment` on the Epic plus `Record` | `architect` |
| Manager, `file-tickets` | Groom File steps 2–6: `create` each item (title `G<n>: <title>`, body copied from its `### G<n>` section), `set-blocker` each planned blocker, `transition` each item `ready`, `transition` the Epic `in_progress`, `comment` on the Epic plus `Record: <groom.md path>`. Then the freeze edit in `out/` | `manager` |
| Manager, stops | `comment` on the stopped ticket or the Epic | `manager` |

**Backend and shell recipes.** Driven runs use the `local` adapter only
in this chunk; kickoff and `/sdlc` refuse any other backend
([`run.json`](#runjson)). Pi workers have no MCP client, so every recipe
in the repo skill must run from `bash`; the `local` recipes do. This
repo's Linear skill uses MCP, so Linear for driven runs needs shell
recipes, a no-model read recipe, and its own security gate: G9
([O5](#questions-for-the-operator)).

### Behavior 8: later items (4, 7, 8)

- **Item 4, `bundle-authoring`.** Walks an author through the
  [bundle layout](#bundle-layout-and-bundlemd), persona files, and
  `flow.json`; ends by running `sdlc-driver check` until it exits `0`.
  It routes to `bundle-spec.md` and `flow-spec.md` and restates no rule.
- **Item 7, OpenCode plugin.** `packages/opencode-sdlc/` provides an
  OpenCode `HarnessAdapter` and a user command. This LLD fixes only that
  it hosts the same core and passes the same driver tests through the
  adapter contract. G7 cannot be groomed until its first deliverable
  exists: `maintainers/design/solo-dlc/opencode-server.md`, a note of
  at most one page that records, for a pinned OpenCode version, the
  command that starts the server, how a session is created and resumed,
  and how the adapter keeps a single worker process at a time. The
  worker shape, acceptance, and proving commands are groomed from that
  note.
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

- **Item 8, `sdlc-kickoff`.** Runs the readiness checklist (tracker and
  onboarding, with `local` the only backend for driven runs; the
  shell-recipe check; the `local` read recipe; project-main from trunk;
  the run root's parent; labels mode; the Pi install, `integrity`, and
  `treeSha256`; models, each slot's key source, and the spending gate),
  Gather, the Epic, then writes `run.json`,
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
| TB2 | Kickoff model → `run.json` | Paths, models, tracker, spending, harness pin | Strict schema; `local` backend only; the operator confirms a summary at the first `/sdlc` and on every change; reviewed refs derived by the driver, never read from `run.json`; a bundle commit outside them, or a `run.json` naming another ref, needs the full SHA typed back, with `scripts/` and persona hashes shown and each script's INTAKE record found at a reviewed ref | Enforced; the refs are local, not fetched (residual) |
| TB3 | Bundle → driver | Flow, personas, skills, scripts | Pinned commit read with `git show`; bundle check; every `scripts/` file listed with its hash and INTAKE record; third-party bundles through INTAKE | Enforced; a malicious intake-passed bundle is out of scope |
| TB3a | Harness → driver | The Pi package the workers run | `harness.version` and `harness.treeSha256` checked at every start, and the tree hash re-checked from a stat cache before each worker spawn; npm checked `integrity` at install | Enforced at start and at each spawn; `harness.node` is not hashed (residual) |
| TB4 | Driver → worker | Prompt, facts, env | Prompt built from driver state; model or operator text fenced as data; facts hash; extension copy hashed; fixed environment denylist | Enforced and detected; the denylist is hygiene, not a boundary |
| TB5 | Worker → files | `write`, `edit`, `sdlc_write` | Allowlist, path guard (fail-closed), run-folder tool | Enforced; the guard's check-then-write race is an accepted residual |
| TB6 | Worker → files through `bash` | Any write | Snapshot, worktree, refs, ancestry, project-main checks | Detected in the run root and worktrees; residual elsewhere (operator accepts in writing) |
| TB7 | Worker → result | `candidate.json` | Strict validation; only validated fields route; prose never routes | Enforced |
| TB8 | Worker → tracker | Every verb, full access to the `tickets` branch | Tracker-state check on state and assignee; tickets content check on every commit (driver-set author and committer), path, front-matter key and value, comment body, and filed ticket body, plus a scan of every touched file | Detected after the stage; the write is public before the check runs (operator accepts in writing) |
| TB9 | Driver → tracker | One read per check | The repo skill's `local` read recipe as fixed git argv; ids checked against the key pattern | Enforced |
| TB10 | Driver and workers → git remote | Pushes with the operator's credentials | Driver code has no force option; pushes only item branches and project-main; L9 is the only remote deletion; moved tips decided by `merge-base --is-ancestor`; the `refs` check compares every remote ref around every stage | Enforced for the driver; worker pushes detected after the stage, public before it (operator accepts in writing) |
| TB11 | Worker → model provider | Prompt, repo content, tool output | Local model by default; a paid slot requires the spending record | Enforced at start |
| TB12 | Proving commands | Shell lines | Only from the frozen, reviewed `groom.md` blob and the pinned bundle; hash per run | Enforced |
| TB13 | Run root → git | Design records | Only declared outputs, regular files, scanned; the operator may allow a non-credential hit; a credential hit is revise-only | Enforced |

**Secrets.**

| Secret | Where it lives | Who reads it | Never in |
| --- | --- | --- | --- |
| Worker tracker credential | `local`: the operator's git credentials. No other backend in this chunk; Linear is G9 | Workers | Run root files the driver writes |
| Git credentials | The operator's credential helper or SSH agent | Driver and workers | `run.json` (origin URL without user info) |
| Model credentials | Pi's own configuration | Pi | Run root files the driver writes; the scrubbed environment |

The driver holds no tracker key in this chunk. A worker can still print
a secret it can read into a log or `out/`: logs stay in the run root
(`0700`); `out/` is scanned before commit, and a credential-shaped hit
there can only be revised.

**Egress.** The git remote (which also carries the `local` tickets
branch), the model provider (local by default), and whatever a
worker's `bash` or a proving command reaches. Workers can read any file
the operator can and can reach the network through `bash`. With a paid
reviewer this is also the spending and egress gate in `run.json`.

**Data class.** The run root holds prompts, transcripts, logs, and tool
output: operator-private, never committed or published. Tracker
comments are public: only the template in
[Tracker calls](#behavior-7-tracker-calls-per-persona), enforced after
the fact by the [tickets check](#tickets-content-check). A `local`
tickets branch on a public repo is public; kickoff warns before the
first write.

**Who may write what.**

| Path | Driver | Builder | Other workers | Plugin |
| --- | --- | --- | --- | --- |
| Own current run folder (worker files) | — | yes | yes | — |
| Item worktree | merges, resets of its own worktrees | its own item | no (detected) | — |
| `worktrees/integrate`, project-main | commits, merges, pushes | no (detected) | no (detected) | — |
| `run.json` | no | no | no | no; kickoff writes it |
| `driver.json`, `index.jsonl`, `plan/`, `driver/`, other persona folders | yes | no (detected) | no (detected) | `driver.json` confirmation and `asks/` answers, while no driver runs |
| Tracker | read only | per table | per table | — |

**Residual risks.** The HLD's [Risks](hld.md#risks), as narrowed
here: tracker comment text and writes to other tickets are now detected
by the tickets check, and worker pushes by the `refs` check, both after
the stage.

**Accepted by security** (review of 34e1278):

1. S4: the driver's bare clone in the run root, hooks off for driver
   git, and the `.pi/` refusal in a worker cwd.
2. S8: one exact-pinned `typescript` dev dependency with a lockfile,
   through INTAKE, for items 5 and 6; no runtime dependency.
3. Path-guard race: a symbolic link swapped between the guard's check
   and the write.
4. Followed mode: an agent keeps the gates, including one session per
   persona; no program detects a deviation.
5. Smaller residuals: ignored files written in a worktree that
   `git status --porcelain` does not show; a worker that escapes the
   leftover sweep; and a worker that tampers with
   `driver/snapshot.json` while the driver is down, which only weakens
   the interrupted-stage check.
6. N4 (re-review of de7c438, low), stated as residuals:
   - The reviewed-ref ancestry test and the INTAKE record lookup use
     the skills home's local remote-tracking refs; the driver does not
     fetch the skills home, so a stale or locally moved ref is trusted
     as the operator left it.
   - `harness.treeSha256` is checked at every start and re-checked
     before each worker spawn from a stat cache. The re-check walks the
     tree, so it hashes added files and notices removed ones. A change
     that keeps a file's inode, size, `mtime`, and `ctime` is not
     re-hashed between starts; the full hash at the next start catches
     it.
   - `harness.node`, the Node binary for the detached driver under
     Pi's compiled binary, is not hashed.

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

### Mockups

`none`. No-screen reason: this chunk has no graphical screen. The
console, chat dialogs, and run-root files are the interface; [Console lines](#console-lines) fixes their
text. UX acceptance of [ux.md](ux.md) by the operator is pending.

### Verify

**Per item.**

| Item | Unit | Fixture and integration | Proving commands (Groom writes the final lines) |
| --- | --- | --- | --- |
| 1 | — | `docs/sdlc/fixtures/results/` holds one fixture per error code and three valid examples | `K1` and `K7` from the [writing standard](../../writing-standard.md#checks); `test "$(wc -l < docs/sdlc/stage-result.md)" -le 150`; `ls docs/sdlc/fixtures/results/*.expect.json` |
| 2 | — | `docs/sdlc/fixtures/flows/` holds one fixture per bundle-check code, including each `gate.*` row's counterexample (`gate.trial` among them), exit `checks`, `extract`, and a script without an intake bullet, and `fixtures/bundles/minimal/` | `K1`, `K7`; `wc -l docs/sdlc/bundle-spec.md docs/sdlc/flow-spec.md` ≤ 150 each |
| 3 | — | `bundles/sdlc/` follows the spec; rule maps; the S5 claim-condition diff | `K1`–`K7`; `node packages/sdlc-driver/src/cli.ts check bundles/sdlc`, which needs G5's bundle check on project-main, hence the land order in [Groom split](#groom-split-proposal) |
| 5 | `node:test` per module: strict reader, result and candidate rules, front matter, bundle check, labels, groom parser, facts, scan, console | Every fixture under `docs/sdlc/fixtures/`; driver tests with the fake worker against a temporary bare origin with a `local` tickets branch | `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check` (`tsc -p . && node --test`) |
| 6 | Argv and env builder; worker extension with a fake extension API: path guard (links, `..`, `.git`, `~`), `sdlc_write`, `sdlc_result` on the shared fixtures, compaction summary | Plugin and adapter against a fake `pi` that records argv and env | `npm --prefix packages/pi-sdlc ci && npm --prefix packages/pi-sdlc run check`; then the Pi checks below |
| 4 | — | Following the skill produces a bundle under `docs/sdlc/fixtures/bundles/authored/` that passes the check | `K1`, `K7`; `node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/authored` |
| 7 | Adapter unit tests | The item 5 driver suite through the OpenCode adapter with a fake server | First deliverable: `maintainers/design/solo-dlc/opencode-server.md`, at most one page (command, session, single worker process), checked by `K1`-style `wc -l` ≤ 60 and the reviewer. G7 is groomed, and its proving commands written, only after that note lands |
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
9. Lost session → `lost-session` ask → `replace` mints with `handoff`.
10. Proving commands edited in the item worktree have no effect; a
    `groom.md` changed after review stops ticket filing.
11. First start creates `repo.git` and `worktrees/integrate` before any
    fetch; a `run.json` with `backend: linear` is refused at start; a
    changed Pi tree hash stops the start.
12. A design record with a credential-shaped line → `scan-secret`, no
    `allow`; the console and ask name file, line, and class, never the
    text. A path hit → `scan-hit`, `allow` commits.
13. A proving command and a worker see none of the denylisted
    variables.
14. A bundle commit outside trunk and project-main shows the full
    SHA, both ancestor results, and the `scripts/` and persona hashes;
    the answer must equal that SHA. A script that has not cleared
    INTAKE stops the start first, including a script whose record
    exists only in the bundle commit's own `docs/INTAKE.md`. A
    `run.json` whose `bundle.reviewedRefs` lists another ref takes the
    typed-SHA path even for a commit on trunk.
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
17. A worker whose Pi tree changed after start fails the pre-spawn
    `harness` re-check without spawning: once for an edited file, once
    for an added file, and once for a removed file.
18. Crash after a design-record push: a test hook kills the driver
    after the Spec record push returns `0` and before pipeline step 11.
    `meta.json` holds `recordCommit` equal to the pushed commit. The
    restart passes `refs` and `worktrees` under the pushed record
    exception, writes `recordCommit` into `interrupted.json`, sets
    `chunk.unposted`, re-runs the Spec node, stages nothing, sets
    `chunk.pendingRoute` with that commit, runs paperwork, and routes by
    the re-run's `choice` after `posted`. A re-run that returns `stop`
    leaves `chunk.unposted` set, and the node's next `pass` runs
    paperwork. Each of these stops at restart with `check failed`:
    project-main at a commit other than `recordCommit`; project-main at
    `recordCommit` while another ref also moved; `worktrees/integrate`
    at another commit or dirty; and a kill after the commit and before
    the push.

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
10. Pi workers have no MCP client, so repo tracker recipes must run from
    `bash`.
11. Driven runs support only the `local` backend in this chunk (security
    ruling S1). This is the HLD's own rule applied: the kickoff stops
    without a no-model `read` recipe, and only `local` has one. The
    draft clarification that tracker reads use built-in readers is
    withdrawn. The HLD's read-command sentence stands, and this LLD
    does not replace it.
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
16. Item 7 (G7) is not groomed with the others. The HLD keeps it in the
    last wave after item 6; here it is deferred until its first
    deliverable, `opencode-server.md`, has landed, and its proving
    commands are written from that note.
17. G9, Linear for driven runs, is new: the HLD has no such item. It
    comes from security ruling S1 and carries S1 and S2, with its own
    LLD addendum and **security** gate.

### Groom split (proposal)

| G | Item | Blocked by | Reason |
| --- | --- | --- | --- |
| G1 | Result format (DER-529) | — | — |
| G2 | Bundle and flow spec, fixtures | G1 | Candidate and `choice` rules extend item 1's fields |
| G5 | Core driver | G1, G2 | Implements both specs; its tests read their fixtures |
| G3 | SDLC bundle, `test-failure-handler`, tracker wiring, `bundle-runs.md` | G2, G5 | Written in the spec's format. Land order: G5 lands before G3, because G3's proving commands run G5's bundle check on `bundles/sdlc`. Differs from the HLD: [clarification](#clarifications-of-the-hld-made-here) 15 |
| G6 | Pi plugin, worker extension, Pi checks | G3, G5 | Hosts the core; the smoke runs `bundles/sdlc` |
| G4 | `bundle-authoring` | G6 | Brief: after the Pi path works |
| G8 | `sdlc-followed-mode`, `sdlc-kickoff` | G6 | Brief: after the Pi path works |
| G7 | OpenCode plugin. Not groomed in this pass: its first deliverable, the one-page server note `opencode-server.md` (command, session, single worker process), must exist before G7 is groomed | G6 | Brief: after the Pi path works; the server's behavior is unconfirmed. Deferral: [clarification](#clarifications-of-the-hld-made-here) 16 |
| G9 | Linear for driven runs: a no-model read recipe for the driver and shell write recipes for workers. Not groomed in this pass: it needs its own LLD addendum and its own **security** gate | G6 | Security ruling S1; carries S1 and S2 (below). Not an HLD item: [clarification](#clarifications-of-the-hld-made-here) 17 |

Waves: 1: G1; 2: G2; 3: G5; 4: G3; 5: G6; 6: G4, G8. G7 and G9 are
groomed later, each after its precondition. No gate items. Item 5 is
the largest for a 100k-token builder. Groom may split it into G5a
(strict reader, result and candidate rules, front matter, bundle check;
← G1, G2), G5b (run root, state machine, stage pipeline, stops, fake
worker; ← G5a), and G5c (git, land, proving commands, snapshot, refs
and tickets checks, tracker read, scan; ← G5b). With the split, G3 ←
G2, G5a (land order G5a before G3), so G3 can build beside G5b and G5c,
and G6 ← G3, G5c.

**G9 carries** from the security review of 34e1278: S1, the Linear read
key, with the constraints **security** set (the key file's content must
match the `lin_api_` format; the key path and its parents are no
symbolic link; the `run.json` confirmation shows the path; a same-uid
process reading the key is residual); and S2, worker tracker
credentials for Linear on Pi.

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
| Pi pin | Harness supply chain | npm `integrity` recorded at install; `treeSha256` (binary hash, or package-tree hash) recorded in `run.json` and checked at every start; 0.73.1 or 1.x is O6 | [`run.json`](#runjson), [Start](#start) |

### Questions for the operator

| # | Question | Recommendation |
| --- | --- | --- |
| O1 | Run a Trial before Build? | No separate Trial. This LLD keeps every Pi fact behind the adapter and the worker extension, so a fallback changes item 6, not item 5's shape; item 6 runs T1–T6 as P1–P6 first |
| O2 | UX Q1–Q3 | Accept the recommended defaults this LLD assumes: replies at the next `/sdlc` (Q1); the handoff block in [Behavior 8](#behavior-8-later-items-4-7-8) (Q2); `index.jsonl` (Q3) |
| O3 | Ticket filing end state: Groom says `ready` and Epic `in_progress`; the HLD table says `backlog` | Follow Groom; the HLD row gets a clarification |
| O4 | Same-item claim rule: contract v2 or v3 | Settled by security ruling S5: v2, with kickoff checking the repo skill for the same-item sentence. No answer needed |
| O5 | Linear for driven runs | Driven runs use `local` only in this chunk. Linear, driver reads and worker writes, becomes G9, blocked by G6, with its own LLD addendum and security gate; it carries S1 and S2. Accept |
| O6 | Pi version: `@mariozechner/pi-coding-agent` 0.73.1 (every Pi fact here was read in it; the registry marks it deprecated) or `@earendil-works/pi-coding-agent` 1.x (the maintained line; facts not yet checked) | Pin 0.73.1 for G6. Record npm `integrity` at install and `treeSha256` in `run.json`; check `treeSha256` at every start. The Pi facts table and the T1–T6 fallbacks were read at 0.73.1. Moving to 1.x is a later item that re-reads the facts table at 1.x and reruns P1–P7. If the operator picks 1.x now, G6's first task is that re-read; nothing else in this LLD names the package |
| O7 | Skill ids `test-failure-handler`, `bundle-authoring`, `sdlc-followed-mode`, `sdlc-kickoff` | Accept |
| O8 | Item 5 split into G5a–G5c | Let Groom split it; with the split, G3 waits only for G5a |
| O9 | The three residuals under "Operator must accept in writing" in [Trust boundaries](#trust-boundaries) | Accept in writing at the `spec` gate. Removing them needs a sandbox for `bash` and network, which the HLD lists as a non-goal; Pi's example bubblewrap extension is a later option after intake |

### Rollout / rollback

The chunk adds new files and routes; existing runs that use sub-agents
are unaffected except by the same-item claim rule, which applies only
inside bundle runs. Rollback is reverting the items' land commits on
project-main before Trunk; run roots are outside git and need no
cleanup.
