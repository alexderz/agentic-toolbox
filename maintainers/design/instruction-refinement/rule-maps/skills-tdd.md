# Change map — `skills/tdd/SKILL.md`

Item: DER-319 (F, vendor-derived light pass).

Old: `skills/tdd/SKILL.md` at main 7a11696, lines 18 and 24.
New: [`skills/tdd/SKILL.md`](../../../../skills/tdd/SKILL.md).
Light pass: changed lines only (writing standard, Rule maps 6).
Disposition: **kept** (same rule, new wording), **route** (the rule
lives in its owner; this file links it). "Old L" = line in the old file;
"L" = line in the new file. 127 lines old, 127 new. The teaching is
unchanged. No upstream text is added and nothing was fetched.

Protected rows touched: none. Operator clarifications (2026-09-27): the
"a person" replacement applies at old L18; the others do not occur here.
`SOURCES.md` `tdd` row: Notes cell only; the SHA cell keeps its pin.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 18 | Ask first: whom to ask before skipping the cycle | kept; "the operator (or the pairing human)" → "the operator, or someone the operator names in writing" (Names; standard 8, no condition in a parenthesis) (MQ1) | L18 |
| 18 | Ask first: how to ask | route (owner: `docs/SDLC.md#asking-the-human`, "An ask is required for: … anything in an Ask-first row"); adds no condition | L18 |
| 24 | Throwaway or prototype: explore, discard, redo with TDD if it ships | kept; "remint" → "rebuild it": "mint" names starting a subagent in the SDLC (standard 3, one name per thing) | L24 |

## Meaning questions

- **MQ1** — Old L18 "the pairing human" could mean the operator in the
  session, or any person working with the agent. Resolved from the text:
  the owner `docs/SDLC.md#asking-the-human` says a decision needs "the
  operator, or someone the operator names in writing" and requires an
  ask for "anything in an Ask-first row"; a route adds no condition
  (standard 5), so the skill cannot widen the owner's set. The first
  reading holds.
