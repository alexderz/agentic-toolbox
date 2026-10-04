# Rule map — `skills/sdlc-artifacts/templates/poc.md`

Item: DER-278. A later item that edits this file appends its own
section. First-party template (`SOURCES.md`, `sdlc-artifacts`), so a
full map, not a light pass.

Old: `skills/sdlc-artifacts/templates/poc.md` at project-main 88455d8
(same as main 7a11696), lines 1–17.
New: [`skills/sdlc-artifacts/templates/poc.md`](../../../../skills/sdlc-artifacts/templates/poc.md).
Disposition: **kept**, **route**, **dropped** (owner named),
**changed** (MQ named). "Old L" = line there; "L" = line in the new
file. Headings and bold labels are unchanged (K6); 17 → 17 lines (K2).

| Old L | Rule | Disposition | L |
| --- | --- | --- | --- |
| 1 | Title `# PoC — <question>` | kept | L1 |
| 3 | Date | kept | L3 |
| 4 | `HLD: docs/<path>` | changed (MQ1): `HLD: <path to the chunk's HLD>`, no fixed folder | L4 |
| 5 | Ticket | kept | L5 |
| 7 | `## Required` | kept | L7 |
| 9 | **Question** — what this PoC must answer | kept | L9 |
| 10 | **Setup** — how to run it | kept; adds "the code sits in `poc/` beside this note" (MQ2) | L10 |
| 11 | **Evidence** — commands, output paths, or screenshots in git | kept | L11 |
| 12 | **Conclusion** — proceed / do not / still unknown | kept | L12 |
| 13 | **What we will not treat as product** | kept; adds the fill hint "all of `poc/`; name what Build must rebuild"; the rule stays in its owner `docs/sdlc/plan-trial-spec.md#trial` | L13 |
| 15 | `## Optional` | kept | L15 |
| 17 | Throwaway tree path | changed (MQ2): "Output kept outside git: where it is, and why it is not in `poc/`" | L17 |

## Meaning questions

- **MQ1** — Where the note and its HLD live. Resolved by the operator,
  2026-09-27: beside the chunk's design records, wherever those live;
  DER-271 decides that place. The header names no folder.
- **MQ2** — "Throwaway tree path" assumed trial code lived outside the
  repo. Resolved by the operator, 2026-09-27: code stays in `poc/`; no
  data dumps, vendored dependencies or build output there. The Optional
  field now records only what stays out, and why. The `poc/README.md`
  content, including the secret-removal exception, is owned by
  `plan-trial-spec.md#trial` step 3, not copied here: the template
  cannot grow (K2).

No open MQ.
