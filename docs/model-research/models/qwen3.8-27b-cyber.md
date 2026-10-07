# Qwen3.8-27B Cyber (abliterated)

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | Qwen3.8-27B-Uncensored-Cyber IQ4_XS (imatrix from Q8, MTP heads included) |
| Architecture | Dense, 27B |

## Summary

An abliterated Qwen3.8-27B aimed at security work, IQ4_XS GGUF with the MTP draft layers kept.

## Verdict

Passed both tests on llama.cpp 0.4 without drafting, but slowly at long context (8-24 tok/s). With its own MTP heads on llama.cpp 0.6 (144k context) it decodes about 72 tok/s, but both MTP runs of test 2 got stuck: one looped on a mistyped call to an invented endpoint under long-horizon sampling, the other failed the same build 23 times on a bracket it could not find. Not recommended with MTP until that is understood.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Cyber (abliterated) · llama.cpp, all on GPU | llama.cpp 0.4 | IQ4_XS | 128k | – | 23.9 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 39 | 23.9 | 52 | 2 py | 2.1 | 128k | – | llama.cpp 0.4 | 5 subcommands |
| 2 | fail | 0 tools | – | 27.3 | 35 | 12/18 | 24.3 | – | – | llama.cpp 0.4 | not graded: OpenCode harness hang 54 min in; rerun queued |
| 2 | pass | 7 tools | 21 | 8.1 | 173 | 24/72 | 86.5 | – | – | llama.cpp 0.4 | hit 3h cap while still refining tests; server full pass; 203 steps no runaway; slow (8.1 tok/s over the run at 229k q8_0, dense 27B on llama.cpp) |

_Generated from the bake-off results on 2026-10-07._
