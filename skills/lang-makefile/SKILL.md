---
name: lang-makefile
description: use this when writing or reviewing Makefile / GNUmakefile. thin skill. do not use instead of the language skill for the code the Makefile builds.
---

# Make

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. No `scripts/`. The language being built
still loads its own skill.

## Iron law

**Every recipe is a real dependency graph. Tabs. Quoted variables.**

## Tooling / verify

```bash
make -n <target>     # print, do not run
make <target>        # then run the target you changed
```

Confirm only intended files changed.

## Idioms a linter misses

- `.PHONY` for non-file targets.
- Automatic vars (`$@`, `$<`, `$^`) instead of repeating names.
- One source of truth for flags (`CFLAGS`, `GOFLAGS`).
- Recipe lines fail closed. Do not hide errors with a leading `-`
  unless you say why.
- The default target is what a stranger should run.

## Errors

- A failed recipe stops the build. `.DELETE_ON_ERROR` if the project
  already uses it.

## Testing

- Run the changed target. Dry-run first when the target is destructive.

## PR review

- Tabs vs spaces in recipes.
- `rm -rf` is quoted and `${DIR:?}`-style guarded.
- Recursive make is not introduced as a new architecture.

## Security

- No `curl | sh` in a recipe.
- No unquoted destructive globs.

## Always

- `.PHONY`. Quoted paths. `make -n` on destructive targets.

## Ask first

- Generating files outside the repo.
- A new recursive make of another tree.

## Never

- Unquoted `rm -rf $(DIR)`.
- Treating Make as a list of shell scripts with no graph.

## Red flags

- "Make is just a script list"
- "The dash prefix makes it more reliable"
