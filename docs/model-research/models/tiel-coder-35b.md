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
| Tiel-Coder-35B 4-bit · llama.cpp 0.6, all on GPU, 262k, author's coding sampling (temperature 0.6) | llama.cpp 0.6 | UD-IQ4_XS | – | – | 99.0 |
| Tiel-Coder-35B Q4_K_XL · llama.cpp 0.6, 6 expert layers in RAM, 131k, temperature 0.6 | llama.cpp 0.6 | UD-Q4_K_XL | – | – | 78.6 |
| Tiel-Coder-35B 6-bit · llama.cpp, 20 expert layers in RAM | llama.cpp 0.4 | Q6_K_XL | 256k | 20 | 42.8 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 41 | 76.7 | 24 | 6 py | 4.6 | – | – | llama.cpp 0.6 | 10 subcommands |
| 1 | pass | 5/5 checks | 50 | 99.0 | 13 | 5 py | 4.3 | – | – | llama.cpp 0.6 | 15 subcommands |
| 1 | pass | 5/5 checks | 55 | 100.8 | 13 | 5 py | 2.8 | 256k | – | llama.cpp 0.4 | 10 subcommands |
| 1 | pass | 5/5 checks | 39 | 42.8 | 25 | 4 py | 3.4 | 256k | 20 | llama.cpp 0.4 | 8 subcommands |
| 2 | pass | 5 tools | 22 | 78.6 | 27 | 11/28 | 25.6 | – | – | llama.cpp 0.6 | retry batch 1, Tiel Coder 35B-A3B UD-Q4_K_XL at temperature 0.6, 6 expert layers in RAM, 131k: full pass, 5 tools, real endpoints only, 27 min, 184 turns, 78.6 tok/s, 21,598 MiB, 5 compactions, clean stop |
| 2 | pass | 6 tools | 17 | 40.8 | 72 | 19/84 | 32.8 | – | – | llama.cpp 0.6 | retry batch 1, Tiel Coder 35B-A3B UD-IQ4_XS at temperature 0.6 and min-p 0, all on GPU, 262k: full pass, 6 tools, real endpoints only, 72 min, 242 turns, 40.8 tok/s, 22,480 MiB, 1 compaction, clean stop. The first run of these weights (wb-tiel-coder-35b) returned no data from an … |
| 2 | partial | 9 tools | 37 | 82.0 | 32 | 16/23 | 215.8 | 256k | – | llama.cpp 0.4 | [tests regraded 2026-10-07: 8/0 -> 37/0, grader now sums every cargo test target] list_entities hits invented /api/entities; also invents /api/states/<id>/history and /api/config/device_registry; /api/states works |
| 2 | pass | 5 tools | 28 | 38.8 | 37 | 7/18 | 16.6 | 256k | 20 | llama.cpp 0.4 |  |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 1 | no | 12/12 | 22.4 | 23 | It sent one probe session with ten numbered calls giving exact arguments and the field it needed from each, asking for isError, the verbatim JSON text and a closing summary block; it built REST ground truth first, noticed that the probe's pasted state=off block was internally … |
| 3O | 14/14 | 4 | fixed: 5 tools, 28 tests pass | 12/12 | 38.4 | 28 | Its first probe found the list tools failing ("expected record, received array on structuredContent"); after confirming it by running the binary directly it wrapped the lists in objects and moved domain and entity_id filtering client-side, then a targeted probe showed the probe … |

_Generated from the bake-off results on 2026-10-11._
