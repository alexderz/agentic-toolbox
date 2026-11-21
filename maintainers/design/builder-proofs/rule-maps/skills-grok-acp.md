# Rule map — `skills/grok-acp/SKILL.md`

Item: DER-809. Brief: [brief](../brief.md).

Old: `skills/grok-acp/SKILL.md` at chunk base commit 80bfbd5, lines 1–178. New: `skills/grok-acp/SKILL.md` (203 lines).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–95 | Unchanged rules in this range | kept | 1–95 |
| 96–100 | SDLC fit, Role: verifier and reviewer never see Grok's transcript; verifier gets ticket and proving commands | changed (R1, R2, R3): Grok runs every check and returns a proof bundle; the reviewer never sees the transcript and gets the pr-review inputs and the bundle | 96–101 |
| 101 | Unchanged rules in this range | kept | 102 |
| 102 | Labels: never resumed to verify or review its own work | changed (R1): never resumed to review its own work | 103 |
| 103–115 | Unchanged rules in this range | kept | 104–116 |
| after 115 | Post-land journeys | route (R5): the manager resumes the item label for touched journeys at the land SHA on the land target | 117–118 |
| 116–130 | Unchanged rules in this range | kept | 119–133 |
| 131 | Handoff "Prove it" line | changed (R1, R6): Grok runs each command fresh, writes and runs span tests and journeys, including missing coverage for changed behavior, and saves full output | 134–138 |
| 132–134 | Unchanged rules in this range | kept | 139–141 |
| 135 | Handoff "Finish with" line | changed (R2): pack the seven fields and the empty-field rule for private review; separate public reporting | 142–157 |
| 136–139 | Unchanged rules in this range | kept | 158–161 |
| 140 | After it returns: you are the manager, not the verifier | changed (R1, R2): nobody re-runs Grok's checks; the manager reads evidence | 162–163 |
| 141–144 | Unchanged rules in this range | kept | 164–167 |
| 145–150 | After it returns steps 2–5: mint/resume a verifier; it runs proving commands; failures to the same label; tests pass from the verifier, never `text` | changed (R2, R3): read the bundle; confirm fields and paths exist; gaps or failures to the same label; tests pass from saved outputs, never `text` alone; then Review with a reviewer that is not Grok | 168–175 |
| 151–166 | Unchanged rules in this range | kept | 176–191 |
| 167–168 | Never: one session builds and verifies; Grok transcript to a verifier or reviewer | changed (R3): never builds and reviews; transcript never to the reviewer, which gets its inputs and the bundle | 192–193 |
| 169–175 | Unchanged rules in this range | kept | 194–200 |
| 176 | Red flag: resume the builder to double-check its own work | changed (R1): "to review its own work"; re-running its own checks is now the builder's job | 201 |
| 177–178 | Unchanged rules in this range | kept | 202–203 |

Protected rows touched: Permission posture (L170–171 old) kept; labels kept; own-item limit changed under R1/R3 (MQ1).

## Meaning questions

- MQ1 — Resolved: R1/R3: the same builder may run checks, never review its own item. Label scope and permissions stay unchanged.
- MQ2 — Resolved: R2: saved outputs, not worker status text, support acceptance.
