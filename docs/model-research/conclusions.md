# Conclusions

This page gives the current picks and the rules that decide them. It
changes as results come in; for dated changes, see the
[Research log](log.md).

"Competent" means the model passed test 2: it built an MCP server that a
real client could connect to and call. "Smartest" weighs how much working
server and how many passing tests it produced. For how the tests work, see
[Method](method.md).

## Picks

| Role | Model and setup | Why |
| --- | --- | --- |
| Smartest | [Qwen3.8-Flash-Next](models/qwen3.8-flash-next.md) on SGLang, EXL3 3-bit, GPU expert cache | The best test-2 server of all runs: 12 tools, 115 tests, 124 minutes at 36 tok/s. One session at a time. |
| Fastest competent | [Qwen3.8-27B](models/qwen3.8-27b.md) on vLLM, MTP drafts, 150k context | Full passes on both tests at about 70 tok/s; test 2 in 39 minutes. The default agent model. |
| Smartest, uncensored | [Flash-Next Heretic2](models/flash-next-heretic2.md) on llama.cpp 0.6, experts in RAM, 262k context | Test-2 full pass with long-horizon settings: 7 tools, 18 tests in 120 minutes at 14.6 tok/s. The [Orcarouter fine-tune](models/orcarouter-flash-next-uncensored.md) reached a similar result (8 tools, 13 tests) at half the speed. |
| Fastest competent, uncensored | [Qwen3.8-27B Uncensored](models/qwen3.8-27b-uncensored-aggressive.md) on vLLM, MTP drafts, 150k context | Two test-2 full passes and 5/5 on test 1 at 61-68 tok/s. Run it with the thinking budget. |

[OrcaSAQ-2-Cyber-27B](models/orcasaq-2-cyber-27b.md) is faster than the
uncensored pick (77-86 tok/s with a draft model) but less consistent: one of
its two test-2 runs shipped a broken HTTP client.
[ThinkingCap-27B Heretic](models/thinkingcap-27b-heretic.md) built the most
complete uncensored 27B server so far (8 tools, 30 tests, 52 minutes) at
25-31 tok/s on llama.cpp: pick it when completeness matters more than speed.

## By family

| Family | Smartest | Fastest competent | Notes |
| --- | --- | --- | --- |
| Qwen3.8 27B | vLLM, MTP drafts, 150k | the same | llama.cpp on the same weights scored the same and ran 2-4x slower. |
| Qwen3.8 Flash-Next | SGLang, EXL3 3-bit | Swift 1.5 (pruned) on Strata | Uncensored: Heretic2 on llama.cpp 0.6. Only llama.cpp runs the uncensored variants; 0.6 is 2.5-4x faster than 0.4 on them. |
| Tiel Coder 35B | Cyber-Tiel-Coder 6-bit | Tiel-Coder 4-bit, all on GPU (101 tok/s on test 1) | The 4-bit test-2 server called an invented endpoint; the 6-bit builds passed. |
| Gemma 4 | 31B | 26B-A4B on vLLM | Fast but thin: 3 tools on test 2. |
| Qwen3.6 | 27B | none passed test 2 | Superseded by Qwen3.8. |
| Kolibri | Kolibri-1 | none passed test 2 | Thin on both tests. |
| GLM, Nemotron, others | none | none | See their cards. |

## Rules we learned

1. **Speed is set by how much of the model sits in VRAM.** Models that fit
   the GPU ran at 25-150 tok/s; models with experts in system RAM ran at
   3-25 tok/s, whatever their size. Pick a tier first, then a model.
2. **The engine matters as much as the model.** The same weights ran 2-5x
   faster on a better-suited engine. See [Engines](engines.md).
3. **Offloaded experts must load eagerly** (`-lm none`), or the first
   request stalls on page faults.
4. **Speculative decoding pays only when the model is GPU-resident.**
5. **Give the agent a context margin and a thinking budget.** Without them,
   runs die on context overflow or on a single think that uses the whole
   reply.
6. **Small context windows cost more than they save.** At 57-64k the agent
   compacts constantly; 150k with OpenCode is the working minimum. The Pi
   agent copes better with a small window.
7. **Runs vary a lot.** The same model and settings can pass and fail on
   different runs. Treat one result as a sample.
