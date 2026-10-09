# GLM-5.3-Flash

**Status:** Tested

| | |
| --- | --- |
| Family | GLM |
| Source | zai-org/GLM-5.3-Flash |
| Architecture | MoE, 320B / 18B active, multimodal |

## Summary

GLM's hybrid linear/sparse-attention MoE. Runs on Project Maya, a Strata-derived engine that tiers the 12,096 experts across VRAM, pinned RAM and disk.

## Verdict

On Maya (Maya-S-v2 IQ2_XXS, 97 GB, with three of our patches: all experts eligible for the RAM tier, VRAM victims kept in RAM, and GLM tool-call parsing) it decodes about 17-19 tok/s once the weights are on titan's local SSD. Test 1 passed 5/5 with 44 tests in 71 minutes; test 2 was a full pass (7 tools, 66 tests) in 322 of its 360 minutes, about 14 tok/s over each run. It works, but it is the slowest model to pass both tests: a second GPU (Maya drafts with MTP only on two) is the way to make it practical. Over NFS and without the patches it managed 4 tok/s. Huihui's abliterated UD-IQ1_S on the same engine failed both tests: it fell into repetition ('-0-0-0...' to the token limit) and its test 2 server had an empty main. Orcarouter's uncensored Q2_K does not load on Maya 1.3: its attention and shared-expert weights are Q2_K, and Maya's dense kernel has no Q2_K path ("unsupported native MMVQ GGML type"), so neither test ran. On llama.cpp (Unsloth's glm5next branch, experts in RAM) it loaded and decoded at about 10 tok/s, but in test 1 it spent 78 minutes probing the API and talking itself out of starting ("Let me now write the code. ... Actually, let me first check ...") and wrote no files; stopped by hand as a failure. Q2_K is too tight a quant for this model.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| GLM-5.3-Flash · Maya (Strata engine for GLM), experts in VRAM and RAM | Maya 1.3 (patched) | Maya-S-v2 IQ2_XXS | – | – | 13.9 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 44 | 13.9 | 71 | 9 py | 7.3 | – | – | Maya 1.3 (patched) | 9 subcommands |
| 2 | pass | 7 tools | 66 | 13.9 | 322 | 5/30 | 9.2 | – | – | Maya 1.3 (patched) | TEST 2 on Project Maya v1.3.0 + bakeoff patches (image -p3, RAM_ALL, DRAIN_SERVE, GLM tool calls), Maya-S IQ2_XXS from titan's local SSD: full pass, 7 tools, 66 tests, 322 min (cap 360), 13.9 tok/s over the run (17-22 live), 285 steps, 2,835 lines of Rust, no compaction, no … |

_Generated from the bake-off results on 2026-10-08._
