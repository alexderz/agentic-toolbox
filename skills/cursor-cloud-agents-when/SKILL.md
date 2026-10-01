---
name: cursor-cloud-agents-when
description: use this when choosing Cursor Cloud Agent, the local grok CLI, or Origin for coding or heavy multi-step work — Cloud Agent for a remote repo or pull request, grok CLI for box-local work under build quota, Origin for forge artifacts. if Cursor credits are empty, degrade to the grok CLI. do not implement with a bot token.
---

# Cloud Agent vs grok CLI vs Origin

Choose the worker for coding or heavy multi-step work. Run steps for the
grok CLI stay in [`grok-acp`](../grok-acp/SKILL.md). Load that skill when
the operator opts in to Grok Build over ACP.

## Iron law

**Builds go to the grok CLI, Cursor Cloud Agents, or both. Do not
implement with a bot token.**

Hand off the whole ticket. The CLI owns the implementation loop. The
**verifier** checks the final result. Prefer Grok 4.7 on launch and on
reply unless the operator names another model. How remote agents and
local CLIs fit the process is in
[docs/SDLC.md](../../docs/SDLC.md) (Workers).

## Default split

| Work | Use |
| --- | --- |
| Box-local design, review, workspace scratch, or build-quota research | grok CLI |
| A change that must land as a remote branch or pull request | Cursor Cloud Agent |
| Greenfield work with no repository named | Cloud Agent `new_repo` |
| SDLC artifacts that live on the Origin forge | Origin, often through a Cloud Agent pull request |
| Files that exist only on a host with no remote checkout | grok CLI or shell on that host |
| Windows, or any host outside the workspace | Off limits unless the operator approved |

Product GitHub repositories stay separate from the Origin forge.

## Prefer Cloud Agent when

Use Cursor Cloud Agent when the deliverable is a branch, a pull request,
or an Origin land on a connected remote repository, or when the work
needs Cursor source control or a cloud VM.

## Credit degrade

If Cloud Agent fails because of usage, credits, quota, or billing, say
so once, then fall back to the grok CLI for the same goal. When a
remote pull request was required, produce the patch on the box and open
or hand off the pull request from an approved host that already has
credentials, or give the operator a branch-ready diff. If the grok CLI
is also unavailable, stop and report both blockers. Do not retry in a
tight loop. Do not implement with a bot token, including a large patch.
Do not work around the block with cookies or a Windows host.

## Launch

Confirm the repository with the operator when it is ambiguous. Launch
with a clear goal, the constraints, and what done looks like. Prefer
Grok 4.7 unless the operator names another model. Do not poll. Resume
when the run completes. Follow up with a reply. Interrupt only when
asked. Do not put bank, mail, password-store, VPN, or chat secrets in
the prompt.

## Roles

The **builder** ships settings and new functionality. The **manager**
after-acts ticketed board moves only. Windows stays off limits unless
the **operator** approved that host. See
[security-hardening](../security-hardening/SKILL.md).
