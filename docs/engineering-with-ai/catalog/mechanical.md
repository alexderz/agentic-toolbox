# Mechanical catalog

Snapshot 2026-11-06. Fields follow [method](../method.md). Class
`tool-driver` means an agent calls a geometry kernel. Class `specialist`
means a model emits geometry or a CAD program.

## Local parametric kernels

### build123d

| Field | Value |
| --- | --- |
| URL | <https://github.com/gumyr/build123d> |
| Capabilities | Python CAD library. Release notes were not reread line by line. CADGenBench names it as a STEP/BREP backend |
| Maturity | GitHub latest release `v0.13.0`, published 2026-09-21. `pushed_at` 2026-11-05. 3,633 stars |
| License | Apache-2.0 (`github-api`) |
| Dependencies | Python. CADGenBench `pyproject.toml` also pins `build123d>=0.10.0` and notes `cadquery-ocp` wheels |
| Formats | STEP/BREP via the CADGenBench baseline. Other exporters unknown on this pass |
| Read/write | Writes geometry by running Python. Reads depend on the script |
| Mode | Local |
| Evidence | `github-api`, CADGenBench README |
| Class | tool-driver |

### CadQuery

| Field | Value |
| --- | --- |
| URL | <https://github.com/CadQuery/cadquery> and <https://cadquery.org> |
| Capabilities | GitHub description: Python parametric CAD scripting framework based on OCCT. CADGenBench baseline can target CadQuery as an alternative STEP backend |
| Maturity | Latest release `v2.8.0` (name "CadQuery 2.8.0"), published 2026-06-20. `pushed_at` 2026-10-24. 6,066 stars |
| License | License file header: Apache Public License, v 2.0. GitHub SPDX `NOASSERTION` |
| Dependencies | OCCT through the project's install path. Exact current install command not re-copied |
| Formats | STEP/BREP in the CADGenBench baseline. Further formats unknown here |
| Read/write | Script writes a solid |
| Mode | Local |
| Evidence | `github-api`, `license-file`, CADGenBench README |
| Class | tool-driver |

### OpenSCAD

| Field | Value |
| --- | --- |
| URL | <https://github.com/openscad/openscad> and <https://www.openscad.org> |
| Capabilities | GitHub description: programmer's solid 3D CAD modeller. Geometry is CSG. `openscad-mcp` README says exports are meshes, not STEP |
| Maturity | `pushed_at` 2026-11-06. 10,597 stars. Latest release tag not requested |
| License | `COPYING` is GNU GPL version 2, plus a stated exception for linking CGAL. GitHub SPDX `NOASSERTION` |
| Dependencies | OpenSCAD executable for the MCP server below |
| Formats | `openscad-mcp` README excerpt: STL, 3MF, AMF, OFF, and 2D DXF, SVG, PDF. No STEP |
| Read/write | Script in, mesh out |
| Mode | Local desktop and CLI |
| Evidence | `github-api`, `license-file`, MCP README excerpt |
| Class | tool-driver |

### OpenSCAD MCP

| Field | Value |
| --- | --- |
| URL | <https://github.com/RobertCoop/openscad-mcp> |
| Capabilities | README excerpt: render, measure, interference and clearance, holes and features, printability, export. FastMCP. Supported floor OpenSCAD 2021.01 |
| Maturity | `pushed_at` 2026-09-10. 170 stars. Created 2025-08-28 |
| License | MIT (`github-api`) |
| Dependencies | OpenSCAD, Python, uv/uvx in the install snippet from search |
| Formats | Meshes and 2D exports as above |
| Read/write | Reads a script, writes renders and exports |
| Mode | Local stdio MCP |
| Evidence | `github-api` plus README excerpt captured in search. Full tool table not re-fetched |
| Class | tool-driver |

## Live CAD sessions

### FreeCAD MCP (neka-nat)

| Field | Value |
| --- | --- |
| URL | <https://github.com/neka-nat/freecad-mcp> |
| Capabilities | README: create and edit models, run Python, inspect documents, run FEM analyses. Two parts: an addon inside FreeCAD and an MCP server. Default connection localhost. Client example uses `uvx freecad-mcp` |
| Maturity | `pushed_at` 2026-10-25. 3,229 stars. Created 2023-11-25. No GitHub latest release (API 404) |
| License | MIT |
| Dependencies | FreeCAD, uv. FreeCAD version floor not stated in the excerpt |
| Formats | Whatever the FreeCAD session can export. List not copied |
| Read/write | Reads and writes the open document. FEM run is a write plus a solver result |
| Mode | Local. FreeCAD GUI process plus stdio MCP |
| Evidence | README page and `github-api` |
| Class | tool-driver |

