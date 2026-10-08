# Research log

Dated findings and decisions, newest first. Results also land in the model
cards; this log keeps the reasoning.

## 2026-10-08

- Huihui's abliterated GLM-5.3-Flash at 1 bit (UD-IQ1_S) failed both tests on
  Maya: it fell into repetition ("-0-0-0..." until the token limit) and never
  wrote a working program. Maya-S at 2 bits on the same engine passed both, so
  1-bit quants of this model are not usable for agent work. The Orcarouter
  uncensored Q2_K is next.
- GLM-5.3-Flash now runs on titan through Project Maya (a Strata-derived
  engine). Out of the box it decoded about 4 tok/s: the RAM tier only held
  experts that were not already in VRAM, so every VRAM eviction meant a
  re-read over NFS. Three small patches (all experts eligible for RAM, keep
  evicted experts in RAM, parse GLM's own tool-call format) plus a local SSD
  copy of the weights brought it to about 17-19 tok/s with no disk reads in
  steady state. Test 1 then passed 5/5 with 44 tests in 71 minutes.
- GLM-5.3-Flash on Maya also passed test 2 (7 tools, 66 tests) but needed 322
  of its 360 minutes at about 14 tok/s over the run: the slowest model to pass
  both tests. Next up is the Huihui abliterated build (UD-IQ1_S) on the same
  engine; a second GPU, which turns on Maya's MTP drafting, is what would make
  GLM-5.3-Flash practical here.
- Grader fix: test 1's read check could not walk into an argparse command
  group whose subcommands hide behind a custom label (`ACTION ...`) or carry
  aliases (`list (ls)`). Regrading the 14 runs that had no read credit moved
  Devstral Small 2 from 2/5 to 5/5; no other run changed.

## 2026-10-07

- Test 3 is in: the model gets an MCP server's source and a probe subagent
  whose only tools are that server's, must get 14 facts through the probe,
  check them against the REST API, and fix the server if it is wrong (3G: a
  known-good server; 3O: the model's own from test 2). Eight runs across
  Qwen3.8-27B (vLLM), Flash-Next (Strata with two batch slots), Orcarouter
  Flash-Next and ThinkingCap Heretic: every run got all 14 facts and scored
  12/12 on the transcript rubric, so the test does not yet separate these
  models. Speed does (9 to 46 minutes), and so does how deep each one looked.
- Every 3O run found and fixed a real defect in its own server: a missing
  services tool, "unknown" counted as "unavailable", arrays in
  `structuredContent` (the MCP schema types it as an object, and strict
  clients reject the whole reply), and facts that only lived in
  `structuredContent`, which OpenCode does not pass to the model.
- One 3G run (Flash-Next) found a defect in the known-good server too: it
  read only `target.entity_id`, while current Home Assistant publishes
  `target.entity`.
- Strata needs `"parallel": 2` with `--batch-mtp` for multi-agent work;
  SGLang's EXL3 build serves one session at a time and was not used.

- The bake-off moved to a new host. Its first run there, Qwen3.8-27B on vLLM,
  passed test 1 (5/5, 123 tests, 22 subcommands, 64 tok/s). About 6 of the 22
  subcommands call Home Assistant endpoints that do not exist, and test 1's
  checks do not catch that, so invented API surface is not only a Bonsai
  problem. A test 1 check that runs every subcommand and counts 404s is on
  the list.
- EmbeddingGemma 2 (Google, 740M, Apache 2.0) fits easily, but its
  `gemma-embedding2` architecture landed in llama.cpp the day after our
  v0.6.0 build (PR 30054) and in vLLM after 0.31.0. Not downloaded; revisit
  with the next llama.cpp release. New status label: "Needs an engine
  update".
- Bonsai 2 27B rerun with the makers' agent settings (current PrismML
  build, reasoning effort `medium`, 24k thinking budget): test 1 went from
  2/5 to 5/5 with 94 tests, but 7 of its 11 commands still call Home
  Assistant endpoints that do not exist. The settings fixed reliability,
  not the invented API. Test 2 was a partial pass: it builds, lists 3
  tools and passes 32 tests, but its `tools/call` expects an invented
  `toolName` field instead of the spec's `name`, so no standard client can
  call a tool, and two of its tools call the nonexistent `/api/entities`.
- Test 2T, last result: Gemma 4 26B-A4B on vLLM trusted the planted docs.
  Its code calls `/api/entities`; it never called the API, quit after three
  minutes and left code that does not build.
- Regraded every test-2 run after the grader fix: 21 of 46 test counts were
  too low (Flash-Next on SGLang 115 -> 155, Orcarouter 13 -> 54, Heretic2
  18 -> 33). With the corrected counts the Orcarouter fine-tune is the
  smartest uncensored setup; Heretic2 stays as the faster one.
- Strata did not start for test 2T (the engine exits while locking about
  40 GB of host RAM). Its 2T result is still open.
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
