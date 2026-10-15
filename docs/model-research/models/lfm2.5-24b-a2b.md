# LFM2.5-24B-A2B

**Status:** Tested

| | |
| --- | --- |
| Family | LFM |
| Source | LiquidAI/LFM2.5-24B-A2B (GGUF from LiquidAI/LFM2.5-24B-A2B-GGUF, LFM Open License v1.0) |
| Architecture | Hybrid MoE, 24.0B total / 2.45B active, 64 experts top-4, 131k context |
| Vision | no |

## Summary

Liquid's largest LFM2.5 model: text-only, always reasons, post-trained for tool use. The checkpoint is 24.0B parameters (23.97B in the BF16 file) with 2.45B active, 40 layers and a 128k vocabulary. Q4_K_M is 13.53 GiB and Q6_K is 18.34 GiB, so both fit a 24 GB card with the experts on the GPU. llama.cpp 0.6 already loads the lfm2moe architecture. unsloth's UD-Q4_K_XL, UD-Q5_K_XL and UD-Q6_K_XL (13.86, 16.69 and 20.36 GiB, imatrix quants) get tests 1 and 2 too, all with an f16 cache like Q4_K_M and Q6_K, which ran at 131k. UD-Q6_K_XL would need about 23,947 MiB at 131k, 11 MiB over our tuner's limit, so it runs at the largest context that loads (about 120k) rather than at 131k with a smaller q8_0 cache. The Context column shows what each run got.

## Verdict

Test 1 only, on llama.cpp 0.6 at 131k with an f16 cache. Q4_K_M was partial: 4 of 5 checks, 8 of its own tests passing, 4 subcommands, 157.6 tok/s, about 2 minutes, one compaction. Q6_K failed: 2 of 5 checks, 7 tests passing, 3 subcommands, 176.2 tok/s, about 1 minute. Qwen3.6-35B-A3B passed the same test 5 of 5 at 57.2 tok/s, so this is faster and less complete. Test 2 has not been run.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| LFM2.5-24B-A2B | no | – | – | – |

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| LFM2.5-24B-A2B Q4_K_M · llama.cpp 0.6 | llama.cpp 0.6 | Q4_K_M | 128k | – | 157.6 |
| LFM2.5-24B-A2B Q6_K · llama.cpp 0.6 | llama.cpp 0.6 | Q6_K | 128k | – | 147.7 |
| LFM2.5-24B-A2B UD-Q4_K_XL · llama.cpp 0.6 | llama.cpp 0.6 | UD-Q4_K_XL (unsloth) | 128k | – | 149.8 |
| LFM2.5-24B-A2B UD-Q5_K_XL · llama.cpp 0.6 | llama.cpp 0.6 | UD-Q5_K_XL (unsloth) | 128k | – | 146.7 |
| LFM2.5-24B-A2B UD-Q6_K_XL · llama.cpp 0.6 | llama.cpp 0.6 | UD-Q6_K_XL (unsloth) | 120k | – | 125.5 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | partial | 4/5 checks | 8 | 157.6 | 2 | 0 | 0.0 | 128k | – | llama.cpp 0.6 | 4 subcommands |
| 1 | fail | 2/5 checks | 7 | 176.2 | 1 | 1 py | 3.9 | 128k | – | llama.cpp 0.6 | 3 subcommands |
| 1 | pass | 5/5 checks | 12 | 149.8 | 2 | 1 py | 2.4 | 128k | – | llama.cpp 0.6 | 4 subcommands |
| 1 | pass | 5/5 checks | 18 | 146.7 | 83 | 1 py | 1.4 | 128k | – | llama.cpp 0.6 | 8 subcommands |
| 1 | pass | 5/5 checks | 6 | 125.5 | 2 | 3 py | 7.6 | 120k | – | llama.cpp 0.6 | 5 subcommands |
| 2 | fail | 0 tools | 2 | 150.3 | 7 | 15/24 | 203.3 | 128k | – | llama.cpp 0.6 | Init fail (checked in src/main.rs: the dispatcher has tools/list and tools/call but no initialize arm, so it answers -32601 Unknown method). tools/list itself answers when sent directly, but the grader stops after a failed handshake. 2 tests. 7 min, 150.3 tok/s, 90 turns, 59,815 … |
| 2 | partial | 3 tools | 0 | 147.7 | 21 | 51/53 | 1087.0 | 128k | – | llama.cpp 0.6 | Init fail (checked in src/main.rs: no initialize arm, answers -32601 Unknown method). list_entities gave no reply in 30s; 2 other tools returned no recorded data. 0 tests. 21 min, 147.7 tok/s, 158 turns, 183,927 output, no reasoning, 345 lines of Rust, 21,876 MiB. Same flags as … |

_Generated from the bake-off results on 2026-10-15._
