# Rule map — `skills/language-router/SKILL.md`

Item: DER-318 (E7). Revised by DER-346 (G53): operator decisions Q17
and Q18, 2026-09-27 (MQ8, MQ9).

Old: `skills/language-router/SKILL.md` at main 7a11696, lines 1–81.
Old: `AGENTS.md` at main 7a11696, lines 53, 57–62, 175–226 (merged in;
this item does not edit `AGENTS.md`, DER-308 removes or routes them).
New: [`skills/language-router/SKILL.md`](../../../../skills/language-router/SKILL.md).
Disposition: **kept** (same rule, new file), **route** (the rule lives in
its owner; the old file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected rows touched: none. Operator clarifications (2026-09-27): none
of their subjects occur in this file. K2 exempt (standard 9).

## Old `skills/language-router/SKILL.md`

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–2, 4 | Frontmatter, `name` | kept | L1–2, L4 |
| 3 | Description: use when files could match more than one language skill, the language is unclear, or before code in a language not loaded; pick at most one; not for docs-only, git-only, planning-only turns | kept, trigger changed to "any turn that writes or reviews code" per the Outcome (MQ1); "owns" clause added to name the three rules | L3 |
| 6 | Heading "Language router" | kept | L6 |
| 8–9 | Map; points at existing ids and the `lang-*` guides; no `scripts/` | kept; the three example ids move into the language-skill definition | L9–11, L15–17 |
| 11 | Heading "Iron law" | kept, first | L13 |
| 13–15 | At most one language-family skill; a second only for a genuinely mixed-language diff; never load the catalog; never remint an existing id | kept; "language-family skill" → one name, **language skill**, defined at first use (standard 3); each "never" names the allowed action (standard 7) | L15, L21–26 |
| 17 | Heading "Algorithm" | kept; moved after Map, Family rules and Stubs so no step refers forward (standard 4) | L102 |
| 19 | List files the turn reads or writes | kept | L106 |
| 20 | Match the table; extensions and well-known filenames beat chat keywords | kept | L107–108 |
| 21 | One language owns ≥80% → load that skill only | kept; DER-346: step 5 first states that a proto-led change (proto ≥80%) with any hand-edited host code loads both (MQ8) | L110–113 |
| 22 | Two first-class languages (SQL + host, TSX + stylesheet, proto + hand-edited host) → load both | kept; parenthesis → "such as" examples (standard 8) (MQ7) | L114–116 |
| 23 | Stub language → load nothing, official docs, do not invent a pack | kept, as step 4 routing to Stubs; the rule itself at Stubs | L109, L98–100 |
| 24 | Read the chosen `SKILL.md`; stop routing; do not summarize the catalog | kept; "Do not" → "Never", allowed action beside it | L117–118 |
| 26 | Heading "Map" | kept | L51 |
| 28–29 | Table header | kept | L55–56 |
| 30 | Go row: pointer `lang-go` → one of `golang-safety` / `golang-testing` / `golang-security` | kept, merged with `AGENTS.md` L199 (MQ4); DER-346: the `lang-go` signals move in (MQ9) | L57 |
| 31 | Python row | kept, merged with `AGENTS.md` L200 | L58 |
| 32 | Shell row | kept, merged with `AGENTS.md` L201 | L59 |
| 33 | Rust row | kept | L60 |
| 34 | JS/TS row | kept; `package.json` added from `AGENTS.md` L203 (MQ3) | L61 |
| 35–51 | Rows C through Lua | kept verbatim (identical to `AGENTS.md` L204–220) | L62–78 |
| 53 | `*.tsx` is `lang-js-ts` unless primarily markup or CSS | kept | L83–84 |
| 55 | Heading "Family rules" | kept, as H3 under Map | L86 |
| 57 | TypeScript wins over JavaScript | kept | L88–89 |
| 58 | C++ wins over C; never both | kept, as if/then; "Never both" names `lang-c` | L90–91 |
| 59 | Go: default safety; tests → testing; input/auth/SQL/files/exec/crypto → security; never all three | dropped: duplicate, merged into the Go row (owner: this file L57; "One of" covers "never all three") | L57 |
| 60 | Frameworks are not language skills; do not invent one mid-session | kept; "Do not invent" → "Never create", allowed action beside it | L92–94 |
| 61 | Process skills may load with the one language skill; load one of the three debug skills | kept, as the Load-with list (MQ2, MQ5) | L41–49 |
| 62 | `discover-the-idea` gather-only, `buying-researcher` research-only, `ux-design` UX-only: no language skill | kept, as No-language turns rows (MQ6) | L28–38 |
| 64 | Heading "Stubs (no body)" | kept as "Stubs"; "no body" into the text | L96 |
| 66–67 | Stub list; say so; official docs only | kept; "load no language skill" and "never create a pack" from old L23 | L98–100 |
| 69 | Heading "Never" | kept | L120 |
| 71 | No second methodology router | kept, allowed action beside it | L122–123 |
| 72 | No two debug skills in one turn | kept, in the Load-with list | L48–49 |
| 73 | No remint of `golang-*`, `modern-python`, `shell-safety` | kept, in the iron law with the old L15 remint rule | L25–26 |
| 74 | No language skill on README-only, git-only, gather/refine-only, research-only, UX-only, templates-only turns | kept, as No-language turns rows | L35, L37–39 |
| 75 | No style guides in context "just in case" | kept, allowed action beside it | L124–125 |
| 77 | Heading "Red flags" | kept; lead-in line added naming the action | L127, L129 |
| 79–81 | Three red-flag thoughts | kept verbatim | L131–133 |

## Old `AGENTS.md` (merged)

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 53 | Load-table Language row: code turn → at most one language skill; table below or `language-router` first if ambiguous; pointers do not count | route: the row stays in the root `AGENTS.md` load table (owner of "which skill loads when"); DER-308 makes it one route to this file. Rules kept here; "if ambiguous" changed to any code turn (MQ1) | L3, L8, L15–19 |
| 57–60 | Process skills that may load with the one language skill (includes `sdlc-artifacts`); `shell-safety` when the turn includes shell | kept (MQ2); the `shell-safety` exception also named in the iron law | L22, L43–47 |
| 60–62 | `discover-the-idea` gather-only, `buying-researcher` research-only: no language skill | kept | L35, L38 |
| 175 | Heading "Language routing" | kept as this file (H1); DER-308 removes the section | L6 |
| 177–178 | At most one; a second only for a truly mixed-language diff; never load the catalog | kept ("truly" = "genuinely", old router L14) | L15, L21–23 |
| 179–181 | `tdd` / `verify-before-done` / `pr-review` / `security-hardening` / `yagni` / `debug` / `docs-google-style` / `tracker-sdlc` may load alongside | kept (MQ2) | L43–45 |
| 182 | `sdlc-onboarding`: an onboarding turn loads no language skill | kept | L34 |
| 183–184 | `discover-the-idea`: gather- and refine-only turns load no language skill | kept (MQ6) | L35 |
| 184–185 | Incoming-item Brief (problem + fix vs removal) loads no language skill | kept; link to the item brief owner added | L36 |
| 185–186 | `ux-design`: UX-only turns load no language skill | kept | L37 |
| 186–187 | `buying-researcher`: research-only turns load no language skill | kept | L38 |
| 187–188 | Load one of `debug` / `debug-pocock` / `debug-anthropic` | kept (MQ5) | L48–49 |
| 190–191 | If `language-router` is installed and the table is ambiguous, load it first, then the one skill it names | changed per the Outcome: the router loads on any code turn (MQ1); "then the one skill it names" kept as step 7 | L3, L8, L117 |
| 193–195 | Pointer ids exist so every identified language has a file; they do not count as a load; they route to the ids | kept | L17–19, L80–81 |
| 197–198 | Table header | kept | L55–56 |
| 199 | Go row: `golang-safety` default; `golang-testing` when writing tests; `golang-security` for input, auth, SQL, files, subprocesses, crypto; pick one; optional pointer | kept, merged with old router L30 (MQ4); "Optional" at L80–81 | L57 |
| 200 | Python row, optional pointer | kept | L58 |
| 201 | Shell row, optional pointer | kept | L59 |
| 202 | Rust row | kept | L60 |
| 203 | JS/TS row with `package.json` | kept (MQ3) | L61 |
| 204–220 | Rows C through Lua | kept verbatim | L62–78 |
| 222–223 | Stubs: no skill body, official docs only | kept | L98–100 |
| 225–226 | Frameworks are not language skills; do not invent one mid-session | kept | L92–94 |

New lines with no old line: L8 (defines **code turn** from `AGENTS.md`
L53 "Writing or reviewing code"), L30, L53 (table lead-ins), L104–105
(step 1 applies No-language turns).

## Rules moved in by DER-346

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| `lang-go` old L20 | Adding or changing tests, tables, race, goleak → `golang-testing` | moved into the Go row: "writing or changing tests or test tables, or when the change touches races or `goleak`"; before, only an agent that read the optional `lang-go` pointer saw it (MQ9) | L57 |
| `lang-go` old L21 | HTTP → `golang-security` | moved into the Go row's `golang-security` list; before, only an agent that read the optional `lang-go` pointer saw it (MQ9) | L57 |
| `lang-protobuf` old L9–10, L46–47 | Proto may be the second skill; any host language change loads the host skill | kept, as step 5's first sentence, for a proto-led change (proto ≥80%), the only case where `lang-protobuf` loaded and its rule applied (MQ8) | L110–112 |

### Before and after, DER-346

"Before" is project-main 44d6842. "After" is this item. Before, the
`lang-go` addendum reached an agent only when it read the optional
`lang-go` pointer; the `lang-protobuf` L8 host rule applied only when
`lang-protobuf` loaded.

| Case | Before | After |
| --- | --- | --- |
| Go: edit a table test, fix a race, or add `goleak` | `golang-testing` if the agent read `lang-go`; the router row alone named only "writing tests" | `golang-testing` (Go row) |
| Go: change an HTTP handler | `golang-security` if the agent read `lang-go`; the router row alone did not name HTTP | `golang-security` (Go row) |
| Proto ≥80% plus a small hand-edited Go change | `lang-protobuf` and the Go skill (step 5, then `lang-protobuf` L8 "if any") | `lang-protobuf` and the Go skill (step 5) |
| Go ≥80% plus a small proto change | Go skill only (step 5) | Go skill only (step 5) |
| Proto and Go both first-class, neither ≥80% | `lang-protobuf` and the Go skill (step 6) | `lang-protobuf` and the Go skill (step 6) |

## Meaning questions

- **MQ1** — When the router loads: old L3 (unclear or multi-match
  language), `AGENTS.md` L53 and L190–191 (only if the table is
  ambiguous). Resolved from the text: HLD "Rule owners" and area E, LLD
  E7 and the ticket Outcome set "loads on any code turn"; the accepted
  Spec chose this, not the rewording.
- **MQ2** — Load-with list: `AGENTS.md` L179–181 omits `sdlc-artifacts`;
  old router L61 and `AGENTS.md` L57–59 list it; only `AGENTS.md` L60
  adds `shell-safety` for a turn that includes shell. Resolved from the
  text: the merge keeps every skill any copy allowed; no copy forbade
  either.
- **MQ3** — `package.json`: in `AGENTS.md` L203, not in old router L34.
  Resolved from the text: the merge keeps the `AGENTS.md` row, the table
  the load table pointed to ("table below", L53).
- **MQ4** — Go row: old texts give no order when a change both writes
  tests and touches input, auth, SQL, files, subprocesses or crypto.
  Resolved from the text: wording and "one of" kept; no precedence
  added, so no reading is chosen.
- **MQ5** — "Load one of `debug` / `debug-pocock` / `debug-anthropic`"
  can read as "always load a debug skill". Resolved from old L72 ("Two
  debug skills in one turn" under Never): the rule caps the count;
  written "When a debug skill loads, load one".
- **MQ6** — Old L62 "gather-only" vs old L74 and `AGENTS.md` L183
  "gather- and refine-only". Resolved from the text: two of three copies
  include refine; the row keeps both.
- **MQ7** — Old L22 "first-class" is not checkable (standard 2).
  Resolved from the text: the word and its three examples are kept, no
  threshold is added; step 5 (≥80%) stays the checkable test.
- **MQ8** — Proto plus hand-edited host code: old L21–22 checks ≥80%
  before the two-language rule, so in a proto-led change a small host
  edit could stop at `lang-protobuf`, while `lang-protobuf` says "if
  any". Resolved by the operator 2026-09-27 (Q17): this file owns the
  rule. Step 5 loads both when proto owns ≥80% and any hand-edited host
  code changed (L110–113). When the host language owns ≥80%,
  `lang-protobuf` never loaded before, so its rule never applied; step 5
  still loads the host skill only. Step 6 keeps the proto example
  unchanged. `lang-protobuf` keeps a route with no condition.
- **MQ9** — Go signals: `lang-go` kept "changing tests, tables, race,
  goleak" and "HTTP" as an addendum to the Go row (DER-332, Q14). That
  pointer is optional (L80–81), so before this item the signals reached
  an agent only when it read `lang-go`; an agent that read only this
  file could load `golang-safety` for them. Resolved by the operator
  2026-09-27 (Q18): the Go row owns them (L57), so every code turn sees
  them; `lang-go` routes to `#map`. This is a deliberate change for
  agents that skipped the pointer. "Tables" are test tables (`lang-go`
  PR checklist "Tables in `_test.go`"). No precedence added (MQ4);
  overlapping signals are backlog DER-347.
