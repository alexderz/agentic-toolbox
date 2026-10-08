# EmbeddingGemma 2

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Embedding |
| Source | google/embeddinggemma-2 (Apache 2.0; GGUF from ggml-org and unsloth) |
| Architecture | Multimodal embedding encoder, 740M (text-only path 270M), 768 dims, 8k context |

## Summary

Google's embedding model on Gemma 4: text, code, images, video and audio in one vector space; Matryoshka sizes down to 128. Weights 1.5 GB; GGUF Q8_0 310 MB plus a 555 MB multimodal projector.

## Verdict

Fits easily, but neither engine we run knows its architecture yet: llama.cpp added it after v0.6.0 (PR 30054, 2026-10-06) and vLLM after 0.31.0. Revisit with the next llama.cpp release. Activations need bf16 or f32, not f16.

_Generated from the bake-off results on 2026-10-08._
