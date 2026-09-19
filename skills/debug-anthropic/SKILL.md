---
name: debug-anthropic
description: use this as an alternative to debug when you want a short reproduce-isolate-diagnose-fix report — Anthropic /debug shape. do not load with debug or debug-pocock.
---

# Debug (Anthropic alternative)

Rewrite of anthropics/knowledge-work-plugins `engineering/skills/debug` @ `ebd7990c`. Compress, not a paste. **Alternative** to default `debug`. Load **one** debug skill. No `scripts/`. Dropped host CONNECTORS placeholders.

## Iron law

**Root cause, then fix, then a guard.** Share error text exactly — do not paraphrase.

## Steps

1. **Reproduce** — expected vs actual, exact steps, scope (when, who).
2. **Isolate** — component/path, recent deploys/config/deps, logs.
3. **Diagnose** — hypotheses you can test, trace the path, name the cause not the symptom.
4. **Fix** — propose with side effects; add a regression test (`tdd`); verify (`verify-before-done`).

## Report

```
## Debug Report: <summary>
### Reproduction
- Expected / Actual / Steps
### Root Cause
### Fix
### Prevention
- Test to add
- Guard to put in place
```

## Always

Mention what changed (deploy, dep, config). Env splits (“staging vs prod”) go in Reproduction.

## Never

- Load with `debug` or `debug-pocock`.
- Invent monitoring you do not have.
- Skip Prevention.

## Upstream

anthropics/knowledge-work-plugins `engineering/skills/debug` @
`ebd7990cfa9495937da7726741e1ee6a96788565`. Apache-2.0: [LICENSE](LICENSE)
in this directory. See [SOURCES.md](../../SOURCES.md).
