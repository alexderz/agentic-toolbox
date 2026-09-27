# SDLC

Shared process for work that uses this skills home: software, docs,
process changes, and other tickets. Git holds durable artifacts. The
issue tracker is the board. Branches and land commits cite a ticket ID
when the project uses tickets.

## How to read

1. Find your step in [Steps](#steps).
2. Read the file in that row's Read column.
3. You are the **manager** → also read
   [branches-and-lands.md](sdlc/branches-and-lands.md) and
   [subagents.md](sdlc/subagents.md).

## Roles

Skills are tools, keyed by role. If no listed skill fits the task, do
the work without one. Never create a new skill id mid-task. Do not
remint a skill that already has an id. Use only these roles. Step jobs
(gatherer, refiner, troubleshooter, verifier, reviewer, groom reviewer)
are agents acting in one of these roles, not new roles.

| Role | Job |
| --- | --- |
| **architect** | Design, HLD/LLD, adversarial review of approach |
| **designer** | User stories, high-level UX, Spec mockups when there is a screen |
| **builder** | Implement and ship |
| **tester** | Mechanical CI, hooks, cleanup, verification evidence |
| **security** | Gates at Spec (trust boundaries) and Review, plus skill intake — not only a monthly vuln pass |
| **manager** | Process, board after-act, and land order (local, serialized merges; no PRs). The only tracker writer. Does not bless ships |
| **operator** | The person in the loop: exceptions, vuln severity, extra hosts, personal accounts |

Workers (agents, CI bots) act as **builder** or **tester**. They do not
bypass **security**.

Which skill to load: the root [AGENTS.md](../AGENTS.md) load table. Skill
ids, ownership and SHA pins: [SOURCES.md](../SOURCES.md). Third-party
content: **security** intake first, per [INTAKE.md](INTAKE.md).

## Names

- **Roles**: the seven names in the Role column above.
- **trunk**: the repo's protected default branch, usually `main`. The
  release target.
- **project-main**: `integrate/<chunk-slug>`, the integration branch of
  one project or chunk. Items land on it; it lands on trunk at Trunk.
- **chunk**: work that needs the operator, or someone the operator
  names in writing, for taste, opinions, or a design talk. Board
  object: Epic.
- **item**: one implementable unit, a Task or Bug under its Epic.
  Mechanical, tactical, or immediate work enters as an item.
- **landed+verified**: merged onto project-main (or onto trunk when
  that was the land target) and verified there.
- **Steps**: Entry, Brief, Repo, Plan, Trial, Spec, Groom, Build,
  Review, Trunk, Changelog, Monthly, in that order.
- Name formats (slugs, branches, skill ids):
  [Conventions](sdlc/conventions.md#name-formats).

## Tracker

| Layer | Typical object | Meaning |
| --- | --- | --- |
| Track | Project (or the tracker's equivalent) | One product or process track |
| Chunk | Epic | Discrete, parallel slice |
| Item | Task or Bug under its Epic | Implementable unit. Sub-items only if the repo's tracker skill enables them |

1. Every tracker read and write goes through
   [`tracker-sdlc`](../skills/tracker-sdlc/SKILL.md) and the product
   repo's `.agents/tracker/SKILL.md`.
2. Only the **manager** writes to the tracker: create, claim, release,
   set-blocker, comment, and every transition.
3. Builders, verifiers, and reviewers never write to the tracker. They
   report to the manager; the manager writes.
4. The manager after-acts the board in the operator's timezone.

States (six): `backlog`, `ready`, `in_progress`, `in_review`, `done`
(= landed+verified; an Epic: on trunk), `canceled`. Blocked is not a
state: an item is blocked while it has an **open blocker**, a blocker
not in `done` or `canceled`.

Designs live in git from onset:
[Designs in git](sdlc/conventions.md#designs-in-git).

## Grain

The board layer is the grain. Do not add a fourth issue type.

| Arrives as | Needs the operator, or someone the operator names in writing, for taste or design talk? | Enter at |
| --- | --- | --- |
| New product or process track | Yes | **Chunk** that also writes `track.md`. Full ladder; write Plan and Spec |
| Feature, redesign, fuzzy idea | Yes | **Chunk**: interview; write or extend Plan and Spec |
| Broken build, failing test, mechanical bug | No | **Item**: problem + fix; align existing Plan and Spec |

- Entry, the first step, classifies, or asks. It does not fix.
- A UI defect stays an item until analysis shows the question is "what
  should this screen be?". Then it is a chunk (or promote it).
- Work split from an accepted Spec is already an item in Build. Do not
  re-run item Brief on it.
- Build finds a shape change → escalate: ask as
  [Asking the operator](#asking-the-human) says, block that issue;
  siblings proceed.

<a id="asking-the-human"></a>

## Asking the operator

A decision needs the operator, or someone the operator names in
writing:

1. Stop and say so. Do not hide the ask in a status dump.
2. Write the message from template
   [`ask-human.md`](../skills/sdlc-artifacts/templates/ask-human.md).
   Fill every part.
3. Use everyday words. A project word (`HLD`, `LLD`, `project-main`,
   `DoD`, a ticket code) → say what it means in the same sentence.
4. Give your recommendation and why. No good default → say so.
5. Ask one question per message when you can. Several must go together
   → number them and say which set you recommend.
6. Wait. Do not continue that part until they answer.

An ask is required for: accepting the write-up, the look-and-feel, or
the detailed design; waiving a check; an open blocker you cannot
finish; three failed fixes; anything in an Ask-first row; spending
money; destructive actions.

Never send "Please advise.", "LGTM?", or "UX verification not
required?" with no explanation: send the full `ask-human.md` message.
Never proceed after silence: keep waiting on that part.

While you wait:

- The wait is a blocker on **that** issue. Other unblocked items keep
  moving. Do not freeze the chunk.
- The operator wrote that they are AFK, headless, or autonomous → the
  manager may pick between two **item** fixes that both honor the
  existing plan. The manager never changes Plan or Spec shape; that
  stays blocked until the operator, or someone the operator names in
  writing, answers.

## Steps

Same names at every grain. Grain changes what you write and how many
agents, not which steps exist. Headings and tickets use the step
**name**. HLD and LLD are artifact names (`docs/hld.md`,
`docs/lld.md`); the steps are Plan and Spec.

| Step | What it is | Read |
| --- | --- | --- |
| [Entry](sdlc/entry-brief-repo.md#entry) | Classify chunk vs item, or ask. Do not fix | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Brief](sdlc/entry-brief-repo.md#brief) | Chunk: Gather ↔ Refine. Item: problem+fix vs removal, then pick | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Repo](sdlc/entry-brief-repo.md#repo) | Git ready, agents aware. Item: confirm, do not reinvent | [entry-brief-repo.md](sdlc/entry-brief-repo.md) |
| [Plan](sdlc/plan-trial-spec.md#plan) | Write or align the HLD. Shape change → escalate | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Trial](sdlc/plan-trial-spec.md#trial) | Optional proof. Item: usually skip | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Spec](sdlc/plan-trial-spec.md#spec) | Write or align the LLD. Shape change → escalate | [plan-trial-spec.md](sdlc/plan-trial-spec.md) |
| [Groom](sdlc/groom-step.md) | Tickets, blockers, land path. Incoming item: this ticket | [groom-step.md](sdlc/groom-step.md) |
| [Build](sdlc/build-review.md#build) | Implement ↔ test until DoD | [build-review.md](sdlc/build-review.md) |
| [Review](sdlc/build-review.md#review) | Reviewer ≠ builder. Required for every land (no PRs) | [build-review.md](sdlc/build-review.md) |
| [Trunk](sdlc/trunk-changelog-monthly.md#trunk) | Land project-main on trunk (when a chunk used one) | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| [Changelog](sdlc/trunk-changelog-monthly.md#changelog) | Promote Unreleased | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| [Monthly](sdlc/trunk-changelog-monthly.md#monthly) | Cadence, not a ship gate | [trunk-changelog-monthly.md](sdlc/trunk-changelog-monthly.md) |
| Manager: branches and lands | Project-main, land path, Never | [branches-and-lands.md](sdlc/branches-and-lands.md) |
| Manager: subagents | Step and item agents, spawn prompts, workers | [subagents.md](sdlc/subagents.md) |
| Conventions | Names, commits, layout, changelog, designs in git | [conventions.md](sdlc/conventions.md) |
| Old Stage numbers | A ticket or chat cites a Stage number | [In-flight map](sdlc/conventions.md#in-flight-map) |
