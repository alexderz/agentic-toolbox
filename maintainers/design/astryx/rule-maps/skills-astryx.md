# Rule map (added file) — `skills/astryx/SKILL.md`

Item: DER-775 (Astryx skill, incoming item).

Old: none (new skill id; SOURCES row pinned in cfe9251 before the body). New:
[`skills/astryx/SKILL.md`](../../../../skills/astryx/SKILL.md).

First-party body. Upstream facts: meta/astryx at `cb2558efd0bd1e8988b8bf3d47fc1252343858a9`
(MIT). No upstream text pasted beyond command names. Every row is **added**; the source column
names the manager ruling and the upstream file the facts come from.

| New section | Rule | Source |
| --- | --- | --- |
| Header, Actors | Upstream, pin, licence line; actors; no scripts, no network by the skill | ruling 1, ruling 8; `LICENSE` |
| Iron law | Facts come from the project's CLI at its version, never memory | ruling 3; plugin `SKILL.md` ("read the CLI, not the package files") |
| When to load | builder on UI code with an `@astryxdesign/*` dependency or an LLD/mockup naming Astryx; designer or architect choosing a React component library; not a language skill | ruling 2 |
| How to read Astryx facts | Runner table: `astryx` script, installed devDependency, scoped pinned `npx` for reads; never unscoped `npx astryx`; reads `search`, `component`, `hook`, `docs`, `template`, `build`, `manifest --json`; `--json`, `--dense`, `--detail` | ruling 3; root `README.md`, `packages/cli/README.md` L1–130, `packages/core/README.md`, `apps/docsite/src/app/llms.txt/route.ts` |
| Build workflow | `build`, then `template <name> <dir>` (writes the template's files into that folder; its receipt names them); keep frame, gap, padding; `template <Block>`; read props first; tokens; existing pages not re-scaffolded | ruling 4; plugin `SKILL.md` WORKFLOW |
| Delivery checks | Re-read; replace raw `div`/`span`, added stylesheet imports and `@apply`, hex/px; build and deliver the build; ui-craft pass; `verify-before-done` | ruling 4; plugin `SKILL.md` |
| What wins on conflict | mockups and stories → Astryx → `ui-craft` → `modern-web-guidance` and the language skill per modern-web-guidance's Precedence list | ruling 5; r1 finding 4 |
| Commands that change things outside the item | `npm i -g`, `init --user`, default `init`, `gap-report --confirm-public`, `swizzle`/`upgrade`/`template <dir>`/`theme`, hosted MCP, upstream plugin: fact plus allowed action | ruling 6; `init.doc.mjs`, `gap-report.doc.mjs`, `global.doc.mjs`, `apps/docsite/src/app/mcp/route.ts`, `plugins/astryx/README.md` |
| Choosing Astryx at design time | React 19+ peers; components, templates, tokens, themes, no build plugin, `className` overrides; Beta; charts canary, lab unpublished; dependencies added; record choice and version in LLD; pinned reads; MIT | ruling 7; root `README.md`, `packages/core/README.md` |

## r1 review changes (DER-775 r1 disposition, all twelve findings taken)

Old: `skills/astryx/SKILL.md` at 232ac65 (193 lines). New: 198 lines. Key: **changed** with the
r1 finding number; no rule dropped.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 42–46 | When to load step 4: not a language skill; loads beside the one language skill, `ui-craft`, `modern-web-guidance` | **changed** (r1-9): the load-with clause names the builder; designer and architect turns load no language skill | L42–47 |
| 100–101 | Build step 3: `template <name> <path>` writes a file | **changed** (r1-3): `template <name> <dir>` writes the template's files into that folder; its receipt names them | L101–102 |
| 116–117 | Delivery check 2: replace raw `div`/`span` | **changed** (r1-5): limited to lines the item adds or changes | L117–119 |
| 121–122 | Delivery check 4: replace hex/px | **changed** (r1-5): limited to lines the item adds or changes | L123–124 |
| 126–127 | Delivery check 6: `ui-craft` pass when the product uses it | **changed** (r1-6): route to the UI craft note; skip on option 2 or 3 | L128–130 |
| 132–134 | Never rows apply throughout; the earlier item wins | **changed** (r1-12): "the earlier item wins" stated once, with "name each conflict in your handoff" moved here | L135–138 |
| 137 | Item 1: a template never adds scope | **changed** (r1-12): allowed action added: drop template parts the mockups and stories do not ask for | L141–142 |
| 142–143 | Item 3: skip `ui-craft` on option 3 | **changed** (r1-6): skip on option 2 or 3 of the UI craft note | L147–148 |
| 144–148 | Items 4–5 (`modern-web-guidance`, then language skill); closing "earlier one wins" sentence | **changed** (r1-4, r1-12): one item routing to modern-web-guidance's Precedence list; closing sentence merged into L135–138 | L149–151 |
| 158 | `init` row | **changed** (r1-7): block goes to `AGENTS.md` and the Claude file (`CLAUDE.md`, else `.claude/CLAUDE.md`); adds `init --remove-agents`; theme feature writes `theme.template.ts` inside the item's scope | L161 |
| 159 | `gap-report` row | **changed** (r1-1): without `--confirm-public`, no public handler runs and no issue is filed; internal handlers always run | L162 |
| 160 | File-edit row | **changed** (r1-2, r1-3): `template <name> <dir>`; `upgrade --apply` also runs `hooks.postCodemod` | L163 |
| 161 | Hosted MCP row | **changed** (r1-10): connecting adds an MCP server to the agent's configuration; the operator may choose that | L164 |
| 172–173 | Design-time item 1: React peers | **changed** (r1-8): `@stylexjs/stylex` is a peer dependency too | L175–176 |
| 190–192 | Design-time item 6: read at the version the LLD will record | **changed** (disposition, open question 3): the architect reads the stable release with `npm view @astryxdesign/core version` (`latest`, never `@canary`), records it, and reads at that version | L193–197 |

## Meaning questions

- **MQ1.** "What wins on conflict" opens with one sentence: Never rows of loaded skills and
  `security-hardening` apply throughout. Ruling 5 does not list them. Resolved as a route, not a
  new rule: `security-hardening` Never rows bind every skill already, and `modern-web-guidance`
  Precedence item 1 states the same. Flagged to the manager in the builder report.
- **MQ2.** Delivery check 3 keeps the Astryx and theme CSS imports the setup requires; upstream's
  check says to replace "imported .css". Resolved by upstream's own setup (root `README.md`:
  "a few CSS imports plus a theme provider"): the check targets stylesheets the builder adds.
- **MQ3.** Does limiting delivery checks 2 and 4 to added or changed lines drop a rule? Resolved by
  r1 finding 5 and build step 8 ("change only what the item asks"): old lines stay out of scope.
