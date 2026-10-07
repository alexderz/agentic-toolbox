# Qwen3.6-35B-A3B

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.6 |
| Source | Qwen/Qwen3.6-35B-A3B |
| Architecture | MoE, 35B / 3B active |

## Summary

Small-active MoE, mostly on the GPU.

## Verdict

57 tok/s and good on test 1; its test-2 server listed no tools. Superseded by Qwen3.8.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.6-35B-A3B · llama.cpp, some experts in RAM | llama.cpp 0.4 | UD-Q4_K_M | 128k | 12 | 57.2 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 52 | 57.2 | 10 | 0 | 0.0 | 128k | 12 | llama.cpp 0.4 | 9 subcommands |
| 2 | fail | 0 tools | 26 | 55.4 | 12 | 10/16 | 21.8 | 256k | 9 | llama.cpp 0.4 | answers but wraps initialize and tools/list in tool-result shape (content/structuredContent), no top-level serverInfo/protocolVersion/tools; replies to a notification with id "null". 14 tools behind the wrapper |

_Generated from the bake-off results on 2026-10-07._
