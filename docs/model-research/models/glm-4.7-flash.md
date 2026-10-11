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

Inconsistent on test 1; its test-2 server rejected numeric JSON-RPC ids. Retried 2026-10-11 on llama.cpp 0.6 with the maker's coding sampling (temperature 0.7, top-p 1.0): test 1 passed 5/5, and the test-2 server took numeric ids, listed 7 tools and returned real data, but never answered `initialize` (it expects snake_case keys and drops the request without a reply), so a standard client still cannot connect.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| GLM-4.7-Flash | llama.cpp 0.4 | Q4 | 198k | – | 34.9 |
| GLM-4.7-Flash · llama.cpp 0.6, coding sampling (temperature 0.7), thinking kept between steps | llama.cpp 0.6 | Q4_K_M | – | – | 44.1 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 34 | 61.7 | 8 | 12 py | 11.2 | 128k | – | llama.cpp 0.4 | 12 subcommands |
| 1 | pass | 5/5 checks | 45 | 34.9 | 14 | 0 | 0.0 | 198k | – | llama.cpp 0.4 | 8 subcommands |
| 1 | pass | 5/5 checks | 23 | 27.8 | 28 | 17 py | 16.6 | – | – | llama.cpp 0.6 | 9 subcommands |
| 2 | fail | 0 tools | 0 | 40.8 | 19 | 42/45 | 389.8 | 198k | – | llama.cpp 0.4 | rejects numeric JSON-RPC ids ("invalid type: integer 1, expected str"); spec allows string or number, so no client gets past initialize; 290 steps, no runaway |
| 2 | partial | 7 tools | 2 | 44.1 | 15 | 10/16 | 49.0 | – | – | llama.cpp 0.6 | checked by hand: retry batch 1, GLM-4.7-Flash at Z.ai's coding sampling (temperature 0.7, top-p 1.0). initialize is never answered: its params struct wants snake_case keys (protocol_version, client_info, client_capabilities: src/main.rs:83-87) and a failed parse is logged and … |

_Generated from the bake-off results on 2026-10-11._
