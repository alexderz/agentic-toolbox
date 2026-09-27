# Changelog

Newest first. Skip empty sections.

## Unreleased

### Added

- `maintainers/writing-standard.md`: the writing standard for agent text
  (ten rules, banned names, rule owners, protected rules, rule-map
  format, checks K1–K10), routed from `maintainers/AGENTS.md` (`DER-291`)
- Maintainer eval step: `maintainers/AGENTS.md` `## Evals` (a PR into
  `main` that changes agent text gets T1–T3 runs, three repeats per
  model, regressions first) and `maintainers/evals/` (procedure, T1 and
  T2 cards, keys and fixture, run template, baseline) (`DER-292`)
- Maintainer eval task T3 in `maintainers/evals/`: build one item of a
  groomed toy chunk to landed+verified; task card, answer key and the
  frozen Groom fixture (`DER-293`)
- `groom.md` template in `sdlc-artifacts`: the Groom plan, reviewed
  before any ticket is filed, then frozen (`DER-275`)
- `sdlc-onboarding` Execution area: asks for and records the Build
  Parallelism ceiling (`max`, `serial`, or `at most <N>`) (`DER-275`)
- `pr-lens` skill, operator opt-in: architecture and data-flow diagrams
  for a pull request, rendered locally with `@coldtea/pr-lens-cli@0.8.1`
  and attached with `gh --attach`. Rewrite of coldteadotai/pr-lens;
  canvas and `analyze` excluded (`DER-274`, unreleased)
- `grok-acp` worker skill and `packages/grok-acp/` ACP client: offload a build
  to the local Grok Build CLI as an SDLC builder, mint or resume by label
  (no ticket, unreleased)
- Sanitized A2A JSON-RPC → HTTPS plain POST webhook adapter at
  `packages/a2a-webhook-adapter/` (`DER-209`, unreleased)

### Changed

- `tdd` skill: light wording pass, same teaching; Ask first names the operator and routes to the SDLC ask rule (`DER-319`)
- `pr-review`: section links fixed, the distinct-reviewer rule routed to
  `docs/sdlc/subagents.md#item-agents`; pins unchanged (`DER-320`)
- `debug` skill: light wording pass (duplicate "default" line dropped); `SOURCES.md` note records it, pins unchanged (`DER-321`)
- `debug-pocock` light pass: duplicate lines dropped, Iron law states its
  run-once step as an instruction; pins unchanged (`DER-322`)
- `debug-anthropic` skill: light wording pass; the Fix step now says to name the fix's side effects; pins unchanged (`DER-323`)
- `docs-google-style` light pass: one punctuation fix, one apostrophe
  fix, and the duplicate `## Source` section dropped; pins unchanged (`DER-324`)
- `shell-safety` light pass, same Always, Ask first and Never rules: the **security** gate names Review, not PR, and the workers rule routes to the SDLC index (`DER-325`)
- `verify-before-done` light pass: the verifier and landed+verified rules route to their SDLC owners, and "HITL" reads "operator in the loop"; pins unchanged (`DER-326`)
- `golang-testing`: light pass; the duplicate pin and samber-pack lines dropped, load-with and workers-bypass rules routed to their owners; `SOURCES.md` note added (`DER-327`)
- `golang-security` light pass: one `language-router` route replaces the
  pairing line; the workers line names **security** (`DER-328`)
- `golang-safety`: Go-skill choice routes to `language-router`; typed-nil
  example compiles; nil-map `cap` row fixed (`DER-329`)
- `pr-lens` light pass: one duplicate clause dropped from the
  description and one upstream name made consistent; CLI pin and
  local-only limits unchanged (`DER-330`)
- `ux-design` light pass: the approver is named the operator, and the review loop routes to `docs/sdlc/plan-trial-spec.md#ux` (`DER-331`)
- `sdlc-onboarding` rewritten to the writing standard, same `## Tracker`
  and `## Execution` formats: numbered steps, a When table, and the
  proposal shape routed to `ask-human.md` (`DER-310`)
- `sdlc-artifacts` and its `changelog.md` template cite the land SHA, not
  a merge SHA or a PR; the tracker-writer line routes to the SDLC index
  `#tracker`; the AGENTS stub names `## Tracker` (`DER-311`)
