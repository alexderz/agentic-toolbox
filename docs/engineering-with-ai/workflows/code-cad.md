# Code to CAD

Documented loop for a local solid. Not executed on 2026-11-06.

## When this is the matching stack

Use it when the artifact is a STEP file and the generator may be any
coding model. CADGenBench's baseline is this loop: write build123d or
CadQuery, export STEP, repeat while the file is invalid.

build123d `v0.13.0` (published 2026-09-21) and CadQuery `2.8.0`
(published 2026-06-20) are the releases recorded in
[mechanical](../catalog/mechanical.md). CADGenBench requires Python
3.12 or newer for its own package.

## Steps the sources already separate

1. Write a Python script that builds one solid in build123d or
   CadQuery. The text-to-cad README uses `python model.py` and a local
   server that also writes STEP. The CADGenBench baseline writes
   `output.step` directly. These are two different runners. Do not mix
   their file layouts.
2. Run the script. A non-zero exit or an Open CASCADE exception is a
   failed generation, before any geometric score.
3. Confirm the STEP file exists.
4. Run a validity check. CADGenBench's gate is a well-formed watertight
   BREP that meshes to a closed manifold. The public inputs ship
   `sanity_check_submission.py` for that gate. The leaderboard's shape,
   interface, and topology scores need the private ground truth and the
   Space.
5. If the task is an edit, start from the given STEP and apply the
   requested change. CADGenBench editing tasks are 32 of the 81
   fixtures. Generation tasks are the other 49 and start from a drawing.

## Assembly and constraints

A solid that passes the validity gate can still be the wrong part.
Sources that add a second check:

- FreeCAD sketch diagnostics in `theosib/FreeCAD-MCP-Server`: degrees
  of freedom, conflicts, redundancies. That server's README requires
  FreeCAD to be running.
- Interference tools named by the Fusion community MCP and by
  OpenSCAD MCP. OpenSCAD output is a mesh, so it does not satisfy a
  STEP-only contract.
- Zoo Zookeeper's mass, area, volume, and center of mass, inside Zoo
  Design Studio, on KCL geometry rather than on a local STEP kernel.

None of these was wired together in this survey.

## Drawings

`skills/engineering-drawing/SKILL.md` was read. It writes one PDF from
a build123d shape: third-angle top, front, and right, plus an isometric
when requested, with hole callouts and numeric `tol=` or `fit=`. It
states that sections, detail views, and auxiliary views are absent, and
that a dimension without a tolerance argument is nominal. It does not
describe a GD&T feature-control frame. OmniMech remains a paper
benchmark whose data release was not confirmed.

## CAM

A STEP file is the input to CAM, not a toolpath. Fusion community
`docs/TOOLS.md` names `cam_create_setup`, `cam_create_operation`,
`cam_generate_toolpath`, and `cam_post_process`. Post-process requires
a full `.cps` path. The text-to-cad `gcode` skill body is still unread,
so this page does not state a post processor from that skill.

## Specialist models on the same artifact

| Model | Output | Extra step the kernel still has to do |
| --- | --- | --- |
| Text2CAD | CAD command sequence | Rebuild the sequence in a kernel that understands that sequence. The paper uses the DeepCAD representation |
| CAD-Recode | CadQuery Python | Execute it. The license on the weights is CC BY-NC 4.0 |
| BrepGen | B-rep sample | Load the sample. License file forbids commercial use |
| STEP-LLM | STEP text from a LoRA adapter on Llama-3.2-3B-Instruct or Qwen2.5-3B | Parse as STEP. Full merged weights are not in the release. The Qwen adapter file is 119,801,528 bytes |

A tool-driver that writes build123d and a specialist that emits a
sequence can be compared only after both produce a solid the same
checker can read. CADGenBench is one such checker for STEP, and only
for its 81 fixtures.
