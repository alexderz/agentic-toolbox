# DER-290 security intake: pbakaus/impeccable

Reader: **security**. Method: `docs/INTAKE.md`, a manual read of a fresh clone. I ran nothing from the repo and did no scanner run. The clone was deleted afterwards.

## 1. Pin, license, version
- SHA: `9d715cc4f5564a990ca8345abfdd5df6dc9b41c8` (2026-09-24, PR #855).
- License: `LICENSE` is Apache-2.0. `NOTICE.md` says `skill/reference/ios.md` and `android.md` are distilled from ehmo/platform-design-skills (MIT).
- Skill v4.4.0 (`.claude-plugin/*.json`, `plugin/.claude-plugin/plugin.json`, and generated SKILL.md frontmatter). Engine v0.1.6 (`ENGINE_VERSION`, `skill/scripts/VERSION`). The root `package.json` still says 4.1.0, which is stale and does not matter here.

## 2. Skill surface inventory
- **Source of truth.** `skill/SKILL.src.md` (89 lines, a template with `{{scripts_path}}` placeholders), `skill/reference/*.md` (38 files, about 6.4k lines), `skill/agents/*.md` (4 subagents) and `skill/scripts/`.
- **Generated copies** with filled placeholders, 22 of them: `.claude/`, `.agents/`, `.agent/`, `.cursor/`, `.gemini/`, `.github/`, `.codex`, `.grok/`, `.kiro/`, `.opencode/`, `.pi/`, `.qoder/`, `.rovodev/`, `.trae/`, `.trae-cn/`, `.vibe/`, `.veto/`, `.hermes/`, `.dsh/`, `plugin/` and `cursor-plugin/`, each under `skills/impeccable/`.
- **Scripts** in `skill/scripts/`:
  - `impeccable`: POSIX launcher.
  - `impeccable.cmd`: Windows launcher.
  - `live-browser*.js`: about 560 KB injected into user pages.
  - `modern-screenshot.umd.js`: a vendored third-party bundle.
  - `command-metadata.json`, and `data/font-index*.json`.
- **Binaries.** None are committed. The launcher uses a sibling `bin/<os>-<arch>/` if present. Otherwise it tries `~/.impeccable/bin/impeccable`, then `~/.impeccable/bin/0.1.6/impeccable`, then `impeccable` on PATH. If all of those fail, it downloads from `github.com/pbakaus/impeccable/releases/download/engine-v0.1.6/impeccable-<os>-<arch>`. The download is checked against a `.sha256` sidecar from the same origin. That is an integrity check, not a signature. The engine source is in the Rust crates under `crates/`.
- **npm path.** `package.json` `bin` points to `cli/bin/cli.js`. Its `optionalDependencies` are `@impeccable/cli-<os>-<arch>@0.1.6`, with a fallback download to the same cache.
- **Hooks and settings writers.**
  - The repo ships these hook manifests: root `.claude/settings.json` (SessionStart, PostToolUse Edit|Write, Stop), `.codex/hooks.json`, `.cursor/hooks.json`, `.gemini/settings.json`, `.github/hooks/impeccable.json`, `plugin/hooks/hooks.json` and `cursor-plugin/hooks/hooks.json` (preToolUse).
  - The installer writes project manifests listed in `crates/skills/src/hook_manifest.rs:35-38` and `reference/hooks.md`.
- **Network calls:**
  - Engine download: see above.
  - Skill bundle: `impeccable.style/api/download/bundle/universal` (`crates/skills/src/bundle.rs:322`, `providers.rs:8`), with a signature check in `bundle_signature.rs`.
  - Update check: `GET impeccable.style/api/version`, at most once every 24 h (`crates/context/src/context_cli.rs:470-546`).
  - Concept roll: `GET impeccable.style/api/roll`. Telemetry: `POST impeccable.style/api/chosen` (`crates/context/src/concept_seed.rs:66-154`). Card images come from `impeccable.style/worlds/cards`.
  - OpenAI: `POST api.openai.com/v1/images/generations` and `/images/edits`, using the user's `OPENAI_API_KEY`, with multipart reference images (`crates/context/src/generate_image.rs:249` onward).
  - Google Fonts is referenced by `crates/comp-verbs/src/build_phase.rs:1025` and `foundation/src/fonts.rs`.
- **Live mode.** A helper HTTP server binds `127.0.0.1` on port 8400 or the next free one, with a token and a host check (`crates/live/src/live_server.rs:278-556`). `serve-question` also binds `127.0.0.1`. There is no `0.0.0.0` bind. The engine starts a Chromium browser through CDP (`crates/browser/`), runs `open` or `xdg-open`, and runs `git` in the project.
- **Install and update.**
  - `impeccable install|link|update` (`crates/skills/src/commands.rs:22-56`) writes skill directories at project or user scope, installs engine binaries and installs hooks.
  - **Hook consent defaults to yes when stdin is not a TTY**, which is the case under an agent (`commands.rs:437-457`).
- **Auto-update.** It does not update itself silently. `context` injects an `UPDATE_AVAILABLE` nudge toward `npx impeccable update`. Opt-outs: `IMPECCABLE_NO_UPDATE_CHECK`, or `updateCheck:false` in `.impeccable/config*.json`.

## 3. Injection-shaped text (instructions that bypass our gates)
1. **`SKILL.md`** (`skill/SKILL.src.md` and all 22 copies):
   - The frontmatter `allowed-tools` pre-approves `Bash(npx impeccable *)` and the launcher.
   - Setup step 1 has the agent run the launcher every session, and the launcher fetches the binary on its first run.
   - The preamble claims it "gives you the tools and permission".
   - It also carries the pin, hooks and doctor verbs.
2. **Runtime directives from the downloaded binary.** These are not in any file an intake reads, and they change whenever the binary changes.
   - `AUTONOMY_DIRECTIVE_CHECK` (`context_cli.rs:186-193`) tells the agent to discount system-prompt claims as a "harness default injected".
   - `SUBAGENT_AUTHORIZATION` (`:196-203`) treats invoking the skill as consent to spawn subagents "without re-asking".
   - `UPDATE_AVAILABLE` (`:491`).
   - `TELEMETRY` (`seed_text.rs:40`) tells the agent to rerun the script so it sends the ping.
3. **`reference/hooks.md`.** `hooks on` installs hooks into `.claude/settings.local.json`, `.codex/hooks.json`, `.cursor/hooks.json`, `.gemini/settings.json` (merged, with a `.bak`) and the committed `.github/hooks/impeccable.json`. The agent may also persist detector ignores itself.
4. **`reference/live.md`.**
   - Line 10: the agent asks for an escalated Codex sandbox from the start.
   - It starts the helper server and dev servers and installs dependencies.
   - Line 307: "Do not ask what to do".
5. **`reference/live-setup.md`.** Patches the project's CSP config (Next, SvelteKit, Nuxt) to allow `localhost:8400`.
6. **`reference/new-work.md`.**
   - Line 48 makes `concept-seed` mandatory ("No substitute, no skip"). That command makes the network roll and sends telemetry.
   - Line 57 downloads card images into the workspace.
   - Lines 41 and 115 send screenshots and crops of the user's UI to OpenAI through `generate-image`.
   - It spawns the finish-reviewer and documenter subagents.
7. **`reference/critique.md:36`.** Parallel subagents are "the default and is mandatory". It also injects an overlay into the page.
8. **`reference/generate.md` and `reference/routing.md:22`.** They drive the browser, run `live-generate`, and auto-run `detect` on a bare invocation.
9. **`reference/init.md`, `reference/doctor.md` and `reference/polish.md`.** They write under `.impeccable/` and call `critique-storage`.
10. **`agents/impeccable-asset-producer.md`** uses the OpenAI fallback. **`agents/impeccable-manual-edit-applier.md`** applies edits that come from the browser page and says "Do not ask". Content on the page becomes agent instructions.
11. **`reference/audit.md`.** It is written as a prompt, but the only thing it tells the agent to execute is "Run the bundled detector" (§5). Everything else is a 5×0-4 scoring checklist with `{{placeholders}}`. It has **no gate bypass beyond the engine call**.
12. **Root hook manifests** (§2). If you open an upstream clone in Claude Code, Cursor or Codex, SessionStart runs the launcher, which can download and run the binary.

## 4. What option 1 (text-only rewrite) may draw from
**Allowed: topics only, in our words, with no copied text.**
- Anti-patterns: `reference/craft-floor.md` (0 commands, 0 URLs), `quieter.md` and `distill.md`.
- Typography: `typeset.md`.
- Color: `colorize.md`, plus the color-strategy idea in `new-work.md`.
- Layout: `layout.md` and `adapt.md`.
- Motion: `animate.md`, including the reduced-motion rule.
- UI states: `harden.md`, `onboard.md`, `clarify.md` and the states list in `polish.md`.
- "The brief wins", and refinement versus redesign (`SKILL.src.md` "How to design").
- One bounded verification pass: build, inspect once, batch the fixes, confirm at most once, stop.
- Optionally, the `audit.md` rubric dimensions as a read-only checklist.

**Leave out:**
- The launcher, `allowed-tools`, and every `impeccable <verb>` (about 40 verbs).
- `npx`, install, update, pin and doctor.
- Hooks and any settings writes.
- Live mode, CSP patching, the helper server and browser driving.
- `concept-seed`, the roll, the card catalog and telemetry.
- `generate-image` and anything else that sends data to OpenAI.
- The 4 shipped subagents and the "mandatory subagents" rule.
- The `AUTONOMY` and `SUBAGENT` directives.
- The `.impeccable/` config tree, and writing or persisting `PRODUCT.md`/`DESIGN.md` workflows.
- The comp and plate pipeline.
- `scripts/` and any vendored JS.
- `ios.md` and `android.md`: these are MIT third-party derived. Omit them, or attribute ehmo separately.
- The "permission"/"go all out" preamble and the model-specific "rendition prior" prose.

## 5. Option 2 (the user runs upstream directly, at their own risk): what happens on the machine
- **Installation writes skill files** into project dirs (`.claude/skills/impeccable/`, `.agents/`, `.cursor/` and others) or into the same dirs under `$HOME`. It **installs hooks without a prompt when run non-interactively**: `.claude/settings.local.json`, `.codex/hooks.json`, `.cursor/hooks.json`, `.gemini/settings.json`, `.github/hooks/impeccable.json` and `.grok/hooks/impeccable.json`. It records consent in `.impeccable/config.local.json`.
- **Binary download.** It downloads and runs a native binary into `~/.impeccable/bin/0.1.6/` from GitHub Releases, verified only against a sidecar hash from the same place. `IMPECCABLE_DOWNLOAD_BASE` can redirect the download, and `IMPECCABLE_BIN` can replace the binary.
- **Hooks run the binary on every agent Edit/Write, and at session start and stop.** They inject reminders into the agent's context, and in Cursor they can deny writes.
- **Network at each session:** a version check to `impeccable.style/api/version` every 24 h, cached in `~/.impeccable/update-check.json`. Opt out with `IMPECCABLE_NO_UPDATE_CHECK=1`.
- **Network for new designs.**
  - A roll request to `impeccable.style/api/roll` and a telemetry POST to `/api/chosen` (card id, key, scope, mode, kind). Opt out with `IMPECCABLE_NO_TELEMETRY=1` or `DO_NOT_TRACK=1`.
  - Card images are fetched from `impeccable.style`.
- **OpenAI.** If `OPENAI_API_KEY` is set, prompts plus screenshots and crops of the user's UI go to `api.openai.com`, billed to that key.
- **Live mode:**
  - A localhost server on port 8400 or higher.
  - JS injected into the user's pages.
  - Proposed CSP edits to framework config.
  - Dev servers started and dependency installs.
  - The browser opened, and a local Chromium launched through CDP.
- **Project files written:** `.impeccable/` (config, critique, mocks), `PRODUCT.md`, `DESIGN.md` and a sidecar, and source edits.
- **Runtime agent directives** that override harness gates on subagents and autonomy (§3.2).

## 6. Verdict
**CLEAR to proceed with option 1 at `9d715cc4f5564a990ca8345abfdd5df6dc9b41c8`**, on these conditions:
1. Write the SOURCES row first: full SHA, Apache-2.0, "topic-only rewrite; no scripts, agents, references or hooks vendored". Attribute Impeccable (Apache-2.0) in the skill.
2. Step 3 needs a scanner run or a recorded maintainer waiver, as for pr-lens. This read does not replace it.
3. The rewrite is at most 250 lines, in our own words, and read-only in tools. It has no `allowed-tools`, no commands, no network, no subagents, and nothing from the §4 leave-out list.
4. Omit `ios.md`/`android.md` content, or carry the MIT attribution.
5. Any upstream link targets the pinned SHA, never `main` or latest. The option-2 pointer is a link plus the §5 disclosure. It carries no runnable install command (`npx`, curl) that our skill endorses.
6. Never open an upstream clone in an agent harness, because its root hook manifests run on SessionStart.
7. No auto-update. A new pin needs a new **security** read.
8. **security** re-reads the PR diff against this list, with particular attention to the option-2 disclosure wording.
