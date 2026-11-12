# Entry, Brief, and Repo

## Entry

Entry classifies the work as a **chunk** or an **item**, read-only,
from what you were handed: no template, no subagent, no tracker write.
The classification line goes on the ticket at Brief.

| Condition | Class |
| --- | --- |
| The work needs the operator, or someone the operator names in writing, for taste, opinions, or a design talk | **chunk** |
| The work is mechanical, tactical, or immediate. Examples: a broken build, a unit failure, a UI bug report until analysis shows it needs taste | **item** |

1. You cannot tell which row fits → take a short look: can you
   reproduce it? Does the fix need a design choice? Then classify again.
2. Still unclear → ask the operator, as
   [Asking the operator](../SKILL.md#asking-the-human) says.

Do not implement at Entry: classify, or ask. Never use the item path to
avoid talking to the operator, or someone the operator names in
writing, about a product change; ask them:
[Never](branches-and-lands.md#never).

## Brief

Brief runs before Plan.

### Chunk brief

Gather ↔ Refine. Skip this loop only when a confirmed brief already
exists for this chunk. Do not implement in this step: write the brief.

1. **Gather.** Load
   [`discover-the-idea`](../../discover-the-idea/SKILL.md). That
   skill owns the interview, environment facts, options map, and the
   brief. Read the skill, or pack it into the gatherer prompt. Never
   copy or paraphrase its loop here; link the skill, because it will
   change.
2. **Refine.** The refiner, a different subagent from the gatherer,
   runs [`discover-the-idea` Refine](../../discover-the-idea/SKILL.md#refine).
   It loads no `yagni`. It works from first principles: the dump and
   looked-up facts, not a product template.
3. Refine returns `back to Gather` → return to Gather with its delta.
   Resume the gatherer.
4. Refine returns `buildable` → run the `tracker-sdlc` setup check. It
   fails → run `sdlc-onboarding` Tracker Check, Discover and Propose.
5. **manager** sends touchpoint 1 ([Touchpoints](../SKILL.md#touchpoints)):
   the brief, its standing permissions, the release permission as its
   own item, the HLD review choice and any onboarding proposal.
6. The operator corrects the brief → step 1 with the correction. The
   operator confirms → End of chunk Brief.

Gatherer and refiner ids: [Step agents](subagents.md#step-agents).
No language skill on a gather- or refine-only turn:
[`language-router` Never](../../language-router/SKILL.md#never).

Write Plan from the confirmed brief, never from a raw dump.

End of chunk Brief:

1. Cut project-main `integrate/<chunk-slug>`. Source:
   [Branches](branches-and-lands.md#branches). Commit the chunk's
   `brief.md`, `rulings.md` and `asks.md` on it. The confirmed brief
   is frozen from here: only the **manager** changes `brief.md`, on
   project-main, to apply an operator answer; the commit cites the ask
   id, and a ruling records the change (GR18).
2. The setup check failed at chunk Brief step 4 → run
   [`sdlc-onboarding`](../../sdlc-onboarding/SKILL.md) Write on the
   operator's touchpoint 1 answer. It writes the tracker files first.
3. Get the Epic (`backlog`):
   - The chunk arrived as a tracker ticket → use that ticket as the
     Epic. Never file a duplicate. Its type is not Epic → ask the operator
     to relabel it.
   - Otherwise → **manager** files it with `tracker-sdlc` `create`.
4. Onboarding ran in step 2 → land it as its own item, before Plan:
   1. Cut an item branch from project-main.
   2. Commit the onboarding as `[<epic-id>] Onboard tracker: <Tracker>`.
   3. Take it through Review as a short item with its own **verifier**,
      **reviewer**, and **security** read of the repo skill. Never land
      a bare commit.
   4. Land it on project-main.
5. **manager** posts the Entry classification and the path and commit
   of the confirmed brief, which holds the standing permissions, on the
   Epic with `tracker-sdlc` `comment`.

### Item brief

An item arrives as a Task or Bug. Always run item Brief on it. The one
exception: the ticket says `n/a — split from accepted Spec` → start at
Build. A confirmed brief on the item's chunk does **not** skip item
Brief.

0. Set up:
   1. Cut `item/<ticket-id>-<slug>`. Source:
      [Branches](branches-and-lands.md#branches).
   2. Run the `tracker-sdlc` setup check. It fails → load
      `sdlc-onboarding`.
   3. **manager** posts the Entry classification on the ticket with
      `tracker-sdlc` `comment`.
1. Problem and fix:
   1. The manager is already working that item, holds no other item's
      work, and holds no builder, verifier or reviewer conversation →
      the manager may be the troubleshooter. Otherwise mint a clean
      troubleshooter.
   2. The **troubleshooter**, an agent in the architect role, writes the
      problem, the proposed fix, and what is out of scope.
   3. It may load one of `debug`, `debug-pocock`, `debug-anthropic` and
      run it through root cause or hypothesis only. Stop there: never
      run the fix phase, `tdd`, or a land.
2. The **contrarian**, a different agent from the troubleshooter, loads
   `yagni` only. It writes a competing fix that **removes** something.
   Examples: a revert, a deleted path, a dropped part of the plan.
   1. Honor the existing HLD, or propose removing a **part** of it.
      Proposing that removal is an escalation.
   2. Never propose deleting the product; remove at most a part.
   3. There is no honest removal path → write `none — already smallest`.
3. The **manager** picks one fix and records why. The troubleshooter and
   the contrarian never pick. The manager is the troubleshooter or the
   contrarian → mint a clean agent for the pick, or ask the operator.
4. Check the pick. The first matching row applies:

   | Condition | Action |
   | --- | --- |
   | The two fixes would look the same to a user, and neither is a plan change | The step 3 pick stands. |
   | The two fixes differ only in two-way choices ([Asking the operator](../SKILL.md#asking-the-human)) | The step 3 pick stands. Log a ruling. |
   | Otherwise | Ask the operator. The wait blocks this issue only; other items proceed: [Asking the operator](../SKILL.md#asking-the-human). |

Contrarian id: [Step agents](subagents.md#step-agents). Use only the
roles in [Roles](../SKILL.md#roles).

## Repo

Before Plan, make sure each exists; set up what is missing:

1. The repo or subdir exists. Make it private only when the operator
   says so.
2. A README or AGENTS stub, so agents who need access are aware. Layout:
   [Product repo layout](conventions.md#product-repo-layout). Stub
   template: [`agents-stub.md`](../../sdlc-artifacts/templates/agents-stub.md).
3. The repo has CI or hooks → a **tester** watch on it.
4. Designs live in git from onset:
   [Designs in git](conventions.md#designs-in-git).

**Item:** confirm the workspace exists. Do not reinvent it; use it.
