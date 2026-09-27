# Groom — Instruction refinement: agent text that works across model strengths

DRAFT (pre-review)

<!-- At freeze, replace the draft marker above with this sentence and
delete this comment: Frozen record of the plan as reviewed at Groom on
<YYYY-MM-DD>. Not live: the tracker is the source of truth for tickets,
blockers and state. -->

- Chunk: `DER-288` · LLD: [lld.md](lld.md) · Date: `2026-09-27`
- Review: `pending` (filled at freeze)
- Tickets: filled at freeze

Each body names its LLD section, branch base and checks. K1–K10, the
every-item set and the rule-map format are defined in the LLD
(`#verify`, `#behavior-work-areas`, `#behavior-rule-map-format`); "old"
means `main` 7a11696. Rule maps go in `rule-maps/` beside this file.

## Items

### G1: A — writing standard and owner map
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (A) · Branch: `item/<ticket-id>-writing-standard` off `integrate/instruction-refinement`
- **Outcome** — `maintainers/writing-standard.md` holds HLD standard 1–10, the rule owners and protected rules with the LLD anchors, banned names, the rule-map format and checks K1–K10; `maintainers/AGENTS.md` routes to it in one line.
- **Acceptance** — anchors `#standard`, `#names`, `#rule-owners`, `#protected-rules`, `#rule-maps`, `#checks`; ≤150 lines; every rule traces to the HLD or LLD (no new rule); every-item set (rule map, clarifications, Unreleased line, K1–K4, K7), where the rule map covers the `maintainers/AGENTS.md` edit (the standard is a new file).
- **Verify** — `wc -l` ≤150; K3, K7, K10 on the diff; a read-through against HLD "Writing standard" and the LLD tables.
- **Blocked by** — `none` (source text is the accepted HLD and LLD) · **Blocks** — G49
- **Out of scope** — editing any other agent file. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: lands first (LLD Land). Rewrite items apply the standard from the HLD and LLD, which already publish it and the file and anchor map, so they need G1 only as land order.

