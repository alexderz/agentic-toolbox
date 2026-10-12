# BitNet embeddings (0.6B and 270M)

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Embedding |
| Source | microsoft/bitnet-embedding-0.6b and microsoft/bitnet-embedding-270m (MIT) |
| Architecture | BitNet text embeddings, 0.6B (1024 dims) and 270M (640 dims), 32k context |

## Summary

Microsoft's 1.58-bit embedding models. The I2_S GGUF files are 0.40 GB and 0.34 GB.

## Verdict

Not downloaded. They fit easily and need bitnet.cpp's I2_S kernels, which none of the engines we run has.

_Generated from the bake-off results on 2026-10-12._
