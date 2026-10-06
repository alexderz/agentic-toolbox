# GLM-5.3-Flash

**Status:** Does not fit

| | |
| --- | --- |
| Family | GLM |
| Source | zai-org/GLM-5.3-Flash |
| Architecture | MoE, 320B / 18B active, multimodal |

## Summary

GLM's hybrid linear/sparse-attention MoE, supported by llama.cpp 0.6.

## Verdict

The smallest quants (87-112 GB, REAP-50 pruned 67-92 GB) only fit with most experts in RAM; 18B active would run around 3 tok/s. Too slow for agent work.

_Generated from the bake-off results on 2026-10-06._
