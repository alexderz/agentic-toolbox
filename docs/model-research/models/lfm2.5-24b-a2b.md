# LFM2.5-24B-A2B

**Status:** Tested

| | |
| --- | --- |
| Family | LFM |
| Source | LiquidAI/LFM2.5-24B-A2B (GGUF from LiquidAI/LFM2.5-24B-A2B-GGUF, LFM Open License v1.0) |
| Architecture | Hybrid MoE, 24.0B total / 2.45B active, 64 experts top-4, 131k context |

## Summary

Liquid's largest LFM2.5 model: text-only, always reasons, post-trained for tool use. The checkpoint is 24.0B parameters (23.97B in the BF16 file) with 2.45B active, 40 layers and a 128k vocabulary. Q4_K_M is 13.53 GiB and Q6_K is 18.34 GiB, so both fit a 24 GB card with the experts on the GPU. llama.cpp 0.6 already loads the lfm2moe architecture.

## Verdict

Test 1 only, on llama.cpp 0.6 at 131k with an f16 cache. Q4_K_M was partial: 4 of 5 checks, 8 of its own tests passing, 4 subcommands, 157.6 tok/s, about 2 minutes, one compaction. Q6_K failed: 2 of 5 checks, 7 tests passing, 3 subcommands, 176.2 tok/s, about 1 minute. Qwen3.6-35B-A3B passed the same test 5 of 5 at 57.2 tok/s, so this is faster and less complete. Test 2 has not been run.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| LFM2.5-24B-A2B Q4_K_M · llama.cpp 0.6 | llama.cpp 0.6 | Q4_K_M | 128k | – | 157.6 |
| LFM2.5-24B-A2B Q6_K · llama.cpp 0.6 | llama.cpp 0.6 | Q6_K | 128k | – | 176.2 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | partial | 4/5 checks | 8 | 157.6 | 2 | 0 | 0.0 | 128k | – | llama.cpp 0.6 | 4 subcommands |
| 1 | fail | 2/5 checks | 7 | 176.2 | 1 | 1 py | 3.9 | 128k | – | llama.cpp 0.6 | 3 subcommands |

_Generated from the bake-off results on 2026-10-14._
