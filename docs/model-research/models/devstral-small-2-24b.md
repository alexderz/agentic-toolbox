# Devstral Small 2 24B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | mistralai/Devstral-Small-2 |
| Architecture | Dense, 24B |
| Vision | yes (head) |

## Summary

Mistral's coding model.

## Verdict

Inconsistent: 2/5, then 4/5 with 13 of its 17 tests passing. In the second run the single-entity lookup is wrong for every id: it prints the first entity in the list and exits 0, so a made-up id looks like a success (the first grading missed this and recorded 5/5; corrected by the regrade of 2026-10-10).

## Vision

| Weights | Vision | Head | Head size | Tokens per 1280x720 screenshot |
| --- | --- | --- | --- | --- |
| Devstral Small 2 24B | yes (head) | pixtral | 0.88 GB | ~1000 (est.) |

- Devstral Small 2 24B: no setup we run loads its vision head or tower: every variant runs blind.

Loading a head costs VRAM: its weights plus a compute buffer, about 1.1 to 2.7 GB by head type. On a card already full with the model and its context, the head goes on the CPU instead (llama.cpp --no-mmproj-offload, or the engine's host-RAM offload): then it costs almost no VRAM but system RAM, and every image is encoded on the CPU, which takes longer per screenshot. Every screenshot also takes context: about 400 to 1,200 tokens for a 1280x720 image, depending on the head. A long agent run that takes screenshots often fills its context and compacts sooner. For example, with a head that costs about 920 tokens per screenshot (the Qwen3-VL style), 100 screenshots in a 2-hour run are about 92,000 tokens, over a third of a 262k window.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Devstral Small 2 24B | llama.cpp 0.4 | Q4 | 200k | – | 33.1 |
| Devstral Small 2 24B Q5_K_M · llama.cpp 0.6, 70k, Mistral sampling (temperature 0.15) and template | llama.cpp 0.6 | Q5_K_M | – | – | 33.4 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 38 | 25.6 | 15 | 1 py | 0.9 | 100k | – | llama.cpp 0.4 | 6 subcommands |
| 1 | partial | 4/5 checks | 13 | 33.1 | 11 | 2 py | 3.0 | 200k | – | llama.cpp 0.4 | 7 subcommands |
| 1 | pass | 5/5 checks | 21 | 33.4 | 9 | 8 py | 12.8 | – | – | llama.cpp 0.6 | 11 subcommands |
| 2 | fail | 0 tools | 0 | 29.1 | 3 | 0 | 0.0 | – | – | llama.cpp 0.6 | checked by hand: initialize answers with snake_case keys and a number for the version (protocol_version 20260728, server_info), so a client finds no protocolVersion or serverInfo; the request struct needs an id (src/main.rs:12), so the notifications/initialized message ends the … |

_Generated from the bake-off results on 2026-10-15._
