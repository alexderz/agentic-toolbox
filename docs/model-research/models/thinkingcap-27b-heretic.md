# ThinkingCap Qwen3.8-27B Uncensored Heretic

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | OS-Software/ThinkingCap-Qwen3.8-27B-Uncensored-Heretic (mradermacher GGUF) |
| Architecture | Dense, 27B |

## Summary

A Heretic (automated abliteration) build of a Qwen3.8-27B fine-tune, Q4_K_M with a vision projector, run fully on the GPU on llama.cpp 0.6.

## Verdict

Passes both tests on llama.cpp 0.6, fully on the GPU: test 1 5/5 with 54 tests, test 2 a full pass with 8 tools and 30 tests in 52 minutes. The most tools of any uncensored 27B so far, at 25-31 tok/s: slower than the vLLM uncensored pick, which has no vLLM build for this model.

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
| 2 | pass | 8 tools | 30 | 25.3 | 52 | 192k | – | llama.cpp 0.6 | ThinkingCap-Qwen3.8-27B Uncensored Heretic Q4_K_M on llama.cpp 0.6, all on GPU, 196k q8_0: full pass, 8 tools, 30 tests, 52 min, 25.3 tok/s, 0 compactions, ended on its own |

_Generated from the bake-off results on 2026-10-06._
