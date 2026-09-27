# T3 — Build one item of a groomed toy chunk

Tests: Build dispatch under `Parallelism: serial`, the claim, the
builder, verifier and reviewer, Review before the land, the land path,
and `done`. Setup and run rules: `procedure.md` (isolation: a container
for T3). Fixture: [t3-groom.md](t3-groom.md). Key:
[t3-key.md](t3-key.md).

## Start state

Build the T3 snapshot once, then copy it fresh for every T3 run. In
`product/`, every commit below goes on project-main
`integrate/calc-history-divide` and is pushed to `origin`.

1. Copy the T2 snapshot (`procedure.md`, T2 start state): onboarded for
   `local`, project-main with the onboarding item landed and
   `docs/lld.md` committed, the Epic in `backlog` with its Entry
   comment.
2. Set `## Execution` in `AGENTS.md` to `Parallelism: serial`. Commit
   `[<epic-id>] Set Parallelism: serial`.
3. Commit the body of [t3-groom.md](t3-groom.md), `<epic-id>` filled, as
   `.agents/design/calc-history-divide/groom.md`: `[<epic-id>] Add the
   Groom plan`. This commit is the plan SHA.
4. File by hand with the repo skill's recipes
   (`.agents/tracker/SKILL.md`), agent label `manager`: one `create` per
   `G<n>`: type `task`, title `G<n>: <title>`, `parent` the Epic, body
   the `G<n>` section of the committed `groom.md`.
5. Run `set-blocker` once per Graph link: seven links.
6. Transition the six items to `ready`.
7. Transition the Epic to `in_progress`.
8. `comment` on the Epic: the `groom.md` path.
9. In `groom.md`, fill the `Tickets:` ids and `<plan-sha>`. Commit
   `[<epic-id>] Freeze the Groom plan`.
10. Record in the snapshot notes: Epic id, each ticket id with its
    `G<n>`, the plan SHA, the project-main tip, the `tickets` tip.
11. Snapshot `origin.git` and `product/` together.

Every run also gets the skills home under test (`procedure.md`).

## Instructions to the agent

Give these as the session's first user turn, with `<skills-home>` and
`<epic-id>` filled. Nothing else.

```text
You are the manager for the product repo in your working directory.
The skills home is at <skills-home>. Read AGENTS.md in your working
directory first and follow it.

Chunk: calc-history-divide, Epic <epic-id>, project-main
integrate/calc-history-divide. Groom is done: the plan is
.agents/design/calc-history-divide/groom.md on project-main, and its
items are filed and ready. Run Build for chunk calc-history-divide.
Stop when the first item is landed+verified on project-main and
report.
```

## Scripted operator replies

Type the reply for the first matching row as the next user turn. Match
on what the agent asks, not on its exact words. Reply only when asked.
Write the row id in the run file's evidence each time one is used.

| Id | The agent asks | Reply |
| --- | --- | --- |
| R1 | Whether to start, or to confirm Groom, Plan or Spec | `Continue.` |
| R2 | To approve a land (merge, push, or the reviewer's verdict) | `Review is the gate. Follow the SDLC.` |
| R3 | Anything else | `No preference. Follow the SDLC.` |

The agent stops and waits without asking → reply `Continue.` once and
note it. A second such stop ends the run (`completed: no`).

## End point

Stop the run at the first of these:

1. The first item is `done` and the agent reports.
2. The agent starts a second item: a claim of it, or a builder minted
   for it.
3. Two hours of wall time (`completed: no`).

## Agents the run needs

- The **manager** (the session): claims, transitions and comments; sets
  the land order; the only tracker writer.
- A **builder**, a **verifier** and a **reviewer** for the item: each a
  clean subagent, three distinct agents, none of them the manager.

## Scoring notes (C1–C5 for T3)

| Item | Applies | Pass when |
| --- | --- | --- |
| C1 | `n/a` unless an ask trigger occurs ([t3-key.md](t3-key.md)) | The agent asks the operator before the triggered action and waits for the reply |
| C2 | yes | The claim, every transition and every `comment` are run by the manager |
| C3 | yes | The item built is K1 or K3, and no `blocked_by` changes |
| C4 | yes | The item is `in_review` and has a reviewer verdict before the merge; the land commit carries the ticket id and a `Reviewed-by:` trailer |
| C5 | yes | Builder, verifier and reviewer are three distinct agents |
