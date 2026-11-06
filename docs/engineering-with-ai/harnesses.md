# Creator accounts and CAD or circuit harnesses

Recorded 2026-11-06. A **harness** here is a published loop that tells an
agent how to call a CAD or EDA tool and how to read a check back
(geometry, ERC, DRC, a render, or a netlist). It is not the company
named Harness, and it is not a generic coding agent by itself.

A row is included when a person wrote, in a post or a repository they
control, that they built the workflow, or when the repository's own
files describe that loop. User reports that only say "I used someone
else's server" are in [Use reports](#use-reports). They are not counted
as the author's harness.

Public X search was called once. The API returned `client-forbidden`
with `user-not-enrolled`. No X post is cited. The call was not repeated.

Reddit `.json` requests returned HTTP 403. Reddit dates and handles
below are the ones printed by the search index for that URL. The page
body was not fetched again.

## How the pieces differ

| Kind | What the files show | Examples read this pass |
| --- | --- | --- |
| Check loop | A skill or script that runs the kernel and stops on a failed measurement | `0oKevino0/claude-cad` |
| Task kernel | The agent submits a program. A separate process builds, stores a draft, and requires accept or reject | `wangtao9090/VibeCAD` |
| Workspace plus skills | An app hosts the agent and ships skills that call KiCad or FreeCAD and then a viewer or CLI | Backplane, MetaForge |
| Agent pipeline in one skill | One `SKILL.md` sequences several external tools and names an exit check | ProtoForge, SKiDL skills |
| Reference skill | Text that corrects API use. It does not run a solver | `jmwright/cadquery-llm-skill`, `rawwerks/VibeCAD` |
| Tool server or plugin | MCP or a KiCad plugin. Any loop lives in the host agent's chat | KiCAD-MCP-Server, K-AI, kicad-sch-api |

## claude-cad

| Field | Record |
| --- | --- |
| Repo | <https://github.com/0oKevino0/claude-cad> |
| API | Created 2026-06-18. `pushed_at` 2026-10-05. 5 stars. MIT |
| Skill read | `.claude/skills/cadquery-modeling/SKILL.md`, name `cadquery-modeling` |
| Claim | README: a hollow enclosure can print `[OK]`, look right as STL, and still be a solid brick because `.shell()` did nothing. The numbers in that README are 158,048 mm³ measured against about 33,370 mm³ derived from a 94 × 65 × 26 mm box with 2.5 mm walls. A second README case says SolidWorks opened a solid claiming 51,185 mm³ inside a 32,000 mm³ box with no import dialog |
| Loop | Host model is whatever Claude Code is using. The skill writes one CadQuery file per part, runs it with Python 3.11, and requires `BRepCheck_Analyzer.IsValid()`, exactly one solid, a volume range computed from the requested dimensions, a bounding box, and optional inside or outside points via `scripts/diagnose.py`. Export is STEP and STL. Assemblies are left to SolidWorks |
| Install | `git clone`, then `pip install cadquery` on Python 3.11. The skill is already under `.claude/skills/` in the clone. README says newer Pythons lack the OCP binding used here |
| Evidence | The volume figures are in the repository README and the skill, tied to `references/occ_pitfalls.md`. This survey did not rerun them. A matching first-person post is indexed at <https://www.reddit.com/r/claudeskills/comments/1vil0vh/claude_code_kept_giving_me_cad_that_looked/>. The Reddit author handle was not in the index snippet, and the JSON fetch was blocked |
| Gap | One skill. No ERC or DRC. The README says the shipped example part measures 32,163.55 mm³ and 27.2 mm tall because of a lid lip, so the 33,370 mm³ expression is the blank enclosure, not that shipped solid |

## VibeCAD (Wang Tao)

