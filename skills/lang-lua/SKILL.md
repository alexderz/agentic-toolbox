---
name: lang-lua
description: use this when writing, reviewing, or testing Lua — *.lua including Neovim, game, and embedded scripts. do not use for JavaScript.
---

# Lua

Thin-but-complete guide. You actually write Lua. Compatible
with `tdd`, `verify-before-done`, `pr-review`, `security-hardening`. No `scripts/`.

## Iron law

**Indexes start at 1. `pairs` is not `ipairs`. Know which Lua you are
on.**

## Tooling / verify

Run the project's test or the host (nvim headless, game harness) on the
changed file. `luacheck` if the tree already has it.

## Idioms a linter misses

- 1-based sequences. Do not port 0-based loops blindly.
- `ipairs` for the array part; `pairs` for maps. Do not mix and assume
  order.
- `local` by default. Globals are a bug unless `_G` is the point.
- `require` paths stay inside the project.
- Lua 5.1 / LuaJIT: no integer subtype. Beware bitwise libs and numbers
  past 2^53.
- Tables are the only data structure. Document whether a table is a
  list, a map, or both.

## Errors

- `error` / `assert` or the project's result convention (`nil, err`).
- Do not swallow with empty `pcall` unless you handle both returns.

## Concurrency

- Lua is typically single-threaded. Coroutines are not threads. Do not
  share a table across two hosts without a plan.
- Neovim: respect the event loop. No blocking syscalls on the main
  thread if the plugin already uses async.

## Testing

- Busted / the host's test command if present. Otherwise a small
  `assert` driver next to the module.

## PR review

- Off-by-one from a JS/C port.
- New global.
- `load` / `loadstring` of anything that is not a literal in-repo chunk.

## Security

- No `load` / `loadstring` / `dofile` of untrusted text.
- `os.execute` / `io.popen`: argument hygiene; prefer none.
- Neovim: no executing user text as Lua.

## Always

- `local`. `ipairs` vs `pairs` chosen on purpose. Tests or a host run.

## Ask first

- Switching Lua version (5.1 / 5.2 / 5.3 / 5.4 / LuaJIT).
- Loading C modules.

## Never

- `load` / `loadstring` of untrusted text.
- Assuming 0-based arrays.
- Mutating `_G` as architecture.

## Red flags

- "Arrays start at 0"
- "pairs and ipairs are the same"
- "I'll loadstring the user config"
