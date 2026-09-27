# Rule map — `skills/discover-the-idea/SKILL.md`

Item: DER-312 (E1).

Old: `skills/discover-the-idea/SKILL.md` at main 7a11696, lines 1–136.
New: [`skills/discover-the-idea/SKILL.md`](../../../../skills/discover-the-idea/SKILL.md) (136 lines).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected rows touched: none. Operator clarifications (2026-09-27): "gate
reasons in parentheses are examples" applied by analogy in MQ4; the other
subjects do not occur in this file. Out of scope: the gather loop's
meaning (steps 0–5, their order, the brief outline).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter, description ("architect gatherer", trigger phrases) | kept, unchanged | L1–4 |
| 6 | Title | kept | L6 |
| 8 | "Architect gatherer." | route: role **architect**; gatherer id, mint, resume → `docs/sdlc/subagents.md#step-agents` | L12–14 |
| 8–9 | Turn a messy thought into a brief another agent can attack; no `scripts/`; subject need not be code | kept; "attack" → "critiques" (standard 8); **brief** and **critiquer** defined at first use (standard 3) | L8–10 |
| 11–14 | Iron law: do not write, do not decide, surface; user owns decisions, you own facts; ends in a brief | kept verbatim, stays first rule section | L18–21 |
| 16 | Heading "Loop" | kept | L23 |
| 18 | Step 0 heading "Stream of consciousness (always first)" | kept as "0. Dump (always first)": one name for the thing (standard 3) | L25 |
| 20 | Ask for a dump; wait; do not start questions in the same message | kept; numbered steps 2–3; "grill" → "questions" (standard 8) | L29, L35 |
| 22–26 | Say this text, then stop | kept, quote verbatim; "then stop" → "send this and nothing else" | L29–33 |
| 28–29 | Dump already in the invoking message: do not ask again, use it | kept, merged with old L108 as one if/then (MQ3); **dump** defined at first use | L27–28 |
| 31–34 | Reflect: one short paragraph in their words, tightened; confirm or correct before any question list; name what is still fog | kept, numbered; "fog" → "vague" (standard 8) | L37–42 |
| 36 | Step 2 heading "(only if it exists)" | kept | L44 |
| 38 | Look around after the dump; may not be a code repo | kept | L46 |
| 40–42 | Inspect only what is there (list); skip when no environment worth reading | kept, numbered, skip condition first; "worth reading" kept verbatim (MQ1, open) | L48–50 |
| 44–45 | Facts you can look up are your job; do not ask what a file, ticket, or public page says | kept; "Never … ; read it instead" names the allowed action (standard 7); owner of old L110, L125 | L51–52 |
| 47 | Step 3 heading "(when alternatives exist)" | kept | L54 |
| 49–50 | Real options (tools, patterns, prior art): research 3–5 before the first round that depends on the choice | kept; parenthesis → "such as" (MQ4); "grill round" → "question round" | L57–59 |
| 50–52 | Per option: who uses it, the ugly part, fit to this dump; cite a source; no invented "industry standard" | kept; "Never claim … ; cite one or leave the claim out" names the allowed action | L60–62 |
| 54 | Skip the map for a personal decision with no market | kept, as step 1 (skip condition first) | L56 |
| 56 | Step 4 heading "Frontier grill" | kept as "Question the frontier" (standard 8: no metaphor; the trigger phrase "grill me" stays in the description) | L64 |
| 58–59 | Treat the idea as a design tree; each decision hangs more decisions off it | kept as a definition; "hangs … off it" → "raises more decisions" | L66 |
| 61–63 | Frontier = questions whose prerequisites are settled; ask the whole frontier in one round; number; recommend each; wait | kept; definition, then numbered steps 1–2 | L67, L69–70, L82 |
| 65–75 | Question format block | kept verbatim, indented under step 1 so the step names it without a forward reference (standard 4) | L72–80 |
| 77–78 | Recompute the frontier; a question depending on one still open goes to the next round | kept | L83–84 |
| 80–81 | Push back on fog ("probably", "later", "something like"); propose a strawman | kept; "fog" → "vague words" | L86–87 |
| 81–82 | When you feel ready to stop, ask one more round on out-of-scope and failure modes, then stop | kept verbatim, moved after the done rule (MQ2, open) | L94–95 |
| 84–86 | Done when the frontier is empty or the next question cannot be answered by talking (prototype, screenshot, live system); mark those open; do not invent | kept; parenthesis → "for example because" (MQ5); "never invent" beside "Mark … open" | L89–92 |
| 88 | Step 5 heading | kept | L98 |
| 90 | Emit the brief; ask the user to confirm | kept, numbered | L100, L114 |
| 90 | Do not implement | dropped: duplicate; owner in this file: Iron law (L20) and Never (L125) | L125 |
| 90–91 | Do not hand the brief to a critiquer until they say so | kept; "Hand … only when the user says so" names the allowed action | L115 |
| 93–102 | Brief outline block | kept verbatim, indented under step 1 | L102–111 |
| 104 | Brief stays in chat; no file unless asked | kept | L113 |
| 106 | Heading "Always" | dropped: every bullet now sits with its owner (rows below) | — |
| 108 | Start at step 0 unless a dump is already in the thread | kept, merged into step 0.1 (MQ3) | L27–28 |
| 109 | Recommended answer on every question | dropped: duplicate of old L63; owner step 4.1 | L69–70 |
| 110 | Look up facts before asking | dropped: duplicate of old L44–45; owner step 2.3 | L51–52 |
| 111–112 | Cap at four rounds; round 4 still widens scope → split, gather one slice | kept, moved into step 4 beside the stop rules | L95–96 |
| 113 | No language skill on a gather-only turn | route: owner `skills/language-router/SKILL.md#family-rules` (rule owners: no-language turns) | L14–16 |
| 115–119 | Ask first: any file; expanding scope; critiquer or builder before the user confirms | kept verbatim | L117–121 |
| 121 | Heading "Never" | kept | L123 |
| 123 | Never implement, scaffold, sketch the API | kept; "emit the brief" names the allowed action | L125 |
| 124 | Never critique the brief in the same turn (different agent) | kept; parenthesis → "the critiquer does that", the critiquer defined in the intro; gatherer ≠ refiner routed to `docs/sdlc/subagents.md#step-agents` (MQ6) | L126, L12–14 |
| 125 | Never ask for what the environment answers | dropped: duplicate of old L44–45; owner step 2.3 | L51–52 |
| 126 | Never recommend a tool not looked at this session | kept; "look first" names the allowed action | L127 |
| 127–128 | Never name pantheon personas; roles are architect / designer / builder / tester / security / manager / operator | kept; role list → route to `docs/SDLC.md#roles` (same seven roles; rule owners: "use only the roles in the table") | L128 |
| 130–136 | Red flags | kept verbatim | L130–136 |

