---
name: lang-csharp
description: use this when writing, reviewing, or testing C# — *.cs, *.csproj, *.sln. do not use for Java or TypeScript. not a Unity or ASP.NET architecture skill.
---

# C#

Language guide. Compatible with `tdd`, `verify-before-done`,
`pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Nullable reference types on. Dispose what you acquire. Async all the
way down.**

## Tooling / verify

```bash
dotnet test --nologo
dotnet format --verify-no-changes   # when the repo already uses it
```

Run on the touched project. Read failing tests. Do not add a second
test framework.

## Idioms a linter misses

- Nullable enabled. Treat warnings as errors if the project already does.
- `await using` / `using` for `IDisposable` / `IAsyncDisposable`.
- Records / required members for values. Do not mutate DTOs in place
  if the file is already immutable.
- LINQ for clarity. Do not enumerate an expensive `IEnumerable` twice
  by accident.
- Public APIs: properties over public fields. `IReadOnlyList<T>` when
  the caller must not mutate.

## Errors

- Throw specific exceptions. Do not swallow.
- `OperationCanceledException` is cancellation, not a generic failure.
- Do not use exceptions for ordinary control flow.

## Concurrency

- `async Task`. No `async void` except event handlers.
- No `.Result` / `.Wait()` on Tasks (deadlock + thread-pool starve).
- `ConfigureAwait(false)` only if the project already does in libraries.
- `CancellationToken` is the last parameter and is plumbed.

## Testing

- xUnit / NUnit / MSTest as the repo chose.
- Test behavior through the public type. `IHttpClientFactory` / time /
  RNG are the mock boundaries.
- `async Task` tests. No `.Result` in tests either.

## PR review

- New `async void` in library code: reject.
- New `IDisposable` without `using` at call sites.
- Nullable suppression (`!`): local and named, or reject.
- Public surface: breaking changes to nullability are breaking.

## Security

- Parameterized SQL. No string concat into commands.
- No `BinaryFormatter` / insecure deserializers.
- `Process.Start`: argument array, never a concatenated command line.
- Secrets not in config committed to git. User-secrets / env as the
  project already does.

## Always

- Dispose / async-dispose.
- `await` the Task.
- Tests for the new branch.

## Ask first

- Disabling nullable for a file.
- Adding an analyzer package the repo does not have.
- Mixing sync-over-async to "keep this controller sync."

## Never

- `async void` in library code.
- `.Result` / `.Wait()` on production paths.
- Public fields on API types.
- `BinaryFormatter`.

## Red flags

- "I'll .Result it to keep this sync"
- "nullable is too noisy"
- "we dispose it in the finalizer"
