# Sources

Pin every third-party cherry-pick here **before** the body lands. Empty
SHA cells mean no body may land.

Repo license is MIT ([LICENSE](LICENSE)); `skills/debug-anthropic/` is
Apache-2.0 ([NOTICE](NOTICE)). See [docs/INTAKE.md](docs/INTAKE.md).
**security** intake before any third-party content. No auto-update.

| Skill | Upstream | SHA | License | Notes |
| --- | --- | --- | --- | --- |
| tracker-sdlc | first-party (this repo) | first-party | MIT | Contract + 5 adapters, prose only. A repo tracker skill has no `scripts/` files and no executable blocks except the fenced shell recipe from `adapters/local.md`; **security** compares it with the adapter's current text (only placeholder fills and baked-in gotchas may differ). Every tracker read/write goes through it and the product repo's `.agents/tracker/SKILL.md`. No vendor body. No `scripts/` in this skill. |
| sdlc-onboarding | first-party (this repo) | first-party | MIT | Onboarding, prose only. Discovers the repo's tracker, proposes to the operator, writes `## Tracker` + `.agents/tracker/SKILL.md` on confirm. No vendor body. No scripts/. |
| discover-the-idea | first-party (this repo) | first-party | MIT | Architect gatherer. Chunk Brief Gather (interview). Do not load on an incoming item. Load the skill; do not paste it into the SDLC. Inspired by public grilling method. |
| sdlc-artifacts | first-party (this repo) | first-party | MIT | Templates for HLD/LLD/tickets/Groom plan/track/changelog/UX. Load the skill; do not paste the SDLC into artifacts. Chunk brief stays discover-the-idea. Incoming item: bug.md / task.md. |
| ux-design | first-party (this repo); variants from mattpocock/skills prototype UI; anti-default UI from addyosmani/agent-skills frontend-ui-engineering; composition from hueyexe/frontend-agent-skills | first-party body; pocock 74ca5fe077456a0b3b2f5310cf9430999fd0b5fd (intent) | MIT (body); MIT upstream intent | Designer. Medium-agnostic mockups. Agent review vs requirements, then human. Not those packs. |
| buying-researcher | first-party (this repo) | first-party | MIT | Research skill for the **researcher** persona when the ask is a buy or market study. Not an SDLC step. Recommend; do not spend. |
| grok-acp | first-party (this repo) | first-party | MIT | Worker skill: run the local Grok Build CLI as an SDLC builder over ACP, with label registry and resume. Prose only; the client is the package `packages/grok-acp/`. Runs Grok with maximum permissions by operator order (2026-09-21). Operator opt-in per ask. |
| cursor-cloud-agents-when | first-party (this repo) | | | When to use Cursor Cloud Agents. No vendor body. |
| tdd | obra/superpowers (test-driven-development) | intent b36e0829c6d0140e93cfef2ca599b1b07d4a7797; merge afb2b6f4b8a6f9c62633b32a9166ca50de72c1c6 (PR #9); blob 57e74392c0d10f3ae35c9e0a735016a2b731d1e9 for skills/tdd/SKILL.md | MIT upstream / rewrite | Compress not paste |
| pr-review | obra/superpowers (requesting-code-review + receiving-code-review) + mattpocock/skills (engineering/code-review) | superpowers b36e0829c6d0140e93cfef2ca599b1b07d4a7797; pocock 3cca18b368ae95cdbdebbff572ccafa662551015 (intent pins; body rewrite) | MIT upstream / rewrite | Id `pr-review`; reviewer ≠ builder; receive-review on the builder; Standards/Spec; review skills do not write. First-party wording edit DER-260 (no internal PRs; Review stays an explicit gate; PRs only for outside/remote workers). Pins unchanged. security-cleared 2026-09-24. |
| debug | obra/superpowers (systematic-debugging) | b36e0829c6d0140e93cfef2ca599b1b07d4a7797 (intent pin; body rewrite) | MIT upstream / rewrite | Default debug. SKILL only. Load one of debug / debug-pocock / debug-anthropic |
| debug-pocock | mattpocock/skills (engineering/diagnosing-bugs) | 74ca5fe077456a0b3b2f5310cf9430999fd0b5fd (intent pin; body rewrite) | MIT upstream / rewrite | Alternative debug. SKILL only. No scripts/ |
| debug-anthropic | anthropics/knowledge-work-plugins (engineering/skills/debug) | ebd7990cfa9495937da7726741e1ee6a96788565 (intent pin; body rewrite) | Apache-2.0 upstream / rewrite | Alternative debug. SKILL only. Dropped CONNECTORS |
| docs-google-style | Google developer documentation style guide | distill of https://developers.google.com/style (not a git SHA) | MIT (distill) | Human how-tos + agent-facing comments. Not a vendor paste |
| security-hardening | first-party (this repo) | e207b9012d33b55014053617cf2992dca1619c70 (merge of PR #3); last main merge 97a0469776978c9f83bf74c9dfa8bb6947d4100b (PR #20 scanner AE1); blob 812124cf3d919a6557ece44b2532d198a97187b2 for skills/security-hardening/SKILL.md | MIT | Always/Ask/Never compress + docs/INTAKE.md; not a vendor body |
| shell-safety | first-party Always/Ask/Never; obra/superpowers `using-superpowers` (intent) | first-party (body); Superpowers `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (intent pin) | MIT (body); MIT upstream intent | Superpowers has no dedicated shell-safety skill — `using-superpowers` (do not skip the gate) is the process pin. konstruktoid bash-secure is **reference only** — not a vendor install. No `scripts/`. Compatible with `security-hardening`. |
| verify-before-done | obra/superpowers (verification-before-completion) | b36e0829c6d0140e93cfef2ca599b1b07d4a7797 (intent pin; body rewrite) | MIT upstream / rewrite | Compress not paste; HITL on flaky/MEDIUM |
| yagni | first-party restraint | first-party (body) | MIT | Thin Always/Ask/Never; ≤40 lines |
| modern-python | first-party (this repo) | first-party | MIT | uv / ruff / ty / pytest. SKILL only; no scripts/ |
| golang-testing | samber/cc-skills-golang (`golang-testing`) | 22c58a55a0a799b901aa251172923180bad9e010 | MIT upstream / rewrite | SKILL only; skip evals/clawhub |
| golang-security | samber/cc-skills-golang (`golang-security`) | 22c58a55a0a799b901aa251172923180bad9e010 (intent pin; body rewrite) | MIT upstream / rewrite | SKILL only / no evals / no scripts; pairs with golang-testing / golang-safety |
| golang-safety | samber/cc-skills-golang (`golang-safety`) | 22c58a55a0a799b901aa251172923180bad9e010 | MIT upstream / rewrite | SKILL only / no evals / no scripts/; compress not paste; pair golang-testing + golang-security |
| pr-lens | coldteadotai/pr-lens (`skills/pr-lens`) | 09f6378c082ff8ddb17e211f36bfc71c2f2b8d86 (intent pin; body rewrite) | MIT upstream / rewrite | Opt-in; operator asks. Local render + PR attach only (no `canvas`, no `analyze`). CLI pinned exactly `@coldtea/pr-lens-cli@0.8.1`; every new release is a one-line SOURCES bump with a security read (no automatic patch releases). SKILL only; references linked at the pin, not vendored. No `scripts/`. CLI subcommands allowlisted to `validate` and `render`. The CLI's transitive dependencies float (`npx` uses no lockfile). Scanner waived by maintainer for DER-274 (scanner work: DER-273); manual security read done. Compared with upstream at Monthly |
| language-router | first-party (this repo) | first-party | MIT | Map only. Pointers do not count as a load. Cap 1–2 language skills. |
| lang-go | first-party pointer (this repo) | first-party | MIT | Routes to golang-safety / golang-testing / golang-security. Does not remint. |
| lang-python | first-party pointer (this repo) | first-party | MIT | Routes to modern-python. Does not remint. |
| lang-shell | first-party pointer (this repo) | first-party | MIT | Routes to shell-safety. Does not remint. |
| lang-rust | first-party (this repo) | first-party | MIT | Distill, not Microsoft/leonardomso dump. |
| lang-js-ts | first-party (this repo) | first-party | MIT | TS-strict default; JS is the subset. |
| lang-c | first-party (this repo) | first-party | MIT | Bounds, alloc, sanitizers. strncpy is not safe strcpy. |
| lang-cpp | first-party (this repo) | first-party | MIT | RAII, Rule of 0. Split from C. |
| lang-csharp | first-party (this repo) | first-party | MIT | Nullable, IDisposable, async. |
| lang-java | first-party (this repo) | first-party | MIT | Language only. No Spring. |
| lang-kotlin | first-party (this repo) | first-party | MIT | Null safety, coroutines. No Compose religion. |
| lang-ruby | first-party (this repo) | first-party | MIT | Language only. No Rails religion. |
| lang-php | first-party (this repo) | first-party | MIT | PHP 8+ types. No eval. No md5 passwords. |
| lang-swift | first-party (this repo) | first-party | MIT | Optionals, value types, Sendable. |
| lang-dart | first-party (this repo) | first-party | MIT | Language only. No Flutter architecture. |
| lang-sql | first-party (this repo) | first-party | MIT | Parameterize. Postgres default. |
| lang-web-markup | first-party (this repo) | first-party | MIT | HTML+CSS+a11y. One skill. |
| lang-lua | first-party (this repo) | first-party | MIT | 1-based, pairs vs ipairs. |
| lang-docker | first-party (this repo) | first-party | MIT | Non-root, pinned bases, no secrets in layers. |
| lang-terraform | first-party (this repo) | first-party | MIT | Plan is read. State is sensitive. |
| lang-makefile | first-party (this repo) | first-party | MIT | Real DAG. Quoted vars. |
| lang-powershell | first-party (this repo) | first-party | MIT | No iex. Stop on error. |
| lang-protobuf | first-party (this repo) | first-party | MIT | Fields forever. Do not edit generated stubs. |

## Packages

Not skills. First-party utilities. Empty SHA still means no body may land for
**skill** ids; package rows use `first-party` when the tree is in this repo.

| Package | Upstream | SHA | License | Notes |
| --- | --- | --- | --- | --- |
| `packages/grok-acp/` | first-party (this repo) | first-party | MIT | Stdlib ACP client for the local Grok Build CLI (`grok agent stdio`): mint or resume a session by label, one prompt turn per call, JSON result. Runs Grok with every permission granted; that posture is an operator order recorded in `skills/grok-acp/SKILL.md`. Not a skill. |
| `packages/a2a-webhook-adapter/` | first-party sanitized extract; protocol inspired by private court adapter in `alexderz/grok-bot-perm` PRs #6 and #7 | first-party | MIT | A2A JSON-RPC → plain HTTPS POST. No house secrets, mesh endpoints, or required house names. Not a skill. DER-209. |

## Knowledge distillations

Not skills. Layout: [knowledge/README.md](knowledge/README.md). Compress;
live vendor docs win. Pin the extract source.

| Note | Upstream | SHA | License | Notes |
| --- | --- | --- | --- | --- |
| `knowledge/ai/models/jev.md` | `alexderz/grok-bot-perm` `docs/integrations/typesafe.md`; TypeSafe public docs | grok-bot-perm `8b2cfffca35d938337f3af524187e6c998ee3e89` | MIT | Jev / System One. Not a skill. Do not marketplace-install TypeSafe’s pack here. |
