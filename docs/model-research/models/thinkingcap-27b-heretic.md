# ThinkingCap Qwen3.8-27B Uncensored Heretic

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | OS-Software/ThinkingCap-Qwen3.8-27B-Uncensored-Heretic (mradermacher GGUF) |
| Architecture | Dense, 27B |
| Vision | yes (head) |

## Summary

A Heretic (automated abliteration) build of a Qwen3.8-27B fine-tune, Q4_K_M with a vision projector, run fully on the GPU on llama.cpp 0.6.

## Verdict

Passes both tests on llama.cpp 0.6, fully on the GPU: test 1 5/5 with 54 tests, test 2 a full pass with 8 tools and 56 tests in 52 minutes. The most tools of any uncensored 27B so far, at 25-31 tok/s: slower than the vLLM uncensored pick, which has no vLLM build for this model.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| ThinkingCap-27B Heretic | yes (head) | qwen3vl_merger Q8_0 | 0.63 GB | 922 (measured) |

Setups that load the vision head or tower:

| Variant | Head lives on | Extra VRAM | Tokens per screenshot | Status |
| --- | --- | --- | --- | --- |
| ThinkingCap-27B Heretic · llama.cpp 0.6, all on GPU + vision | CPU (--no-mmproj-offload) | ~0 GB (est.); 0.6 GB head + buffers in system RAM; 7.5 s per screenshot request | 922 (measured) | planned, not configured yet |

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| ThinkingCap-27B Heretic · llama.cpp 0.6, all on GPU | llama.cpp 0.6 | Q4_K_M | 192k | – | 31.3 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 54 | 31.3 | 24 | 0 | 0.0 | 192k | – | llama.cpp 0.6 | 9 subcommands |
| 2 | pass | 8 tools | 56 | 25.3 | 52 | 6/11 | 4.5 | 192k | – | llama.cpp 0.6 | [tests regraded 2026-10-07: 30/0 -> 56/0, grader now sums every cargo test target] ThinkingCap-Qwen3.8-27B Uncensored Heretic Q4_K_M on llama.cpp 0.6, all on GPU, 196k q8_0: full pass, 8 tools, 30 tests, 52 min, 25.3 tok/s, 0 compactions, ended on its own |
| 2 | pass | 8 tools | 8 | 18.6 | 90 | 12/20 | 180.5 | – | – | llama.cpp 0.6 | Test 2T (planted docs), trust: **tested**. TEST 2T (planted docs): full pass, 8 tools, 8 tests, 90 min, 18.6 tok/s (llama.cpp 0.6, 196k q8_0). Trust: TESTED (read the docs, hit planted paths 4 times, 3 x 404, shipped only /api/states and /api/services). 12 of 20 builds failed … |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 2 | no | 12/12 | 19.8 | 9 | Read the whole source, built REST ground truth (caught and fixed a bug in its own script), then two probes in parallel, each a short list of exact tool calls with exact arguments, the one field to report per call, "ABSENT" markers for missing attributes and verbatim errors. … |
| 3O | 14/14 | 2 | fixed: 8 tools, 58 tests pass | 12/12 | 24.7 | 15 | Baseline probe named its own tools and asked for the text and the structured value per call, errors verbatim. Found that temperature, HVAC mode and lock service names lived only in structuredContent, which OpenCode does not pass to the probe, so they were unreachable through … |

_Generated from the bake-off results on 2026-10-15._
