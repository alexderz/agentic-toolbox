# Orcarouter Flash-Next Uncensored

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | orcarouter/Qwen3.8-Flash-Next-Uncensored-GGUF |
| Architecture | MoE, 125B total / 6B active |

## Summary

An uncensored fine-tune of Flash-Next, IQ4_XS, with a separate MTP draft file. Runs on llama.cpp with experts in RAM.

## Verdict

Test-2 full pass on llama.cpp 0.6 with long-horizon settings (8 tools, 54 tests, 191 min), but slow: 7.6 tok/s over the run. Smartest uncensored model on the corrected test counts (2026-10-07 regrade): more tools and tests and half the compiler errors per 1,000 lines of Heretic2. Heretic2 is twice as fast. On llama.cpp 0.4 it ran out of time.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Orcarouter Flash-Next Uncensored · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4_XS | 128k | 42 | 8.8 |
| Orcarouter Flash-Next Uncensored · llama.cpp 0.6, experts in RAM, 262k context | llama.cpp 0.6 | IQ4_XS | 256k | 40 | 7.6 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 54 | 8.8 | 104 | 0 | 0.0 | 128k | 42 | llama.cpp 0.4 | 13 subcommands |
| 2 | pass | 8 tools | 54 | 7.6 | 191 | 9/22 | 13.2 | 256k | 40 | llama.cpp 0.6 | [tests regraded 2026-10-07: 13/0 -> 54/0, grader now sums every cargo test target] orcarouter Flash-Next uncensored on llama.cpp v0.6.0 (lcpp6, -ncmoe 40, 262k, -fit off), long-horizon settings (temp 1.0/top-p 0.95/top-k 20, 26k budget, 8 h cap): FULL PASS, 191 min, 7.6 tok/s … |
| 2 | fail | 0 tools | – | 7.4 | 155 | 0 | 0.0 | – | – | llama.cpp 0.4 | does not build (lib path in Cargo.toml not written yet); hit 3h cap mid-project; no runaway, 7.4 tok/s |

_Generated from the bake-off results on 2026-10-07._
