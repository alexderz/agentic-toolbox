# Nemotron 3 Nano 30B

**Status:** Dropped

| | |
| --- | --- |
| Family | Nemotron |
| Source | nvidia/Nemotron-3-Nano-30B |
| Architecture | Hybrid Mamba MoE |

## Summary

NVIDIA's small hybrid MoE.

## Verdict

83-91 tok/s but quits within minutes (2/5 twice).

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Nemotron 3 Nano 30B | llama.cpp 0.4 | Q4 | 416k | 9 | 90.7 |
| Nemotron 3 Nano 30B · llama.cpp 0.6, tool-calling sampling (temperature 0.6), thinking budget | llama.cpp 0.6 | Q4_K_M | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 0 | 83.3 | 2 | 0 | 0.0 | 128k | 10 | llama.cpp 0.4 | 3 subcommands |
| 1 | fail | 2/5 checks | 0 | 90.7 | 2 | 0 | 0.0 | 416k | 9 | llama.cpp 0.4 | 2 subcommands |

_Generated from the bake-off results on 2026-10-10._
