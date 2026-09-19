---
name: lang-c
description: use this when writing, reviewing, or testing C — *.c, *.h without C++ files in the same change. do not use for C++ (load lang-cpp) or Rust.
---

# C

CERT-shaped, not a CERT paste. Compatible with `tdd`,
`verify-before-done`, `pr-review`, `security-hardening`. No
`scripts/`.

## Iron law

**Every buffer has a size. Every allocation has an owner. Every return
is checked.**

## Tooling / verify

```bash
# project flags first; do not invent a second build
cc -Wall -Wextra -Werror   # when the project already errors on warnings
# tests under sanitizers when the harness exists
ASAN_OPTIONS=detect_leaks=1 ./the-test
```

Prefer ASan + UBSan on tests. Do not claim DoD from a warning-free compile
without running the test binary.

## Idioms a linter misses

- Destination size is an argument to every copy/format
  (`snprintf`, `memcpy` with known `n`).
- `malloc` / `realloc` / `fopen` results are checked. One free path
  (goto-cleanup is fine if that is the file's style).
- Initialize everything. No indeterminate reads.
- Document who frees a returned pointer in the header comment.
- Headers: include guards or `#pragma once` as the repo already does.
  Minimal includes. No `using` — this is C.
- Prefer explicit widths (`uint32_t`) at ABI and file boundaries.

## Errors

- Return `int` error codes or the project's existing error type. Do not
  mix `errno` writes with ignored returns.
- Check every I/O and alloc. Partial writes are errors unless the API
  documents retry.

## Concurrency

- No data races. Shared mutable state needs a documented lock or is
  not shared.
- `volatile` is not a mutex.
- Signal handlers: async-signal-safe calls only, or don't.

## Testing

- Tests are real binaries or the project's harness. Assert on return
  codes and output, not "it compiled."
- Boundary cases: zero-length, max-length, alloc failure if you can
  inject it.

## PR review

- Every `memcpy`/`strcpy`/`sprintf` cousin has a bound in the diff.
- Ownership of every `*alloc` is visible.
- No new signed/unsigned surprises in length math.
- Public headers stay C-linkable (`extern "C"` only if the project
  already wraps).

## Security

- Integer overflow on sizes before `malloc(n * sz)` — check or use a
  helper the project already has.
- Format strings are literals. Never a user buffer as the format.
- No `gets`. No `scanf("%s")` without a width.
- Path and command inputs are untrusted. No `system()` with concat.

## Always

- Size next to the pointer.
- Sanitizer-clean tests when sanitizers exist.
- A named owner for every allocation.

## Ask first

- Changing signedness of a public API.
- Adding `goto` in a file that does not use cleanup-goto.
- Disabling a warning instead of fixing the site.

## Never

- `gets`, `strcpy`, `strcat`, `sprintf` into a fixed buffer.
- `strncpy` as a "safe strcpy" — it does not always NUL-terminate.
- Double-free, use-after-free, returning a stack pointer.
- Unchecked narrowing (`int64_t` → `int` / `size_t` surprises).
- Mixing `new`/`delete` into a `.c` file.

## Red flags

- "The buffer is big enough"
- "malloc never fails here"
- "I'll add the size check later"
- "It's C, sanitizers are overkill"
