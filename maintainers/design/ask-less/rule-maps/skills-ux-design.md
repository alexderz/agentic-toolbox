# Rule map — ux-design

Item: DER-739 (G8, source item A7 of DER-712).

Old: `skills/ux-design/SKILL.md` at main c26f424, lines 66–83. New: `skills/ux-design/SKILL.md`.

Only the Review loop section changes. A0 changed only link paths here (old L64, L68, L80).
Edit: [overlay G8](../opus-rebuild.md#g8--design-gate-hld-touchpoint-delivery-route-a7), which
overrides the `ux-design` edit of [LLD A7](../lld.md#a7--design-gate-and-hld-touchpoint).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 66 | Heading: Review loop (agents, then operator) | **kept** | L66 |
| 68 | Loop and operator acceptance: link to the SDLC UX step | **kept** | L68 |
| 70–77 | Step 1: the UX reviewer reads the brief, stories and written taste; the checks; no taste of its own | **kept** | L70–77 |
| 78 | Step 2: the designer fixes; the UX reviewer re-checks until the agents agree | **kept** | L78 |
| 79–80 | The agents disagree on the requirements → ask the operator ([Asking the operator](../../../../skills/sdlc/SKILL.md#asking-the-human)) | **kept**: a "theirs" question (LLD A7) | L79–80 |
| 81–83 | Step 3: the agents agree → ask the operator the same way, with the variants, the agents' pick and why | **changed** (R154–R156; overlay G8): the variants go to the operator at the design gate; the designer hands them to the **manager** with the pick and why, and sends no message itself. MQ1 | L81–84 |

## Meaning questions

- MQ1. Old L81 "ask the operator the same way" let the designer ask directly. The new step routes
  the variants through the manager to the design gate. Is the operator's acceptance still there?
  Resolved: yes. The operator still accepts the variants, at touchpoint 3. Only the sender
  changes: the liaison sends touchpoints. Cited: [hld.md](../hld.md) Touchpoints table, row 3
  ("LLD, UX and mockup acceptance"); overlay G8 Security focus ("the designer never messages the
  operator").
