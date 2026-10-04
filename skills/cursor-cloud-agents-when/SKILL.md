---
name: cursor-cloud-agents-when
description: use this when choosing Cursor Cloud Agent or the local grok CLI for coding or heavy multi-step work — Cloud Agent for a remote repo or pull request, the grok CLI for work on this machine under build quota, and the operator's private workspace for artifacts that live there. if Cursor credits are empty, degrade to the grok CLI. do not implement with a bot token.
---

# Cloud Agent vs grok CLI

Choose the worker for coding or heavy multi-step work: Cursor Cloud
Agent, the local grok CLI, or both.

## Iron law

**Builds go to the grok CLI, Cursor Cloud Agents, or both. Do not
implement with a bot token; hand the build to one of those workers.**

## Hand-off

1. Hand off the whole ticket.
2. Let the worker own the implementation loop.
3. **verifier** checks the final result.

How remote agents and local CLIs fit the process:
[Workers](../../docs/sdlc/subagents.md#workers). A worker's pull request
into this repo still goes through intake:
[Workers](../../docs/INTAKE.md#workers).

## Default split

| Work | Use |
| --- | --- |
| Design, review, scratch work, or build-quota research on this machine | grok CLI |
| A change that must land as a remote branch or pull request | Cursor Cloud Agent |
| Greenfield work with no repository named | Cloud Agent `new_repo` |
| SDLC artifacts that live in the operator's private workspace | That workspace, often through a Cloud Agent pull request |
| Files that exist only on a host with no remote checkout | grok CLI or shell on that host |
| Windows, or any host outside the workspace | Off limits unless the operator approved that host: [Never](../security-hardening/SKILL.md#never) |

Keep product GitHub repositories separate from the operator's private
workspace.

## Prefer Cloud Agent when

Use Cursor Cloud Agent when any of these holds:

- The deliverable is a branch or a pull request on a connected remote
  repository.
- The deliverable lands in the operator's private workspace through a
  connected remote repository.
- The work needs Cursor source control or a cloud VM.

## Credit degrade

If Cloud Agent fails because of usage, credits, quota, or billing:

1. Say so once.
2. Fall back to the grok CLI for the same goal.
3. If a remote pull request was required, produce the patch on this
   machine.
4. If step 3 applies, open or hand off the pull request from an approved
   host that already has credentials, or give the operator a branch-ready
   diff.
5. If the grok CLI is also unavailable, stop and report both blockers.

- Do not retry in a tight loop. Fall back as above.
- Do not implement with a bot token, including for a large patch. Use
  the grok CLI or a branch-ready diff.
- Do not work around the block with cookies or a Windows host. Stop and
  report the blocker.

## Launch

1. If the repository is ambiguous, confirm it with the operator.
2. Launch with a clear goal, the constraints, and what done looks like.
3. On launch and on reply, prefer Grok 4.7 unless the operator names
   another model.
4. Do not poll. Wait for the run to complete, then resume.
5. Follow up with a reply.
6. Interrupt a run only when asked.
7. Keep bank, mail, password-store, VPN, and chat secrets out of the
   prompt.

For the grok CLI, the run steps are in [`grok-acp`](../grok-acp/SKILL.md).
Load it when the operator opts in to Grok Build over ACP.

## Roles

Role names and jobs: [Roles](../../docs/SDLC.md#roles). Tracker writes:
[Tracker](../../docs/SDLC.md#tracker). Host lock:
[Never](../security-hardening/SKILL.md#never).
