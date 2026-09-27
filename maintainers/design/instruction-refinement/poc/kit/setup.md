# Eval kit — setup (T1, T2)

Harness-agnostic. This page says what each run gets and what must be
true before it starts, not which commands the harness uses. T3 is not
in the Trial.

## What the harness must support

- Multi-turn agent sessions with tool use: read and write files, run
  shell commands (bash ≥ 5, git ≥ 2.42: the `local` tracker recipe
  needs both).
- Subagents with their own transcripts, and resuming one by id. T1 and
  T2 need several distinct agents (see the task cards). No subagents →
  C5 is scored `n/a` and the sheet says so.
- A pause where the operator's scripted reply is typed in, as a normal
  user turn.
- Token counts in and out per run, summed over the main agent and
  every subagent. Wall time per run.
- The model, its variant, quantization, and context size are recorded
  per run. Context must hold the largest file an arm loads: arm A's
  `docs/SDLC.md` is 1128 lines.
- Transcripts stay on the harness. They never enter this repo.

## Skills home (per arm)

The agent reads a **skills home**: a read-only export of this repo, not
a git clone of it, placed outside the product repo. Every run directory
(skills-home export, scratch product repo, snapshots) lives outside
this repo's checkout.

1. Export this repo at main `7a11696` (tracked files only).
2. Delete `maintainers/` from the export. The agent is a toolbox user;
   this repo's own `## Tracker` is a live hosted tracker and must never
   be reachable.
3. **Arm A (current):** use the export as is.
4. **Arm B (rewrite):**
   1. copy `docs/SDLC.md` of the export to `docs/sdlc/not-yet-split.md`
      (byte-identical);
   2. overlay the tree under `poc/rewrite/` onto the export root: it
      replaces `docs/SDLC.md` and `skills/sdlc-onboarding/SKILL.md` and
      adds `docs/sdlc/groom-step.md`;
   3. change nothing else.
5. Make the export read-only for the agent.

## Scratch product repo

Outside this repo, per run, one scratch directory holding:

- `origin.git`: a bare git repo, the product's `origin` (a local path;
  no network, no hosted remote).
- `product/`: a clone of `origin.git`, the agent's working directory.

Repo-local git config in `product/`: user name `eval`, email
`eval@example.invalid`, `commit.gpgsign=false`. Nothing depends on the
operator's identity or signing keys.

`main` of the product (T1 start), one commit, pushed to `origin`:

- `README.md`: "calc — a tiny command-line calculator. Usage:
  `python -m calc 2 + 3`."
- `AGENTS.md`: the product stub from
  `skills/sdlc-artifacts/templates/agents-stub.md`, with
  `<skills-home>` replaced by the skills home's absolute path. No
  `## Tracker`, no `## Execution`.
- `CLAUDE.md`: one line, "Read AGENTS.md first." (Harmless for other
  harnesses.)
- `calc/__main__.py`: reads `a op b` from argv, `op` one of `+ - *`,
  prints the result; bad input → message and exit code 2.
- `tests/test_calc.py`: one test per operator.
- `CHANGELOG.md`: `# Changelog` and an empty `## Unreleased`.

No `tickets` branch exists at T1 start. No environment variable names a
tracker token; if the harness environment has some, unset them for the
run.

## T2 start state (shared snapshot)

Built once, then copied fresh for every T2 run (both arms, all models):

1. Run T1 once with a frontier model on arm A, or by hand, until its
   result matches [t1-key.md](t1-key.md) in full.
2. On project-main `integrate/calc-history-divide`, commit
   `docs/lld.md` with the body of [t2-lld.md](t2-lld.md)
   (`[<epic-id>] Add LLD`). Push.
3. Record in the snapshot notes: Epic id; tickets prefix; that Plan and
   Spec are accepted and the **security** gate passed (trust
   boundaries: `n/a`, no boundary).
4. Snapshot `origin.git` and `product/` together.

## Run hygiene

- Fresh session per run; no memory, no project instructions from the
  operator's own setup beyond what this page lists.
- No MCP server configured and no tracker CLI logged in for the run:
  onboarding's Discover reads MCP and CLI config, and must find none.
- Same sampling settings for both arms on one model.
- Alternate arms (A, B, B, A…) so harness drift does not favor one.
- One run per task per arm per model: 2 tasks × 2 arms × 2 models = 8.
- Stop a run at the task card's end point, or at 2 hours wall time
  (then `completed: no`).
- Score with [scoring-sheet.md](scoring-sheet.md), from the transcript
  and the final state of `origin.git`.
