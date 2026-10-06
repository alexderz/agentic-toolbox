# Research log

Dated findings and decisions, newest first. Results also land in the model
cards; this log keeps the reasoning.

## 2026-10-06

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
