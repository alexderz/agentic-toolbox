# BitNet b1.58 2B4T

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Other |
| Source | microsoft/bitnet-b1.58-2B-4T (MIT) |
| Architecture | Dense, 2.4B, ternary weights |

## Summary

Microsoft's 1.58-bit chat model. The official I2_S GGUF is 1.1 GB.

## Verdict

Not downloaded. It fits easily, but it runs on bitnet.cpp (or ik_llama.cpp for a community IQ2_BN file), not on llama.cpp 0.6, vLLM, SGLang or Strata. Too small for the agent tests unless a 1-bit baseline is wanted.

_Generated from the bake-off results on 2026-10-15._
