# Qwen3.6-27B

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.6 |
| Source | Qwen/Qwen3.6-27B |
| Architecture | Dense, 27B |
| Vision | yes (head) |

## Summary

The previous dense Qwen.

## Verdict

Good on test 1; on test 2 its server had no initialize method. Superseded by Qwen3.8-27B.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| Qwen3.6-27B | yes (head) | qwen3vl_merger | 0.93 GB | ~920 (est.) |

- Qwen3.6-27B: no setup we run loads its vision head or tower: every variant runs blind.

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.6-27B · llama.cpp, all on GPU | llama.cpp 0.4 | Q4_K_M | 128k | – | 30.7 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 65 | 30.7 | 20 | 1 py | 0.6 | 128k | – | llama.cpp 0.4 | 7 subcommands |
| 2 | partial | 7 tools | 22 | 24.5 | 23 | 6/16 | 19.6 | 192k | – | llama.cpp 0.4 | no initialize method (-32601 Method not found); tools/list and calls work without it, but no client gets past the handshake; replies to notifications |

_Generated from the bake-off results on 2026-10-15._
