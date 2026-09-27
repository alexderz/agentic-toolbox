---
name: lang-go
description: use this when the change is Go but it is unclear which Go skill to load — routes to golang-safety, golang-testing, or golang-security. do not use as a fourth Go body. do not use for other languages.
---

# Go (router)

**This id routes.** Do not remint Go advice. No `scripts/`.
At most one language skill per turn, and the process skills that may load with it: `language-router` [Iron law](../language-router/SKILL.md#iron-law), [Load-with list](../language-router/SKILL.md#load-with-list).

## Iron law

**Never write a parallel Go guide.**

## Load

Which Go skill loads: the Go row in `language-router` [Map](../language-router/SKILL.md#map). Go-only addendum to that row:

| Situation | Load |
| --- | --- |
| Changing tests or tables; race; goleak | `golang-testing` |
| HTTP | `golang-security` |

Then stop. Apply that skill.

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
