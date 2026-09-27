# Subagents

## Item agents

- **Work item**: one Task, Bug, or outside or remote PR; one
  implementable unit.
- **Mint**: start a new subagent.
- **Contrarian**: the agent that loads `yagni` at item Brief; its id is
  `contrarian_id`.
- **Clean**: a subagent whose transcript is empty except the crafted
  task: ticket, LLD, acceptance, paths, and standards. Never seed it
  with another role's chat.
- **Resume**: continue that subagent (`resume_from` that id, or the
  host's equivalent). It already read the item. Send what changed, what
  failed, and what to do next. Never re-paste the spec, the tree, or
  prior logs it produced.

The manager, a session or a workflow, keeps two ids per work item:
`builder_id` and `verifier_id`. Review adds `reviewer_id`. The builder,
verifier, and reviewer are three different agents.

| Role | First pass on this item | Later passes on this item |
| --- | --- | --- |
| **builder** | Mint a **clean** subagent. Store `builder_id`. | **Resume** `builder_id`. Prompt only the delta. |
| **verifier** | Mint a **clean** subagent. Never the builder. Store `verifier_id`. | **Resume** `verifier_id`. Prompt only the delta. Re-run proving commands. |
| **reviewer** (Review) | Mint a **clean** subagent. Never the builder. Store `reviewer_id`. | **Resume** `reviewer_id` for re-review of the same item. |

A manager that spawns in parallel still mints one pair per item, not
one pair per loop. Give independent items independent pairs.

Never:

- Never let the builder verify or review its own work as the only gate;
  the verifier and the reviewer are other agents.
- Never give the verifier or reviewer the builder's transcript as
  memory; mint them clean.
- Never reuse an item's builder, verifier, or reviewer on a
  **different** item; mint clean agents for that item.
- Never mint a new builder or verifier on each Build loop while this
  item's previous one is still resumable; resume it.
- Never make the manager the contrarian, builder, or verifier of that
  item; mint a clean subagent for the role.

## Fallback

| Condition | Action |
| --- | --- |
| Resume fails (expired, quota, host error) | 1. Mint a new clean agent of the **same role** for this item. 2. Replace the stored id. 3. Pass a short handoff: paths, decisions, open failures. |
| A resumed transcript is more than half the context window, or the harness cannot load it or has to compact it | Replace that role's agent the same way: clean mint and short handoff. |

Never pass the other role's transcript; pass the short handoff. Never
rotate roles to "save" context; replace the agent of the same role.

## Step agents

- **Chunk Brief** keeps `gatherer_id` and `refiner_id` on the chunk.
  Mint a clean gatherer and a clean refiner on the first pass of the
  chunk. Resume those ids on later Gather ↔ Refine rounds. Never use the
  same agent for both. Steps: [Brief](entry-brief-repo.md#brief).
- **Plan–Spec** keeps `designer_id` and `ux_reviewer_id` on the chunk.
  They are two different agents, and neither is the architect. Resume
  them across UX and mockup rounds. The review loop and the operator's
  acceptance: [UX](plan-trial-spec.md#ux).
- **Groom** keeps `groom_reviewer_id`: [Groom names](groom-step.md#names).
- **Incoming item Brief** keeps `contrarian_id` on the item. Resume the
  contrarian if the fix-vs-removal choice gets another round. The
  troubleshooter, and when the manager may be it: [Item
  brief](entry-brief-repo.md#item-brief), step 1. The troubleshooter
  and the contrarian are two different agents. Neither is the builder,
  verifier, or reviewer of that item.

Item grain, fewer agents: for a no-screen incoming item, do not mint a
gatherer, designer, or UX reviewer. Mint the contrarian at Brief. Mint
the builder, verifier, and reviewer as usual. Add **security** if a
trust boundary moves.

## Tracker writes

Only the **manager** writes to the tracker: [Tracker](../SDLC.md#tracker).
Builder, verifier, and reviewer prompts carry no tracker-writing
instructions; those roles report.

## Writable worktree

Some hosts pin a subagent's writable worktree to the manager's current
worktree. On such a host, only one item worktree is writable at a time.
Then either builders for other items write to scratch for the manager
to commit, or the items run one after another.

## Spawn prompts

On each **mint**, the manager picks the prompt mode for that child: the
manager holds the bodies and the child needs them → **Pack**; else →
**Point**.

| Mode | Prompt | Child does |
| --- | --- | --- |
| **Pack** | Comprehensive: ticket/LLD, the skill bodies it will need, and any MCP tool schemas it will call. Name the ids packed. Tell it **not** to reload those. | Work. Do not `read_file` the packed skills or re-fetch packed MCP schemas. |
| **Point** | High-level task + which skill ids / MCP servers to load (or the host default: "read the matching `SKILL.md`"). | Load those itself. Still **at most one** language-family skill. |

Typical pack mints: first gatherer with `discover-the-idea`; first
refiner with `yagni`; contrarian with `yagni`; designer with
`ux-design` + `sdlc-artifacts`; UX reviewer, review loop only, with
`ux-design`; architect Plan/Spec with `sdlc-artifacts`; first builder
with one language skill + `tdd` / `yagni` / `debug` /
`docs-google-style`, no `tracker-sdlc`, no tracker writes; verifier
with `verify-before-done` plus the proving commands; reviewer with
`pr-review` plus the range vs project-main.

**Resume** is always delta-only. Do not re-pack skills or MCP guides
already in that child's transcript. A new skill or tool is required on
this pass → pack that slice or name it, not the whole set again.

Never:

- Never load a catalog into the manager just to pack it; point instead.
- Never pack the language catalog, every MCP server, or skills for a
  different role "just in case"; pack only what the child needs.
- Never pack a skill and also tell the child to go read the same file;
  tell it not to reload the packed skill.
- Never point at "load whatever you need" with no ids when the manager
  already knows the one or two that apply; name those ids.

## Workers

| Worker | When |
| --- | --- |
| Remote agent | Remote repo / PR work |
| Local CLI | Box-local gated builds. Grok Build: load `grok-acp` when the operator picks it |
| Local mirror | Inbound copy of git. Not the design source of truth |

**architect** adversarial-reviews other agents' tools when the work
needs it. The other role jobs: [Roles](../SDLC.md#roles).

Workers do not bypass **security**: [Roles](../SDLC.md#roles). A worker
PR into this skills home still needs intake and a SHA-pin match:
[Workers](../INTAKE.md#workers).
