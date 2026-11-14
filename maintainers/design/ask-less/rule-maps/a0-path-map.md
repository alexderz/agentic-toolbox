# Path map — A0, SDLC move

Item: DER-730 (A0 of DER-712). Old: `main` at c26f424. New: this item's
branch. A0 moves files and rewrites paths only; no rule changes, so it
carries this path map instead of rule maps (R47). Procedure and rule
sets: [A0 steps](../lld.md#a0-steps) and
[A0 link rules](../lld.md#a0-link-rules).

## Moved files

Every heading and `<a id>` anchor is unchanged: the old and new bodies
differ only by the A0 link rules ([A0 check](../lld.md#a0-check) part 1).

| Old path (lines) | New path (lines) | Anchors (old → new) | Rule set |
| --- | --- | --- | --- |
| `docs/SDLC.md` (174) | `skills/sdlc/SKILL.md` (178: 4 frontmatter lines + 174) | `#asking-the-human`, `#how-to-read`, `#roles`, `#names`, `#tracker`, `#grain`, `#asking-the-operator`, `#steps` → same | `idx` |
| `docs/sdlc/branches-and-lands.md` (69) | `skills/sdlc/references/branches-and-lands.md` (69) | `#branches`, `#project-main`, `#land-path`, `#never` → same | `ref` |
| `docs/sdlc/build-review.md` (102) | `skills/sdlc/references/build-review.md` (102) | `#build`, `#open-blockers`, `#dispatch`, `#definition-of-done`, `#debug-in-build`, `#skills-home-dod`, `#review` → same | `ref` |
| `docs/sdlc/conventions.md` (100) | `skills/sdlc/references/conventions.md` (100) | `#name-formats`, `#commits`, `#product-repo-layout`, `#changelog-and-connection`, `#designs-in-git`, `#in-flight-map` → same | `ref` |
| `docs/sdlc/entry-brief-repo.md` (134) | `skills/sdlc/references/entry-brief-repo.md` (134) | `#entry`, `#brief`, `#chunk-brief`, `#item-brief`, `#repo` → same | `ref` |
| `docs/sdlc/groom-step.md` (139) | `skills/sdlc/references/groom-step.md` (139) | `#names`, `#iron-law`, `#blockers`, `#waves`, `#gates`, `#review-items`, `#procedure`, `#1-draft`, `#2-review`, `#3-file`, `#4-freeze`, `#late-insertion`, `#incoming-item` → same | `ref` |
| `docs/sdlc/plan-trial-spec.md` (148) | `skills/sdlc/references/plan-trial-spec.md` (148) | `#plan`, `#comparables`, `#ux`, `#trial`, `#spec`, `#mockups`, `#security-gate`, `#documentation` → same | `ref` |
| `docs/sdlc/stage-result.md` (150) | `skills/sdlc/references/stage-result.md` (150) | `#status`, `#schema`, `#rules`, `#examples`, `#pass`, `#fail`, `#blocked`, `#needs_input`, `#out-of-scope` → same | `ref` |
| `docs/sdlc/stage-result-migration.md` (83) | `skills/sdlc/references/stage-result-migration.md` (83) | `#prepare-at-a-safe-boundary`, `#adopt-the-contract`, `#check-the-next-invocation`, `#preserve-history-and-close-the-migration` → same | `ref` |
| `docs/sdlc/subagents.md` (136) | `skills/sdlc/references/subagents.md` (136) | `#item-agents`, `#fallback`, `#step-agents`, `#tracker-writes`, `#writable-worktree`, `#spawn-prompts`, `#workers` → same | `ref` |
| `docs/sdlc/trunk-changelog-monthly.md` (34) | `skills/sdlc/references/trunk-changelog-monthly.md` (34) | `#trunk`, `#changelog`, `#monthly` → same | `ref` |
| `docs/INTAKE.md` (55) | `skills/sdlc/references/intake.md` (55) | `#checklist`, `#workers`, `#layout-only-exception` → same | `itk` |
| — | `docs/SDLC.md` (7), pointer page | — (links `skills/sdlc/SKILL.md` and its `#asking-the-human`) | LLD step 6 text |

## Edited files

Each differs from c26f424 only by its rule set (A0 check part 2).

| Files | Rule set or edit |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md` | `root` |
| `SOURCES.md` | `root`; new `sdlc` row above `tracker-sdlc` (step 7); path-edit note on `pr-review`, `tdd`, `shell-safety`, `verify-before-done`, `golang-testing`, `golang-security`, `ux-design`, `ui-craft`, `security-hardening`, with body blobs for `tdd` and `security-hardening` (step 8) |
| `skills/<id>/SKILL.md` for the 19 ids in the LLD table; `skills/sdlc-artifacts/templates/{agents-stub,changelog}.md` | `skl` |
| `docs/ARCHITECTURE.md` | `arc` |
| `docs/security-skill-packs/README.md` | `ssp` |
| `knowledge/ai/vendors/security-skill-packs-2026-10-18.md`, `knowledge/ai/vendors/x-chatter-security-skill-packs-2026-10-18.md` | `kn` |
| `maintainers/AGENTS.md`, `maintainers/CHERRY-PICK-CANDIDATES.md`, `maintainers/CI-HOOKS-PLAN.md`, `maintainers/goal.md` | `mnt` |
| `maintainers/writing-standard.md` | `mnt` except L142; L141 file-map link → `design/ask-less/lld.md#a0-file-map` (step 9) |
| `CHANGELOG.md` | the A0 line under `## Unreleased`, `### Changed` (step 10) |

Not touched: `docs/engineering-with-ai/log.md`, `maintainers/design/**`
outside this file, `maintainers/evals/**`.

## Protected rows

A0 changes only paths in these rows; each maps `kept`. Mechanical checks:
A0 check part 6.

| Protected rule | Old path | New path | Disposition |
| --- | --- | --- | --- |
| `security-hardening` Never, Ask first | `skills/security-hardening/SKILL.md` | same | kept (links only) |
| Intake checklist | `docs/INTAKE.md` | `skills/sdlc/references/intake.md` | kept |
| `tracker-sdlc` Claim, Never, Ask first | `skills/tracker-sdlc/SKILL.md` | same | kept (links only) |
| `adapters/local.md` recipe | `skills/tracker-sdlc/adapters/local.md` | same | kept (untouched) |
| `grok-acp` posture, labels, own-item limits | `skills/grok-acp/SKILL.md` | same | kept (links only) |
| Public-repo rule | `AGENTS.md` | same | kept (untouched) |
| SDLC index `#roles`, `#tracker` | `docs/SDLC.md` | `skills/sdlc/SKILL.md` | kept |
| `branches-and-lands.md#never` | `docs/sdlc/branches-and-lands.md` | `skills/sdlc/references/branches-and-lands.md` | kept |
| `subagents.md#tracker-writes` | `docs/sdlc/subagents.md` | `skills/sdlc/references/subagents.md` | kept; A2 adds its line under `## Step agents`, not here |

## Meaning questions

None: no wording changes.
