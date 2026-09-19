---
name: lang-java
description: use this when writing, reviewing, or testing Java — *.java, pom.xml, build.gradle. language only; not a Spring skill. do not use for Kotlin (load lang-kotlin).
---

# Java

Language guide. No Spring / Jakarta religion. Compatible with
`tdd`, `verify-before-done`, `pr-review`, `security-hardening`.
No `scripts/`.

## Iron law

**Nulls are explicit. Resources close themselves. Dependencies point
inward.**

## Tooling / verify

```bash
# one of these, as the repo does
mvn -q test
gradle test
```

Do not add a second build tool. Read the surefire/gradle test output.

## Idioms a linter misses

- Records / sealed types when the language level allows and the type is
  data.
- Try-with-resources for every `AutoCloseable`.
- Constructor injection. Do not `new` a service inside another service
  if the module already injects.
- Never return `null` for a collection; return empty.
- `equals` and `hashCode` together. Prefer records.
- Prefer `final` locals when the file already does. No clever var
  shadowing.
- `java.time` over `Date` / `Calendar` for new code.

## Errors

- Specific exceptions. Wrap with cause. Do not catch `Exception` to
  return null.
- Checked exceptions: do not punch them through a listener that cannot
  declare them — map at the boundary.

## Concurrency

- Prefer `java.util.concurrent` over home-rolled wait/notify.
- Virtual threads: only if the project already uses them or the language
  level is there **and** you Ask first before flipping a thread model.
- No unsynchronized shared mutable state.
- `synchronized` on `this` is usually the wrong lock object for public
  types.

## Testing

- JUnit as the repo uses it. Assert on behavior, not log strings.
- Test doubles at I/O boundaries. Do not mock the type under test.

## PR review

- New public API: null contract documented or non-null by type
  (`Optional` only when absence is the point).
- No leaked persistence entities across a module boundary.
- Module / package cycles.

## Security

- No string-built SQL or process commands.
- `Runtime.exec` / `ProcessBuilder`: argument list, not a shell string.
- No `ObjectInputStream` / Java serialization of untrusted bytes.
- Paths stay inside an allowlisted root.

## Always

- Try-with-resources.
- Empty collections, not null lists.
- Tests for the new branch.

## Ask first

- Bumping the language level.
- Adding Spring / Jakarta annotations in a non-Spring module.
- Switching thread model to virtual threads.

## Never

- Empty `catch (Exception e) {}`.
- Public mutable static state.
- Raw types.
- `Runtime.exec` with concatenated input.

## Red flags

- "I'll null-check it at every call"
- "Spring will wire it" on a type that is not a bean
- "it's just a static Map"
