# Open questions

Status after the 2026-11-06 refinement. Closed rows stay here so a
later edit can see what was answered. A closed row's evidence is in
the linked page.

| ID | Status | Question | Where it stands |
| --- | --- | --- | --- |
| G1 | partial | text-to-cad drawing and CAD skills | `engineering-drawing` and the `cad` skill were read. PDF, third-angle views, `tol` and `fit`, STEP/STL/3MF/GLB/xbf exports. `gcode`, `dfm`, `urdf`, `srdf`, and `sdf` bodies were not |
| G2 | closed | SolidCraft MCP tools and formats | `docs/mcp.md`: tool names, STEP/3MF/STL/OBJ/URDF, read versus write. Live command catalog is `list_commands`, about 350 KB, and was not dumped |
| G8 | closed | STEP-LLM code and weights | <https://github.com/JasonShiii/STEP-LLM> exists, MIT, 35 stars. Released artifacts are LoRA adapters. Qwen adapter file is 119,801,528 bytes. Full merged weights were not in the repo. Runtime memory unknown |
| G11 | closed | Fusion community CAM tools | `docs/TOOLS.md` lists setup, operation, toolpath, and post. Post needs a `.cps` path. Official Fusion MCP tool list is still dynamic |
| G12 | closed | Foam-Agent repository | <https://github.com/csml-rpi/Foam-Agent>, MIT, `v2.2.0`, OpenFOAM v10 and ESI v2006, seven MCP tools. Two author-reported success rates, not rerun |
| G14 | closed | FPGA and OpenROAD CLIs | Yosys 0.70, nextpnr 0.11.1, ORFS `make` line. No agent skill for those CLIs was opened |
| G16 | closed | platformio-mcp | README documents build, flash, monitor, and the `agent_*` tools. Approval stays with a person. Not run |
| G17 | closed | pyvisa-mcp | Tool table read. Known-scope dialects may be written. Others need `unlock_writes`. No instrument was opened |
| G18 | closed | KiCad MCP Pro skill copies | Seven workflow names are five identical blobs each. Four other skill names exist once |
| G19 | closed | mcp-server-kicad maintenance | README: maintenance mode as of October 2026, KiCad 9 or 10, and a recommendation to use `kicad-cli`. The skill file still forbids `kicad-cli`. The 18-edit comparison is the author's, on an unpublished board |
| G20 | closed | Konnect archive | README says the repo is read-only and points at `Orchis-ai-LLC/Konnect-EDA`, described there as commercial and closed source, free during beta. Archived tree stays AGPL-3.0 per that README |
| G21 | closed | 24 GB coding and VL checkpoints | Official Qwen file sizes are in [models](catalog/models.md). Every listed file is under 24 GiB. Runtime peaks were not measured, so a fit is not claimed |
| G10 | partial | GD&T verification | Drawing skill records numeric `tol` and `fit` only. FreeCAD TechDraw GD&T page title is listed. Page body was not retrieved. No symbol checker was found |
| G15 | partial | Power and control | ngspice `.ac`, python-control `margin`, ltspice-mcp phase margin, and atopile clearance are documented separately. Magnetics plus compensator plus firmware was not found as one artifact |
| G3 | open | Fusion license tier for the local MCP | Help page still does not name a tier |
| G4 | open | Onshape FeatureScript MCP tool schema | Official posts still do not publish a fixed tool list |
| G5 | open | Where the Zoo kernel runs | Unstated on the pages read |
| G6 | open | KCL and Zoo engine license | Unstated on the pages read |
| G7 | open | OmniMech public release | Paper still says it will be released. No repository confirmed |
| G9 | open | AutoSiMP and LLM-SIMP code | Papers still defer the code. No repository was found on this pass |
| G13 | open | CAE-Agent-Hub commercial solver licenses and independent runs | README table unchanged. No third-party run log was opened |
| G22 | open | CADGenBench rows after 2026-11-06 | Snapshot stands. Board is live |
| G23 | open | Independent reproduction of published scores | Still not run, on purpose |
| G24 | open | gitcad and NativeCAD | Not built |
| G25 | open | Amagine3D and Multi-Agent CAD kernels | READMEs still not opened |