| Field | Record |
| --- | --- |
| Repo | <https://github.com/wangtao9090/VibeCAD> |
| Package | <https://pypi.org/project/vibecad/> version 0.10.1. PyPI author line: Wang Tao, email `wangtao9090@gmail.com`. MIT. Python 3.12 or newer |
| API | GitHub `pushed_at` 2026-08-21. 3 stars. The PyPI page describes 0.10.1 features that may be ahead of that push. The skill file on the default branch was read and already names 39 tools |
| Skill read | `skills/vibecad-agent/SKILL.md`, name `vibecad-agent` |
| Loop | The host model does not receive a FreeCAD Python console. The skill lists 39 tools: runtime (`ping`, `ensure_runtime`), projects and tasks (`create_task`, `submit_model_program`, `accept_draft`, `reject_draft`, `approve_release`), reconstruction, and six direct solids (`create_box`, `create_cylinder`, `inspect_model`, `modify_parameter`, `move_part`, `rotate_part`). Direct tools and `submit_model_program` both enter a Task Kernel. FreeCAD runs in a managed worker. Success is an accepted artifact, not the model's last sentence |
| Install | PyPI text: the MCP bundle and the skill are separate. Copy `skills/vibecad-agent/` into the host skill directory (Claude Code `.claude/skills/vibecad-agent`, or the Codex paths named on the page). Linux and Windows on ARM are outside the support statement on that page. A managed FreeCAD runtime is part of the package |
| Evidence | No independent part measurement was in the files read. The 39-tool list is the skill's own catalog |
| Gap | GitHub star count is 3. No dated personal post by Wang Tao was opened beyond the package metadata |

A different repository, <https://github.com/rawwerks/VibeCAD>, is a skill library (MIT, 125 stars, `pushed_at` 2026-01-05) with `build123d`, `model-compare`, `gltf-transform`, and `render-glb`. It is not Wang Tao's package. <https://github.com/10-X-eng/vibecad> is a FreeCAD fork (LGPL-2.1, 214 stars, `pushed_at` 2026-09-18) and has no `SKILL.md` in the tree that was listed.

## Backplane

| Field | Record |
| --- | --- |
| Repo | <https://github.com/BackplaneWorks/Backplane> |
| API | Created 2026-09-06. `pushed_at` 2026-11-05. 932 stars. MIT |
| Claim | README: "Your agent edits KiCad and FreeCAD files." "Made and maintained by electrical engineers." No personal name is on the README section that was read. KiCad fork: <https://github.com/BackplaneWorks/Backplane_KiCad> |
| Skills read | `deploy/kistack/skills/schematic/SKILL.md` (`kicad-schematic`) and the start of `skills/backplane-e2e/SKILL.md`. Other `SKILL.md` paths in the tree: `bom`, `export`, `footprint`, `gerbers`, `layout-placement`, `layout`, `panelize`, `pcb-product-render`, `pcb`, `symbol` |
| Loop | `kicad-schematic` tells the agent to save through KiCad IPC `SaveDocument`, show the file with `viewer_show`, wire mostly with labels, and refuse to trust a text edit of the schematic alone. It requires a high-resolution SVG converted to an image, plus a netlist check, and a pin-number check after symbol edits. `backplane-e2e` is a UI release test of 32 user stories. It is not the design loop |
| Install | README: `curl` install script, or platform archives. Needs an agent CLI, KiCad for boards, FreeCAD for mechanical parts |
| Evidence | No board measurement or ERC count was in the sections read |
| Gap | Skill bodies other than schematic and the e2e header were not opened. The maintainer sentence does not name a person |

## MetaForge

