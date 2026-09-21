---
name: grok-acp
description: use this when the operator chooses to offload work to Grok Build — "offload to grok", "have grok build it", "delegate to grok", "resume the grok session" — to run the local Grok CLI as an SDLC worker (builder by default) over ACP, with session resume. do not use on your own initiative, and do not use for a quick read, search, or one-line fix you can do inline.
---

# Grok over ACP

Run Grok Build on this machine as a **worker** in the SDLC sense: a
separate agent with its own transcript that you mint clean, resume by id,
and never trust without verification. Transport is ACP (JSON-RPC over
`grok agent stdio`), driven by the `grok-acp` command from
[packages/grok-acp](../../packages/grok-acp/) in this repo. Stdlib Python,
Linux only. No `grok-acp` on `PATH`: run that package's `grok_acp.py`
directly, or install it as its README says.

## Iron law

**The operator picks Grok; you do not.** Offloading is opt-in per ask.
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

One invocation is one prompt turn. Stdout is one JSON object; progress
lines go to stderr. Builds outlast a foreground shell call: start `run`
**in the background** and read the result when notified. `--timeout`
defaults to 3600 seconds. On timeout or SIGTERM the client sends ACP
`session/cancel`, waits up to 20 seconds, and exits 5; the session stays
resumable. A SIGTERM before the prompt is sent stops the run with no turn
spent. A label and a session each take one turn at a time: a second run
gets `busy` (exit 2).

| Flag | Use |
| --- | --- |
| `--cwd` | Item branch worktree. Required. A resumed label must use the cwd it was minted in |
| `--label` | Registry name, `<item-id>:<role>`. This is the `builder_id` you store on the item |
| `--resume` | A label, or a raw Grok session id (`grok sessions list` finds ones started elsewhere; add an unused `--label` to adopt it) |
| `--replace` | With `--label` only: mint a new session under a label that already exists (fallback / overflow) |
| `--prompt` / `--prompt-file` / stdin | The handoff. Prefer a file |
| `--model`, `--effort` | `low` `medium` `high` `xhigh`. Omit for Grok's defaults |
| `--rules-file` | Extra system-prompt rules. New sessions only; refused with `--resume` |
| `--out` | Run directory. Default `~/.local/state/grok-acp/runs/<stamp>-<pid>` |

`$GROK sessions` prints the label registry
(`~/.local/state/grok-acp/sessions.json`; the state directory and every
run directory are forced to `0700`, and the state directory moves with
`GROK_ACP_STATE`). `$GROK forget <label>` drops a label;
Grok keeps the session.

### Result

| Field | Meaning |
| --- | --- |
| `ok`, `error`, `stopReason` | `ok` only when the turn ended with `end_turn`. Usage failures carry `error` + `detail` only |
| `sessionId`, `label`, `resumed` | Store these on the item |
| `text` | Grok's **final** message only. Full text: `response.md` in `runDir` |
| `filesEdited`, `toolCalls`, `failedToolCalls` | From ACP tool-call updates. A hint, not a diff |
| `leftoverProcessesKilled` | Grok's child processes still alive at exit and sent SIGTERM (its shell commands outlive it otherwise) |
| `permissionRequestsAutoApproved`, `plan`, `durationSec` | Permission prompts answered for Grok; its last plan, if any; wall time |
| `usage` | Model, tokens, calls for this turn |
| `runDir` | `prompt.md`, `response.md`, `result.json`, `events.ndjson` (every ACP message), `grok.stderr` |

| Exit | Meaning | Do |
| --- | --- | --- |
| 0 | `end_turn` | Verify |
| 2 | Usage: `bad_cwd`, `empty_prompt`, `unreadable_file`, `bad_args`, `label_exists`, `unknown_label`, `cwd_mismatch`, `busy`, `bad_out` | Fix the call. `unknown_label` is a typo, not a reason to `--replace` |
| 3 | Resume failed | Mint `--replace` with a short handoff (SDLC fallback) |
| 4 | Agent or protocol error | Read `grok.stderr`. Auth: operator runs `grok login` |
| 5 | Timeout, signal, or cancelled | Resume with what is left, or raise `--timeout`. `sessionId: null` means it stopped before a session existed: mint again |
| 6 | Stopped for another reason (`max_tokens`, `refusal`, …) | Read `stopReason`; usually overflow → `--replace` |

## SDLC fit

- **Role.** Grok is a **builder** unless the operator says otherwise. The
  verifier and the reviewer of that item are different agents and never
  see Grok's transcript. Do not read `response.md` or `events.ndjson` into
  their prompts.
- **One label per role per item.** `DER-12:builder` is never reused on
  another item and never resumed to verify or review its own work.
- **Mint = pack.** The first prompt is the whole handoff: ticket, LLD
  slice, acceptance, paths, standards, the proving commands, and the repo
  rules that bind it (tell it to read the repo `AGENTS.md` first). Grok
  cannot see this skills home unless you pack the text or give the path.
- **Resume = delta.** What changed, what failed, what to do next. Do not
  re-send the spec.
- **Branching is yours.** Create the item branch and worktree from
  project-main (or trunk) yourself and pass it as `--cwd`. Tell Grok to
  commit on that branch, **never** to push, and never to merge the item
  branch into anything. De-conflicting is still the builder's job: when
  project-main moves, resume the label with a delta that tells it to
  merge or rebase project-main **into** the item branch. Lands stay
  serialized and stay with the orchestrator.
- **Blockers and gates.** Check the item's blockers before minting.
  Offloading the build skips no gate: Review and security still run.
- **Fallback and overflow.** Exit 3, or a session too long to be useful:
  `--replace` with a short handoff (paths, decisions, open failures).

### Handoff shape

```text
You are the builder for <item-id> in <repo>. Read AGENTS.md first.

Goal:        <what done looks like>
Acceptance:  <from the ticket>
Design:      <LLD slice or path>
Scope:       <paths>. Do not touch <paths>.
Standards:   <language / test rules, packed or by path>
Prove it:    <exact commands that must pass>
Git:         commit on <branch>. Never push. Never merge <branch> into another
             branch or switch branches. Merge <base> into <branch> only when asked.

Finish with: files changed, commands run and their results, open risks.
```

## After it returns

Load `verify-before-done`. You are the orchestrator, not the verifier:

1. Smoke-check yourself: `git status` and `git diff <base>...` in the
   worktree (`filesEdited` misses shell-made changes), and that the branch
   and git rule were kept. This is not the gate.
2. The item's **verifier** runs the proving commands. First pass: mint it
   clean with the ticket and the commands. Later passes: resume that
   `verifier_id` with the delta. Never give it Grok's output.
3. Verifier failures go back to the **same** Grok label as a delta.
4. Do not take "tests pass" from `text` at any step.

## Always

- State scope, do-not-touch paths, and the git rule in every mint.
- Keep secrets out of prompts; `prompt.md` is written to disk.
- Report to the operator what was offloaded, the label, and the evidence.

## Ask first

- Offloading when the operator did not ask for Grok on this work.
- Pointing `--cwd` at a live host's config tree, `$HOME`, or `/`.
- Work that needs credentials the prompt would have to carry.

## Never

- Treat `ok: true` as landed+verified.
- Let one Grok session build and verify the same item.
- Feed Grok's transcript to a verifier or reviewer.
- Run two turns against the same session at once.
- Tighten or loosen the permission posture here without a new operator
  order; it is recorded above with its date.

## Red flags

- "Grok said the tests pass"
- "I'll resume the builder to double-check its own work"
- "New session each loop, it is simpler"
- "Let Grok merge it, it has the perms"
