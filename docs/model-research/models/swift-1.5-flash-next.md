# Swift 1.5 Flash-Next (pruned)

**Status:** Recommended

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | ukisai/Swift-1.5-Qwen3.8-Flash-Next-GSQ-RCO-GGUF |
| Architecture | MoE, pruned Flash-Next |

## Summary

An expert-pruned Flash-Next, GSQ-RCO IQ3_XXS. Smaller, so more of it stays on the GPU.

## Verdict

On Strata: test-2 full pass, 10 tools, 114 tests, 130 min. On llama.cpp 0.4 it ran out of time.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Swift 1.5 Flash-Next (pruned) · llama.cpp, experts in RAM | llama.cpp 0.4 | GSQ-RCO IQ3_XXS | 128k | 42 | 7.1 |
| Swift 1.5 Flash-Next · Strata, GPU expert cache, 262k context | Strata | GSQ-RCO IQ3_XXS | 256k | – | 21.4 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 96 | 7.1 | 161 | 4 py | 2.0 | 128k | 42 | llama.cpp 0.4 | 16 subcommands |
| 2 | pass | 10 tools | 114 | 21.4 | 130 | 21/38 | 18.2 | 256k | – | Strata | [tests regraded 2026-10-07: 63/0 -> 114/0, grader now sums every cargo test target] Strata v0.1.39, swift15 IQ3_XXS (rerun after PLE fix), NO thinking budget: full pass, 130 min, 21.4 tok/s over the run (40-45 decode), 147 steps, clean stop; 1 compaction whose summary looped in … |
| 2 | fail | 0 tools | – | 6.9 | 151 | 8/8 | 9.6 | – | – | llama.cpp 0.4 | does not build (Cargo.toml lib path missing); hit 3h cap while still writing the project after long spec/fixture study; no runaway, 6.9 tok/s |

_Generated from the bake-off results on 2026-10-10._