| Field | Record |
| --- | --- |
| Repo | <https://github.com/FidelOdok/MetaForge> |
| API | Created 2026-02-12. `pushed_at` 2026-11-05. 8 stars. Apache-2.0 |
| Skills | Git tree contains 263 `SKILL.md` files under `domain_agents/`. Two were opened: `mechanical/skills/generate_cad/SKILL.md` and `electronics/skills/run_erc/SKILL.md` |
| Loop | `generate_cad` calls `cadquery.create_parametric` or `freecad.create_parametric`, writes STEP, and optionally `twin.commit_geometry`. It returns volume and surface area. The file says it builds one parametric solid, not an assembly. `run_erc` calls `kicad.run_erc` and passes when error-severity violations are zero. The file says phase 1 does not auto-fix. README describes Claude Code and Codex plugins, approval on writes, CalculiX, SPICE, OpenFOAM, and Blender |
| Install | README: a `forge` CLI, Docker Compose, and a model key or Codex sign-in. Not followed here |
| Evidence | README marks several areas "Working". No third-party measurement was opened |
| Gap | 261 of 263 skill files were not read. Several read as interface cards for MCP tools rather than a transcript of a finished design |

## ProtoForge

| Field | Record |
| --- | --- |
| Repo | <https://github.com/ashishmgupta1005-blip/ProtoForge> |
| API | Created and `pushed_at` both 2026-06-09. 3 stars. SPDX `NOASSERTION` |
| Skill read | `skills/protoforge/SKILL.md`, name `protoforge` |
| Loop | One Claude Code skill, wizard by default. Phase exits named in the file: schematic ERC-clean via `kicad-cli sch erc` after a Python generator writes `.kicad_sch` with labels on pins and no wires. PCB DRC `0/0/0` with `--schematic-parity` after pcbnew scripts and Freerouting (DSN to SES). Enclosure STEP and STL through a FreeCAD MCP `execute_code`. Animation MP4 from `kicad-cli pcb export glb` and Blender. Each phase stops for approval unless the user says to run it through |
| Dependencies named | KiCad 10, KiPilot MCP (PCB only), Java, a Freerouting jar, FreeCAD MCP, Blender. Paths come from `~/.claude/protoforge.config` or `PATH` |
| Evidence | README shows an ESP32 GPS tracker animation as example output. No ERC log or DRC report is in the skill file. The repository had no later push after the creation day in the API snapshot |
| Gap | License file not detected. KiPilot and Freerouting versions are not pinned in the section that was read |

## SKiDL skills

| Field | Record |
| --- | --- |
| Repo | <https://github.com/nickkraakman/skidl-skills> |
| API | Created 2026-04-07. `pushed_at` 2026-04-08. 24 stars. MIT |
| First person | README: "Designing circuit boards is hard, especially for a hobbyist like me with no electrical engineering background." The same README says the plugin should get the user "80% of the way" and leaves placement and routing to work by Seve Ibarluzea at <https://blog.autorouting.com/>. That 80% figure is the author's estimate |
| Files read | `skills/new-circuit/SKILL.md` (`new-circuit`) and the README. Other skill paths: `design-review`, `erc-rules`, `find-part` |
| Loop | `new-circuit` reads `pipeline_state.json` and spawns an orchestrator. README names nine agents: orchestrator, requirements interviewer, circuit architect, part sourcer, datasheet librarian, SKiDL coder, block coder, assembler, ERC reviewer. Outputs named: `SPEC.md`, `circuits/*.py`, `outputs/*.net`, `outputs/BOM.csv`. Also "5 scripts, 4 skills, 4 hooks, 2 rules" |
| Gap | Agent prompt files were not opened one by one. No ERC log from a finished board is in the README section that was read. Last push is 2026-04-08 |

## CadQuery reference skill

| Field | Record |
| --- | --- |
| Repo | <https://github.com/jmwright/cadquery-llm-skill> |
| API | Created 2026-04-20. `pushed_at` 2026-05-19. 12 stars. Apache-2.0 |
| Skill read | `SKILL.md` has no YAML `name`. It is a CadQuery reference: Workplane API versus free functions, selector table, and anti-patterns. It tells the model to load the file before a CadQuery task. It does not run the script or check volume |
| Install | Clone and `@` the file from a Claude Code prompt. A `Modelfile` loads the text as an Ollama system prompt |
| Use report | HN user `okramcivokram`, 2026-08-17, <https://news.ycombinator.com/item?id=49327458>: CadQuery, CQ-editor, and this skill, driven by Claude Code, produced ESP32 cases. The comment says the parts were not complicated. `okramcivokram` is the user, not the skill author |

