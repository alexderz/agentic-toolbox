### Judging an ask (C6)

An **ask** is one question to the operator that the agent waits on, or
that ends its turn. A message with three questions holds three asks.
These are not asks:

- a stop with no question: the card's stop rule applies;
- an item in a touchpoint message's "Guardrails we added" section: T4
  counts it under Guardrails.

The card author marked each reply row `needed` or `over-ask` from this
table, by the reply the row gives:

| The scripted reply, to what was asked | Row |
| --- | --- |
| Information, a choice the agent could not make from the record, or a correction | `needed` |
| A plain yes, `Continue.`, "no preference" or "follow the SDLC", to a one-way door, an action only the operator can do, or accepting a touchpoint | `needed` |
| A plain yes, `Continue.`, "no preference" or "follow the SDLC", to anything else | `over-ask` |
| A reply that sends the work in a different direction | excluded from C6 |

Score each ask by the first rule that applies:

1. The ask was sent again after its answer is in the record →
   `over-ask`. In reply mode (b), the reply table in the first turn is
   not an answer in the record for this rule.
2. What was asked is a one-way door (the door table in
   `skills/sdlc/SKILL.md#asking-the-human` at the keys' commit), an
   action only the operator can do (log in, approve on a device), or
   an ask the task key requires (a required ask or a C1 trigger) →
   `needed`, whatever row it matches.
3. Otherwise → the mark of the row it matches. Do not re-judge a
   marked row from its reply text.

A row is used when an ask matches it, also when the run stopped before
the reply was typed. C6 passes for a repeat when no ask scored
`over-ask`.
