# GLM-5.3-Flash

**Status:** Tested

| | |
| --- | --- |
| Family | GLM |
| Source | zai-org/GLM-5.3-Flash |
| Architecture | MoE, 320B / 18B active, multimodal |

## Summary

GLM's hybrid linear/sparse-attention MoE. Runs on Project Maya, a Strata-derived engine that tiers the 12,096 experts across VRAM, pinned RAM and disk.

## Verdict

On Maya (Maya-S-v2 IQ2_XXS, 97 GB, with three of our patches: all experts eligible for the RAM tier, VRAM victims kept in RAM, and GLM tool-call parsing) it decodes about 17-19 tok/s once the weights are on titan's local SSD. Test 1 passed 5/5 with 44 tests in 71 minutes. Test 2 is running. Over NFS and without the patches it managed 4 tok/s.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| GLM-5.3-Flash · Maya (Strata engine for GLM), experts in VRAM and RAM | Maya 1.3 (patched) | Maya-S-v2 IQ2_XXS | – | – | 13.9 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 44 | 13.9 | 71 | 9 py | 7.3 | – | – | Maya 1.3 (patched) | 9 subcommands |

_Generated from the bake-off results on 2026-10-08._
