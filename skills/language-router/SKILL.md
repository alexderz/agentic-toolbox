---
name: language-router
description: use this on any turn that writes or reviews code. it owns the language map, the process skills that may load with the one language skill, and the turns that load no language skill; pick at most one language skill. do not use for docs-only, git-only, or planning-only turns.
---

# Language router

Load this skill on every **code turn**: a turn that writes or reviews
code. This file owns three rules: the language map, the load-with list
and the no-language turns. It routes to existing ids and to the `lang-*`
guides in this pack. It has no `scripts/`.

## Iron law

**Load at most one language skill per turn.** A **language skill** is
`golang-safety`, `golang-testing`, `golang-security`, `modern-python`,
`shell-safety`, or a `lang-*` skill other than a pointer. A **pointer**
is `lang-go`, `lang-python` or `lang-shell`; a pointer does not count as
a load.

- Load a second language skill only when the diff is genuinely
  mixed-language, or `shell-safety` when the turn includes shell.
- Never load the catalog; read only the `SKILL.md` you chose and its
  pointer.
- Never remint an id that already exists, such as `golang-*`,
  `modern-python` or `shell-safety`; load the existing id.

## No-language turns

A turn in this table loads no language skill.

| Turn | Language skill |
| --- | --- |
| Onboarding turn (`sdlc-onboarding`) | none |
| Gather-only or refine-only turn (`discover-the-idea`) | none |
| Incoming-item Brief: problem, then fix vs removal ([Item brief](../../docs/sdlc/entry-brief-repo.md#item-brief)) | none |
| UX-only turn (`ux-design`) | none |
| Research-only turn (`buying-researcher`) | none |
| README-only, docs-only, git-only, planning-only or templates-only turn | none |

## Load-with list

1. These process skills may load with the one language skill: `tdd`,
   `verify-before-done`, `pr-review`, `security-hardening`, `yagni`,
   `sdlc-artifacts`, `debug`, `docs-google-style`, `tracker-sdlc`.
2. If the turn includes shell, `shell-safety` may also load with the
   one language skill.
3. When a debug skill loads, load **one** of `debug`, `debug-pocock` or
   `debug-anthropic`. Never load two of them in one turn.

## Map

Match files to a row. The Load column names the language skill.

| Files / signals | Load |
| --- | --- |
| `*.go`, `go.mod` | **One** of: `golang-safety` by default; `golang-testing` when writing or changing tests or test tables, or when the change touches races or `goleak`; `golang-security` when the change touches input, auth, HTTP, SQL, files, subprocesses, or crypto. Pointer: `lang-go`. |
| `*.py`, `pyproject.toml`, `uv.lock` | `modern-python`. Pointer: `lang-python`. |
| `*.sh`, `*.bash`, shebang sh/bash, agent shell | `shell-safety`. Pointer: `lang-shell`. |
| `*.rs`, `Cargo.toml` | `lang-rust` |
| `*.ts`, `*.tsx`, `*.js`, `*.mjs`, `*.cjs`, `tsconfig.json`, `package.json` | `lang-js-ts` |
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

Pointers exist so every identified language has a file. Reading a
pointer is optional; it routes to the language skill in its row.

`*.tsx` loads `lang-js-ts`, not `lang-web-markup`, unless the change is
primarily markup or CSS.

### Family rules

- TypeScript wins over JavaScript when `tsconfig.json` or a `*.ts` or
  `*.tsx` file exists.
- If any `.cpp` or `.hpp` file is in the change, load `lang-cpp`. Never
  load `lang-c` beside it.
- React, Spring, Rails, FastAPI and Flutter are frameworks, not language
  skills. Never create a framework skill mid-session; load the language
  skill its files map to.

## Stubs

Elixir, Scala, Haskell, Zig, Solidity, Perl, Objective-C, R and Assembly
have no skill body. For a stub language, load no language skill, say
so, and use the official docs only. Never create a pack for it.

## Algorithm

1. If the turn is a no-language turn, load no language skill. Stop
   routing.
2. List the files this turn will read or write.
3. Match each file to a Map row. Extensions and well-known file names
   beat chat keywords.
4. If a file's language is a stub, follow Stubs for it.
5. If `*.proto` files own ≥80% of the change and any hand-edited host
   code changed, load `lang-protobuf` and the host language skill.
   Otherwise, if one language owns ≥80% of the change, load that
   language skill only.
6. If two languages are first-class in the change, such as SQL and its
   host language, TSX and a stylesheet, or proto and hand-edited host
   code, load both.
7. Read the chosen `SKILL.md`. Stop routing. Never summarize the
   catalog; name only the skill you load.

## Never

- Never add a second methodology router beside this repo's ids; route
  with this file.
- Never paste official style guides into context "just in case"; read
  only the chosen `SKILL.md` and its pointer.

## Red flags

If you think one of these, stop and reread the iron law:

- "Load Go testing and safety and security to be thorough"
- "Polyglot repo, load every matching skill"
- "Install the vendor language pack instead of the id in this repo"
