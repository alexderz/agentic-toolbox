# AGENTS (maintainers)

Entry point for sessions that work on this repository itself: skills,
docs, packages, or process. Agents that only use the toolbox stop at the
root [AGENTS.md](../AGENTS.md) and do not load this file.

Read the root [AGENTS.md](../AGENTS.md) and [docs/SDLC.md](../docs/SDLC.md)
first. This file adds only what is specific to building this repository.

The tracker skill path in `## Tracker` is relative to this directory:
[`maintainers/.agents/tracker/SKILL.md`](.agents/tracker/SKILL.md).

## Tracker

Linear — load .agents/tracker/SKILL.md (tracker-sdlc v2).

## Execution

Parallelism: max

## Where notes go

- Design records: `maintainers/design/<chunk>/` (HLD, LLD, UX,
  comparables), shapes from
  [`sdlc-artifacts`](../skills/sdlc-artifacts/SKILL.md).
- Planning notes (candidates, plans, goals): `maintainers/`.
- Everything here is agent context under the root
  [Public repo](../AGENTS.md#public-repo) rule: informal is fine, but
  civil and credential-free. No tone review.
- Skills, human-facing docs, and packages stay where the root
  `AGENTS.md` puts them; they never link into `maintainers/` for
  routing.
