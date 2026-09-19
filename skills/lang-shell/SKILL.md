---
name: lang-shell
description: use this when the change is shell or bash and you need the pointer — routes to shell-safety. do not use as a second shell body. do not use for PowerShell (load lang-powershell) or Docker RUN trivia (load lang-docker first).
---

# Shell (router)

**This id routes.** Load `shell-safety`. Do not remint Always / Ask first /
Never for bash. Compatible with `security-hardening`, `tdd`,
`verify-before-done`. No `scripts/`.

## Iron law

**`shell-safety` is the shell skill.** Classify Always / Ask first / Never
before a command runs.

## Load

`shell-safety` only. Then stop.

Dockerfile `RUN` snippets stay `lang-docker` first. Load `shell-safety`
only when the change is a real `.sh` / shebang script or an agent shell
command.

## Combined verify (after shell-safety)

```bash
shellcheck path/to/script.sh
```

Run the script on a throwaway path. No live destructive targets.

## Combined PR checklist

- `set -euo pipefail` and quoted `"$var"` / `"$@"`.
- No `eval`, no `curl | sh`, no unquoted `rm -rf $dir`.
- `${path:?}` before destructive ops on a variable path.

## Never

- A second bash skill that copies konstruktoid or wshobson packs.
- PowerShell rules in this file (`lang-powershell`).
- Skipping classification because "it's a one-liner."
