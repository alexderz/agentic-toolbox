# OpenCode server note — solo-dlc (DER-421)

How the driver runs OpenCode workers, for the [LLD](lld.md) OpenCode
sections (item 7, the first harness). Written at Spec, 2026-10-18.

- **Pinned:** `opencode-ai` 1.19.3, `@opencode-ai/sdk` 1.19.3, and
  `@opencode-ai/plugin` 1.19.3: npm `latest` on 2026-10-18, published
  2026-10-16. Read from the npm tarballs and the `v1.19.3` source tag,
  without installing or running anything. The [docs](https://opencode.ai/docs/)
  were read from their source at the same tag. Where docs and source
  differ, the source wins and the row says so.
- `S` = `https://github.com/anomalyco/opencode/blob/v1.19.3/packages`;
  `P` = `https://unpkg.com/@opencode-ai/plugin@1.19.3/dist`;
  `K` = `https://unpkg.com/@opencode-ai/sdk@1.19.3/dist`.

## Chosen shape

The driver starts one `opencode run` process per stage and waits for
it to exit. It does not use [`opencode serve`](https://opencode.ai/docs/server/)
or the SDK's `createOpencode`: both open a TCP listener, and
`createOpencode` only spawns `opencode serve` on a fixed default port
with `OPENCODE_CONFIG_CONTENT`. `opencode run` without `--attach`
serves its own client in process and opens no listener.

```text
<harness.bin> run --format json [--session <id>] --agent <label>
  --model <provider/model> --title "<label> <run>" --dir <cwd>
  < RUN_ROOT/<persona>/run-N/prompt.md
```

| Variable | Value | Why |
| --- | --- | --- |
| `OPENCODE_DB` | `RUN_ROOT/<persona>/opencode.db` | One session database per persona: the persona's session file |
| `OPENCODE_CONFIG_CONTENT` | The worker config the driver builds per stage | Agent, permissions, plugin, providers |
| `XDG_CONFIG_HOME` | `RUN_ROOT/driver/opencode/xdg-config`, holding only an empty `opencode/` folder with mode `0500` | The operator's global OpenCode config, plugins, tools, agents, MCP servers, and `AGENTS.md` do not load. OpenCode creates `opencode/` at start-up, so the driver creates it first; unwritable, it also stops OpenCode's background `npm` install there |
| `OPENCODE_DISABLE_PROJECT_CONFIG`, `OPENCODE_DISABLE_CLAUDE_CODE` | `1` | No `opencode.json`, `.opencode/`, `AGENTS.md`, `CLAUDE.md`, or `.claude/` from the cwd or home |
| `OPENCODE_DISABLE_AUTOUPDATE`, `OPENCODE_DISABLE_MODELS_FETCH`, `OPENCODE_DISABLE_LSP_DOWNLOAD` | `1` | No self-update of the pinned binary; no start-up downloads |

The worker config sets `autoupdate: false`, `share: "disabled"`,
`snapshot: false`, `lsp: false`, `formatter: false`, one `plugin`
entry (`file://` URL of the hashed worker plugin copy), the providers
from `run.json`, `agent.title.disable: true`, and one agent per stage:
the persona label, `mode: "primary"`, its model, and its permission
rules ([Tools](#tools-per-persona)).

**Session.** A mint omits `--session`: `run.ts` calls `session.create`
with no `parentID`, which starts a root session with an empty
transcript. Every JSON line carries `sessionID`; the adapter records it
from the first line. A resume passes `--session <id>`: `run.ts` calls
`session.get`, and a missing id prints `Session not found` and exits
`1`, so OpenCode never resumes into a blank session. Before each resume
the adapter also checks that the database exists and that
`opencode session list --format json`, run with the same environment,
lists that id.

**Prompt and wait.** `run.ts` joins piped stdin into the message, sends
it with `session.prompt`, prints one JSON event per line (`step_start`,
`tool_use`, `text`, `step_finish`, `error`), and exits when the session
goes idle. It exits `1` on a `session.error` or a failed request. It
rejects every permission ask that no rule allows, unless `--auto` is
passed; the adapter never passes it.

**One worker at a time.** The driver runs one `opencode run` at a time.
`task: "deny"` removes the sub-agent tool. `--title` and the disabled
`title` agent stop the first-message title call, the only parallel
model call the prompt loop makes; compaction runs inline.

### Tools per persona

Permission rules are the tool allowlist. A rule with pattern `*` and
action `deny` removes the tool from the model's tool list, and the
last matching rule wins. `edit` covers `edit`, `write`, and
`apply_patch`. The worker agent's rules:

| Neutral name (persona `tools`) | OpenCode permission |
| --- | --- |
| — | `"*": "deny"` first; also denies `task`, `webfetch`, `websearch`, `skill`, `todowrite`, `question` |
| `read`, `bash`, `grep` | `read`, `bash`, `grep`: `allow` |
| `find`, `ls` | `glob`: `allow` (1.19.3 registers no `list` tool) |
| `edit`, `write` | `edit`: `allow`; read-only personas get no rule, so the `*` deny removes all three edit tools |
| run-folder tools | `sdlc_write`, `sdlc_result`: `allow` |
| — | `external_directory`: `allow` for the run root, the system temporary folder, and the compiled files folder `<checkout>/.sdlc/compiled/*` (the rules match folder globs; O-T10 checks whether a single file path matches in `tool/external-directory.ts`), `deny` elsewhere |

### Worker plugin hooks

| Hook | Use |
| --- | --- |
| Plugin init | Parse `SDLC_*`, check the facts hash, write `logs/ext.json`. A plugin that fails to load is logged and skipped, so the driver's marker check fails the stage |
| `tool` | `sdlc_write` and `sdlc_result`. Args may be plain JSON Schema, so the plugin imports nothing but Node built-ins; then every property is required and the host does not validate args, so each tool validates its own |
| `tool.execute.before` | Path guard. It runs before the tool executes; a throw rejects the call. It checks `filePath` for `write` and `edit`, and every `*** Add File:`, `*** Update File:`, `*** Delete File:`, and `*** Move to:` path in `apply_patch`'s `patchText` |
| `chat.message` | Records the agent name in `logs/ext.json`, so the marker shows which agent ran |
| `experimental.session.compacting` | Sets `output.prompt`: return the deterministic summary verbatim |
| `experimental.chat.messages.transform` | Runs on every model request. Replaces the text of each `summary: true` message with the deterministic summary: persona header, `state.md`, driver facts |
| `experimental.chat.system.transform` | Appends the driver-facts block to every request's system prompt |
| `shell.env` | Sets `output.env.XDG_CONFIG_HOME` back to the operator's value for `bash`, so `git` reads the operator's config. A returned object is ignored |

**Compaction differs from Pi.** OpenCode has no hook that supplies the
summary. The hidden `compaction` agent writes it in a model call with
no tools. The hook can only replace that agent's prompt. The
`messages.transform` replacement makes every later request carry the
deterministic summary, whatever the stored summary says. Compaction
fires when tokens reach `usable()` in `session/overflow.ts`: when the
model sets `limit.input`, `usable()` is `limit.input -
compaction.reserved`; otherwise it is `limit.context -
maxOutputTokens`, and `compaction.reserved` is ignored.
`compaction.auto: false` turns it off.

**Structured output.** The HTTP prompt body accepts `format:
{type: "json_schema", schema}`: OpenCode forces a `StructuredOutput`
tool and returns the value in the assistant message's `structured`
field. `opencode run` does not expose it, so it is the O-T6 fallback.

### `/sdlc` in the operator's OpenCode

- **Command.** A TUI plugin (default export `{id, tui}`, listed in the
  operator's `tui.json`) registers
  `api.keymap.registerLayer({commands: [{name: "sdlc.run",
  slashName: "sdlc", namespace: "palette", run}]})`, as the built-in
  diff viewer does. Picking `/sdlc` from the autocomplete or the palette
  calls `run()` in the TUI process: no model turn. The command takes no
  argument; `run()` asks for the run root in `api.ui.DialogPrompt`.
- **Typed text.** Text such as `/sdlc RUN_ROOT` that the autocomplete
  does not pick is sent to the model as a prompt. A server command named
  `sdlc` would also run a model turn, so none exists. A server plugin
  in the operator's session throws in `chat.message` for text that
  starts with `/sdlc`, and for any prompt while a driver holds the
  lock. The throw fails the prompt before the message is saved and
  before any model call.
- **Headless.** `opencode run` loads no TUI plugin, so nothing headless
  can start the driver.
- **Listener.** The 1.19.3 TUI opens its server listener only with
  `--port`, `--hostname`, or `--mdns`; otherwise it talks to the
  server in process. The [server docs](https://opencode.ai/docs/server/)
  say the TUI picks a random port; the source wins. `/sdlc` refuses when
  the TUI was started with one of those flags.

## Facts read in 1.19.3

| Fact | Source |
| --- | --- |
| `opencode run`: no listener without `--attach`; stdin joined into the message; `--session` missing → `Session not found`, exit `1`; mint calls `session.create` without `parentID`; JSON lines carry `sessionID`; exit `1` on `session.error`; asks rejected unless `--auto`; `question`, `plan_enter`, `plan_exit` denied; `--port` unused | `S/opencode/src/cli/cmd/run.ts` |
| `--agent` naming a missing agent, or a sub-agent, warns and falls back to the default agent | `S/opencode/src/cli/cmd/run.ts` |
| `session.create` body `{parentID?, title?, agent?, model?, permission?}`; prompt body `{agent?, model?, system?, tools?, format?, parts}`; `session.get` 404 when missing | `K/v2/gen/types.gen.d.ts` |
| `createOpencode` spawns `opencode serve` on loopback with `OPENCODE_CONFIG_CONTENT` | `K/v2/server.js` |
| `OPENCODE_DB` sets the database path; absolute paths are used as is | `S/core/src/database/database.ts`, `S/core/src/flag/flag.ts` |
| Config layers: well-known remote config from `auth.json`, global config dir, `OPENCODE_CONFIG`, project files, `.opencode/` folders (project ones skipped, `~/.opencode/` always read), `OPENCODE_CONFIG_DIR`, `OPENCODE_CONFIG_CONTENT`, account organization config, `/etc/opencode/` | `S/opencode/src/config/config.ts`, `config/paths.ts`, `config/managed.ts` |
| The data, config, and state folders are created at start-up; an unwritable config folder skips the `npm` install and `.gitignore` write | `S/core/src/global.ts`, `S/core/src/npm.ts`, `S/opencode/src/config/config.ts` |
| Instructions: global `AGENTS.md`, `~/.claude/CLAUDE.md`, project `AGENTS.md`/`CLAUDE.md`; project files skipped with `OPENCODE_DISABLE_PROJECT_CONFIG` | `S/opencode/src/session/instruction.ts` |
| Built-in tool ids; `apply_patch` replaces `edit` and `write` for `gpt-` models | `S/opencode/src/tool/registry.ts` |
| Every `{tool,tools}/*.{js,ts}` file in each config folder, `~/.opencode/` and `/etc/opencode/` included, is imported as a tool; `debug config` does not list these tools | `S/opencode/src/tool/registry.ts`, `config/config.ts` |
| `deny` with pattern `*` removes a tool; `edit` covers three tools; last match wins; agent `tools` is deprecated for `permission` | `S/opencode/src/permission/index.ts`, `session/llm/request.ts`, `S/core/src/v1/config/agent.ts` |
| `external_directory` asks for paths outside the project in `read`, `write`, `edit`, `apply_patch`, and `bash` | `S/opencode/src/tool/external-directory.ts`, `tool/shell.ts` |
| `tool.execute.before` runs before execute; a throw rejects the call | `S/opencode/src/session/tools.ts`, `plugin/index.ts`; [Plugins](https://opencode.ai/docs/plugins/) |
| Plugin tools accept JSON Schema args; a plugin tool overrides a built-in of the same name | `S/opencode/src/tool/registry.ts`; [Plugins](https://opencode.ai/docs/plugins/) |
| A plugin that fails to load is logged and skipped | `S/opencode/src/plugin/index.ts` |
| Compaction: model-written by the `compaction` agent; `session.compacting` changes only the prompt; trigger at `usable()`: `limit.input - compaction.reserved` when `limit.input` is set, else `limit.context - maxOutputTokens` with `reserved` ignored; `compaction.auto` | `S/opencode/src/session/compaction.ts`, `session/overflow.ts`, `P/index.d.ts` |
| `messages.transform` runs on each model request before conversion; `system.transform` on each request | `S/opencode/src/session/prompt.ts`, `session/llm/request.ts` |
| `chat.message` runs before the user message is saved | `S/opencode/src/session/prompt.ts` |
| `shell.env` gets `{env}` as its output object; the hook mutates `output.env`, which is spread over `process.env` for `bash`; its return value is not read | `S/opencode/src/tool/shell.ts` |
| Structured output through `format`, forced tool, `structured` field | `S/opencode/src/session/prompt.ts` |
| Title call skipped when the title is set or the `title` agent is disabled | `S/opencode/src/session/prompt.ts`, `agent/agent.ts` |
| TUI slash commands from plugins; typed text goes to `session.command` only for a server command, else to `session.prompt` | `S/tui/src/keymap.tsx`, `tui/src/component/prompt/index.tsx`, `tui/src/feature-plugins/system/diff-viewer.tsx`, `P/tui.d.ts` |
| TUI listener only with network flags | `S/opencode/src/cli/cmd/tui.ts`, `cli/tui/worker.ts` |
| The `opencode-ai` package copies a platform binary into `bin/` at `postinstall` | `opencode-ai@1.19.3` tarball, `postinstall.mjs` |
| Provider SDKs such as `@ai-sdk/openai-compatible` are bundled in the binary (`BUNDLED_PROVIDERS`) | `S/opencode/src/provider/provider.ts` |

## Trial checks

Not run. Item 7 runs these first, on the operator's machine with one
local model, before any other acceptance test. Each failure switches to
its fallback.

| Check | Prove | Fallback if disproved |
| --- | --- | --- |
| O-T1 Headless worker | Mint, then three resumed passes keep context; a missing id exits `1`; a model error exits `1`; no TCP listener while it runs | `opencode serve` on loopback with a random port and a per-stage `OPENCODE_SERVER_PASSWORD`, driven over HTTP with `fetch`, killed after the stage. Adds a listener that a worker's `bash` can reach: a new trust-boundary row for **security** |
| O-T2 Isolation | With the worker environment, `opencode debug config` shows only the driver's plugin, agent, permissions, and providers, with no MCP server and no instructions | None needed: the adapter runs the same compare before every spawn and stops on a difference (`check failed: harness-config`) |
| O-T3 `bash` config | `shell.env` setting `output.env.XDG_CONFIG_HOME` restores it; `git` in a worker uses the operator's settings | Set `GIT_CONFIG_GLOBAL` to the operator's global git config file in the worker environment |
| O-T4 Write controls | No edit tool for read-only personas; the guard blocks writes outside the writable set, through a symbolic link, inside `.git`, and when it throws, for `write`, `edit`, and `apply_patch`; `sdlc_write` stays in the run folder | Pi's T6 fallback: permissions alone, detection for the rest, reported to **security** |
| O-T5 Compaction | With the limit that `usable()` reads made small (`limit.input` when the trial model's provider entry sets it, else `limit.context`), compaction fires under `opencode run` at `usable()`; the next request carries the deterministic summary; a fact removed from `state.md` stays in the facts block | `compaction.auto: false`, and an `operator` stop when the session nears `usable()` for a `rehydrate` mint, as in Pi's T4 fallback |
| O-T6 Results | Ten runs of a fixed task; count valid candidates first time and after one repair | `format: json_schema` through the O-T1 fallback shape; below 8 of 10, ask the operator for another model |
| O-T7 `/sdlc` | The TUI command runs with no model turn; `DialogPrompt`, `DialogSelect`, and `DialogConfirm` work when called as functions without JSX; the detached driver starts under `harness.node`; the TUI stays usable; toasts show `STOP` and ask lines | A terminal command, `node packages/opencode-sdlc/src/cli.ts RUN_ROOT`, with the same steps on its own terminal: still no model, outside OpenCode |
| O-T8 Input guard | A `chat.message` throw stops a prompt with no model call while the lock is held, and stops typed `/sdlc` text; the operator sees the reason | A toast only: the operator's own session can start a model call while a worker runs. Operator question O11 in the LLD |
| O-T9 Agent | The marker names the persona's agent | None needed: a wrong agent fails the marker check, an `operator` stop |
| O-T10 Paths | The `external_directory` rules let the `local` tracker recipes, `git` reads, and a `read` of the compiled file in the operator checkout run | `external_directory: allow`: Pi's posture, writes outside are detected only |
