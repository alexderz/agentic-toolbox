---
name: lang-rust
description: use this when writing, reviewing, or testing Rust — Cargo.toml, *.rs, clippy, borrow checker, unsafe, async Tokio. do not use for C, C++, or Go. do not dump Microsoft or leonardomso rule catalogs into context.
---

# Rust

Language guide. Distills what agents get wrong; not a paste of
the Microsoft Pragmatic Rust Guidelines or a 200-rule dump. Compatible
with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Do not clone, unwrap, or `unsafe` your way around the type system.**
Own, borrow, or share on purpose.

## Tooling / verify

```bash
cargo fmt --check
cargo test --all-targets
cargo clippy --all-targets -- -D warnings
```

Workspace: run on the touched crate, then the workspace if the API crossed
a crate boundary. Read the output. A green `cargo check` is not enough.

## Idioms a linter misses

- Ownership is the API: owned value, `&T`, `&mut T`. `Arc<Mutex<T>>` only
  when shared mutation is real and documented.
- Invalid states are unrepresentable. Newtypes and enums over stringly
  modes. Parse at the boundary; do not re-validate in every function.
- `impl Trait` in return position when there is one type. `Box<dyn Trait>`
  only for genuine heterogeneity.
- Builders validate in `build()`, not in every setter.
- `Drop` owns cleanup. No manual free paired with a comment.
- `From` for error conversion in libraries. `map_err` only when the
  target type is not yours to implement `From` for.
- Modules stay balanced. Do not re-export the same item on two paths.

## Errors

- Library crates: typed errors (`thiserror` or equivalent already in the
  tree). Application glue may use `anyhow` if the crate already does.
- `?` on `Result`/`Option`. No `unwrap` / `expect` on production paths.
- `expect` in tests is fine when the panic message names the invariant.
- Do not catch panics as control flow (`catch_unwind` is Ask first).

## Concurrency

- `Send`/`Sync` are part of the API. Do not lie with `unsafe impl`.
- Do not hold a `Mutex`/`RwLock` guard across `.await`.
- Blocking or CPU work: `spawn_blocking` or a dedicated thread. Do not
  stall the runtime.
- Channels and tasks have a shutdown story (cancel token, drop of sender,
  or JoinHandle awaited).

## Testing

- Unit tests next to the code. Integration tests under `tests/`.
- Table-driven: array of cases + `for`. Name the case.
- Property tests for parsers, codecs, and invariants if the crate already
  uses proptest/quickcheck — do not add a framework unasked.
- `#[should_panic]` is last resort; prefer a `Result` assertion.

## PR review

- New `clone()`: is it required, or is it silencing borrowck?
- New `unsafe`: SAFETY comment names a falsifiable invariant. Tests hit
  the boundary. Public API around it is safe to call.
- Public types: is there one path to the item? Docs on every public item.
- Error type changes are API. Wrapping vs replacing matters.
- No `todo!()` / `unimplemented!()` on the shipped path.

## Security

- No hand-rolled crypto. Use the crate the project already picked.
- Path joins stay inside an allowlisted root. No `../` trust.
- Command args are arrays, never a shell string.
- `unsafe` + FFI: treat foreign data as untrusted until parsed into
  owned Rust types.

## Always

- `clippy` clean or an `allow` that explains why.
- `Result` on fallible public functions.
- Tests for the new branch before calling it done (`tdd` if the change
  is behavior).

## Ask first

- Any `unsafe`.
- Interior mutability as the default design (`RefCell`, global `Mutex`).
- MSRV bump, edition bump, or a new async runtime.
- Adding `unwrap` in a library crate.

## Never

- `unwrap()` on production paths.
- `.clone()` as a habit to please borrowck.
- `unsafe` without `// SAFETY:`.
- `transmute` or raw pointer arithmetic outside a reviewed boundary.
- Catching panics as logic.
- Pasting the 33k-token Microsoft "all guidelines" file into context.

## Red flags

- "I'll just clone it"
- "unwrap is fine, we know it's Some"
- "unsafe is faster"
- "`Box<dyn Trait>` everywhere is simpler"
- "cargo check passed so it's good"
