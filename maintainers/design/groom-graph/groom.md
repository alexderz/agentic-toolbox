# Groom — Groom graph (reviewed plan, blockers as the live graph)

Frozen record of the plan as reviewed at Groom on 2026-09-26. Not live:
the tracker is the source of truth for tickets, blockers and state.

- Chunk: `DER-275` · LLD: [lld.md](lld.md) · Date: `2026-09-25`
- Review: `groom-reviewer` — pass on 2026-09-26 at `04cbf57`
- Tickets: `G1` = `DER-279`, `G2` = `DER-280`, `G3` = `DER-281`,
  `G4` = `DER-282`, `G5` = `DER-283`

## Items

### G1: SDLC Groom, Build dispatch, and layout text

- Type: Task · Parent: `DER-275` · Branch: `item/<ticket-id>-sdlc-groom`
  off `integrate/groom-graph`
- LLD: `maintainers/design/groom-graph/lld.md#behavior-1-sdlc-groom`,
  `#behavior-2-other-sdlc-and-agents-edits`
- **Outcome** — `docs/SDLC.md` and root `AGENTS.md` state the reviewed
  Groom: draft → clean review → file from the reviewed SHA → freeze;
  blocker meaning, waves, gates by shape, review items, late insertion;
  Build dispatch up to the `Parallelism:` ceiling; `.agents/design/` in
  the layout as data.
- **Acceptance**
  - `### Groom` up to **Incoming item** matches LLD Behavior 1; the
    Incoming-item paragraph is unchanged.
  - Build dispatch sentence, layout row and data note, Subagents
    `groom_reviewer_id` sentence, `sdlc-onboarding` skill-table Notes,
    and root `AGENTS.md`:98 match LLD Behavior 2.
  - CHANGELOG Unreleased, Changed: one line citing `DER-275`.
  - DoD per SDLC Build: docs current, clean verifier, Review with
    `Reviewed-by:`.
- **Verify** — `grep -n 'max safe parallelism' docs/SDLC.md` empty; the
  frozen sentence appears once in `docs/SDLC.md`; anchors
  `#land-path-manager`, `#asking-the-human`, `#subagents-per-work-item`
  resolve; read-through: no label, stored cache, or verb added;
  `Contract version: 2` unchanged; style read of the new text.
- **Blocked by** — `none` (exact wording is in the LLD).
- **Blocks** — G5.
- **Out of scope** — moving HLD/LLD under `.agents/design/` (DER-271);
  how a chunk reaches `main` (DER-266); throttling logic.
- **Proposed fix** / **Removal alternative** / **Pick** / **Plan /
  Spec** — `n/a — split from accepted Spec`.
- Notes: CHANGELOG is shared with G2 and G3; whichever lands later
  rebases and keeps every line (land order, not a blocker).

### G2: `groom.md` template and chunk note in `sdlc-artifacts`

- Type: Task · Parent: `DER-275` · Branch: `item/<ticket-id>-groom-template`
  off `integrate/groom-graph`
- LLD: `maintainers/design/groom-graph/lld.md#behavior-3-sdlc-artifacts`
- **Outcome** — `sdlc-artifacts` has a Groom plan template and map row;
  the chunk template points at `groom.md` and the wave-view comment.
- **Acceptance**
  - `templates/groom.md` matches LLD Behavior 3 (draft marker, `Review:`
    line with SHA, Items with the self-contained, no-secrets placeholder,
    Graph, Gates); ≤40 lines.
  - `SKILL.md` map row and description; `templates/chunk.md` `Groom:`
    line and **Wave view** bullet; SOURCES `sdlc-artifacts` Notes.
  - CHANGELOG Unreleased, Added: one line citing `DER-275`.
  - DoD per SDLC Build: docs current, clean verifier, Review with
    `Reviewed-by:`.
- **Verify** — `wc -l` budgets (template ≤40, `chunk.md` ≤26,
  `SKILL.md` ≤80); the frozen sentence appears once in the template;
  `maintainers/design/groom-graph/groom.md` fits the template's shape.
- **Blocked by** — `none` (template text is in the LLD; the SDLC link to
  it resolves once G1 and G2 both land on project-main, not trunk).
- **Blocks** — G5.
- **Out of scope** — other templates; a stored wave cache.
- **Proposed fix** / **Removal alternative** / **Pick** / **Plan /
  Spec** — `n/a — split from accepted Spec`.
- Notes: CHANGELOG Added is shared with G3; the later land rebases and
  keeps both lines.

### G3: `sdlc-onboarding` Execution area

- Type: Task · Parent: `DER-275` · Branch: `item/<ticket-id>-execution-area`
  off `integrate/groom-graph`
- LLD: `maintainers/design/groom-graph/lld.md#behavior-4-sdlc-onboarding-execution`
- **Outcome** — onboarding asks for and records `## Execution`
  (`Parallelism: max`, `serial`, or `at most <N>`) at first touch or
  when its Check fails; any other value fails the Check.
