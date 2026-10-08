# Qwen3.6-27B

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.6 |
| Source | Qwen/Qwen3.6-27B |
| Architecture | Dense, 27B |

## Summary

The previous dense Qwen.

## Verdict

Good on test 1; on test 2 its server had no initialize method. Superseded by Qwen3.8-27B.

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

_Generated from the bake-off results on 2026-10-08._
