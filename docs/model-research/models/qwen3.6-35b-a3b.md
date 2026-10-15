# Qwen3.6-35B-A3B

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.6 |
| Source | Qwen/Qwen3.6-35B-A3B |
| Architecture | MoE, 35B / 3B active |
| Vision | yes (head) |

## Summary

Small-active MoE, mostly on the GPU.

## Verdict

57 tok/s and good on test 1; its test-2 server listed no tools. Superseded by Qwen3.8.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B | yes (head) | qwen3vl_merger | 0.90 GB | ~920 (est.) |

Setups that load the vision head or tower:

| Variant | Head lives on | Extra VRAM | Tokens per screenshot | Status |
| --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B · llama.cpp, some experts in RAM | GPU | +1.4-2.7 GB (est.) | ~920 (est.) | configured |

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B · llama.cpp, some experts in RAM | llama.cpp 0.4 | UD-Q4_K_M | 128k | 12 | 57.2 |
| Qwen3.6-35B-A3B Q6 · llama.cpp 0.6, 18 expert layers in RAM, 131k, coding sampling (temperature 0.6) | llama.cpp 0.6 | UD-Q6_K_XL | – | – | 38.1 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 83 | 38.1 | 25 | 1 py | 0.6 | – | – | llama.cpp 0.6 | 10 subcommands |
| 1 | pass | 5/5 checks | 52 | 57.2 | 10 | 0 | 0.0 | 128k | 12 | llama.cpp 0.4 | 9 subcommands |
| 2 | partial | 9 tools | 9 | 36.2 | 17 | 9/12 | 44.8 | – | – | llama.cpp 0.6 | checked by hand: initialize answers with snake_case keys (protocol_version, server_info, capabilities nested twice), so a client finds no protocolVersion or serverInfo; every tool gets 404 because the client joins HA_URL with paths that lack /api (states, config, services … |
| 2 | fail | 0 tools | 26 | 55.4 | 12 | 10/16 | 21.8 | 256k | 9 | llama.cpp 0.4 | answers but wraps initialize and tools/list in tool-result shape (content/structuredContent), no top-level serverInfo/protocolVersion/tools; replies to a notification with id "null". 14 tools behind the wrapper |

_Generated from the bake-off results on 2026-10-15._
