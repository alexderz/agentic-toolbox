# Flash-Next Heretic2

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | Heretic2 (automated abliteration) of Flash-Next, IQ4XS-NGQ4 |
| Architecture | MoE, 125B total / 6B active |

## Summary

Flash-Next with refusals removed by Heretic's automated abliteration. Vision-capable.

## Verdict

Test 1 passed (5/5) at 8.7 tok/s on llama.cpp 0.4. A long-horizon test-2 run on llama.cpp 0.6 is queued.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Heretic2 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4XS-NGQ4 | 128k | 42 | 8.7 |
| Flash-Next Heretic2 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4XS-NGQ4 | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 25 | 8.7 | 123 | 128k | 42 | llama.cpp 0.4 | 12 subcommands |

_Generated from the bake-off results on 2026-10-06._
