# Electrical catalog

Snapshot 2026-11-06. Class labels match [method](../method.md).

## KiCad and board files

### KiCad CLI

| Field | Value |
| --- | --- |
| URL | <https://docs.kicad.org/10.0/en/cli/cli.html> and the 9.0 manual at <https://docs.kicad.org/9.0/en/cli/cli.html> |
| Capabilities | `kicad-cli sch erc` writes an electrical-rule report. `kicad-cli pcb drc` writes a design-rule report. Both manuals: `--format report` or `json`, and `--exit-code-violations` returns 0 when no violations are found and 5 when any are found. KiCad 10 DRC also documents `--refill-zones` and `--save-board`. The 9.0 page fetched does not list those two flags |
| Maturity | Manuals for 10.0 and 9.0, fetched 2026-11-06. Installed KiCad version in this environment was not queried |
| License | KiCad's license was not re-read. The manuals are the project docs |
| Dependencies | `kicad-cli` on `PATH` |
| Formats | Input `.kicad_sch` or board file. Output `.rpt` or `.json`. Other export subcommands exist in the same manuals and were not copied |
| Read/write | Reads the design and writes a report. `--save-board` on KiCad 10 DRC can write the board |
| Mode | Local CLI |
| Evidence | `official-doc`. Commands not run |
| Class | tool-driver |

### mcp-server-kicad

| Field | Value |
| --- | --- |
| URL | <https://github.com/ProductOfAmerica/mcp-server-kicad> |
| Capabilities | Description: maintenance mode, security and KiCad compatibility fixes only. Skill text fetched for `skills/using-kicad/SKILL.md` says 109 tools and forbids direct edits of `.kicad_sch`, `.kicad_pcb`, and related files. Tree has 6 `SKILL.md` files. Catalog names in that skill: `circuit-design`, `schematic-plan`, `schematic-design`, `pcb-layout`, `verification` |
| Maturity | `pushed_at` 2026-11-05. Created 2026-03-09. 16 stars. PyPI project linked: `mcp-server-kicad` |
| License | GPL-3.0 |
| Dependencies | KiCad, from the skill text. Version floor unknown |
| Formats | KiCad schematic, board, Gerber, BOM, IPC-2581, named in the skill's tool list |
| Read/write | Skill requires MCP writes. ERC, DRC, and exports are reads |
| Mode | Local MCP |
| Evidence | `github-api`, one skill file, `git-tree`. Not run (G19) |
| Class | tool-driver |

### kicad-mcp-pro

| Field | Value |
| --- | --- |
| URL | <https://github.com/oaslananka/kicad-mcp-pro> |
| Capabilities | Description: schematic and PCB workflows, ERC/DRC, DFM, BOM, manufacturing preparation. Canonical names under `skills/`: `drc-check`, `fabrication-output`, `kicad-design-review`, `pcb-design`, `schematic-review`, `visual-excellence`, `wired-subcircuit-design`. Git tree contains 39 `SKILL.md` paths because those names are copied for Claude, OpenCode, Gemini, Cursor, and package data |
| Maturity | Latest release tag `kicad-mcp-gui-v4.7.0`, published 2026-11-04. `pushed_at` 2026-11-06. 182 stars. Created 2026-05-31 |
| License | MIT |
| Dependencies | KiCad. Version not taken from the README |
| Formats | Named at the description level: schematic, PCB, fabrication outputs. Exact exporter list not copied |
| Read/write | Description says controlled edits and human-gated release workflows |
| Mode | Local MCP. Example configs exist for Codex, VS Code, and OpenCode. Not opened in full |
| Evidence | `github-api`, `git-tree`, repository page excerpt |
| Class | tool-driver |

### KiCAD-MCP-Server and Konnect

| Repo | API | License | What was read |
| --- | --- | --- | --- |
| <https://github.com/mixelpixx/KiCAD-MCP-Server> | 3,174 stars, `pushed_at` 2026-11-04, created 2025-04-26 | MIT | Page excerpt: MCP server for schematic and PCB actions, symbols, footprints, routing, checks, production files. Tool inventory not counted |
| <https://github.com/mixelpixx/Konnect> | 1,453 stars, `pushed_at` 2026-11-02, created 2026-07-05, `archived` true | AGPL-3.0 | Description: KiCad 10 plugin, one Rust binary, 217 tools. 6 `SKILL.md` files. Archive flag and later push are both API fields (G20). Skill excerpt says KiCad files are not to be edited as text |

## Code-defined electronics

### SKiDL

| Field | Value |
| --- | --- |
| URL | <https://github.com/devbisme/skidl> and <https://devbisme.github.io/skidl/> |
| Capabilities | Description: design circuits in Python. Third-party page lists `nickkraakman/skidl-skills` and Circuitron. A GitHub discussion proposes simulation ERC and a layout package. That discussion is a proposal, not a merged release note |
| Maturity | `pushed_at` 2026-10-17. 1,717 stars. Created 2016-08-16 |
| License | MIT |
| Dependencies | Python. KiCad libraries are the usual footprint source. Version coupling not rechecked |
| Formats | Netlist and, per project docs not fully reread, KiCad schematic output. Treat schematic generation as README-dependent |
| Read/write | Python writes a netlist |
| Mode | Local library |
| Evidence | `github-api`, third-party tools page |
| Class | tool-driver |

