# Change map — `docs/ARCHITECTURE.md`

Item: DER-337 (G47). Light pass (LLD "Behavior: rule-map format"):
changed lines only. Old = project-main 120d298. "Old L" = line in the
old file; "L" = line in the new file. No rule changes meaning; people
docs are not agent text.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 20–21 | Prose name "SDLC Conventions" → link [Product repo layout](../../../../docs/sdlc/conventions.md#product-repo-layout); re-wrapped | LLD "Links": the `docs/ARCHITECTURE.md` L20 prose section name | 20–22 |
| 24 | "unless they waive." → "unless they waive it." | Tone pass | 25 |
| 25 | `[SDLC.md](SDLC.md)` → `[Steps](SDLC.md#steps)` | Link to the section that names the steps | 26 |
| 69–77 | Header "Boundary" → "Job"; rows replaced by the SDLC index `#roles` rows | G47: role tables = the index's seven roles and jobs | 70–78 |

## Checks

- Role table equals `docs/SDLC.md` L25–33 byte for byte.
- K3 (names that apply to people docs): no "improvise", "orchestrator",
  "official copy", "parent agent/session", "a person".
- K7: every relative link and anchor resolves.
- K10: added lines hold no hostnames, IPs, ports, paths or tokens.
