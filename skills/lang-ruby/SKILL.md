---
name: lang-ruby
description: use this when writing, reviewing, or testing Ruby — *.rb, Gemfile. do not use for Rails-only architecture; stay on the language. do not use for Python.
---

# Ruby

Language, not a Rails pack. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`. No
`scripts/`.

## Iron law

**Be explicit. Don't monkey-patch in app code. Parameters, not string
SQL.**

## Tooling / verify

```bash
bundle exec rspec    # or
bundle exec rake test
```

Use whatever the repo already runs. Do not add a second test framework.

## Idioms a linter misses

- Keyword args for 3+ parameters.
- Frozen string literals if the file/project already uses them.
- Raise specific errors. Do not rescue `StandardError` to return nil.
- Enumerable methods over index loops when they are clearer.
- Predicate methods end in `?`. Bang methods mutate or raise as the
  existing API already does — do not invent a new convention.

## Errors

- Rescue the type you can handle. Re-raise the rest.
- No empty rescue. No `rescue nil`.

## Concurrency

- MRI threads are not a scaling plan. If you add threads, document
  what is shared and what is not.
- No mutable class variables as global state.

## Testing

- minitest or RSpec as the repo chose. One behavior per example.
- Doubles at I/O boundaries. Do not stub the type under test into
  meaninglessness.

## PR review

- New gem: why not stdlib or an existing gem?
- New monkey-patch of a core class: reject in app code.
- SQL and shell interpolation.

## Security

- SQL via binds. No `#{user}` in queries.
- No `eval`, no `send` of untrusted names, no `constantize` of user
  strings.
- `system` / backticks: argument arrays, not interpolated strings.
- Mass-assignment: permit lists as the framework already does.

## Always

- Specific raises. Binds. Tests for the new branch.

## Ask first

- Adding a gem when stdlib will do.
- Introducing Rails helpers in a non-Rails gem.

## Never

- Rescue-and-ignore.
- Monkey-patching core classes in application code.
- `eval` / untrusted `send`.
- Interpolated `system`.

## Red flags

- "I'll rescue StandardError and move on"
- "It's Ruby, duck typing means no checks"
- "send is fine, the string is almost static"
