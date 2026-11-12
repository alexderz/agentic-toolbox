# Rulings and guardrails — ask less (DER-712)

Format: `Ruling: <what> — <why> — <cost if wrong>` and `Guardrail:
<what> — <why> — <what it costs> — <how to remove it>`. The operator
reviews this log at each touchpoint. Ids keep their original numbers;
gaps are entries that concerned only the throwaway Trial's private data
or other projects and are not carried here. R7–R19 settle the
refiner's minor points; R34 onward are the architect's calls at Plan.

## Rulings

### Brief

- R1. Ruling: chunk slug `ask-less`, project-main `integrate/ask-less` — matches the chunk name — rename a branch.
- R2. Ruling: keep this log outside the repo until project-main exists — no toolbox writes before the brief is confirmed — a file move.
- R3. Ruling: ask ids continue from the highest id already in use (SD-Q17 onward) — ids are never reused — renumber before sending.
- R4. Ruling: the refiner's checklist is a `## Refine` section of `discover-the-idea` (the skill that owns the brief), not a new skill — avoids a new skill id and `SOURCES.md` row; a **security** cut is needed either way (`AGENTS.md`, Skill ids row) — move a section.
- R5. Ruling: the rulings log format is one line in the SDLC plus a path rule in `conventions.md`, no template — one line needs no template — add a template later.
- R6. Ruling: the chunk's eval run also records the first baseline (run on `main`, then on the PR head) — `baseline.md` is empty and `maintainers/AGENTS.md` § Evals rule 5 asks for a model's row before the next agent-text PR — one extra run per model.
- R7. Ruling: the over-ask fail is a new C6 "no unneeded ask", scored on every task from reply rows each card marks as over-asks — keeps missed asks (C1) and unneeded asks apart; with no baseline, the table change costs nothing — fold C6 into C1 later.
- R8. Ruling: the baseline run on `main` is scored with the PR head's keys, and the run file says so — otherwise C6 has no baseline — rescore from transcripts.
- R9. Ruling: auto mode and production are declared in an optional `## Autonomy` section of the product `AGENTS.md` (`Auto mode: on|off`, `Production: <what is real>`); absent means the defaults — leaves `## Execution` and its onboarding check unchanged — rename a section.
- R10. Ruling: the asks file is `asks.md` beside `rulings.md` in the chunk's design folder — one place per chunk, found by path — move a file.
- R11. Ruling: the pull floor is the liaison's first step of every operator turn (read open asks in each active chunk's asks file), plus a read on every child stage result; no hook — works on any host — add a schedule where the host has one.
- R12. Ruling: "child done" is signalled by its stage result, which is always persisted (`stage-result.md` Rules step 1); ask status comes from the asks file — reuses an existing contract — add a tracker signal later.
- R13. Ruling: protected security and tracker Ask-first rows stay as they are, and the SDLC keeps "anything in an Ask-first row" — they are protected rules with mechanical checks (writing standard, Protected rules); loosening them is a security decision, not this chunk's — a later security-reviewed item.
- R14. (Changed 2026-11-11 by the operator, GR9 removed.) Ruling: Parallelism defaults to `max` with no onboarding question; only the tracker ask stays, sent in the brief-touchpoint batch — the operator removed the Parallelism guardrail; the tracker touches shared resources only the operator knows — reinstate the question.
- R15. Ruling: `needs_input`'s `question` reads `asks: <path> <ids>`; no new field — the schema rejects unknown keys (`stage-result.md` Schema) — a schema field later.
- R16. Ruling: ask ids are unique within a project and never renumbered; a project may prefix them (as `SD-Q<n>`) — matches existing practice — renumber in one file.
- R17. (Superseded by R31.) Was: T3's fixture gets two traps and no new eval task.
- R18. Ruling: leave "AFK" in `debug-pocock/SKILL.md` — plain English in a vendor-derived body; changing it needs intake — a one-word intake later.
- R19. Ruling: standing permissions are recorded in the confirmed brief, with a pointer in the Entry comment on the Epic — A4 says what to ask, not where; the Entry comment already exists — a second comment.

