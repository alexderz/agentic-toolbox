# Qwen3.8-27B Uncensored (Aggressive, AWQ)

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | philbert440/Qwen3.8-27B-Uncensored-Aggressive-W4A16-AWQ |
| Architecture | Dense, 27B |

## Summary

An uncensored fine-tune of Qwen3.8-27B, AWQ 4-bit, run on vLLM with MTP drafts at 150k context.

## Verdict

The steadiest fast uncensored model: two test-2 full passes and 5/5 on test 1 at 61-68 tok/s. It needs the thinking budget: without it, its first test-1 run spent the whole reply on one think.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Uncensored · vLLM, MTP drafts, 150k context | vLLM (HyperQwen) | AWQ W4A16 | 146k | – | 67.8 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 1/5 checks | – | 89.3 | 7 | 1 py | – | 146k | – | vLLM (HyperQwen) |  |
| 1 | pass | 5/5 checks | 158 | 67.8 | 59 | 2 py | 0.7 | 146k | – | vLLM (HyperQwen) | 11 subcommands |
| 1 | pass | 5/5 checks | 137 | 64.2 | 44 | 2 py | 0.8 | 146k | – | vLLM (HyperQwen) | 9 subcommands |
| 2 | pass | 7 tools | 41 | 60.8 | 60 | 10/30 | 17.1 | 146k | – | vLLM (HyperQwen) | no budget (baseline for -tb/-pp); 138k reasoning tokens over 192 steps, no runaway |
| 2 | pass | 5 tools | 0 | 63.7 | 47 | 16/26 | 17.8 | 146k | – | vLLM (HyperQwen) | 24k thinking budget: no runaway (max 15.8k reasoning/step, 133 steps); full pass; ended on ContextOverflowError at 118k+32k>150k (started before the -10%% margin fix); 64 tok/s, 47 min |
| 2 | pass | 6 tools | 45 | 61.1 | 80 | 28/41 | 88.2 | 146k | – | vLLM (HyperQwen) | 24k budget + presence_penalty 1.5 + -10%% context margin: full pass, no runaway (max 21.2k reasoning/step, 255 steps), no overflow (peak 112k of 135k), ran to completion; 61 tok/s, 80 min |

_Generated from the bake-off results on 2026-10-06._
