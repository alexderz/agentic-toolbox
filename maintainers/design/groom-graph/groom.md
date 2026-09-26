# Groom — Groom graph (reviewed plan, blockers as the live graph)

DRAFT (pre-review)

- Chunk: `DER-275` · LLD: [lld.md](lld.md) · Date: `2026-09-25`
- Review: `<groom reviewer label>` — pass on `<date>` (filled at freeze)
- Tickets: `G1` = `<id>`, `G2` = `<id>`, `G3` = `<id>`, `G4` = `<id>`,
  `G5` = `<id>` (filled at freeze)

Every item: Type Task · Parent `DER-275` · Branch
`item/<ticket-id>-<short-slug>` off `integrate/groom-graph` · Proposed
fix, Removal alternative, Pick, Plan / Spec: `n/a — split from accepted
Spec`. DoD per SDLC Build (changelog line, docs current, clean verifier,
Review with `Reviewed-by:`).

## Items

### G1: SDLC Groom, Build dispatch, and layout text

- LLD: `lld.md` Behavior 1 and 2
- **Outcome** — `docs/SDLC.md` and root `AGENTS.md` state the reviewed
  Groom: draft → clean review → file → freeze; blocker meaning, waves,
  gates by shape, late insertion; Build dispatch up to the ceiling.
- **Acceptance**
  - `### Groom` up to **Incoming item** matches LLD Behavior 1; the
    Incoming-item paragraph is unchanged.
  - Build dispatch sentence, product-repo layout row, Subagents
    `groom_reviewer_id` sentence, `sdlc-onboarding` skill-table Notes,
    and root `AGENTS.md`:98 match LLD Behavior 2.
  - CHANGELOG Unreleased, Changed: one line citing `DER-275`.
- **Verify** — `grep -n 'max safe parallelism' docs/SDLC.md` empty; the
  frozen sentence appears once in `docs/SDLC.md`; anchors
  `#land-path-manager`, `#asking-the-human`, `#subagents-per-work-item`
  resolve; `Contract version: 2` unchanged; style read of the new text.
- **Blocked by** — `none` (exact wording is in the LLD).
- **Blocks** — G5.
- **Out of scope** — moving HLD/LLD under `.agents/design/` (DER-271);
  how a chunk reaches `main` (DER-266); throttling logic.

### G2: `groom.md` template and chunk note in `sdlc-artifacts`

- LLD: `lld.md` Behavior 3
- **Outcome** — `sdlc-artifacts` has a Groom plan template and map row;
  the chunk template points at `groom.md` and the wave-view comment.
- **Acceptance**
  - `templates/groom.md` matches LLD Behavior 3 (draft marker, header,
    Items, Graph, Gates); ≤40 lines.
  - `SKILL.md` map row and description; `templates/chunk.md` `Groom:`
    line and **Wave view** bullet; SOURCES `sdlc-artifacts` Notes.
  - CHANGELOG Unreleased, Added: one line citing `DER-275`.
- **Verify** — `wc -l` budgets; the frozen sentence appears once in the
  template; this chunk's [groom.md](groom.md) fits the template's shape.
- **Blocked by** — `none` (template text is in the LLD; the SDLC link to
  it resolves once G1 and G2 both land on project-main, not trunk).
- **Blocks** — G5.
- **Out of scope** — other templates; a stored wave cache.

### G3: `sdlc-onboarding` Execution area

- LLD: `lld.md` Behavior 4
- **Outcome** — onboarding asks for and records `## Execution`
  (`Parallelism: max | serial | <description>`), at first touch or when
  its Check fails.
- **Acceptance**
  - Intro, When line, and `## Execution` (Discover, Propose, Write,
    Check) match LLD Behavior 4; `SKILL.md` ≤200 lines.
  - SOURCES `sdlc-onboarding` Notes updated.
  - CHANGELOG Unreleased, Added: one line citing `DER-275`.
- **Verify** — `wc -l skills/sdlc-onboarding/SKILL.md` ≤200; onboarding
  `#branch` anchor resolves; **security** read (it writes `AGENTS.md`;
  the value only lowers concurrency).
- **Blocked by** — `none` (independent file; block text is in the LLD).
- **Blocks** — `none`.
- **Out of scope** — any tracker schema or contract change.

### G4: Record this repo's Parallelism ceiling

- LLD: `lld.md` Behavior 5
- **Outcome** — `maintainers/AGENTS.md` has `## Execution` with the
  value the operator chose.
- **Acceptance**
  - Two lines after `## Tracker`: `## Execution`, `Parallelism:
    <operator's value>` (proposed `max`).
  - The `## Tracker` pointer stays the next non-empty line after its
    heading (Map check).
  - Commit `[<ticket-id>] Record execution: <value>`, landed through
    Review.
- **Verify** — the LLD Behavior 4 Check passes on `maintainers/AGENTS.md`;
  the `tracker-sdlc` Map check still passes.
- **Blocked by** — `none` (block format fixed by the LLD; the operator's
  answer is a wait on this issue, not a link).
- **Blocks** — `none`.
- **Out of scope** — CHANGELOG (maintainer note, not a deliverable).

### G5: Replay DER-252 against the landed rules

- LLD: `lld.md` Appendix and Verify
- **Outcome** — a clean agent shows the landed Groom text reproduces
  the LLD replay of DER-252.
- **Acceptance**
  - From `docs/SDLC.md` Groom and `templates/groom.md` alone, write
    DER-252 G1–G6 as a `groom.md` and review it: flags needless G3–G5
    (and G6) ← G1, keeps G2 ← G1.
  - Late insertions G7, G8, G9, G10, G11 in order: open waves after each
    match the Appendix; missing G8 ← G3–G6 is caught; the G8/G9 cycle is
    refused; G7 blocking in-progress G2 triggers ask-first.
  - Output: findings + verdict. Fixes become new items (late insertion).
- **Verify** — findings list each rule with the SDLC line it came from.
- **Blocked by** — G1 (replays the landed Groom text), G2 (drafts with
  the landed template).
- **Blocks** — `none`.
- **Out of scope** — editing files; the Execution area (not exercised by
  the replay).

## Graph

- Wave 1: G1, G2, G3, G4
- Wave 2: G5 ← G1, G2

Gates: `none` — G5 is a final check with nothing after it; no
integration or bottleneck need forces one.
