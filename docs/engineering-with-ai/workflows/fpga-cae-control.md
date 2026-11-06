# FPGA, CAE, CAM, and control

Documented commands and tool lists read on 2026-11-06. None of these
programs was installed or started. No bitstream, mesh, or instrument
session was produced.

## FPGA place and route

Yosys and nextpnr are the open FPGA path in their own READMEs.
OpenROAD-flow-scripts is an RTL-to-GDSII path for an ASIC-style flow.
It uses Yosys for logic synthesis and then floorplan, placement, clock
tree, and routing. It is not the iCE40 example below.

| Tool | Release recorded | License | `pushed_at` |
| --- | --- | --- | --- |
| [Yosys](https://github.com/YosysHQ/yosys) | `v0.70`, published 2026-10-13 | ISC | 2026-11-06 |
| [nextpnr](https://github.com/YosysHQ/nextpnr) | `nextpnr-0.11.1`, published 2026-08-11 | ISC | 2026-11-04 |
| [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | no GitHub latest release | BSD-3-Clause | 2026-11-05 |
| [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) | not requested | SPDX `NOASSERTION` | 2026-11-05 |

Yosys's getting-started page says to run `verilator --lint-only` on the
Verilog before synthesis, because `read_verilog` is a weak error
reporter. The same page's iCE40 example is `synth_ice40 -top fifo -json
fifo.json`. JSON is an input nextpnr can load.

nextpnr's README gives this iCE40 sequence for the blinky example. It
was not executed.

```text
yosys -p 'synth_ice40 -top blinky -json blinky.json' blinky.v
nextpnr-ice40 --hx1k --json blinky.json --pcf blinky.pcf --asc blinky.asc
icepack blinky.asc blinky.bin
```

`--hx1k` is the device in that example. Other nextpnr binaries named in
the same README, each with its own chip database: `nextpnr-ecp5`
(Project Trellis), `nextpnr-nexus` (Project Oxide), `nextpnr-mistral`
(Cyclone V), `nextpnr-machxo2`, `nextpnr-generic`, and
`nextpnr-himbaechel` (the README names Gowin and ng-ultra split
binaries). `icepack` and `iceprog` are Project IceStorm tools, not
nextpnr subcommands.

A pass for that example is a nextpnr run that writes `blinky.asc`, then
an `icepack` that writes `blinky.bin`. Timing slack and pin checks are
in the nextpnr log. This survey did not define a numeric slack limit.

OpenROAD-flow-scripts README: the flow stages are synthesis (Yosys,
inputs RTL, SDC, `.lib`, `.lef`), floorplan, placement, clock-tree
synthesis, routing, then GDSII and DRC/LVS through KLayout. A project
kept outside the ORFS tree is invoked as:

```text
make --file=~/OpenROAD-flow-scripts/flow/Makefile DESIGN_CONFIG=somefolder/config.mk
```

The `DESIGN_CONFIG` path is the project's. The README points at the
flow tutorial for a full RTL-to-GDSII run. No config was written here.

## OpenFOAM through Foam-Agent

<https://github.com/csml-rpi/Foam-Agent> release `v2.2.0`. MCP command
documented as `foamagent-mcp`. Tools: `plan`, `input_writer`, `run`,
`review`, `apply_fixes`, `run_case`, `visualization`. Default solver
tree is Foundation OpenFOAM v10. ESI/OpenCFD v2006 is selected with
`FOAMAGENT_OPENFOAM_TARGET=esi-v2006` and is a different Docker image.
The README says one image does not switch distributions at launch.

Author-reported scores differ by model and were not rerun: the paper
abstract says 88.2% of 110 tasks with Claude 3.5 Sonnet, and the README
says 100% of FoamBench's 110 tasks with Claude Opus 4.6. A later reader
has to keep those rows apart.

`run` is described as local Allrun. Gmsh, custom meshes, and HPC
routing are described as the CLI graph, not as that one MCP tool.

## Drawings, GD&T, and CAM

text-to-cad `engineering-drawing` writes a PDF from a build123d solid.
Tolerances on that sheet are the numbers the script passes in `tol=`,
`fit=`, or `general_tolerance=`. The skill does not describe a feature
control frame, a datum feature symbol checker, or a check that the
tolerance is the one the design required. It tells the caller to supply
those values. Sections and auxiliary views are named as absent.

FreeCAD's documentation index lists TechDraw Geometric dimensioning and
tolerancing. The article body was not fetched. Until it is, that title
is evidence the workbench has a GD&T page, not a list of symbols or a
pass rule.

Fusion community MCP `docs/TOOLS.md` names the CAM tools in
[mechanical](../catalog/mechanical.md). `cam_post_process` needs a
`.cps` file path. The README says cloud-post builds do not ship local
posts. Which post matches which machine is a Fusion library question.
The Autodesk post-library help page exists and was not transcribed.

SolidCraft `expect` is a numeric check on a solid (volume, body count,
bounding box), documented in `docs/mcp.md`. It is not a GD&T check and
not a toolpath check.

## Control and power

Three separate interfaces, not one closed loop.

Small-signal AC in ngspice, manual section 11.3.1, fetched from
<https://ngspice.sourceforge.io/docs/ngspice-html-manual/manual.xhtml>:

```text
.ac dec nd fstart fstop
.ac oct no fstart fstop
.ac lin np fstart fstop
```

`dec` is points per decade. The manual's example is `.ac dec 10 1 10K`.
That statement is the analysis card. It does not by itself print gain
margin or phase margin.

python-control 0.10.2 documents `control.margin` as "Gain and phase
margins and associated crossover frequencies," called as `margin(sys)`
for a SISO linear system or as `margin(mag, phase, omega)`. Page:
<https://python-control.readthedocs.io/en/0.10.2/generated/control.margin.html>.
The library was not imported. Feeding it an ngspice frequency sweep
requires an export step this survey did not specify, because neither
manual shows that adapter.

ltspice-mcp's README already names phase margin as a measurement it
can return from a simulator run. The acceptable margin is still a
design limit. The README does not set one.

atopile 0.16.15's validator includes IPC-2221 clearance by voltage.
That is a board-geometry rule, not a control-loop margin.

No repository opened in this pass closes magnetics design, compensator
coefficients, and firmware on one bench. PlatformIO's documented
`flash` and `monitor` commands are the firmware side, and they act on
a connected board. No board was used.
