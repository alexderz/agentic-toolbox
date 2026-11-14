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
| Build workflow | `build`, then `template <name> <path>`; keep frame, gap, padding; `template <Block>`; read props first; tokens; existing pages not re-scaffolded | ruling 4; plugin `SKILL.md` WORKFLOW |
| Delivery checks | Re-read; replace raw `div`/`span`, added stylesheet imports and `@apply`, hex/px; build and deliver the build; ui-craft pass; `verify-before-done` | ruling 4; plugin `SKILL.md` |
| What wins on conflict | mockups and stories → Astryx → `ui-craft` → `modern-web-guidance` → language skill | ruling 5 |
| Commands that change things outside the item | `npm i -g`, `init --user`, default `init`, `gap-report --confirm-public`, `swizzle`/`upgrade`/`template <path>`/`theme`, hosted MCP, upstream plugin: fact plus allowed action | ruling 6; `init.doc.mjs`, `gap-report.doc.mjs`, `global.doc.mjs`, `apps/docsite/src/app/mcp/route.ts`, `plugins/astryx/README.md` |
| Choosing Astryx at design time | React 19+ peers; components, templates, tokens, themes, no build plugin, `className` overrides; Beta; charts canary, lab unpublished; dependencies added; record choice and version in LLD; pinned reads; MIT | ruling 7; root `README.md`, `packages/core/README.md` |

## Meaning questions

- **MQ1.** "What wins on conflict" opens with one sentence: Never rows of loaded skills and
  `security-hardening` apply throughout. Ruling 5 does not list them. Resolved as a route, not a
  new rule: `security-hardening` Never rows bind every skill already, and `modern-web-guidance`
  Precedence item 1 states the same. Flagged to the manager in the builder report.
- **MQ2.** Delivery check 3 keeps the Astryx and theme CSS imports the setup requires; upstream's
  check says to replace "imported .css". Resolved by upstream's own setup (root `README.md`:
  "a few CSS imports plus a theme provider"): the check targets stylesheets the builder adds.
