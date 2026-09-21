# grok-acp

Stdlib Python client that drives the local **Grok Build** CLI as a
subagent over [ACP](https://agentclientprotocol.com) (`grok agent stdio`,
JSON-RPC). One invocation is one prompt turn in one Grok session, new or
resumed. MIT, same as the repository [LICENSE](../../LICENSE). Linux only.

The process rules for using it (who picks Grok, SDLC roles, what to verify
afterwards) live in the skill
[skills/grok-acp/SKILL.md](../../skills/grok-acp/SKILL.md). This page is
the tool.

## What this is

An orchestrating agent calls `grok-acp run` with a working directory and a
prompt. The client starts `grok agent stdio`, opens or resumes a session,
sends the prompt, records every ACP message, and prints one JSON result.
A label registry maps names such as `DER-12:builder` to Grok session ids,
so a later call resumes the same worker.

**Permissions are wide open on purpose.** The client starts Grok with
`--always-approve`, `_meta.yoloMode`, sandbox `off`, and answers any
permission request with the widest allow option. Grok then acts with the
full rights of the calling user. Only `deny` rules and hooks in the user's
own Grok and Claude settings still apply. Do not run this where that is not
acceptable.

## Install

Needs Python 3.12+ and a logged-in `grok` CLI (`grok login`). No
dependencies.

```bash
ln -s "$PWD/packages/grok-acp/grok_acp.py" ~/.local/bin/grok-acp
# Claude Code, system-wide skill:
ln -s "$PWD/skills/grok-acp" ~/.claude/skills/grok-acp
```

## Use

```bash
# new session under a label
grok-acp run --cwd ~/src/app-der-12 --label DER-12:builder --prompt-file handoff.md

# same session later
grok-acp run --cwd ~/src/app-der-12 --resume DER-12:builder --prompt-file delta.md

grok-acp sessions            # the label registry
grok-acp forget DER-12:builder
```

`--resume` also takes a raw Grok session id (`grok sessions list`).
`--replace` mints a new session under an existing label. `--model`,
`--effort`, `--rules-file` (new sessions only), `--timeout` (default 3600
seconds) and `--out` are optional. `grok-acp run --help` lists them.

Stdout is one JSON object: `ok`, `error`, `sessionId`, `label`, `resumed`,
`stopReason`, `text` (Grok's final message), `toolCalls`,
`failedToolCalls`, `filesEdited`, `plan`, `permissionRequestsAutoApproved`,
`leftoverProcessesKilled`, `durationSec`, `usage`, `runDir`. The run
directory holds `prompt.md`, `response.md`, `result.json`, `events.ndjson`
and `grok.stderr`.

| Exit | Meaning |
| --- | --- |
| 0 | Turn ended with `end_turn` |
| 2 | Usage error; `error` names it (`label_exists`, `unknown_label`, `busy`, …) |
| 3 | Resume failed |
| 4 | Agent or protocol error, or `grok` not found |
| 5 | Timeout, signal, or cancelled |
| 6 | Turn stopped for another reason; see `stopReason` |

## How it behaves

- **Cancel.** On `--timeout`, SIGTERM or SIGINT during a prompt it sends
  ACP `session/cancel` once, waits 20 seconds, and exits 5. A signal before
  the prompt is sent stops the run and spends no turn.
- **One turn at a time.** A label and a session are each locked for the
  length of a run; a second run gets `busy`.
- **Leftovers.** Grok runs shell commands in their own sessions, so they
  outlive it. At exit the client sends SIGTERM to every process Grok
  started that is still alive.
- **State.** `~/.local/state/grok-acp` (`GROK_ACP_STATE` moves it), forced
  to mode `0700`, as is every run directory. Transcripts can contain
  anything Grok read.

## Test

```bash
cd packages/grok-acp
uvx --with pytest pytest
uvx ruff check . && uvx ruff format --check .
```

The tests run the client against `tests/fake_grok.py`, a fake ACP agent.
They start no real Grok session and cost nothing.
