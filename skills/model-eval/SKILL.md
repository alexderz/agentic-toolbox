---
name: model-eval
description: use this when comparing local or self-hosted models on a real agentic coding task — model bake-off, "which model should I use", evaluating a newly released model, or building a repeatable eval suite. Not for one-shot prompt tests and not for benchmark-score lookups.
---

# Model eval

Run the same agentic coding task across many models and grade the
result by **running it**, not by reading it. An **evaluator** skill.
No `scripts/` — the runnable harness is `packages/model-eval-harness`.

## Iron law

**Gate before you spend.** Every hour of model time you spend on a
broken setup produces a confident, wrong ranking. Prove the stack works
before you measure anything with it.

## When

Load when someone wants to compare models on real work: a bake-off, a
"should we switch", a new release to qualify. Skip for a single prompt
comparison — that is not an eval, that is a spot check.

Companion files (read when relevant):

- `references/gates.md` — the pre-flight checks and why each exists
- `references/grading.md` — execution-based rubric design
- `references/live-endpoints.md` — safe read-only access to real systems
- `assets/case-matrix.md` — matrix format and variant conventions

## The shape

1. **Define one task.** Identical prompt for every model. Real enough to
   separate good from bad, small enough to finish.
2. **Gate the stack** (`references/gates.md`). Non-negotiable.
3. **Isolate the workspace.** Clean tree, no ambient context.
4. **Run the matrix.** One model resident at a time, warmed first.
5. **Grade by execution** (`references/grading.md`).
6. **Report**, keeping every failure on record.

## Gates, in order

Run all of these before the first real case. They cost minutes and
save days.

| gate | proves | typical catch |
|---|---|---|
| tool-call round-trip | the model emits tool calls the server can parse | a model whose chat template the runtime cannot terminate on — it generates to the token limit forever and scores zero for reasons that have nothing to do with capability |
| variant load | every parameter set actually loads | a context/offload combination that OOMs, discovered mid-run instead of up front |
| loop iteration | the driver runs every case, not just the first | a command in the loop body consuming the loop's stdin |
| workspace isolation | nothing ambient reaches the model | repo instruction files silently injecting a process the eval was meant to exclude |
| metric sanity | counters measure the model's work | a virtualenv counted as model output |

## Isolation

Agents inherit more than you think.

- **Run in a clean tree.** Work in a directory with no instruction
  files (`AGENTS.md`, `CLAUDE.md`, …) anywhere in its ancestry. Agent
  runners walk *up* the tree. Disabling discovery by flag is weaker: a
  model that shells out can still read what is up there.
- **Disable ambient discovery too.** Belt and braces — skills, prompt
  templates, extensions, context files.
- **One variable at a time.** Do not change runtime config mid-matrix.
  A setting changed halfway makes the halves incomparable.

Ambient instructions do not affect models evenly. Some obey them and
stop to ask permission; some ignore them and build. Graded naively,
obedience looks like incompetence.

## Failures: setting vs capability

Separate them, always.

- A **setting** failure (context too small, reasoning budget exhausted,
  offload misconfigured) gets a **new case with adjusted settings**.
  The original stays on record.
- A **capability** failure (code that does not compile, an API ignored)
  stays as-is. Do not tune it away.

Never delete a recorded failure. A resume that skips only successful
cases will re-run failures and destroy them — skip on *any* recorded
result and require an explicit flag to re-run.

Ladder a setting rather than guessing one value. Unlimited / bounded /
disabled across three or four points tells you whether a model needs
room or is looping. More budget is sometimes *worse*.

## Grading

**LOC is not quality, ever.** It measures verbosity. Rank on what runs:

- does `--help` work and exit 0
- does it perform a real read against the target system
- does bad input fail cleanly, non-zero, no traceback
- does bad auth fail cleanly
- do the model's own tests run and pass
- how much of the target API is genuinely exercised

Execute generated code in a **container**, never on the host — it is
model-written and unreviewed. See `references/grading.md`.

## Repeatability

An eval you cannot re-run is an anecdote.

- **Snapshot the environment** with the results: runtime version, model
  files and quantisation, parameters per case, harness commit, date.
- **Keep every artifact**: prompt, matrix, raw event stream, produced
  files, grades.
- **Expect drift** when the target is a live system. Record a
  fingerprint (entity counts, API version) so a later run can tell
  "the model changed" from "the house changed". Re-run the baseline
  alongside the new model rather than comparing to an old number.
- **Archive conditions separately.** If you change the prompt or the
  isolation, that is a new round, not an edit to the old one.

## Prompting the models

Two variants are worth running, and the delta between them is often the
most useful result in the whole exercise:

- **Unguided** — the bare task, no criteria.
- **Graded** — the task plus the criteria they are judged on, stated
  plainly. Requirements only; no process, no steps.

Telling models what "good" means tends to lift weak models far more
than strong ones. If you only ever run unguided prompts, you are
measuring the floor, not the model.
