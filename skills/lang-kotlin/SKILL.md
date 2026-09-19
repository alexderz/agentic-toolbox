---
name: lang-kotlin
description: use this when writing, reviewing, or testing Kotlin — *.kt, *.kts. do not use for Java-only files (load lang-java). not a Compose or Android architecture skill.
---

# Kotlin

Null safety and coroutines, not a framework pack. Compatible
with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Nullability lives in the type. Prefer immutability. Coroutines
cancel.**

## Tooling / verify

Run the module test task the repo already uses (`gradle test`, etc.).
`kotlin` compiler warnings stay on.

## Idioms a linter misses

- `val` default. `data class` for values. No `!!` unless you can name
  the invariant.
- Exhaustive `when` on sealed types.
- Platform types from Java: wrap at the boundary into a nullable or
  non-null Kotlin type. Do not let `String!` leak.
- Extension functions stay local to a module unless they are the API.

## Errors

- `Result` or exceptions as the file already does. Do not mix both in
  one API.
- No empty `catch`.

## Concurrency

- Pass a `CoroutineScope` in. No `GlobalScope.launch`.
- Handle cancellation (`ensureActive`, do not swallow
  `CancellationException`).
- Main-safe: no blocking IO on the main/UI dispatcher.
- `withContext(Dispatchers.IO)` for blocking JDK calls.

## Testing

- `runTest` for coroutines if the project uses it.
- Same JUnit / kotlin.test runner the module already has.

## PR review

- New `!!`: reject without an invariant comment.
- New `GlobalScope`: reject.
- Java interop boundary typed?

## Security

- Same JVM rules as `lang-java`: parameterized SQL, no concat into
  `ProcessBuilder`, no untrusted deserialize.

## Always

- `val`, exhaustive `when`, structured concurrency.
- Wrap Java platform types at the interop boundary.

## Ask first

- Calling a large Java API that returns platform types without a wrapper.
- Adding a coroutine library the module does not use.

## Never

- `!!` as a habit.
- `GlobalScope`.
- `runBlocking` on UI or request threads.
- Ignoring cancellation.
- Java-style empty catch.

## Red flags

- "It's never null"
- "GlobalScope is simpler"
- "I'll just block this coroutine"