### FreeCAD Robust MCP (spkane)

| Field | Value |
| --- | --- |
| URL | <https://github.com/spkane/freecad-addon-robust-mcp-server> |
| Capabilities | README: 150+ tools, primitives, PartDesign, booleans, export, macros. Connection modes XML-RPC, JSON-RPC socket, or embedded. GUI and headless. Package name `freecad-robust-mcp` |
| Maturity | `pushed_at` 2026-11-05. 265 stars. Created 2026-01-03. Docs: <https://spkane.github.io/freecad-addon-robust-mcp-server/> |
| License | Apache-2.0 |
| Dependencies | README: FreeCAD 1.0.2 or newer, 1.1.4 or newer recommended by that README. Python 3.11+ for the external server |
| Formats | Export named. Exact format list not copied |
| Read/write | Reads and writes FreeCAD |
| Mode | Local |
| Evidence | README and `github-api` |
| Class | tool-driver |

### Other FreeCAD bridges

| Repo | API on 2026-11-06 | License | Notes from the page opened |
| --- | --- | --- | --- |
| <https://github.com/blwfish/freecad-mcp> | 64 stars, `pushed_at` 2026-11-02 | LGPL-2.1 | README: 32 tools. CAM tools need a current FreeCAD weekly. Other tools claimed on FreeCAD 1.1.x. Smoke-tested by the author against LM Studio MCP |
| <https://github.com/theosib/FreeCAD-MCP-Server> | 38 stars, `pushed_at` 2026-03-05 | none detected | README: document graph, shape topology, sketch degrees of freedom, recompute diff, `execute_script`, screenshot. TCP to an addon |
| <https://github.com/contextform/freecad-mcp> | 139 stars, `pushed_at` 2025-08-15 | none detected | README: PartDesign, Part, view, Python. Created 2025-08-08. No push since 2025-08-15 |

These three were not installed.

### Autodesk Fusion MCP (official)

| Field | Value |
| --- | --- |
| URL | <https://help.autodesk.com/view/fusion360/ENU/?guid=FMCP-OVERVIEW> |
| Capabilities | Two servers. Local server drives a live Fusion desktop session. Cloud "Fusion Data MCP" queries Manufacturing Data Model hubs, projects, folders, and items. Help says tool lists are dynamic and discovered at connection time |
| Maturity | Help page fetched 2026-11-06. First-ship date not on that page. A Fusion blog post documents enabling the server under Preferences, General, API |
| License | Proprietary Fusion application. MCP protocol is the client's connection. Product license terms not copied |
| Dependencies | Local server: Fusion desktop running, preference enabled. Cloud server: Autodesk account and `https://developer.api.autodesk.com` |
| Formats | The design in the live session. Export formats not listed on the overview page |
| Read/write | Local server reads and writes the session. Cloud server, as described, manages data-model records |
| Mode | Local HTTP while Fusion runs. Cloud server is remote. Blog example URL `http://127.0.0.1:27182`, with the port taken from Fusion preferences. The blog says the default is usually 27182 |
| Evidence | `official-doc` plus Fusion blog |
| Class | tool-driver |

Which Fusion subscription includes the toggle is unknown (G3).

### Fusion 360 community MCP

| Field | Value |
| --- | --- |
| URL | <https://github.com/shinobi81/fusion360-mcp-server> |
| Capabilities | README: 96 tools in 17 groups, including sketch constraints, features, joints, interference, physical properties, CAM setup and post, STEP/STL/f3d export, viewport PNG, `execute_code` |
| Maturity | Created 2026-11-01. `pushed_at` 2026-11-05. 0 stars. README pins client example `v0.3.1` |
| License | AGPL-3.0 |
| Dependencies | uv, Fusion 360, an MCP client. Add-in listens on `127.0.0.1:9876` per README |
| Formats | README names STL, STEP, f3d, and a view sheet |
| Read/write | Reads and writes the Fusion session |
| Mode | Local socket plus stdio |
| Evidence | README excerpt and `github-api`. Not run |
| Class | tool-driver |

### Onshape FeatureScript MCP (official)

