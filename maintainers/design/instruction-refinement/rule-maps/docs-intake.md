# Rule map — `docs/INTAKE.md`

Item: DER-336 (H).

Old: `docs/INTAKE.md` at main 7a11696, lines 1–55.
New: [`docs/INTAKE.md`](../../../../docs/INTAKE.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected row touched: `docs/INTAKE.md` checklist. Check: six numbered
steps under `## Checklist`, old and new. Every row below is **kept**; no
step or requirement changes. **security** reads it at Review. Headings
and anchors kept: `#checklist`, `#workers`, `#layout-only-exception`.
Step numbers kept (`docs-sdlc.md` cites "step 4"). Operator
clarifications (2026-09-27): none of their subjects occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept verbatim | L1 |
| 3 | Checklist applies before any third-party skill body lands | kept verbatim | L3 |
| 4–5 | **security** owns this gate; workers (remote agents, local CLIs, mirrors) do not bypass it | kept; the list moves out of the parenthesis (standard 8); "go through it" names the allowed action (standard 7) (MQ1) | L4–5 |
| 7–9 | First-party files written in this repo (this checklist, `security-hardening`, language guides) are not vendor intake; still no secrets or `scripts/` | kept; the parenthesis becomes "for example" (MQ2); "must not ship" → imperative "Ship them without" | L7–9 |
| 11 | Heading "Checklist" | kept (`#checklist`) | L11 |
| 13–16 | Step 1: clone or fetch + checkout; no marketplace install; no `npx` installer, runner, or "add this skill"; no second process pack beside this repo's ids | kept; parenthesis → colon; "Do not" → "Never", the step head "Clone" is the allowed action | L13–16 |
| 17–20 | Step 2: never copy `scripts/`; never run upstream install, postinstall, bootstrap; executable helpers untrusted until **security** says otherwise, default drop | kept; "default is drop them … until security says otherwise" → "Drop … keep one only if **security** clears it" (allowed action beside "never") | L17–19 |
| 21–24 | Step 3: run SkillSpector, cisco skill-scanner, and/or a verified obielin skillguard; verify the tool's GitHub org before trusting binary or action; name collisions are not a clear | kept; "and/or" → "one or more of" (MQ3); the parenthesis becomes its own sentence | L20–23 |
| 25–27 | Step 4: pin SHA in `SOURCES.md` before the body; row names upstream, SHA, license, notes; empty SHA → no body; first-party rows use `first-party` | kept; "Empty SHA means no body" → if/then; imperative | L24–26 |
| 28–31 | Step 5: rewrite ≤250 lines, least privilege; no verbatim vendor `SKILL.md`; compress; review skills must not write; no secrets; no extra bodies in the same PR unless **security** asked | kept; "compress" sits beside "never paste" (standard 7); "Review skills must not write" verbatim (MQ4) | L27–30 |
| 32–33 | Step 6: pin stays until a later **security**-cleared bump; no marketplace sync, no "latest", no unattended vendor pull | kept; first sentence → imperative; second verbatim | L31–32 |
| 35 | Heading "Workers" | kept (`#workers`; linked from `poc/rewrite/skills/sdlc-onboarding`) | L34 |
| 37–39 | Remote-agent PRs still need a security clear; remote authoring no exemption; Build DoD: diff matches the pinned SHA, or `first-party` for first-party prose | kept; singular; the parenthesized condition becomes its own sentence (standard 8) | L36–38 |
| 41–44 | Product-repo `.agents/tracker/SKILL.md`, each one a governing `## Tracker` names (root, or a subdirectory whose `AGENTS.md` the root `AGENTS.md` or `CLAUDE.md` names): no SOURCES row; **security** reads the change that adds or edits it | kept; the scope moves out of the parenthesis into its own sentence, words unchanged | L40–43 |
| 44–46 | It holds no tokens, no `scripts/` files, no executable blocks except the fenced shell recipe from `adapters/local.md` | kept; numbered **security** step (standard 1) | L44–46 |
| 46–48 | **security** compares the recipe with the adapter's current text; only placeholder fills and baked-in gotchas may differ | kept verbatim, as a **security** step | L47–48 |
| 48–49 | Any other executable content fails the read | kept; **security** step, active voice | L49 |
| 51 | Heading "Layout-only exception" | kept (`#layout-only-exception`) | L51 |
| 53–54 | Empty skill directories holding only `.gitkeep` (layout, no `SKILL.md`, no scripts) are OK without scan | kept; the parenthesis becomes a sentence after a colon | L53–54 |
| 54–55 | Intake and scanners start when a body, script, or third-party file would land | kept; imperative "Start" | L54–55 |

## Meaning questions

- **MQ1** — Old L4–5 "Workers … do not bypass it" repeats the owner rule
  "Workers do not bypass security" (`docs/SDLC.md#roles`), whose worker
  list differs (agents, CI bots). A route would drop "local CLIs" and
  "mirrors" from this gate. Resolved from the text: `docs/INTAKE.md` owns
  third-party intake and the rule-owner table does not list it as a copy
  to route; the line stays here, scoped to this gate, with its list.
- **MQ2** — Old L7–8 parenthesis: exhaustive list or examples? Resolved
  from the text: `SOURCES.md` lists other first-party skills (for example
  `tracker-sdlc`) that are not vendor intake either, so the list is
  examples; "for example" keeps that reading.
- **MQ3** — Old L21 "and/or": resolved from the text; it means at least
  one of the three scanners, which "one or more of" states. No scanner
  becomes required or optional.
- **MQ4** — Old L30 "Review skills must not write" has no stated object
  (files, tracker, comments). Resolved from the text: kept verbatim, so
  no reading is chosen.
