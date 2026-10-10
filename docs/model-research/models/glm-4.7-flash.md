# GLM-4.7-Flash

**Status:** Dropped

| | |
| --- | --- |
| Family | GLM |
| Source | zai-org/GLM-4.7-Flash |
| Architecture | MoE |

## Summary

GLM's fast MoE.

## Verdict

Inconsistent on test 1; its test-2 server rejected numeric JSON-RPC ids.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| GLM-4.7-Flash | llama.cpp 0.4 | Q4 | 198k | – | 34.9 |
| GLM-4.7-Flash · llama.cpp 0.6, coding sampling (temperature 0.7), thinking kept between steps | llama.cpp 0.6 | Q4_K_M | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 34 | 61.7 | 8 | 12 py | 11.2 | 128k | – | llama.cpp 0.4 | 12 subcommands |
| 1 | pass | 5/5 checks | 45 | 34.9 | 14 | 0 | 0.0 | 198k | – | llama.cpp 0.4 | 8 subcommands |
| 2 | fail | 0 tools | 0 | 40.8 | 19 | 42/45 | 389.8 | 198k | – | llama.cpp 0.4 | rejects numeric JSON-RPC ids ("invalid type: integer 1, expected str"); spec allows string or number, so no client gets past initialize; 290 steps, no runaway |

_Generated from the bake-off results on 2026-10-10._
