# Landscape

Pass 0, closed 2026-11-06. No winner is selected.

## Job

Record how an agent can produce or check a mechanical part, an
electrical design, or a design that is both, using public interfaces.
The output of interest is a file a later tool can check: STEP, a mesh,
a drawing, a solver deck, a schematic, a board, a netlist, HDL, or a
test log.

## Facets

| Domain | Facet | Primary artifact a check can read |
| --- | --- | --- |
| Mechanical | Parametric CAD | Script plus rebuilt solid |
| Mechanical | Text or code to CAD | Prompt or code in, STEP or mesh out |
| Mechanical | Assembly and constraints | Mates, joints, or degrees of freedom |
| Mechanical | Drawings and GD&T | Drawing sheet, dimensions, tolerances |
| Mechanical | CAM and manufacturing | Toolpath, G-code, or DFM report |
| Mechanical | FEA, CFD, multiphysics | Solver deck and a result file |
| Mechanical | Topology and generative design | Density field or generated solid |
| Electrical | Schematic and PCB | Schematic, board, Gerber, BOM |
| Electrical | SPICE and analog | Netlist and a simulation log |
| Electrical | Digital, HDL, FPGA | HDL and a simulator or P&R log |
| Electrical | Power and control | Converter or controller design files |
| Electrical | Embedded interfacing | Firmware project and a build log |
| Electrical | Test and instruments | SCPI or VISA session log |
| Both | Electromechanical | Shared envelope, STEP, URDF, or board outline |

## Two classes

| Class | What it is | Examples recorded in this pass |
| --- | --- | --- |
| Tool-driver | A general coding or vision-language agent writes code or calls MCP tools. Geometry and electrical checks happen in an external program | build123d or CadQuery scripts, KiCad CLI, FreeCAD MCP, Fusion MCP, Onshape FeatureScript MCP, PlatformIO MCP |
| Specialist | A model trained to emit a CAD sequence, a boundary representation, point-cloud-to-code, a Verilog module, or a circuit graph | Text2CAD, BrepGen, CAD-Recode, RTLCoder, AnalogGenie |

Hosted product agents (Zoo Zookeeper, Autodesk Fusion MCP, Onshape
FeatureScript MCP, atopile's agent) sit with the tool they attach to.
Their weights, if any, were not published in the pages read.

## Inclusion

Include a candidate when one of these is true:

- The GitHub API returned the repository on 2026-11-06.
- An official documentation page or paper page was fetched.
- A Hugging Face model or dataset card was fetched.

A name that appears only in a roundup, with no page opened, goes to
[open questions](open-questions.md) instead of a catalog card.

## Exclusion

This directory does not vendor skill bodies, MCP servers, or weights.
Marketplace install commands that appear in a README are quoted as
documentation of that project. They were not run.

## Question frontier

Questions Pass 1 and Pass 2 were required to touch. Status is the state
after the 2026-11-06 pass.

| ID | Question | Status |
| --- | --- | --- |
| Q1 | Which local, headless kernels accept Python and write STEP? | Answered for build123d 0.13.0 and CadQuery 2.8.0. See [mechanical](catalog/mechanical.md) |
| Q2 | Which MCP servers drive a live CAD session, and which need a GUI? | Answered for the FreeCAD, Fusion, Onshape, and OpenSCAD servers that were opened. Install not tested |
| Q3 | Is there a public mechanical benchmark with a validity gate? | CADGenBench README: STEP validity gate, then shape, interface, and topology. Scores not recomputed |
| Q4 | Which electrical checks are non-interactive? | KiCad 9 and 10 CLI docs: `sch erc` and `pcb drc` with exit code 0 or 5. Not run |
| Q5 | Which open weights are specialist CAD or HDL models with a stated size? | RTLCoder and CAD-Recode have sourced sizes. Qwen2.5-Coder and Qwen2.5-VL-7B weight-file bytes are in [models](catalog/models.md). Runtime peaks remain unknown |
| Q6 | Where do mechanical and electrical models meet? | URDF, SRDF, SDF, and JITX mechanical skill names; STEP export; KiCad 3D export named in MCP tool lists. No joint project was built |
| Q7 | Which papers release code, and which defer it? | See the artifacts column in [papers](catalog/papers.md). Several 2026 simulation papers say release is later |
| Q8 | What can a 24 GB-class machine run, without assuming a GPU is attached? | Only figures a paper or file listing states. See [models](catalog/models.md) |
| Q9 | Which GD&T, CAM, power-electronics, and instrument agents are real? | CAM tool names, the drawing skill, ngspice `.ac`, and the pyvisa-mcp tool table were read. A GD&T frame checker and a combined power-and-firmware loop remain open |
| Q10 | Do commercial MCP servers list a fixed tool schema? | Fusion help says tools are dynamic. Onshape FeatureScript MCP tools were not enumerated from a schema file |

## Market split observed in sources

The pages group into four stacks. This is a map of what the sources
are, not a ranking.

| Stack | Where geometry or the netlist is computed | Agent interface the sources describe |
| --- | --- | --- |
| Local open kernel | build123d, CadQuery, OpenSCAD, FreeCAD, KiCad, ngspice, Verilator | Python, CLI, or a community MCP bridge |
| Vendor desktop session | Autodesk Fusion MCP | Local HTTP MCP while the desktop app is running |
| Vendor cloud document | Onshape FeatureScript MCP, Zoo Agent API | Hosted MCP or web agent API |
| Research generator | Text2CAD, BrepGen, CAD-Recode, RTLCoder, AnalogGenie | Checkpoint or agent code beside a paper |
