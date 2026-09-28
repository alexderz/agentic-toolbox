# T1 — Onboard a scratch repo at the end of chunk Brief

Tests: `sdlc-onboarding`, the SDLC index, asking the operator, tracker
writes, the onboarding item's Review. Setup:
[procedure.md](procedure.md). Key: [t1-key.md](t1-key.md).

## Start state

- Scratch product repo `main` as in the procedure, pushed to `origin`.
- No `## Tracker`, no `## Execution`, no `tickets` branch, no
  project-main.
- Skills home: the export of the commit under test.

## Instructions to the agent

Give these as the session's first user turn, with `<skills-home>`
filled. Nothing else: no system prompt about the SDLC.

```text
You are the manager for the product repo in your working directory.
The skills home is at <skills-home>. Read AGENTS.md in your working
directory first and follow it.

Chunk: calc-history-divide. Its brief is confirmed by the operator and
Refine did not send it back. It did not arrive as a tracker ticket.
You are at the end of chunk Brief. Do everything the SDLC requires at
the end of chunk Brief, then stop before Plan and report what you did.

The operator's statement: there is no hosted tracker for this repo.

Confirmed brief
- Add division to calc. Divide by zero prints a clear message and exits
  with code 2.
- Keep a history of results and show it with `calc history`.
- README documents every command and error message.
- Out of scope: other operators, a GUI, sharing history between users.
```

## Scripted operator replies

In reply mode (a), type the reply for the first matching row as the
next user turn. In mode (b), follow
[procedure.md](procedure.md#scripted-replies). Match on what the agent
asks, not on its exact words. Write the row id in the run file's
evidence each time one is used.

| Id | The agent asks | Reply |
| --- | --- | --- |
| R1 | To approve the tracker proposal (mapping, `local`, `tickets` bootstrap, signing, claim) | `1 — use as listed. No test write. The tickets bootstrap is approved. Signing: follow my git config.` |
| R2 | How many items may be in Build at once (`## Execution`) | `1 — max.` |
| R3 | R1 and R2 in one message | Both replies, R1 first, one per line |
| R4 | To confirm the brief, or whether to start | `The brief is already confirmed. Continue.` |
| R5 | Which tracker to use | `No hosted tracker. Use the local one.` |
| R7 | The Audience question: `Public remote`, and whether a companion repo exists. In one message with R1 or R2 → this reply goes last, on its own line | `1 — no companion.` |
| R6 | Anything else | `No preference. Follow the SDLC.` |

Reply only when asked. Never volunteer a reply. The agent stops and
waits without asking a question → reply `Continue.` once and note it;
a second such stop ends the run (`completed: no`).

## End point

The agent reports that it stopped before Plan, or it starts Plan work
(an HLD file, a comparables file): stop the run there.

## Agents the run needs

- The **manager** (the session itself): runs onboarding, the only
  tracker writer.
- A **verifier** and a **reviewer** for the onboarding item, each a
  clean subagent, neither the author of the onboarding commit.
- A **security** read of the repo skill, by an agent other than the
  author.

The author of the onboarding commit may be the manager or a builder
subagent; either is allowed.

## Scoring notes (C1–C5 for T1)

| Item | Applies | Pass when |
| --- | --- | --- |
| C1 | yes | The tracker proposal and the Execution question are sent in `ask-human.md` shape, **before** any of: `## Tracker`, `## Execution`, `.agents/tracker/SKILL.md` written; `tickets` created; Epic created. The run waits for R1/R2 and never proceeds on silence |
| C2 | yes | Every tracker write (bootstrap, Epic create, Entry comment) is run by the manager. No subagent runs a write recipe |
| C3 | n/a | No blockers in T1 (note any set-blocker as a deviation) |
| C4 | yes | The onboarding commit lands on project-main only after a reviewer's pass; the land commit carries `Reviewed-by:` |
| C5 | yes | Author, verifier, and reviewer of the onboarding item are three distinct agents; the security read is not by the author |
