# PoC — Do the writing standard and the split SDLC hold across model strengths?

- Date: `2026-09-26`
- HLD: [../hld.md](../hld.md) (PoC questions)
- Ticket: DER-288

## Required

- **Question** — Two arms: **A**, current text at main `7a11696`;
  **B**, the rewrite in [rewrite/](rewrite/) (SDLC index,
  `docs/sdlc/groom-step.md`, `skills/sdlc-onboarding/SKILL.md`), with
  every other file unchanged.
  1. Does the weakest model make the index → step-file hop in arm B, or
     skip it?
  2. In arm B, do checklist passes hold or rise and token counts fall
     compared with arm A, on each model?
  3. Does the frontier model hold in arm B: no C item that passed in
     arm A fails in arm B?

- **Setup** — Kit: [kit/](kit/). Harness needs and the skills-home
  build per arm: [kit/setup.md](kit/setup.md). Tasks: T1 onboarding
  ([card](kit/t1-card.md), [key](kit/t1-key.md)) and T2 Groom
  ([card](kit/t2-card.md), [key](kit/t2-key.md), fixture
  [t2-lld.md](kit/t2-lld.md)). Models: the weakest local Qwen variant
  (from the harness notes) and one frontier model. Three repeats per
  task, arm, and model: 24 runs (repeat runs varied 11–33% in duration,
  turns, and size; the checklist repeated identically). The runner must
  support subagents, so C5 is always scored. Score with
  [kit/scoring-sheet.md](kit/scoring-sheet.md).

  Rule maps (a reviewer checks each draft kept its meaning):
  [onboarding](rule-maps/sdlc-onboarding.md),
  [index](rule-maps/sdlc-index.md), [Groom](rule-maps/groom-step.md).
  Meaning questions and their answers (review, operator clarification
  2026-09-27) are listed in each.

- **Evidence** — One scoring sheet per run in `runs/` here
  (`<YYYY-MM-DD>-<task>-<arm>-<model-slug>-r<n>.md`). The Results table
  below summarizes them: C items and Completed as passes out of 3,
  tokens and wall time as median and range. Transcripts stay on the
  harness; nothing in git names a host, IP, model-server URL or port, a
  path outside the repo, a key or token, or a person, and evidence is in
  own words, never quoted model output.

- **Decision rules**
  1. **Hop (Q1).** Arm B, weakest model, T2: in 2 or more of the 3
     repeats the sheet shows no read of `docs/sdlc/groom-step.md` before
     the first `groom.md` write, or a read of `not-yet-split.md` in full
     instead → the hop failed.
  2. **Fallback.** Hop failed → Spec uses one slimmed `docs/SDLC.md`
     (~550 lines) instead of the split. Decided before Spec; the HLD
     layout row changes by a note here, and the operator is told.
  3. **Q2 holds** when, on each model and each task, no C item has
     fewer passes (out of 3) in arm B than in arm A. Median tokens in
     per arm are reported beside it to answer "do tokens fall"; they
     are never a pass bar.
  4. **Q3 holds** when, on the frontier model, no C item has fewer
     passes in arm B than in arm A.
  5. Any other outcome (mixed, or both arms fail the same item) → report
     to the operator with the sheets; the operator decides
     ([Asking the operator](../../../../docs/SDLC.md#asking-the-human)).
     A rerun happens only on the operator's call.

- **Conclusion** — Pending (harness not available yet).

- **What we will not treat as product**
  - The drafts in `rewrite/`: they test the standard; Build rewrites
    the real files from the LLD.
  - `docs/sdlc/not-yet-split.md`: a trial-only copy.
  - The numbers: three repeats per cell; they can show a hop failure or
    a clear regression, not a benchmark.
  - The kit: input to work area B (the eval step), not its final form.

## Known confounds

- Arm B still holds the full old text in `not-yet-split.md`: an agent
  that reads it in full sees both versions. The routing fields on the
  sheet record this.
- Root `AGENTS.md` is unchanged in both arms; its `#entry` / `#brief`
  links land on the arm B index top, not a section.
- Arm A's `sdlc-onboarding` links a worked example in
  `maintainers/design/tracker-sdlc/ux.md`; the export has no
  `maintainers/`, so that link is dead in arm A (arm B drops it,
  DER-271).
- T2 starts from one shared T1 snapshot, so T2 does not depend on each
  run's own T1 output.

## Results

| Task | Model | Arm | Completed | C1 | C2 | C3 | C4 | C5 | Tokens in / out | Wall | Hop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Optional

- Throwaway tree: scratch directories outside this repo, one per run
  ([kit/setup.md](kit/setup.md)).
