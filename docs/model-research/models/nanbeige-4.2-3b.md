# Nanbeige 4.2 3B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | Nanbeige4.2-3B |
| Architecture | Dense, 3B |

## Summary

A 3B model.

## Verdict

Writes a lot of compiling code for its size, but failed the checks (2/5, 1/5).

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Nanbeige 4.2 3B | llama.cpp 0.4 | Q8 | 128k | – | 19.6 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 7 | 19.6 | 39 | 5 py | 4.8 | 128k | – | llama.cpp 0.4 | 7 subcommands |
| 1 | fail | 1/5 checks | 0 | 15.6 | 38 | 0 | 0.0 | 200k | – | llama.cpp 0.4 | 11 subcommands |

_Generated from the bake-off results on 2026-10-07._
