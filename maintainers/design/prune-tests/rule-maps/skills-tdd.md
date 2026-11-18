# Change map (light pass) — `skills/tdd/SKILL.md`

Item: DER-800. Vendor-derived skill: light pass per `maintainers/writing-standard.md`
Rule maps step 6.

Old: `skills/tdd/SKILL.md` at main c318ec7, lines 3, after 61, after 120. New:
[`skills/tdd/SKILL.md`](../../../../skills/tdd/SKILL.md). 127 lines old, 175 new
(cap 250). No old rule is removed or reworded.

Upstream: caldoai/skills `skills/prune-tests/SKILL.md` at
`bd73b2ea5eb854ab8f0553fb41f77c8786f28f82` (MIT, root `LICENSE`, copyright 2026 Maze),
fetched by git fetch and checkout into quarantine. The folder holds only `SKILL.md`.
Pinned in `SOURCES.md` (the `tdd` row); the source pin and this body are included in the same change before landing.

Protected rows touched: none. Operator clarifications (2026-09-27): none occur in
the changed lines. The frontmatter `description` is metadata, not a copy (Q16).

| Old L | Change | Disposition | New location |
| --- | --- | --- | --- |
| 3 | Frontmatter `description`: adds "also use it to prune tests in the item's scope that guard no behavior" | changed (metadata; DER-800) | L3 |
| after 61 | New section `Prune tests that guard no behavior`: provenance line; definitions of "guards behavior" and "prune case"; scope rule; condition → action table; four builder steps; a line that pruning is not new behavior; a failing-test mismatch table; one Never with its allowed action; a four-line diff example | changed (new rules; DER-800, adapted from upstream) | L63–108 |
| after 120 | Checklist box: no test this item added is a prune case | changed (route to L63 in the same file, backward reference) | L168 |

## Upstream intent and adaptations

| Upstream text | Here | Why |
| --- | --- | --- |
| "Prune every test that guards no behavior" (whole suite, optional path) | The builder prunes only tests of the behavior the item's ticket changes and tests the ticket names for pruning; a pruning ticket may name a whole suite; editing a file does not put its tests in scope; prune cases outside that scope are not edited | No silent scope leftover (DoD, `build-review.md#definition-of-done`); smallest change for the ask (`yagni`); feature work does not become a cleanup campaign; no approval gate and no report duty added |
| Keep a test only if it depends on intended behavior | "Guards behavior": fails on a regression in what users, callers, a ticket, the LLD or a **security** finding rely on | Checkable conditions (writing standard 2) |
| Delete tests that assert a removed feature or moved module is gone | Delete only when no ticket, LLD, **security** finding or caller requires the absence; otherwise keep | A removed endpoint that must stay gone is a guarded behavior |
| (not in upstream) | Regression tests for fixed bugs: keep | `tdd` already requires a test with every bugfix (old L110) |
| Delete tests of the browser, or of what the type system guarantees | Same, and the type check counts only if the repo's CI runs it | A type checker CI does not run guarantees nothing |
| Delete tests that mock the unit under test | Rewrite against the real unit; delete if nothing real is left | Keeps behavior the test may also cover (upstream step 2, "rewrite") |
| Delete tests on private state, internal call order or helpers | Same, when callers cannot observe it; keep a call or order that is the contract | A sent message, write, charge or protocol step is behavior callers see (MQ1) |
| No two tests guard the same behavior | A copy guards the same behavior through the same boundary and catches the same faults; another boundary, or a fault only one catches, is not a copy, even on the same inputs | Equal inputs do not show equal coverage |
| Delete production code that existed only for removed tests | Same, after a repo-wide search finds no other caller | A hook can have another caller |
| (not in upstream) | Unclear case: keep and list in `findings` | A safe default with no new ask gate |
| "Each one would fail on a regression" (done criteria) | Verify with the checks the item already uses; pruning adds no test runs | No mutation or full-suite run that the item does not already require (MQ3) |
| (not in upstream) | Pruning is not new behavior; new or fixed behavior still follows red → green → refactor | Keeps `tdd`'s iron law for behavior changes |
| (not in upstream) | A failing test is debugged against the accepted contract; fix the code if it is wrong, update a stale expected value when the contract changed, report when unclear; never delete or weaken a test to hide a regression | Pruning must not hide a red suite, and a stale assertion is not a regression (MQ4) |
| Five-file example diff | Four-line diff: literal expected value; caller-visible result | Compress, not a paste (intake step 5) |

No `scripts/`, no install command, no marketplace or `npx` text, no hooks, no
network use. The upstream README's install instructions are not carried.

## Meaning questions

- **MQ1** — Old L60 `Good tests` row "Real": "Don't: Assert that a mock was called".
  The new row keeps a test that asserts a call or order that is the contract. Do
  they conflict? Resolved from the text: old L60 guides how to write a new test;
  the new row decides whether to delete an existing one, and its definition (new
  L67) counts only what users, callers or a rule rely on. A sent message, write or
  charge is behavior a caller observes, so the new row describes a test that meets
  old L60's "Do". It does not license new mock-call assertions.
- **MQ2** — Does the scope rule add a gate or limit? Resolved from the text: it adds
  no approval and no ask. It applies the DoD "no silent scope leftover" and `yagni`,
  and adds no report duty or channel for out-of-scope cases; they are left unedited (DER-800 r1 R1).
- **MQ3** — Do old L36 "the rest of the suite stays green" and old L119 "Suite is
  green" now require a full-suite run for pruning? Resolved: those lines govern the
  red → green cycle for behavior changes and are unchanged; new L88 says pruning
  uses the checks the item already uses and adds none (DER-800 r1 correction). The
  unchanged `Checklist` ("Before calling the work done", old L114–121) still applies
  to pruning too; that commissions no new whole-suite or mutation run beyond the
  item's agreed checks and evidence (DER-800 r1 O4).
- **MQ4** — Does updating a failing test's expected value break the iron law or old
  L48 "Test already passes? … Fix the test"? Resolved: the update is allowed only
  when the ticket or LLD shows the accepted contract changed, and is cited in
  `findings`; otherwise the code is fixed or the mismatch reported. It adds no
  production code, so the iron law (old L12) is untouched.
