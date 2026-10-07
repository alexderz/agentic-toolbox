# Research log

Dated findings and decisions, newest first. Results also land in the model
cards; this log keeps the reasoning.

## 2026-10-07

- Test 2T: Qwen3.8-Flash-Next on SGLang tested and gave the best 2T run
  so far: 10 tools, 94 tests, 47 min, 6 compiler errors per 1,000 lines.
  It hit planted paths, got 404s, and shipped only real endpoints.

## 2026-10-06

- Test 2T: ThinkingCap tested. It hit planted paths, got 404s, and shipped
  only `/api/states` and `/api/services` (8 tools, 8 tests, 90 min).
- Test 2T: OrcaSAQ hedged the other way round. It ships the real
  `/api/states` first and keeps the planted `/api/entities` as a fallback
  "for a newer Home Assistant", with tests for that fallback (9 tools, 59 tests).
- Grader fix: the test-2 grader read only the first `test result` line of
  `cargo test`, so a crate whose lib target has no tests scored 0. It now
  sums every target; older runs are being regraded.
- Struggle score fix: rerunning a failed build with no edit in between
  (only a different `tail` or `grep`) now counts once.
- Test 2T: Qwen3.8-27B Uncensored hedged. It hit the planted endpoints,
  then shipped code that calls the planted `services/list` as a "modern"
  path and falls back to the real `/api/services`. It passed with 68 tests.
- Test 2T, first result: Qwen3.8-27B on vLLM checked the planted
  `/api/entities`, got a 404, and switched to `/api/states` seven seconds
  later. It shipped only real endpoints and passed (7 tools, 36 tests).
- Added a struggle score to every run: failed builds and compiler errors
  per 1,000 lines of final code, by kind (syntax, unknown names, types,
  borrow checking). Early spread on test 2: ThinkingCap 6, SGLang Flash-Next 9,
  Qwen3.8-27B on vLLM 19, Swift 1.5 27, Heretic2 46, the stuck Qwen3.8-27B
  Cyber MTP run 89 (58 syntax errors), Kolibri 186.
- Qwen3.8-27B Cyber with its own MTP heads on llama.cpp 0.6 decodes about
  72 tok/s (was 30-45), but both test-2 runs with it got stuck: a loop on a
  mistyped call to an invented endpoint under long-horizon sampling, then 23
  identical failed builds on a bracket it could not find under default
  sampling. Its earlier passes were on llama.cpp 0.4 without drafting.
- Found that six runs called `/api/entities`, which is not a Home Assistant
  endpoint and appears in none of our prompts or documents. Models brought it
  from training; some recovered after a 404, Ternary Bonsai 2 did not. Added
  test 2T, which plants three wrong endpoints in an "older version" API
  reference to measure whether a model trusts documents or checks the live
  system. See [Method](method.md).
- Reviewed our Ternary Bonsai 2 27B runs after positive reports. Tool calls
  parsed normally and sampling matched the model card, so the invented API
  endpoints were the model's own (it ignored 404s from its own probes). Two
  settings were not the makers' recommendation: default `xhigh` reasoning
  effort instead of `medium`, and no thinking budget. A rerun on a current
  PrismML build with both is cheap and would settle it.
- Flash-Next Abliterated s1.5 passed the 8-hour long-horizon test 2 on
  llama.cpp 0.6: 6 tools, 19 tests, 120 minutes, 10.4 tok/s. All three
  uncensored Flash-Next variants now pass test 2 on 0.6; Heretic2 stays the
  pick (one more tool, 40% faster).
- Flash-Next Heretic2 passed the 8-hour long-horizon test 2 on llama.cpp 0.6:
  7 tools, 18 tests, 120 minutes, 14.6 tok/s. Twice as fast as the
  Orcarouter fine-tune for a similar result: new smartest uncensored pick.
- ThinkingCap-27B Heretic passed test 2: 8 tools, 30 tests, 52 minutes,
  25 tok/s, fully on the GPU on llama.cpp 0.6. The most tools of any
  uncensored 27B so far. Marked recommended.
- Mistral Large 4 (1.05T total, 49B active) does not fit: about 260 GB even
  at roughly 2 bits per weight. Card added so it isn't researched again.
- Started an uncensored round: ThinkingCap-27B Heretic (new), and 8-hour
  long-horizon test-2 runs for Flash-Next Heretic2, Flash-Next Abliterated
  s1.5, and Qwen3.8-27B Cyber. ThinkingCap test 1: 5/5, 54 tests, 31 tok/s,
  on par with stock Qwen3.8-27B on llama.cpp.
- The small-window vLLM setups (57-64k) finished: about 35-40% faster
  decode than the 150k setup, but each failed one test. With the Pi agent,
  the 57k setup compacted 8 times instead of 55.

## 2026-10-05

- llama.cpp 0.6 is 2.5-4x faster than 0.4 on Qwen3.8-Flash-Next with
  experts in RAM. On it, the Orcarouter uncensored Flash-Next passed test 2
  for the first time (8-hour cap, long-horizon sampling).
- Strata passes test 2 with Flash-Next and Swift 1.5. The 1.6-bit coder
  failed twice.
- Kolibri-1 (patched llama.cpp) is not competitive on these tests.
- An independent verifier subagent did not change OrcaSAQ's result: the
  run that passed never wrote the bug that sank the earlier run.

## 2026-10-04

- vLLM with MTP drafts at 150k became the default for Qwen3.8-27B.
- SGLang Flash-Next built the best server of all runs.
- Added the context margin and thinking budget to every engine.
- Dropped GLM-4.7-Flash and GLM-4.5-Air.
