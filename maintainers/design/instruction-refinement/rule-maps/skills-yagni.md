# Rule map — `skills/yagni/SKILL.md`

Item: DER-313 (E2).

Old: `skills/yagni/SKILL.md` at main 7a11696, lines 1–41.
New: [`skills/yagni/SKILL.md`](../../../../skills/yagni/SKILL.md).
Disposition: **kept** (same rule, new wording or place), **route** (the
rule lives in its owner; this file links it), **dropped** (duplicate,
owner named), **DER-265**, **DER-271**. "Old L" = line in the old file;
"L" = line in the new file. Wording only; 41 lines old, 41 new.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter: name, description | kept verbatim | L1–4 |
| 6 | Title "YAGNI" | kept | L6 |
| 8 | "Restraint." | kept, as the imperative "Use restraint." | L8 |
| 8 | Prefer the smallest change that meets **this** Task | kept; "Task" → "ask", with "the ask" defined at first use (MQ1); "speculative generality" defined at first body use (standard 3), from Iron law L12: "a need the ask does not have (a future need)", matching "If the ask does not need it" | L8 |
| 8 | Do not build for imagined tomorrow | kept; metaphor "imagined tomorrow" → "a need the ask does not have" (standard 8) | L8 |
| 8 | Compatible with `tdd` and `verify-before-done` | kept, as a sentence | L8 |
| 8 | No `scripts/` | kept, as "This skill has no `scripts/`." (MQ2) | L8 |
| 10–12 | Iron law: do not ship speculative generality; if the ask does not need it, leave it out | kept verbatim, first (standard 7) | L10–12 |
| 14 | Heading "Always" | kept | L14 |
| 16 | Prefer one focused PR (~≤300–400 lines, one idea) | kept; parenthesis → colon, numbers verbatim (MQ3) | L16 |
| 17 | Delete or skip dead code paths you replace; do not leave dual routers | kept; "do not" → "Never" with the allowed action "keep one path" beside it (standard 7) | L17 |
| 18 | Reuse an existing skill id before inventing a parallel procedure | kept; "inventing" → "you write" | L18 |
| 19 | Keep AGENTS.md thin (ids + repo rules); put procedures in skills | kept; parenthesis → "thin: ids and repo rules only"; two sentences | L19 |
| 21 | Heading "Ask first" | kept | L21 |
| 21 | Ask first: whom and how | route (owner: `docs/SDLC.md#asking-the-human`, "An ask is required for: … anything in an Ask-first row"); lead line names the operator (MQ4) | L23 |
| 23 | New abstraction "for later reuse" with no second caller yet | kept verbatim | L25 |
| 24 | New config flag / feature toggle with no current consumer | kept; "/" → "or" | L26 |
| 25 | Expanding a skill past ~250 lines or adding `scripts/` to a skill dir | kept verbatim (MQ3) | L27 |
| 26 | Second toolkit that overlaps an installed skill id (dual router risk) | kept; parenthesis → ": a dual-router risk" (a reason, no condition) | L28 |
| 28 | Heading "Never" | kept | L30 |
| 30 | Remint a MERGED skill body without a new **security** cut | kept; allowed action "get the cut first" beside it (standard 7) | L32 |
| 31 | Add marketplace installers or auto-update upstream into skills | kept; allowed action: route to `docs/INTAKE.md` (owner of third-party intake; checklist steps 1 and 6 hold the same ban), no condition added | L33 |
| 32 | Personal finance, mail, password stores, or extra hosts via "just in case" helpers | kept, as the imperative "Never add “just in case” helpers for …"; allowed action "leave them out" (standard 7) | L34 |
| 34 | Heading "Red flags" | kept, as the bold label "**Red flags.**" (no link targets `#red-flags`), so the file stays at 41 lines | L36 |
| 36–39 | Four red-flag phrases | kept verbatim | L38–41 |
| 41 | Stop. Shrink the change. Ship the ask. | kept verbatim; the unstated trigger → "If your plan says one of these," before the list (standard 2) (MQ5) | L36 |

## Meaning questions

- **MQ1** — Old L8 "this Task" could name a tracker Task (an item) or the
  current task in general. Resolved from the text: the description (L3)
  and the Iron law (L12) call the same thing "the current ask" and "the
  ask", and the skill also loads for chunk Refine, so "the ask" (the
  current task's request) keeps the old meaning; **this** stays bold.
- **MQ2** — Old L8 "No `scripts/`." could state that this skill ships no
  scripts, or forbid `scripts/` everywhere. Resolved from the text: old
  L25 makes adding `scripts/` to a skill dir an Ask-first case, so a
  blanket ban would contradict it; the skill-level statement is the
  reading consistent with the file and with the same phrase in other
  skills (`lang-*`, `debug-*`).
- **MQ3** — Old L16 "~≤300–400 lines" and old L25 "~250 lines" are
  approximate, so the exact threshold has two readings (standard 2 wants
  a checkable one). Resolved from the text: the numbers stay verbatim,
  so no reading is chosen.
- **MQ4** — Old "Ask first" names no one to ask. Resolved from the text:
  the owner `docs/SDLC.md#asking-the-human` requires an operator ask for
  "anything in an Ask-first row"; the lead line routes there and adds no
  condition.
- **MQ5** — Old L41 has no stated trigger. Resolved from the text: the
  red flags are sentences a plan would contain, and old L41 follows them
  directly; "If your plan says one of these" states that link and adds
  no new case.
