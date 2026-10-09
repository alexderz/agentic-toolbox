# Flash-Next Heretic2

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | Heretic2 (automated abliteration) of Flash-Next, IQ4XS-NGQ4 |
| Architecture | MoE, 125B total / 6B active |

## Summary

Flash-Next with refusals removed by Heretic's automated abliteration. Vision-capable.

## Verdict

Fastest of the big uncensored models. On llama.cpp 0.6 with long-horizon settings it passed test 2 (7 tools, 33 tests) in 120 minutes at 14.6 tok/s: about twice as fast as the Orcarouter fine-tune on the same engine, which built more (8 tools, 54 tests). Test 1 passed (5/5) on llama.cpp 0.4.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Heretic2 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4XS-NGQ4 | 128k | 42 | 8.7 |
| Flash-Next Heretic2 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4XS-NGQ4 | 256k | 40 | 14.6 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 25 | 8.7 | 123 | 0 | 0.0 | 128k | 42 | llama.cpp 0.4 | 12 subcommands |
| 2 | pass | 7 tools | 33 | 14.6 | 120 | 14/22 | 28.3 | 256k | 40 | llama.cpp 0.6 | [tests regraded 2026-10-07: 18/0 -> 33/0, grader now sums every cargo test target] Flash-Next Heretic2 on llama.cpp 0.6 (-ncmoe 40, 262k, -fit off), long-horizon settings (8 h cap): FULL PASS, 7 tools, 18 tests, 120 min, 14.6 tok/s over the run (twice the orcarouter run on the … |

_Generated from the bake-off results on 2026-10-09._
