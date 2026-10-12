# PersonaPlex-7B

**Status:** Needs an engine update

| | |
| --- | --- |
| Family | Speech |
| Source | nvidia/personaplex-7b-v1 (gated; licence field other) |
| Architecture | 7B full-duplex speech-to-speech, Moshi |

## Summary

NVIDIA's conversational speech model: it listens and speaks at the same time, conditioned on a voice prompt and a text role.

## Verdict

Not downloaded. The official weights are 16 GB and gated. A community 4-bit GGUF is 4.4 GB, but only moshi.cpp loads it. None of the engines we run serves speech.

_Generated from the bake-off results on 2026-10-12._