| Field | Value |
| --- | --- |
| URL | <https://www.onshape.com/en/features/featurescript-mcp> and <https://www.onshape.com/en/blog/featurescript-mcp-server-enables-text-code-cad> |
| Capabilities | Official posts: an MCP client writes FeatureScript into a Feature Studio, runs it, reads errors, and revises it. The feature remains a parametric Onshape feature. Endpoint published as `https://fs-mcp.labs.onshape.app/mcp`, transport HTTP |
| Maturity | Described as Onshape Labs early access. Page dates not extracted |
| License | Onshape account and App Store subscription. FeatureScript standard-library license not opened |
| Dependencies | Onshape account, App Store subscribe, MCP client, user authorization |
| Formats | FeatureScript inside an Onshape document. STEP export is a separate Onshape capability and was not described on these MCP pages |
| Read/write | Writes FeatureScript and reads execution feedback |
| Mode | Vendor-hosted MCP |
| Evidence | `official-doc`. Tool schema not downloaded (G4) |
| Class | tool-driver |

### Community Onshape MCP servers

| Repo | Stars | `pushed_at` | License | Evidence |
| --- | --- | --- | --- | --- |
| <https://github.com/hedless/onshape-mcp> | 163 | 2026-09-10 | none detected | Description only: "mcp server for interacting with onshape". README not opened |
| <https://github.com/ReshefElisha/jarvis-onshape-mcp> | 175 | 2026-04-22 | SPDX `NOASSERTION` | Description claims a Claude Code plugin, vision decomposition, parametric iteration, FeatureScript. README not opened |
| <https://github.com/altendky/onshape-mcp> | 20 | 2026-11-06 | Apache-2.0 | Description: AI-assisted access to Onshape documents. README not opened |

Mode for these is local process plus Onshape API credentials, inferred from the descriptions. Credential scope unknown.

### SolidCraft

| Field | Value |
| --- | --- |
| URL | <https://github.com/tangency-labs/solidcraft> and <https://docs.solidcraft.io/> |
| Capabilities | README: open-source parametric 3D CAD in Rust. Sketch, constraints, feature timeline, desktop, browser, and a built-in MCP server. 17 `SKILL.md` files in the tree. Skill bodies not read |
| Maturity | Latest release `v0.30.1`, published 2026-11-02. `pushed_at` 2026-11-06. Created 2026-10-07. 14,178 stars |
| License | Apache-2.0 (`github-api`) |
| Dependencies | Desktop install or the web app. MCP command line not copied from docs |
| Formats | Unknown in this pass (G2) |
| Read/write | README says agents model through MCP. Exact read/write split unknown |
| Mode | Local app, plus a browser app |
| Evidence | `readme`, `github-api`, `git-tree` |
| Class | tool-driver |

### text-to-cad plugin

| Field | Value |
| --- | --- |
| URL | <https://github.com/earthtojake/text-to-cad> and <https://www.texttocad.dev> |
| Capabilities | README: agent writes build123d Python. `python model.py` builds an `.xbf` document and declared STEP, GLB, STL, or 3MF. Viewer follows rebuilds. Skills in tree: `cad`, `dfm`, `dfam-check`, `dxf`, `engineering-drawing`, `gcode`, `step-parts`, `bambu-labs`, `sendcutsend`, `urdf`, `srdf`, `sdf` |
| Maturity | `pushed_at` 2026-11-05. Created 2026-04-22. 25,621 stars. PyPI package `cad-server` linked from the README badge. Version not fetched |
| License | MIT (`github-api` and README badge) |
| Dependencies | README install uses `curl` to `https://texttocad.dev/install.sh` or a Windows script, then uv. Not run |
| Formats | STEP, GLB, STL, 3MF, DXF, G-code, URDF, SRDF, SDF, drawings, named by skill paths and README |
| Read/write | Writes models and checks named by skills. Skill internals unread (G1) |
| Mode | Local server and local files, per README |
| Evidence | `readme`, `git-tree`, `github-api` |
| Class | tool-driver |

### CADAM

| Field | Value |
| --- | --- |
| URL | <https://github.com/Adam-CAD/CADAM> and <https://adam.new/cadam> |
| Capabilities | Description: open source text-to-CAD web application. README not opened |
| Maturity | `pushed_at` 2026-10-15. Created 2025-09-01. 5,400 stars |
| License | GPL-3.0 |
| Dependencies | unknown |
| Formats | unknown |
| Read/write | unknown |
| Mode | Web application, from the description |
| Evidence | `github-api` |
| Class | unknown until the README is read |

### Zoo Agent API and Zookeeper

