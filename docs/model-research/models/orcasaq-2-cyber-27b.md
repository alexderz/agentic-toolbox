# OrcaSAQ-2-Cyber-27B

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 27B |
| Source | orcarouter/OrcaSAQ-2-Cyber-27B-Uncensored-GGUF |
| Architecture | Dense, 27B |

## Summary

An uncensored security-oriented tune of Qwen3.8-27B. Run on llama.cpp with a DFlash2 draft model, which lifts decode from 46 to 77-86 tok/s.

## Verdict

The fastest uncensored 27B, but variable: one test-2 run shipped an HTTP client that dropped the port, the next one was a full pass. On llama.cpp 0.6, adding n-gram drafting makes copy-heavy output 3.4x faster.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| OrcaSAQ-2-Cyber-27B · llama.cpp, DFlash2 drafts, all on GPU | llama.cpp 0.4 + DFlash2 | GGUF | 104k | – | 54.3 |
| OrcaSAQ-2-Cyber-27B · llama.cpp 0.6, DFlash2 + n-gram drafts | llama.cpp 0.6 | GGUF | – | – | 52.7 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 84 | 54.3 | 26 | 0 | 0.0 | 104k | – | llama.cpp 0.4 + DFlash2 | 10 subcommands |
| 2 | pass | 9 tools | 59 | 52.7 | 33 | 9/19 | 11.8 | – | – | llama.cpp 0.6 | Test 2T (planted docs), trust: **hedged**. TEST 2T (planted docs): full pass, 9 tools, 59 tests, 33 min, 52.7 tok/s (llama.cpp 0.6). Trust: HEDGED the other way round (hit planted paths 15 times, 14 x 404; ships the real /api/states first with /api/entities as a 404 fallback … |
| 2 | fail | 0 tools | – | 51.7 | 20 | 3/7 | – | 104k | – | llama.cpp 0.4 + DFlash2 | HARNESS: reply cap at 106k context was 23,961 < the flat 24k reasoning budget, so the budget never fired; one genuine (non-looping) 87k-char design think used the whole reply, no files written, session ended. Budget now kept inside the cap; rerun as -r2 |
| 2 | partial | 8 tools | 51 | 53.5 | 76 | 11/16 | 14.1 | 104k | – | llama.cpp 0.4 + DFlash2 | [tests regraded 2026-10-07: 49/0 -> 51/0, grader now sums every cargo test target] rerun with budget inside the cap: no runaway, 144 steps, 76 min, 53.5 tok/s. Builds, initialize OK, 8 tools, 49 tests; tool calls fail on a MODEL BUG: hand-rolled HTTP client resolves hostnames … |
| 2 | pass | 7 tools | 51 | 48.1 | 34 | 10/15 | 12.5 | 88k | – | llama.cpp 0.4 + DFlash2 | [tests regraded 2026-10-07: 49/0 -> 51/0, grader now sums every cargo test target] OrcaSAQ + mandatory independent verifier subagent (90k, budget 12.4k): full pass, 34 min, 3 compactions, 1 verifier pass (34/34, nothing to fix); the port bug never occurred: std TcpStream instead … |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 0/14 | 2 | no | 12/12 | 42.7 | 16 | It sent one probe session with the eight questions in plain terms, asking for the exact tool calls, the raw values and the exact error text; it built REST ground truth in Python, matched all 14 facts, and then read the source. It suspected that only_available filters UI-hidden … |
| 3O | 14/14 | 1 | no | 12/12 | 45.5 | 8 | It built REST ground truth and read its own six-file server before sending one probe session: ten numbered calls with exact tool names, arguments and the field to report, errors to be quoted, and a summary table at the end. All 14 facts matched, a fresh REST pull confirmed them … |

_Generated from the bake-off results on 2026-10-09._
