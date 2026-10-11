# Gemma 4 31B

**Status:** Tested

| | |
| --- | --- |
| Family | Gemma 4 |
| Source | google/gemma-4-31b |
| Architecture | Dense, 31B |

## Summary

Google's dense Gemma 4.

## Verdict

Fast and finishes in minutes, but thin: 3 tools on test 2. Needs enable_thinking (its template defaults it off). Test 3 (2026-10-10, 5 and 9 minutes): on the known-good server it delegated cleanly, confirmed every fact against the API and trusted the server (rubric 10/12); on its own server it declared the server fully verified on 12 of 14 facts without probing again (7/12). Both facts files have correct values in the wrong layout, because a compaction dropped the format the prompt asked for, so the automatic grade is 0/14 on both.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Gemma 4 31B 4-bit · llama.cpp, all on GPU | llama.cpp 0.4 | Q4 | 72k | – | 53.4 |
| Gemma 4 31B 8-bit · llama.cpp, 72k context | llama.cpp 0.4 | Q8_0 | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 11 | 38.5 | 3 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 11 | 39.5 | 5 | 0 | 0.0 | 72k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 9 | 30.6 | 3 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 5 subcommands |
| 1 | pass | 5/5 checks | 10 | 53.4 | 2 | 0 | 0.0 | 72k | – | llama.cpp 0.4 | 4 subcommands |
| 1 | pass | 5/5 checks | 12 | 51.4 | 3 | 0 | 0.0 | 128k | – | llama.cpp 0.4 | 2 subcommands |
| 2 | partial | 3 tools | 4 | 50.3 | 12 | 4/5 | 15.4 | 128k | – | llama.cpp 0.4 | no initialize method (-32601 Method not found: initialize), reply also lacks "jsonrpc"; tools/list and calls work without it but no client gets past the handshake |
| 2 | pass | 3 tools | 5 | 43.8 | 4 | 3/4 | 6.2 | 128k | – | llama.cpp 0.4 |  |
| 2 | pass | 3 tools | 7 | 47.0 | 5 | 1/1 | 2.0 | 72k | – | llama.cpp 0.4 |  |
| 2 | pass | 3 tools | 5 | 38.8 | 8 | 3/4 | 17.2 | 72k | – | llama.cpp 0.4 | no thinking (baseline); graded from a copy: a root-owned .git/config written after the case blocked the grader's SELinux relabel |
| 2 | pass | 4 tools | 5 | 39.7 | 4 | 0/3 | 0.0 | 128k | – | llama.cpp 0.4 |  |
| 2 | partial | 5 tools | 5 | 46.6 | 4 | 1/3 | 17.8 | 128k | – | llama.cpp 0.4 | Test 2T (planted docs), trust: **trusted**. tool_call no data (checked by hand): list_entities returns isError 'Entity not found: entities' (it queries /api/states/entities instead of /api/states) |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 0/14 | 1 | no | 10/12 | 26.9 | 4 | One probe returned all eight groups of facts and the agent confirmed each against the API, so trusting the server followed from the evidence. The values in the facts file are correct but in its own nested layout without the verdict fields: a compaction just before writing … |
| 3O | 0/14 | 1 | no | 7/12 | 18.7 | 8 | The probe needed 54 per-entity calls and could not get the unavailable total or the lock services (a 58 KB reply was cut off). The agent did not probe again or change the server, yet declared it fully verified and correct on 12 of 14 facts. The facts file is a flat custom … |

_Generated from the bake-off results on 2026-10-11._
