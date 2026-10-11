# Qwen3.8-27B DFlash2 draft for ExLlamaV3

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | Mia-AiLab/Qwen3.8-27B-DFlash2-EXL3-5.0bpw (Apache 2.0) |
| Architecture | DFlash2 draft model for Qwen3.8-27B, EXL3 5.0 bpw, 1.4 GB |

## Summary

A draft model for speculative decoding of Qwen3.8-27B on ExLlamaV3, which supports DFlash2 drafting since v1.5.1 (v1.6.1 is current).

## Verdict

Not downloaded. It is a serving path for a model we already run, not a new model: we use DFlash2 drafts on llama.cpp and have no ExLlamaV3 server for the 27B. Worth a container of its own only to compare speed against the vLLM setup with MTP drafts.

_Generated from the bake-off results on 2026-10-11._