- **Acceptance**
  - Intro, When line, and `## Execution` (Discover, Propose, Write,
    Check) match LLD Behavior 4, including the `max` bound and
    "**security** reads any change to `## Execution`"; `SKILL.md` ≤200.
  - SOURCES `sdlc-onboarding` Notes updated.
  - CHANGELOG Unreleased, Added: one line citing `DER-275`.
  - DoD per SDLC Build: docs current, clean verifier, Review with
    `Reviewed-by:`.
- **Verify** — `wc -l skills/sdlc-onboarding/SKILL.md` ≤200; `#branch`
  resolves; the Check accepts exactly the three forms (read-through with
  `max`, `serial`, `at most 4`, `at most 0`, `lots`); **security** read.
- **Blocked by** — `none` (independent file; block text is in the LLD).
- **Blocks** — `none`.
- **Out of scope** — any tracker schema or contract change.
- **Proposed fix** / **Removal alternative** / **Pick** / **Plan /
  Spec** — `n/a — split from accepted Spec`.
- Notes: CHANGELOG Added is shared with G2; the later land rebases and
  keeps both lines.

### G4: Record this repo's Parallelism ceiling

- Type: Task · Parent: `DER-275` · Branch: `item/<ticket-id>-execution-value`
  off `integrate/groom-graph`
- LLD: `maintainers/design/groom-graph/lld.md#behavior-5-this-repo-and-changelog`
- **Outcome** — `maintainers/AGENTS.md` has `## Execution` with the
  value the operator chose.
- **Acceptance**
  - Two lines after the `## Tracker` block: `## Execution`, then
    `Parallelism: max`, `serial`, or `at most <N>` as the operator
    chose (proposed `max`).
  - The `## Tracker` pointer stays the next non-empty line after its
    heading (Map check).
  - Commit `[<ticket-id>] Record execution: <value>`; **security** read;
    landed through Review with `Reviewed-by:`.
- **Verify** — the LLD Behavior 4 Check passes on `maintainers/AGENTS.md`;
  the `tracker-sdlc` Map check still passes.
- **Blocked by** — `none` (format fixed by the LLD; the operator's
  answer is a wait on this issue, not a link).
- **Blocks** — `none`.
- **Out of scope** — CHANGELOG (maintainer note, not a deliverable).
- **Proposed fix** / **Removal alternative** / **Pick** / **Plan /
  Spec** — `n/a — split from accepted Spec`.

### G5: Blind replay of DER-252 against the landed rules

- Type: Task (review item: output is findings + verdict, no diff) ·
  Parent: `DER-275` · Branch: none
- LLD: `maintainers/design/groom-graph/lld.md#appendix-replay-of-der-252`
- **Outcome** — a clean agent shows whether the landed Groom text,
  applied blind, reproduces the LLD replay of DER-252.
- **Inputs** — landed `docs/SDLC.md` Groom and Build,
  `skills/sdlc-artifacts/templates/groom.md`,
  `maintainers/design/tracker-sdlc/lld.md` (Groom plan; Behavior 4
  adapter outline), DER-252 children DER-254…DER-262, DER-268, DER-270
  (read-only), and their recorded links: G2–G6 ← G1; G2 ← G7;
  G8 ← G2, G7, G9; G7 related to G1; G10, G11 none; G7 filed while G2
  was in progress; G9 filed from G8's verdict while G8 was in progress.
- **Acceptance**
  - Blind: derive the results from the inputs before opening the LLD
    Appendix; then compare and list every difference.
  - Draft G1–G6 as a `groom.md` and review it: needless G3–G5 (and G6)
    ← G1 flagged; G2 ← G1 kept.
  - Insert G7, G8, G9, G10, G11 in order; give the open waves after
    each; catch the missing G8 ← G3–G6; G7 blocking in-progress G2 asks
    first; for G8/G9, refuse the cycle **and** propose the review-item
    split (G8 closes with its verdict; G9 ← G8; any re-check is a new
    item ← G9).
  - Findings with the SDLC line each rule came from, and a verdict. The
    agent reports; the manager posts them as one comment on `DER-275`.
    Fixes become new items (late insertion).
- **Verify** — the comparison list; every Appendix step is matched or
  its difference is explained.
- **Blocked by** — G1 (replays the landed Groom text), G2 (drafts with
  the landed template).
- **Blocks** — `none`.
- **Out of scope** — editing files; the Execution area (the replay does
  not exercise it).
- **Proposed fix** / **Removal alternative** / **Pick** / **Plan /
  Spec** — `n/a — split from accepted Spec`.

## Graph

- Wave 1: G1, G2, G3, G4
- Wave 2: G5 ← G1, G2

Gates: `none` — G5 is a final check with nothing after it; no
integration or bottleneck need forces one. Shared CHANGELOG lines
(G1, G2, G3) are land order, not blockers.
