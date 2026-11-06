# Evaluation criteria

Checks below are copied from a tool's own documentation or from a
benchmark README. None of them was executed on 2026-11-06. A later run
can mark a row pass or fail only after the command or scorer runs.

## Mechanical solids

| Check | Source | Pass condition the source states | Fail |
| --- | --- | --- | --- |
| STEP validity gate | CADGenBench README | BREP is well-formed and watertight, and meshes to a closed manifold | Any validity failure zeroes shape, interface, and topology scores |
| Shape similarity | CADGenBench README | Surface-distance F1 and volume IoU against private ground truth | Defined only when ground truth is available. Local runs without the private set cannot compute the leaderboard score |
| Interface match | CADGenBench README | Keep-in and keep-out sub-volumes for mating features | Same ground-truth limit |
| Topology match | CADGenBench README | Betti numbers b0, b1, b2 of the tessellated boundary | Same |
| Script execution | CADGenBench baseline description | The Python program (build123d or CadQuery) runs and writes `output.step` or `output.stp` | Non-zero interpreter or kernel error, or missing file |
| Sketch constraints | theosib FreeCAD MCP README | `get_sketch_diagnostics` reports degrees of freedom, conflicts, and redundancies | A conflict or a non-zero degree of freedom when the design intent was a fully constrained sketch. The numeric target depends on the sketch |
| Interference | Fusion community MCP README and OpenSCAD MCP README | A named interference or clearance tool returns the overlap | Tool-specific. Thresholds are design requirements, not a universal constant |
| Mass properties | Zoo Zookeeper page | Center of mass, mass, area, and volume from the engine | Units and material density must be the ones the engine used. Those defaults were not copied |

CADGenBench also ships `sanity_check_submission.py` with the public
inputs so a candidate can be checked against the validity gate before
upload. The leaderboard score still needs the Space, because ground
truth is private.

## Drawings and GD&T

No checker with a published pass rule was opened. OmniMech describes
annotation-grounded constraints and says current models do poorly.
That is a paper result, not a local command. text-to-cad has an
`engineering-drawing` skill path. Its pass rule was not read.

## CAM and manufacturing

| Check | Source | What a later run can record |
| --- | --- | --- |
| DFM rule list | atopile 0.16.15 blog, for boards | Shorts, opens, body intersections, clearance, track width, and the other rule types the blog names. Mechanical DFM is a different skill path (`dfm` in text-to-cad) and was not read |
| CAM job creation | Fusion community MCP README | Whether `cam_create_setup` and `cam_post_process` return a toolpath file. G-code correctness against a machine was not specified by that README |

## Schematic and PCB

From the KiCad 10.0 CLI manual, and the same exit-code sentence in the
9.0 manual.

Schematic ERC:

```text
kicad-cli sch erc --format json --severity-all --exit-code-violations INPUT.kicad_sch
```

Board DRC:

```text
kicad-cli pcb drc --format json --severity-all --exit-code-violations INPUT.kicad_pcb
```

| Exit code | Meaning in both manuals |
| --- | --- |
| 0 | No violations found |
| 5 | Any violation found |

KiCad 10 additionally documents `--refill-zones` and `--save-board` on
`pcb drc`. The 9.0 page that was fetched does not. Use the manual that
matches the installed `kicad-cli`.

Schematic parity is a separate flag, `--schematic-parity`, on `pcb drc`.
It checks the board against the schematic. It is not a substitute for
ERC.

atopile's blog lists a second validator (manufacturing, physical, and
design defaults, including IPC-2221 clearance by voltage). That
validator is atopile's, not KiCad's. A design that passes one can still
fail the other. Both were not run.

## SPICE

| Check | Source | Pass condition |
| --- | --- | --- |
| Netlist runs | AnalogCoder README and paper | PySpice drives ngspice. A run that does not start is a failure |
| Named measurements | ltspice-mcp README | The server returns the requested name, such as phase margin or rise time. The numeric limit is the design spec, which the README does not fix |
| DC, AC, transient | circuit-sim-mcp README | Each analysis returns data. Author claims this on one macOS machine with ngspice 44 |

AnalogCoder's "20 circuits" count is the paper's score on its own task
list. It is not a general SPICE pass rate.

## HDL

| Check | Source | Pass condition |
| --- | --- | --- |
| Functional simulation | VerilogEval paper | Transient outputs match the golden solution on that problem |
| Specification-to-RTL | VerilogEval revisit | Same style of pass rate on the added task split. The paper says prompt choice changes the rate |

Syntax-only acceptance is a weaker check. The VerilogEval papers use
simulation. A Yosys read or a Verilator build was not documented in
this pass (G14). Those tools can still be used as extra checks. Their
command lines are not copied here because the manuals were not opened.

## Embedded and instruments

| Check | Source | Pass condition the source states |
| --- | --- | --- |
| Firmware build | platformio-mcp README | `pio-agent build` or `platformio-mcp build` exits successfully. `--json` is the machine-readable form. Exit-code table was not copied |
| Flash and serial | same README | `flash` and `monitor` are separate commands. `monitor` can take `--expect`. A board is required. None was used |
| Scope identity | pyvisa-mcp README | `open_instrument` then `learn_instrument` stores `*IDN?`. Writes stay off until the dialect is one the README allows, or `unlock_writes confirm=true` |

## What not to treat as a pass

- The model says the part or the board is finished.
- A render looks right, unless the metric is explicitly visual and the
  scorer is the one in the paper.
- A KiCad or STEP file exists but the validity, ERC, or DRC command
  was not run.
- A leaderboard row, unless the submission id and the dataset revision
  are cited and the score was not hand-edited.
