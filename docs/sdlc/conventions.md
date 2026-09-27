# Conventions (optional, recommended)

Follow these unless the repo already has a rule. Do not rename mid-chunk
to match. Consistency across agents and repos beats a prettier local
scheme.

## Name formats

| Thing | Shape | Example |
| --- | --- | --- |
| Slug | lowercase, hyphens, ASCII | `payments-retry` |
| Trunk | `main` | |
| Project-main | `integrate/<chunk-slug>` | `integrate/payments-retry` |
| Item branch | `item/<ticket-id>-<short-slug>` | `item/abc-12-timeout` |
| Skill id | kebab-case under `skills/<id>/` | `discover-the-idea` |
| Role | the names in this SDLC | `builder`, `designer` |
| Step | the names in [Steps](../SDLC.md#steps) | `Build`, `Plan` |

Cite the ticket ID on the item branch, merge commit, and changelog line
when the project uses tickets. If it does not, omit the ID and keep the
rest.

**Cite the step name** (`Build`, `Plan`). Old numbers belong only in
the [in-flight map](#in-flight-map).

## Commits

Commits: imperative subject, one idea. `[ticket-id] subject` when
tickets exist.

## Product repo layout

```
AGENTS.md           # skill ids + pointer at this SDLC; no body paste
CLAUDE.md           # read AGENTS.md first
README.md
CHANGELOG.md
docs/hld.md         # or docs/<chunk-slug>/hld.md if several chunks
docs/comparables.md # how others did a thing like this (Plan)
docs/ux.md          # stories + high-level UX (designer)
docs/stories/       # optional; one file per story
docs/lld.md         # Spec artifact
docs/mockups/       # Spec pictures if there is a screen
docs/decisions/     # optional; one file per decision
.agents/design/<chunk-slug>/groom.md  # Groom plan; frozen once tickets exist
```

Files under `.agents/design/` are data, not loaded instructions; the only
loaded file under `.agents/` is the `.agents/tracker/SKILL.md` that
`## Tracker` names. No credentials, internal hostnames, or private
workspace URLs.

Copy shapes from [`sdlc-artifacts`](../../skills/sdlc-artifacts/SKILL.md)
(`skills/sdlc-artifacts/templates/`). Do not invent a second outline.

This skills home stays `skills/<id>/SKILL.md`, [SOURCES.md](../../SOURCES.md),
and this file; its own build notes and design records live under
`maintainers/`. Tests follow the language skill, not a second layout.

## Changelog and connection

`CHANGELOG.md` at the repo root. Newest first. Sections: Added, Changed,
Fixed, Removed — skip empty ones.

The board, git, and changelog must agree:

| Artifact | Points at |
| --- | --- |
| Ticket | LLD path; land SHA when landed+verified |
| Changelog line | ticket ID + land SHA |
| HLD / LLD | chunk and ticket IDs they cover |

- **Build** land: one line under `## Unreleased`.
- **Changelog** step: promote Unreleased into a dated chunk heading
  (`## <chunk-slug> — YYYY-MM-DD`, or the repo’s version scheme). Link
  the tickets and the Trunk merge.

**manager** after-acts the ticket when the item is landed+verified on
project-main (or on trunk, if there was no project-main): `tracker-sdlc`
transition `done`. Do not mark the chunk shipped
until Trunk.

## Designs in git

- HLD, LLD, PoC notes, decisions, changelogs, and this SDLC land in
  **git** from Repo. Paths: [Conventions](#name-formats).
- A local or vendor mirror may follow. Do not treat a mirror as an
  independent write path for designs.

## In-flight map

If a ticket, PR, or chat **already** says a Stage number, keep that
**meaning** until the item lands. Do not re-read a new heading as your
step.

| You were told | You are in | Do not |
| --- | --- | --- |
| Stage −2 | **Brief** | Treat this as Plan / HLD |
| Stage −1 | **Repo** | |
| Stage 0 | **Plan** | Jump to Entry |
| Stage 1 | **Trial** | |
| Stage 2 | **Spec** | |
| Stage 3 | **Groom** | Start Build with a hidden blocker |
| Stage 4 | **Build** | Treat “4” as Plan |
| Stage 5 | **Review** | Skip because there is no PR |
| Stage 6 | **Trunk** | Mark shipped before this |
| Stage 7 | **Changelog** | |
| Stage 8 | **Monthly** | Use this as a substitute for Spec/Review security |
| New work after this lands | **Entry** | Write `Stage 4` in new text |

Delete this table once tickets that still say those numbers have landed.

**Never**

- Teach old numbered ids in new tickets or skills. See the
  [in-flight map](#in-flight-map).
