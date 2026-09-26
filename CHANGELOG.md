# Changelog

Newest first. Skip empty sections.

## Unreleased

### Added

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
