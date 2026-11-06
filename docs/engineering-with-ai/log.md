# Log

## 2026-11-06 — Pass 0

Opened the repository guidance (`AGENTS.md`, `docs/SDLC.md`,
`knowledge/README.md`, `docs/security-skill-packs/README.md`) and used
that catalog shape: dated survey, per-candidate fields, unknowns left
unknown.

Wrote the facet table, the tool-driver and specialist split, inclusion
rules, and questions Q1–Q10 in [landscape](landscape.md).

## 2026-11-06 — Pass 1

Fetched GitHub repository metadata, license files, release tags, and
`SKILL.md` trees for the repositories named in
[sources](sources.md). Fetched official docs for KiCad CLI 9 and 10,
Autodesk Fusion MCP, Onshape FeatureScript MCP, Zoo Agent API,
Zookeeper, and KCL 3. Fetched paper or dataset pages for Text2CAD,
DeepCAD, Fusion 360 Gallery, BrepGen, OpenECAD, CAD-Recode, CADGenBench,
VerilogEval, RTLCoder, AnalogCoder, AnalogGenie, EDA Corpus, Foam-Agent,
STEP-LLM, OmniMech, AutoSiMP, and the LLM-SIMP controller paper.

Did not install clients, skills, or MCP servers. Did not run FreeCAD,
Fusion, Onshape, KiCad, ngspice, Verilator, or any instrument.

## 2026-11-06 — Pass 2

Deepened three workflows that already publish a check:

- Code to STEP, using the CADGenBench validity gate and the build123d
  and CadQuery releases.
- KiCad ERC and DRC, using the KiCad 9 and 10 CLI manuals.
- HDL and SPICE loops, using VerilogEval's simulation check and
  AnalogCoder's PySpice plus ngspice description.

Recorded cross-domain file handoffs (STEP, URDF, SRDF, SDF, board
exports) without composing an untested pipeline.

Left GD&T semantics, CAM toolpath quality, power-electronics control
design, FPGA place-and-route agents, and instrument sessions as open
questions.

## 2026-11-06 — Refinement

Read skill and MCP documents that the first pass had only counted:
text-to-cad `engineering-drawing` and `cad`, SolidCraft `docs/mcp.md`,
Fusion community `docs/TOOLS.md`, Foam-Agent README, platformio-mcp
README, pyvisa-mcp README, mcp-server-kicad maintenance section,
Konnect archive notice, and KiCad MCP Pro blob SHAs.

Recorded official Qwen2.5-Coder GGUF and AWQ file sizes and the
Qwen2.5-VL-7B BF16 file size. Separated those byte counts from runtime
peaks. Did not load a model.

Verified <https://github.com/JasonShiii/STEP-LLM> and the Qwen LoRA
adapter size. Copied Yosys, nextpnr, OpenROAD-flow-scripts, ngspice
`.ac`, and python-control `margin` from their manuals into
[fpga-cae-control](workflows/fpga-cae-control.md).

Did not install tools, flash a board, open an instrument, or rerun a
benchmark.
