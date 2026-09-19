---
name: lang-cpp
description: use this when writing, reviewing, or testing C++ — *.cpp, *.cc, *.cxx, *.hpp. do not use for C-only changes (load lang-c) or Rust. do not paste the C++ Core Guidelines.
---

# C++

RAII and ownership, not a Core Guidelines dump. Compatible
with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**RAII owns every resource. Rule of Zero by default. No bare
`new`/`delete`.**

## Tooling / verify

Build the touched target with the project's system. Then:

```bash
# names vary
ctest --output-on-failure
# sanitizers when the project already has a sanitizer target
```

`-Wall -Wextra` stay on. Do not weaken flags to green the build.

## Idioms a linter misses

- `unique_ptr` default. `shared_ptr` only for real shared ownership.
- Const-correct. `enum class`. `nullptr`, not `NULL` or `0`.
- `override` on overrides. No object slicing: pass/return by reference
  or `unique_ptr`.
- Headers are self-contained. No `using namespace` in a header.
- Prefer STL algorithms when they are clearer than the loop. Do not
  invent clever iterator puzzles.
- Return local values; do not `return std::move(local)` (elision).
- `string_view` / `span` for non-owning views. Views must not outlive
  the owner.

## Errors

- Pick the file's policy: exceptions **or** error codes. Do not mix in
  one module.
- Never throw from a destructor.
- Check every I/O. `iostream` failbit is an error.

## Concurrency

- `std::lock_guard` / `unique_lock`. No manual lock/unlock.
- No shared mutable data without a mutex or atomic with a documented
  memory order.
- Do not hold a lock across a callback you do not control.

## Testing

- Use the harness already in the tree (GoogleTest, Catch2, doctest).
- Test ownership: moved-from objects are empty; views do not dangle.
- Sanitizer-clean on the new tests.

## PR review

- New special members: if you write one, you owe Rule of Five — or
  delete the rest. Prefer Rule of Zero.
- New `shared_ptr`: justify why unique ownership failed.
- `string_view` / `span` stored on a struct is a lifetime bug until proven otherwise.
- Include-what-you-use. No namespace pollution in headers.
- ABI / public headers: no `using namespace std`.

## Security

- Bounds on every C-string API that remains. Prefer `std::string`.
- Integer overflow on sizes same as C.
- No `reinterpret_cast` of untrusted bytes into objects.
- Command and path inputs: no `std::system` with concat.

## Always

- RAII for files, locks, sockets, allocations.
- Const and `override`.
- Tests under sanitizers when available.

## Ask first

- Introducing exceptions into a no-exception tree, or the reverse.
- A custom special member.
- `shared_ptr` as the default pointer in a new module.

## Never

- Bare `new`/`delete`. Manual lock/unlock.
- `using namespace std` in a header.
- Unchecked C-style casts.
- Treating C++ as "C with classes" (load `lang-c` for `.c` files).

## Red flags

- "unique_ptr is too noisy"
- "I'll delete it in the caller"
- "C++ is just C with classes"
- "shared_ptr fixes lifetime"