| Field | Value |
| --- | --- |
| URL | <https://zoo.dev/docs/developer-tools/agent-api>, <https://zoo.dev/research/zookeeper>, <https://zoo.dev/blog/kcl-3> |
| Capabilities | Agent API page: CAD-focused LLM agent through a web interface, for creating models, CAD questions, and analysis including FEA tools available to it. Zookeeper page (January 2026, Design Studio v1.1): conversational agent inside Zoo Design Studio. Tools write and debug KCL, take visual snapshots, and compute center of mass, mass, area, and volume. KCL 3 announced 2026-10-08. New files default to KCL 3. KCL 2 files keep working. Zookeeper can migrate KCL 2 to 3 |
| Maturity | Dates above are the pages' own dates. App version beyond the v1.1 mention was not checked |
| License | unknown for the engine and for KCL (G5, G6) |
| Dependencies | Zoo account and Design Studio or the API. SDK source is an OpenAPI spec, per the Agent API page |
| Formats | KCL. Export formats not listed on the pages read |
| Read/write | Creates and edits models. Analysis tools read geometry |
| Mode | Web agent. Kernel location unknown (G5) |
| Evidence | `official-doc` |
| Class | tool-driver (hosted). A separate Text-to-CAD product from December 2023 is described on the Zookeeper page as two endpoints, generate and edit, implemented as an agent |

`KittyCAD/text-to-cad-ui` is archived. `pushed_at` 2026-01-16. 296 stars. MIT. Description: lightweight UI for the Zoo Text-to-CAD API.

### gitcad

| Field | Value |
| --- | --- |
| URL | <https://github.com/gitcad-xyz/gitcad> |
| Capabilities | Search-captured README: headless B-rep, mechanical and electrical, text canonical model, MCP as primary interface, STEP/STL/DXF, drawings with GD&T, mates, schematic ERC, board DRC, Gerber, SPICE export. 2 stars |
| Maturity | Created 2026-07-22. `pushed_at` 2026-07-31 |
| License | Apache-2.0 |
| Dependencies | unknown beyond the README's own stack |
| Formats | As named in that excerpt |
| Read/write | README claims both |
| Mode | Local, from the excerpt |
| Evidence | Search excerpt and `github-api`. Not built (G24) |
| Class | tool-driver |

## CAM, FEA, CFD

CAM tool names that were actually seen:

- `shinobi81/fusion360-mcp-server` README: `cam_create_setup`, `cam_create_operation`, `cam_post_process`.
- `blwfish/freecad-mcp` README: CAM toolpath generation on a current FreeCAD weekly, not on 1.1.x.
- text-to-cad skill paths: `gcode`, `dfm`, `dfam-check`, `dxf`, `sendcutsend`, `bambu-labs`. Bodies unread.

No toolpath was generated in this survey.

### CAE-Agent-Hub

| Field | Value |
| --- | --- |
| URL | <https://github.com/Cai-aa/CAE-Agent-Hub> |
| Capabilities | README table lists MCP servers for Abaqus/CAE, ANSYS Fluent, ANSYS Workbench, Ansys AEDT/HFSS, Altair HyperWorks, LAMMPS, OVITO, CalculiX (`ccx` decks, design variables, modal results, sizing optimization), Peridigm (prototype), and a FreeCAD plus Elmer plus ParaView coordinator |
| Maturity | `pushed_at` 2026-10-27. Created 2026-04-27. 1,279 stars |
| License | MIT for the hub repository. Solver products have their own licenses |
| Dependencies | Each bridge names its solver. Commercial solvers need that vendor's install. Not verified here |
| Formats | CalculiX row names `.inp`, `.dat`, `.frd`. Others per the table |
| Read/write | The table describes live sessions, job submit, and result readback |
| Mode | Local bridges |
| Evidence | README table captured from the repository page. Servers not started (G13) |
| Class | tool-driver |

### Foam-Agent

Paper only on this pass. See [papers](papers.md). Repository not found (G12).

## Assemblies

Sources that name assembly operations, without an assembly benchmark:

| Source | What it names |
| --- | --- |
| Fusion community MCP README | `create_component`, `add_joint`, `set_joint_value`, `create_rigid_group`, `check_interference` |
| theosib FreeCAD MCP README | Sketch constraint health: degrees of freedom, conflicts, redundancies |
| text-to-cad skills | `urdf`, `srdf`, `sdf` |
| Zoo Zookeeper page | Mass properties and multi-view review, not a mate solver |
| gitcad excerpt | Mate checking and interference budgets |

Constraint satisfaction was not measured.
