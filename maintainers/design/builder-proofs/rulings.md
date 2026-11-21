# Verification design notes

- R1–R4: `skills/sdlc/references/proofs.md` owns builder checks and the proof bundle. The reviewer reads direct evidence for the tested revision without repeating the same run. Public reports omit the private bundle.
- R2: the Grok handoff includes the bundle fields because workers may not have the skills checkout. It separates the private handoff from public reporting.
- R5: verify the item on its land target at the land SHA. Only chunks have a second, full journey run on project-main before Trunk.
- R6: the changed behavior determines journey and span coverage. Missing coverage of a touched journey requires a test; unchanged behavior needs no speculative journey.
- R7–R9: Build links the proof guide, vendor-derived edits retain their pins, and the changelog records the workflow change.
