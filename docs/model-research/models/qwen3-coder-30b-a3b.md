# Qwen3-Coder-30B-A3B

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.6 |
| Source | Qwen/Qwen3-Coder-30B-A3B |
| Architecture | MoE, 30B / 3B active |

## Summary

Coder MoE.

## Verdict

Passed test 1 but wrote thin code with a failing test. Qwen3.6-35B-A3B was better on every measure.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3-Coder-30B-A3B · llama.cpp, experts in RAM | llama.cpp 0.4 | Q4 | 128k | 26 | 23.8 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 0 | 23.8 | 7 | 3 py | 8.2 | 128k | 26 | llama.cpp 0.4 | 7 subcommands |

_Generated from the bake-off results on 2026-10-07._