### G2: B — eval rule, procedure and run format
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#eval-step`, `#trust-boundaries` · Branch: `item/<ticket-id>-eval-procedure` off `integrate/instruction-refinement`
- **Outcome** — `maintainers/AGENTS.md` has `## Evals` after `## Execution`; `maintainers/evals/` has `procedure.md` (from `maintainers/design/instruction-refinement/poc/kit/setup.md`, no arms, names no runner), `t1-*` and `t2-*` from the kit, `run-template.md` (from `maintainers/design/instruction-refinement/poc/kit/scoring-sheet.md`), `baseline.md`, `runs/`.
- **Acceptance** — `## Evals` matches the LLD block byte for byte; `procedure.md` carries Run setup (isolation, pre-run probe, tool-call gate, read-only export, reply modes) and the LLD eval-run rules (scratch directories outside the checkout, `local` adapter, bare local `origin`, never this repo's live `## Tracker`, token variables unset, git identity `eval@example.invalid`, unsigned commits), three repeats, candidate models (confirmed at B1), regression rule; run file and `baseline.md` columns as the LLD; K10 clean; **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — diff of `## Evals` against the LLD block is empty; K7, K10; diff touches only `maintainers/AGENTS.md`, `maintainers/evals/`, `CHANGELOG.md`.
- **Blocked by** — `none` (the LLD fixes rule and files; the kit is on project-main) · **Blocks** — G6
- **Out of scope** — T3 files (G3); runner choice; any run. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: if PR #7's `model-eval` meets the runner needs, `procedure.md` routes to it (land order); if #7 reaches `main` first, its `SKILL.md` joins by late insertion.

### G3: B — T3 Build task: card, key, groom fixture
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#eval-step` (T3 outline) · Branch: `item/<ticket-id>-eval-t3` off `integrate/instruction-refinement`
- **Outcome** — `maintainers/evals/t3-card.md`, `t3-key.md`, `t3-groom.md` per the LLD T3 outline.
- **Acceptance** — start state (T2 snapshot, toy items K1–K6 filed by hand from `t3-groom.md`, all `ready`, Epic `in_progress`, `Parallelism: serial`); card text, replies R1–R3 and end conditions as the LLD; key scores C1–C5 and Completed as the LLD; K10 clean; **security** reads it at Review with G2; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `t3-groom.md` fits `skills/sdlc-artifacts/templates/groom.md` and its Graph has seven `←` links; K7, K10.
- **Blocked by** — `none` (outline in the LLD; T2 fixtures in the kit) · **Blocks** — G6
- **Out of scope** — T1, T2, procedure (G2). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G4: OpenCode runner smoke test
- Type: Task (findings, no diff) · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#open`, `#eval-step` (Runner, Run setup) · Branch: none
- **Outcome** — a record of whether OpenCode, set up per Run setup on the operator's local model server, meets every runner need.
- **Acceptance** — version recorded; pass/fail with a phrase for each need: subagents in separate contexts minted and resumed by id, tool use (bash ≥5, git ≥2.42), tokens in/out summed over every agent, wall time, per-run timeout, context for the largest file, transcripts stay on the runner; pre-run probe and tool-call gate on one model; reply mode (a) checked; the manager posts the record on `DER-288`, K10 clean. A failed need → report to the operator, stop. A proxy or network bind → ask first (`security-hardening`).
- **Verify** — the record has a line per need, the probe and the gate.
- **Waits on** — the operator making the GPU available (a wait on this issue, not a link).
- **Blocked by** — `none` · **Blocks** — G5
- **Out of scope** — scoring T1–T3; picking another runner. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G5: Security read of the runner
- Type: Task (review item: verdict, no diff; **security**) · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#eval-step` (Runner), `#trust-boundaries` · Branch: none
- **Outcome** — a recorded **security** decision on OpenCode as set up in G4.
- **Acceptance** — findings on tool permissions, sandbox, isolation (separate user or container, empty home, no SSH agent), egress, telemetry, where transcripts are stored, any proxy bound to loopback; verdict; the manager posts it on `DER-288`. Fixes are items blocked by this one; a later runner change is a new read.
- **Verify** — each listed point has a finding; K10 on the posted text.
- **Blocked by** — G4 (reads the version and setup the smoke test settled) · **Blocks** — G6, G7
- **Out of scope** — the eval files (read at G2, G3 Review). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G6: B1 — baseline run on `main` 7a11696
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#eval-step`, `#behavior-work-areas` (B1) · Branch: `item/<ticket-id>-baseline-run` off `integrate/instruction-refinement`
- **Outcome** — T1–T3, three repeats each, on `main` 7a11696 for every confirmed model; one run file per model in `maintainers/evals/runs/`; a `baseline.md` row per model.
- **Acceptance** — run per `procedure.md`; models confirmed with the operator (variant, quantization, context); probe, gate and reply mode in each header; `## Regressions` reads `none (first run)`; evidence in own words; K10 clean; **security** reads the first run file at Review.
- **Verify** — one file per model named `<YYYY-MM-DD>-7a11696-<model-slug>.md`; 3/3 repeats per task; `baseline.md` rows match the files; K10.
- **Waits on** — the operator making the GPU available (a wait on this issue, not a link).
- **Blocked by** — G2 (procedure, T1–T2, run template), G3 (T3 card and key), G5 (runner cleared by **security**) · **Blocks** — G50
- **Out of scope** — runs on any other commit. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G7: Trial runs (hop and hold)
- Type: Task (Trial evidence) · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (Trial line) · PoC: `maintainers/design/instruction-refinement/poc/poc.md` · Branch: `item/<ticket-id>-trial-runs` off `integrate/instruction-refinement`
- **Outcome** — the 24 Trial runs scored; `poc.md` Results and Conclusion filled from the decision rules.
- **Acceptance** — per the PoC Setup: T1, T2 × arms A and B × weakest and frontier model × 3; sheets in `maintainers/design/instruction-refinement/poc/runs/`; hop verdict per rule 1; a failed hop or any mixed outcome → report to the operator, who decides; K10 clean.
- **Verify** — 24 sheets; the Results table matches them; the Conclusion cites the rule applied.
- **Waits on** — the operator making the GPU available (a wait on this issue, not a link).
- **Blocked by** — G5 (runner cleared by **security**) · **Blocks** — G50
- **Out of scope** — editing area C; a failed hop reworks C by late insertion. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: the LLD says Trial runs are not Build items; this ticket tracks the wait and the result only, and lands the sheets and `poc.md` update.

### G8: C1 — move the SDLC into the index, step files and people doc
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#paths--modules-file-and-anchor-map`, `#verify` · Branch: `item/<ticket-id>-sdlc-move` off `integrate/instruction-refinement`
- **Outcome** — old `docs/SDLC.md` lines sit verbatim in the mapped files with the map's headings and anchors; 21 internal links become `path#anchor`; the 4 broken inbound anchors (`AGENTS.md` `#entry`, `#brief`; `README.md`; `pr-lens` `#monthly`) are fixed; the index has How to read and the Read column.
- **Acceptance** — no other wording; `#asking-the-human` kept by `<a id>`; Stage table kept; the file and anchor map is the rule map; **security** reads the `pr-lens` line (vendor-derived body); the `pr-lens` `SOURCES.md` Notes line is added by G40, or by this item if G40 has not landed; one Unreleased line.
- **Verify** — the LLD C1 move check (only added routing lines); K7 on all changed files; K8; K9; every map anchor exists; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G9–G17, G18
- **Out of scope** — rewording; caps. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: diff exceeds 400 lines but is a verbatim move checked mechanically; a partial move would break anchors.

### G9: C2 — rewrite the SDLC index
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C2), `#behavior-protected-rules` · Branch: `item/<ticket-id>-sdlc-index` off `integrate/instruction-refinement`
- **Outcome** — `docs/SDLC.md` from the Trial draft (`maintainers/design/instruction-refinement/poc/rewrite/docs/SDLC.md`), ≤200; owner of `#tracker`, `#roles`, `#asking-the-human` rules.
- **Acceptance** — skill table gone: each note gets a map row naming its home (step file, `AGENTS.md`, or `SOURCES.md`), added there if missing; "designs in git" (old L96–99) → route to `docs/sdlc/conventions.md#designs-in-git`; Stage table kept; protected rows index `#roles`, `#tracker` kept or routed, **security** reads them at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤200; K9; K3, K7 on the file; rule map (start from `maintainers/design/instruction-refinement/poc/rule-maps/sdlc-index.md`) covers every non-blank old line; K10 before each push.
- **Blocked by** — G8 (rewrites the index C1 creates) · **Blocks** — G47
- **Out of scope** — step files. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G10: C3 — rewrite Entry, Brief, Repo
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C3), `#paths--modules-file-and-anchor-map` · Branch: `item/<ticket-id>-entry-brief-repo` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/entry-brief-repo.md` to the standard, ≤150.
- **Acceptance** — end-of-chunk Brief → numbered list; item Brief step 4 → condition table; "not too dirty to reason" → a checkable condition, else ask; copies owned elsewhere (AFK pick, step-agent ids, branch source, designs in git) → one-line routes; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — other step files. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G11: C4 — rewrite Plan, Trial, Spec, Documentation
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C4) · Branch: `item/<ticket-id>-plan-trial-spec` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/plan-trial-spec.md` to the standard, ≤150; owner of the UX review loop and operator acceptance (`#ux`).
- **Acceptance** — the UX copies collapse into `#ux`; "Monthly is not the security gate" → route to `trunk-changelog-monthly.md#monthly`; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — `ux-design` (G41). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G12: C5 — rewrite the Groom step
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C5) · Branch: `item/<ticket-id>-groom-step` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/groom-step.md` from the Trial draft (`maintainers/design/instruction-refinement/poc/rewrite/docs/sdlc/groom-step.md`), ≤150; owner of the groom reviewer id (`#names`).
- **Acceptance** — the operator clarifications on groom-review fixes, gate reasons and review-item verdicts applied; old L970–972 dropped; incoming-item branch and File land order → routes; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K3, K7 on the file; rule map (start from `maintainers/design/instruction-refinement/poc/rule-maps/groom-step.md`) complete; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — the `groom.md` template shape. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G13: C6 — rewrite Build and Review
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C6) · Branch: `item/<ticket-id>-build-review` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/build-review.md` to the standard, ≤150; owner of "notify only landed+verified" (`#definition-of-done`).
- **Acceptance** — DoD links `#review` and `branches-and-lands.md#land-path`; builder/verifier/reviewer, branch source, workers-and-security copies → routes to their owners; the Build copy of serialized lands → route to `docs/sdlc/branches-and-lands.md#land-path`; Review's "not deferred to Monthly" (old L867) → route to `docs/sdlc/trunk-changelog-monthly.md#monthly`; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — subagent and land rules (G15, G16). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G14: C7 — rewrite Trunk, Changelog, Monthly
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C7) · Branch: `item/<ticket-id>-trunk-changelog-monthly` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/trunk-changelog-monthly.md` to the standard, ≤80; owner of "Monthly is not the security gate".
- **Acceptance** — every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤80; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — other step files. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G15: C8 — rewrite branches and lands
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C8), `#behavior-protected-rules` · Branch: `item/<ticket-id>-branches-and-lands` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/branches-and-lands.md` to the standard, ≤120; owner of `#branches` and `#land-path`.
- **Acceptance** — "(an operator-confirmed rule)" dropped; protected `#never`: each old L945–961 bullet kept here or at its owner, **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤120; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — `AGENTS.md` branch paragraphs (G18). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G16: C9 — rewrite subagents
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C9), `#behavior-protected-rules` · Branch: `item/<ticket-id>-subagents` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/subagents.md` to the standard, ≤150; owner of `#step-agents` and `#item-agents`.
- **Acceptance** — pack vs point → "the manager holds the bodies and the child needs them: pack; else point"; tracker-writer, security and landed+verified copies → routes; protected `#tracker-writes` rows kept, **security** reads them at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — `grok-acp` (G25). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G17: C10 — rewrite conventions
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C10) · Branch: `item/<ticket-id>-conventions` off `integrate/instruction-refinement`
- **Outcome** — `docs/sdlc/conventions.md` to the standard, ≤100; owner of `#designs-in-git`; `#in-flight-map` kept.
- **Acceptance** — old L460–463 (manager marks `done` after land+verify) → route to `docs/sdlc/branches-and-lands.md#land-path`; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤100; K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (rewrites the file C1 creates) · **Blocks** — G49
- **Out of scope** — product-repo formats. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G18: C11 — slim the root `AGENTS.md`
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (C11), `#behavior-protected-rules` · Branch: `item/<ticket-id>-agents-slim` off `integrate/instruction-refinement`
- **Outcome** — `AGENTS.md` ≤100: what the repo is, `maintainers/` pointer, public-repo rule, load table (one row per need, one file each; Workers and Diagrams opt-in rows kept; `researcher` only in Research), intake route, related.
- **Acceptance** — role table, inventory, `cursor-cloud-agents-when`, language section, subagent and branch paragraphs out (each mapped to its owner); prose names L37, L100–101 fixed; public-repo rule rows all `kept`, **security** reads them at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l AGENTS.md` ≤100; K3, K7; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — G8 (its load table points each need at a file C1 creates and C1 retargets its links), G28 (the language section routes to the map E7 merges into `language-router`) · **Blocks** — G49
- **Out of scope** — `SOURCES.md` rows. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G19: D1 — `tracker-sdlc` to ≤150 (DER-265)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (D), `#behavior-protected-rules` · Branch: `item/<ticket-id>-tracker-sdlc` off `integrate/instruction-refinement`
- **Outcome** — `skills/tracker-sdlc/SKILL.md` ≤150; writer rule → route to index `#tracker`; Contract version, Model, Verbs, Claim, Map, Repair keep meaning; adapters: names only.
- **Acceptance** — Claim steps 1–5 kept; Never and Ask-first bullet counts equal; `adapters/local.md` recipe unchanged; **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤150; K5; K6 (`Contract version: 2` once); K3, K7; rule map complete; K10 before each push.
- **Blocked by** — `none` (the route target is in the LLD map) · **Blocks** — G49
- **Out of scope** — verbs, states, contract bump. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: delivers DER-265's wording bullets.