## Meaning questions

Resolved from the text:

- **MQ3** (old L28–29, L108): L28 says "in the invoking message", L108
  says "in the thread". The invoking message is in the thread, so the
  L108 condition covers both; the merged step uses "the thread" and
  names the invoking message as an example.
- **MQ4** (old L49): "(tools, patterns, prior art)" lists examples of
  real options, as the operator clarification reads parenthesized gate
  reasons; written "such as". "real" is kept.
- **MQ5** (old L85–86): "(needs a prototype, a screenshot, a live
  system)" illustrates "cannot be answered by talking"; that clause is
  the test. Written "for example because".
- **MQ6** (old L124): "(different agent)" names who critiques. The
  owner, `docs/sdlc/subagents.md#step-agents`, says the gatherer and the
  refiner are never the same agent; the route adds no condition. "In the
  same turn" is kept.

Open (old wording kept; the item is blocked until the operator answers):

- **MQ1** (old L41–42): "Skip this step when there is no environment
  worth reading" is a judgment condition (standard 2). Reading A: skip
  only when none of the listed sources (L40–41) exist, matching the
  heading "(only if it exists)". Reading B: also skip when sources exist
  but none bears on the idea. Proposed: reading A, written "If none of
  these exist, skip this step."
- **MQ2** (old L81): "When you feel ready to stop" is a judgment
  condition. Reading A: when the done rule (old L84–86) holds. Reading
  B: the agent's own sense, which may come earlier, for example at the
  four-round cap. Also open: whether that extra round counts toward the
  cap of four. Proposed: reading A, written "When the session is done by
  the rule above, ask one more round … then stop". No proposal on the
  cap; the operator says whether the extra round counts.