### Trial (throwaway, before Spec)

- R24. Ruling: the asking text splits what to build (the operator's unless the brief settles it) from how (cost to undo decides), lists how-questions that never count as what, and lets earlier operator words imply a standing permission; Spec starts from draft v3, whose content the HLD restates — the Trial showed that cost to undo alone lets models decide product questions and read a recommended default as a granted permission, and that "what is always theirs" alone brings every unneeded ask back — rework at Spec if an eval model disagrees.
- R26. Ruling: asks are scored by the operator's judging rule — a follow-up or discussion means the ask was needed; a plain yes means it was unneeded unless it was a one-way door or an action only the operator can do; a reply in a different direction is excluded — the operator is the judge, and the rule needs no labeller; it now scores C6 and T4 — rescore from stored transcripts.

### Scope additions and gate answers

- R29. Ruling: the move out of `docs/` is Chunk A's first item, move-only, before any rewrite — avoids editing every file twice and keeps the rewrite diffs readable, as DER-288's move did — re-order two items.
- R30. Ruling: `docs/INTAKE.md` moves with the SDLC as `skills/sdlc/references/intake.md`; human-facing pages stay in `docs/` — intake is an agent procedure; the split is agent text vs human docs — move one file back.
- R31. Ruling: the browser Breakout job is the over-ask measure (scripted replies; scored by R26: unneeded asks, needed asks kept, unrequested guardrails disclosed), and T1–T3 still run on both eval models for the merge rule — `maintainers/AGENTS.md` § Evals requires T1–T3; the operator named the job, not a waiver — drop T1–T3 if the operator says Breakout replaces them.
- R32. Ruling: the Breakout job runs on both eval models, current text vs Chunk A text, 3 repeats each — matches the eval procedure's repeat count — 12 runs; fewer if one model is slow.

### Plan (architect)

- R34. Ruling: `docs/SDLC.md` stays as a pointer page of at most 8 lines naming `skills/sdlc/SKILL.md` and its `#asking-the-human` — product-repo stubs written before the move cite the old path, and DER-288 kept that path for the same reason — one stale file until it is removed (later list).
- R35. Ruling: the liaison procedure (L2–L5) lives in a new `skills/sdlc/references/liaison.md` that the manager reads; the child's three steps (answer from the record, report to the manager, keep working) stay in the index — keeps the index under 250 lines and keeps each actor's rule in one file (writing standard 6) — fold it into the index if the budget allows.
- R36. Ruling: one writer per asks-file field: the chunk's manager writes asks; the liaison writes `status` and `answer`; role agents report asks to their manager and never write the file — parallel children in separate worktrees would otherwise conflict on one file, and it mirrors "only the manager writes the tracker" — a per-child asks file.
- R37. Ruling: a new template `asks.md` holds the asks-file section shape; `ask-human.md` stays the operator-message shape and becomes the batch and touchpoint message — one shape per template, as the other templates do — merge them into one template.
- R38. Ruling: in a product repo, `rulings.md` and `asks.md` go in `.agents/design/<chunk-slug>/` beside `groom.md` (one layout line edited in place); in this skills home, `maintainers/design/<chunk-slug>/`; an item outside any chunk logs its rulings in a ticket `comment` by the manager — `.agents/design/` is already the agent-data design folder and is read as data, and `conventions.md` is at its cap — move two files.
- R39. Ruling: the HLD-review recommendation reads "more than three components, a new trust boundary or a new technology" — "about three" is not checkable (writing standard 2) — change the number.
- R40. Ruling: T4 ends when the first item is landed and verified on project-main — that covers Entry through Review, where the asking happens, in a bounded run — extend the end point to every item.
- R41. Ruling: T4's card sets a 4-hour wall-time cap in place of the procedure's 2 hours, and the procedure's rule reads "the card's cap, else 2 hours" — a run through Brief, Plan, Spec and a first land does not fit in 2 hours — see GR13.
- R42. Ruling: C6 is pass/fail per repeat on T1–T4, and T4 also reports counts (unneeded asks, needed asks kept, guardrails added and disclosed) — pass/fail fits the run-template table; counts show size — counts on every task later.
- R43. Ruling: T3's ask triggers change with the Build text: "start or land past an open blocker" passes on resolve-or-defer, "wrong kind of change" passes on escalation to the item rung, force-push stays an ask — the brief names only the second, but the Open blockers rewrite changes the first too — revert one row.
- R44. Ruling: this chunk's rule maps go in `maintainers/design/ask-less/rule-maps/`, with `Old: <path> at main c26f424`; the writing standard's rule-map rule names the chunk folder and its base commit instead of DER-288's — that rule hardcodes DER-288's folder and commit — keep a per-chunk note instead.
- R45. Ruling: writing standard 9 reads "rewrites may grow up to their cap; a cap that needs a new file → add the file and log a ruling; dropping a rule the operator asked for needs their sign-off", and K2 checks the cap, not the old length — SD-Q22 granted growth to caps and new files; S1 keeps the sign-off for drops — restore "never grow".
- R46. Ruling: Ask-first lists in skills other than `yagni` and the protected rows are not reworded in Chunk A — the brief reconciles only `yagni`; several are vendor-derived and need intake — a later audit item.
- R47. Ruling: item A0 carries a path map (old path and anchor → new), not rule maps — no rule changes in a move; DER-288's move was exempt from caps and K1 the same way — write rule maps for A0.
- R48. Ruling: the SDLC index's cap becomes 250 lines (a `SKILL.md` cap) instead of 200, with the asking section and touchpoints at most 85 lines; over budget → move the door table's examples, not a rule — the brief sets the index at ≤250; a section budget keeps the "principles, not rules" check honest — raise the section budget.
- R49. Ruling: agents read only the `Auto mode:` and `Production:` lines of `## Autonomy`; the rest of the section is data — same posture as `## Execution`'s one line — parse more lines later.
- R50. Ruling: `stage-result.md`'s `needs_input` example changes from a retry-limit question to an `asks:` pointer — the old example is a parameter value, a how-question the new rules settle without asking — keep both examples.
- R51. Ruling: the release guard counts a T4 drop in needed asks kept, against the baseline, as a regression — the operator's guard covers "any drop in required asks", and T4 is where needed asks are counted — guard on C-items only.

## Guardrails (G1)

Only guardrails this chunk added without being asked. Ones a toolbox
or task rule requires (the procedure's security reads, isolation and
2-hour cap; the protected rows) are not listed.

- GR6. Guardrail: release guard — any eval regression against the baseline, or any drop in required asks, means no merge and a report to the operator — protects a public, permanent merge into `main` — one noisy repeat can turn auto-ship into a report and a wait — approved with SD-Q18; remove by answering "auto-ship, no guard".
- GR8. Guardrail: keep the protected security and tracker Ask-first rows unchanged (R13) — they are security-owned protected rules — some two-way-door asks remain (for example CORS or rate-limit changes) — a later security-reviewed item to loosen them.
- GR9. (Removed by the operator, 2026-11-11.) Was: onboarding's Parallelism question stays an ask. Now: `Parallelism: max` by default, no question (R14).
- GR10. (Removed by the operator, 2026-11-11.) Was: a standing permission counts only when written down for this work. Now: the operator's earlier words may imply one (R24).
- GR11. (Changed by the operator, 2026-11-11.) Guardrail: deleting beyond what the chunk created is allowed when the agent weighs the maintenance impact (links, readers, downstream copies) and logs a ruling that names it — repo content others read is not disposable — one ruling per such delete — widen the delete list in the brief.
- GR13. Guardrail: T4's 4-hour wall-time cap per repeat (R41) — a hung run must not hold the runner; it raises the procedure's existing 2-hour cap rather than adding a new one — a slow but healthy repeat is cut and scored Completed `no` — raise or drop the cap in `t4-card.md`.
- GR14. Guardrail: agents write `## Autonomy` only from the operator's written words — auto mode answers every "theirs" question, one-way doors included, so it is a standing permission (A4) and protects one-way doors (G3) — an agent cannot turn auto mode on for a repo where the operator only implied it — let implied words count, as R24 does for other permissions.
