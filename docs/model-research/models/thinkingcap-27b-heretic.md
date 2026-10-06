# ThinkingCap Qwen3.8-27B Uncensored Heretic

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | OS-Software/ThinkingCap-Qwen3.8-27B-Uncensored-Heretic (mradermacher GGUF) |
| Architecture | Dense, 27B |

## Summary

A Heretic (automated abliteration) build of a Qwen3.8-27B fine-tune, Q4_K_M with a vision projector, run fully on the GPU on llama.cpp 0.6.

## Verdict

Test 1 on par with stock Qwen3.8-27B on llama.cpp (5/5, 54 tests, 31 tok/s). Test 2 in progress.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| ThinkingCap-27B Heretic · llama.cpp 0.6, all on GPU | llama.cpp 0.6 | Q4_K_M | 192k | – | 31.3 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 54 | 31.3 | 24 | 192k | – | llama.cpp 0.6 | 9 subcommands |

_Generated from the bake-off results on 2026-10-06._
