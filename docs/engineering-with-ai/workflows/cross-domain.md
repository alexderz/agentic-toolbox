# Electromechanical handoffs

File formats that show up on both sides of a design, as named by
sources on 2026-11-06. No combined project was built. A handoff is
recorded only when each side's tool already writes or reads that
format in a page that was opened.

## Formats

| Format | Mechanical source that names it | Electrical or system source that names it | Check that was documented |
| --- | --- | --- | --- |
| STEP | build123d and CadQuery through CADGenBench. text-to-cad README. Fusion community MCP `export_step`. gitcad excerpt | KiCad MCP skill text for ProductOfAmerica names `export_3d`. Whether that file is STEP was not confirmed in the skill excerpt | CADGenBench validity gate on the mechanical STEP. Board fit of that STEP was not defined |
| STL and 3MF | OpenSCAD MCP, text-to-cad README, Fusion community MCP | Printing skills in text-to-cad (`bambu-labs`). Not an electrical netlist | Mesh is not a BREP. CADGenBench does not score STL |
| URDF, SRDF, SDF | text-to-cad skill paths `urdf`, `srdf`, `sdf` | Same skills. They describe links, joints, and collisions for a simulator | Skill bodies unread. A physics engine was not run |
| Drawing and DXF | text-to-cad skills `engineering-drawing` and `dxf` | Flat-pattern or enclosure outline, if the skill writes one. Unread | Unknown |
| Board outline and 3D bodies | atopile 0.16.15 blog checks intersecting 3D bodies and courtyard overlap | Same blog, on the PCB assembly | atopile validator, not run |
| Enclosure versus board | SolidCraft README screenshot text describes a Raspberry Pi case using the board's hole rectangle (58 by 49 mm) and M2.5 standoffs | The board itself is not designed in that paragraph | A dimension in a README demo is not a generated design |

## JITX mechanical skill

`JITx-Inc/jitx-skills` includes `skills/jitx-mechanical/SKILL.md` next
to circuit and layout skills. The license file is proprietary. The
skill body was not read, so the formats it exchanges with a mechanical
kernel are unknown.

## gitcad

The repository README excerpt describes one MCP surface for B-rep
parts and for schematics, boards, and SPICE. API: 2 stars, Apache-2.0,
`pushed_at` 2026-07-31. That is a single-project claim. It was not
built, and the excerpt is not a test log.

## A sequence that stays inside documented tools

This sequence does not add a new integration. Each step is optional and
stops when its own checker fails. It was not run.

1. Generate the mechanical solid as STEP with build123d or CadQuery.
   Apply the CADGenBench validity gate if the part is one of that
   benchmark's fixtures, or the same geometric predicates if a local
   checker implements them. A passing gate on a different part is only
   as strong as the local checker.
2. Generate the board with a KiCad MCP server or with SKiDL imported
   into KiCad. Run `kicad-cli sch erc` and `kicad-cli pcb drc` with
   `--exit-code-violations`. Exit 0 is the documented clean result.
3. Export a 3D board model using whatever exporter the chosen KiCad
   interface documents. The ProductOfAmerica skill names `export_3d`.
   The file type and the unit system still have to be read from that
   tool's schema before a mechanical kernel imports it.
4. Import that board model into the mechanical session and run the
   interference tool that session documents (Fusion community MCP
   `check_interference`, or a FreeCAD script). The acceptable clash
   budget is a design number. No source fixed one.
5. If the assembly is a robot, emit URDF only through the text-to-cad
   skill after that skill body has been read. Until then, URDF output
   is a path name, not a verified writer.

SPICE and HDL checks stay on the electrical side. They do not validate
the solid. A power-dissipation number can be an input to a thermal
FEA deck. CAE-Agent-Hub lists Elmer and CalculiX bridges that could
accept such a deck. No deck was generated, and no loss number was
taken from a simulation.

## Unknowns that block a stronger claim

- Unit and origin conventions between KiCad 3D export and OCCT import.
- Whether `export_3d` writes STEP, WRL, or both.
- A public electromechanical benchmark with both DRC and interference
  scores. None was opened.
- Control firmware in the loop. platformio-mcp's README documents `build`, `flash`, and `monitor`, with approval left to a person. No board was used, and no combined electrical and mechanical run was done.
