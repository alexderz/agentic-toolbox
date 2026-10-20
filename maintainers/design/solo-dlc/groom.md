# Groom — solo-dlc

DRAFT (pre-review)

<!-- At freeze, replace the draft marker above with this sentence and
delete this comment: Frozen record of the plan as reviewed at Groom on
<YYYY-MM-DD>. Not live: the tracker is the source of truth for tickets,
blockers and state. -->

- Chunk: `DER-421` · LLD: `maintainers/design/solo-dlc/lld.md` · Date: `2026-10-20`
- Review: `pending`
- Tickets: pending at freeze. `G1` is the existing `DER-529` (update it; do not file a second ticket). Every other `G` id is unassigned.
- Out of scope for this plan: general-SDLC follow-ups `DER-565` (build-environment gate for the SDLC itself) and `DER-570` (general-SDLC toolbox-copy layout). `G9` (Linear for driven runs, security rulings S1 and S2) is not groomed; it needs its own LLD addendum and its own security gate.
- Test environment: this chunk is a TypeScript driver, two harness packages, and docs. Tests run on Node.js `>=22.18` (`packages/sdlc-driver` `engines`), npm, and the pinned `typescript` devDependency (ruling S8), via `node:test` (`tsc -p . && node --test`) and the writing-standard K checks. No database, container, or other service. No env-prep item: this chunk does not need a build-environment gate to build or test. The product still implements env-prep for bundles that carry a `json sdlc-env` block (`G5e`, `G3`).

Each item below is the ticket body. The `json sdlc-item` block is the driver's copy of `blockedBy`, `skills`, and `prove`; it must agree with the prose. `prove` lines are the final proving commands from the LLD Verify table.

## Items

### G0: Run prep, Gather, restore (`sdlc-kickoff`) and `run-state.md`

```json sdlc-item
{"slug": "run-prep", "blockedBy": [], "skills": ["shell-safety"],
 "prove": ["test \"$(wc -l < skills/sdlc-kickoff/SKILL.md)\" -le 250",
           "test \"$(wc -l < docs/sdlc/run-state.md)\" -le 250"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#item-0-sdlc-kickoff-run-prep-gather-restore`
- Branch: `item/<ticket-id>-run-prep`

## Required

- **Outcome** — `skills/sdlc-kickoff/SKILL.md` is the Run prep, Gather, and restore procedure, and `docs/sdlc/run-state.md` is the owner of the run-root formats item 5 builds against. Neither starts the driver.
- **Acceptance** —
  - The skill has three modes: `prep`, `gather`, and `restore`. None starts the driver or a worker.
  - For a followed run, Run prep offers only the `plain` durability level; `pushed` and `local` are not offered.
  - Run prep asks the SD-1 setup questions, toolbox remote first with no default, and refuses a remote that fails the remote rule before any clone or fetch. The tracker answer is `local` only, with the ux.md J2 warning.
  - The readiness checklist is a preview until the operator replies. R1–R4 are the skill's own git, `gh`, and tracker steps and are walkable on a fixture repo with a bare origin. R5–R10 and the `sdlc-driver` subcommands (`readiness`, `toolbox`, `state-init`, `drill`, `persist`, `status`, `restore`) are named as not available until item 5 (O14).
  - After the reply, the procedure files the Epic, writes `run.json`, `machine.json`, `checklist.md`, and empty `refiner/run-1/` and `gatherer/run-1/`, and prints the only genesis note (typed remote and trunk) in the `state-init` turn.
  - Gather runs in a new session, confirms a brief in words, writes `gatherer/run-1/brief.md`, lists the copied session in `machine.json`, and prints the OpenCode or Pi start line (O10).
  - Restore asks only machine-local questions, runs R5, R6, and R8, and names `sdlc-driver restore` without implementing it.
  - `docs/sdlc/run-state.md` states the run-root layout and its D marks, `run.json`, `machine.json`, `asks/`, the run folder, labels, durability levels, the state branch and `sdlc-state.json`, persist, lease, restore, drill, the toolbox copy, compiled files, rehydrate, and session backup. Rules only, one or two lines each. Examples stay in the LLD.
  - A `SOURCES.md` row exists for `sdlc-kickoff`.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1 and K7 on the two new files. Walk R1–R4 on a fixture repo with a bare origin. `test "$(wc -l < skills/sdlc-kickoff/SKILL.md)" -le 250` and `test "$(wc -l < docs/sdlc/run-state.md)" -le 250`. R5–R10 are not this item's prove; item 5's Run prep test covers them.
