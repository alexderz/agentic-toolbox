---
name: lang-powershell
description: use this when writing or reviewing PowerShell — *.ps1, *.psm1. do not use for bash (load lang-shell / shell-safety).
---

# PowerShell

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. No `scripts/`.

## Iron law

**Stop on error. Quote. No `Invoke-Expression`.**

## Tooling / verify

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
# run the script in a throwaway session
# Pester if the repo already has it
```

Use `-WhatIf` when the cmdlet supports it.

## Idioms a linter misses

- Named parameters. Splat hashtables. No concatenated command strings.
- `-LiteralPath` when the path is data.
- Approved verbs on exported functions.
- `cmdletbinding` + `process` when the file is already that style.

## Errors

- `$ErrorActionPreference = 'Stop'` in scripts.
- Catch specific exceptions. No empty `catch`.

## Testing

- Pester if present. Otherwise run in a throwaway session and read
  errors.

## PR review

- No `iex`. No download-and-execute.
- Secrets not on the command line (they land in history).

## Security

- No `Invoke-Expression` / `iex` of data or model text.
- No unsigned remote scripts as the default path.
- Paths stay inside an allowlisted root.

## Always

- Strict mode. Stop on error. Named params.

## Ask first

- Running unsigned remote scripts.
- Changing execution policy.

## Never

- `Invoke-Expression` of untrusted text.
- Downloading and executing in one pipeline.
- Secrets on the command line.

## Red flags

- "iex is fine, I wrote the string"
- "Set-ExecutionPolicy Unrestricted just this once"
