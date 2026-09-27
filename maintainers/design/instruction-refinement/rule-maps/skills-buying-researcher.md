# Rule map — `skills/buying-researcher/SKILL.md`

Item: DER-314 (E3).

Old: `skills/buying-researcher/SKILL.md` at main 7a11696, lines 1–132.
New: [`skills/buying-researcher/SKILL.md`](../../../../skills/buying-researcher/SKILL.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. `assets/brief-intake.md` is
unchanged: a form with no rules, no banned name, title "Purchase brief".
Wording only: the research method is unchanged.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter, description | kept, unchanged | L1–4 |
| 6 | Title | kept | L6 |
| 8 | Market research for a buy; a **researcher** skill, not an SDLC step | kept | L8 |
| 9 | No `scripts/` | kept | L9 |
| 9 | Recommend; do not spend | dropped: duplicate; owner Iron law (this file) | L13 |
| 36, 46, 96 | "they", "the user" (the person the research is for) | kept as one name, **Buyer**, defined at first use (standard 3; MQ1) | L9 |
| 11 | Heading "Iron law" | kept, stays first | L11 |
| 13–14 | Recommend. Do not spend. Purchases hand off to the operator (or the repo's purchase path) for human confirm | kept; "Do not" → "Never"; parenthesis → plain "or" (an alternative, no condition); old L117 "place an order, just buy it" folded in; "for human confirm" → "for a human to confirm" (MQ2) | L13–15 |
| 16 | Heading "When" | kept, as a condition → action table | L17–20 |
| 18–19 | Load when the **researcher** persona has a purchase, product shortlist, or market-choice ask | route (owner: root `AGENTS.md` load table, Research row, "Which skill loads when") | L21 |
| 19 | Skip when there is no market | kept | L22 |
| 19–20 | No language skill on a research-only turn | route (owner: `language-router`, no-language turns; its Family rules name `buying-researcher`) | L23 |
| 22–27 | Companion files, "read when relevant" | kept as links at their point of use: brief-intake → Intake; workflow → Procedure 2; review-skepticism → Procedure 3; guide-template → Procedure 4. "When relevant" gives way to those steps (standard 2) | L27–29, L53–58 |
| 29 | Heading "First reply — intake, not research" | kept as heading "Intake" plus the first sentence | L25, L27 |
| 31 | If the brief is thin, ask only what blocks a useful search | kept; "if the brief is thin" dropped as not checkable; "only what blocks" carries the condition (MQ3) | L44 |
| 31–32 | Do not dump a 20-question form | kept; "Never send", with the allowed action beside it | L44–45 |
| 34 | Always capture, infer, or mark unknown | kept, step 2 | L33–34 |
| 36–44 | Intake fields | kept; constraints parenthesis → "for example" (examples, no condition); "let them edit" → "for the buyer to edit"; named **purchase brief** (standard 3: "Brief" is an SDLC step name; the asset's title) | L27–29, L35–43 |
| 46–47 | If they say just go, proceed with stated priorities plus explicit assumptions | kept | L46–47 |
| 47 | Re-rank if weights change mid-project | kept, as if/then | L48 |
| 49–50 | If `discover-the-idea` already produced a brief, do not re-interview; use it as Phase 0 | kept; "as Phase 0" → "as the purchase brief" (Phase 0 fills it, workflow L19) | L31–32 |
| 52 | Heading "Map" | dropped: the phase map's owner is `references/workflow.md` | — |
| 54–55 | Frame → survey → refine by decision impact; phases in `workflow.md` | route (owner: workflow L3) | L53–54 |
| 57–62 | Phase table, Phases 3–6 collapsed | dropped: duplicate of workflow L5–13 (owner) | — |
| 64 | Heading "Research standard" | kept as heading "Procedure", numbered steps (standard 1) | L50 |
| 66–67 | Map the category: tiers, current vs outgoing, refresh cadence only when it changes the buy | dropped: duplicate; owner workflow Phase 1 (L29–33) | L53–54 |
| 68–69 | Long list → 4–8 serious candidates, + 1–2 popular traps if widely recommended | dropped: duplicate; owner workflow Phase 2 (L39–41) (MQ4) | L53–54 |
| 70–71 | Exact SKU / model year / config; never compare base to loaded without saying so | dropped: verbatim duplicate of workflow Phase 2 step 4 (L42) | L53–54 |
| 72–74 | Mine feedback across source types; prefer long-ownership, instrumented tests, forums, recall databases, repair communities over star averages | dropped: duplicate; owner workflow Phase 4 (L59; "repair communities" = its "specialist/repair forums") | L53–54 |
| 74–75 | Marketplace stars are polluted by default; see `review-skepticism.md` | route (owner: review-skepticism L3, L69) | L55–56, L91–92 |
| 76–77 | Live-enough pricing, stock, warranty, parts/service, return policy; note temporary deals | dropped: duplicate; owner workflow Phase 3 fields (L49–50) and Phase 4 class 4 (L68) | L53–54 |
| 77 | Default market: US retail unless stated | dropped: duplicate; owner workflow L15 | L53–54 |
| 78–79 | Score against **this** brief's weighted criteria, not a universal rubric | dropped: duplicate; owner workflow Phase 5 (L74) | L53–54 |
| 80–81 | Deliver a calm, specific, evidence-tagged guide willing to say wait or buy last-gen | dropped: duplicates; "calm, specific" owner Voice (L70, "No hype"); "evidence-tagged" owner review-skepticism L57 (routed L71–72); wait or last-gen owner workflow Phase 6 (L87) | L57–58, L70–72 |
| 81–82 | Follow `guide-template.md` unless they want shorter | route (owner of the "unless shorter" condition: guide-template L3) | L57–58 |
| 84 | Heading "Voice" | kept | L68 |
| 86 | Direct, dry, specific. No hype | kept, imperative | L70 |
| 87–88 | Tag source class (lab test, 3-year owner thread, technician forum, recall, affiliate roundup) | route (owner: review-skepticism L57 and its class table; the examples are its rows) | L71–72 |
| 89 | Quantify when possible. Ranges beat fake precision | kept; "when possible" → "when the evidence gives numbers" (standard 2; MQ5) | L73 |
| 90 | Thin evidence → say so. Never invent prices, scores, or quotes | kept, merged with old L122 into one Never bullet | L93–94 |
| 92 | Heading "Minimum viable guide" | kept as Procedure step 4, "Every guide carries at least" (MQ6) | L57–59 |
| 94–99 | Minimum guide contents | kept; "the user's criteria" → "the buyer's criteria"; parenthesis → colon | L60–65 |
| 101 | Chat-first. Offer a file only if asked | kept | L66 |
| 103 | Heading "Always" | dropped: each bullet duplicates a rule kept elsewhere (rows below) | — |
| 105 | Intake (or a confirmed `discover-the-idea` brief) before research | kept, merged into Never bullet 1; parenthesis → plain text (MQ7) | L86–88 |
| 106 | Recommend; do not spend | dropped: duplicate; owner Iron law | L13 |
| 107 | Cite source class | dropped: duplicate; owner review-skepticism L57 (routed L71–72) | L71–72 |
| 107 | No invented stats | dropped: duplicate of Never bullet 4 | L93–94 |
| 109 | Heading "Ask first" | kept; one route line to the owner of when and how to ask (SDLC index `#asking-the-human`, "anything in an Ask-first row") | L75, L77 |
| 111 | Writing a file | kept | L79 |
| 112 | Expanding "what should I buy" into "rebuild the product" | kept | L80 |
| 113 | Ticketed tracking on the board; **manager** after-acts if used | kept; the manager clause routes to its owner, SDLC index `#tracker` (only the manager writes the tracker; the manager after-acts the board) | L81–82 |
| 115 | Heading "Never" | kept | L84 |
| 117 | Spend, place an order, or "just buy it" | kept, folded into Iron law (allowed action: hand the purchase off) | L13–15 |
| 118 | Crown a winner from one review site or video | kept; "crown" → "pick" (standard 8: no metaphor); old L129 "affiliate roundup" folded in; allowed action "Weigh several source classes" (standard 7) | L89–90 |
| 119 | Treat marketplace stars as quality | route (owner: review-skepticism L3); allowed action beside it | L91–92 |
| 120 | Compare list to street without labeling which | dropped: duplicate; owner workflow Phase 3 (L49, "label list vs street") | — |
| 121 | Depth-first rabbit holes before the brief exists | kept, merged into Never bullet 1; metaphor removed (MQ7) | L86–88 |
| 122 | Fabricated stats or fake citations | kept, with old L90; allowed action "If the evidence is thin, say so" | L93–94 |
| 123 | Load a language skill "in case we code next" | route (owner: `language-router`, no-language turns) | L23 |
| 124 | Name pantheon personas | kept; allowed action: SDLC role names, or **researcher** (standard 7; MQ8) | L97–98 |
| 126 | Heading "Red flags" | dropped: each flag duplicates a Never rule; the one unique flag moves to Never | — |
| 128 | Research before priorities exist or are assumed out loud | kept, merged into Never bullet 1 (MQ7) | L86–88 |
| 129 | Crowning a winner from one affiliate roundup | kept, merged into Never bullet 2 | L89–90 |
| 130 | Treating marketplace stars as quality | dropped: duplicate of old L119 | L91–92 |
| 131 | Moralizing brands | kept, moved to Never; allowed action "Grade each candidate against the purchase brief" | L95–96 |
| 132 | "I'll purchase it to test" | dropped: duplicate; owner Iron law | L13–15 |

## Meaning questions

- **MQ1** — Old L36, L46, L96 call the person the research is for
  "they" and "the user"; old L13 names "the operator". Reading one: one
  person. Reading two: the operator may research for someone else.
  Resolved from the text: **Buyer** is "the person who asked for the
  research"; the Iron law keeps "the operator" verbatim, so no reading
  is chosen.
- **MQ2** — Old L14 "for human confirm" does not say which human.
  Resolved from the text: kept as "for a human to confirm"; no reading
  is chosen. "Human" is not a banned name.
- **MQ3** — Old L31 "If the brief is thin" is not checkable (standard
  2). Resolved from the text: "ask only what blocks a useful search"
  already limits the ask to blocking gaps, so with no blocking gap
  nothing is asked, as before.
- **MQ4** — Old L68–69 keeps traps "if widely recommended"; workflow
  (old L45) adds "and likely to waste money". Resolved from the text:
  old workflow L27 defines a trap as "popular-but-wrong", so every trap is
  likely to waste money; the owner keeps the full condition.
- **MQ5** — Old L89 "Quantify when possible". Resolved from the text:
  old L90 forbids invented numbers, so the only possible quantities are
  those the evidence gives.
- **MQ6** — Old L92 "Minimum viable guide": the floor for a shorter
  guide, or for every guide. Resolved from the text: both readings put
  the list in every guide, since the full template (guide-template
  L9–50) holds each item.
- **MQ7** — The research gate appears four ways: old L49 "already
  produced a brief", L105 "a confirmed `discover-the-idea` brief", L121
  "before the brief exists", L128 "before priorities exist or are
  assumed out loud". Resolved from the text: `discover-the-idea` asks
  the user to confirm its brief before it stops (its step 5), so
  "produced" and "confirmed" meet at its end; the merged bullet keeps
  "confirmed" (L105) and "assumed out loud" (L128).
- **MQ8** — Old L124 gives no allowed action. Resolved from the text:
  `discover-the-idea` L127–128 pairs the same Never with the SDLC role
  names; this skill adds its own **researcher** persona (old L8). The
  line names agents only; "buyer" and "operator" stay.
