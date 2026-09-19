---
name: debug
description: use this when a test fails, a bug appears, or behavior is unexpected — find root cause before any fix. default debugging skill. do not use to skip TDD or to land past an open blocker.
---

# Debug (default)

Rewrite of obra/superpowers `systematic-debugging` @ `b36e0829`. Compress, not a paste. **Default** debug skill. Alternatives in this repo: `debug-pocock` (tight loop first), `debug-anthropic` (short report). Load **one**.

Pairs with `tdd` (failing test for the cause) and `verify-before-done` (prove the fix). No `scripts/`.

## Iron law

**No fix without root cause.** Phase 1 first. Symptom patches are failure.

## When

Test failures, unexpected behavior, build/integration breaks, performance. Especially under time pressure or after a failed “quick fix.”

## Phases (in order)

### 1. Root cause

- Read the full error and stack. Note files, lines, codes.
- Reproduce. If you cannot, gather data — do not guess.
- Check recent changes (diff, deps, config, env).
- Multi-component: log enter/exit at each boundary, run once, see **where** it breaks, then go there.
- Deep stack: trace the bad value **up** to its source. Fix the source.

### 2. Pattern

Find working similar code. Read the reference completely. List every difference. Name dependencies and assumptions.

### 3. Hypothesis

One hypothesis: “X is the root cause because Y.” Smallest test of that one variable. Worked → phase 4. Failed → new hypothesis, do not stack fixes. If you do not know, say so.

### 4. Fix

1. Failing test for this cause (`tdd`).
2. One change. No “while I’m here.”
3. Verify (`verify-before-done`). Full relevant suite, not vibes.
4. Failed fix: if fewer than 3 attempts, back to phase 1. **If 3+ failed: stop. Question architecture with the operator.** Do not attempt fix #4 alone.

## Always

- One variable at a time.
- After a confirmed cause, add a guard if the layer can lie (validation at the boundary that failed).
- Remove temporary instrumentation before land.

## Ask first

- Fourth fix attempt or an architectural change after 3 failures.
- Production-only instrumentation.

## Never

- “Quick fix now, investigate later.”
- Several untested changes in one run.
- Skip the failing test.
- Land past an open blocker because debugging “unblocked” you in chat.

## Red flags

- “It’s probably X”
- “Just try changing this”
- Each fix reveals a new symptom elsewhere
- Lists of fixes with no investigation

## Upstream

obra/superpowers `skills/systematic-debugging` @ `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` (MIT). See [SOURCES.md](../../SOURCES.md).
