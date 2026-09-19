# AGENTS

This repository is a **shared skills home**. It is not an application
repo. Claude Code: you were sent here from [CLAUDE.md](CLAUDE.md). Stay
on this file, then load what it names.

Git is the source of truth. Do not write skill bodies only on a local or
vendor mirror.

## How to load

Do not paste skill or SDLC bodies into this file. **Read** the named
path (or **pack** that text into a subagent prompt — see Spawn prompts
in the SDLC).

| What | When | How |
| --- | --- | --- |
| **SDLC** | Any project, ticket, chunk, or multi-agent run | **Read [docs/SDLC.md](docs/SDLC.md)** before implementing. Owns named steps, grain (chunk vs item), asking the human, project-main, subagents, pack vs point, land path, and optional conventions. |
| **Need a person** | Any gate, waiver, blocker, or unclear choice | Stop. Use [Asking the human](docs/SDLC.md#asking-the-human) / template `ask-human.md`: plain question, options, recommendation and why, what to reply. That wait blocks **this** issue; other items may proceed. Do not continue that part until they answer. |
| **Requirements** | Fuzzy idea, interview, or refining a brief | **Chunk:** Gather: **read `skills/discover-the-idea/SKILL.md`**. Refine: load `yagni` on a **different** agent. Loop is in the SDLC. No language skill on a gather- or refine-only turn. |
| **Incoming item** | Bug report, red build, unit failure, mechanical ticket | **Read [Entry](docs/SDLC.md#entry) + [Brief](docs/SDLC.md#brief) first.** Do **not** load `discover-the-idea`. Do not implement yet. Problem + fix vs removal, then align Plan/Spec. |
| **Research** | Purchase, product shortlist, or market research | **researcher** persona: **read `skills/buying-researcher/SKILL.md`** when that ask is in play. Not an SDLC step. |
| **UX** | User stories, high-level UX, or screen mockups | **designer:** **read `skills/ux-design/SKILL.md`**. Agent review vs requirements (no reviewer taste), then human unless they waive. |
| **Artifacts** | Writing HLD, LLD, tickets, epics, track/roadmap, PoC, decision, changelog, PR, monthly, human how-to, or AGENTS stub | **Read `skills/sdlc-artifacts/SKILL.md`** and copy the matching `templates/` file. Chunk brief stays `discover-the-idea`. Incoming item: `bug.md` / `task.md` (problem + fix vs removal). |
| **Debug** | Failure while implementing a chosen fix, or unexpected behavior in Build | If this is a **new** ticket (not already in Build), follow **Incoming item** (Entry + Brief). In Build, or after a chosen fix: **read `skills/debug/SKILL.md`** (default). Alternatives: `debug-pocock`, `debug-anthropic`. Load **one**. Then `tdd` + `verify-before-done`. At item Brief, the troubleshooter may load `debug` for root cause and must **not** implement. |
| **Docs** | Human how-to or agent-facing comments after Spec | **Read `skills/docs-google-style/SKILL.md`**. Human: what it is, how it works, how to use it. Agent: locatable contracts. |
| **A skill** | The id applies to this turn | **Read `skills/<id>/SKILL.md`**. Ids are listed below. |
| **Language** | Writing or reviewing code | At most **one** language-family skill (table below, or load `language-router` first if ambiguous). Pointers `lang-go` / `lang-python` / `lang-shell` do not count as a load. |
| **Pins / intake** | Third-party content, or checking ownership | [SOURCES.md](SOURCES.md), [docs/INTAKE.md](docs/INTAKE.md) |
| **Knowledge** | Facts about a model, vendor, API, or platform that are not a skill | Read [knowledge/README.md](knowledge/README.md), then `knowledge/<domain>/<kind>/<slug>.md`. Do not remint as a skill. Live vendor docs win. |

Process skills that may load with the one language skill: `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`, `yagni`,
`sdlc-artifacts`, `debug`, `docs-google-style`.
`shell-safety` when the turn includes shell. `discover-the-idea` is
gather-only — no language skill on that turn. `buying-researcher` is
research-only — no language skill on that turn.

Skills live under `skills/<id>/` in this repo. Knowledge distillations
live under `knowledge/<domain>/<kind>/`. Do not install a second
process pack beside these ids (see [docs/INTAKE.md](docs/INTAKE.md)).

## Skills are tools, keyed by role

| Role | Job |
| --- | --- |
| architect | Design, HLD/LLD, adversarial review of approach |
| designer | User stories, high-level UX, mockups when there is a screen |
| builder | Implement and ship |
| tester | Mechanical CI, hooks, cleanup |
| security | Security gates and skill intake |
| manager | Process, SDLC after-act, land path (PR vs merge-and-delete) |
| operator | HITL, exceptions, vuln severity |
| researcher | Market / buy research when that ask is in play. Not an SDLC step |

Pick the tool that matches the role. Improvise when the work needs it.
Do not remint a skill that already has an id here.

Per work item: mint a **clean builder** and a **clean verifier** on the
first pass; **resume** those subagents for later builds and verifies of
the same item. Do not reuse the builder as the verifier. On mint, **pack**
skill/MCP text into the prompt when that is cheaper, otherwise **point**
the child at the ids (host default: it reads the skill files). Resume is
delta-only — do not re-pack.

Branch items off **project-main** (`integrate/<slug>`) when that branch
exists; land each merge-ready item there (serialized), then land
project-main on trunk. Incoming item with no live project-main: branch from trunk,
Review versus trunk, merge-and-delete. Do not invent a project-main for
a lone incoming item.

**manager** picks PR vs merge-and-delete from how many items are in
flight. Groom sets board **blockers** (Linear `blockedBy` / `blocks`).
Do not start or land an item with an open blocker unless the operator
said so. Full rules: [docs/SDLC.md](docs/SDLC.md) (Groom, Build,
Project-main, Subagents per work item, Spawn prompts).

## Inventory

Authoritative table: [SOURCES.md](SOURCES.md). Bundles: [README.md](README.md).

Skill ids with `SKILL.md` (do not remint without a new **security** cut):

- `discover-the-idea`
- `ux-design`
- `sdlc-artifacts`
- `tdd`
- `debug`
- `debug-pocock`
- `debug-anthropic`
- `docs-google-style`
- `verify-before-done`
- `pr-review`
- `shell-safety`
- `security-hardening`
- `modern-python`
- `golang-testing`
- `golang-security`
- `golang-safety`
- `yagni`

Research (not SDLC). **researcher** loads when relevant:

- `buying-researcher`

Language pack. Do not remint the Go / Python / Shell ids above.

- `language-router`
- `lang-go` (pointer → one of `golang-safety` / `golang-testing` / `golang-security`)
- `lang-python` (pointer → `modern-python`)
- `lang-shell` (pointer → `shell-safety`)
- `lang-rust`
- `lang-js-ts`
- `lang-c`
- `lang-cpp`
- `lang-csharp`
- `lang-java`
- `lang-kotlin`
- `lang-ruby`
- `lang-php`
- `lang-swift`
- `lang-dart`
- `lang-sql`
- `lang-web-markup`
- `lang-lua`
- `lang-docker`
- `lang-terraform`
- `lang-makefile`
- `lang-powershell`
- `lang-protobuf`

First-party placeholders / empty dirs (no body claim until SHA +
`SKILL.md` on `main`):

- `tracker-sdlc`
- `cursor-cloud-agents-when`

Load by id from this repo.

## Language routing

Load **at most one** language-family skill per turn. A second is allowed
only for a truly mixed-language diff. Never load the catalog.
`tdd` / `verify-before-done` / `pr-review` / `security-hardening` /
`yagni` / `debug` / `docs-google-style` may load alongside.
`discover-the-idea` does not: gather- and refine-only turns load no
language skill. Incoming-item Brief (problem + fix vs removal) loads
no language skill. `ux-design` does not: UX-only turns load no language
skill. `buying-researcher` does not: research-only turns load
no language skill. Load **one** of `debug` / `debug-pocock` /
`debug-anthropic`.

If `language-router` is installed and the table is ambiguous, load it
first, then the one skill it names.

Pointer ids (`lang-go`, `lang-python`, `lang-shell`) exist so every
identified language has a file. They do **not** count as a skill load.
They route to the ids below.

| Files / signals | Load |
| --- | --- |
| `*.go`, `go.mod` | `golang-safety` by default. `golang-testing` when writing tests. `golang-security` when the change touches input, auth, SQL, files, subprocesses, or crypto. Pick **one**. Optional pointer: `lang-go`. |
| `*.py`, `pyproject.toml`, `uv.lock` | `modern-python`. Optional pointer: `lang-python`. |
| `*.sh`, `*.bash`, shebang bash/sh, agent shell | `shell-safety`. Optional pointer: `lang-shell`. |
| `*.rs`, `Cargo.toml` | `lang-rust` |
| `*.ts`, `*.tsx`, `*.js`, `*.mjs`, `*.cjs`, `tsconfig.json`, `package.json` | `lang-js-ts` |
| `*.c`, `*.h` and no C++ files | `lang-c` |
| `*.cpp`, `*.cc`, `*.cxx`, `*.hpp` | `lang-cpp` |
| `*.cs`, `*.csproj`, `*.sln` | `lang-csharp` |
| `*.java`, `pom.xml`, `build.gradle` | `lang-java` |
| `*.kt`, `*.kts` | `lang-kotlin` |
| `*.rb`, `Gemfile` | `lang-ruby` |
| `*.php`, `composer.json` | `lang-php` |
| `*.swift`, `Package.swift` | `lang-swift` |
| `*.dart`, `pubspec.yaml` | `lang-dart` |
| `*.sql` | `lang-sql` |
| `*.html`, `*.htm`, `*.css`, `*.scss` | `lang-web-markup` |
| `Dockerfile`, `*.dockerfile`, `compose.y*ml` | `lang-docker` |
| `*.tf`, `*.hcl` | `lang-terraform` |
| `Makefile`, `GNUmakefile` | `lang-makefile` |
| `*.ps1`, `*.psm1` | `lang-powershell` |
| `*.proto` | `lang-protobuf` |
| `*.lua` | `lang-lua` |

Stubs (no skill body — official docs only): Elixir, Scala, Haskell, Zig,
Solidity, Perl, Objective-C, R, Assembly.

Frameworks (React, Spring, Rails, FastAPI, Flutter) are **not** language
skills. Do not invent one mid-session.

## Intake (security)

Before any third-party content:

1. Pin the cherry-pick SHA in [SOURCES.md](SOURCES.md).
2. Complete **security** intake ([docs/INTAKE.md](docs/INTAKE.md)).
3. No marketplace install, no auto-update, no scripts, no secrets in this
   repo.

Empty SHA cells mean the body must not exist yet.

## Related

- README: [README.md](README.md)
- SDLC (load this): [docs/SDLC.md](docs/SDLC.md)
- Knowledge: [knowledge/README.md](knowledge/README.md)
- License: [LICENSE](LICENSE) (MIT), [NOTICE](NOTICE)
- Claude Code entry: [CLAUDE.md](CLAUDE.md)
