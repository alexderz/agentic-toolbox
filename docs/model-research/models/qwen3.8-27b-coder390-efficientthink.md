# Qwen3.8-27B Coder390 EfficientThink

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | nerkyor/Qwen3.8-27B-Coder390-EfficientThink-Opus5.5-GPT6Astra-Grok4.7-DSV4Pro-K3-SFT-RLOO-MTP-DFlash2 (the author's Q4 GGUF with Q8 MTP heads) |
| Architecture | Dense, 27B |

## Summary

An uncensored coding fine-tune of Qwen3.8-27B trained to think briefly. Run on llama.cpp 0.6 with its own MTP draft heads, fully on the GPU at 80k context with two slots.

## Verdict

Passed both tests on the first try and quickly: test 1 scored 5/5 with 59 passing tests in 27 minutes, and test 2 was a full pass with 33 passing tests in 31 minutes, both at 50 tok/s. Neither run repeated a tool call, unlike the Cyber tune of the same base, which looped on every quant. The cost of fitting the 19.8 GB file on a 24 GB card is the 80k context: the agent compacted its conversation 6 and 8 times. The four default slots do not fit, because each MTP slot keeps about 750 MiB of draft state, so it runs with two slots that share one context.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Coder390 EfficientThink (uncensored) Q4 with Q8 MTP heads · llama.cpp 0.6, MTP drafts, all on GPU at 80k, two slots | llama.cpp 0.6 | Q4 (Lynn style) + Q8 MTP | – | – | 50.2 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 59 | 50.2 | 27 | 0 | 0.0 | – | – | llama.cpp 0.6 | 9 subcommands |
| 2 | pass | 3 tools | 33 | 50.0 | 31 | 7/11 | 154.0 | – | – | llama.cpp 0.6 | full pass; no repeated tool calls; 8 compactions in the 81,920-token context |

_Generated from the bake-off results on 2026-10-10._
