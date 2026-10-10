# Qwen-Image-2.1-Turbo

**Status:** Downloaded, not tested yet

| | |
| --- | --- |
| Family | Image generation |
| Source | Qwen/Qwen-Image-2.1-Turbo (Qwen Research License; unsloth GGUF for stable-diffusion.cpp) |
| Architecture | 7B image generation and editing model, 8-step distilled checkpoint |

## Summary

The accelerated checkpoint of Qwen-Image 2.1: text-to-image and natural-language edits in 8 denoising steps at CFG 1, with the sampling schedule stored in the checkpoint. Official folder 30 GB (16 GB of it the text encoder); the transformer alone is 7 GB as a Q8 GGUF.

## Verdict

Downloaded, not run yet. Same architecture as Qwen-Image 2.1, so it uses the same ComfyUI and stable-diffusion.cpp setups; the GGUF fits a 24 GB card with the text encoder in RAM. To be compared with the full-schedule model on the same prompts.

_Generated from the bake-off results on 2026-10-10._
