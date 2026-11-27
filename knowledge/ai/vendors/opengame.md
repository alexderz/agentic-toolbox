# OpenGame (`nexu-io/opengame`)

- Source: [`nexu-io/opengame`](https://github.com/nexu-io/opengame) (Apache-2.0, commit `cd98165f15a440a6cb597ea89eb1be4d8edee9a4`), `README.md`, `docs/opengame-setup.md`, `skills/opengame/SKILL.md`, `skills/openmotion/SKILL.md`; discovery post <https://x.com/tuturetom/status/2125885821068972135>.
- Distilled: `2026-11-27`
- Live docs win: [`nexu-io/opengame`](https://github.com/nexu-io/opengame) (`README.md`, `docs/opengame-setup.md`, `shared/game-tools.ts`). Fast-moving repository created 2026-11-25.

## What it is

An Apache-2.0 local browser-game studio and stdio MCP server from OpenDesign (`nexu-io`), built on the OpenMotion stack. It connects local coding agents (BYOA: Claude Code, Codex, Gemini CLI, Cursor, Hermes, DeepSeek Harness, and others) to a single-player HTML5 / Three.js game pipeline: template remixing, re-styling, BYOK multimodal asset generation, deterministic simulation, headless Chromium playtesting, cover capture, and gameplay trailer export.

## When to read

Read this before evaluating or setting up OpenGame for browser-game prototyping, before wiring its stdio MCP server to a local agent, or before proposing its upstream skills for [intake](../../../skills/sdlc/references/intake.md).

## Key facts

- **Templates:** The README highlights 25 featured playable templates (16:9 3D/voxel/anime/pixel/narrative and 9:16 portrait/playable-ad formats). On 2026-11-27 `templates/games/` contained 278 entries; additional template assets are SHA-256 pinned in `templates/game-downloads.json` and fetched on demand from immutable R2 bundles or Git LFS when a title is played or remixed.
- **Prerequisites:** Git, Git LFS, npm, and Node.js 22.18+ (`package.json`; CI pins 26.11.1). Chrome/Chromium is required for screenshots and playtesting; FFmpeg/ffprobe is required for gameplay trailers.
- **Shallow install (avoid bulk LFS pull):** A full bare clone is ~1.04 GB. Upstream recommends cloning with LFS smudge disabled (`git -c filter.lfs.process= -c filter.lfs.smudge= -c filter.lfs.required=false clone --depth 1 --single-branch --branch main https://github.com/nexu-io/opengame.git`), then `git lfs install --local --skip-smudge`, `npm ci --include=optional`, and `npm run build:studio`.
- **Workspace separation:** Set `MOTION_DATA_DIR` outside the repo checkout and pass the exact same absolute path to both Studio (`npm run prepare:account && npm start`, open `<previewUrl>/game`) and the MCP server (`node --experimental-strip-types /abs/path/to/opengame/mcp.ts`). The Studio URL is not an HTTP MCP endpoint.
- **MCP surface:** Local stdio only (no hosted cloud MCP endpoint). Public tool prefix stays `openmotion_game_*` (12 tools, including `openmotion_game_validate` 50-tick smoke test, `openmotion_game_simulate` 3-tier deterministic balance run, `openmotion_game_playtest` headless Chromium across 1–4 clients, `openmotion_game_capture_cover`, `openmotion_game_trailer`, and `openmotion_game_publish`). Specialist workflow MCP resource URIs are `openmotion://workflow/game/start` and `openmotion://workflow/media/start`.
- **Assets and fallbacks:** Model Gateway supports BYOK image, music, voice, and video providers or an OpenDesign account, with zero-key procedural fallbacks (Canvas/SVG sprites, Web Audio SFX/music, procedural Three.js).
- **Upstream skills (not vendored here):** `skills/opengame`, `skills/openmotion-game`, `skills/openmotion-media`, `skills/openmotion-design`, `skills/openmotion-video`, `skills/openmotion`.

## Operational and security cautions

- **Silent 24-hour auto-update by default:** On a clean `main` checkout, creation and generation tool calls (`openmotion_game_create`, `openmotion_create_project`, `openmotion_design_project` create, `openmotion_capability_run`, `openmotion_assets_use`/`openmotion_media_use` generate) check `origin/main` once every 24 hours (`MOTION_DATA_DIR/.update-check.json`), silently pull and rebuild, refresh local copies of installed skills, and restart an idle backend. Set `OPENMOTION_AUTO_UPDATE=0` in the MCP server `env` block to disable automatic updates.
- **Local vs public publishing:** `openmotion_game_publish` publishes only to the local Studio catalog. `openmotion_assets_use` with `action="web_publish"` uploads a static snapshot to OpenDesign Cloud (outward-facing; ask the operator first).
- **Multiplayer scope:** New creation is single-player; static hosting does not deploy multiplayer room servers.

## Unknown

- Build cleanliness, Linux runtime behavior, headless Chromium playtest reliability, and trailer export — not built or executed for this note.
- Security audit of the codebase, npm dependency graph, R2 template download path, and upstream `SKILL.md` bodies — not audited or scanned.
- License status of individual bundled assets or nested license files (for example `skills/openmotion-game/LICENSE-HIGGSFIELD`) beyond the repository's root Apache-2.0 license.

## Do not

- Install upstream skills into this toolbox with `npx skills add`. Third-party skill bodies require security intake per [skills/sdlc/references/intake.md](../../../skills/sdlc/references/intake.md).
- Copy upstream `SKILL.md` bodies, templates, or scripts into this repo.
- Leave `OPENMOTION_AUTO_UPDATE` enabled in pinned or controlled environments.
- Store media-provider API keys, OpenDesign credentials, or `secrets.json` in this repo or in generated game source.
- Remint this note as a skill id.
