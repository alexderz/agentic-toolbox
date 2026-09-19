---
name: tdd
description: use this when implementing a feature or bugfix, changing behavior, or refactoring — write a failing test first, watch it fail for the right reason, then write the smallest code that passes.
---

# Test-driven development

Rewrite of `obra/superpowers` `skills/test-driven-development` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`. Compress, not a paste. `skills/tdd/` is the skill home.

## The iron law

**No production code without a failing test first.**

Wrote code first? Delete it. Restart from a failing test. Do not keep it as reference, do not adapt it, do not glance at it while writing tests. Delete means delete.

## Ask first

Stop and ask the operator (or the pairing human) before skipping the cycle for:

| Topic | Why it is a stop |
| --- | --- |
| Renames / mechanical moves | Easy to treat as "no behavior" and skip the proof |
| Configuration-only changes | Config can still change runtime behavior |
| Throwaway / prototype | Fine to explore; throw the exploration away and remint with TDD if it ships |
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
- [ ] Edges and error paths covered

Missing a box? You skipped TDD. Restart.

## Final rule

Production code exists only after a test existed and failed first. Otherwise it is not TDD. No self-exceptions — Ask first.
