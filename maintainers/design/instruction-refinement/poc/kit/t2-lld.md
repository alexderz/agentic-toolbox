# T2 fixture — `docs/lld.md` of the scratch product

Commit everything below the line as `docs/lld.md` on project-main when
building the T2 snapshot ([setup.md](setup.md)). `<epic-id>` is the
snapshot's Epic id. The part names are neutral on purpose: the key maps
items by content, not by order.

---

# LLD — calc: history and divide

- Chunk: `<epic-id>` (`calc-history-divide`)
- HLD: n/a — toy chunk; the brief on the Epic is the plan
- Date: `2026-09-26`
- Status: accepted. **security**: no trust boundary moves (local files
  only); `n/a` accepted.

## Paths

| Path | Change |
| --- | --- |
| `calc/__main__.py` | entry point; several parts edit `main()` |
| `calc/parse.py` | new: parser |
| `calc/ops.py` | new: operator table and errors |
| `calc/history.py` | new: history store |
| `tests/` | one test file per part |
| `README.md` | usage section |
| `CHANGELOG.md` | every part adds one line under `## Unreleased` |

## Part: parser

Move parsing out of `__main__.py`. `calc/parse.py` gets
`parse(args) -> Expr(a, op, b)` (numbers as `float`). `calc/ops.py`
gets `OPS`, a table from operator symbol to function, for `+ - *`.
`main()` calls `parse`, then `OPS[op](a, b)`. Behaviour is unchanged.
Tests: every existing case still passes; bad input still exits 2.

## Part: divide

Add `/` to `OPS` in `calc/ops.py`. A zero divisor raises
`CalcError("cannot divide by zero")`, a class defined in `calc/ops.py`.
`main()` catches `CalcError`, prints its message to stderr, and exits
with code 2. Tests: `6 / 3` prints `2.0`; `1 / 0` prints the message
and exits 2.

## Part: history store

`calc/history.py` with `append(line)` and `read_all() -> list[str]`.
The file is `$CALC_HISTORY` if set, else `~/.calc_history`; one entry
per line, UTF-8, created on first append. Tests use a temporary
`CALC_HISTORY`.

## Part: history command

`python -m calc history` prints every entry from `read_all()`, oldest
first. No entries → prints `no history`. This branch runs in `main()`
before any parsing. Tests seed the history file directly with
`append()`; they do not run calculations.

## Part: record results

After a successful evaluation, `main()` appends `<a> <op> <b> =
<result>` with `append()`, using the parsed `Expr`. A failed
evaluation records nothing: any exception propagates unchanged, before
the append. This part edits the same lines of `main()` as the divide
part. Tests: `2 + 3` adds `2.0 + 3.0 = 5.0` to a temporary history.

## Part: README

A usage section in `README.md`. Its examples are pasted from real runs
of the built CLI, with the exact output text: every command and every
error message this chunk adds, and the sequence `python -m calc 2 + 3`
then `python -m calc history`, showing the recorded entry.

## Integration

After every part has landed, the manager runs the full test suite on
project-main before Trunk (Build DoD). Nothing else runs across parts.

## Trust boundaries

`n/a`: no new input source beyond argv, no network, no secrets; the
history file is the user's own.

## Acceptance

- `python -m calc 1 / 0` prints `cannot divide by zero`, exits 2.
- `python -m calc 2 + 3` then `python -m calc history` shows
  `2.0 + 3.0 = 5.0`.
- README examples match real output.
