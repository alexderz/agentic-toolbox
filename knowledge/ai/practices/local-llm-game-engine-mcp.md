# Driving game and 3D engines over MCP with local models

- Source: Unsloth documentation [Blender, Unreal Engine, Unity, Godot, Roblox with Local Models](https://unsloth.ai/docs/basics/mcp/mcp-engines) and [How to Use MCP Servers with Local LLMs](https://unsloth.ai/docs/basics/mcp); discovery post <https://x.com/UnslothAI/status/2126322382239649959>; GitHub API metadata for referenced community MCP repositories verified 2026-11-27.
- Distilled: `2026-11-27`
- Live docs win: <https://unsloth.ai/docs/basics/mcp/mcp-engines> and each engine's official MCP documentation or GitHub repository.

## What it is

A setup reference and operating map for connecting local tool-calling LLMs (demonstrated by Unsloth with local GGUF quants such as `Qwen3.8-27B` `UD-Q4_K_XL`, `Qwen3.8-Flash-Next`, and `Inkling 2 Mini`) to Blender, Unity, Unreal Engine, Godot, Figma, and Roblox Studio over local MCP servers.

## When to read

Read this before wiring a local model or MCP host to a 3D/game engine or design editor, before choosing between built-in and community MCP plugins, or before running those editors headless on Linux.

## Engine setup matrix

| Engine | MCP server / plugin | Default port | Headless Linux / key notes |
| --- | --- | --- | --- |
| **Blender 5.1+** | Official [Blender Lab MCP add-on](https://www.blender.org/lab/mcp-server/) | `9876` | Enable Online Access in Preferences → System; drag install button twice (repo, then add-on). Headless: `xvfb-run -a ./blender` (**bridge does not start with `blender -b`**) |
| **Unity 2021.3+** | [`CoplayDev/unity-mcp`](https://github.com/CoplayDev/unity-mcp) (MIT, HEAD `19b66ecef4ac3a9be22a7a62ea21accb975c39e7`) | `8080` (HTTP) | Install via Package Manager git URL `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#main`; requires `uv`. Amber = server up without an editor joined; green = connected |
| **Unreal Engine 5.8+** | Epic's built-in [Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) plugin; community alternative EngineWire [`ChiR24/Unreal_mcp`](https://github.com/ChiR24/Unreal_mcp) (MIT, HEAD `29a0ae03816eec26f4d993564261f79cd61c5d98`) | `8000` (official) / `3000` (EngineWire) | Official plugin: enable `Unreal MCP` and `All Toolsets` in Edit → Plugins, then enable `Auto Start Server` in Editor Preferences → General → Model Context Protocol. Headless: `Engine/Binaries/Linux/UnrealEditor MyProject.uproject -RenderOffscreen -ModelContextProtocolStartServer` |
| **Godot 4.5+** | [`yurineko73/Godot-MCP-Native`](https://github.com/yurineko73/Godot-MCP-Native) (MIT, HEAD `eef4807190e7765e69d59c9e707d0ba170f6770d`) | `9080` (HTTP) | Install from AssetLib / Asset Store, enable in Project Settings → Plugins, start HTTP server in the editor's MCP tab. Headless: `godot --headless --editor --path /path/to/project -- --mcp-server` |
| **Figma** (Windows, macOS) | Built-in desktop MCP server (Dev or Full seat) | `3845` | With nothing selected, enter Dev Mode → Enable desktop MCP server. **Read-only** (inspects frames, styles, assets; does not mutate) |
| **Roblox Studio** (Windows, macOS) | Built-in [Studio MCP](https://create.roblox.com/docs/studio/mcp) launcher | none | Enable via Assistant → … → Manage MCP Servers → Enable Studio as MCP server |

## Prompting and workflow notes

- **Keep the engine open on the same host** as the MCP client.
- **Iterate one visible change at a time** and inspect a render or Game view screenshot between turns before applying the next edit.
- **Name toolsets explicitly** when an editor exposes large tool catalogs (for example `SceneTools`, `PrimitiveTools`, and `MaterialInstanceTools` in Unreal Engine) so smaller local models select tools reliably.
- **Multi-step builds:** Raise the client's max tool calls per message limit; if a run stops partway through, ask the model to inspect current scene state and continue.

## Security boundary

- Engine MCP servers execute code inside the desktop application. Unsloth restricts engine MCP tools to the owner account and disables them when Remote access or LAN access is enabled.
- Exposing stdio MCP through a remote/public link requires opting in (`UNSLOTH_STUDIO_ALLOW_STDIO_MCP=1` in Unsloth); treat that as a trust-boundary expansion and require explicit operator approval.

## Unknown

- End-to-end tool-calling reliability and scene quality across other local models, quants, or non-Unsloth MCP clients — not benchmarked for this note.
- Security audit of the three community MCP repositories (`CoplayDev/unity-mcp`, `ChiR24/Unreal_mcp`, `yurineko73/Godot-MCP-Native`) — not audited.
- Compatibility with engine versions older than the minimums listed above.

## Do not

- Bind or expose engine MCP ports (`9876`, `8080`, `8000`, `3000`, `9080`, `3845`) to untrusted networks or enable remote stdio MCP without explicit operator approval.
- Vendor third-party MCP server code or marketplace-install skills into this repo.
- Store credentials or host-specific endpoints in this note.
- Remint this note as a skill id.
