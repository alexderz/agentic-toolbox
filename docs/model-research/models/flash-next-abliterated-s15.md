# Flash-Next Abliterated s1.5

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | weight-abliterated Flash-Next, IQ4_XS |
| Architecture | MoE, 125B total / 6B active |

## Summary

Flash-Next with refusal directions removed from the weights (strength 1.5). Text only.

## Verdict

Passed the long-horizon test 2 on llama.cpp 0.6 (6 tools, 20 tests, 120 minutes, 10.4 tok/s) and test 1 (5/5) on llama.cpp 0.4. Slightly behind Heretic2, which built one more tool at 40% higher speed.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Abliterated s1.5 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4_XS | 128k | 42 | 9.6 |
| Flash-Next Abliterated s1.5 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4_XS | 256k | 39 | 10.4 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 26 | 9.6 | 119 | 3 py | 4.5 | 128k | 42 | llama.cpp 0.4 | 8 subcommands |
| 2 | pass | 6 tools | 20 | 10.4 | 120 | 10/21 | 20.3 | 256k | 39 | llama.cpp 0.6 | [tests regraded 2026-10-07: 19/0 -> 20/0, grader now sums every cargo test target] Flash-Next Abliterated s1.5 on llama.cpp 0.6 (-ncmoe 39, 262k, -fit off), long-horizon settings (8 h cap): FULL PASS, 6 tools, 19 tests, 120 min, 10.4 tok/s, 0 compactions, ended on its own |

_Generated from the bake-off results on 2026-10-08._
