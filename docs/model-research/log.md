# Research log

Dated findings and decisions, newest first. Results also land in the model
cards; this log keeps the reasoning.

## 2026-10-13

- MiniCPM-V 4.7 (OpenBMB, Apache-2.0), released 2026-10-12: a 1.55B dense vision-language model and a 35.3B MoE (8 of 256 experts). Official GGUF is public and not gated. The 1B Q8_0 file is 1.01 GiB plus a 1.03 GiB projector and fits a 24 GB card. The 35B Q4_K_M file is 19.71 GiB plus a 1.04 GiB projector (20.8 GiB), so only a short context fits on the card; Q8_0 is 34.37 GiB and fits with experts in RAM.
- Not downloaded. The language files are qwen35 and qwen35moe, which llama.cpp 0.6 already loads, but vision projector type minicpmv4_7 was added on 2026-10-10 (PR 29416), after the v0.6.0 image (build 11429, 2026-10-05). Current llama.cpp master has it; today's release tag is b11588.

## 2026-10-12

- Looked at four models that fit a 24 GB card but need an engine we do not run. None downloaded.
  [PersonaPlex-7B](models/personaplex-7b.md) is a gated 16 GB full-duplex speech model; its 4-bit GGUF loads only in moshi.cpp.
  [BitNet b1.58 2B4T](models/bitnet-b1.58-2b-4t.md) is a 1.1 GB ternary chat model for bitnet.cpp.
  [BitNet embeddings](models/bitnet-embeddings.md) (0.6B and 270M) use those same kernels.
  [VibeVoice-ASR-BitNet](models/vibevoice-asr-bitnet.md) is a 1.6 GB speech recognizer for VibeASR.cpp, aimed at AVX2 CPUs.
- Rechecked the abliterated DeepSeek V4.1 Flash. Still nothing near 135 GB; the smallest build seen today is about 190 GB.
- A third-party GLM-5.3-Flash IQ2_XXS is 81 GB. Not pulled: the author points at an unmerged llama.cpp change, and the Maya quant of the same model is already tested.

## 2026-10-11

- Looked at three new items, none downloaded. [Decision 3.0](models/decision-3.0.md) loads through its own
  Transformers code and has no requants yet. The [DFlash2 draft for ExLlamaV3](models/qwen3.8-27b-dflash2-exl3.md)
  is a serving path for Qwen3.8-27B that needs an ExLlamaV3 server. [Qwen 4](models/qwen4.md) is a rumour without
  weights.
- Retry wave: nine models that had failed earlier, rerun on llama.cpp 0.6 with researched sampling and less compressed weights.
  [Tiel Coder 35B](models/tiel-coder-35b.md) turned out to be a sampling problem: at temperature 0.6 the 4-bit file
  that had called an invented endpoint passes both tests, and the Q4_K_XL build passes test 2 in 27 minutes at
  78.6 tok/s with real endpoints only. [Devstral Small 2](models/devstral-small-2-24b.md),
  [Qwen3.6-35B-A3B](models/qwen3.6-35b-a3b.md) and [GLM-4.7-Flash](models/glm-4.7-flash.md) now pass test 1 and
  still fail test 2 on the MCP handshake: all three wrote `initialize` with snake_case fields. None of them sent a
  request to Home Assistant during its run, but that alone does not explain it: three passing runs sent none
  either. Nemotron 3 Nano, Nemotron 3.5 Lightning, Nanbeige 4.2, Qwen3-VL 8B and MiMo v2.6 did not pass test 1.
- Strata 0.1.42 runs [Qwen3.8-Flash-Next](models/qwen3.8-flash-next.md) through both tests (test 1 5/5 twice; test
  2 a full pass with 9 tools and 72 tests in 98 minutes), but slower over the run than 0.1.39 (19.2 against 24.4
  tok/s). A settings probe, repeated with a warm-up and in both orders, found one setting that matters: going back
  to the older PCIe share about doubled decode speed on long answers (95 against 48 tok/s) and read large prompts
  1.7 times faster. The first probe could not rank the settings because its opening run was a cold start: the same
  prompt was read at 44 tok/s cold and 1,269 warm.
- A newer SGLang build for Flash-Next handles several sessions at once (11 of 11 checks in a multi-session probe;
  the older build crashed under several) and passed test 1 5/5 at 25.3 tok/s. Its test 2 is not run yet.
- Test 3 now also gives the task as a file in the work folder, because models that compacted their conversation
  lost the required answer layout, and the grader credits a right value written in another layout. Four earlier
  runs gained; the cards show both counts.
- Harness finding: the coding agent's file search tools (glob and grep) have failed inside our test sandbox since
  the first runs, because the agent image lacks ripgrep. 57 of 181 runs asked for them and got an error, and the
  models fell back to shell commands. Every model had the same handicap, so the rankings hold, but turn counts are
  inflated. Not fixed yet.
- The test queue is finished for now.

## 2026-10-08

- New [story test](story-test/README.md): each model writes a Neuromancer-style short story from a fixed
  brief, then edits its own draft. OrcaSAQ-2 Cyber 27B, Qwen3.8 27B and the Orcarouter Flash-Next fine-tune ran it.
  Orcarouter wrote the best story (the longest and the best fight, at about 15-19 tok/s); none reached 5,000 words, and
  none really revised its own draft (they inserted passages or, in Qwen's case, reprinted the draft). Thinking needs a
  cap: uncapped, Qwen spent all 20,000 tokens planning.
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

## 2026-10-09

- Step 5 Preview (StepFun, about 600B total / 27B active): does not fit. Official weights are announced for about 15 October; the earlier Hugging Face copies are third-party uploads and were not downloaded.
- Unsloth decision-model training noted as a way to build a local classifier; not a model, nothing downloaded.

## 2026-10-10

- Qwen-Image-2.1-Turbo (the 8-step checkpoint of Qwen-Image 2.1): downloaded, official folder plus a Q8 GGUF of the transformer. Same architecture as Qwen-Image 2.1, so the same image setups apply. Not run yet.
- Mirai S (Qwen3.8-27B compressed to about 8 GB with a speculator): needs its own engine (Mirai's vLLM build or a llama.cpp fork). Not downloaded.
- Samsung LittleBit (sub-1-bit compression): code only, no checkpoints, non-commercial licence. On the watch list.
- TensorFold "Living Weights" (a served model that writes learned facts into its own weights) and Helix Foundry (a local data workspace): tools, not models. Nothing to test.
