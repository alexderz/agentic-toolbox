# Jan Nano 128k

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | janhq/Jan-nano-128k |
| Architecture | Dense, 4B |

## Summary

Small long-context model.

## Verdict

41 tool calls and no files: it tried to install its own harness.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Jan Nano 128k | llama.cpp 0.4 | Q8 | 128k | – | 47.9 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 1/5 checks | – | 47.9 | 1 | 0 | – | 128k | – | llama.cpp 0.4 |  |

_Generated from the bake-off results on 2026-10-08._
