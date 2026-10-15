# Qwen3-VL-8B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | Qwen/Qwen3-VL-8B-Instruct |
| Architecture | Dense, 8B, vision |
| Vision | yes (head) |

## Summary

Small vision-language model. Also the text encoder for Qwen-Image 2.1.

## Verdict

0/5 on test 1: the code did not import.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| Qwen3-VL-8B | yes (head) | qwen3vl_merger | 1.16 GB | ~920 (est.) |

Setups that load the vision head or tower:

| Variant | Head lives on | Extra VRAM | Tokens per screenshot | Status |
| --- | --- | --- | --- | --- |
| Qwen3-VL-8B | GPU | +1.4-2.7 GB (est.) | ~920 (est.) | configured |

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3-VL-8B | llama.cpp 0.4 | Q4_K_M | 128k | – | 39.5 |
| Qwen3-VL-8B Q8 · llama.cpp 0.6, makers' sampling with presence penalty 1.5 | llama.cpp 0.6 | Q8_0 | – | – | 40.7 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 0 | 40.7 | 180 | 222 py | 418.1 | – | – | llama.cpp 0.6 | 7 subcommands |
| 1 | fail | 0/5 checks | – | 39.5 | 65 | 0 | 0.0 | 128k | – | llama.cpp 0.4 |  |

_Generated from the bake-off results on 2026-10-15._
