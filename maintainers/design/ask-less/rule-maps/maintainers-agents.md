# Rule map — `maintainers/AGENTS.md`

Item: DER-740 (G9, source item A8 of DER-712). A later item that edits this file appends its own
section.

Old: `maintainers/AGENTS.md` at main c26f424, lines 1–50.
New: [`maintainers/AGENTS.md`](../../../AGENTS.md).
Key: **kept** (same rule, same place), **route** (the rule lives in its owner; this file links it),
**dropped** (owner named), **changed** (with the brief, ruling or LLD id that decides it). "Old L"
= line in the old file. Design: [LLD A8](../lld.md#a8--writing-standard-and-maintainer-rules).

A0 (DER-730) rewrote paths on L7 and L24 without moving any line; its
[path map](a0-path-map.md) records those rewrites.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–5 | Entry point for work on this repo; toolbox users stop at the root `AGENTS.md` | kept | L3–5 |
| 7–9 | Read the root `AGENTS.md` and the SDLC index first; write to the writing standard | kept | L7–9 |
| 11–12 | Tracker skill path is relative to this directory | kept | L11–12 |
| 14, 16 | `## Tracker`: Linear, tracker-sdlc v2 | kept | L14, L16 |
| 18, 20 | `## Execution`: `Parallelism: max` | kept | L18, L20 |
| 22 | `## Evals` | kept | L22 |
| 24–25 | Agent text list | changed (HLD A0 item 6; LLD A8 § Evals line): one line; `skills/` holds the SDLC | L24 |
| 27–37 | Evals rules 1–5: T1–T3 merge rule, run files, decision, baseline, new model | kept (R59) | L26–36 |
| 39–50 | Where notes go | kept | L38–49 |

## Meaning questions

None. The Agent text list names the same files: `skills/` already held `skills/sdlc/`.
