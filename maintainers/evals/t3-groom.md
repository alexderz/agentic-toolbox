# T3 fixture — `groom.md` of the scratch product

Commit everything below the line as
`.agents/design/calc-history-divide/groom.md` on project-main when
building the T3 snapshot ([t3-card.md](t3-card.md), Start state). It is
the frozen Groom plan for the T2 fixture LLD (`t2-lld.md`): the right
graph of the T2 key, seven links. `G<n>` here is key item `K<n>` in
[t3-key.md](t3-key.md). Fill `<epic-id>` when you commit it; fill the
`Tickets:` ids and `<plan-sha>` at the freeze commit. The Graph writes
one `←` per link, so `grep -o '←'` on it counts the seven links.

---

# Groom — calc: history and divide

Frozen record of the plan as reviewed at Groom on 2026-09-27. Not live:
the tracker is the source of truth for tickets, blockers and state.

- Chunk: `<epic-id>` · LLD: `docs/lld.md` · Date: `2026-09-27`
- Review: `groom-reviewer` — pass on `2026-09-27` at `<plan-sha>`
- Tickets: `G1` = `<id>`, `G2` = `<id>`, `G3` = `<id>`, `G4` = `<id>`,
  `G5` = `<id>`, `G6` = `<id>`

## Items

### G1: Parser and operator table
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-parser` · Branch: `item/<ticket-id>-parser` off `integrate/calc-history-divide`
- **Outcome** — `calc/parse.py` has `parse(args) -> Expr(a, op, b)` with numbers as `float`; `calc/ops.py` has `OPS`, operator symbol → function, for `+ - *`; `main()` calls `parse`, then `OPS[op](a, b)`.
- **Acceptance** — every existing test passes; bad input still exits 2; new tests cover `parse`; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — the full test suite passes on the item branch.
- **Blocked by** — `none` · **Blocks** — G2, G5
- **Out of scope** — the `/` operator; history. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: G4 also edits `calc/__main__.py`: land order, not a blocker.

### G2: Divide
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-divide` · Branch: `item/<ticket-id>-divide` off `integrate/calc-history-divide`
- **Outcome** — `OPS` has `/`; a zero divisor raises `CalcError("cannot divide by zero")`, defined in `calc/ops.py`; `main()` catches `CalcError`, prints its message to stderr, exits 2.
- **Acceptance** — `6 / 3` prints `2.0`; `1 / 0` prints `cannot divide by zero` and exits 2; tests for both; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — the full test suite passes on the item branch.
- **Blocked by** — G1 (`OPS` and `calc/ops.py` exist only after it) · **Blocks** — G6
- **Out of scope** — history. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: G5 edits the same lines of `main()`: land order, not a blocker.

### G3: History store
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-history-store` · Branch: `item/<ticket-id>-history-store` off `integrate/calc-history-divide`
- **Outcome** — `calc/history.py` has `append(line)` and `read_all() -> list[str]`; the file is `$CALC_HISTORY` if set, else `~/.calc_history`; one entry per line, UTF-8, created on first append.
- **Acceptance** — tests use a temporary `CALC_HISTORY` and cover append, read, and the first append creating the file; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — the full test suite passes on the item branch.
- **Blocked by** — `none` · **Blocks** — G4, G5
- **Out of scope** — the `history` command; recording results. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

### G4: History command
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-history-command` · Branch: `item/<ticket-id>-history-command` off `integrate/calc-history-divide`
- **Outcome** — `python -m calc history` prints every entry from `read_all()`, oldest first, or `no history` when there is none; this branch of `main()` runs before any parsing.
- **Acceptance** — tests seed the history file with `append()` and run no calculation; the empty case prints `no history`; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — the full test suite passes on the item branch.
- **Blocked by** — G3 (`read_all()`) · **Blocks** — G6
- **Out of scope** — recording results. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: G1 also edits `calc/__main__.py`: land order, not a blocker.

### G5: Record results
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-record-results` · Branch: `item/<ticket-id>-record-results` off `integrate/calc-history-divide`
- **Outcome** — after a successful evaluation, `main()` appends `<a> <op> <b> = <result>` with `append()`, from the parsed `Expr`; a failed evaluation records nothing and its exception propagates unchanged.
- **Acceptance** — `2 + 3` adds `2.0 + 3.0 = 5.0` to a temporary history; a failed evaluation adds no entry; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — the full test suite passes on the item branch.
- **Blocked by** — G1 (the parsed `Expr`), G3 (`append()`) · **Blocks** — G6
- **Out of scope** — the `history` command. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`
- Notes: G2 edits the same lines of `main()`: land order, not a blocker.

### G6: README usage section
- Type: Task · Parent: `<epic-id>` · LLD: `docs/lld.md#part-readme` · Branch: `item/<ticket-id>-readme` off `integrate/calc-history-divide`
- **Outcome** — `README.md` has a usage section whose examples are pasted from real runs of the built CLI, exact output text.
- **Acceptance** — every command and every error message this chunk adds; `python -m calc 2 + 3` then `python -m calc history` showing the recorded entry; one line under `## Unreleased` in `CHANGELOG.md`.
- **Verify** — each example, run on the item branch, prints the text the README shows.
- **Blocked by** — G2 (the divide-by-zero message), G4 (`calc history` output), G5 (recorded entries in that output) · **Blocks** — `none`
- **Out of scope** — code changes. **Proposed fix / Removal alternative / Pick / Plan / Spec** — `n/a — split from accepted Spec`

## Graph

- Wave 1: G1, G3
- Wave 2: G2 ← G1; G4 ← G3; G5 ← G1; G5 ← G3
- Wave 3: G6 ← G2; G6 ← G4; G6 ← G5

Gates: `none` — the LLD's Integration section is Build DoD, not an item.

Land order (not blockers): G2 and G5 edit the same lines of `main()`;
G1 and G4 both edit `calc/__main__.py`; every item adds a
`CHANGELOG.md` line. The later land rebases and keeps every line.
