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

text-to-cad lists `skills/engineering-drawing/SKILL.md`. The body was
not read, so this page does not state which views or GD&T symbols it
emits. OmniMech is a paper benchmark for dimensioned drawings, and its
data was not public on the HTML that was read.

## CAM

A STEP file is the input to CAM, not a toolpath. The Fusion community
MCP README names setup, operation, and post tools. text-to-cad lists a
`gcode` skill. Neither path was read far enough to state a post
processor or a stock setup. Record those as unknown until the tool
schema is opened.

## Specialist models on the same artifact

| Model | Output | Extra step the kernel still has to do |
| --- | --- | --- |
| Text2CAD | CAD command sequence | Rebuild the sequence in a kernel that understands that sequence. The paper uses the DeepCAD representation |
| CAD-Recode | CadQuery Python | Execute it. The license on the weights is CC BY-NC 4.0 |
| BrepGen | B-rep sample | Load the sample. License file forbids commercial use |
| STEP-LLM | STEP text | Parse as STEP. Public weights were not confirmed |

A tool-driver that writes build123d and a specialist that emits a
sequence can be compared only after both produce a solid the same
checker can read. CADGenBench is one such checker for STEP, and only
for its 81 fixtures.
