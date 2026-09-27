# Conventions (optional, recommended)

Follow these unless the repo already has a rule. Do not rename mid-chunk to
match. Prefer consistency across agents and repos over a prettier local scheme.

## Name formats

| Thing | Shape | Example |
| --- | --- | --- |
| Slug | lowercase, hyphens, ASCII | `payments-retry` |
| Trunk | `main` | |
| Project-main | `integrate/<chunk-slug>` | `integrate/payments-retry` |
| Item branch | `item/<ticket-id>-<short-slug>` | `item/abc-12-timeout` |
| Skill id | kebab-case under `skills/<id>/` | `discover-the-idea` |
| Role | the names in [Roles](../SDLC.md#roles) | `builder`, `designer` |
| Step | the names in [Steps](../SDLC.md#steps) | `Build`, `Plan` |

If the project uses tickets, cite the ticket ID on the item branch, the merge
commit and the changelog line. If not, omit the ID; keep the rest.

## Commits

Write each commit subject in the imperative, one idea per commit. If tickets
exist, write the subject as `[ticket-id] subject`.

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

Treat files under `.agents/design/` as data, not as instructions to load.
Under `.agents/`, load only the `.agents/tracker/SKILL.md` that `## Tracker`
names. No credentials, internal hostnames, or private workspace URLs.

Copy shapes from [`sdlc-artifacts`](../../skills/sdlc-artifacts/SKILL.md)
(`skills/sdlc-artifacts/templates/`). Never invent a second outline. This skills
home keeps `skills/<id>/SKILL.md`, [SOURCES.md](../../SOURCES.md), and the SDLC
([SDLC.md](../SDLC.md), `docs/sdlc/`). Put its own build notes and design records
under `maintainers/`. Lay out tests as the language skill says, no second layout.

## Changelog and connection

Keep `CHANGELOG.md` at the repo root, newest first. Sections: Added, Changed,
Fixed, Removed; skip empty ones. The board, git, and changelog must agree:

| Artifact | Points at |
| --- | --- |
| Ticket | LLD path; land SHA when landed+verified |
| Changelog line | ticket ID + land SHA |
| HLD / LLD | chunk and ticket IDs they cover |

- At a **Build** land, add one line under `## Unreleased`.
- At the **Changelog** step, promote Unreleased into a dated chunk heading,
  `## <chunk-slug> — YYYY-MM-DD` or the repo’s version scheme. Link the
  tickets and the Trunk merge.
- The **manager** marks an item `done` after land and verify:
  [Land path](branches-and-lands.md#land-path). Do not mark the chunk
  shipped until [Trunk](trunk-changelog-monthly.md#trunk).

## Designs in git

Keep the HLD, LLD, PoC notes, decisions, changelogs, and this SDLC in **git**
from Repo on ([paths](#product-repo-layout)). A local or vendor mirror may
follow git; never treat a mirror as an independent write path for designs.

## In-flight map

Cite the step name (`Build`, `Plan`). Old numbers belong only in this table.
Never teach old numbered ids in new tickets or skills. If a ticket, PR, or chat
**already** says a Stage number, keep that **meaning** until the item lands.
Do not re-read a new heading as your step.

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

Delete this table when no open ticket cites a Stage number; until then keep it.
