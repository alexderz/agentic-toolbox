# Gemma 4 31B

**Status:** Tested

| | |
| --- | --- |
| Family | Gemma 4 |
| Source | google/gemma-4-31b |
| Architecture | Dense, 31B |

## Summary

Google's dense Gemma 4.

## Verdict

Fast and finishes in minutes, but thin: 3 tools on test 2. Needs enable_thinking (its template defaults it off).

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Gemma 4 31B 4-bit · llama.cpp, all on GPU | llama.cpp 0.4 | Q4 | 72k | – | 53.4 |
| Gemma 4 31B 8-bit · llama.cpp, 72k context | llama.cpp 0.4 | Q8_0 | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 11 | 38.5 | 3 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 0 | 39.5 | 5 | 0 | 0.0 | 72k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 9 | 30.6 | 3 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 5 subcommands |
| 1 | pass | 5/5 checks | 10 | 53.4 | 2 | 0 | 0.0 | 72k | – | llama.cpp 0.4 | 4 subcommands |
| 2 | partial | 3 tools | 4 | 50.3 | 12 | 4/5 | 15.4 | 128k | – | llama.cpp 0.4 | no initialize method (-32601 Method not found: initialize), reply also lacks "jsonrpc"; tools/list and calls work without it but no client gets past the handshake |
| 2 | pass | 3 tools | 5 | 43.8 | 4 | 3/4 | 6.2 | 128k | – | llama.cpp 0.4 |  |
| 2 | pass | 3 tools | 7 | 47.0 | 5 | 1/1 | 2.0 | 72k | – | llama.cpp 0.4 |  |
| 2 | pass | 3 tools | 5 | 38.8 | 8 | 3/4 | 17.2 | 72k | – | llama.cpp 0.4 | no thinking (baseline); graded from a copy: a root-owned .git/config written after the case blocked the grader's SELinux relabel |

_Generated from the bake-off results on 2026-10-08._
