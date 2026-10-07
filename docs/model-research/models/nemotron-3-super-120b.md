# Nemotron 3 Super 120B

**Status:** Dropped

| | |
| --- | --- |
| Family | Nemotron |
| Source | nvidia/Nemotron-3-Super-120B |
| Architecture | Hybrid MoE, 120B |

## Summary

Large hybrid MoE, 77 expert layers in RAM.

## Verdict

Passed test 1 with no tests written, at 8.5 tok/s. Not taken further.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Nemotron 3 Super 120B · llama.cpp, experts in RAM | llama.cpp 0.4 | UD-Q4_K_M | 128k | 77 | 8.5 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 0 | 8.5 | 46 | 0 | 0.0 | 128k | 77 | llama.cpp 0.4 | 5 subcommands |

_Generated from the bake-off results on 2026-10-07._
