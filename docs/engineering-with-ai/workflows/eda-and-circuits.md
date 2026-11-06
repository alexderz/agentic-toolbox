# EDA and circuits

Documented checks for schematic, board, SPICE, and HDL work. Not
executed on 2026-11-06. Command text matches the KiCad manuals cited
in [evaluation](evaluation.md).

## Schematic and board

Three file-producing routes are recorded. They do not share a project
format.

| Route | Source of truth | Check the docs name |
| --- | --- | --- |
| KiCad files through an MCP server | `.kicad_sch` and `.kicad_pcb` | `kicad-cli sch erc` and `kicad-cli pcb drc` |
| SKiDL Python | A Python circuit and a generated netlist | ERC after import into KiCad, or Circuitron's claimed ERC loop. Circuitron's README was not opened |
| atopile `.ato` | atopile source | The 0.16.15 validator: manufacturing rules, shorts, opens, 3D overlaps, voltage clearance |
| tscircuit TSX | TypeScript components | A fabrication-file check was not on the pages read |
| JITX Python | JITX source | Skills exist. The compiler's check command was not copied. License is proprietary |

KiCad MCP skill text from ProductOfAmerica tells the agent not to
rewrite KiCad files as plain text and not to shell out to `kicad-cli`,
and to call MCP tools instead. That is that skill's rule. The CLI
manual is still the documented non-interactive checker, and a review
run can call it on the files the MCP tools wrote. Whether a given MCP
server's ERC matches `kicad-cli` was not compared.

Exit codes, KiCad 9 and 10 manuals: 0 means no violations, 5 means
violations, when `--exit-code-violations` is set. Write JSON with
`--format json` if a later script must parse the report.

KiCad 10 DRC can refill zones before the check (`--refill-zones`) and
can save the board (`--save-board`). Those flags change the file.
A read-only check omits `--save-board`.

## SPICE

AnalogCoder's published loop:

1. The model writes PySpice.
2. ngspice simulates it.
3. Failures go back into the prompt.
4. A design that meets the paper's tests can be stored as a subcircuit.

Dependencies stated in that repository: Python 3.10 or newer, PySpice
1.5 or newer, ngspice, and an OpenAI client. The loop uses a remote
model API.

ltspice-mcp is a different interface: it edits `.asc` when LTspice is
available and can simulate with ngspice alone. It returns named
measurements. The acceptable numeric range is a design spec. The README
does not set one.

circuit-sim-mcp exposes DC, AC, and transient tools over PySpice. It
has no license file in the API result and 1 star. The author's platform
note is macOS ARM64 and ngspice 44.

AnalogGenie generates a topology graph. A graph is not a netlist until
a second step assigns devices and parameters and a simulator runs.
That second step is not in the pages read as a single command.

## HDL

VerilogEval's check is simulation against a golden waveform, not a
visual read of the Verilog. The repository is `NVlabs/verilog-eval`,
MIT text in the license file. The 2025 revisit reports pass rates for
named models. Those rates are not reproduced here, and they move when
the prompt changes. The paper says that directly.

RTLCoder is a local 7B specialist for the same kind of task. Size
evidence is in [models](../catalog/models.md). The repository has no
license file. Using the weights needs a license decision this survey
does not make.

OpenROAD script generation is a different task from RTL generation.
EDA Corpus supplies prompt and script pairs under CC-BY-4.0. OpenROAD
Agent's abstract reports 94% on its script tasks and says the model is
open. The download URL was not opened.

Place-and-route CLIs (Yosys, nextpnr, OpenROAD's own shell) were not
copied. See open question G14.

## Embedded

`jl-codes/platformio-mcp` documents `build`, `flash`, and `monitor`,
plus the `agent_*` tools listed in [electrical](../catalog/electrical.md).
The README says approval of risky operations stays with a person. No
board was flashed. `powerdragonfire/platformio.mcp` was not read.

## Instruments

`abhinav937/pyvisa-mcp` lists the tools in the electrical catalog.
Writes are allowed for the dialects the README names, and blocked for
other identities until `unlock_writes` with `confirm=true`. This survey
did not send SCPI and did not open an instrument.
