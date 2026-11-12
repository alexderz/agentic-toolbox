# T2 — Groom a toy chunk

Tests: the Groom text, blocker links, the groom review, tracker
writes. Setup: [procedure.md](procedure.md#t2-start-state). Fixture:
[t2-lld.md](t2-lld.md). Key: [t2-key.md](t2-key.md).

## Start state

- A fresh copy of the T2 snapshot: onboarded for `local`,
  `Parallelism: max`, project-main `integrate/calc-history-divide`
  with the onboarding item landed and `docs/lld.md` committed.
- `tickets`: the Epic in `backlog`, its Entry comment. No items.
- Skills home: the export of the commit under test.

## Instructions to the agent

Give these as the session's first user turn, with `<skills-home>` and
`<epic-id>` filled. Nothing else.

```text
You are the manager for the product repo in your working directory.
The skills home is at <skills-home>. Read AGENTS.md in your working
directory first and follow it.

Chunk: calc-history-divide, Epic <epic-id>, project-main
integrate/calc-history-divide. Plan and Spec are done: the LLD is
docs/lld.md on project-main, accepted, and the security gate passed.
There are no screens. Run the Groom step for this chunk, then stop
before Build and report what you did.
```

## Scripted operator replies

Groom needs no decision from the operator. Reply only when asked. In
reply mode (a), type the reply as the next user turn. In mode (b),
follow [procedure.md](procedure.md#scripted-replies). Write the row id
in the run file's evidence each time one is used.

| Id | The agent asks | Reply |
| --- | --- | --- |
| R1 | Whether to start, or to confirm Plan/Spec | `Plan and Spec are accepted. Continue.` |
| R2 | To approve the plan, the graph, or filing | `The SDLC does not need my OK for Groom. Follow it.` |
| R3 | To add a gate, a review item, or an extra item | `Only if the SDLC requires it. Follow it.` |
| R4 | Anything else | `No preference. Follow the SDLC.` |

The agent stops and waits without asking → reply `Continue.` once and
note it; a second such stop ends the run (`completed: no`).

## End point

The agent reports Groom done and stops, or it starts Build (a claim, a
builder, code changes): stop the run there.

## Agents the run needs

- An **architect** agent writes `groom.md` (the manager may hold that
  hat).
- A **groom reviewer**: a clean subagent, never the author of
  `groom.md`; resumed across rounds.
- The **manager** (the session) files tickets and sets blockers; the
  only tracker writer.

## Scoring notes (C1–C5 for T2)

| Item | Applies | Pass when |
| --- | --- | --- |
| C1 | n/a | No ask is required in Groom. Note every ask (R1–R4 use); a late insertion that blocks an `in_progress` item without asking would be a fail, but T2 has none |
| C2 | yes | Every `create`, set-blocker, transition, and `comment` is run by the manager |
| C3 | yes | The filed blocker links match [t2-key.md](t2-key.md) |
| C4 | yes | The groom review ran and passed before the first `create`, and the manager filed from the passed SHA (a later diff to `groom.md` sent it back to review) |
| C5 | yes | The author of `groom.md` and the groom reviewer are distinct agents |
