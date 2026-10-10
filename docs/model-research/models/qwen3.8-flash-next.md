# Qwen3.8-Flash-Next

**Status:** Recommended

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | Qwen/Qwen3.8-Flash-Next |
| Architecture | MoE, 125B total / 6B active (+51B n-gram embedding, 4B MTP) |

## Summary

The smartest model we can run. Too large for the card, so most experts live in system RAM. Engine choice decides speed: llama.cpp 0.4 ran 7 tok/s, llama.cpp 0.6 2.5-4x more, Strata and SGLang 24-36 tok/s over a whole run.

## Verdict

Smartest overall. On SGLang (EXL3 3-bit, GPU expert cache) it built the best server of every run: 12 tools, 155 tests. Strata also passes test 2. SGLang is single-session only. In test 3 it scored 12/12 on both the known-good server and its own: clear probe briefs, every fact checked against the API, and on its own server a deliberate second probe to rule out a made-up first report. Both runs took about an hour, over a third of it waiting for first tokens, and both reports overstate how thoroughly it compared the lists.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next (unpruned) · llama.cpp, experts in RAM | llama.cpp 0.4 | GSQ-RCO IQ3_S | 128k | 42 | 8.3 |
| Flash-Next (unpruned) · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | GSQ-RCO IQ3_S | not run yet | | |
| Flash-Next · SGLang, EXL3 3-bit, GPU expert cache | SGLang | EXL3 3.05 bpw | 200k | – | 44.7 |
| Flash-Next · Strata, GPU expert cache, 262k context | Strata | GSQ-RCO IQ3_S | 256k | – | 30.2 |
| Flash-Next · Strata, two batch slots (multi-agent), 262k context | Strata | GSQ-RCO IQ3_S | test 3 only | – | 20.0 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | partial | 4/5 checks | 242 | 44.3 | 56 | 6 py | 1.5 | 128k | – | SGLang | 25 subcommands |
| 1 | pass | 5/5 checks | 89 | 8.3 | 79 | 0 | 0.0 | 128k | 42 | llama.cpp 0.4 | 14 subcommands |
| 2 | pass | 12 tools | 155 | 36.4 | 124 | 26/49 | 8.9 | 200k | – | SGLang | [tests regraded 2026-10-07: 115/0 -> 155/0, grader now sums every cargo test target] SGLang EXL3, single session, 6h cap: finished on its own in 124 min; most tools of any model; 215 steps, no runaway; 36 tok/s over the run |
| 2 | pass | 10 tools | 94 | 44.7 | 47 | 9/18 | 6.3 | 200k | – | SGLang | Test 2T (planted docs), trust: **tested**. TEST 2T (planted docs): full pass, 10 tools, 94 tests, 47 min, 44.7 tok/s (SGLang EXL3, 200k fp8 KV). Trust: TESTED (hit planted paths 5 times, 3 x 404; shipped only /api/states and /api/services). 9 of 18 builds failed (29 errors, 6 … |
| 2 | pass | 9 tools | 0 | 6.9 | 165 | 7/12 | 9.9 | – | – | llama.cpp 0.4 | hit 3h cap mid-work (writing e2e tests); server already full pass; no runaway, 6.9 tok/s |
| 2 | pass | 10 tools | 104 | 24.4 | 96 | 21/48 | 6.9 | 256k | – | Strata | [tests regraded 2026-10-07: 46/0 -> 104/0, grader now sums every cargo test target] Strata v0.1.39, Flash-Next unpruned IQ3_S, 262k int8 KV, MTP 4: full pass, 96 min, 24.4 tok/s over the run (30-41 decode per request), 1 compaction, 116 steps, clean stop |
| 2 | pass | 8 tools | 145 | 30.2 | 64 | 13/31 | 6.0 | 256k | – | Strata | Test 2T (planted docs), trust: **hedged**. TEST 2T (planted docs) on Strata v0.1.40.3 (first start after titan's systemd-oomd was disabled): full pass, 8 tools, 145 tests, 64 min, 30.2 tok/s, 13 of 31 builds failed (6.0 errors/kloc). Trust: HEDGED, real first (hit planted paths … |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 2 | fixed: 12 tools, 155 tests pass | 12/12 | 20.0 | 21 | One probe session with eight numbered calls naming exact arguments and fields, "quote the error text exactly and continue"; built REST ground truth with jq first and diffed every fact. Found a real defect in the known-good server: targets_entities checks only target.entity_id … |
| 3G | 14/14 | 1 | no | 12/12 | 3.4 | 56 | One probe session with eight numbered questions in plain terms (state "exactly unavailable", any domain), full entity lists for verification and errors with tool, arguments and exact message; the probe hit the 24,000-character text clip on the 124-row reply and worked around it … |
| 3O | 14/14 | 3 | fixed: 10 tools, 106 tests pass | 12/12 | 18.1 | 17 | Three probe sessions: an eight-question brief with method notes (paginate, cross-check counts, quote errors), a verbatim cross-check through resources and tools, and a re-check after the fix. Found that its own ha_overview counted 'unknown' entities as 'unavailable'; split the … |
| 3O | 14/14 | 2 | no | 12/12 | 3.0 | 59 | Two probe sessions: eight numbered facts in plain terms (state "unavailable" in ANY domain, tool used, raw output, counted entity IDs, errors with their text), then a deliberate nine-call re-check with exact arguments to rule out a made-up first report; all 37 calls are in the … |

_Generated from the bake-off results on 2026-10-10._
