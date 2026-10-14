# MiniCPM-V 4.7

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | MiniCPM-V |
| Source | openbmb/MiniCPM-V-4.7-1B and openbmb/MiniCPM-V-4.7-35B-A3B (Apache 2.0; official GGUF) |
| Architecture | Vision-language. 1.55B dense (qwen35) and 35.3B MoE (qwen35moe, 256 experts, 8 active); projector minicpmv4_7 |

## Summary

OpenBMB's image and video models, released 2026-10-12. The 1B checkpoint is 2.90 GiB in bf16; its Q8_0 GGUF is 1.01 GiB plus a 1.03 GiB vision projector. The 35B-A3B checkpoint is 65.71 GiB in bf16; Q4_K_M is 19.71 GiB plus a 1.04 GiB projector, and Q8_0 is 34.37 GiB.

## Verdict

Not downloaded. llama.cpp 0.6 already loads the qwen35 and qwen35moe language files, but not this vision projector: type minicpmv4_7 was added on 2026-10-10 (PR 29416), after the v0.6.0 image from 2026-10-05. Current llama.cpp master has it. The 1B fits a 24 GB card easily. The 35B Q4_K_M plus projector is 20.8 GB, so only a short context fits on the card; the Q8_0 fits with experts in RAM.

_Generated from the bake-off results on 2026-10-14._
