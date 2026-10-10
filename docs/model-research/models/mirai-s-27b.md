# Mirai S (Qwen3.8-27B-S experimental)

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | trymirai/Qwen3.8-27B-S-experimental (Apache 2.0) |
| Architecture | Dense 27B compressed to about 8 GB, with a 3.4 GB speculator model |

## Summary

Mirai's compressed Qwen3.8-27B for consumer GPUs: about 8 GB of weights plus a speculator for drafting, aimed at 8 to 12 GB cards with very long context.

## Verdict

Not downloaded. It ships in Mirai's own formats (a patched vLLM and the uzu runtime) and a community llama.cpp fork serves it; none of the engines we run loads it. Worth a container of its own if the small footprint matters, in the same way as the Bonsai ada build.

_Generated from the bake-off results on 2026-10-10._
