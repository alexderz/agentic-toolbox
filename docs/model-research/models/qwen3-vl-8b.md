# Qwen3-VL-8B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | Qwen/Qwen3-VL-8B-Instruct |
| Architecture | Dense, 8B, vision |

## Summary

Small vision-language model. Also the text encoder for Qwen-Image 2.1.

## Verdict

0/5 on test 1: the code did not import.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3-VL-8B | llama.cpp 0.4 | Q4_K_M | 128k | – | 39.5 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 0/5 checks | – | 39.5 | 65 | 0 | 0.0 | 128k | – | llama.cpp 0.4 |  |

_Generated from the bake-off results on 2026-10-08._
