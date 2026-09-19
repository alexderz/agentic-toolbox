---
name: lang-swift
description: use this when writing, reviewing, or testing Swift — *.swift, Package.swift. do not use for Kotlin or Objective-C.
---

# Swift

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. No `scripts/`.

## Iron law

**Optionals are the type. Value types until you need identity. No
force-unwrap as a habit.**

## Tooling / verify

```bash
swift test
# or the Xcode test action the project uses
```

## Idioms a linter misses

- `let` default. `guard` / `if let` over `!`.
- Struct/enum for data. Class when identity or shared mutation is
  required.
- Protocol + extension over deep class trees.
- Access control is part of the API (`internal` default is fine;
  `public` is a contract).

## Errors

- `throws` / `Result` as the file already does.
- No `try!` on production paths.
- Typed errors that callers can switch on.

## Concurrency

- Isolation is part of the type (`@MainActor`, `Sendable`).
- Do not cross isolation domains with unsound types.
- `Task` has a cancellation story. Do not ignore `Task.checkCancellation`.

## Testing

- XCTest or Swift Testing as the package already uses.
- Test optionals via `guard` / `#expect`, not `!`.

## PR review

- New `!` / `try!`: reject without an invariant.
- New class: why not a struct?
- Retain cycles (`self` in escaping closures) named and broken
  (`[weak self]`).

## Security

- Keychain / secrets as the app already does. No secrets in source.
- No string-built SQL or shell.
- URL / path inputs stay inside an allowlisted container.

## Always

- `let`, `guard`, tests for the new branch.

## Ask first

- New concurrency annotations in a file that does not use them.
- Mixing Objective-C in a Swift package.

## Never

- `!` and `try!` as the default.
- Retain cycles with no story.
- String-built SQL or shell.

## Red flags

- "I'll force-unwrap, it's there"
- "class is simpler than struct"
