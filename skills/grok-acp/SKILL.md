---
name: grok-acp
description: use this when the operator chooses to offload work to Grok Build — "offload to grok", "have grok build it", "delegate to grok", "resume the grok session" — to run the local Grok CLI as an SDLC worker (builder by default) over ACP, with session resume. do not use on your own initiative, and do not use for a quick read, search, or one-line fix you can do inline.
---

# Grok over ACP

Run Grok Build on this machine as a **worker** in the SDLC sense: a
separate agent with its own transcript that you mint clean, resume by id,
and never trust without verification. Transport is ACP, JSON-RPC over
`grok agent stdio`, driven by the `grok-acp` command from
[packages/grok-acp](../../packages/grok-acp/) in this repo. Stdlib Python,
Linux only. If `grok-acp` is not on `PATH`, run `packages/grok-acp/grok_acp.py`
from the checkout that holds this skill directory's real path, or install it
as the package README says. This skill directory is usually a symlink.

## Iron law

**The operator picks Grok; you do not.** Offloading is opt-in per ask.
Exception: the credit-failure fallback in [cursor-cloud-agents-when](../cursor-cloud-agents-when/SKILL.md#credit-degrade) is pre-approved.
**Grok's summary is a claim, not evidence.** Verify before you report.

## Permissions (operator order, 2026-09-21)

Grok runs with maximum permissions, on purpose: `--always-approve`,
`_meta.yoloMode`, sandbox `off`, and any permission request that still
arrives is auto-approved. It runs as the same user, so it can read, write,
run, push, and reach the network exactly as the operator can.

What still binds it: `deny` rules and hooks in `~/.grok/config.toml` and
`~/.claude/settings.json` (Grok reads it). Project-level rules, hooks, and
auto-loaded instructions apply only in a folder Grok already trusts; a
fresh item worktree usually is not, so do not count on them. Nothing else.
Scope is set by your prompt, so write the scope down.

## Run it

```bash
GROK=grok-acp

# mint a clean worker for a work item
$GROK run --cwd <item worktree> --label <item-id>:builder --prompt-file <handoff.md>

# resume the same worker later: delta only
$GROK run --cwd <item worktree> --resume <item-id>:builder --prompt-file <delta.md>
```

One invocation is one prompt turn. Stdout is one JSON object; progress lines
go to stderr. Start `run` **in the background** and read the result when
notified; builds outlast a foreground shell call. `--timeout` defaults to
3600 seconds. On timeout or SIGTERM the client sends ACP `session/cancel`,
waits up to 20 seconds, and exits 5; the session stays resumable. A SIGTERM
before the prompt is sent stops the run with no turn spent. A label and a
session each take one turn at a time: a second run gets `busy` (exit 2).

| Flag | Use |
| --- | --- |
| `--cwd` | Item branch worktree. Required. A resumed label must use the cwd it was minted in |
| `--label` | Registry name, `<item-id>:<role>`. This is the `builder_id` you store on the item |
| `--resume` | A label, or a raw Grok session id. `grok sessions list` finds ids started elsewhere. To adopt one, add an unused `--label` |
| `--replace` | With `--label` only: mint a new session under a label that already exists. For fallback or overflow |
| `--prompt` / `--prompt-file` / stdin | The handoff. Prefer a file |
| `--model`, `--effort` | `low` `medium` `high` `xhigh`. Omit for Grok's defaults |
| `--rules-file` | Extra system-prompt rules. New sessions only; refused with `--resume` |
| `--out` | Run directory. Default `~/.local/state/grok-acp/runs/<stamp>-<pid>` |

`$GROK sessions` prints the label registry, `~/.local/state/grok-acp/sessions.json`.
If `GROK_ACP_STATE` is set, the state directory is that path. The state
directory and the run directories it creates are `0700`.
`$GROK forget <label>` drops a label; Grok keeps the session.

### Result

| Field | Meaning |
| --- | --- |
| `ok`, `error`, `stopReason` | `ok` only when the turn ended with `end_turn`. Usage failures carry `error` + `detail` only |
| `sessionId`, `label`, `resumed` | Store these on the item |
| `text` | Grok's **final** message only. Full text: `response.md` in `runDir` |
| `filesEdited`, `toolCalls`, `failedToolCalls` | From ACP tool-call updates. A hint, not a diff |
| `leftoverProcessesKilled` | Grok's child processes still alive at exit and sent SIGTERM. Its shell commands outlive it otherwise |
| `permissionRequestsAutoApproved`, `plan`, `durationSec` | Permission prompts answered for Grok; its last plan, if any; wall time |
| `usage` | Model, tokens, calls for this turn |
| `runDir` | `prompt.md`, `response.md`, `result.json`, `events.ndjson` (every ACP message), `grok.stderr` |

| Exit | Meaning | Do |
| --- | --- | --- |
| 0 | `end_turn` | Verify |
| 2 | Usage: `bad_cwd`, `empty_prompt`, `unreadable_file`, `bad_args`, `label_exists`, `unknown_label`, `cwd_mismatch`, `busy`, `bad_out` | Fix the call. `unknown_label` is a typo, not a reason to `--replace` |
| 3 | Resume failed | Mint `--replace` with a short handoff, per SDLC [Fallback](../sdlc/references/subagents.md#fallback) |
| 4 | Agent or protocol error | Read `grok.stderr`. Auth: operator runs `grok login` |
| 5 | Timeout, signal, or cancelled | Resume with what is left, or raise `--timeout`. If `sessionId` is `null`, it stopped before a session existed: mint again |
| 6 | Stopped for another reason (`max_tokens`, `refusal`, …) | Read `stopReason`; usually overflow → `--replace` |

## SDLC fit

- **Role.** Grok is a **builder** unless the operator says otherwise. It
  runs every check for its item and returns a proof bundle:
  [Proofs](../sdlc/references/proofs.md#builder-checks). The reviewer of
  that item is a different agent and never sees Grok's transcript. Do not
  read `response.md` or `events.ndjson` into its prompt. Give the reviewer
  the inputs [pr-review](../pr-review/SKILL.md) names and Grok's proof bundle.
- **One label per role per item.** `DER-12:builder` is never reused on
  another item and never resumed to review its own work.
- **Mint = pack.** The first prompt is the whole handoff: ticket, LLD
  slice, acceptance, paths, standards, the proving commands, and the repo
  rules that bind it. Tell it to read the repo `AGENTS.md` first. Grok
  cannot see this skills home, so pack the text or give the path.
- **Resume = delta.** What changed, what failed, what to do next. Do not
  re-send the spec.
- **Branching is yours.** Create the item branch and worktree yourself from
  the source [Branches](../sdlc/references/branches-and-lands.md#branches) names;
  pass it as `--cwd`. Tell Grok to commit on that branch, **never** to push,
  and never to merge the item branch into anything. De-conflicting is still
  the builder's job: when project-main moves, resume the label with a delta
  that tells it to merge or rebase project-main **into** the item branch.
  Lands stay serialized and stay with the manager ([Land path](../sdlc/references/branches-and-lands.md#land-path)).
- After the land, resume the same label to run the touched journeys on the
  land target at the land SHA: [After integration](../sdlc/references/proofs.md#after-integration) step 1.
- **Blockers and gates.** Check the item's blockers before minting.
  Offloading the build skips no gate: Review and security still run.
- **Fallback and overflow.** Exit 3, or a session too long to be useful:
  `--replace` with a short handoff, per SDLC [Fallback](../sdlc/references/subagents.md#fallback).

### Handoff shape

```text
You are the builder for <item-id> in <repo>. Read AGENTS.md first.

Goal:        <what done looks like>
Acceptance:  <from the ticket>
Design:      <LLD slice or path>
Scope:       <paths>. Do not touch <paths>.
Standards:   <language / test rules, packed or by path>
Prove it:    <exact commands that must pass>. Run each one yourself, fresh,
             before you finish. Write and run the span tests and journeys the
             ticket's Verify names. Add and run any missing end-to-end test for a
             touched journey even if Verify omitted it. No behavior change: explain
             why journeys are n/a. Save each run's full output under <scratch folder>.
Git:         commit on <branch>. Never push. Never merge <branch> into another
             branch or switch branches. Merge <base> into <branch> only when asked.

Finish with: files changed, open risks, and a proof bundle in the private review channel.
For a public report, use only public-safe results, revision and shareable artifact links.
The bundle has these fields. A field with nothing to record holds `n/a`
and why.

1. **Criteria**: per acceptance criterion, the proving command, its exit
   code, its counts (passed, failed, skipped) and its raw output path.
2. **Seen failing**: per new check, how it failed first (red before
   green, or the broken variant) and that run's raw output path.
3. **Visual**: per UI behavior, the screenshot or video path.
4. **Scope**: what is verified, under which bounds and assumptions; what
   is left out, and why.
5. **Sync commit**: the commit the checks ran on.
6. **Direct evidence**: the build workspace path on disk, and the CI run
   link when the repo has CI.
7. **Journeys**: per journey and span test run, the fields of field 1.
```

## After it returns

Load `verify-before-done`. You are the manager. Nobody re-runs Grok's
checks; you read its evidence.

1. Smoke-check the worktree yourself: `git status`, `git diff <base>...`,
   and that the branch and git rule were kept. `filesEdited` misses
   shell-made changes. This smoke check is not the gate.
2. Read the proof bundle in `text`. Confirm every field is there and
   every output path it names exists on disk.
3. A field or file is missing, or a check failed → send that to the
   **same** Grok label as a delta.
4. At every step, take "tests pass" from the bundle's saved outputs,
   never from `text` alone.
5. Then run [Review](../sdlc/references/build-review.md#review) with a
   reviewer that is not Grok.

## Always

- State scope, do-not-touch paths, and the git rule in every mint.
- Keep secrets out of prompts; `prompt.md` is written to disk.
- Report to the operator what was offloaded, the label, and the evidence.

## Ask first

- Offloading when the operator did not ask for Grok on this work.
- Pointing `--cwd` at a live host's config tree, `$HOME`, or `/`.
- Work that needs credentials the prompt would have to carry.

## Never

- Treat `ok: true` as landed+verified. Run [After it returns](#after-it-returns).
- Let one Grok session build and review the same item. Mint a separate reviewer.
- Feed Grok's transcript to the reviewer. Give it its Role inputs and Grok's proof bundle.
- Run two turns against the same session at once. Wait, then resume.
- Tighten or loosen the permission posture here without a new operator
  order; it is recorded above with its date. Ask the operator for one.

## Red flags

- "Grok said the tests pass"
- "I'll resume the builder to review its own work"
- "New session each loop, it is simpler"
- "Let Grok merge it, it has the perms"
