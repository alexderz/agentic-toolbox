---
name: tdd
description: use this when implementing a feature or bugfix, changing behavior, or refactoring — write a failing test first, watch it fail for the right reason, then write the smallest code that passes. also use it to prune tests in the item's scope that guard no behavior.
---

# Test-driven development

Rewrite of `obra/superpowers` `skills/test-driven-development` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. Compress, not a paste. `skills/tdd/` is the skill home.

## The iron law

**No production code without a failing test first.**

Wrote code first? Delete it. Restart from a failing test. Do not keep it as reference, do not adapt it, do not glance at it while writing tests. Delete means delete.

## Ask first

Stop and ask the operator, or someone the operator names in writing, before skipping the cycle for a topic below. Ask per [Asking the operator](../sdlc/SKILL.md#asking-the-human).

| Topic | Why it is a stop |
| --- | --- |
| Renames / mechanical moves | Easy to treat as "no behavior" and skip the proof |
| Configuration-only changes | Config can still change runtime behavior |
| Throwaway / prototype | Fine to explore; throw the exploration away and rebuild the change with TDD if it ships |
| Generated code | Confirm it is generated and not behavior you owe a test |

Thinking "skip TDD just this once"? Stop. That is rationalization. Ask first — do not self-except.

## Red → green → refactor

One behavior at a time. Text cycle, not a diagram.

1. **Red.** Write one minimal failing test for the next behavior. Name the behavior. Prefer real code over mocks.
2. **Watch it fail for the right reason.** Run the test. Confirm it fails because the feature is missing — not a typo, import error, or assertion on existing behavior. If it passes immediately, the test is wrong. If it errors, fix the harness until it is a real failure.
3. **Green.** Write the smallest production code that makes that test pass. No extra features. No drive-by refactors.
4. **Watch it pass.** The new test is green; the rest of the suite stays green; output is clean.
5. **Refactor.** Only after green. Clean names and duplication. Do not add behavior. Stay green.
6. Repeat for the next behavior.

### Watch the fail

Mandatory. If you did not watch the test fail, you do not know it tests the right thing.

- Fail (assertion), not crash (syntax / import)
- Failure message matches what you expected
- Cause is "feature missing," not a broken test

Test already passes? You are testing existing behavior. Fix the test.

### Green is minimal

YAGNI. Hard-code if that is enough for this test. Do not add options, retries, or helpers the test does not require.

## Good tests

| Quality | Do | Don't |
| --- | --- | --- |
| Minimal | One behavior. "And" in the name? Split. | `validates email and domain and whitespace` |
| Clear | Name the behavior | `test1`, `works` |
| Real | Assert on the code's behavior | Assert that a mock was called |
| Intent | Show the API you want | Hide the contract behind fixtures |

## Prune tests that guard no behavior

Adapted from `caldoai/skills` `skills/prune-tests` @ `bd73b2ea5eb854ab8f0553fb41f77c8786f28f82` (MIT). Rewrite, not a paste.

A test **guards behavior** when it fails if something that users, callers, a ticket, the LLD or a **security** finding rely on regresses, and keeps passing when the code changes without that behavior changing. A **prune case** is a test that does not guard behavior.

**Scope.** The builder prunes only tests inside the current item's scope: tests of the behavior the item's ticket changes, and tests the ticket names for pruning. A ticket that asks for pruning may name a whole suite. On any other item, a test is not in scope only because the item edits its file. Do not edit a prune case outside that scope.

| The test | Action |
| --- | --- |
| Fails when a fixed bug comes back (a regression test) | Keep |
| Asserts that removed code, a moved file or an old path is absent, and no ticket, LLD, **security** finding or caller requires the absence | Delete |
| Asserts an absence that a ticket, LLD, **security** finding or caller requires, such as a removed endpoint staying gone | Keep |
| Asserts only what the browser, framework, language, or the type checker the repo's CI runs already guarantees | Delete |
| Mocks the unit under test, then asserts what the mock returns | Rewrite against the real unit; if nothing real is left to assert, delete |
| Computes its expected value with the same logic as the code | Rewrite with a literal expected value worked out by hand |
| Asserts private state, internal call order or which helper ran, and callers cannot observe it | Rewrite against what callers see; if callers see nothing, delete |
| Asserts a call or an order that is the contract: a sent message, a write, a charge, a protocol step | Keep |
| Guards the same behavior as another test through the same boundary (unit, integration or end-to-end), so every fault that fails one also fails the other | Delete the copy; keep the one closest to callers. A test through another boundary, or one that catches a fault the other misses, is not a copy, even on the same inputs |
| Fits no row, or the code, ticket and LLD do not show whether anyone relies on it | Keep; list it in `findings` |

Steps for the builder, for each prune case in scope:

1. Apply the row's action.
2. Delete production code that exists only for a deleted test, such as a `_resetCacheForTests` hook, after a repo-wide search finds no other caller.
3. Verify with the checks the item already uses; pruning adds no test runs of its own.
4. List each deleted or rewritten test, with its table row, in `findings`.

Pruning changes tests, not behavior. New or fixed behavior in the same item still follows red → green → refactor.

A failing test is not a prune case because it fails. Find the cause with `debug`, then compare the assertion with the accepted contract in the ticket or LLD:

| The mismatch | Action |
| --- | --- |
| The code breaks the accepted contract | Fix the code; keep the test |
| The accepted contract changed and the test still asserts the old one | Update the expected value to the new contract; cite the ticket or LLD line in `findings` |
| The code, ticket and LLD do not show which side is wrong | Change neither; report the mismatch in `findings` |

Never delete or weaken a test to hide a regression; fix the code, or report the mismatch.

```diff
-  expect(applyDiscount(100, 0.2)).toBe(100 - 100 * 0.2); // repeats the code's logic
+  expect(applyDiscount(100, 0.2)).toBe(80);
-  expect(cart._items.length).toBe(1);                    // private state
+  expect(cart.total()).toBe(book.price);
```

## Example: bug fix

**Bug:** empty email accepted.

**Red** — `rejects empty email` calls `submitForm({ email: '' })` and expects `error: 'Email required'`.

**Watch the fail** — assertion fails because the error is missing, not because the test cannot import the function.

**Green** — reject blank email. Nothing else.

**Refactor** — extract shared validation only if a later test demands it.

## Rationalizations (all false)

| Excuse | Reality |
| --- | --- |
| Too simple to test | Simple code still breaks. The test is cheaper than the bug. |
| I'll test after | After-the-fact tests pass immediately and prove nothing. You never watched them catch the miss. |
| Same goals, skip the ritual | Tests-after ask "what does this do?"; tests-first ask "what should this do?" |
| Already manually tested | No record, no rerun, easy to miss edges. |
| Deleting hours of code is waste | Sunk cost. Untrusted code is the waste. |
| Keep as reference | You will adapt it. That is testing after. Delete. |
| Need to explore first | Explore, then throw it away and start at red. |
| Hard to test | The design is wrong. Simplify the interface. |
| TDD will slow me down | Debugging in production is slower. |

## Red flags — delete and restart

- Production code before a failing test
- Tests written after the implementation
- Test passes on the first run
- Cannot explain why it failed
- "Just this once"
- "Keep as reference" / "adapt the existing code"
- "Spirit not ritual" / "I'm being pragmatic"

All of these mean: delete the production code. Start over at red.

## When stuck

| Problem | Move |
| --- | --- |
| Don't know how to test | Write the wished-for API and the assertion first. Ask. |
| Test is a novel | Design is a novel. Shrink the interface. |
| Everything needs a mock | Too coupled. Inject dependencies. |
| Setup is huge | Extract helpers; if still huge, simplify. |

Bug found later? Reproduce with a failing test, then follow the cycle. Never ship a bugfix with no test.

## Checklist

Before calling the work done:

- [ ] Each new behavior has a test
- [ ] Each test was watched failing for the right reason
- [ ] Production code was the minimum to go green
- [ ] Suite is green and output is clean
- [ ] Mocks only when unavoidable
- [ ] No test this item added is a prune case
- [ ] Edges and error paths covered

Missing a box? You skipped TDD. Restart.

## Final rule

Production code exists only after a test existed and failed first. Otherwise it is not TDD. No self-exceptions — Ask first.
