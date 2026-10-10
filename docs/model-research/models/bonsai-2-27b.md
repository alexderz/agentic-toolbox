# Ternary Bonsai 2 27B

**Status:** Dropped

| | |
| --- | --- |
| Family | Other |
| Source | prism-ml/Ternary-Bonsai-2-27B-gguf |
| Architecture | Dense, 27B, ternary weights |

## Summary

Qwen3.8-27B compressed to ternary weights by PrismML (PTQ1_0 5.9 GB, PQ2_0 7.2 GB); needs PrismML's llama.cpp fork. The makers report 98% of FP16 Qwen3.8-27B on 14 thinking-mode benchmarks.

## Verdict

Fast (41-47 tok/s) but invents APIs: in test 1 most of its subcommands targeted Home Assistant endpoints that do not exist (11 of 14 paths in one run), even after its own probes got 404s for them. A 2026-10-06 review of our runs found tool calls parsed normally and sampling matched the model card, but we ran the default `xhigh` reasoning effort (the makers recommend `medium` for agent work; `xhigh` has a known looping issue) with no thinking budget, on a PrismML build from 2026-09-25. Rerun 2026-10-07 with the makers' settings (PrismML build 2026-10-05, PQ2_0, `medium`, 24k budget, model-card sampling): test 1 scored 5/5 with 94 tests at 50.8 tok/s (old runs 2/5 and 4/5), but 7 of its 11 subcommands still call Home Assistant endpoints that do not exist (`/api/entities`, `/api/entity_count`, `/api/system_state`, `/api/scheduler`, `/api/config/users`, `/api/version`, `/api/history/data`), and it kept `/api/entities` after a 404. The settings fixed reliability, not the invented API surface. Test 2 rerun (153 min, 48.1 tok/s): partial pass. It builds, initializes, lists 3 tools and passes 32 tests, but `tools/call` demands an invented `toolName` field instead of the spec's `name`, so no standard client can call a tool, and two of its three tools call the nonexistent `/api/entities`. Its final message claimed live Home Assistant worked. 33 of 59 builds failed (65 errors per 1k lines). Tried 2026-10-09 on the community serving stack (professorpalmer/bonsai-ada-surgery: 46 patches on PrismML llama.cpp with MTP drafting, tool-call grammar, reasoning-effort and budget handling; PTQ1_0 with a grafted MTP head; the repo's Python layer proxy not used). With the model's recommended sampling it ran fast and clean (65-73 tok/s, about 16 GB VRAM at 262k q8_0); without it, the first try degenerated into repeated tokens. The habit stayed: test 1 helped and passed 64 tests but failed the read checks because its CLI calls invented endpoints (`/api/entities`, `/api/timers`, `/api/themes`, `/api/scripts`); test 2 built a 4-tool server with 27 passing tests whose list tool calls `/api/entities` and gets 404. The serving fixes address speed and agent-loop failures, not the invented API surface. Abliterated variants exist; not tested.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Bonsai 2 27B (ternary) | llama.cpp 0.4 | ternary | 128k | – | 40.8 |
| Bonsai 2 27B PQ2 | llama.cpp 0.4 | PQ2 | 248k | – | 47.5 |
| Bonsai 2 27B PQ2 · PrismML fork 2026-10-05, effort medium, 24k budget | PrismML llama.cpp | PQ2 | 248k | – | 50.8 |
| Bonsai 2 27B PTQ1_0 + MTP · bonsai-ada-surgery llama.cpp (46 patches), 262k q8_0, recommended sampling | llama.cpp-ada-ternary bonsai-q8-product (5251968) | PTQ1_0 | – | – | 73.3 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | fail | 2/5 checks | 68 | 40.8 | 42 | 4 py | 1.9 | 128k | – | llama.cpp 0.4 | 20 subcommands |
| 1 | fail | 2/5 checks | 64 | 65.3 | 41 | 5 py | 2.0 | – | – | llama.cpp-ada-ternary bonsai-q8-product (5251968) | 16 subcommands |
| 1 | fail | 2/5 checks | 46 | 46.5 | 57 | 5 py | 3.4 | 128k | – | llama.cpp 0.4 | 14 subcommands |
| 1 | partial | 4/5 checks | 75 | 47.5 | 36 | 4 py | 2.7 | 248k | – | llama.cpp 0.4 | 17 subcommands |
| 1 | pass | 5/5 checks | 94 | 50.8 | 33 | 3 py | 1.9 | 248k | – | PrismML llama.cpp | 11 subcommands |
| 2 | partial | 4 tools | 27 | 73.3 | 39 | 22/35 | 111.1 | – | – | llama.cpp-ada-ternary bonsai-q8-product (5251968) | tool_call no data (checked by hand): ha_list_entities calls the nonexistent /api/entities (6 uses in the code) and gets 404 from the replay; init and tools/list work; same invented endpoint as the earlier Bonsai PQ2 runs |
| 2 | partial | 3 tools | 32 | 48.1 | 153 | 33/59 | 64.9 | 248k | – | PrismML llama.cpp | TEST 2: PARTIAL, tools/call fails. Builds, initialize ok, 3 tools (get_config, list_entities, get_entity), 32 tests pass. Verified by hand: tools/call returns -32602 'Missing required field toolName' (it invented a toolName param instead of the spec's name), so no standard … |

_Generated from the bake-off results on 2026-10-10._
