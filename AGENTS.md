# AGENTS

This repository is a **shared skills home**. It is not an application
repo. Claude Code: you were sent here from [CLAUDE.md](CLAUDE.md). Stay
on this file, then load what it names.

Git is the source of truth. Do not write skill bodies only on a local or
vendor mirror.

`maintainers/` holds build notes for this repository. If you are using
the toolbox, skip it; routing tables never point into it. If you are
working on this repository, read
[maintainers/AGENTS.md](maintainers/AGENTS.md) next; its `## Tracker`
governs.

## Public repo

This is a public, open-source repo.

- **Deliverables** (skills, human-facing docs, code, collateral): write
  for outside readers in a professional voice, per the project's style
  guide (default `docs-google-style`). No people's names beyond
  maintainer credits and git authorship, no who said what, and no
  private tracker workspace URLs or names, internal hostnames or
  IPs, credentials (see [Never](skills/security-hardening/SKILL.md#never)),
  or agent-session leftovers such as interview question labels. Bare
  ticket ids (`DER-123`) are fine.
- **Agent context** (`maintainers/design/<chunk>/` design records,
  `maintainers/.agents/`, other `maintainers/` notes, scratch notes)
  can be informal: civil and credential-free, not tone-reviewed.
- **Commit messages, PR descriptions, and tags** are public and
  effectively permanent: write them for outside readers.

## How to load

Do not paste skill or SDLC bodies into this file. **Read** the named
path, or **pack** its text into a subagent prompt per
[Spawn prompts](docs/sdlc/subagents.md#spawn-prompts).

| What | When | How |
| --- | --- | --- |
| **SDLC** | Any project, ticket, chunk, or multi-agent run | **Read [docs/SDLC.md](docs/SDLC.md)** before implementing. |
| **Roles** | You need a role's name or job | **Read [Roles](docs/SDLC.md#roles).** |
| **Ask the operator** | Any gate, waiver, blocker, or unclear choice | **Read [Asking the operator](docs/SDLC.md#asking-the-human)** and follow it. |
| **Requirements** | Chunk Brief, Gather: a fuzzy idea or an interview | **Read `skills/discover-the-idea/SKILL.md`.** |
| **Refine** | Chunk Brief, Refine: refining a brief, as the refiner agent | **Read `skills/yagni/SKILL.md`.** |
| **Incoming item** | Bug report, red build, unit failure, mechanical ticket | **Read [Entry](docs/sdlc/entry-brief-repo.md#entry), then [Item brief](docs/sdlc/entry-brief-repo.md#item-brief).** Do not load `discover-the-idea`. |
| **Research** | Purchase, product shortlist, or market research | **researcher** persona: **read `skills/buying-researcher/SKILL.md`**. Not an SDLC role or step: [Roles](docs/SDLC.md#roles). |
| **UX** | User stories, high-level UX, or screen mockups | **designer:** **read `skills/ux-design/SKILL.md`**. |
| **Artifacts** | Writing HLD, LLD, tickets, epics, track/roadmap, PoC, decision, changelog, PR, monthly, human how-to, AGENTS stub, or repo tracker skill (`tracker-skill.md`) | **Read `skills/sdlc-artifacts/SKILL.md`** and copy the matching `templates/` file. A chunk brief uses `discover-the-idea` instead. An incoming item uses `bug.md` or `task.md`. |
| **Debug** | Failure while implementing a chosen fix, or unexpected behavior in Build | A **new** ticket that is not in Build → follow **Incoming item**. In Build, or after a chosen fix: **read `skills/debug/SKILL.md`** (default). Alternatives: `debug-pocock`, `debug-anthropic`. Load **one**. Then `tdd` + `verify-before-done`. At item Brief, the troubleshooter may load `debug` for root cause and must **not** implement. |
| **Tracker** | Any tracker read or write: file, claim, move, block, comment, list ready work | **Read `skills/tracker-sdlc/SKILL.md`**. Use the **product repo's own** `## Tracker`. The skill loads the product repo's `.agents/tracker/SKILL.md`, or `sdlc-onboarding` when the setup check fails. Only the **manager** writes: [Tracker](docs/SDLC.md#tracker). |
| **Docs** | Human how-to or agent-facing comments after Spec | **Read `skills/docs-google-style/SKILL.md`**. |
| **A skill** | The id applies to this turn | **Read `skills/<id>/SKILL.md`** in this repo. |
| **Skill ids** | Checking a skill id, its ownership, or its SHA pin | **Read [SOURCES.md](SOURCES.md)**. Agents at work never remint a skill: [Roles](docs/SDLC.md#roles). Changing a skill body is maintainer work: [Intake](docs/INTAKE.md) plus a new **security** cut. |
| **Language** | Writing or reviewing code | Load at most one language skill per turn: [iron law](skills/language-router/SKILL.md#iron-law). **Read `skills/language-router/SKILL.md`**: its [map](skills/language-router/SKILL.md#map), [load-with list](skills/language-router/SKILL.md#load-with-list) and [no-language turns](skills/language-router/SKILL.md#no-language-turns). |
| **Workers** | The operator picks Grok Build over ACP as a builder | **Read `skills/grok-acp/SKILL.md`**. Operator opt-in: load it only then. |
| **Diagrams** | The operator asks for a diagram, such as one in the PR into `main` | **Read `skills/pr-lens/SKILL.md`**. Operator opt-in: load it only then. |
| **Branches and lands** | Branching an item, or landing one | **Read [branches-and-lands.md](docs/sdlc/branches-and-lands.md)**. |
| **Subagents** | Minting, resuming, or prompting a subagent or worker | **Read [subagents.md](docs/sdlc/subagents.md)**. |
| **Knowledge** | Facts about a model, vendor, API, or platform that are not a skill | **Read [knowledge/README.md](knowledge/README.md)**, then `knowledge/<domain>/<kind>/<slug>.md`. |

## Intake (security)

Before any third-party content, complete **security** intake:
[docs/INTAKE.md](docs/INTAKE.md).

## Related

- README and bundles: [README.md](README.md)
- SDLC (load this): [docs/SDLC.md](docs/SDLC.md)
- Knowledge: [knowledge/README.md](knowledge/README.md)
- License: [LICENSE](LICENSE) (MIT), [NOTICE](NOTICE)
- Claude Code entry: [CLAUDE.md](CLAUDE.md)