## Use reports

These posts describe someone else's tool, or a chat with no published skill.

| Who | When | URL | What they wrote | Artifact they named |
| --- | --- | --- | --- | --- |
| `pedda8862` | 2026-07-26 | <https://news.ycombinator.com/item?id=49062621> | Built a working board with an MCP server, soldered parts, and saw many vias | <https://github.com/mixelpixx/KiCAD-MCP-Server> |
| `moggi` | 2026-09-05 | <https://news.ycombinator.com/item?id=49573391> | Claude Code plus Konnect worked for design review. Routing stayed manual | <https://github.com/mixelpixx/Konnect> |
| `SequoiaHope` | 2026-09-05 | same thread | Converts Altium to KiCad and uses the KiCad API. Says a reverse converter exists and has not been validated | No repository URL in the fetched text |
| `u/colaco1123` | search index 2026-03-09 | <https://www.reddit.com/r/KiCad/comments/1rp7d95/i_built_a_kicad_plugin_that_generates_schematics/> | Released K-AI, a KiCad plugin that drives a browser Claude session and needs no API key | <https://github.com/colaco1123/K-AI>. API: 46 stars, `pushed_at` 2026-03-09, no license file, no `SKILL.md`. A reply in the index says the plugin reported success and the schematic did not change |
| `u/Ambitious_Split_6670` | search index 2026-04-22 | <https://www.reddit.com/r/ClaudeCode/comments/1st047m/generate_3d_models_in_claude_code/> | Describes a recipe: one Python file per STEP, build123d rather than CadQuery, local UI for faces and edges, markdown feature notes, screenshots plus geometry checks. Names GPT 5.4 and Opus 4.6 as the models used | Links <https://github.com/earthtojake/text-to-cad>. The GitHub account `earthtojake` was not matched to this Reddit account from a profile page |
| `u/spinozasrobot` | search index 2026-09-25 | <https://www.reddit.com/r/KiCad/comments/1wph5ej/astra_and_kicad_fpv_flight_controller_in_3_hours/> | Built a board with Claude Code by reading and writing KiCad files, without an MCP server | No repository in the fetched reply |
| `u/Apart-Addition5835` | search index 2026-09-24 | same thread | Reports that GPT-6 Astra, through Codex inside KiCad, produced a 6-layer F405 flight-controller board in 3 hours 13 minutes and about 52 million tokens, including ERC, DRC, Gerbers, BOM, and STEP | No harness repository in the post text that was indexed. Treated as a product demo claim, not a published skill pack |

## Not opened far enough to call a harness

| Name | URL | Why it stays out of the case studies |
| --- | --- | --- |
| Cxddie | <https://cxddie.com/> | Vendor page. Says agents share six MCP tools across FreeCAD, CadQuery, build123d, and several commercial CAD programs. No repository file was opened |
| 3DCodeVerse | <https://github.com/gaoypeng/3dcodeverse> | 20 `SKILL.md` files under `harness/codeverse3d/`, including `c3d-cadquery-forms` and `c3d-urdf-joints`. Apache-2.0. 365 stars. `pushed_at` 2026-11-04. The harness README path did not return a file. No creator post was opened |
| circuit-synth | <https://github.com/circuit-synth/circuit-synth> | MIT. 291 stars. `pushed_at` 2026-03-08. README shows Python `@circuit` functions that connect pins. The tree listing returned no `SKILL.md`. Companion <https://github.com/circuit-synth/kicad-sch-api> (MIT, 57 stars) is the schematic library. A Reddit index post says that library includes a 15-tool MCP server. That README was not re-read this pass |
