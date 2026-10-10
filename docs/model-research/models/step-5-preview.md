# Step 5 Preview

**Status:** Does not fit

| | |
| --- | --- |
| Family | Other |
| Source | StepFun Step 5 Preview (official open weights announced for about 2026-10-15; hosted free on OpenCode Zen until then) |
| Architecture | Sparse MoE, about 600B total / 27B active, 1M context, text, image and video input |

## Summary

StepFun's software-engineering and knowledge-work model.

## Verdict

Does not fit: about 600B parameters is roughly 1.2 TB in BF16 and over 600 GB in the smallest third-party 3-bit GGUF, against 24 GB VRAM + 125 GB RAM; 27B active would also decode slowly from RAM. The copies on Hugging Face before the official release are third-party uploads of unknown provenance (one is a 'derisked' NVFP4 re-quant), so none were downloaded. Revisit only if StepFun releases a much smaller variant.

_Generated from the bake-off results on 2026-10-10._
