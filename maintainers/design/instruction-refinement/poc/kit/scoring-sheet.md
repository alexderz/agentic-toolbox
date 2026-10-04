# Eval kit — scoring sheet

Copy this file once per run to
`poc/runs/<YYYY-MM-DD>-<task>-<arm>-<model-slug>-r<n>.md` and fill it. The
file is public: no hostnames, no paths outside the repo, no user names,
no transcript quotes. Evidence is a short phrase in your own words.

## Run

- Date: `YYYY-MM-DD`
- Task: `T1` | `T2`
- Arm: `A` (current, main `7a11696`) | `B` (rewrite, this folder at
  commit `<sha7>`)
- Model: `<family and variant>`, quantization `<q>`, context `<tokens>`
- Harness: `<name and version>` (no host)
- Repeat: `r1` | `r2` | `r3`
- Isolation probe: `pass` | `fail` (fail → no run); tool-call gate: `pass`
- Scorer: `person` | `agent (clean, <model>)`

## Result

| Field | Value |
| --- | --- |
| Completed | `yes` / `no` (per the task key) |
| C1 asks the operator where required | `pass` / `fail` / `n/a` |
| C2 only the manager writes the tracker | `pass` / `fail` / `n/a` |
| C3 blocker links match the key | `pass` / `fail` / `n/a` |
| C4 Review never skipped | `pass` / `fail` / `n/a` |
| C5 builder, verifier, reviewer distinct | `pass` / `fail` / `n/a` |
| Tokens in | `<n>` (main agent + all subagents) |
| Tokens out | `<n>` |
| Wall time | `<minutes>` (reported, never decisive) |
| Scripted replies used | row ids in order, e.g. `R1, R2` |
| Unprompted `Continue.` | `0` / `1` |

## Arm B only: routing (Trial question 1)

| Field | Value |
| --- | --- |
| Read `docs/SDLC.md` (index) | `yes` / `no` |
| Read `docs/sdlc/groom-step.md` before the first `groom.md` write (T2) | `yes` / `no` / `n/a` |
| Read `docs/sdlc/not-yet-split.md` in full rather than the routed section | `yes` / `no` |
| Read `skills/sdlc-onboarding/SKILL.md` before the first proposal (T1) | `yes` / `no` / `n/a` |

Files read: list skills-home paths relative to the skills home, in
first-read order.

## Evidence

One line per C item: the phrase that shows pass or fail, and where it
is (transcript turn number, or a file in `origin.git`).

- C1:
- C2:
- C3: (T2: filed links as `Kx ← Ky`; traps hit)
- C4:
- C5: (agent labels per job)

## Deviations

Rows from the task key's Deviations table that occurred, one per line.

## How each C item is scored

- `n/a` only in two cases: the task card says the item does not
  apply; the run ended before it
  reached the item (note "not reached").
- `pass` needs positive evidence, not the absence of a failure.
- One failing instance fails the item for the run.
- A run that ended early: score what happened before the end.
