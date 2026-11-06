# Skill-pack comparison

Snapshot 2026-11-06. Counts are `SKILL.md` paths from
`git/trees/HEAD?recursive=1` unless a row says a file was opened.
Case studies, with the text that was actually read, are in
[harnesses](../harnesses.md). Earlier directory counts that were not
re-opened this pass stay in [agents, MCP, and skills](agents-mcp-skills.md).

| Pack | Kind | Skills opened or named | Feedback the files name | License | Stars | `pushed_at` |
| --- | --- | --- | --- | --- | --- | --- |
| [claude-cad](https://github.com/0oKevino0/claude-cad) | Check loop | `cadquery-modeling` opened | `IsValid`, one solid, derived volume, bbox, inside and outside points | MIT | 5 | 2026-10-05 |
| [VibeCAD agent](https://github.com/wangtao9090/VibeCAD) | Task kernel | `vibecad-agent` opened. Skill text says 39 tools | Draft accept or reject, release approval, inspect | MIT | 3 | 2026-08-21 |
| [rawwerks/VibeCAD](https://github.com/rawwerks/VibeCAD) | Reference skills | Paths: `build123d`, `model-compare`, `gltf-transform`, `render-glb`. Bodies not quoted | `render-glb` and `model-compare` names only | MIT | 125 | 2026-01-05 |
| [Backplane kistack](https://github.com/BackplaneWorks/Backplane) | Workspace skills | `kicad-schematic` opened. Eleven design skill paths plus `backplane-e2e` | SVG image plus netlist. IPC `SaveDocument` | MIT | 932 | 2026-11-05 |
| [MetaForge](https://github.com/FidelOdok/MetaForge) | Skill cards over MCP | 263 files. `generate_cad` and `run_erc` opened | STEP volume. ERC error count zero | Apache-2.0 | 8 | 2026-11-05 |
| [ProtoForge](https://github.com/ashishmgupta1005-blip/ProtoForge) | One orchestration skill | `protoforge` opened | `kicad-cli` ERC, DRC with schematic parity, STEP/STL, MP4 | none detected | 3 | 2026-06-09 |
| [skidl-skills](https://github.com/nickkraakman/skidl-skills) | Agent pipeline | `new-circuit` opened. Also `design-review`, `erc-rules`, `find-part`. README lists 9 agents | ERC reviewer PASS/FAIL. Netlist and BOM | MIT | 24 | 2026-04-08 |
| [cadquery-llm-skill](https://github.com/jmwright/cadquery-llm-skill) | Reference text | `SKILL.md` opened. No YAML name | None. The model is told how to call CadQuery | Apache-2.0 | 12 | 2026-05-19 |
| [text-to-cad](https://github.com/earthtojake/text-to-cad) | Local CAD server plus skills | 12 paths. `cad` and `engineering-drawing` were read in the prior pass | Rebuild, PDF drawing notes, STEP export | MIT | 25,621 | 2026-11-05 |
| [3DCodeVerse harness](https://github.com/gaoypeng/3dcodeverse) | Research skill tree | 20 paths listed, including `c3d-cadquery-forms` and `c3d-urdf-joints`. Bodies not opened this pass | Unknown until a skill body is read | Apache-2.0 | 365 | 2026-11-04 |
| [kicad-mcp-pro](https://github.com/oaslananka/kicad-mcp-pro) | MCP plus copied skills | Seven names, five identical blobs each. See [electrical](electrical.md) | ERC/DRC skills exist. Bodies not re-read this pass | MIT | 182 | 2026-11-06 |
| [mcp-server-kicad](https://github.com/ProductOfAmerica/mcp-server-kicad) | MCP plus skills | 6 files. Maintenance mode. Skill forbids `kicad-cli`. README recommends it | Server tools and CLI disagree. See [electrical](electrical.md) | GPL-3.0 | 16 | 2026-11-05 |
| [JITX skills](https://github.com/JITx-Inc/jitx-skills) | Vendor skills | 11 paths listed earlier. Bodies not re-read | JITX compiler. License file is proprietary | proprietary | 20 | 2026-11-05 |
| [K-AI](https://github.com/colaco1123/K-AI) | KiCad plugin, no skill file | No `SKILL.md` | Browser Claude session edits a schematic. A Reddit reply says one run reported success with no file change | none detected | 46 | 2026-03-09 |
| [circuit-synth](https://github.com/circuit-synth/circuit-synth) | Python circuits, no skill file in the tree | No `SKILL.md` | Python connectivity. KiCad export is described in the README | MIT | 291 | 2026-03-08 |

Stars and `pushed_at` are the GitHub API values from 2026-11-06.
text-to-cad's star count is the whole repository, not a measure of one
skill. MetaForge's 263 files were not each reviewed.
