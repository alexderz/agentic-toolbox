# Subagents

## Step agents

**Brief (chunk)** keeps `gatherer_id` and `refiner_id` on the chunk.
Those two must not be the same agent. Resume them across Gather ↔ Refine
rounds. See [Brief](entry-brief-repo.md#brief). Plan–Spec keeps `designer_id` and
`ux_reviewer_id` on the chunk (not each other, not the architect).
Resume across UX and mockup rounds. Reviewer checks requirements only,
not personal taste. Human sees it after those two agree. Groom keeps
`groom_reviewer_id` on the chunk: a clean mint, never the author of
`groom.md`; resume it across review rounds.

**Brief (incoming item)** keeps `contrarian_id` (yagni agent). The
troubleshooter may be the parent. Those two must not be the same, and
neither is the builder, verifier, or Reviewer of that item.

## Item agents

A **work item** is one Task, Bug, or outside/remote PR — one
implementable unit. The orchestrator (manager session, parent agent, or
workflow) keeps two ids per item: `builder_id` and `verifier_id`. Review
adds `reviewer_id`. Those three must not be the same agent.

| Role | First pass on this item | Later passes on this item |
| --- | --- | --- |
| **builder** | Mint a **clean** subagent. Store `builder_id`. | **Resume** `builder_id`. Prompt only the delta. |
| **verifier** | Mint a **clean** subagent. Never the builder. Store `verifier_id`. | **Resume** `verifier_id`. Prompt only the delta. Re-run proving commands. |
| **reviewer** (Review) | Mint a **clean** subagent. Never the builder. Store `reviewer_id`. | **Resume** `reviewer_id` for re-review of the same item. |

**Clean** means an empty transcript except the crafted task: ticket /
LLD / acceptance, paths, and standards. Do not seed it with another
role’s chat, and do not use the orchestrator as the builder or verifier.

**Resume** means continue that subagent (`resume_from` that id, or the
host’s equivalent). The agent already read the item. Do not re-paste the
spec, the tree, or prior logs it produced. Send what changed, what
failed, and what to do next.

**Never**

- Builder verifies (or reviewer-reviews) its own work as the only gate.
- Verifier or reviewer is given the builder’s transcript as memory.
- An item’s builder / verifier / reviewer is reused on a **different**
  item.
- A new builder or verifier is minted on every Build loop when the
  previous one for this item is still resumable.
- Parent is the yagni agent, builder, or verifier of that item.

## Fallback

**Fallback.** If resume fails (expired, quota, host error), mint a new
clean agent of the **same role** for this item and replace the stored
id. Pass a short handoff (paths, decisions, open failures) — still not
the other role’s transcript.

**Overflow.** If a resumed transcript is too large to be useful, replace
that role’s agent the same way (clean mint + short handoff). Do not
rotate roles to “save” context.

Orchestrators that spawn in parallel still mint **one pair per item**,
not one pair per loop. Independent items get independent pairs.

**Item grain, fewer agents.** Do not mint gatherer, designer, or UX
reviewer for a no-screen incoming item. Mint the yagni agent at Brief;
mint builder, verifier, and Reviewer as usual. Security if a trust
boundary moves.

## Tracker writes

**Tracker writes.** Only the orchestrator writes to the tracker (see
[Hierarchy](../SDLC.md#tracker)). Builder, verifier, and reviewer
prompts carry no tracker-writing instructions; those roles report.

## Writable worktree

**Writable worktree.** Some hosts pin a subagent's writable worktree to
the orchestrator's current worktree. Then only one item worktree is
writable at a time: builders for other items write to scratch for the
orchestrator to commit, or the items run one after another.

## Spawn prompts

On each **mint**, the orchestrator (**manager**) picks the cheaper prompt
for that child. There is no default that is always right.

| Mode | Prompt | Child does |
| --- | --- | --- |
| **Pack** | Comprehensive: ticket/LLD, the skill bodies it will need, and any MCP tool schemas it will call. Name the ids packed. Tell it **not** to reload those. | Work. Do not `read_file` the packed skills or re-fetch packed MCP schemas. |
| **Point** | High-level task + which skill ids / MCP servers to load (or the host default: “read the matching `SKILL.md`”). | Load those itself. Still **at most one** language-family skill. |

**Pack** when the parent already has the bodies, the child will use most
of them, and one round-trip to re-read would cost more than inlining.
Typical: first gatherer mint with `discover-the-idea`; first refiner
mint with `yagni`; item yagni-agent mint with `yagni`; designer mint
with `ux-design` + `sdlc-artifacts`; UX reviewer mint with `ux-design`
(review loop only); architect Plan/Spec mint with `sdlc-artifacts`;
first builder mint with one language skill + `tdd` / `yagni` / `debug` /
`docs-google-style` (no `tracker-sdlc`, no tracker writes); verifier
mint with `verify-before-done` plus the proving commands; reviewer mint with `pr-review` plus the range vs
project-main.

**Point** when several skills or MCP servers might apply, the parent
does not already have the bodies, or only a thin slice of a large guide
matters. Do not load a catalog into the parent just to pack it.

**Resume** is always delta-only. Do not re-pack skills or MCP guides
already in that child’s transcript. If a new skill or tool is required
on this pass, pack that slice or name it — not the whole set again.

**Never**

- Pack the language catalog, every MCP server, or skills for a
  different role “just in case.”
- Pack a skill and also tell the child to go read the same file.
- Point at “load whatever you need” with no ids when the parent already
  knows the one or two that apply.

## Workers

| Worker | When |
| --- | --- |
| Remote agent | Remote repo / PR work |
| Local CLI | Box-local gated builds. Grok Build: load `grok-acp` when the operator picks it |
| Local mirror | Inbound copy of git. Not the design source of truth |

**architect** adversarial-reviews other agents’ tools when the work needs
it. **tester** owns mechanical CI/hooks. **security** owns gates (Spec
trust boundaries + Review) and skill intake. **manager** after-acts the
board; does not bless before ship.

**Workers do not bypass security.** A remote or local agent PR into this
skills home still requires intake and SHA-pin match. Worker choice is not
an exemption.
