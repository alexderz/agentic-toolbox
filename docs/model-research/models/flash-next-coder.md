# Qwen3.8-Flash-Next Coder (1.6-bit)

**Status:** Dropped

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF (IQ1_M) |
| Architecture | MoE, 125B total / 6B active |
| Vision | yes (head) |

## Summary

A coder tune of Flash-Next squeezed to IQ1_M (about 1.6 bits per weight).

## Verdict

Failed test 2 twice on Strata: first a thinking loop (no budget), then a library with no binary. The quantization is too aggressive for this work.

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| Flash-Next Coder (1.6-bit) | yes (head) | qwen3vl_merger | 0.91 GB | ~920 (est.) |

- Flash-Next Coder (1.6-bit): no setup we run loads its vision head or tower: every variant runs blind.

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Coder (1.6-bit) · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ1_M | 128k | 26 | 9.9 |
| Flash-Next Coder (1.6-bit) · Strata, GPU expert cache | Strata | IQ1_M | 256k | – | 25.9 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 24 | 9.9 | 44 | 1 py | 1.4 | 128k | 26 | llama.cpp 0.4 | 7 subcommands |
| 2 | fail | 0 tools | – | 25.9 | 37 | 11/15 | – | 256k | – | Strata | Strata coder IQ1_M, NO thinking budget (Strata default off): 46 steps, 39 min, then a thinking LOOP ("Hmm, real Rust: String::from_utf8?" repeated) filled the 32k reply; no files written. Rerun with budget queued (wb-strata-coder-tb) |
| 2 | fail | 0 tools | – | 20.4 | 219 | 15/21 | 190.8 | 256k | – | Strata | Strata coder IQ1_M with the 24k budget (rerun): FAIL verified by hand: a library crate only (lib.rs + 5 modules, 1,242 lines), no main.rs or [[bin]], so no server to start; 118 steps, 219 min, 20.4 tok/s, 1 compaction, no thinking loop (the budget fixed that); ended on its own |

_Generated from the bake-off results on 2026-10-15._