- `yagni` skill rewritten to the writing standard, same rules (`DER-313`)
- `buying-researcher` skill and its references rewritten to the writing standard, same research method: one owner per rule, a numbered procedure, and a Never list with allowed actions (`DER-314`)
- `grok-acp` skill rewritten to the writing standard: "manager" replaces
  "orchestrator", each Never rule names the allowed action, and branch
  source and fallback route to their SDLC owners; permission posture,
  labels and own-item limits unchanged (`DER-315`)
- `security-hardening` rewritten to the writing standard, same rules:
  Ask first as numbered steps, Never and Ask first rows unchanged, and
  the workers, intake and Monthly rules routed to their owners (`DER-316`)
- `language-router` owns the language map (merged from `AGENTS.md`), the
  load-with list and the no-language turns, and loads on any code turn
  (`DER-318`)
- `docs/INTAKE.md` rewritten to the writing standard, same six-step
  checklist and rules; the tracker-skill **security** read is numbered
  steps (`DER-336`)
- Tracker-sdlc HLD fixes the two stale lines DER-271 names: signing follows git config; a chunk's onboarding lands as its own reviewed item before Plan (`DER-338`).
- `modern-python` rewritten to the writing standard, same rules; the
  load-with list routes to `language-router` (`DER-317`)
- `docs/SDLC.md` index rewritten to the writing standard: numbered
  tracker and asking rules, a Names list, the ask shape routed to
  `ask-human.md`, and the skill table replaced by routes to the root
  `AGENTS.md` load table and `SOURCES.md` (`DER-299`)
- SDLC conventions (`docs/sdlc/conventions.md`) rewritten to the writing
  standard, same rules: the item `done` rule routes to the land path, the
  old Stage-number rule sits with the in-flight map, and "this file" names
  the SDLC again (`DER-307`)
- `docs/SDLC.md` moves, text unchanged, into an index, step files under
  `docs/sdlc/`, and a people doc, `docs/how-software-gets-built.md`; the
  index adds How to read and a Read column, and links follow the move
  (`DER-298`)
- Maintainer notes move under `maintainers/` (design records, planning
  notes, this repo's `## Tracker` and tracker skill) with their own
  entry point, `maintainers/AGENTS.md`; the root `AGENTS.md` routing
  skips them. The `tracker-sdlc` setup check reads the `AGENTS.md` that
  governs your work, with the repo skill path relative to it; contract
  stays v2 (`DER-272`)
- SDLC Groom: a clean reviewer passes `groom.md` before any ticket is
  filed from the reviewed commit, then it freezes; blockers only for real
  output needs, waves and gates by shape, review items, late insertion;
  Build dispatches up to the `Parallelism:` ceiling (`DER-275`)

## tracker-sdlc — 2026-09-25

Tracker-agnostic SDLC (`DER-252`, PR #2).

### Added

- `tracker-sdlc` contract + Linear adapter, `sdlc-onboarding`, and the
  `tracker-skill.md` template (`DER-252`, `DER-254`, PR #2)
- Asana adapter for `tracker-sdlc` (`DER-252`, `DER-257`, PR #2)
- Jira adapter for `tracker-sdlc` (`DER-252`, `DER-256`, PR #2)
- Trello adapter for `tracker-sdlc` (`DER-252`, `DER-258`, PR #2)
- Local adapter for `tracker-sdlc`: tickets on a shared `tickets` git
  branch with a race-tested write recipe (`DER-252`, `DER-259`, PR #2)

### Changed

- A chunk's onboarding commit lands as its own reviewed item before
  Plan; agents use the product repo's own `## Tracker`; a repo tracker
  skill may copy the local adapter's fenced shell recipe but has no
  `scripts/` files (`DER-252`, `DER-270`, PR #2)
- Only the orchestrator writes to the tracker; Plan and Groom post to
  tickets with `comment`; land commits carry `Reviewed-by:`; the
  onboarding commit lands through Review (`DER-252`, `DER-262`,
  PR #2)
- `tracker-sdlc` contract v2: claim posts a `Claimed by` comment and
  re-checks for an earlier claim; Linear blockers stay listed when
  resolved; repo-skill budget ≤180; SDLC lands are local, serialized
  merges with no PRs (`DER-252`, `DER-260`, PR #2)
- SDLC Entry is read-only; branches are cut at Brief; every tracker
  read/write goes through `tracker-sdlc` (`DER-252`, `DER-254`,
  PR #2)