### G20: D2 — `sdlc-onboarding` from the Trial draft (DER-271)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (D) · Branch: `item/<ticket-id>-sdlc-onboarding` off `integrate/instruction-refinement`
- **Outcome** — `skills/sdlc-onboarding/SKILL.md` from `maintainers/design/instruction-refinement/poc/rewrite/skills/sdlc-onboarding/SKILL.md`, with no `maintainers/` link.
- **Acceptance** — `## Tracker` and `## Execution` formats it writes are unchanged; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7); the rule map starts from `maintainers/design/instruction-refinement/poc/rule-maps/sdlc-onboarding.md`.
- **Verify** — K2 (≤200); `grep -c 'maintainers/' skills/sdlc-onboarding/SKILL.md` = 0; K3, K7; rule map complete; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — DER-271's process bullets. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G21: D3 — `sdlc-artifacts` and templates
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (D), `#verify` (K6) · Branch: `item/<ticket-id>-sdlc-artifacts` off `integrate/instruction-refinement`
- **Outcome** — `<merge SHA>` → `<land SHA>`; `agents-stub.md` gains one bullet naming `## Tracker`; tracker-writer copy → route; `templates/changelog.md` L4 prose name fixed.
- **Acceptance** — template shapes and `tracker-skill.md` unchanged; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K6; K3, K7 on changed files; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — new templates. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G22: E1 — `discover-the-idea` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E) · Branch: `item/<ticket-id>-discover-the-idea` off `integrate/instruction-refinement`
- **Outcome** — the skill meets the standard; step-agent copies → route to `docs/sdlc/subagents.md#step-agents`.
- **Acceptance** — every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K1, K2, K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — the gather loop's meaning. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G23: E2 — `yagni` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E) · Branch: `item/<ticket-id>-yagni` off `integrate/instruction-refinement`
- **Outcome** — the skill meets the standard.
- **Acceptance** — every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K1, K2, K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — other skills. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G24: E3 — `buying-researcher` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E) · Branch: `item/<ticket-id>-buying-researcher` off `integrate/instruction-refinement`
- **Outcome** — `SKILL.md`, `references/` and `assets/` meet the standard.
- **Acceptance** — every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K1, K2, K3, K7 on changed files; rule maps complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — research method changes. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G25: E4 — `grok-acp` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E), `#behavior-protected-rules` · Branch: `item/<ticket-id>-grok-acp` off `integrate/instruction-refinement`
- **Outcome** — the skill meets the standard.
- **Acceptance** — permission posture, labels, own-item limits: every map row `kept`; **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K1, K2, K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — `packages/grok-acp/`. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G26: E5 — `security-hardening` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E), `#behavior-protected-rules` · Branch: `item/<ticket-id>-security-hardening` off `integrate/instruction-refinement`
- **Outcome** — the skill meets the standard.
- **Acceptance** — Never and Ask first keep their row counts; **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — the LLD `sed … | grep -c '^\| '` check equal old vs new for both sections; K1, K2, K3, K7; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — new rules. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G27: E6 — `modern-python` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E) · Branch: `item/<ticket-id>-modern-python` off `integrate/instruction-refinement`
- **Outcome** — the skill meets the standard.
- **Acceptance** — every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — K1, K2, K3, K7 on the file; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — tool choices. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G28: E7 — `language-router` owns the language map
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (E7) · Branch: `item/<ticket-id>-language-router` off `integrate/instruction-refinement`
- **Outcome** — `skills/language-router/SKILL.md` ≤250 owns the language map (old `AGENTS.md` L203–229 merged), the load-with list and the no-language turns (including `sdlc-onboarding`); it loads on any code turn.
- **Acceptance** — every merged `AGENTS.md` row mapped; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7) (K2 exempt).
- **Verify** — `wc -l` ≤250; K3, K7; rule map complete, no open MQ; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G18
- **Out of scope** — removing the section from `AGENTS.md` (G18). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G29: F — `tdd` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-tdd-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/tdd/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: the Notes cell uses the LLD `tdd` exception (`new body blob <sha>`); the SHA cell keeps its pin.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G30: F — `pr-review` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-pr-review-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/pr-review/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: prose section name at old L20 fixed; the distinct-reviewer copy → route to `docs/sdlc/subagents.md#item-agents`.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G31: F — `debug` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-debug-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/debug/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G32: F — `debug-pocock` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-debug-pocock-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/debug-pocock/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G33: F — `debug-anthropic` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-debug-anthropic-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/debug-anthropic/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: keeps the "Rewrite of anthropics/… @ `ebd7990c`" line (Apache-2.0 change notice).
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G34: F — `docs-google-style` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-docs-google-style-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/docs-google-style/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G35: F — `shell-safety` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-shell-safety-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/shell-safety/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G36: F — `verify-before-done` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-verify-before-done-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/verify-before-done/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: prose section name at old L17 fixed; verifier and landed+verified copies → routes to `docs/sdlc/subagents.md#item-agents`, `docs/sdlc/build-review.md#definition-of-done`.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G37: F — `golang-testing` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-golang-testing-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/golang-testing/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G38: F — `golang-security` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-golang-security-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/golang-security/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G39: F — `golang-safety` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-golang-safety-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/golang-safety/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G40: F — `pr-lens` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-pr-lens-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/pr-lens/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: keeps `@coldtea/pr-lens-cli@0.8.1`.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G41: F — `ux-design` light pass
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (F), `#behavior-vendor-derived-list`, `#trust-boundaries` · Branch: `item/<ticket-id>-ux-design-light` off `integrate/instruction-refinement`
- **Outcome** — `skills/ux-design/SKILL.md` gets naming, dedupe and real-defect fixes only; its `SOURCES.md` Notes cell gets the LLD note exactly. Also: the UX review-loop copy → route to `docs/sdlc/plan-trial-spec.md#ux`.
- **Acceptance** — no new upstream text, no upstream fetch; SHA column, license, tools and pins unchanged; change map (changed lines only); one Unreleased line; **security** reads the body at Review.
- **Verify** — `git diff 7a11696 -- SOURCES.md` changes only this row's Notes cell; K2, K3, K7, K10 on the diff.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — rewrites beyond the light pass. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G42: G — `lang-*` batch 1 (lang-c … lang-go)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (G) · Branch: `item/<ticket-id>-lang-batch-1` off `integrate/instruction-refinement`
- **Outcome** — `skills/<id>/SKILL.md` for `lang-c`, `lang-cpp`, `lang-csharp`, `lang-dart`, `lang-docker`, `lang-go` use the standard's names; lines repeating `language-router` rules (load-with list, one language skill) become one route line per file.
- **Acceptance** — change map (changed lines only); one Unreleased line.
- **Verify** — K1 (≤250), K2, K3, K7 on the 6 files; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — language advice. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G43: G — `lang-*` batch 2 (lang-java … lang-php)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (G) · Branch: `item/<ticket-id>-lang-batch-2` off `integrate/instruction-refinement`
- **Outcome** — `skills/<id>/SKILL.md` for `lang-java`, `lang-js-ts`, `lang-kotlin`, `lang-lua`, `lang-makefile`, `lang-php` use the standard's names; lines repeating `language-router` rules (load-with list, one language skill) become one route line per file.
- **Acceptance** — change map (changed lines only); one Unreleased line.
- **Verify** — K1 (≤250), K2, K3, K7 on the 6 files; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — language advice. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G44: G — `lang-*` batch 3 (lang-powershell … lang-rust)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (G) · Branch: `item/<ticket-id>-lang-batch-3` off `integrate/instruction-refinement`
- **Outcome** — `skills/<id>/SKILL.md` for `lang-powershell`, `lang-protobuf`, `lang-python`, `lang-ruby`, `lang-rust` use the standard's names; lines repeating `language-router` rules (load-with list, one language skill) become one route line per file.
- **Acceptance** — change map (changed lines only); one Unreleased line.
- **Verify** — K1 (≤250), K2, K3, K7 on the 5 files; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — language advice. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G45: G — `lang-*` batch 4 (lang-shell … lang-web-markup)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (G) · Branch: `item/<ticket-id>-lang-batch-4` off `integrate/instruction-refinement`
- **Outcome** — `skills/<id>/SKILL.md` for `lang-shell`, `lang-sql`, `lang-swift`, `lang-terraform`, `lang-web-markup` use the standard's names; lines repeating `language-router` rules (load-with list, one language skill) become one route line per file.
- **Acceptance** — change map (changed lines only); one Unreleased line.
- **Verify** — K1 (≤250), K2, K3, K7 on the 5 files; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — language advice. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G46: H — `docs/INTAKE.md` to the standard
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (H), `#behavior-protected-rules` · Branch: `item/<ticket-id>-intake` off `integrate/instruction-refinement`
- **Outcome** — `docs/INTAKE.md` meets the standard, ≤55.
- **Acceptance** — six numbered steps under `## Checklist`; **security** reads it at Review; every-item set (rule map, clarifications, Unreleased line, K1–K4, K7).
- **Verify** — `wc -l` ≤55; the checklist step count = 6; K3, K7; rule map complete; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — intake policy. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G47: I — people docs tone pass and role tables
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (I) · Branch: `item/<ticket-id>-people-docs` off `integrate/instruction-refinement`
- **Outcome** — `README.md`, `CONTRIBUTING.md`, `docs/ARCHITECTURE.md` pass a `docs-google-style` tone read; links point at the new layout; role tables = the index's seven roles and jobs; README "Improvise…" replaced per the clarification; `docs/ARCHITECTURE.md` L20 prose name fixed.
- **Acceptance** — change map; one Unreleased line; verifier checks tone against `docs-google-style`.
- **Verify** — K7 on the three files; role tables diff clean against the index roles table; K10 before each push.
- **Blocked by** — G9 (the role tables copy the roles and jobs C2 lands in the index) · **Blocks** — G49
- **Out of scope** — other people-doc content; `docs/how-software-gets-built.md`. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G48: J — stale lines in the tracker-sdlc HLD (DER-271)
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (J) · Branch: `item/<ticket-id>-tracker-hld-stale` off `integrate/instruction-refinement`
- **Outcome** — `maintainers/design/tracker-sdlc/hld.md` fixes only the lines DER-271 names as stale.
- **Acceptance** — the item quotes each DER-271 bullet it applies; no other line changes.
- **Verify** — the diff maps one-to-one to the quoted bullets; K7; K10 before each push.
- **Blocked by** — `none` · **Blocks** — G49
- **Out of scope** — DER-271's process bullets. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G49: Z — integrated check of the whole text
- Type: Task (review item: findings + verdict, no diff) · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#behavior-work-areas` (Z), `#verify` · Branch: none
- **Outcome** — a verdict on project-main's tip: K1–K10 on the tree, one copy per owner row, and each gate the index names resolves to a step file.
- **Acceptance** — each Duplicate-owners row: owner holds the rule, every copy is a route or gone; protected-rule checks rerun; findings list the check or row; the verdict says whether a whole re-check is needed. Fixes are items blocked by this one; the manager files them and links G50 to each.
- **Verify** — every K check and owner row has a result line.
- **Blocked by** — G1, G10–G27, G29–G48 (checks the tree those items land; G8, G9, G28 reach it through G10–G18 and G47) · **Blocks** — G50
- Notes: runs after G2 and G3 have landed, so the tree includes `maintainers/evals/` (land order, not a link).
- **Out of scope** — editing files. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G50: K — before-merge eval run
- Type: Task · Parent: `DER-288` · LLD: `maintainers/design/instruction-refinement/lld.md#eval-step`, `#behavior-work-areas` (K) · Branch: `item/<ticket-id>-final-run` off `integrate/instruction-refinement`
- **Outcome** — T1–T3, three repeats, on project-main's tip for every baseline model; one run file per model; a report for the PR into `main`, regressions first.
- **Acceptance** — run per `procedure.md` with the same runner, models and reply mode as the baseline (a change is recorded); regressions against `baseline.md` in each run file; K10 clean; the operator decides merge, fix or rerun.
- **Verify** — one file per baseline model; 3/3 repeats per task; K10 on the files and the report.
- **Waits on** — the operator making the GPU available (a wait on this issue, not a link).
- **Blocked by** — G49 (runs the text that passed the integrated check), G6 (compares against its baseline), G7 (its hop verdict decides whether the split layout K measures is final) · **Blocks** — `none`
- **Out of scope** — the `baseline.md` update after the merge (`## Evals` rule 4, at Trunk). **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

