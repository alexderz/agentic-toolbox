---
name: debug-pocock
description: use this as an alternative to debug when you want a tight red-capable feedback loop before any hypothesis — Pocock diagnosing-bugs shape. do not load with debug or debug-anthropic.
---

# Debug (Pocock alternative)

Rewrite of mattpocock/skills `diagnosing-bugs` @ `74ca5fe0`. Compress, not a paste. **Alternative** to default `debug`. Load **one** debug skill. No `scripts/`.

## Iron law

**No hypothesis until you have a tight loop that can go red on this exact symptom.** You have already run that command once (show output, secrets redacted).

## Phases

1. **Loop** — failing test, curl, CLI fixture, headless script, replay, harness, fuzz, bisect, or differential. Tighten: faster, sharper assert, more deterministic. Flakes: raise repro rate until debuggable. Cannot build a loop → stop, list tries, ask the operator.
2. **Reproduce + minimise** — same failure the user named. Shrink until every remaining piece is load-bearing.
3. **Hypothesise** — 3–5 ranked, each falsifiable (“If X, then changing Y …”). Show the list; don’t block if the operator is AFK.
4. **Instrument** — one variable; debugger over log-spam. Tag logs `[DEBUG-xxxx]` so cleanup is one grep. Perf: measure first.
5. **Fix** — failing test at a **real** seam (`tdd`), then fix, then re-run the original loop. No correct seam → that is the finding; do not fake a shallow test.
6. **Cleanup** — loop green, tagged logs gone, throwaways gone, winning hypothesis in the commit/PR.

## Always

Redact secrets in anything you show (`<REDACTED>`). Credentials stay in env, not in the log you paste.

## Never

- Load with `debug` or `debug-anthropic`.
- Copy `scripts/` from upstream.
- Hypothesise from reading code with no red-capable command.

## Upstream

mattpocock/skills `skills/engineering/diagnosing-bugs` @ `74ca5fe077456a0b3b2f5310cf9430999fd0b5fd` (MIT). See [SOURCES.md](../../SOURCES.md).
