---
name: lang-go
description: use this when the change is Go but it is unclear which Go skill to load — routes to golang-safety, golang-testing, or golang-security. do not use as a fourth Go body. do not use for other languages.
---

# Go (router)

**This id routes.** Do not remint Go advice. Load **one** existing Go skill.
Compatible with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Pick one Go skill. Never load all three. Never write a parallel Go guide.**

## Load

| Situation | Load |
| --- | --- |
| Default write or review of `*.go` | `golang-safety` |
| Adding or changing tests, tables, race, goleak | `golang-testing` |
| Input, auth, SQL, files, subprocesses, crypto, HTTP | `golang-security` |

Then stop. Apply that skill. Pair process skills as they already say.

## Combined verify (after the chosen skill)

```bash
gofmt -l .
go test ./...
go test -race ./...
```

Add `staticcheck` / `errcheck` when **tester** already wired them. Read the output.

## Combined PR checklist

- Errors wrapped with `%w`; compared with `errors.Is` / `As`, not `==`.
- `context.Context` is first param and is plumbed, not stored on structs.
- No goroutine without a documented lifetime (return, ctx cancel, or WaitGroup).
- No string-built SQL or `os/exec` from concatenated input.
- Tables in `_test.go` for the new behavior.

## Never

- A new `lang-go` body that copies samber or Effective Go into this repo.
- `npx` / marketplace install of `samber/cc-skills-golang`.
- Loading `golang-safety` + `golang-testing` + `golang-security` in one turn.
