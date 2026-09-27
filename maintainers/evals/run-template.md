# Eval run file — template

Copy this file once per model and commit under test to
`runs/<YYYY-MM-DD>-<sha7>-<model-slug>.md`, keep the sections from
`## Run` down, and fill them. One file holds every repeat of T1–T3 on
that model. Procedure: [procedure.md](procedure.md).

The file is public. Write no hostnames, IPs, model-server URLs or
ports, paths outside this repository, keys or tokens, or personal
names. Never quote model output: evidence is a short phrase in your own
words.

## Run

- Commit: `<sha7>` (`main`, or the head of PR `#<n>`)
- Model: `<model-slug>`: `<family and variant>`, quantization `<q>`,
  context `<tokens>`
- Runner: `<name>` `<version>` (no host)
- Pre-run probe: `pass` before every repeat (a fail means no run)
- Tool-call gate: `pass`
- Reply mode: `a` (next user turn) | `b` (all replies in the first
  turn); the same mode as the baseline run
- Scorer: `person` | `agent` (never a name)
- Baseline: `runs/<baseline run file>` | `none (first run)`

## Regressions

One line per regression, or `none`:

`<task> <item>: <n>/3 → <m>/3 — <phrase>`

## Results

C1–C5 and Completed: passes out of 3 (`n/3`). A repeat scored `n/a`
because the run ended before the item ("not reached") counts as a
non-pass. Write `n/a` for a task only where the card says the item
does not apply; C5 is never `n/a`. Tokens and wall time: `median (min–max)`,
never a pass bar.

| Task | Completed | C1 | C2 | C3 | C4 | C5 | Tokens in/out | Wall |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | `n/3` | `n/3` | `n/3` | `n/a` | `n/3` | `n/3` | `<in> (<low>–<high>)` / `<out> (<low>–<high>)` | `<minutes> (<low>–<high>)` |
| T2 | `n/3` | `n/a` | `n/3` | `n/3` | `n/3` | `n/3` | same | same |
| T3 | `n/3` | `n/3` or `n/a` | `n/3` | `n/3` | `n/3` | `n/3` | same | same |

## Evidence

One block per task and repeat, in order T1 r1 … T3 r3. Each C line: the
phrase that shows pass or fail, and where it is (transcript turn
number, or a file in `origin.git`).

### T1 r1

- Completed: `yes` | `no` (per the task key)
- C1:
- C2:
- C3: (T2: filed links as `Kx ← Ky`; traps hit)
- C4:
- C5: (agent labels per job)
- Replies used: row ids in order, e.g. `R1, R2`; unprompted `Continue.`
  `0` | `1`
- Deviations: rows from the task key's Deviations table that occurred,
  or `none`
- Tokens in / out: `<n>` / `<n>` (main agent and every subagent);
  wall time: `<minutes>`

## How each C item is scored

- `n/a` only in two cases: the task card says the item does not
  apply; the run ended before it reached the item (note "not
  reached").
- `pass` needs positive evidence, not the absence of a failure.
- One failing instance fails the item for the run.
- A run that ended early: score what happened before the end.
