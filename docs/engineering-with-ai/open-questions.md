# Open questions

Left open on 2026-11-06. A later pass can close a row by filling the
source column and moving the result into the matching catalog page.

| ID | Question | Why it is open |
| --- | --- | --- |
| G1 | What does each text-to-cad skill body require of build123d, and which checks does `engineering-drawing` actually emit? | Paths were listed from the git tree. Skill bodies were not read |
| G2 | Does SolidCraft's MCP expose a stable tool list, and which formats does `solidcraft-cli mcp` read and write? | README and release `v0.30.1` were fetched. Tool schema was not |
| G3 | Which Fusion license tiers enable the local MCP server? | Fusion help requires the desktop app and the preference toggle. Tier is unstated there |
| G4 | What is the fixed tool list for Onshape FeatureScript MCP? | Official posts describe generate, run, and revise FeatureScript. A schema file was not downloaded |
| G5 | Where does the Zoo geometry kernel execute, local or vendor cloud? | Agent API page describes a web interface. Execution location was not stated on the pages read |
| G6 | What license covers KCL the language, the Zoo CLI, and the engine? | Not stated on the Zoo pages opened |
| G7 | Are OmniMech's 251,000 drawings and the evaluation code public? | The paper says they will be released. A repository was not found in this pass |
| G8 | Are STEP-LLM weights public, and what is the checkpoint size? | Paper fetched. Artifact URL not confirmed |
| G9 | AutoSiMP and the LLM-SIMP controller both defer code. Did either repository appear after the HTML versions read here? | Papers say release is on acceptance or publication. Not rechecked beyond those HTML pages |
| G10 | What GD&T callouts can a checker verify, as distinct from drawing text? | No GD&T verification tool was read end to end |
| G11 | What CAM operation types and post processors do the Fusion MCP tools support? | Community README names `cam_create_setup`, `cam_create_operation`, `cam_post_process`. Post list unknown. Official Fusion MCP tool list is dynamic |
| G12 | Foam-Agent's MCP tools: repository, license, and OpenFOAM version | Paper HTML describes an MCP design. GitHub search for `foam-agent openfoam` returned no repository |
| G13 | CAE-Agent-Hub solvers: which commercial licenses are required at runtime, and which profiles were executed by someone other than the author? | README table lists Abaqus, Fluent, Workbench, AEDT, HyperWorks, CalculiX, Elmer, ParaView. Independent runs unknown |
| G14 | FPGA flow agents for Yosys, nextpnr, and OpenROAD beyond the EDA Corpus and OpenROAD Agent abstract | Awesome-LLM4EDA was last pushed 2024-07-08. Individual flow repos were not opened |
| G15 | Power electronics and control: bode, loop stability, magnetics, and firmware co-design | AnalogGenie discusses converters. atopile 0.16.15 blog lists IPC-2221 clearance by voltage. No control-design repository was opened |
| G16 | `jl-codes/platformio-mcp` tool list and whether flash or serial is in scope | Description was empty in the API. README not opened |
| G17 | `abhinav937/pyvisa-mcp`: which instrument classes and transports the README claims, and whether it writes instrument state | API description names discovery and control over LAN, USB, GPIB, and serial. README body not opened. 1 star |
| G18 | KiCad MCP Pro: which of the 7 `skills/` names are the canonical set versus generated copies | Tree shows repeated copies under `.agents`, `.opencode`, Gemini, and `src/`. Behavior not compared |
| G19 | Does ProductOfAmerica `mcp-server-kicad` still match its skill text after the README maintenance-mode notice? | Description says security and KiCad compatibility fixes only. Tool behavior not run |
| G20 | Konnect archive state | API `archived` is true and `pushed_at` is 2026-11-02. Whether the archive blocks new use was not tested |
| G21 | General coding models that fit a 24 GB GPU or a CPU-only machine for these workflows | No general-model card was measured here. See [models](catalog/models.md) |
| G22 | CADGenBench leaderboard rows after 2026-11-06 | Dataset viewer rows from that day are a snapshot. The Space is the live board |
| G23 | Independent reproduction of VerilogEval, RTLCoder, AnalogCoder, Text2CAD, and CADGenBench numbers | All figures in [papers](catalog/papers.md) are author-reported or leaderboard rows. None were rerun |
| G24 | `gitcad` and NativeCAD claims | gitcad has 2 stars. NativeCAD was a vendor page. Neither was built |
| G25 | Amagine3D and Multi-Agent CAD: what kernel and which benchmark | API metadata only. READMEs not opened |
