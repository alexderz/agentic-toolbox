# Rule map — `ask-human.md` (A2, DER-734)

Old: `skills/sdlc-artifacts/templates/ask-human.md` at main c26f424, lines 1–19. New: `skills/sdlc-artifacts/templates/ask-human.md`.

The new text is `rebuild/ask-human-template.md`, which replaces the LLD A2 block (overlay §6 G3, edit 3).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Opening line: a decision is needed on one ticket before the agent continues | changed (R57, R130): the opening names the message (a touchpoint or open questions) and counts the questions and guardrails; each question carries its own `<chunk-slug or ticket id> <ask id>` tag | Opening line; each question's heading |
| 3–4 | What I need: the choice in everyday words, no project jargon | kept, as the line under each ask-id heading; a project word is explained in the same sentence | `**Questions**`, each question |
| 6–7 | Why it matters: what happens if we wait, guess, or pick each way | kept | `- Why it matters:` |
| 9–12 | Choices numbered 1, 2, 3 | kept (R57, as changed at Spec round 2, D11) | `- Choices:` |
| 14–15 | Recommend one choice, with reasons; say so if none is clearly better | kept | `- I recommend` |
| 17–18 | Reply with 1, 2 or 3, "wait", or "don't need my OK on this" | kept per ask id; guardrails gain keep, change, or remove (R57) | `**What to reply**` |
| 19 | The agent stops this part until the operator answers | changed (L5, W1): work that does not depend on the questions continues | Opening line |
| — | (new) `none` under Questions; guardrails listed `GR<n>` until answered; rulings since the last touchpoint; a "For this message" part | changed (R57, R118, R130) | `**Guardrails we added**`, `**Rulings since the last touchpoint**`, `**For this message**` |

## Meaning questions

- MQ1: the rewrite changes the template's shape (one decision per message → a batch of ask-id
  questions with guardrails and rulings). Resolved by the brief (L2, G2, G4), operator-confirmed
  2026-11-11 (LLD A2; R92), and widened by R130 (`none` under Questions, the counts, the ticket-id
  tag, `GR<n>` ids, "For this message").
