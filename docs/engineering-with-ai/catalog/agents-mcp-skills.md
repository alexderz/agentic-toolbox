# Agents, MCP servers, and skills

Snapshot 2026-11-06. Counts are `SKILL.md` files on the default branch
tree unless a row says otherwise. Bodies were read only where a catalog
page says so.

## Harnesses named by the sources

These clients appear in official setup pages. None was configured here.

| Client | Where it is named | What that page uses it for |
| --- | --- | --- |
| Claude Desktop | Fusion help, FreeCAD MCP README | MCP client for a local CAD server |
| Claude Code | Onshape tech tip, JITX skills README, text-to-cad README | Terminal client that adds an HTTP or stdio MCP server, or loads a plugin |
| Cursor | Fusion blog (`http://127.0.0.1:27182`), text-to-cad README | Editor MCP client |
| Codex | JITX skills README, kicad-mcp-pro file tree (`.codex` example named on the repo page) | Plugin or MCP client |
| VS Code / Copilot | Fusion help for the cloud data MCP, kicad-mcp-pro example | Streamable HTTP or workspace MCP |
| OpenCode | kicad-mcp-pro tree has `.opencode/skills/` | Skill files plus an example MCP config |
| Gemini CLI | kicad-mcp-pro tree under `integrations/gemini-cli/` | Copied skills |
| LM Studio | blwfish FreeCAD MCP README | Author smoke test of MCP with named local models |

A harness in this table does not contain a geometry kernel. It hosts
the tool-driver loop.

## Skill packs with a tree count

| Pack | URL | `SKILL.md` count | License | `pushed_at` | Stars | Domain named by paths or README |
| --- | --- | --- | --- | --- | --- | --- |
| text-to-cad | <https://github.com/earthtojake/text-to-cad> | 12 | MIT | 2026-11-05 | 25,621 | CAD, DFM, drawings, G-code, URDF, SRDF, SDF |
| SolidCraft | <https://github.com/tangency-labs/solidcraft> | 17 | Apache-2.0 | 2026-11-06 | 14,178 | MCP tools and STEP/3MF/STL/OBJ/URDF exports are in `docs/mcp.md`. Bundled names: modeling, mechanisms, editing, checking |
| JITX skills | <https://github.com/JITx-Inc/jitx-skills> | 11 | Proprietary file | 2026-11-05 | 20 | Components, circuits, layout, mechanical |
| kicad-mcp-pro | <https://github.com/oaslananka/kicad-mcp-pro> | 39 files, 7 names under `skills/` | MIT | 2026-11-06 | 182 | Schematic, PCB, DRC, fabrication |
| mcp-server-kicad | <https://github.com/ProductOfAmerica/mcp-server-kicad> | 6 | GPL-3.0 | 2026-11-05 | 16 | KiCad tool use. Maintenance mode in the repo description |
| Konnect | <https://github.com/mixelpixx/Konnect> | 6 | AGPL-3.0 | 2026-11-02 | 1,453 | KiCad 10, repository archived |
| skidl-skills | <https://github.com/nickkraakman/skidl-skills> | 4 | MIT | 2026-04-08 | 24 | SKiDL to KiCad |
| flowful-ai/cad-skill | <https://github.com/flowful-ai/cad-skill> | 1 | SPDX `NOASSERTION` | 2026-10-25 | 715 | Description: CadQuery skill for printable STL |
| 3DCodeVerse | <https://github.com/gaoypeng/3dcodeverse> | 20 | Apache-2.0 | 2026-11-04 | 363 | Description: official codebase. One path seen in search: `c3d-cadquery-forms` |
| ai-cad | <https://github.com/ai-cad-labs/ai-cad> | 6 | Apache-2.0 | 2026-10-16 | 31 | Search showed `cadquery-anti-hallucination` and `cadquery-cookbook` |

`flowful-ai/cad-skill` description says CadQuery export to STL. The
license file was not opened, so SPDX `NOASSERTION` stands.

## MCP servers by domain

Detailed cards are in [mechanical](mechanical.md) and
[electrical](electrical.md). Index:

| Domain | Server | Mode |
| --- | --- | --- |
| FreeCAD | neka-nat, spkane, blwfish, theosib, contextform | Local app bridge |
| OpenSCAD | RobertCoop/openscad-mcp | Local CLI |
| Fusion | Autodesk local MCP and Fusion Data MCP | Local HTTP, and remote data |
| Fusion | shinobi81/fusion360-mcp-server | Local add-in, 0 stars |
| Onshape | Official FeatureScript MCP | Hosted HTTP |
| Onshape | hedless, jarvis, altendky | Local plus Onshape API. READMEs unread |
| CAD files | earthtojake/text-to-cad | Local, build123d |
| CAD app | SolidCraft built-in MCP | Local. Tool names in `docs/mcp.md`. Command catalog is dynamic |
| CAE | Cai-aa/CAE-Agent-Hub | Local solver bridges |
| KiCad | ProductOfAmerica, oaslananka, mixelpixx, Konnect | Local. Konnect repo archived. Successor is Konnect-EDA |
| SPICE | Cognitohazard/ltspice-mcp, ghensley/circuit-sim-mcp | Local |
| Embedded | jl-codes/platformio-mcp | README: build, flash, monitor. Not run |
| Instruments | abhinav937/pyvisa-mcp | README tool table read. Writes gated |
| CFD | csml-rpi/Foam-Agent | `foamagent-mcp`, seven tools, OpenFOAM v10 or ESI v2006 |

## Hosted agents that are not local weights

| Name | URL | What the page states |
| --- | --- | --- |
| Zoo Zookeeper | <https://zoo.dev/research/zookeeper> | Conversational CAD agent in Design Studio, KCL tools, snapshots, mass properties. Shipped with Design Studio v1.1 in January 2026 |
| Zoo Agent API | <https://zoo.dev/docs/developer-tools/agent-api> | Web API over the same agent direction. OpenAPI-derived SDKs |
| Fusion local MCP | Fusion help overview | Live session tools, list discovered at connect time |
| Onshape FeatureScript MCP | Onshape feature page | FeatureScript authoring inside documents |
| atopile agent | atopile 0.16.15 blog | Placement, routing, and a validator on each build |

Weights for these products were not published on the pages read.

## Applications with metadata only

| Name | URL | Stars | License | Note |
| --- | --- | --- | --- | --- |
| Amagine3D | <https://github.com/amagine-ai/Amagine3D> | 6,300 | Apache-2.0 | `pushed_at` 2026-10-22. Description: hardware requirements to editable 3D designs. README not opened |
| Multi-Agent CAD | <https://github.com/Pan-Chera/Multi-Agent-CAD> | 1,071 | MIT | `pushed_at` 2026-11-04. Description: text-to-CAD with constrained test-time compute. README not opened |
| NativeCAD | <https://featureboard.ai/nativecad/> | unknown | unknown | Vendor page claims 177 MCP tools, STEP, sheet metal, FEA and CFD. No repository confirmed |
