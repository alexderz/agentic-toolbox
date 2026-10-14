# Decision 3.0 (d3 family)

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Decision |
| Source | vllm-sr/d3, d3-flash, d3-mini, d3-nano, d3-lite, d3-edge (Apache 2.0) |
| Architecture | Decision models with vision and video input, 0.6B to 26B, built on Qwen3.5 and Qwen3.8-27B |

## Summary

The multimodal follow-up to Decision 2.0: text or JSON plus optional images and video in, and a choice, yes/no or score with probabilities out, in one call without generating text. Six sizes; the 26B flagship is 49 GB in bf16 and the 8B d3-flash is 16 GB.

## Verdict

Not downloaded. The models load through their own Transformers code and server, which none of the engines we run can serve, and there are no GGUF or other requants yet. The five smaller sizes would fit a 24 GB card as released; the flagship needs a 4-bit build. The benchmark ranking is the authors' own claim.

_Generated from the bake-off results on 2026-10-14._
