# GLM-4.5-Air

**Status:** Dropped

| | |
| --- | --- |
| Family | GLM |
| Source | zai-org/GLM-4.5-Air |
| Architecture | MoE, 106B / 12B active |

## Summary

Larger GLM MoE, experts in RAM.

## Verdict

3-6 tok/s and its test-2 server never answered initialize. MTP drafting gave nothing with experts in RAM.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| GLM-4.5-Air · llama.cpp, experts in RAM | llama.cpp 0.4 | Q4 | 128k | 43 | 6.0 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | – | 3.1 | 94 | 128k | 55 | llama.cpp 0.4 | 5 subcommands |
| 2 | partial | 3 tools | 0 | 6.0 | 102 | 128k | 43 | llama.cpp 0.4 | no initialize method (-32601 Unknown method: initialize); also sends result:null with error; 103 steps, no runaway, 6.0 tok/s |

_Generated from the bake-off results on 2026-10-06._
