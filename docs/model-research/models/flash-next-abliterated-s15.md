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

Test 1 passed (5/5) at 9.6 tok/s on llama.cpp 0.4. A long-horizon test-2 run on llama.cpp 0.6 is queued.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Abliterated s1.5 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4_XS | 128k | 42 | 9.6 |
| Flash-Next Abliterated s1.5 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4_XS | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 26 | 9.6 | 119 | 128k | 42 | llama.cpp 0.4 | 8 subcommands |

_Generated from the bake-off results on 2026-10-06._
