---
name: language-router
description: use this when the files in play could match more than one language skill, when the language is unclear, or before writing code in a language that is not already loaded — pick at most one language-family skill. do not use for docs-only, git-only, or planning-only turns.
---

# Language router

Map. Points at existing ids (`golang-safety`, `modern-python`,
`shell-safety`) and the `lang-*` guides in this pack. No `scripts/`.

## Iron law

**Load at most one language-family skill per turn.** A second only when
the diff is genuinely mixed-language. Never load the catalog. Never
remint an id that already exists.

## Algorithm

1. List files this turn will read or write.
2. Match the table. Extension and well-known filenames beat chat keywords.
3. If one language owns ≥80% of the change, load that skill only.
4. If two languages are first-class (SQL + host, TSX + stylesheet, proto + hand-edited host), load both.
5. Stub language → load nothing, use official docs, do not invent a pack.
6. Read the chosen `SKILL.md`. Stop routing. Do not summarize the catalog.

## Map

| Files / signals | Load |
| --- | --- |
| `*.go`, `go.mod` | `lang-go` (pointer; does not count as a load) → **one** of `golang-safety` / `golang-testing` / `golang-security` |
| `*.py`, `pyproject.toml`, `uv.lock` | `lang-python` (pointer; does not count) → `modern-python` |
| `*.sh`, `*.bash`, shebang sh/bash, agent shell | `lang-shell` (pointer; does not count) → `shell-safety` |
| `*.rs`, `Cargo.toml` | `lang-rust` |
| `*.ts`, `*.tsx`, `*.js`, `*.mjs`, `*.cjs`, `tsconfig.json` | `lang-js-ts` |
| `*.c`, `*.h` and no C++ files | `lang-c` |
| `*.cpp`, `*.cc`, `*.cxx`, `*.hpp` | `lang-cpp` |
| `*.cs`, `*.csproj`, `*.sln` | `lang-csharp` |
| `*.java`, `pom.xml`, `build.gradle` | `lang-java` |
| `*.kt`, `*.kts` | `lang-kotlin` |
| `*.rb`, `Gemfile` | `lang-ruby` |
| `*.php`, `composer.json` | `lang-php` |
| `*.swift`, `Package.swift` | `lang-swift` |
| `*.dart`, `pubspec.yaml` | `lang-dart` |
| `*.sql` | `lang-sql` |
| `*.html`, `*.htm`, `*.css`, `*.scss` | `lang-web-markup` |
| `Dockerfile`, `*.dockerfile`, `compose.y*ml` | `lang-docker` |
| `*.tf`, `*.hcl` | `lang-terraform` |
| `Makefile`, `GNUmakefile` | `lang-makefile` |
| `*.ps1`, `*.psm1` | `lang-powershell` |
| `*.proto` | `lang-protobuf` |
| `*.lua` | `lang-lua` |

`*.tsx` is `lang-js-ts`, not `lang-web-markup`, unless the change is primarily markup or CSS.

## Family rules

- TypeScript wins over JavaScript when `tsconfig.json` or `*.ts`/`*.tsx` exists.
- C++ wins over C when any `.cpp`/`.hpp` is in the change. Never both.
- Go: default `golang-safety`. Tests → `golang-testing`. Input/auth/SQL/files/exec/crypto → `golang-security`. Never all three.
- Frameworks (React, Spring, Rails, FastAPI, Flutter) are not language skills. Do not invent one mid-session.
- Process skills (`tdd`, `verify-before-done`, `pr-review`, `security-hardening`, `yagni`, `sdlc-artifacts`, `debug`, `docs-google-style`, `tracker-sdlc`) may load with the one language skill. Load **one** of `debug` / `debug-pocock` / `debug-anthropic`.
- `discover-the-idea` is gather-only. `buying-researcher` is research-only. `ux-design` is UX-only. No language skill on those turns.

## Stubs (no body)

Elixir, Scala, Haskell, Zig, Solidity, Perl, Objective-C, R, Assembly.
Say so. Official docs only.

## Never

- A second methodology router beside this repo’s ids.
- Two debug skills in one turn (`debug` + `debug-pocock` / `debug-anthropic`).
- Remint `golang-*`, `modern-python`, or `shell-safety` under a new id.
- Language skills on README-only, git-only, gather/refine-only, research-only, UX-only, or templates-only turns.
- Dumping official style guides into context "just in case."

## Red flags

- "Load Go testing and safety and security to be thorough"
- "Polyglot repo, load every matching skill"
- "Install the vendor language pack instead of the id in this repo"
