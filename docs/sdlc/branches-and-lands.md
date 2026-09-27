# Branches and lands

## Branches

| Branch | What | Lifetime |
| --- | --- | --- |
| **trunk** | Repo default (`main` / protected). Release target. | Permanent |
| **project-main** | Integration branch for this project or chunk. Tip is the latest landed items. | Brief → Trunk |
| **item branch** | One work item. Created from current project-main, or from trunk if there is no project-main. Created at item Brief for an incoming item, or at Build for an item split from Spec. | Until that item lands |

An item's **land target** is the branch its item branch was created
from: project-main, or trunk. **Landed** means on the land target.

- Create project-main from trunk at the end of chunk Brief when this
  chunk is still integrating.
- Name project-main and item branches as in
  [Conventions](conventions.md#name-formats).
- When project-main exists, builders branch off the current tip.
- After an item lands, in-flight builders rebase or merge project-main
  and resume. The verifier re-runs.
- Cut an incoming item's branch at item Brief, per this table. Never
  create a project-main for an incoming item.

  | Condition at item Brief | Branch from | Land |
  | --- | --- | --- |
  | A project-main already exists: this chunk is still integrating | project-main | On project-main |
  | No project-main: no chunk in flight, or the parent chunk already Trunked | trunk | Review versus trunk, then a local merge into trunk. [Trunk](trunk-changelog-monthly.md#trunk) is then `n/a` |

## Project-main

Integrate **each** merge-ready item onto project-main, a temporary
project branch. Then land project-main on trunk as the chunk
([Trunk](trunk-changelog-monthly.md#trunk)). Never build a stack of
isolated item branches and integrate them once at the end.

**Lands on project-main are serialized.** Builds may run in parallel.
Only one item merges at a time. Never race two merges onto project-main.

The landing builder de-conflicts against the current project-main tip:

1. Resume that builder.
2. Then resume its verifier.

## Land path

No PRs. **manager** sets the land order; builders follow it.

| Step | Rule |
| --- | --- |
| Review | An explicit SDLC gate ([Review](build-review.md#review)), not a PR |
| Durability | Push the item branch while it is built and reviewed. Push project-main after each land. |
| Land | After Review, merge the item branch locally into its land target, one land at a time. Push. Delete the item branch. |
| Done | After land + verify, **manager** transitions the item to `done` with `tracker-sdlc` and posts a `comment` citing the land SHA, the verifier result, and the reviewer verdict. |

Every land commit carries the ticket ID and a `Reviewed-by:
<reviewer-label> (<verdict>)` trailer, so the review stays auditable
without a PR. PRs remain only for outside or remote workers.

## Never

| Never | Do instead |
| --- | --- |
| Branch an item off trunk or off another item branch while project-main exists. | Branch it off the current project-main tip ([Branches](#branches)). |
| Leave merge-ready items unmerged so they can “integrate together later.” | Land each merge-ready item in the land order ([Land path](#land-path)). |
| Skip Review because there is no PR. | Run [Review](build-review.md#review) before every land. |
| Force-push project-main to win a race. Project-main is a shared branch; force-push is **shell-safety** Ask first. | De-conflict against the current project-main tip ([Project-main](#project-main)). |
| Treat a green item branch as landed+verified. | Treat an item as landed+verified only when it is on its land target ([Branches](#branches)) and verified. |
| Start or land an item that still has an **open** blocker without an operator call. | Follow [Open blockers](build-review.md#open-blockers). |
| Use the item path to avoid talking to the operator, or someone the operator names in writing, about a product change. | Ask them ([Asking the operator](../SDLC.md#asking-the-human)). |
