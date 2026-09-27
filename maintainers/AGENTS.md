# AGENTS (maintainers)

Entry point for sessions that work on this repository itself: skills,
docs, packages, or process. Agents that only use the toolbox stop at the
root [AGENTS.md](../AGENTS.md) and do not load this file.

Read the root [AGENTS.md](../AGENTS.md) and [docs/SDLC.md](../docs/SDLC.md)
first. This file adds only what is specific to building this repository.
Write agent text to the [writing standard](writing-standard.md#standard).

The tracker skill path in `## Tracker` is relative to this directory:
[`maintainers/.agents/tracker/SKILL.md`](.agents/tracker/SKILL.md).

## Tracker

Linear — load .agents/tracker/SKILL.md (tracker-sdlc v2).

## Execution

Parallelism: max

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