## Graph

- Wave 1: G1–G4, G8, G19–G46, G48
- Wave 2: G5 ← G4; G9–G17 ← G8 (each); G18 ← G8, G28
- Wave 3: G6 ← G2, G3, G5; G7 ← G5; G47 ← G9
- Wave 4: G49 ← G1, G10–G27, G29–G48
- Wave 5: G50 ← G49, G6, G7

Gates: G49 — review of the integrated text (one copy per owner, K1–K10
on the tree) before K spends GPU time. Harness items G4–G7 run beside
it, so it is gate-like only on the text side.

The PR into `main` (Trunk, not an item) needs G6, G7 and G50 `done`.
G4, G6, G7 and G50 wait on the operator making the GPU available; that
wait sits on each of those issues, not as a link, and no rewrite item
waits on it.

Land order (not blockers):

- G1, G2, G3 land first (LLD Land: A, B); G1 and G2 share
  `maintainers/AGENTS.md`. G6 lands in any order (fixed commit).
- G8 before every item that links a new path: G9–G18, G19–G21,
  G22–G28, G29–G41, G47. Items built before G8 lands rebase on it
  before Review so K7 passes.
- G42–G45 route to `language-router` by path and anchor; if G28 lands a
  different anchor, whichever lands later retargets.
- `CHANGELOG.md` (every item) and `SOURCES.md` (G9, G29–G41): the later
  land rebases and keeps every line.
- Shared files: `AGENTS.md` (G8, G9, G18); `skills/pr-lens/SKILL.md`
  (G8, G40); rewrites that add a route into another file land after that
  file's owner item.
