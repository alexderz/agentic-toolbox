# Mistral Large 4

**Status:** Does not fit

| | |
| --- | --- |
| Family | Other |
| Source | Mistral Large 4 (open weights, 2026-10-06) |
| Architecture | MoE, 1.05T total / 49B active, 1M context, vision |

## Summary

Mistral's open-weight flagship.

## Verdict

Does not fit: even about 2 bits per weight is roughly 260 GB against 24 GB VRAM + 125 GB RAM, and 49B active would decode at 1-2 tok/s from RAM. Revisit only for a much smaller variant.

_Generated from the bake-off results on 2026-10-09._
