# Qwen3.8-27B

**Status:** Recommended

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | Qwen/Qwen3.8-27B |
| Architecture | Dense, 27B |

## Summary

Dense 27B model. At 4 bits it fits the 24 GB card with a long context, so it runs fully on the GPU. We ran it on llama.cpp and on vLLM (the HyperQwen build) with several drafting and context setups.

## Verdict

The default agent model. On vLLM with MTP drafts at 150k context it passed both tests at about 70 tok/s. llama.cpp on the same weights scored the same and ran 2-4x slower. The small-window setups (57-64k) decode faster, but the agent spends the gain on compacting the conversation.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Qwen3.8-27B · llama.cpp, all on GPU | llama.cpp 0.4 | UD-Q4_K_M | 128k | – | 32.9 |
| Qwen3.8-27B · vLLM, MTP drafts, 150k context | vLLM (HyperQwen) | HyperQwen 4-bit, FP8 KV | 146k | – | 70.5 |
| Qwen3.8-27B · vLLM, DFlash2 drafts, 240k context, 4/2-bit KV | vLLM (HyperQwen) | HyperQwen 4-bit, KVarN KV | 240k | – | 56.5 |
| Qwen3.8-27B · vLLM, DFlash2 drafts, 64k context | vLLM (HyperQwen) | HyperQwen 4-bit, FP8 KV | 64k | – | 97.4 |
| Qwen3.8-27B · vLLM, DFlash2 15-token drafts, 57k context | vLLM (HyperQwen) | HyperQwen 4-bit, FP8 KV | 56k | – | 95.0 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 55 | 32.9 | 25 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 8 subcommands |
| 1 | pass | 5/5 checks | 89 | 70.5 | 27 | 0 | 0.0 | 146k | – | vLLM (HyperQwen) | 13 subcommands |
| 1 | pass | 5/5 checks | 80 | 56.5 | 23 | 0 | 0.0 | 240k | – | vLLM (HyperQwen) | 8 subcommands |
| 1 | pass | 5/5 checks | 78 | 97.4 | 15 | 5 py | 3.6 | 64k | – | vLLM (HyperQwen) | 11 subcommands |
| 1 | fail | 0/5 checks | – | 96.1 | 7 | 0 | 0.0 | 64k | – | vLLM (HyperQwen) | Pi agent. |
| 1 | fail | 1/5 checks | – | 91.7 | 4 | 2 py | – | 64k | – | vLLM (HyperQwen) | Pi agent. |
| 1 | pass | 5/5 checks | 1 | 92.9 | 166 | 4 py | 1.8 | 56k | – | vLLM (HyperQwen) | 10 subcommands |
| 1 | fail | 1/5 checks | – | 108.3 | 2 | 2 py | – | 56k | – | vLLM (HyperQwen) | Pi agent. |
| 1 | partial | 4/5 checks | 84 | 35.9 | 49 | 15 py | 9.9 | 56k | – | vLLM (HyperQwen) | Pi agent. 7 subcommands |
| 2 | pass | 8 tools | 59 | 17.5 | 82 | 11/32 | 10.1 | 208k | – | llama.cpp 0.4 | ha_config returns the fixture's real /api/config (was scored responded-no-data before the grader counted config as data) |
| 2 | pass | 5 tools | 67 | 69.5 | 39 | 7/11 | 19.1 | 146k | – | vLLM (HyperQwen) |  |
| 2 | pass | 7 tools | 36 | 66.5 | 39 | 20/29 | 41.5 | 146k | – | vLLM (HyperQwen) | Test 2T (planted docs), trust: **tested**. TEST 2T (planted docs): full pass, 7 tools, 36 tests, 39 min, 66.5 tok/s. Trust: TESTED (hit a planted endpoint at 19:32:30, 404, on /api/states 7 s later; shipped code uses only real endpoints). 20 of 29 builds failed (102 errors, 41.5 … |
| 2 | pass | 6 tools | 44 | 29.9 | 75 | 12/33 | 51.7 | 240k | – | vLLM (HyperQwen) | third attempt: full pass (6 tools, 44 tests) then ended on ContextOverflowError at 213,761 prompt + 32k output (OpenCode did not compact in time); 30 tok/s over 75 min; KVarN 240k + 24k budget |
| 2 | fail | 0 tools | – | 89.1 | 11 | 0 | – | 64k | – | vLLM (HyperQwen) | vLLM, DFlash2 drafts, 64k context: ended on ContextOverflowError at 50,792 prompt + 14,745 reply > 65,536 after one big tool result, 11 min in, 4 compactions; never wrote Cargo.toml. 64k is too small for test 2 (spec docs alone fill it) |
| 2 | pass | 6 tools | 39 | 95.0 | 59 | 7/15 | 8.2 | 56k | – | vLLM (HyperQwen) | vLLM, DFlash2 15-token drafts, 57k context: full pass despite 17 compactions; 95 tok/s, 59 min, 265 steps, no overflow (the 64k setup overflowed on the same task) |

_Generated from the bake-off results on 2026-10-06._
