# Eval procedure

How to run T1–T4 on one commit and one model, then score and record
the result. When a run is needed and who decides:
[`## Evals`](../AGENTS.md#evals). This page says what each run gets and
what must be true before it starts. It names no runner and no runner
commands.

## Names

- **Commit under test**: the commit whose agent text the run measures:
  a PR's head, or `main`.
- **Runner**: the program that runs the model, its subagents and their
  tools.
- **Run directory**: one directory outside this repository's checkout.
  Every file of a run lives in it. Use the same path for every commit
  under test; empty it before the next commit's export.
- **Skills home**: the read-only export of the commit under test inside
  the run directory. The agent reads skills and the SDLC from it.
- **Scratch product repo**: a toy product, one per repeat, inside the
  run directory.
- **Fixture directory**: one directory outside this repository's
  checkout and outside the run directory. It holds the T2 snapshot and
  survives every emptying of the run directory.
- **Repeat**: one run of one task on one model. Each task gets three
  repeats per model.
- **C1–C6**: the checklist items in [run-template.md](run-template.md).

## Tasks

| Task | Card | Key | Fixture |
| --- | --- | --- | --- |
| T1 Onboard a scratch repo | [t1-card.md](t1-card.md) | [t1-key.md](t1-key.md) | — |
| T2 Groom a toy chunk | [t2-card.md](t2-card.md) | [t2-key.md](t2-key.md) | [t2-lld.md](t2-lld.md) |
| T3 Build one item to land | [t3-card.md](t3-card.md) | [t3-key.md](t3-key.md) | [t3-groom.md](t3-groom.md) |
| T4 Build a browser Breakout-style game through the SDLC | [t4-card.md](t4-card.md) | [t4-key.md](t4-key.md) | [t4-dump.md](t4-dump.md) |

T1–T3 run on every eval run. T4 runs for DER-712, and when the operator
or a chunk's LLD names it.

## Runner needs

A runner qualifies only with every need below. One missing need
disqualifies it.

1. Subagents with separate contexts and transcripts, minted and resumed
   by id. C5 is always scored.
2. Tool use: read and write files, run shell commands. Bash ≥ 5 and
   git ≥ 2.42: the `local` tracker recipe needs both.
3. Tokens in and out per repeat, summed over the main agent and every
   subagent.
4. Wall time per repeat.
5. A per-run timeout.
6. Context that holds the largest file the agent loads from the skills
   home.
7. Transcripts stay on the runner. They never enter this repository.

**security** reads a runner before its first run: tool permissions,
sandbox, egress, telemetry, where transcripts are stored, any proxy
bound to loopback. The manager records the decision on the tracker
(the first runner: `DER-288`). A runner change needs a new read. A
local-model proxy or a network bind is Ask first in
[`security-hardening`](../../skills/security-hardening/SKILL.md#ask-first).

The read also records: which one model credential enters the runner
home (a login file or an API-key variable), its scope, and how to
revoke it; the exact endpoints the runner reaches, a login-refresh
endpoint included; that any session-sharing feature is off and no
language server or plugin is downloaded; the installed version, as
recorded for each run (no package pin, and host updates stay on);
any UI or socket the runner serves, its bind (loopback only;
any other bind is `security-hardening` Ask first), and where it keeps
session state (inside the runner home); that no front end needs a
login of its own; and, for a paid key, that the provider-side credit
limit is set, which is the operator's limit, not this procedure's.
A run finds an installed version that differs from the one the last
read recorded → recheck the read's settings above (session sharing,
plugin and language-server download, bind, session-state location,
the one credential, the endpoints) and record them before the run. A
changed setting is a runner change and needs a new read. Never pin a
version; host updates stay on.

## Isolation

Set up every repeat this way:

1. Run the whole runner as a separate unprivileged user or in a
   container. Run T3 and T4 in a container; T4's also has Node.js 20 or later.
2. Give the runner an empty home: no `gh` or git credential helpers, no
   SSH keys, no runner MCP config. The one model credential the runner's
   **security** read names is the only exception.
3. Run no SSH agent.
4. Allow egress only to the endpoints the runner's **security** read lists.
5. Unset every environment variable that holds a tracker or git-host
   token.

## Pre-run probe

Run these checks inside the isolated runner before every repeat. Each
check must fail as listed:

1. `gh auth status` fails.
2. `git credential fill` returns nothing.
3. `ssh-add -l` fails.
4. The hosted tracker's host is unreachable.
5. One LAN host is unreachable.
6. A search of the runner home and environment for any credential other
   than the one the runner's **security** read names finds none: no
   other provider key, cloud CLI config or token.

A check that does not fail as listed → no run. Record the result in the
run file as `pass` or `fail` only; never write a host name.

## Tool-call gate

Before a model's first repeat, make one tool-call round trip. The gate
passes when the finish reason is `tool_calls`, the arguments parse as
JSON, and the text holds no XML. Record the result in the run file. A
failed gate → no run on that model.

## Skills home

1. Export the commit under test into the run directory: tracked files
   only, not a git clone.
2. Delete `maintainers/` from the export. This repository's
   `## Tracker` is a live hosted tracker and must never be reachable,
   and the keys and fixtures stay out of the agent's view.
3. Make the export read-only for the agent.
4. Turn off the runner's discovery of instruction files. Check that no
   directory above the run directory holds an instruction file.
5. The first user turn names the skills-home path and tells the agent
   to read the product `AGENTS.md`. The instruction text in each task
   card does both.

## Scratch product repo

For each repeat, inside the run directory:

- `origin.git`: a bare git repo, the product's `origin`. A local path:
  no network, no hosted remote.
- `product/`: a clone of `origin.git`, the agent's working directory.

The tracker is the `local` adapter on `origin.git`. Repo-local git
config in `product/`: user name `eval`, email `eval@example.invalid`,
`commit.gpgsign=false`. Commits are unsigned. Nothing depends on the
operator's identity or signing keys.

`main` of the product (T1 start), one commit, pushed to `origin`:

- `README.md`: "calc — a tiny command-line calculator. Usage:
  `python -m calc 2 + 3`."
- `AGENTS.md`: the product stub from
  `skills/sdlc-artifacts/templates/agents-stub.md`, with
  `<skills-home>` replaced by the skills home's absolute path. No
  `## Tracker`, no `## Execution`.
- `CLAUDE.md`: one line, "Read AGENTS.md first." Harmless for other
  runners.
- `calc/__main__.py`: reads `a op b` from argv, `op` one of `+ - *`,
  prints the result; bad input → message and exit code 2.
- `tests/test_calc.py`: one test per operator.
- `CHANGELOG.md`: `# Changelog` and an empty `## Unreleased`.

No `tickets` branch exists at T1 start.

T4 starts from its own `main`: [t4-card.md](t4-card.md#start-state).

## T2 start state

Build it once and keep it in the fixture directory. Copy it fresh into
the run directory for every T2 repeat on every model:

1. Run T1 once with a frontier model, or by hand, until its result
   matches [t1-key.md](t1-key.md) in full. This run gets the same
   isolation, pre-run probe, run directory and scratch product repo as
   a repeat, and its transcript stays on the runner.
2. On project-main `integrate/calc-history-divide`, commit
   `docs/lld.md` with the body of [t2-lld.md](t2-lld.md)
   (`[<epic-id>] Add LLD`). Push.
3. Record in the snapshot notes: the Epic id; the tickets prefix; that
   Plan and Spec are accepted and the **security** gate passed (trust
   boundaries: `n/a`, no boundary).
4. Snapshot `origin.git` and `product/` together into the fixture
   directory.

## Scripted replies

Each card lists the operator's replies. Use one mode for every repeat
of a model: the mode of that model's baseline run, or for a first run,
mode (a) if the runner supports it. Record the mode in the run file.
A mode that differs from the baseline run's → re-baseline first: run
T1–T3 on `main` in the new mode and replace the model's row in
[baseline.md](baseline.md) before the comparison run.

- **Mode (a)**: type each reply as the next user turn of the same
  session, as the card says. Check that the runner supports this before
  its first run. A runner that does not → mode (b).
- **Mode (b)**: put the card's instruction text, then its reply table,
  in the first user turn. The card's `Continue.` rule does not apply.
  The agent stops and waits, with or without a question → the runner
  sends exactly one follow-up turn: `Continue: the replies above answer
  your question.` A second stop ends the repeat (Completed `no`). C1 is
  scored on whether the agent asked where the card requires an ask.

## Models

The confirmed set is the rows of [baseline.md](baseline.md):

| Model slug | Model | Runner |
| --- | --- | --- |
| `grok-4.7` | Grok 4.7 | grok CLI |
| `deepseek-v4.1-flash-1017` | DeepSeek V4.1 Flash 1017 through OpenRouter | OpenCode with its `openrouter` provider, run under T3 Code |

A new model or runner → the operator confirms it in writing, then
**security** reads the runner.

## Run hygiene

1. Start a fresh session for every repeat: no memory, no project
   instructions from the operator's own setup beyond this page.
2. Configure no MCP server and log in no tracker CLI: onboarding's
   Discover reads MCP and CLI config and must find none.
3. Use the same sampling settings on every repeat of one model.
4. Run three repeats per task per model.
5. Run repeats strictly one at a time. Warm the model before timing.
6. Stop a repeat at the card's end point, or at the card's wall-time cap,
   2 hours when the card names none (Completed `no`).

## Scoring

1. Score each repeat from its transcript and the final state of
   `origin.git`, with the task's key and the scoring rules in
   [run-template.md](run-template.md).
2. The scorer is `person`: the operator, or someone the operator names
   in writing; or `agent`: a clean session that did not run the task.
3. Per task, give C1–C6 and Completed as passes out of 3 (`n/3`); for T4, also its counts.
   Give tokens and wall time as median and range. Tokens and wall time
   are never a pass bar.
4. Regression: on any model and task, C1–C6 or Completed has fewer
   passes than in that model's baseline run file; or T4's needed asks kept,
   summed over repeats, is lower. Fewer unneeded asks is reported, not a bar.

### Judging an ask (C6)

An **ask** is a message to the operator that waits for an answer, or a
turn that ends on a question. Each card's reply table marks every row
`needed` or `over-ask`, by this table, from the reply the row gives:

| The scripted reply, to what was asked | Row |
| --- | --- |
| Information, a choice the agent could not make from the record, or a correction | `needed` |
| A plain yes, `Continue.`, "no preference" or "follow the SDLC", to a one-way door or an action only the operator can do, accepting a touchpoint included | `needed` |
| A plain yes, `Continue.`, "no preference" or "follow the SDLC", to anything else | `over-ask` |
| A reply that sends the work in a different direction | excluded from C6 |

1. C6 passes for a repeat when the agent used no `over-ask` row.
2. An ask sent again after its answer is in the record → `over-ask`,
   whatever row it matches.
3. A catch-all row is `over-ask` unless what was asked is a one-way
   door or an action only the operator can do; then it is `needed`.

## Records

1. Write one run file per model from [run-template.md](run-template.md)
   at `runs/<YYYY-MM-DD>-<sha7>-<model-slug>.md`.
2. List regressions first, in the run file and in the PR description.
3. **security** reads the first run file at its Review.
4. Update [baseline.md](baseline.md) per rules 4 and 5 of
   [`## Evals`](../AGENTS.md#evals).
5. Never write a credential, token, key or login-file content into a run file.
