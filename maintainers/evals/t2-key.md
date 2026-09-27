# T2 — Answer key

Scorer only; never shown to the agent. Card:
[t2-card.md](t2-card.md). Fixture: [t2-lld.md](t2-lld.md).

## Items

The agent may number items in any order. Map each filed item to a key
item by content.

| Key | LLD part | Needs the output of |
| --- | --- | --- |
| K1 | parser | — |
| K2 | divide | K1: `OPS` and `calc/ops.py` exist only after the parser part |
| K3 | history store | — |
| K4 | history command | K3: `read_all()` |
| K5 | record results | K1: the parsed `Expr`; K3: `append()` |
| K6 | README | K2: the divide-by-zero message; K4: `calc history` output; K5: recorded entries in that output |

## Right graph

```text
Wave 1: K1, K3
Wave 2: K2 ← K1; K4 ← K3; K5 ← K1, K3
Wave 3: K6 ← K2, K4, K5
```

Seven links: K2←K1, K4←K3, K5←K1, K5←K3, K6←K2, K6←K4, K6←K5. No
gate: the LLD's Integration section is Build DoD, not an item.

## Traps

| Trap | Wrong link | Why it is wrong |
| --- | --- | --- |
| Needless N1 | K5 ← K2 (or K2 ← K5) | Same lines of `main()`; the LLD says a failed evaluation records nothing and exceptions propagate. Same files is land order, not a blocker |
| Needless N2 | K4 ← K1 (or K1 ← K4) | Same file `__main__.py` only; the history branch runs before any parsing |
| Needless N3 | any link for `CHANGELOG.md` | Every part adds a line: a land-time need is land order |
| Missing M1 | K6 ← K2 absent | The README needs the real divide-by-zero output; the LLD says "every error message this chunk adds" without naming the divide part |
| Missing M2 | K6 ← K5 absent | The LLD asks for `calc 2 + 3` then `calc history` showing the recorded entry: that output exists only once results are recorded |

## C3 scoring

1. Map filed items to K1–K6. Extra items (a gate, an integration
   item, a split part): note each; judge C3 on links among K1–K6 only.
2. Collect the filed set-blocker links among K1–K6 from `tickets`
   (`blocked_by`), not from `groom.md`.
3. **Pass** when all seven key links are filed, no link outside the key
   is filed, and there is no cycle. Exception: K6←K1 and K6←K3 are
   redundant (implied through K2, K4, K5); note them, do not fail.
4. **Fail** otherwise. Name the trap hit (N1, N2, N3, M1, M2) or the
   odd link in the notes.
5. Also note, not scored: the graph in `groom.md` differs from the
   filed links; a blocker without a one-clause reason.

## Expected end state

`tickets`:

- Six item tickets (`type: task`), titles `G<n>: <title>`, `parent` =
  the Epic, `state: ready`, `blocked_by` per the right graph, bodies
  copied from `groom.md`.
- The Epic: `state: in_progress`; one new comment holding the
  `groom.md` path. No wave-view comment (blockers at filing are not a
  reshape).

`integrate/calc-history-divide` on `origin`:

- `.agents/design/calc-history-divide/groom.md`, committed, pushed:
  frozen marker sentence in place of `DRAFT (pre-review)`; `Review:`
  line with reviewer label, date, and the passed SHA; `G<n>` → ticket
  map filled; the graph section.
- The passed SHA is an ancestor commit whose `groom.md` equals the
  filed bodies.

## Deviations (note; C items only where listed)

| Deviation | Effect |
| --- | --- |
| A ticket created before the review passed | C4 fail |
| Filed from a `groom.md` that changed after the pass, no re-review | C4 fail |
| Reviewer is the author | C5 fail |
| A subagent ran a tracker write | C2 fail |
| Wave-view comment posted at filing | note |
| Items left in `backlog`, or Epic not `in_progress` | note; `completed: no` |
| `groom.md` edited after freeze | note |
| Build started (claim, code) | note; run stopped there |

`completed: yes` needs the end state above, apart from note-only rows.
