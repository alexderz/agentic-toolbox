# Ternary Bonsai 2 27B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | prism-ml/Ternary-Bonsai-2-27B-gguf |
| Architecture | Dense, 27B, ternary weights |

## Summary

A 27B model with ternary weights.

## Verdict

Fast (41-47 tok/s) but invents APIs: 11 of 14 API paths in one run did not exist. Abliterated variants exist; not tested for the same reason.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Bonsai 2 27B (ternary) | llama.cpp 0.4 | ternary | 128k | – | 40.8 |
| Bonsai 2 27B PQ2 | llama.cpp 0.4 | PQ2 | 248k | – | 47.5 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 68 | 40.8 | 42 | 128k | – | llama.cpp 0.4 | 20 subcommands |
| 1 | fail | 2/5 checks | 46 | 46.5 | 57 | 128k | – | llama.cpp 0.4 | 14 subcommands |
| 1 | partial | 4/5 checks | 75 | 47.5 | 36 | 248k | – | llama.cpp 0.4 | 17 subcommands |

_Generated from the bake-off results on 2026-10-06._
