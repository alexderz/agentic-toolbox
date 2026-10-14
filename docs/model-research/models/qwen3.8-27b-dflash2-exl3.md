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

Not downloaded, and not needed: we built an ExLlamaV3 server and paired turboderp's EXL3 4.00 bpw weights with z-lab's own DFlash2 drafter (2026-10-13): 158 tok/s on short code against 116 with the model's MTP head, at a 98k window with an 8-bit cache. Both setups are on the Qwen3.8-27B card. This 5.0 bpw requant of the drafter would only matter if the z-lab drafter stopped fitting.

_Generated from the bake-off results on 2026-10-14._
