# Changelog

Newest first. Skip empty sections.

## Unreleased

### Added

- `tracker-sdlc` contract + Linear adapter, `sdlc-onboarding`, and the
  `tracker-skill.md` template (`DER-252`, `DER-254`, unreleased)
- Asana adapter for `tracker-sdlc` (`DER-252`, `DER-257`, unreleased)
- Jira adapter for `tracker-sdlc` (`DER-252`, `DER-256`, unreleased)
- `grok-acp` worker skill and `packages/grok-acp/` ACP client: offload a build
  to the local Grok Build CLI as an SDLC builder, mint or resume by label
  (no ticket, unreleased)
- Sanitized A2A JSON-RPC → HTTPS plain POST webhook adapter at
  `packages/a2a-webhook-adapter/` (`DER-209`, unreleased)

### Changed

- SDLC Entry is read-only; branches are cut at Brief; every tracker
  read/write goes through `tracker-sdlc` (`DER-252`, `DER-254`,
  unreleased)
