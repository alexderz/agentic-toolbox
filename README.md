# Agentic Toolbox

Skills here are **tools**, not a marketplace dump. Agents pick the right
tool for the job. The process applies to software, docs, process
changes, and other tickets using this home. SDLC work is keyed by
**role** (`architect`, `designer`, `builder`, `tester`, `security`,
`manager`, `operator`).

Git is the source of truth. A local or vendor mirror may follow. Do not
treat a mirror as an independent write path for skill bodies.

**License:** MIT ([LICENSE](LICENSE)). `skills/debug-anthropic/` is
Apache-2.0 ([NOTICE](NOTICE)). Pins: [SOURCES.md](SOURCES.md).

How the work gets done, in plain language (including a calculator
walkthrough):
[docs/SDLC.md](docs/SDLC.md#how-software-gets-built).

## Roles

| Role | Job |
| --- | --- |
| **architect** | Design, HLD/LLD, adversarial review of approach |
| **designer** | User stories, high-level UX, mockups when there is a screen |
| **builder** | Implement and ship |
| **tester** | Mechanical CI, hooks, cleanup |
| **security** | Security gates across the SDLC, including skill intake |
| **manager** | Process and SDLC after-act. Does not bless ships |
| **operator** | Human in the loop: exceptions, vuln severity, extra hosts |

Improvise beyond predefinition when the work needs it. Do not remint a
skill that already lives here.

PRs welcome. Maintainer: [alexderz](https://github.com/alexderz). See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Bundles

There is no plugin manifest yet. Natural install groups:

| Bundle | Skills | When |
| --- | --- | --- |
| **sdlc-process** | `discover-the-idea`, `ux-design`, `sdlc-artifacts`, `tracker-sdlc`, `sdlc-onboarding`, `tdd`, `debug`, `docs-google-style`, `verify-before-done`, `pr-review`, `yagni`, `security-hardening`, `shell-safety` | Any repo using this process. Chunk gather-only turns load `discover-the-idea` and no language skill. Incoming items skip that interview. Default debug is `debug`; `debug-pocock` / `debug-anthropic` are alternatives |
| **research** | `buying-researcher` | **researcher** persona when the ask is a buy or market study. Not an SDLC step |
| **workers** | `grok-acp` | Operator opt-in. Offload a build to the local Grok CLI over ACP. Needs the `grok-acp` package on `PATH` |
| **diagrams** | `pr-lens` | Operator opt-in. Architecture and data-flow diagrams for a PR, rendered locally and attached with `gh`. Needs Node (`npx`) and `gh` 2.99+ |
| **languages** | `language-router`, `lang-*`, `golang-safety`, `golang-testing`, `golang-security`, `modern-python` | Writing or reviewing code. Load **at most one** language-family skill per turn |
| **optional / empty** | `cursor-cloud-agents-when` | Placeholder. No `SKILL.md` yet |

`lang-go`, `lang-python`, and `lang-shell` are **pointers**. They do not
count as a skill load. They route to `golang-*`, `modern-python`, and
`shell-safety`. `shell-safety` sits in **sdlc-process** because every
agent shell is in scope; `lang-shell` only points at it.

Authoritative pins: [SOURCES.md](SOURCES.md). Routing table:
[skills/language-router/SKILL.md](skills/language-router/SKILL.md).

## Intake rules (security first)

Placeholders remain for empty ids. Bodies land via **security** intake
and a compress, not a vendor paste.

- Do not install a second process pack beside this repo’s ids. See
  [docs/INTAKE.md](docs/INTAKE.md).
- Pin every third-party cherry-pick **SHA** in [SOURCES.md](SOURCES.md).
  Empty SHA cells mean the body is not here yet.
- **security** intake before any third-party content lands in this repo.
- **No auto-update.** No marketplace install. No scripts. No secrets.
- First-party skills (`tracker-sdlc`, `sdlc-onboarding`,
  `cursor-cloud-agents-when`, language guides) are written here; they are not vendor copies.

Directories under `skills/<id>/` are placeholders (`.gitkeep` only) until
a body lands.

## Skill ids

See [SOURCES.md](SOURCES.md) for upstream, SHA, license, and notes.

### sdlc-process

| Id | Ownership |
| --- | --- |
| `discover-the-idea` | First-party gatherer (interview → brief). Chunk Brief Gather. Do not load on an incoming item |
| `ux-design` | Designer. Stories + UX at Plan; mockups at Spec if there is a screen |
| `sdlc-artifacts` | First-party templates (HLD, LLD, tickets, track, changelog, …) |
| `tracker-sdlc` | First-party contract for every tracker read/write, plus per-tracker adapters. Loads the product repo's `.agents/tracker/SKILL.md` |
| `sdlc-onboarding` | First-party. Discovers a repo's tracker, proposes a mapping, writes the repo tracker skill on confirm |
| `tdd` | Rewrite (MIT). Pin in [SOURCES.md](SOURCES.md) |
| `debug` | Default systematic debug (MIT). Alternatives: `debug-pocock`, `debug-anthropic` |
| `docs-google-style` | Distill of Google developer docs style. Human + agent surfaces |
| `verify-before-done` | Rewrite (MIT). Pin in [SOURCES.md](SOURCES.md) |
| `pr-review` | Rewrite (MIT). Pin in [SOURCES.md](SOURCES.md) |
| `yagni` | First-party restraint |
| `security-hardening` | First-party Always/Ask/Never |
| `shell-safety` | First-party Always/Ask/Never. Pin in [SOURCES.md](SOURCES.md) |

### research

| Id | Ownership |
| --- | --- |
| `buying-researcher` | First-party market / buy research. **researcher** persona; not SDLC |

### workers

| Id | Ownership |
| --- | --- |
| `grok-acp` | First-party. Grok Build over ACP as a builder. Prose only; the client is [packages/grok-acp](packages/grok-acp/). Operator opt-in |

### diagrams

| Id | Ownership |
| --- | --- |
| `pr-lens` | Rewrite of coldteadotai/pr-lens (MIT). Local render + PR attach only; no canvas, no `analyze`. Pin in [SOURCES.md](SOURCES.md). Operator opt-in |

### languages

| Id | Ownership |
| --- | --- |
| `language-router` | First-party map |
| `lang-go` / `lang-python` / `lang-shell` | First-party pointers |
| `golang-safety` / `golang-testing` / `golang-security` | Rewrite of samber/cc-skills-golang (MIT) |
| `modern-python` | First-party (MIT). uv / ruff / ty / pytest |
| `lang-rust`, `lang-js-ts`, `lang-c`, `lang-cpp`, `lang-csharp`, `lang-java`, `lang-kotlin`, `lang-ruby`, `lang-php`, `lang-swift`, `lang-dart`, `lang-sql`, `lang-web-markup`, `lang-lua`, `lang-docker`, `lang-terraform`, `lang-makefile`, `lang-powershell`, `lang-protobuf` | First-party language guides |

### optional / empty

| Id | Ownership |
| --- | --- |
| `cursor-cloud-agents-when` | First-party placeholder (Cursor-specific) |

## Packages

Not skills. Optional stdlib utilities that live next to the skills home.

| Package | What |
| --- | --- |
| [grok-acp](packages/grok-acp/) | ACP client for the local Grok Build CLI: mint or resume a session, one prompt turn per call. Used by the `grok-acp` skill. MIT, stdlib only |
| [a2a-webhook-adapter](packages/a2a-webhook-adapter/) | A2A JSON-RPC peer → HTTPS plain POST webhook (Cursor Grok Bot allowlist). MIT, stdlib-first |

## Knowledge

Compressed facts (not skills): [knowledge/README.md](knowledge/README.md).
Path `knowledge/<domain>/<kind>/<slug>.md`. First note:
[Jev](knowledge/ai/models/jev.md).

## Related

- SDLC: [docs/SDLC.md](docs/SDLC.md)
- Architecture: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Intake: [docs/INTAKE.md](docs/INTAKE.md)
- First cherry-pick candidates: [maintainers/CHERRY-PICK-CANDIDATES.md](maintainers/CHERRY-PICK-CANDIDATES.md)
- CI hooks (fmt/lint): [maintainers/CI-HOOKS-PLAN.md](maintainers/CI-HOOKS-PLAN.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

Agents landing in this repo: start at [AGENTS.md](AGENTS.md). Claude
Code reads [CLAUDE.md](CLAUDE.md), which points at AGENTS.md. Work on
this repository itself starts at
[maintainers/AGENTS.md](maintainers/AGENTS.md).
