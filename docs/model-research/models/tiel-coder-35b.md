# Tiel-Coder-35B-A3B

**Status:** Tested

| | |
| --- | --- |
| Family | Tiel Coder 35B |
| Source | Tiel-Coder-35B-A3B (GGUF) |
| Architecture | MoE, 35B / 3B active |

## Summary

Small-active coder MoE. At IQ4_XS it fits entirely on the GPU at 262k context; the 6-bit build keeps 20 expert layers in RAM.

## Verdict

The fastest model that writes working test-1 code (101 tok/s). Its 4-bit test-2 server called an invented endpoint; the 6-bit build passed test 2.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Tiel-Coder-35B 4-bit · llama.cpp, all on GPU, 262k context | llama.cpp 0.4 | UD-IQ4_XS | 256k | – | 100.8 |
| Tiel-Coder-35B 6-bit · llama.cpp, 20 expert layers in RAM | llama.cpp 0.4 | Q6_K_XL | 256k | 20 | 42.8 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 55 | 100.8 | 13 | 5 py | 2.8 | 256k | – | llama.cpp 0.4 | 10 subcommands |
| 1 | pass | 5/5 checks | 39 | 42.8 | 25 | 4 py | 3.4 | 256k | 20 | llama.cpp 0.4 | 8 subcommands |
| 2 | partial | 9 tools | 8 | 82.0 | 32 | 21/30 | 405.3 | 256k | – | llama.cpp 0.4 | list_entities hits invented /api/entities; also invents /api/states/<id>/history and /api/config/device_registry; /api/states works |
| 2 | pass | 5 tools | 28 | 38.8 | 37 | 10/21 | 29.7 | 256k | 20 | llama.cpp 0.4 |  |

_Generated from the bake-off results on 2026-10-06._
