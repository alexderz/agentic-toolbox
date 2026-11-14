---
name: astryx
description: use this when a builder implements or reviews UI code in a product whose package.json depends on an @astryxdesign/* package, or whose approved LLD or mockups name Astryx; or when a designer or architect chooses a component library for a React web UI. it says how to get Astryx facts from the project's own CLI, how to build a page from Astryx templates, which delivery checks to run, and what wins on conflict. it loads beside the one language skill, ui-craft and modern-web-guidance, not in place of them. do not use for backend-only work, non-React UIs, or products that do not use or choose Astryx.
---

# Astryx

Upstream: [meta/astryx](https://github.com/meta/astryx/tree/cb2558efd0bd1e8988b8bf3d47fc1252343858a9)
at `cb2558efd0bd1e8988b8bf3d47fc1252343858a9`, MIT, Copyright (c) 2026
Meta Platforms, Inc. This file is a first-party rewrite in this
repository's words (MIT); no upstream text, plugin, CLI code or agent
block is vendored. Pin and notes: [SOURCES.md](../../SOURCES.md).

**Astryx** is a React design system: components, design tokens, themes,
page and block templates, and a CLI, `@astryxdesign/cli`, that prints
their docs. This skill has no `scripts/`. It runs no command of its own
and uses no network; the commands below are ones you run in the product
repo.

**Actors.** The **builder** implements or reviews UI code with Astryx. The
**designer** and the **architect** consider Astryx when they choose a
component library. The **operator** decides the actions this file marks
as theirs. The **manager** receives rulings and asks.

## Iron law

**Get Astryx facts from the project's own CLI, at the project's version.**
Never write a component name, prop, token, template or command from
memory. Read it from the CLI first.

## When to load

1. **builder:** load this skill when the turn implements or reviews UI
   code in a product repo and either condition holds:
   - the product's `package.json` lists an `@astryxdesign/*` package in
     `dependencies`, `devDependencies` or `peerDependencies`;
   - the product's approved LLD or approved mockups name Astryx.
2. **designer** or **architect:** load this skill when the turn chooses a
   component library for a React web UI.
3. Do not load it for backend, tooling, config, tests-only, docs-only or
   copy-only turns, or for a UI that is not React.
4. This skill is not a language skill. It loads beside the one language
   skill per the [load-with list](../language-router/SKILL.md#load-with-list),
   beside [`ui-craft`](../ui-craft/SKILL.md) and
   [`modern-web-guidance`](../modern-web-guidance/SKILL.md). It replaces
   none of them.

## How to read Astryx facts

**Facts.** The project's CLI is a devDependency, `@astryxdesign/cli`, at
the same version as `@astryxdesign/core`. Find that version in
`package.json` and the lockfile. The CLI documents itself; read its docs,
not the files under `node_modules/@astryxdesign/`.

Pick the runner from the first row that matches:

| Condition in the product repo | Runner |
| --- | --- |
| `package.json` has an `astryx` script | The package manager's run command, such as `npm run astryx -- <args>` |
| `@astryxdesign/cli` is installed as a devDependency | The package manager's exec runner, such as `pnpm exec astryx <args>` or `npx @astryxdesign/cli <args>` |
| `@astryxdesign/core` is installed, the CLI is not | `npx @astryxdesign/cli@<core version> <args>`, for reads only |

- The package manager is the one the lockfile names, per
  [`lang-js-ts`](../lang-js-ts/SKILL.md#tooling--verify).
- Never run the unscoped `npx astryx`: upstream states that it resolves to
  an unrelated npm package. Use a runner from the table.
- Adding the CLI as a devDependency is a dependency change. Follow the
  language skill's dependency rules and the LLD; until then, use the
  third row.
- When a command prints a follow-up command, run it with your runner.

Reads, in the order to try them:

1. `search "<what you need>"` — one ranked list across components, hooks,
   docs, templates and themes, each with its follow-up command. Narrow
   with `--type component|hook|doc|template|theme`.
2. `component <Name>` — props, variants, examples and related block
   templates. `component --list` lists every component.
3. `hook <name>` — one hook's docs.
4. `docs <topic>` — reference docs, such as `docs tokens`, `docs theme`,
   `docs layout`. `docs` alone lists the topics.
5. `template --list`; `template <name>` prints a template's source;
   `template <name> --skeleton` prints its layout skeleton.
6. `build "<idea>"` — the template to start a page from and the parts it
   lacks.
7. `manifest --json` — every command, option and response type of the
   installed version. `<command> --help` gives one command.

Output options: `--json` gives a typed envelope on every command except
bare groups; `--dense` gives compact text for `component` and `docs`;
`--detail brief|compact|full` sets list and docs size.

## Build workflow

1. Read the approved stories and mockups from
   [`ux-design`](../ux-design/SKILL.md), the LLD, and the nearest existing
   screen. They decide what to build.
2. For each new page, run `build "<idea>"`. Note the template it names and
   the parts it lacks.
3. Run `template <name> <path>`, with `<path>` inside the item's scope. It
   writes the template into that file.
4. Keep the template's frame, gap and padding. Replace only its content.
5. For each part the template lacks, run `template <Block>` for a block
   template, then `component <Name>` for each component you use.
6. Read a component's props with `component <Name>` before you write it.
7. For colors, spacing, radius and type, read `docs tokens`; for theming,
   `docs theme`. Use tokens, not literal values.
8. On an existing page, keep its structure and change only what the item
   asks; do not re-scaffold it.

## Delivery checks

Run these before you hand off, in order:

1. Re-read each file you changed.
2. Replace each raw `<div>` or `<span>` that an Astryx component or layout
   covers with that component. Read it with `component <Name>`.
3. Replace each stylesheet import and each `@apply` you added with a
   component prop or a token. The Astryx and theme CSS imports that the
   project's setup requires stay.
4. Replace each hard-coded hex color or px value with a token from
   `docs tokens`.
5. Run the project's build script. Hand off that build and its output, not
   a description of the page. If the build fails, fix it or report the
   failure.
6. Run the [`ui-craft`](../ui-craft/SKILL.md#one-verification-pass) pass
   when the product uses `ui-craft`. Done evidence follows
   [`verify-before-done`](../verify-before-done/SKILL.md).

## What wins on conflict

The earlier item wins. Never rows of every loaded skill and
[`security-hardening`](../security-hardening/SKILL.md#never) apply
throughout; this list orders the rest.

1. **What is built:** the approved mockups and stories (`ux-design`), the
   brief and the LLD. An Astryx template never adds scope.
2. **How it is built:** Astryx components, tokens and templates, read from
   the CLI.
3. **Visual rules where Astryx is silent:** `ui-craft`. Where a `ui-craft`
   rule and an Astryx token or template disagree, the Astryx token or
   template wins. If the product's UI craft note records option 3, skip
   `ui-craft`.
4. **Platform features:** `modern-web-guidance`.
5. **Code:** the one language skill, such as `lang-js-ts`.

If two items conflict, follow the earlier one and name the conflict in
your handoff.

## Commands that change things outside the item

Each row states what the command changes, then what you may do.

| Command | What it changes | Allowed action |
| --- | --- | --- |
| `npm i -g @astryxdesign/cli` | Installs a CLI for the whole computer. It prints update notices and keeps computer-level agent skill files in home-folder agent folders current | Use the project-local CLI. The operator may choose it for their own computer |
| `astryx init --user` | Writes `~/.agents/skills/astryx/SKILL.md` and links or copies it into other agents' skill folders, such as `~/.claude/skills` | Use the project-local CLI. The operator may choose it for their own computer |
| `astryx init`, `astryx init --all`, or `--features` with `agents` | Writes a managed Astryx block into the repo's `AGENTS.md`, `CLAUDE.md` or `.claude/CLAUDE.md`, and an import line into `GEMINI.md`. In a repo governed by this SDLC, those files are agent text | Run `astryx init --features theme,template`. If the product wants the agent block, make it its own reviewed item |
| `astryx gap-report ... --confirm-public` | Files a public GitHub issue with the user's `gh` login: a public post | Ask the operator first per [Asking the operator](../sdlc/SKILL.md#asking-the-human). Without `--confirm-public` nothing is sent; you may prepare the report and put it in the ask, with every destination the output lists |
| `swizzle <Name>`, `upgrade --apply`, `template <name> <path>`, `theme` commands that add, switch or build a theme | Edit or add project files: ejected component source, codemods, scaffolded pages, theme files | Run them only on files inside the item's scope |
| The hosted MCP server, `https://astryx.atmeta.com/mcp` (tools `search`, `get`) | Sends your query to a public remote service | Prefer the local CLI. Send only generic component questions; never private code, names or data |
| The upstream Claude Code or Codex plugin | A marketplace install of agent text this repo has not reviewed | Never marketplace-install it from this skill. Load this skill instead |

## Choosing Astryx at design time

**designer** and **architect:** apply this section; the build workflow
and delivery checks are the builder's. Give these facts in the list of
component-library options; this skill does not recommend Astryx for every
product.

1. **Fit.** Astryx is a candidate when the product UI is React 19 or
   later. `react` and `react-dom` 19 or later are peer dependencies of
   `@astryxdesign/core`.
2. **What it offers.** Over 150 accessible components, page and block
   templates (dashboards, settings, forms, detail pages), design tokens,
   dark mode and brand theming through CSS custom properties, and seven
   ready-made themes. Styles are pre-built CSS imports: no build plugin.
   Consumers may override with `className` using Tailwind, CSS modules or
   plain CSS.
3. **Status.** Astryx is Beta. The chart packages (`@astryxdesign/vega`,
   `@astryxdesign/charts`) are published only under the `@canary` tag, and
   `@astryxdesign/lab` is not published.
4. **Cost.** Adopting it adds npm dependencies: `@astryxdesign/core`, a
   theme package such as `@astryxdesign/theme-neutral`, and
   `@stylexjs/stylex`, plus `@astryxdesign/cli` as a devDependency. Follow
   the product's dependency rules.
5. **Record.** If the product chooses Astryx, the **architect** records
   the choice and the exact version in the product's LLD. That version is
   the one the builder's CLI reads at.
6. **Reading before a project exists.** Use
   `npx @astryxdesign/cli@<version> <read>`, with the version the LLD will
   record. The hosted MCP row above applies to remote questions.
7. **License.** MIT.
