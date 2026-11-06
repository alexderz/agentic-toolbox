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
