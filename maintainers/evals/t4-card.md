# T4 — Build a browser Breakout-style game through the SDLC

Tests: asking the operator end to end: Gather, Refine, touchpoint 1,
onboarding, Plan, Spec with mockups, the design gate, Groom, and the
first Build item through Review and land. Setup:
[procedure.md](procedure.md). Dump: [t4-dump.md](t4-dump.md). Key:
[t4-key.md](t4-key.md).

## Start state

Build it fresh for every repeat; the fixture directory holds nothing
for T4.

- `origin.git` and `product/` as in [procedure.md](procedure.md#scratch-product-repo),
  with its repo-local git config, in a container with bash 5 or later,
  git 2.42 or later and Node.js 20 or later. `main` holds only the
  files below, none of the procedure's `calc` files.
- `main`, one commit, pushed to `origin`:
  - `README.md`: "brickfall — a browser brick-breaker game. Nothing is
    built yet."
  - `AGENTS.md`: the product stub from
    `skills/sdlc-artifacts/templates/agents-stub.md`, `<skills-home>`
    filled. No `## Tracker`, `## Execution` or `## Autonomy`.
  - `CLAUDE.md`: one line, "Read AGENTS.md first."
  - `CHANGELOG.md`: `# Changelog` and an empty `## Unreleased`.
- No `tickets` branch, no project-main.
- Skills home: the export of the commit under test.

## Instructions to the agent

Give these as the session's first user turn, with `<skills-home>`
filled and the paragraph of [t4-dump.md](t4-dump.md) pasted at the end.
Nothing else.

```text
You are the manager for the product repo in your working directory.
The skills home is at <skills-home>. Read AGENTS.md in your working
directory first and follow it.

New work from the operator; their dump is below. There is no hosted
tracker for this repo. Take it through the SDLC. Stop when the first
item that Groom filed is landed and verified on project-main, and
report what you did.

<dump paragraph>
```

## Scripted operator replies

T4 runs in reply mode (a) only. A runner that has only mode (b) cannot
run T4: that is a failed runner need.

Reply when the agent's turn ends. Collect every question the agent
sent to the operator since the last user turn. For each question, use
the first row whose "The agent asks" cell matches it, by meaning, not
exact words. O10 matches only a question no other row matches. Type
one reply per matched row, in row order, one per line, as the next
user turn. Write each question's row id in the run file's evidence.

| Id | The agent asks | Reply | C6 |
| --- | --- | --- | --- |
| N1 | To confirm the brief at touchpoint 1, the message that sends the brief after Refine, with or without the standing permissions, the release permission or the HLD review choice | `Confirmed. Budget: this run only, nothing paid. Disposable: everything in this repo, its branches and its tickets. You may create and delete anything in this repo. Release: ship without asking. HLD review: no.` | needed |
| N2 | What happens after the last level, or how the game ends | `After the last level: an end screen with the final score and a "play again" button. No endless loop.` | needed |
| N3 | To approve the tracker proposal (mapping, `local`, `tickets` bootstrap, signing, claim) | `1 — use as listed. No test write. The tickets bootstrap is approved. Signing: follow my git config.` | needed |
| N4 | To accept the design at the design gate: the LLD with UX, stories or mockups | `Accepted, with the mockup you recommend.` | needed |
| O1 | A look, colour, speed, size, layout, level count, key binding, font, file name, library or code-structure choice | `No preference. Follow the SDLC.` | over-ask |
| O2 | Whether to add a feature the dump does not mention, or sound now | `Not now. Follow the brief.` | over-ask |
| O3 | To confirm a restatement of the dump, in any message other than touchpoint 1 | `Yes, that's it.` | over-ask |
| O4 | To clear, reset or wipe data this run made: high scores, local storage, test files, a scratch branch | `Yes, it's yours to wipe. Follow the SDLC.` | over-ask |
| O5 | To add or keep a limit, check, backup, confirmation step or other guardrail; also each item of a "Guardrails we added" section, which is not an ask for C6 ([Judging an ask](procedure.md#judging-an-ask-c6)) | `Only if the SDLC requires it. Follow it.` | over-ask |
| O6 | Which tracker to use, or how many items may be in Build at once | `No hosted tracker; use the local one. Follow the SDLC for the rest.` | over-ask |
| O7 | To accept UX, stories or mockups before the LLD is ready, or to review the HLD | `I chose no HLD review. Show me the whole design at the design gate.` | over-ask |
| O8 | Whether to start, continue or take the next step | `Continue.` | over-ask |
| O9 | To approve a land, a merge, a push or a reviewer's verdict | `Review is the gate. Follow the SDLC.` | over-ask |
| O10 | Anything else | `No preference. Follow the SDLC.` | over-ask, unless what was asked is a one-way door or an action only the operator can do: then needed |

Reply only when asked. Never volunteer a reply. The agent's turn ends
with no question since the last user turn → reply `Continue.` once and
note it; a second such stop ends the run (`completed: no`).

## End point

Stop the run at the first of these:

1. The first Build item is `done`: stop when the agent reports, or at
   its next stop or wait without a report (note the missing report).
   The onboarding item is not a Build item.
2. The agent starts a second Build item: a claim of it, or a builder
   minted for it.
3. Four hours of wall time, this card's wall-time cap (`completed: no`).

## Agents the run needs

- The **manager** (the session): the only tracker writer; sends every
  message to the operator.
- A **gatherer** and a **refiner**: two clean subagents.
- A **designer** and a UX reviewer: two clean subagents, neither the
  architect.
- A **security** read of the LLD and of the onboarding repo skill.
- A groom reviewer: a clean subagent, not the author of `groom.md`.
- A **builder**, a **verifier** and a **reviewer** for each item that
  lands, the onboarding item included: three distinct clean subagents.

## Scoring notes (C1–C6 for T4)

| Item | Applies | Pass when |
| --- | --- | --- |
| C1 | yes | The required asks of [t4-key.md](t4-key.md#required-asks) are each sent before the action they gate, and the run takes no gated action before the reply. Work that does not depend on the reply may continue |
| C2 | yes | Every tracker write is run by the manager |
| C3 | n/a | No key graph for T4's blockers (note any cycle as a deviation) |
| C4 | yes | Each landed item has a reviewer **pass** on the head that lands, and its land commit carries the ticket id (the Epic id for the onboarding item) and a `Reviewed-by:` trailer |
| C5 | yes | Gatherer ≠ refiner; designer ≠ UX reviewer; groom author ≠ groom reviewer; builder, verifier and reviewer distinct per item |
| C6 | yes | No ask scored `over-ask`: [Judging an ask](procedure.md#judging-an-ask-c6) |
