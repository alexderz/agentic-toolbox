---
name: lang-dart
description: use this when writing, reviewing, or testing Dart — *.dart, pubspec.yaml. language only; Flutter architecture is out of scope unless the file already is Flutter.
---

# Dart

Language, not a Flutter pack. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`. No
`scripts/`.

## Iron law

**Null safety is not optional. Await failures. Don't catch everything.**

## Tooling / verify

```bash
dart test
# or flutter test when the package is Flutter
dart analyze
```

## Idioms a linter misses

- Sound null safety. No `!` without an invariant.
- `final` default. Prefer immutability on public types.
- `async`/`await` over raw `then` chains unless the file is already
  that style.
- Libraries: `show` / hide exports so the public surface is small.

## Errors

- Typed errors or the project's result type.
- No empty `catch (e) {}`. Don't catch `Error`.

## Concurrency

- Isolates for CPU. Don't block the UI isolate with heavy work.
- Unawaited futures in app code are bugs (`unawaited` only when the
  file already documents fire-and-forget).

## Testing

- `package:test` or `flutter_test` as the package already uses.

## PR review

- New `dynamic` on a public API: reject.
- New `!`: named invariant or reject.
- Flutter widgets: this skill stays on Dart. Do not invent a BLoC
  religion.

## Security

- No concatenated SQL or process strings.
- Path joins inside an allowlisted root.
- Secrets not in `pubspec` or source.

## Always

- Null-safe types. Awaited futures. Tests.

## Ask first

- Adding Flutter to a pure Dart package.
- A new state-management package.

## Never

- Empty `catch`.
- `dynamic` as an escape hatch on public APIs.
- Concatenated SQL or process strings.

## Red flags

- "dynamic is faster to write"
- "I'll unawait it, it's just logging"