### skidl-skills

| Field | Value |
| --- | --- |
| URL | <https://github.com/nickkraakman/skidl-skills> |
| Capabilities | Description: agentic KiCad PCB workflow for SKiDL. 4 `SKILL.md` files. Bodies not read |
| Maturity | `pushed_at` 2026-04-08. Created 2026-04-07. 24 stars |
| License | MIT |
| Dependencies | SKiDL and KiCad, from the description |
| Formats | unknown beyond KiCad netlists |
| Read/write | unknown |
| Mode | Local skill files |
| Evidence | `github-api`, `git-tree` |
| Class | tool-driver |

### Circuitron

| Field | Value |
| --- | --- |
| URL | <https://github.com/Shaurya-Sethi/circuitron> |
| Capabilities | Description: natural language to PCB designs using SKiDL. SKiDL third-party page: OpenAI Agents SDK, schematic, netlist, SVG, KiCad PCB, iterate until ERC passes. README not opened |
| Maturity | `pushed_at` 2026-06-06. Created 2025-06-12. 129 stars |
| License | MIT |
| Dependencies | As the third-party page states. Not verified against the README |
| Formats | Named on that page |
| Read/write | Generates design files, per that page |
| Mode | Local project plus a hosted model API, if the third-party page is accurate |
| Evidence | `github-api` and SKiDL third-party page. README unread |
| Class | tool-driver |

### atopile

| Field | Value |
| --- | --- |
| URL | <https://github.com/atopile/atopile> and <https://atopile.io/blog/atopile-0-16-15> |
| Capabilities | Blog 2026-10-13 for version 0.16.15: agent places and routes, each build runs a validator. Checks named: 15 manufacturing rule types, shorts, opens, 3D body intersections, insulation versus voltage, IPC-2221 clearance by voltage, floating copper, courtyard overlaps. Also parametric footprints, variant `@if`, and external MCP connections. An earlier blog sentence says a filmed layout run took 24 minutes. That is the vendor's timing |
| Maturity | GitHub latest release `v0.12.5`, published 2026-01-20. `pushed_at` 2026-10-14. 4,042 stars. The 0.16.15 identifier is from the blog, not from the GitHub latest-release object |
| License | MIT (`github-api`) |
| Dependencies | atopile compiler and its IDE or CLI. Not installed |
| Formats | `.ato` source. Manufacturing outputs not listed in the excerpt |
| Read/write | Agent edits source. Validator reads the build |
| Mode | Local toolchain. Vendor cloud, if any, not stated in the excerpt |
| Evidence | `github-api` and vendor blog |
| Class | tool-driver |

### tscircuit

| Field | Value |
| --- | --- |
| URL | <https://github.com/tscircuit/tscircuit> and <https://tscircuit.com/> |
| Capabilities | Site: TypeScript/React (TSX) circuits, components, connections, layout constraints. Packages named: `@tscircuit/core`, `@tscircuit/eval`, `@tscircuit/runframe`. Site says agents can be told to use tscircuit and that a CLI skill exists. Skill repository path on that site was not opened |
| Maturity | `pushed_at` 2026-11-06. Created 2024-03-14. 2,946 stars. Latest GitHub release API returned 404 |
| License | MIT |
| Dependencies | Node, Bun, or browser, per the package list on the site |
| Formats | Circuit JSON named. Gerber and other fabrication outputs unknown on the pages read |
| Read/write | Code writes a circuit description |
| Mode | Local libraries |
| Evidence | `github-api` and product site. "State of the art" sentence on the site is a vendor claim, not a result reproduced here |
| Class | tool-driver |

### JITX skills

| Field | Value |
| --- | --- |
| URL | <https://github.com/JITx-Inc/jitx-skills> |
| Capabilities | README excerpt: skills for Claude Code and Codex. Names from the git tree: `jitx`, `jitx-component-modeler`, `jitx-circuit-builder`, `jitx-physical-layout`, `jitx-pin-assignment`, `jitx-layout-constraints`, `jitx-interconnect-constraints`, `jitx-mechanical`, `jitx-substrate-modeler`, `jitx-project-builder`, `jitx-code-review`. README examples: datasheet to component, wiring, code-based copper |
| Maturity | `pushed_at` 2026-11-05. Created 2026-01-29. 20 stars |
| License | License file: proprietary, all rights reserved, no license except a separate written agreement. Points at <https://www.jitx.com/legal/tos>. GitHub SPDX `NOASSERTION` |
| Dependencies | JITX product. Terms not copied |
| Formats | JITX Python, from the README examples |
| Read/write | Skills author components, circuits, and layout |
| Mode | Skills are local files. The JITX compiler location was not read |
| Evidence | `readme` excerpt, `license-file`, `git-tree` |
| Class | tool-driver |

### SchGen dataset

