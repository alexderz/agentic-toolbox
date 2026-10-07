# Kolibri-1

**Status:** Dropped

| | |
| --- | --- |
| Family | Kolibri |
| Source | Aleph-Alpha/Kolibri-1 (Hob-forge GGUF + llama.cpp patch) |
| Architecture | MoE, 78B / 3.5B active, EN/DE |

## Summary

Aleph Alpha's bilingual MoE. Needs a patched llama.cpp (we built v0.6.0 plus the patch). Q8_0 with 39 of 50 layers' experts in RAM.

## Verdict

Thin on both tests at about 19 tok/s; its test-2 server answered only server/discover, not initialize. Not competitive here.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Kolibri-1 8-bit · llama.cpp 0.6 + patch, experts in RAM | llama.cpp 0.6 + Kolibri patch | Q8_0 | 256k | 39 | 19.6 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 0 | 18.9 | 29 | 0 | 0.0 | 256k | 39 | llama.cpp 0.6 + Kolibri patch | 4 subcommands |
| 2 | partial | 3 tools | 5 | 19.6 | 36 | 7/15 | 114.6 | 256k | 39 | llama.cpp 0.6 + Kolibri patch | Kolibri-1 Q8_0 (llama.cpp v0.6.0 + kolibri1 patch, -ncmoe 39, 262k): PARTIAL, verified by hand: implements only server/discover, answers the required legacy initialize with -32601 Method not found; 3 tools, a real tool call works, 5 tests; thin: 253 lines in one file, 36 min … |

_Generated from the bake-off results on 2026-10-06._
