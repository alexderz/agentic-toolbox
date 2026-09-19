---
name: shell-safety
description: use this when writing, reviewing, or running shell or bash — including agent tool commands, CI steps, one-liners, and scripts — classify Always / Ask first / Never before the command runs.
---

# Shell safety

First-party Always / Ask first / Never for **tester** and **security**. Compatible with `security-hardening`: **LLM output is untrusted**; encode for the shell sink; the system prompt is not a boundary.

If this skill applies, use it; do not rationalize past the gate. No
`scripts/` in this skill dir.

konstruktoid bash-secure is **reference only** — do not install or copy that pack.

## Iron law

**No shell command runs until it is classified Always, Ask first, or Never.**

Model-chosen commands, generated scripts, and `$(...)` from untrusted text are client input.

## Always

| Rule | Why |
| --- | --- |
| Read the command before it runs | You cannot classify what you have not read |
| `set -euo pipefail` and `IFS=$'\n\t'` on scripts | Fail closed on error, unset, and pipe fail |
| Quote `"$var"` and `"$@"` | Word-split and glob are injection |
| Arrays, then `"${args[@]}"` | Do not build command strings |
| `${path:?}` before `rm` / `mv` / `chmod` on a variable path | Empty path becomes `/` or cwd |
| `[[ ]]` tests; `printf` not `echo` for untrusted text | `[` and `echo` are footguns |
| `mktemp` plus `trap` cleanup | Predictable temps; no `/tmp/foo` races |
| `cd -- "$dir" \|\| exit` | Failed cd must not continue |
| ShellCheck on committed scripts (**tester**) | Static catch before CI |
| Allowlist / encode before model text reaches a shell | Same as security-hardening encode-for-sink |
| Workspace-scoped paths; non-interactive flags | Agents must not hang or roam |

## Ask first

| Topic | Why it is a stop |
| --- | --- |
| Elevated shell, setuid, new capabilities | Privilege is a trust-boundary widen |
| Recursive force-remove / wipe outside the repo or this task's temp dir | Blast radius |
| Pipe remote content into a shell; unpinned vendor installers | INTAKE: clone, do not run installers |
| Force-push, history rewrite, deleting shared remote branches | Irreversible git |
| Writes under home, `/etc`, or credential dirs | Secrets and host config |
| New network egress or piping remote content | New trust |
| Disabling strict mode (`set +e` and kin) for a whole script | Fail-open |
| Running an opaque script you have not read | Same as untrusted client input |

Record the decision. Do not self-except.

## Never

| Never | Why |
| --- | --- |
| Dynamic shell evaluation of user or model text (`eval` / `-c` / `source` of untrusted input) | Injection; security-hardening Never |
| Pipe unpinned remote script into a shell | Supply chain |
| Recursive force-remove of filesystem root or unguarded variable paths; unquoted destructive globs | Host wipe |
| Secrets in scripts, git, or command lines that will be logged | History is forever |
| Copy `scripts/` into a skill dir | INTAKE quarantine |
| Extra hosts / Windows outside the workspace without operator approval | Host lock |
| Personal finance, mail, or password-manager via shell | Out of agent scope |
| Bind all interfaces or public mesh from a one-liner | Network becomes the client |
| World-writable mode bits on secrets | Data-class fail |

Host and personal-account locks are **Never**, not Ask first.

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **security** | This gate at LLD/PR when shell touches a boundary; skill intake | Writing tester CI yaml |
| **tester** | shellcheck hooks when `.sh` appears | Skipping **security** because CI is green |
| **builder** | Classifying commands before they run | Self-excepting “just this once” |
| **manager** | After-act | Blessing a ship that skipped the gate |

Workers do not bypass. A green ShellCheck is not a **security** clear.

## Red flags

- “The model said the command is safe”
- “I’ll pipe remote content into a shell just this once”
- “Elevated shell is faster than asking”
- “Empty path is fine”
- “The extra host is convenient”

Stop. Classify. Ask or never — do not run.

## Upstream pin

Intent: obra/superpowers `using-superpowers` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. Body is first-party. See [SOURCES.md](../../SOURCES.md).
