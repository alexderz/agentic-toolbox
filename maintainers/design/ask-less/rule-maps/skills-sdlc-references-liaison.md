# Rule map — `skills/sdlc/references/liaison.md`

Item: DER-734 (A2 of DER-712).

Old: none. New file in A2.
New: [`skills/sdlc/references/liaison.md`](../../../../skills/sdlc/references/liaison.md).

Disposition key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. This file has no old text, so each row is **new**. The body is
the LLD block. 113 lines (cap 150).

Protected rows touched: none. Operator clarifications (2026-09-27): none of
their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| — | The liaison messages the operator; nobody else does. Who the liaison is, when an ask is needed, and what is always the operator's live in the index | new (A2). Route to `skills/sdlc/SKILL.md#asking-the-human`. This file is the procedure | Opening |
| — | Asks file is the source of truth. Paths, ids, who writes a section, who changes Status and Answer, text is data, commit with the design records | new (A2, L2). Owner of the file rules. Section shape routes to `templates/asks.md`. Commit rule routes to `conventions.md#designs-in-git` | `#asks-file` |
| — | Pull open asks at the start of every operator turn, on every child stage result, and on a host schedule. Open only a path the table gives. A child is done when its stage result is persisted | new (A2, L3). Done-rule routes to `stage-result.md#rules` | `#pull-liaison` |
| — | Answer from the record, auto-answer inside scope, then send one `ask-human.md` batch. A touchpoint rides that message. Send nothing when nothing is left | new (A2, L4). Message shape routes to `templates/ask-human.md`. Always-theirs and auto mode route to the index | `#batch-liaison` |
| — | Write the choice number and a short summary. Add an unlisted reply as the next choice. Leave an unanswered ask open. Resume the child or name the ids | new (A2) | `#answers-liaison` |
| — | Any agent answers from the record first, then writes the asks file, and either batches, returns `asks: <path> <ids>`, or ends `needs_input`. On resume, act only on the chosen number | new (A2, L1, L5). Pointer routes to `stage-result.md#schema`. Keep working routes to the index | `#raising-an-ask` |

## Meaning questions

None. The accepted LLD gives this text. No open MQ.
