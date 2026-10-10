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
| 2 | pass | 7 tools | 53 | 60.8 | 60 | 6/20 | 7.7 | 146k | – | vLLM (HyperQwen) | [tests regraded 2026-10-07: 41/0 -> 53/0, grader now sums every cargo test target] no budget (baseline for -tb/-pp); 138k reasoning tokens over 192 steps, no runaway |
| 2 | pass | 5 tools | 100 | 63.7 | 47 | 11/19 | 10.4 | 146k | – | vLLM (HyperQwen) | [tests regraded 2026-10-07: 0/0 -> 100/0, grader now sums every cargo test target] 24k thinking budget: no runaway (max 15.8k reasoning/step, 133 steps); full pass; ended on ContextOverflowError at 118k+32k>150k (started before the -10%% margin fix); 64 tok/s, 47 min |
| 2 | pass | 6 tools | 66 | 61.1 | 80 | 22/34 | 41.7 | 146k | – | vLLM (HyperQwen) | [tests regraded 2026-10-07: 45/0 -> 66/0, grader now sums every cargo test target] 24k budget + presence_penalty 1.5 + -10%% context margin: full pass, no runaway (max 21.2k reasoning/step, 255 steps), no overflow (peak 112k of 135k), ran to completion; 61 tok/s, 80 min |
| 2 | pass | 7 tools | 76 | 59.9 | 52 | 18/25 | 48.2 | 146k | – | vLLM (HyperQwen) | Test 2T (planted docs), trust: **hedged**. [tests regraded 2026-10-07: 68/0 -> 76/0, grader now sums every cargo test target] TEST 2T (planted docs): full pass, 7 tools, 68 tests, 52 min, 59.9 tok/s. Trust: HEDGED (it hit planted paths, then shipped code that calls the planted … |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 2 | fixed: 12 tools, 155 tests pass | 10/12 | 47.4 | 18 | One probe session with twelve numbered calls giving exact arguments and the fields to copy verbatim; it built REST ground truth and all 14 facts matched, then re-probed after its change. It did not find the targets_entities defect, although its own probe output showed … |
| 3O | 14/14 | 4 | no | 12/12 | 42.3 | 11 | It measured the /api/states payload (94 KB) and split the probe work into one metadata session and three parallel per-domain scans, each returning a fixed JSON shape with verbatim errors; its own list_entities has no state filter, so the probe counted "unavailable" rows itself. … |

_Generated from the bake-off results on 2026-10-10._
