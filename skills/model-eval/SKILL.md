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

**Sandbox the agent too, not just its output.** The agent is the active party:
it installs packages, writes files, reaches services. Run it in a container with
only its work dir mounted, its own throwaway package roots, an unprivileged
user, and no route to host-local services. Agents left on the host for one
cohort installed 199 crates and 45 Python packages into the operator's home
directory, and two cases discovered another model's project through shared
site-packages — `pip install -e` writes a `.pth` that every later run can see.
An audit of 3,733 executed tool calls found no credential access and no sudo,
but nothing had prevented either.

## A broken check produces a plausible negative

This is the failure mode that costs the most, because nothing errors. A
broken grader does not crash -- it reports that the model failed, which is
exactly what you half-expected, so you believe it and move on.

Every one of these was found only by checking a result that looked normal:

- A login shell (`bash -lc`) re-reads the profile and **replaces** the
  container image's `PATH`. The toolchain disappears and every project
  "does not build". Use `bash -c`.
- `cmd | tail` exits with `tail`'s status, so a failing build reports
  success. Set `pipefail` and check the real code.
- A sourced library that does `set -euo pipefail` overrides the caller's
  `set`. Combined with `pipefail`, a `grep` that finds nothing exits 1 and
  kills the run -- and "found nothing" is usually a *result*, not an error.
  It dies silently on exactly the cases worth recording.
- A sourced library that already defines `RESULTS` makes
  `RESULTS="${RESULTS:-default}"` a no-op, so output lands in another
  cohort's directory. Capture the caller's value *before* sourcing.
- Binary discovery that matches `target/release/deps/<name>-<hash>` picks a
  test artifact. Launched as the server, it answers nothing.

So: **verify the runner on one case before spending a matrix on it**, and
classify harness faults with their own exit codes so they can never be
recorded as model failures. Distinguish, in the recorded status, "the tool
under test could not be reached", "it was reached and never used", and "it
was used and the model still produced nothing". Collapsing those into one
`ok` with a zero score hides three different findings.

## Grade with a real client

A hand-rolled grader drifts toward leniency, because you write it from the
same assumptions as the thing you are grading.

One cohort's grader accepted any response *containing* `serverInfo` as a
successful handshake. A real client refused the same server: the response
carried `"id": null`, so it could not be correlated to the request. The
grader had certified a server that nothing could talk to.

Check the protocol's actual requirements -- id correlation, required
fields, error shape -- or drive the grading through a real client and let
it refuse. Where both exist, run both and treat disagreement as a bug in
the grader first.

**Watch the version window.** Give models the newest specification and
their output may be unusable by the tooling you own: the server answers
with a version your client does not accept, both sides behave correctly,
and nothing connects. Decide deliberately whether to document the version
your client speaks, or bridge the gap with a shim that rewrites *only* the
negotiated version and logs what was really advertised. A shim must never
supply a field the server omitted -- that converts a genuine protocol
violation into a pass.

**Do not let the agent framework's permission layer double as the
sandbox.** Headless runners often auto-deny every permission prompt. Then a
model that reached for `/tmp` stalls while one that happened to pick the
work directory succeeds, and you have measured which scratch path each
model guessed. The container is the boundary; turn the prompt layer off
inside it.

## Checking claims made in prose

When the artifact is a report rather than a program, the grader is a set of
patterns, and patterns are where the bias hides.

- **Match the domain's distinctions.** One grader scored "unavailable"
  against `unavailable + unknown`. They are different states. The model
  reported the correct narrower figure and was marked wrong *for being more
  precise than the grader*.
- **Order patterns by authority, not position.** A table cell is a
  deliberate statement of a count; a number that merely appears near the
  word somewhere in 13 KB of prose is not. Taking the first textual match
  let a stray "16 button" override `| button | 21 |`.
- **Run a negative control.** If you adjusted the grader until the output
  scored well, corrupt a known-good artifact and confirm the grader still
  catches it. Otherwise you have tuned it to pass.
- **Record every check, not just the totals**, so a WRONG verdict can be
  audited instead of trusted.

## Cohorts, not baselines

An eval measures a **cohort**: these models, this harness, this day. That is the
only unit that compares.

There is no baseline to anchor to. Re-running a model six months later does not
measure that model against its past self -- the runtime moved, the libraries
moved, the harness moved. You get a second cohort, not a trend.

So:

- **Rank only within a cohort.** All models saw the same fixture, the same
  harness, the same day. That comparison is defensible.
- **Do not carry numbers across cohorts.** "It scored 5/5 in September" and the
  same model in March are two different measurements of two different systems.
- **Snapshot conditions to describe them, not to recreate them.** Runtime
  version, model files and quantisation, flags per case, harness commit, date.
- **Re-run the whole cohort** when a new model arrives, baseline models included.
  That is cheaper and more honest than trying to freeze the world.

What survives across cohorts is the **method** and the **qualitative findings** --
"bounded reasoning beats unbounded", "a graded prompt lifts weak models most",
"LOC measures nothing". Those are claims about how things behave. The numbers
are not.

For the same reason, do not freeze a package cache to make runs reproducible: it
only guarantees that every future cohort is tested against staler libraries.

## Measure your variance, or do not rank

Run two or three representative cases three times each, same settings, before
believing any ordering. Observed in one real cohort:

| metric | spread across identical runs |
|---|---|
| duration | 11-25% |
| turns | 16-32% |
| lines of code | 12-22% (one model: 926 / 1091 / 1535) |
| **execution checks** | **one model swung 5/5, 5/5, 2/5** |

Execution grading is more stable than LOC. It is **not** stable. A one- or
two-check difference between models is noise. Report tiers -- works / partly
works / does not work -- not a leaderboard, and say n=1 where it is n=1.

## Prompting the models

Two variants are worth running, and the delta between them is often the
most useful result in the whole exercise:

- **Unguided** — the bare task, no criteria.
- **Graded** — the task plus the criteria they are judged on, stated
  plainly. Requirements only; no process, no steps.

Telling models what "good" means tends to lift weak models far more
than strong ones. If you only ever run unguided prompts, you are
measuring the floor, not the model.
