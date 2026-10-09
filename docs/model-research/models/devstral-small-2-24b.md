# Devstral Small 2 24B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | mistralai/Devstral-Small-2 |
| Architecture | Dense, 24B |

## Summary

Mistral's coding model.

## Verdict

Inconsistent: 2/5, then 5/5 with a failing test.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Devstral Small 2 24B | llama.cpp 0.4 | Q4 | 200k | – | 33.1 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 38 | 25.6 | 15 | 1 py | 0.9 | 100k | – | llama.cpp 0.4 | 6 subcommands |
| 1 | pass | 5/5 checks | 0 | 33.1 | 11 | 2 py | 3.0 | 200k | – | llama.cpp 0.4 | 7 subcommands |

_Generated from the bake-off results on 2026-10-09._
