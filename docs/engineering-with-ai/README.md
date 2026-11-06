# Mechanical and electrical engineering with AI

**Surveyed 2026-11-06.** Living notes. Nothing here is vendored, installed,
or cleared for use.

This directory records public tools, agent skills, Model Context Protocol
(MCP) servers, harnesses, papers, datasets, benchmarks, and local models
for mechanical and electrical engineering work. A general coding agent
that drives a CAD or EDA program is recorded separately from a model
trained to emit geometry or a circuit.

## How to read

| Page | What it holds |
| --- | --- |
| [Method](method.md) | Passes, evidence grades, candidate fields |
| [Landscape](landscape.md) | Pass 0: facets, inclusion, question frontier |
| [Log](log.md) | What each pass checked |
| [Sources](sources.md) | URLs opened on 2026-11-06 |
| [Open questions](open-questions.md) | Unknowns left for a later pass |
| [Mechanical catalog](catalog/mechanical.md) | CAD, CAM, FEA, CFD, topology |
| [Electrical catalog](catalog/electrical.md) | Schematic, PCB, SPICE, HDL, embedded, instruments |
| [Agents, MCP, skills](catalog/agents-mcp-skills.md) | Skills, MCP servers, hosted agents |
| [Models](catalog/models.md) | Specialist weights and local-size evidence |
| [Papers](catalog/papers.md) | Papers, datasets, benchmarks |
| [Evaluation](workflows/evaluation.md) | Checks a later run can execute |
| [Code CAD workflow](workflows/code-cad.md) | Documented code-to-solid loop |
| [EDA workflow](workflows/eda-and-circuits.md) | Documented schematic, SPICE, and HDL loops |
| [Cross-domain](workflows/cross-domain.md) | Electromechanical handoffs |

GitHub star counts and `pushed_at` dates come from the GitHub REST API
on 2026-11-06. `pushed_at` is the repository push timestamp, which can
differ from the newest commit on the default branch. Licenses are the
SPDX id GitHub detected, or the license file text when that detection
was `NOASSERTION` or missing.

This survey did not install skills or MCP servers, did not run solvers
or devices, and did not reproduce any benchmark score.

## Coverage on 2026-11-06

| Facet | Where | Depth |
| --- | --- | --- |
| Parametric CAD | [Mechanical](catalog/mechanical.md), [code CAD](workflows/code-cad.md) | Primary pages and releases for build123d, CadQuery, OpenSCAD, FreeCAD MCP, Fusion MCP, Onshape FeatureScript MCP, SolidCraft |
| Text and code to CAD | [Mechanical](catalog/mechanical.md), [papers](catalog/papers.md) | Zoo Agent API and Zookeeper pages, text-to-cad plugin, CADAM, Text2CAD, CAD-Recode, CADGenBench |
| Assembly and constraints | [Mechanical](catalog/mechanical.md), [cross-domain](workflows/cross-domain.md) | Tool claims for joints, mates, URDF, SRDF, SDF. No assembly benchmark was scored here |
| Drawings and GD&T | [Mechanical](catalog/mechanical.md), [papers](catalog/papers.md) | engineering-drawing skill name; OmniMech paper. Drawing skill body not read. No GD&T checker was run |
| CAM and manufacturing | [Mechanical](catalog/mechanical.md) | Fusion community MCP CAM tool names; text-to-cad `gcode`, `dfm`, `dxf` skill names. Toolpath quality unknown |
| FEA, CFD, multiphysics | [Mechanical](catalog/mechanical.md) | FreeCAD MCP FEM claim, CAE-Agent-Hub README table, Foam-Agent paper |
| Topology and generative design | [Papers](catalog/papers.md) | AutoSiMP and LLM-SIMP papers. Both say code follows publication or acceptance |
| Schematic and PCB | [Electrical](catalog/electrical.md), [EDA workflow](workflows/eda-and-circuits.md) | KiCad CLI docs, three KiCad MCP repositories, atopile, tscircuit, SKiDL, JITX skills |
| SPICE and analog | [Electrical](catalog/electrical.md), [papers](catalog/papers.md) | AnalogCoder, AnalogGenie, ltspice-mcp, circuit-sim-mcp |
| Digital, HDL, FPGA | [Electrical](catalog/electrical.md), [papers](catalog/papers.md) | VerilogEval, RTLCoder, EDA Corpus, OpenROAD Agent abstract. Yosys and nextpnr agent skills not surveyed |
| Power and control | [Open questions](open-questions.md) | Named inside analog and clearance checks. No dedicated control-design agent was read end to end |
| Embedded interfacing | [Electrical](catalog/electrical.md) | platformio-mcp repository metadata. Firmware behavior not run |
| Test and instruments | [Electrical](catalog/electrical.md) | pyvisa-mcp metadata. No instrument session was opened |
| Electromechanical | [Cross-domain](workflows/cross-domain.md) | URDF, SRDF, SDF, JITX mechanical skill, STEP and board exports |
| Skills and packs | [Agents](catalog/agents-mcp-skills.md) | `SKILL.md` path counts from Git trees |
| Harnesses | [Agents](catalog/agents-mcp-skills.md) | Clients named by vendor docs. No client was configured |
| Local models | [Models](catalog/models.md) | RTLCoder and CAD-Recode sizes from paper or file listing. Other VRAM figures unknown |

## Maintenance

Add a dated row to [log](log.md) when a page changes. Replace a number
only with a new source and the date it was read. Leave a field as
unknown when the source does not state it.