- **Blocked by** — `none`
- **Blocks** — `G5b` — the run-root implementation is written against `run-state.md`; `G3` — `bundle-runs.md` routes to `run-state.md`
- **Out of scope** — The driver subcommands and R5–R10 execution (`G5d`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- Operator answers already accepted that this procedure must not reopen: O7 (skill id), O12 (no default durability on a public repo), O13 (250-line cap), O14, O20 (genesis note), O21(a), O22 (typed toolbox remote).

### G1: Stage result v1

```json sdlc-item
{"slug": "result-format", "blockedBy": [], "skills": [],
 "prove": ["test \"$(wc -l < docs/sdlc/stage-result.md)\" -le 150",
           "ls docs/sdlc/fixtures/results/*.expect.json"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-1-stage-result-v1-item-1`
- Branch: `item/<ticket-id>-result-format`
- Existing ticket: `DER-529`. The manager updates that ticket with this body and does not create another.

## Required

- **Outcome** — `docs/sdlc/stage-result.md` is the v1 result contract, within 150 lines, with a fixture for every result error code and three valid examples.
- **Acceptance** —
  - Top-level fields are exactly `schemaVersion` (integer `1`), `step`, `status`, `choice` (pattern `^[a-z][a-z0-9-]{0,31}$`), `ticket`, `artifact` (one run-root-relative path; no `.`, `..`, leading `/`, or `\`), `evidence`, and `findings`. Unknown keys and nulls fail.
  - The harness-fill rule, the command-wrapper `choice`/`artifact` rule, and the out-of-scope pointer to `flow-spec.md` match Behavior 1. No flow-aware rule is added here.
  - The line-budget edits land the file at 148 lines before item 3's one-line route (149). The file stays ≤150.
  - `docs/sdlc/fixtures/results/` has one fixture per error code, each with `NAME.expect.json` of the form `{"valid": false, "codes": ["…"]}`, for every code listed in Behavior 1, plus three valid examples.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1 and K7. `test "$(wc -l < docs/sdlc/stage-result.md)" -le 150`. `ls docs/sdlc/fixtures/results/*.expect.json` lists one expect file per invalid fixture.
- **Blocked by** — `none`
- **Blocks** — `G2` — candidate and `choice` rules extend these fields; `G5a` — the result reader is written against this contract and its fixtures
- **Out of scope** — Flow-aware codes (`G2`). The driver that enforces the contract (`G5a`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G2: Bundle and flow spec, with fixtures

```json sdlc-item
{"slug": "bundle-flow-spec", "blockedBy": ["G1"], "skills": [],
 "prove": ["test \"$(wc -l < docs/sdlc/bundle-spec.md)\" -le 150",
           "test \"$(wc -l < docs/sdlc/flow-spec.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-2-bundle-and-flow-spec-item-2`
- Branch: `item/<ticket-id>-bundle-flow-spec`

## Required

- **Outcome** — `docs/sdlc/bundle-spec.md` and `docs/sdlc/flow-spec.md` own the bundle layout, personas, `flow.json`, exits, bundle check, chunk land, re-entry, the `json sdlc-env` block, and the error codes, and the fixtures cover every bundle-check code.
- **Acceptance** —
  - `bundle-spec.md` (≤150) owns bundle layout, `bundle.md`, persona files, prompt kinds, and placeholders.
  - `flow-spec.md` (≤200, O13) owns `flow.json`, exits, reserved exits, driver-fixed exits and route, candidate rules, bundle check B1–B14, the `gate.*` rows including `gate.trial` and `gate.env`, chunk land and re-entry, the `json sdlc-env` block, and the error codes.
  - `docs/sdlc/fixtures/flows/` holds one fixture per bundle-check code, including each `gate.*` counterexample (`gate.trial` and `gate.env` among them), exit `checks`, `extract`, a chunk land, `envSpec`, a valid and an invalid `json sdlc-env` block, and a script without an intake bullet. `docs/sdlc/fixtures/bundles/minimal/` passes the check. Its flow has exactly two nodes: `refine` (model, persona `refiner`, exit `next` on `pass` to `ask`) and `ask` (gate `brief`, exit `accept` on `pass` to `@done`, exit `revise` on `fail` to `refine`). A passing followed walk of that flow writes three results: `docs/sdlc/fixtures/followed/minimal/refiner/run-1/result.json` for node `refine`, `docs/sdlc/fixtures/followed/minimal/manager/run-1/result.json` for the manager stage with `choice` `escalate`, and `docs/sdlc/fixtures/followed/minimal/operator/run-1/result.json` for node `ask`. The manager path is not a third flow node.
  - `docs/INTAKE.md` gains a `## Script records` section: one line per bundle script security has cleared.
  - Candidate and `choice` rules extend G1's fields; they do not redefine them.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1 and K7. `test "$(wc -l < docs/sdlc/bundle-spec.md)" -le 150` and `test "$(wc -l < docs/sdlc/flow-spec.md)" -le 200`. Fixture files exist for every code named above. The checker that exits with those codes is G5a's prove, not this item's.
- **Blocked by** — `G1` — candidate and `choice` rules extend item 1's result fields
- **Blocks** — `G5a` — the checker implements this spec and reads these fixtures; `G3` — the SDLC bundle is written in this format; `G4` — `bundle-authoring` routes to these two specs; `G8` — followed mode walks `fixtures/bundles/minimal/`
- **Out of scope** — Implementing `sdlc-driver check` (`G5a`). The SDLC bundle itself (`G3`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G5a: Driver core — reader, results, bundle check

```json sdlc-item
{"slug": "driver-check", "blockedBy": ["G1", "G2"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check",
           "test \"$(wc -l < packages/sdlc-driver/README.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-5-core-driver-item-5`
- Branch: `item/<ticket-id>-driver-check`

## Required

- **Outcome** — `packages/sdlc-driver` exists and can check a bundle and validate a stage result, with no harness import and no runtime dependency.
- **Acceptance** —
  - Package layout matches the LLD: private ESM, `engines` Node `>=22.18`, strict `tsconfig` with `erasableSyntaxOnly` and `noEmit`. `npm run check` is `tsc -p . && node --test`.
  - Shipped in this item: `json.ts` (duplicate keys, nulls, trailing text), `result.ts` (stage-result v1 and candidate rules), `frontmatter.ts`, `flow.ts`, `bundle.ts`, `check.ts`, and `index.ts` exporting `checkBundle` and `validateResult`, and CLI `check BUNDLE_DIR [--at COMMIT]` and `validate RESULT --flow F --node N`.
  - `check` prints one error per line in the LLD's format and exits `0` only when clean. Rules B1–B14 and every `gate.*` row hold, including the counterexamples in G2's fixtures.
  - Every fixture under `docs/sdlc/fixtures/results/`, `flows/`, and `bundles/` is a `node:test`, including the three valid results and `bundles/minimal/`.
  - `README.md` ≤200 lines and names the driver-only formats this package owns, even if later items fill them in.
  - No harness import and no runtime dependency. Pinned `typescript` devDependency only (S8), with a lockfile, through INTAKE.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check`. `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200`.
- **Blocked by** — `G1` — result and candidate rules implement the v1 contract and its fixtures; `G2` — bundle check implements the flow spec and its fixtures
- **Blocks** — `G5b` — the stage pipeline validates candidates with this reader; `G3` — `check bundles/sdlc` is this item's CLI; `G4` — `bundle-authoring` proves by running `check`; `G8` — followed-mode results are proved with `validate`
- **Out of scope** — The run loop, git, land, durable state, toolbox copy, and env-prep (`G5b`–`G5e`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- Later driver items edit this same package. Sharing files is not a blocker; merge, do not serialize beyond the blocker list.

### G5b: Driver loop — run root, state machine, stage pipeline

```json sdlc-item
{"slug": "driver-loop", "blockedBy": ["G0", "G5a"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check",
           "test \"$(wc -l < packages/sdlc-driver/README.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-5-core-driver-item-5`
- Branch: `item/<ticket-id>-driver-loop`

## Required

- **Outcome** — The driver can open a run root, walk a flow with a fake worker, and stop on the pipeline's own failures, without git land, durable state, or env-prep.
- **Acceptance** —
  - Implements `adapter.ts` (the `HarnessAdapter` interface), `facts.ts` (the driver-facts writer), `runroot.ts`, `machine.ts`, `stage.ts`, `prompts.ts`, `console.ts`, `labels.ts`, `index.ts` exporting `prepare` and `run` (extending G5a's exports), and the fake worker at `packages/sdlc-driver/test/fake-worker.ts`. The fake worker performs the scripted actions and misbehaviors in the Verify "Fake worker" paragraph and records argv and environment.
  - Run-root files the driver owns match `run-state.md` and the LLD: `driver.json`, `driver/state.json` only as far as the loop needs it, `index.jsonl`, `plan/items.json`, `asks/`, run folders, and the lock. `state-init`, `persist`, and `restore` still refuse when `SDLC_RUN_DIR` is set or the lock is held, once those commands exist; this item implements the lock those commands share.
  - Console lines match the LLD's fixed text, including the OpenCode summary ending `pick /sdlc, then enter RUN_ROOT to continue`.
  - These Verify scenarios are tests in this item: 3 (invalid candidate and repair run folder), 4 (manager `resume`, `defer`, `escalate`, invalid manager, operator-only stops), 5 (gate answer, `trial-gate`, paperwork `posted`), 8 (crash mid-stage and restart), and 16 (paperwork ends the stage before it starts, and a kill during paperwork replays).
  - Scenario 2's repair counter, `repair N/3` lines, and the pending `test-failure` or `fix` prompt are tests here. The land-red count is G5c's assertion, not a stub that passes here.
  - `README.md` stays ≤200 lines.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check`. `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200`. The tests above use the fake worker and G2's fixtures.
- **Blocked by** — `G0` — run-root files follow `run-state.md`; `G5a` — the pipeline accepts only candidates this reader validates
- **Blocks** — `G5c` — land and post-stage checks run on this loop; `G5d` — durable state, restore, and repin sit on this run root
- **Out of scope** — Git, land, snapshot, refs, tickets, scan, and proving-command execution (`G5c`). Toolbox copy, lease, drill, rehydrate, repin (`G5d`). Env-prep (`G5e`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G5c: Driver land — git, prove, snapshot, tickets

```json sdlc-item
{"slug": "driver-land", "blockedBy": ["G5b"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check",
           "test \"$(wc -l < packages/sdlc-driver/README.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#land-sub-machine`
- Branch: `item/<ticket-id>-driver-land`

## Required

- **Outcome** — The driver can prove, check, and land an item against a temporary bare origin, and refuse the worker misbehaviors the post-stage checks name.
- **Acceptance** —
  - Implements `git.ts` (hooks and fsmonitor off, replace objects off, no force option), `land.ts` (L1–L9 for item land), `prove.ts`, `snapshot.ts` including the driver-file ledger, `tracker.ts` (the local read recipe as fixed git argv), `scan.ts`, and `groom.ts` (frozen `groom.md` parser).
  - Proving lines come only from the frozen `groom.md` blob and pinned defaults. A copy edited in the item worktree has no effect.
  - These Verify scenarios are tests here, against a temporary bare origin with a `local` tickets branch: 1 (two-item flow, blocker, both `done`, `project-main` check), 2 (the land-red event counts exactly once, on top of G5b's repair tests), 6 (every land row named in the scenario), 7 (each post-stage check, including `refs`, `tickets`, and `extension`; command stages skip worker-only checks), 10 (worktree edits to proving commands do nothing; a `groom.md` changed after review stops filing), 12 (credential-shaped design record is `scan-secret` with no `allow`; a path hit is `scan-hit` and `allow` commits; text never shown), 13 (proving command and worker see none of the denylisted variables), 15 (N1 tickets cases), 18 (crash after a design-record push, and the worker-push case), and 19 (driver-file ledger).
  - Scenario 11's creation of `repo.git` and `worktrees/integrate` before any fetch is this item's git API. The `backend: linear` refusal and the harness-tree stop are Start step 2, before `repo.git` exists; they are not this API's callers. `state-init` (G5d) is the caller.
  - `README.md` stays ≤200 lines.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check`. `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200`.
- **Blocked by** — `G5b` — land and the checks run inside the stage pipeline and on its run root
- **Blocks** — `G5d` — `state-init` runs this item's first-start git; `G5e` — env command stages, chunk land, and re-entry extend this land sub-machine
- **Out of scope** — Durable state, toolbox copy, repin (`G5d`). The env block and chunk env land (`G5e`). Tracker writes and Linear (`G9`). `DER-565` and `DER-570`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- Scenario 11 is split as the acceptance says. G5d waits on G5c because `state-init` runs G5c's first-start git. Other shared edits to `packages/sdlc-driver` are file overlap, not blockers.

### G5d: Driver state — toolbox copy, lease, restore, repin

```json sdlc-item
{"slug": "driver-state", "blockedBy": ["G5b", "G5c"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check",
           "test \"$(wc -l < packages/sdlc-driver/README.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#durable-run-state`
- Branch: `item/<ticket-id>-driver-state`

## Required

- **Outcome** — A run can be prepared, persisted, drilled, restored, and repinned from the run root, and Start refuses a tampered toolbox copy.
- **Acceptance** —
  - Implements `state.ts`, `toolbox.ts`, `compiled.ts`, `backup.ts`, the `repin` export in `index.ts`, and CLI `readiness`, `toolbox`, `state-init`, `status`, `persist`, `restore`, and `drill`.
  - `state-init` refuses a second run root for a chunk slug whose state branch already exists (O21(a)).
  - Run prep's command sequence from the G0 skill is tested here on a fixture repo: R5–R10, including `toolbox`, `readiness`, `state-init`, and `drill` (O14).
  - These Verify scenarios are tests here: 9 (rehydrate and session backup), 11 (the `backend: linear` refusal and the changed harness-tree stop; both are Start step 2, before `repo.git`), 14 (bundle commit outside trunk, typed SHA, INTAKE record not satisfied by the bundle commit itself), 17 (pre-spawn harness re-check for an edited, added, or removed file), 20 (durable state at `pushed` against a temporary bare origin, every case in that scenario), 21 (restore and drill, every case, including the typed remote and the genesis pin), 22 (toolbox copy and compiled files, every case), and 25 (`/sdlc-repin` refusals and the three kill cases).
  - The drill writes nothing outside its `<tmp>`, including when it fails.
  - `README.md` stays ≤200 lines and now covers `driver.json`, `driver/state.json`, `driver/ledger.json`, `index.jsonl`, and `plan/items.json`.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check`. `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200`.
- **Blocked by** — `G5b` — persist, restore, and repin sit on the run root and the loop. G0 is already required through G5b; the skill text is on project-main before this item starts; `G5c` — `state-init` runs Start's first-start git (`repo.git`, `worktrees/integrate`), which is G5c's `git.ts`
- **Blocks** — `G5e` — chunk land re-renders compiled files with this item's `compiled.ts`; `G7` — the OpenCode host's start, restore confirmation, and `/sdlc-repin` call this driver
- **Out of scope** — Env-prep (`G5e`). The kickoff skill text (`G0`). `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- Accepted residuals this item must not reopen: O12, O15 (the driver never deletes the state branch), O17, O20, O21(a), O22.

### G5e: Driver env — env block, chunk land, re-entry

```json sdlc-item
{"slug": "driver-env", "blockedBy": ["G5c", "G5d"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check",
           "test \"$(wc -l < packages/sdlc-driver/README.md)\" -le 200"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#build-environment-gate`
- Branch: `item/<ticket-id>-driver-env`

## Required

- **Outcome** — The driver builds, proves, and lands the accepted `json sdlc-env` block, and re-enters that path when a persona asks for a missing capability.
- **Acceptance** —
  - Implements `env.ts`: parse the block, env command stages, dependency pre-steps, and the env branch.
  - Chunk land uses G5c's land sub-machine with `worktrees/env`, `env-prove`, and the env-reviewer trailer. In place of L8–L9 it sets `env.landCommit`, deletes the remote env branch, and re-renders compiled files.
  - Verify scenario 23 is a test: one fake dependency; `env-prove` order is toolchain, `setup`, `start`, `ready`, `reset`, then `prove`; a red baseline is `known` and reaches the env-verifier; an env-verify `fix` counts on the chunk repair counter; `env` gate `accept` lands, deletes the env branch, and re-renders compiled files; Groom starts only then; an edited block after the gate is `fail` with an `operator` stop; a `passEnv` name reaches the command stage and no worker.
  - Verify scenario 24 is a test: `env-capability:` ask; `env` re-enters `env-prep` and resumes the builder with the land commit; `spec` re-runs Spec, security, and the `spec` gate first; a dependency `ready` failure before proving commands is `environment not ready` and counts no repair.
  - O16 stays out of scope: a re-entry that needs new items is `defer`, not a driven Groom edit.
  - `README.md` stays ≤200 lines.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/sdlc-driver ci && npm --prefix packages/sdlc-driver run check`. `test "$(wc -l < packages/sdlc-driver/README.md)" -le 200`. Scenarios 23 and 24 use a fixture LLD and a fake dependency, not a real service.
- **Blocked by** — `G5c` — env stages and chunk land extend the land sub-machine and the proving wrapper; `G5d` — chunk land re-renders compiled files with `compiled.ts`
- **Blocks** — `G7` — the first harness hosts a driver that already implements env-prep and re-entry
- **Out of scope** — Filing an env-prep gate for building this chunk (no such gate). `DER-565` and `DER-570`. A driven amendment of `groom.md` when an env re-entry needs new items (O16). `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G3: SDLC bundle, tracker claim rule, `bundle-runs.md`

```json sdlc-item
{"slug": "sdlc-bundle", "blockedBy": ["G0", "G2", "G5a"], "skills": ["shell-safety"],
 "prove": ["test \"$(wc -l < docs/sdlc/bundle-runs.md)\" -le 150",
           "test \"$(wc -l < skills/test-failure-handler/SKILL.md)\" -le 60",
           "node packages/sdlc-driver/src/cli.ts check bundles/sdlc"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-3-the-sdlc-bundle-item-3`
- Branch: `item/<ticket-id>-sdlc-bundle`

## Required

- **Outcome** — `bundles/sdlc` is a bundle the driver accepts, the same-item claim rule is in the tracker skill, and `bundle-runs.md` owns the HLD rule changes.
- **Acceptance** —
  - `bundles/sdlc/` contains `bundle.md`, `flow.json`, and `personas/*.md` for every persona in the LLD table. `flow.json` has `entry: refine`, `itemEntry: build`, and the nodes from `refine` through `land`, including `env-prep` through `env-land` and the `env-builder`, `env-verifier`, and `env-reviewer` personas.
  - Prompt kinds match the LLD table, including `node-spec`'s required `## Build environment` section and `node-hld`'s `## Test harness and environment` section.
  - `skills/test-failure-handler/SKILL.md` is ≤60 lines and follows the steps in the LLD: it never edits proving commands, `groom.md`, or the env block, never adds a harness, and never moves the ticket. It has a `SOURCES.md` row.
  - `docs/sdlc/bundle-runs.md` (≤150) owns every HLD Rule changes row and routes run-root formats to `run-state.md`. One-line routes land in `docs/SDLC.md`, `docs/sdlc/subagents.md`, `build-review.md`, `branches-and-lands.md`, `plan-trial-spec.md`, `stage-result.md`, and `skills/debug/SKILL.md`. The `stage-result.md` route keeps that file ≤150.
  - The same-item claim rule is only the condition the LLD states, in `skills/tracker-sdlc/SKILL.md` and `adapters/local.md`. Contract version stays 2. The S5 review diff of `adapters/local.md` against `7a11696` is exactly one changed line, the assignee test in `change: claim`.
  - `node packages/sdlc-driver/src/cli.ts check bundles/sdlc` exits 0. That CLI is G5a's; this item does not reimplement it.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1–K7, with the one expected K5 difference recorded in the rule map. `test "$(wc -l < docs/sdlc/bundle-runs.md)" -le 150`. `test "$(wc -l < skills/test-failure-handler/SKILL.md)" -le 60`. `node packages/sdlc-driver/src/cli.ts check bundles/sdlc`.
- **Blocked by** — `G0` — the `bundle-runs.md` route to run-root formats targets `run-state.md`; `G2` — the bundle is written in the bundle and flow specs; `G5a` — the prove command runs G5a's `check` on `bundles/sdlc`
- **Blocks** — `G7` — the OpenCode end-to-end smoke runs `bundles/sdlc`
- **Out of scope** — Driver implementation (`G5b`–`G5e`), including env-prep code. `G4` and `G8`. `DER-565`, `DER-570`, and `G9`. Not blocked by G5b–G5e: their outputs are not inputs to this bundle.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- Clarification 15 and O8: this item waits for G0, G2, and G5a, and still builds beside G5b–G5e. The G5a wait is a blocker because the prove command executes G5a's CLI, not a separate land-order edge.

### G7: OpenCode plugin, first harness

```json sdlc-item
{"slug": "opencode-plugin", "blockedBy": ["G3", "G5d", "G5e"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/opencode-sdlc ci && npm --prefix packages/opencode-sdlc run check"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#behavior-6-harness-plugins-item-7-opencode-first-item-6-pi-second`
- Branch: `item/<ticket-id>-opencode-plugin`

## Required

- **Outcome** — OpenCode 1.19.3 can start, stop, and repin a run through `/sdlc`, with a worker plugin the operator's session does not load.
- **Acceptance** —
  - `packages/opencode-sdlc` matches the file table: TUI commands `/sdlc`, `/sdlc-stop`, and `/sdlc-repin`; server input guard; `opencode-adapter.ts`; `worker-config.ts`; `driver-main.ts`; hand-written `opencode-types.ts` (no `@opencode-ai/plugin` dependency); `worker/sdlc-worker.ts` not in package `exports`.
  - `/sdlc` takes the run root in a dialog, not as an argument (O10).
  - Unit tests: argv, env, and worker-config permission rules (read-only personas get no edit tool); preflight; worker path guard for `write`, `edit`, and `apply_patch` (links, `..`, `.git`, `~`); `sdlc_write` and `sdlc_result` on the shared fixtures; the three compaction hooks; `shell.env`. The item 5 suite runs through this adapter against a fake `opencode` that records argv, env, and the worker config.
  - O-T1–O-T10 from `maintainers/design/solo-dlc/opencode-server.md` run first, on the operator's machine, OpenCode 1.19.3, one local model, gated by `SDLC_OPENCODE_SMOKE=1`, spending no money. A failure uses that table's fallback. A fallback that names security or the operator waits for that answer before it is used. If O-T1 fails, the loopback fallback is not used until security rules on it. If O-T8 fails, O11's accepted fallback applies (toast and console warning; no second gate).
  - O-E2E: `smoke/run.sh` as the LLD specifies. Pass: both items `done` in order; two land commits with `Reviewed-by`; every `result.json` passes `sdlc-driver validate`; `meta.json` argv shows the `opencode run` flags; each worker-config file holds the persona's permission rules; no check failed.
  - Harness pin: npm `integrity` at install and `treeSha256` in `run.json`, checked at every start. OpenCode package version pinned to 1.19.3.
  - Definition of done: this acceptance, the prove line green, the manual OpenCode checks green, package README current, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/opencode-sdlc ci && npm --prefix packages/opencode-sdlc run check`. Then O-T1–O-T10, then O-E2E, with `SDLC_OPENCODE_SMOKE=1`.
- **Blocked by** — `G3` — O-E2E runs `bundles/sdlc`; `G5d` — start, restore, and `/sdlc-repin` are that driver's API; `G5e` — the hosted driver includes env-prep and re-entry. G5a–G5c are required through those two.
- **Blocks** — `G6` — the Pi plugin reuses this item's adapter tests, fake-harness pattern, and smoke fixture
- **Out of scope** — Pi (`G6`). `bundle-authoring` and followed mode (`G4`, `G8`). Linear credentials (S2, `G9`). `DER-565` and `DER-570`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Optional

- The manual smoke is acceptance, not a `prove` line: it needs the operator's machine and must not run inside `npm run check`.
- O6 (Pi version) is answered and gates only G6; it does not block this item.

### G6: Pi plugin, second harness

```json sdlc-item
{"slug": "pi-plugin", "blockedBy": ["G7"], "skills": ["lang-js-ts"],
 "prove": ["npm --prefix packages/pi-sdlc ci && npm --prefix packages/pi-sdlc run check"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#pi-host-shape-and-sdlc`
- Branch: `item/<ticket-id>-pi-plugin`

## Required

- **Outcome** — Pi, at the latest version at G6 build time, can start a detached run with `/sdlc RUN_ROOT` and can enforce the input guard.
- **Acceptance** —
  - O6 is answered (Alex, 2026-10-20): use the latest Pi at G6 build time and pin that version then. The first task is to look up the latest Pi release, pin it, re-read the Pi facts table at that version (it was read at `@mariozechner/pi-coding-agent` 0.73.1, now deprecated), and rerun P1–P7. O6 gates only this item.
  - `packages/pi-sdlc` matches the file table. The worker extension is not in the Pi package manifest. `pi-types.ts` replaces a dependency on the Pi package.
  - `/sdlc` takes `RUN_ROOT` as a typed argument (O10). `pi -p "/sdlc RUN_ROOT"` refuses.
  - Unit tests: argv and env builder; worker path guard (links, `..`, `.git`, `~`); `sdlc_write` and `sdlc_result` on the shared fixtures; compaction summary. Plugin and adapter run against a fake `pi` that records argv and env.
  - P1–P7 run on the operator's machine at the pinned version, one local model, gated by `SDLC_PI_SMOKE=1`, spending no money. Each failure uses the fallback in Trial-dependent decisions. P7 is O-E2E's fixture and pass conditions under the Pi adapter.
  - npm `integrity` recorded at install; `treeSha256` in `run.json`, checked at every start.
  - Definition of done: this acceptance, the prove line green, P1–P7 green, package README current, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — `npm --prefix packages/pi-sdlc ci && npm --prefix packages/pi-sdlc run check`. Then P1–P7 with `SDLC_PI_SMOKE=1`.
- **Blocked by** — `G7` — reuses its adapter tests, fake-harness pattern, and smoke fixture
- **Blocks** — `none`
- **Out of scope** — OpenCode fallbacks (`G7`). `G9`, `DER-565`, and `DER-570`. Choosing the Pi version before G6's build time (O6: latest at build time).
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G4: `bundle-authoring` skill

```json sdlc-item
{"slug": "bundle-authoring", "blockedBy": ["G2", "G5a"], "skills": [],
 "prove": ["node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/authored"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#items-4-and-8`
- Branch: `item/<ticket-id>-bundle-authoring`

## Required

- **Outcome** — An author following `skills/bundle-authoring/SKILL.md` produces a bundle the driver accepts, without the skill restating the specs.
- **Acceptance** —
  - The skill walks bundle layout, persona files, and `flow.json`, and ends by running `sdlc-driver check` until it exits 0.
  - It routes to `bundle-spec.md` and `flow-spec.md` and restates no rule.
  - Following it writes `docs/sdlc/fixtures/bundles/authored/`, and `check` exits 0 on that directory.
  - A `SOURCES.md` row exists for `bundle-authoring`.
  - Definition of done: this acceptance, the prove line green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1 and K7. `node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/authored`.
- **Blocked by** — `G2` — the skill routes to the bundle and flow specs; `G5a` — the prove command runs G5a's `check`
- **Blocks** — `none`
- **Out of scope** — The OpenCode and Pi plugins. The LLD says this item starts after the first harness works; that is not a blocker, because the skill does not read either plugin. `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

### G8: `sdlc-followed-mode` skill

```json sdlc-item
{"slug": "followed-mode", "blockedBy": ["G2", "G5a"], "skills": [],
 "prove": ["node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/minimal",
           "node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/refiner/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node refine",
           "node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/manager/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node manager",
           "node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/operator/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node ask"]}
```

- Type: Task
- Parent: `DER-421`
- LLD: `maintainers/design/solo-dlc/lld.md#items-4-and-8`
- Branch: `item/<ticket-id>-followed-mode`

## Required

- **Outcome** — Followed mode is the driver algorithm in prose, and a walk-through of `fixtures/bundles/minimal/` leaves results `validate` accepts.
- **Acceptance** —
  - The skill states the loop, the stage pipeline without process isolation, the same run folders and `result.json`, and the exit rule. The first line, every stage's prose, and every stop contain `followed, not enforced`.
  - At each separate-agent step it prints the handoff block from the LLD (UX Q2) and stops. A mint names the persona's compiled file. Runs are `plain`; Run prep offers only that level for a followed run.
  - It restates no rule that `bundle-spec.md` or `flow-spec.md` owns.
  - A walk-through of `docs/sdlc/fixtures/bundles/minimal/` writes three results. `docs/sdlc/fixtures/followed/minimal/refiner/run-1/result.json` is node `refine`. `docs/sdlc/fixtures/followed/minimal/manager/run-1/result.json` is the manager stage, persona `manager`, `choice` `escalate`, and `status` `needs_input`, validated with `--node manager`. `docs/sdlc/fixtures/followed/minimal/operator/run-1/result.json` is node `ask`. `refine` and `ask` remain the model and gate nodes. Each `validate` command below exits 0 once the checker accepts node `manager` for that driver-fixed stage. On the checker at G8 `07f4a8e`, `--node manager` exits with `has no node manager`.
  - A `SOURCES.md` row exists for `sdlc-followed-mode`.
  - Definition of done: this acceptance, the prove lines green, one `CHANGELOG.md` line under `## Unreleased` citing the ticket, and a rule map for every edited agent file.
- **Verify** — K1 and K7. `node packages/sdlc-driver/src/cli.ts check docs/sdlc/fixtures/bundles/minimal`. `node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/refiner/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node refine`. `node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/manager/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node manager`. `node packages/sdlc-driver/src/cli.ts validate docs/sdlc/fixtures/followed/minimal/operator/run-1/result.json --flow docs/sdlc/fixtures/bundles/minimal/flow.json --node ask`. The manager result's `choice` is `escalate` and its `status` is `needs_input`.
- **Blocked by** — `G2` — the walk-through uses `fixtures/bundles/minimal/`; `G5a` — prove runs `check` and `validate`
- **Blocks** — `none`
- **Out of scope** — A driver, a persist step, or any harness plugin. The LLD says this item starts after the first harness works; that is not a blocker, because the skill does not read the plugin. `DER-565`, `DER-570`, and `G9`.
- **Proposed fix** — `n/a — split from accepted Spec`
- **Removal alternative** — `n/a — split from accepted Spec`
- **Pick** — `n/a — split from accepted Spec`
- **Plan / Spec** — `n/a — split from accepted Spec`

## Graph

- Wave 1: G0, G1
- Wave 2: G2 ← G1
- Wave 3: G5a ← G1, G2
- Wave 4: G5b ← G0, G5a
- Wave 4: G3 ← G0, G2, G5a
- Wave 4: G4 ← G2, G5a
- Wave 4: G8 ← G2, G5a
- Wave 5: G5c ← G5b
- Wave 6: G5d ← G5b, G5c
- Wave 7: G5e ← G5c, G5d
- Wave 8: G7 ← G3, G5d, G5e
- Wave 9: G6 ← G7

O6 (Pi version) is answered: Alex, 2026-10-20: use the latest Pi at G6 build time and pin that version then. It gates only G6 and is not a blocker. No operator question is open: O1–O22 are answered in the LLD, and the accepted residuals are not build blockers.

Not groomed: G9.

Gates: `none`. No review items. G5a is the checker later prove commands run, not an integration gate.

Land order beyond these blockers: none.

Not used as blockers, on purpose: G4 and G8 do not wait on G7. The LLD's "after the first harness works" is not an output those skills need (Blockers rule 1). G3 does not wait on G5b–G5e (clarification 15, O8). Same-file edits inside `packages/sdlc-driver` are not blockers (rule 2).