Hugging Face `microsoft/SchGen_dataset`: 8,420 pairs of natural-language requests and Python schematic code that the card says can be rendered to KiCad. Construction note on the card: GPT-5 drafts, human correction, then requests synthesized from the schematic. Research dataset, not a tool. See [papers](papers.md).

## SPICE and analog

### AnalogCoder

| Field | Value |
| --- | --- |
| URL | <https://github.com/laiyao1/AnalogCoder> |
| Capabilities | README: training-free agent. Designs analog circuits as Python with PySpice. Feedback loop and a library of successful subcircuits. Backend ngspice |
| Maturity | `pushed_at` 2026-09-12. 211 stars. Paper: AAAI 2025 oral. DOI <https://doi.org/10.1609/aaai.v39i1.32016> |
| License | MIT |
| Dependencies | README: Python 3.10 or newer, PySpice 1.5 or newer, `openai` 1.16.1 or newer, ngspice |
| Formats | PySpice source and SPICE netlists |
| Read/write | Generates code and reads simulator output |
| Mode | Local simulator, remote LLM API |
| Evidence | `readme`, `github-api`, paper abstract |
| Class | tool-driver (the LLM is general; the loop is domain-specific) |

Author-reported abstract result: 20 circuits designed, 5 more than the paper's GPT-4o baseline. Not rerun (G23).

### ltspice-mcp

| Field | Value |
| --- | --- |
| URL | <https://github.com/Cognitohazard/ltspice-mcp> |
| Capabilities | README: run LTspice and ngspice, edit `.asc` schematics, return named measurements (cutoff, overshoot, phase margin, rise time, `gm`, `gds`, `vth`). Built on spicelib. Version 0.6.0 merged tools. QSPICE and Xyce are secondary, netlists only |
| Maturity | `pushed_at` 2026-11-06. Created 2026-03-02. 68 stars. No GitHub latest-release object |
| License | GPL-3.0 |
| Dependencies | LTspice for `.asc` editing (Windows, WSL2, or Linux via Wine, per README). ngspice for simulation without LTspice |
| Formats | LTspice `.asc`, netlists, simulator raw output |
| Read/write | Reads and writes schematics. Runs simulations |
| Mode | Local |
| Evidence | README excerpt and `github-api`. Not run |
| Class | tool-driver |

### circuit-sim-mcp

| Field | Value |
| --- | --- |
| URL | <https://github.com/ghensley/circuit-sim-mcp> |
| Capabilities | README: PySpice tools for create, validate, DC, AC, transient, plot, export. Author states tests on macOS ARM64 with Homebrew ngspice 44 |
| Maturity | `pushed_at` 2025-07-11. Created 2025-07-09. 1 star |
| License | none detected |
| Dependencies | PySpice, ngspice |
| Formats | JSON, CSV, TXT export named |
| Read/write | Creates circuits in the server process and reads simulation results |
| Mode | Local MCP |
| Evidence | README excerpt and `github-api` |
| Class | tool-driver |

### AnalogGenie

Specialist graph generator. Paper only. See [papers](papers.md).

## HDL, FPGA, and OpenROAD

Specialist and benchmark entries are in [papers](papers.md) and [models](models.md): VerilogEval, RTLCoder, EDA Corpus, OpenROAD Agent.

`Thinklab-SJTU/Awesome-LLM4EDA` has 300 stars, no license file detected, `pushed_at` 2024-07-08. It is an index, last updated well before this survey. Entries after that date are not in that list.

Yosys, nextpnr, Amaranth, and cocotb agent skills were not opened (G14). Their use as checkers is still valid as ordinary tools. This pass did not document their CLIs.

## Embedded and instruments

### platformio-mcp

| Field | Value |
| --- | --- |
| URL | <https://github.com/jl-codes/platformio-mcp> |
| Capabilities | unknown. API description is empty. Several alias repositories point at this one and were not opened |
| Maturity | `pushed_at` 2026-10-13. Created 2026-01-10. 54 stars |
| License | MIT |
| Dependencies | PlatformIO, presumed from the name. Not confirmed in a README |
| Formats | unknown |
| Read/write | unknown (G16) |
| Mode | unknown |
| Evidence | `github-api` only |
| Class | tool-driver if the README matches the name |

A second repository, `powerdragonfire/platformio.mcp`, has the description "build, flash, serial monitor, tests, crash decoding, size reports" and 6 stars, updated 2026-11-04. README not opened.

### pyvisa-mcp

| Field | Value |
| --- | --- |
| URL | <https://github.com/abhinav937/pyvisa-mcp> |
| Capabilities | API description: discover and control oscilloscopes and other VISA instruments over LAN, USB, GPIB, and serial. README body not opened |
| Maturity | `pushed_at` 2026-09-13. Created 2026-09-12. 1 star |
| License | MIT |
| Dependencies | PyVISA and a VISA backend, not confirmed |
| Formats | unknown |
| Read/write | Description says control, which includes writes to instruments. Scope unknown (G17) |
| Mode | Local MCP, instruments on the host's buses |
| Evidence | `github-api` |
| Class | tool-driver |

No instrument session was opened. No SCPI script was written.
