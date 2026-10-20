# Flow spec

Tickets: chunk `DER-421`.

This file owns `flow.json`, exits, reserved exits, driver-fixed exits and route, candidate rules, bundle check, chunk land, re-entry, the `json sdlc-env` block, and the error codes below. Bundle layout, personas, prompt kinds, and placeholders are owned by [bundle-spec.md](bundle-spec.md). `schemaVersion`, `step`, `status`, the `choice` pattern, `ticket`, `artifact`, `evidence`, and `findings` are owned by [stage-result.md](stage-result.md). Do not restate them.

A step is one of Entry, Brief, Repo, Plan, Trial, Spec, Groom, Build, Review, Trunk, Changelog, Monthly ([Names](../SDLC.md#names)). The four statuses are `pass`, `fail`, `blocked`, and `needs_input`.

## flow.json

One JSON object. The strict reader rejects trailing text, a duplicate key, a null, and an unknown key. Any of those is `flow.json` and stops the check. A field that breaks this table is `flow.field`.

| Field | Rule |
| --- | --- |
| `schemaVersion` | Integer `1` |
| `id` | The bundle id |
| `entry` | Id of a `chunk` node |
| `itemEntry` | Id of an `item` model node whose persona job is `builder`. Omit it when no node has scope `item`. Require it when one does |
| `defaults.prove` | Array of command lines. `[]` is allowed. Each line is a string, at most 1000 characters, with no newline |
| `defaults.commandTimeoutSec` | Integer. Omit means `1800` |
| `defaults.workerTimeoutSec` | Integer. Omit means `7200` |
| `nodes` | Array of node objects, in flow order |

`defaults` is required. A path is normalized when it uses `/`, has no leading `/`, no `\\`, and no empty, `.`, or `..` segment. `{design}` may be the first segment. `outputs` entries do not end with `/`. `outputDirs` entries do.

| Field | Kinds | Rule |
| --- | --- | --- |
| `id` | all | `^[a-z][a-z0-9-]{0,31}$`, unique |
| `label` | all | `^[A-Z][A-Za-z]{0,11}$` |
| `step` | all | A step name |
| `kind` | all | `model`, `command`, `gate`, or `land` |
| `scope` | all | `chunk` or `item` |
| `persona` | `model` | A persona id of the same scope |
| `envSpec` | `model`, `chunk` | Optional. Omit unless `true`. At most one `true`, on step Spec, with an `outputs` path ending `/lld.md`. A break is `flow.env`, not `flow.field` |
| `skills` | `model` | Optional skill ids |
| `outputs` | `model`, `chunk` | Optional normalized paths |
| `outputDirs` | `model`, `chunk` | Optional normalized prefixes ending `/` |
| `checks` | `model` | Optional names matching `^[a-z][a-z0-9-]{0,31}$` |
| `commands` | `command` | `"groom"`, `"env"`, `"env-test"`, or an array of `scripts/<file>` paths. `"env"` and `"env-test"` are chunk-only |
| `gate` | `gate` | `brief`, `ux`, `plan`, `trial`, `mockup`, `spec`, or another `^[a-z][a-z0-9-]{0,15}$` word |
| `ask` | `gate` | Non-empty ask text. The gate prompt passes it as `{{ask}}` |
| `builder`, `prove`, `verify`, `review` | `land` | Node ids of the land's scope. A second `land` in that scope is `flow.land-ref` |
| `exits` | all | Array of exit objects. Empty is `flow.dead-end`, not `flow.exit-shape` |

A `scripts/<file>` command whose file is missing is `bundle.layout`. A file name that is not `scripts/<file>` is `flow.field`.

## Exits

`name` matches `^[a-z][a-z0-9-]{0,31}$` and is unique on the node. `statuses` is a non-empty subset of the four statuses. `to` is a node id, `@items`, or `@done`.

Optional `say` is one line. Its placeholders are the closed set in bundle-spec. Any other `{{…}}` is `flow.field`.

Optional `checks` adds names required when a candidate takes this exit. For these names, `n/a` is not a finding.

Optional `extract` is allowed on a `gate` exit only: `{"from", "heading", "to"}`. `from` is a normalized path and may use `{design}`. `heading` is non-empty. `to` matches `^[a-z0-9-]{1,40}\.md$`. Any extract violation is `flow.extract`. On take, copy the `##` section of `from` at the project-main tip into the gate run folder as `to`, and set `{{extracted}}` to that absolute path. A missing file or heading is `check failed: extract`, an `operator` stop.

`@items` ends the chunk phase and starts each planned item at `itemEntry`. Only a chunk node may use it. `@done` ends the scope: the item is landed and verified, or the chunk run is complete once every item is done. An item `to` is an item node id or `@done`. A `to` that does not resolve, an item that targets a chunk node, or `@items` from an item node is `flow.target`.

A `command` node has exactly two exits: one `statuses` is `["pass"]`, the other `["fail"]`. Each `gate` exit has exactly one status, `pass` or `fail`. A `land` exit is the only exit, named `done`, with `["pass"]`: an item land targets `@done`, and a chunk land targets a chunk node. Any other shape is `flow.exit-shape`.

## Reserved exits

Every node has `stop` and `operator`. A flow that lists either name is `flow.reserved-listed`.

| Exit | Worker status | Driver-authored status | Route |
| --- | --- | --- | --- |
| `stop` | `blocked`, `needs_input` | `fail` | Resume the manager. It may `resume`, `defer`, or `escalate` |
| `operator` | `needs_input` | `fail` | Resume the manager. It may only `escalate` |

A worker candidate with `fail` and a reserved exit is `flow.reserved-status`. A driver-authored `fail` with `operator` records failed checks on a model stage.

## Driver-fixed exits

These stages take exits from this table, not from the flow file. A candidate `choice` must be in the row for its status. Reserved exits apply unless the row says otherwise.

| Stage | Prompt kinds | Exits |
| --- | --- | --- |
| Land builder, merging the tip | `merge-tip` | `ready` with `pass` |
| Land builder, fixing after a land check | `test-failure`, `fix` | `ready` with `pass` or `fail` |
| Land verifier, re-run or post-land | `land-recheck`, `post-land` | `ok` with `pass`, `fix` with `fail` |
| Land proving commands | none | `ok` with `pass`, `fix` with `fail` |
| Architect paperwork | `paperwork` | `posted` with `pass`. Reserved exit: `stop` only |
| Manager | `stop`, `gate`, `apply-answer` | `resume` with `pass`, `defer` with `pass`, `escalate` with `needs_input`. An `operator` stop or a gate offers `escalate` only. Do not offer reserved exits |
| Invalid-result repair | `repair` | The exits of the stage it repairs |
| Answer | `answer` | The exits of the stopped node or stage |
| Rehydrated session | `rehydrate`, wrapping the kind the stage would have sent | The exits of that stage |

While `chunk.reentry` is set, the chunk `land` node's `done` goes to `@items`, not to its flow `to`. Bundle check adds no edge for that override.

## json sdlc-env

The LLD `## Build environment` section holds exactly one fenced block with info string `json sdlc-env`, read by the strict reader. `schemaVersion` is integer `1`. The LLD field table omits `schemaVersion`; this file requires it because an unknown key is an error and the block example includes it.

| Field | Rule |
| --- | --- |
| `toolchain` | Array of command lines. May be empty |
| `deps` | Array. May be empty. `name` matches `^[a-z][a-z0-9-]{0,31}$` and is unique. `setup`, `start`, `ready`, `reset`, and `stop` are arrays of command lines and may be empty. `ready` is non-empty when `start` is |
| `passEnv` | Array of `^[A-Z][A-Z0-9_]{0,63}$`. May be empty. Command stages keep these names |
| `prove` | Non-empty array of command lines |
| `test` | One command line |

Every command line is at most 1000 characters and has no newline. Reject a line the design-record scan classes as `credential`, `ip`, `path`, `host`, or `userinfo`: a private-key block; `lin_api_`, `ghp_`, `github_pat_`, `AKIA`, `xox[abprs]-`, or `sk-` plus the body length in that scan; a URL with a password or a user name; an IPv4 address other than `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`, and `127.0.0.1`; `/home/`, `/Users/`, `/root/`, `/var/lib/`, or `C:\Users\`; a host suffix `.lan`, `.local`, `.internal`, `.ts.net`, or `.home.arpa`. Any invalid block is `flow.env-block`.

## Chunk land and re-entry

A chunk `land` is allowed only when the one `envSpec` node exists. Its `prove` is a chunk `command` with `commands` `"env"`. Its `verify` is a model whose job is `verifier`. Its `review` is step Review, job `reviewer`, and `checks` holds `intake`, `sha-pins`, and `trust-boundary`. Its `done` targets a chunk node. A broken land reference is `flow.land-ref`. A review missing one of those three names is `flow.review-checks`. `"env"` or `"env-test"` without the `envSpec` node is `flow.env`.

A builder, verifier, or reviewer that needs a missing capability stops with `needs_input`, `choice` `operator`, and an `env-capability: <one line>` check. The ask choices are:

| Choice | When | Driver then |
| --- | --- | --- |
| `env` | The capability is inside the accepted block | Set `chunk.reentry`, set the chunk node to `env-prep`, and add 1 to `env.pass` |
| `spec` | The LLD must change | Set `chunk.reentry` and the chunk node to `spec`. The run passes `security`, the `spec` gate, and env-prep again |
| `deny` | Use the accepted environment | Resume the stopped persona with the answer |
| `defer` | Not now | Leave the item `waiting` |

The chunk then runs before every item. The chunk land's `done` goes to `@items`. Clear `reentry` and resume the stopped persona with the `answer` prompt naming `env.landCommit`. Re-entry is not a flow edge. It enters only the chunk builder or the Spec node, after every item already passed `gate.spec` and `gate.env`, and follows flow edges through the `env` gate and the chunk land before any item runs again.

## Candidate rules

A worker writes `candidate.json`. With a flow, a present `schemaVersion`, `step`, `ticket`, or `evidence.kind` that differs from the invocation is `flow.fixed-field`. The driver rejects it and does not overwrite the field. Pattern failures stay the stage-result codes. Behavior 1 also names `result.ticket-mismatch` for a differing ticket; with a flow, report `flow.fixed-field` and not both.

1. Omitted `schemaVersion`, `step`, `ticket`, and `evidence.kind` are filled from the invocation.
2. `choice` is an exit of the node whose `statuses` contain `status`, a reserved exit allowed for that status, or a driver-fixed exit for the stage. Otherwise `flow.choice-not-allowed`.
3. On `pass`, every node `checks` name and every chosen-exit `checks` name is the prefix `<name>: ` of one `evidence.checks` entry, followed by a finding. For a node check, `n/a — <why>` is a finding. A miss is `flow.check-missing`.
4. On `pass`, each node `outputs` path exists as a regular file at `out/<path>` in the run folder. No symbolic link anywhere under `out/`. Codes: `flow.output-missing`, `flow.output-symlink`.
5. `artifact` follows stage-result.md and lies in this stage's run folder. No extra code.
6. `state.md` exists and has at most 60 lines and 6000 characters, or `flow.state-size`.
7. A builder `pass` or `fail` leaves no uncommitted change in its worktree, or `flow.uncommitted`.
8. The verifier's `ledger.json` exists and is a JSON array of objects with `id` `V<n>`, `criticality` one of `breaking`, `critical`, `major`, `minor`, `nit`, `status` `open` or `fixed`, `summary` at most 200 characters, `raised`, and `fixed`. Ids stay across runs. A pass has no `open` entry above `nit`. Otherwise `flow.ledger`.
9. `pass` on the `envSpec` node: `out/<lld path>` has one `## Build environment` section and exactly one valid block, or `flow.env-block`.
10. An `env-capability: <one line>` entry in `evidence.checks` is allowed only with `needs_input` and `choice` `operator`. Otherwise `flow.env-capability`.

A failing rule makes the candidate invalid.

| Result | `evidence.kind` | Evidence |
| --- | --- | --- |
| Model stage, including land model stages, paperwork, and the manager | `model` | `pass` needs `checks`. Paperwork uses `comment: <id>`. Manager `resume` or `defer` uses `source: …` |
| Command stage, including land proving and an L7x push | `command` | `command`, `exit_code`, and findings per stage-result rule 1 |
| Gate result from the operator's answer | `model` | `pass` checks are `operator-answer: asks/ask-N`. Findings are the answer. An empty answer records nothing, so `fail` has findings |
| Failed check or invalid result on a model stage | `model` | `fail`. Findings name the check or the error codes |
| Failed check on a command stage | `command` | Keep the wrapper result. Write the failed check in `check.json` |

A gate uses `model` because the result contract has two kinds and the decision is not an exit code.

## Bundle check

`sdlc-driver check BUNDLE_DIR [--at COMMIT]` reads the bundle at `COMMIT`, or the working tree when `--at` is omitted. Print one error per line: `<file>: node <id> exit <name>: <code>: <message>`, or `<file>: <field>: <code>: <message>` when no node applies. Exit `0` when clean, and `1` on any error.

| # | Rule | Code |
| --- | --- | --- |
| B1 | Strict reader and the field tables | `flow.json`, `flow.field` |
| B2 | Ids unique; every `to` resolves; `@items` only from chunk nodes; item nodes never target chunk nodes | `flow.target` |
| B3 | Every node reachable from `entry`; item nodes only through `@items`; every node has an exit | `flow.unreachable`, `flow.dead-end` |
| B4 | Command, gate, and land exit shapes | `flow.exit-shape` |
| B5 | `stop` and `operator` are not listed | `flow.reserved-listed` |
| B6 | Each model persona exists, scope matches, and prompt kinds exist | `flow.persona`, `persona.prompt-missing` |
| B7 | Front matter, read-only, tools, placeholders, persona sections | `persona.frontmatter`, `persona.readonly`, `persona.tools`, `persona.placeholder`, `persona.section` |
| B8 | Every skill id resolves, and `## Required skills` matches | `bundle.skill` |
| B9 | `outputs` and `outputDirs` are normalized | `flow.output-path` |
| B10 | Land names, kinds, and review checks | `flow.land-ref`, `flow.review-checks` |
| B11 | The gate rows hold on every path | `gate.comparables`, `gate.plan`, `gate.trial`, `gate.spec`, `gate.env`, `gate.land` |
| B12 | Headings, symlinks, size, script bullets, reviewed-ref record | `bundle.layout`, `bundle.script-intake` |
| B13 | `extract` shape | `flow.extract` |
| B14 | `envSpec`, `"env"`, `"env-test"`, and a chunk land | `flow.env` |

The LLD writes B7 as `persona.*` and names `persona.frontmatter` and `persona.placeholder` only. This file assigns `persona.readonly`, `persona.tools`, and `persona.section` to the other B7 rules.

A gate row whose target node does not exist holds. A target that exists without its required node is an error. Search breadth-first over pairs `(node, k)`, where `k` counts required nodes passed in order. Entering the k-th required node increments `k`. The source counts as entered when the search starts. Reaching the target with `k` too small is a violation. Name the exit on the last edge of the shortest counterexample. Stops and the manager add no edges. Land re-runs reach Review only through that land's `prove`, `verify`, and `review` edges.

| Code | From | Reaching | Must pass, in order |
| --- | --- | --- | --- |
| `gate.comparables` | `entry` | Chunk `model`, step Plan, an `outputs` path ending `/hld.md` | Chunk `model`, step Plan, an `outputs` path ending `/comparables.md` |
| `gate.plan` | `entry` | `model`, step Spec, an `outputs` path ending `/lld.md` | `gate` tagged `plan` |
| `gate.trial` | `entry` | That Spec node | `gate` tagged `trial` |
| `gate.spec` | `entry` | A step Groom node, an item node, a chunk node whose persona job is `builder`, or a chunk `"env"` or `"env-test"` command | The Spec node, then step Spec job `security`, then `gate` tagged `spec` |
| `gate.env` | `entry` | A step Groom node, or an item node | `gate` tagged `env`, then the chunk `land` |
| `gate.land` | Each `model` whose job is `builder` | The `land` of that scope | That land's `prove`, `verify`, and `review` |

## Fixtures

`docs/sdlc/fixtures/flows/<name>/expect.json` is `{"valid": <bool>, "codes": [<codes>], "phase": "<phase>"}`. `phase` `bundle` checks `bundle/` and expects that set of codes, ignoring order and repeats. `phase` `candidate` requires `bundle/` to pass, and `candidate.json` to miss an exit `checks` finding (`flow.check-missing`). This fixture does not assert the other candidate rules. `phase` `env-block` checks the one block in `block.md`.

The directory name is the code, except `chunk-land` (`flow.land-ref`, a chunk land whose prove is not `"env"`), `exit-checks` (`flow.check-missing`), `sdlc-env-valid` (no codes), and `sdlc-env-invalid` (`flow.env-block`).

`docs/sdlc/fixtures/bundles/minimal/` is a bundle that passes. Its nodes are `refine` and `ask`. `minimal.expect.json` beside that directory is the passing expect file.
