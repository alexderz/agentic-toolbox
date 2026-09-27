# Rule map — `skills/discover-the-idea/SKILL.md`

Item: DER-312 (E1).

Old: `skills/discover-the-idea/SKILL.md` at main 7a11696, lines 1–136.
New: [`skills/discover-the-idea/SKILL.md`](../../../../skills/discover-the-idea/SKILL.md) (135 lines).
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
| 8 | "Architect gatherer." | route: role **architect**; gatherer and refiner ids, mint, resume → `docs/sdlc/subagents.md#step-agents` | L12–14 |
| 8–9 | Turn a messy thought into a brief another agent can attack; no `scripts/`; subject need not be code | kept; "attack" → "critiques" (standard 8); **brief** and **refiner** defined at first use (standard 3); "refiner" is the one name for the critiquing agent, as in `docs/sdlc/entry-brief-repo.md` | L8–10 |
| 11–14 | Iron law: do not write, do not decide, surface; user owns decisions, you own facts; ends in a brief | kept verbatim, stays first rule section | L18–21 |
| 16 | Heading "Loop" | kept | L23 |
| 18 | Step 0 heading "Stream of consciousness (always first)" | kept as "0. Dump (always first)": one name for the thing (standard 3) | L25 |
| 20 | Ask for a dump; wait; do not start questions in the same message | kept; numbered steps 2–3; "grill" → "questions" (standard 8) | L30, L36 |
| 22–26 | Say this text, then stop | kept, quote verbatim; "then stop" → "send this and nothing else" | L30–34 |
| 28–29 | Dump already in the invoking message: do not ask again, use it | kept, merged with old L108 as one if/then (MQ3); "invoking message" kept as the example; **dump** defined at first use | L27–29 |
| 31–34 | Reflect: one short paragraph in their words, tightened; confirm or correct before any question list; name what is still fog | kept, numbered; "fog" → "vague" (standard 8) | L38–43 |
| 36 | Step 2 heading "(only if it exists)" | kept | L45 |
| 38 | Look around after the dump; may not be a code repo | kept | L47 |
| 40–42 | Inspect only what is there (list); skip when no environment worth reading | kept, one step, skip condition first; "no environment worth reading" → "only when there is nothing to read" (MQ1, resolved by operator 2026-09-27 (Q7)) | L49–51 |
| 44–45 | Facts you can look up are your job; do not ask what a file, ticket, or public page says | kept; "Never … ; read it instead" names the allowed action (standard 7); owner of old L110, L125 | L52–53 |
| 47 | Step 3 heading "(when alternatives exist)" | kept | L55 |
| 49–50 | Real options (tools, patterns, prior art): research 3–5 before the first round that depends on the choice | kept; parenthesis → "such as" (MQ4); "grill round" → "question round" | L58–60 |
| 50–52 | Per option: who uses it, the ugly part, fit to this dump; cite a source; no invented "industry standard" | kept; "Never claim … ; cite one or leave the claim out" names the allowed action | L61–63 |
| 54 | Skip the map for a personal decision with no market | kept, as step 1 (skip condition first) | L57 |
| 56 | Step 4 heading "Frontier grill" | kept as "Question the frontier" (standard 8: no metaphor; the trigger phrase "grill me" stays in the description) | L65 |
| 58–59 | Treat the idea as a design tree; each decision hangs more decisions off it | kept as a definition; "hangs … off it" → "raises more decisions" | L67 |
| 61–63 | Frontier = questions whose prerequisites are settled; ask the whole frontier in one round; number; recommend each; wait | kept; definition, then numbered steps 1–2 | L68, L70–71, L83 |
| 65–75 | Question format block | kept verbatim, indented under step 1 so the step names it without a forward reference (standard 4) | L73–81 |
| 77–78 | Recompute the frontier; a question depending on one still open goes to the next round | kept | L84–85 |
| 80–81 | Push back on fog ("probably", "later", "something like"); propose a strawman | kept; "fog" → "vague words" | L87–88 |
| 81–82 | When you feel ready to stop, ask one more round on out-of-scope and failure modes, then stop | kept; "When you feel ready to stop" → "When the frontier is empty"; that round counts toward the cap of four (MQ2, resolved by operator 2026-09-27 (Q8)); placed after the cap so it names the cap without a forward reference (standard 4) | L91–93 |
| 84–86 | Done when the frontier is empty or the next question cannot be answered by talking (prototype, screenshot, live system); mark those open; do not invent | kept; the frontier-empty branch is the L91–93 stop (Q8); "Also stop when …" keeps the other branch; parenthesis → "for example because" (MQ5); "never invent" beside "Mark … open" | L93–95 |
| 88 | Step 5 heading | kept | L97 |
| 90 | Emit the brief; ask the user to confirm | kept, numbered | L99, L113 |
| 90 | Do not implement | dropped: duplicate; owner in this file: Iron law (L20) and Never (L124) | L124 |
| 90–91 | Do not hand the brief to a critiquer until they say so | kept; "critiquer" → "the refiner"; "Hand … only when the user says so" names the allowed action | L114 |
| 93–102 | Brief outline block | kept verbatim, indented under step 1 | L101–110 |
| 104 | Brief stays in chat; no file unless asked | kept | L112 |
| 106 | Heading "Always" | dropped: every bullet now sits with its owner (rows below) | — |
| 108 | Start at step 0 unless a dump is already in the thread | kept, merged into step 0.1 (MQ3) | L27–29 |
| 109 | Recommended answer on every question | dropped: duplicate of old L63; owner step 4.1 | L70–71 |
| 110 | Look up facts before asking | dropped: duplicate of old L44–45; owner step 2.2 | L52–53 |
| 111–112 | Cap at four rounds; round 4 still widens scope → split, gather one slice | kept, moved into step 4 before the stop rules | L90–91 |
| 113 | No language skill on a gather-only turn | route: owner `skills/language-router/SKILL.md#no-language-turns` (added by DER-318; this item lands after it) (rule owners: no-language turns) | L14–16 |
| 115–119 | Ask first: any file; expanding scope; critiquer or builder before the user confirms | kept; "a critiquer or builder" → "the refiner or a builder" (one name) | L116–120 |
| 121 | Heading "Never" | kept | L122 |
| 123 | Never implement, scaffold, sketch the API | kept; "emit the brief" names the allowed action | L124 |
| 124 | Never critique the brief in the same turn (different agent) | kept; parenthesis → "the refiner does that", the refiner defined in the intro; gatherer ≠ refiner routed to `docs/sdlc/subagents.md#step-agents` (MQ6) | L125, L12–14 |
| 125 | Never ask for what the environment answers | dropped: duplicate of old L44–45; owner step 2.2 | L52–53 |
| 126 | Never recommend a tool not looked at this session | kept; "look first" names the allowed action | L126 |
| 127–128 | Never name pantheon personas; roles are architect / designer / builder / tester / security / manager / operator | kept; role list → route to `docs/SDLC.md#roles` (same seven roles; rule owners: "use only the roles in the table") | L127 |
| 130–136 | Red flags | kept verbatim | L129–135 |

## Meaning questions

Resolved from the text:

- **MQ3** (old L28–29, L108): L28 says "in the invoking message", L108
  says "in the thread". The invoking message is in the thread, so the
  L108 condition covers both; the merged step (L27–29) uses "the
  thread" and keeps "in the invoking message" as the example.
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

Resolved by the operator:

- **MQ1** (old L41–42): "Skip this step when there is no environment
  worth reading" was a judgment condition (standard 2). Resolved by
  operator 2026-09-27 (Q7): skip the environment read only when there is
  nothing to read. Written at L49–51.
- **MQ2** (old L81): "When you feel ready to stop" was a judgment
  condition. Resolved by operator 2026-09-27 (Q8): "ready to stop" means
  the frontier is empty, and the extra round on out-of-scope and failure
  modes counts toward the four-round cap. Written at L91–93.
