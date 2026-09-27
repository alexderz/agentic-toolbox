# Branches and lands

## Branches

| Branch | What | Lifetime |
| --- | --- | --- |
| **trunk** | Repo default (`main` / protected). Release target. | Permanent |
| **project-main** | Integration branch for this project or chunk. Tip is the latest landed items. | Brief → Trunk |
| **item branch** | One work item. Created from current project-main (or from trunk if none) at item Brief (incoming) or Build (split from Spec). | Until that item lands |

Create project-main from trunk at the end of chunk Brief **when this
chunk is still integrating**. Do not create one for an incoming item that has no live
project-main. Name it and item branches as in
[Conventions](conventions.md#name-formats). When project-main
exists, builders **branch off the current tip.** After an item lands,
in-flight builders rebase or merge project-main and resume; the
verifier re-runs.

## Project-main

Do not build a stack of isolated item branches and integrate them once
at the end. Integrate **each** merge-ready item onto a temporary
project branch, then land that branch on trunk as the chunk.

**Lands on project-main are serialized.** Builds may run in parallel;
only one item merges at a time. The landing builder de-conflicts against
the current project-main tip (resume that builder; then resume its
verifier). Do not race two merges onto project-main.

## Land path

No PRs. **manager** sets the land order; builders follow it.

| Step | Rule |
| --- | --- |
| Review | An explicit SDLC gate ([Review](build-review.md#review)), not a PR |
| Durability | Push the item branch while it is built and reviewed; push project-main after each land |
| Land | After Review, merge the item branch locally into project-main (or trunk), one land at a time; push; delete the item branch |
| Done | After land + verify, **manager** transitions the item to `done` with `tracker-sdlc` and posts a `comment` citing the land SHA, the verifier result, and the reviewer verdict |

Every land commit carries the ticket ID and a `Reviewed-by:
<reviewer-label> (<verdict>)` trailer (an operator-confirmed rule), so
the review stays auditable without a PR. PRs remain only for outside or
remote workers.

## Never

- Branch an item off trunk or off another item branch while project-main
  exists.
- Leave merge-ready items unmerged so they can “integrate together later.”
- Skip Review because there is no PR.
- Force-push project-main to win a race (shared branch; **shell-safety**
  Ask first).
- Treat a green item branch as landed+verified. Landed means **on
  project-main** (or on trunk if that was the land target).
- Start or land an item that still has an **open** blocker without an
  operator call.

- Use the item path to avoid talking to a person about a product change.
