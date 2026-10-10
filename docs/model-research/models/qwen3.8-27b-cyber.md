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

Passed both tests on llama.cpp 0.4 without drafting, but slowly at long context (8-24 tok/s). With its own MTP heads on llama.cpp 0.6 (144k context) it decodes about 72 tok/s, but both MTP runs of test 2 got stuck: one looped on a mistyped call to an invented endpoint under long-horizon sampling, the other failed the same build 23 times on a bracket it could not find. Not recommended with MTP until that is understood. A test-3 run looped too (one call repeated 32 times). The author's own Q5_K_M, run with the recommended sampling and OpenCode's loop guard, passed test 1 5/5 (12 subcommands, 24 tests) but spent its last hour re-reading the same eleven lines of its test file 62 times, varied just enough to slip past the guard. Its test 2 failed: the server refuses any plain-http address but localhost, so it never started against the test endpoint, and it ran one sed-and-cargo command 100 times in a row until the 3-hour limit. The Q6_K and Q8_0 do not fit on a 24 GB card.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B Cyber (abliterated) · llama.cpp, all on GPU | llama.cpp 0.4 | IQ4_XS | 128k | – | 23.9 |
| Qwen3.8-27B Cyber (abliterated) IQ4_XS · llama.cpp 0.6, MTP drafts | llama.cpp 0.6 | IQ4_XS | – | – | 40.1 |
| Qwen3.8-27B Cyber (abliterated) Q5_K_M · llama.cpp 0.6, all on GPU at 80k, recommended sampling | llama.cpp 0.6 | Q5_K_M | – | – | 22.1 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 24 | 22.1 | 169 | 13 py | 16.0 | – | – | llama.cpp 0.6 | 12 subcommands |
| 1 | pass | 5/5 checks | 39 | 23.9 | 52 | 2 py | 2.1 | 128k | – | llama.cpp 0.4 | 5 subcommands |
| 2 | fail | 0 tools | – | 40.1 | 83 | 36/39 | 48.6 | – | – | llama.cpp 0.6 | Qwen3.8-27B Cyber + MTP n3 (llama.cpp 0.6, 144k), model default sampling: STOPPED after 83 min with no progress for 60 min: code frozen at 1,049 lines, 23 identical failed builds on an unclosed delimiter it could not locate, 579 reads of lib.rs. 40 tok/s over the run. The … |
| 2 | fail | 0 tools | 1 | 27.6 | 180 | 24/582 | 104.9 | – | – | llama.cpp 0.6 | checked by hand: the server refuses to start because its own URL check allows plain http:// only for <host> or localhost (src/ha.rs:82), so the given http://<host> fails; looped 100x on one sed+cargo command in its last hour; timed out at 3h |
| 2 | fail | 0 tools | – | 27.3 | 35 | 12/18 | 24.3 | – | – | llama.cpp 0.4 | not graded: OpenCode harness hang 54 min in; rerun queued |
| 2 | pass | 7 tools | 22 | 8.1 | 173 | 24/72 | 86.5 | – | – | llama.cpp 0.4 | [tests regraded 2026-10-07: 21/0 -> 22/1, grader now sums every cargo test target] hit 3h cap while still refining tests; server full pass; 203 steps no runaway; slow (8.1 tok/s over the run at 229k q8_0, dense 27B on llama.cpp) |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 0/14 | 3 | no | – | 19.4 | 105 | Not scored: stopped by hand at 105 min (operator saw the loop). A probe session repeated the identical ha_list_entities {"limit":30,"state":"unavailable"} call 32+ times while writing "Let me actually pass 300" (audit: 13 runs of identical calls, longest 52); no facts.json. … |

_Generated from the bake-off results on 2026-10-10._
