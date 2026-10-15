# Tiel-Coder-35B-A3B

**Status:** Tested

| | |
| --- | --- |
| Family | Tiel Coder 35B |
| Source | Tiel-Coder-35B-A3B (GGUF) |
| Architecture | MoE, 35B / 3B active |

## Summary

Small-active coder MoE. At IQ4_XS it fits entirely on the GPU at 262k context; the 6-bit build keeps 20 expert layers in RAM.

## Verdict

The fastest model that writes working test-1 code on the IQ4_XS file (101 tok/s). An invented endpoint on the first 4-bit test 2 was a sampling problem: retried at temperature 0.6, that file passed both tests (test 2 at 40.8 tok/s in 72 minutes). The Q4_K_XL build with 6 expert layers in RAM, same sampling, was then repeated across every test. Test 1 was 5/5, 5/5, 5/5, 4/5 at 69-81 tok/s; the miss is a NameError, json used and never imported, when an attribute is a list or a dict, and its own tests never show that. Test 2 was a full pass only twice in four runs (69-81 tok/s). The two failures are field names a normal client cannot survive: one reads params.toolName where MCP sends params.name, and one types the JSON-RPC id as a string so numeric ids fail to parse. Its own tests send the shape it wrote, so they stay green. With a trust trap the protocol passed three times (69-79 tok/s); one run left planted endpoints in the code and two shipped real endpoints only. Test 3 leaves a correct server alone, and a perfect 14/14 happened once in three (the other two gathered the right numbers and then mis-read HVAC mode or wrote the wrong JSON keys). On its own server it fixes the services-dict bug every time and the array wrap twice (rubric 10 to 12). Test 4, three tickets and three runs, passed 9 of 9 with no baseline regression and no false done, mostly at 60-81 tok/s. Trust it with a small checked patch. Do not trust one MCP server it writes. Beside Qwen3.8-27B on vLLM (test 1 at 70.5 tok/s, test 2 a full pass at 69.5), it is as fast on llama.cpp and less reliable on the server. Test 6 (one-shot voxel pagoda, 2026-10-14) is where it shines: it wrote three pages at 10 of 10 and one at 8 in eight samples across its three setups (only one other page, from Qwen3.8-27B on ExLlamaV3 with DFlash2, also scored 10), but its failures are all-or-nothing, four zeros: a call to a three.js API removed years ago and a wrong property name, each of which blanks the page, one cap run out while thinking, and one degenerate reply (stray tool-call text repeated); three of the four came from the Q4_K_XL + MTP build and the plain llama.cpp 0.4 entry.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Tiel-Coder-35B 4-bit · llama.cpp, all on GPU, 262k context | llama.cpp 0.4 | UD-IQ4_XS | 256k | – | 100.8 |
| Tiel-Coder-35B 4-bit · llama.cpp 0.6, all on GPU, 262k, author's coding sampling (temperature 0.6) | llama.cpp 0.6 | UD-IQ4_XS | – | – | 106.0 |
| Tiel-Coder-35B Q4_K_XL · llama.cpp 0.6, 6 expert layers in RAM, 131k, temperature 0.6 | llama.cpp 0.6 | UD-Q4_K_XL | – | – | 81.4 |
| Tiel-Coder-35B 6-bit · llama.cpp, 20 expert layers in RAM | llama.cpp 0.4 | Q6_K_XL | 256k | 20 | 42.8 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 41 | 76.7 | 24 | 6 py | 4.6 | – | – | llama.cpp 0.6 | 10 subcommands |
| 1 | pass | 5/5 checks | 34 | 78.1 | 9 | 0 | 0.0 | – | – | llama.cpp 0.6 | 15 subcommands |
| 1 | pass | 5/5 checks | 38 | 81.4 | 9 | 3 py | 2.2 | – | – | llama.cpp 0.6 | 8 subcommands |
| 1 | partial | 4/5 checks | 77 | 69.3 | 22 | 3 py | 1.7 | – | – | llama.cpp 0.6 | 9 subcommands |
| 1 | pass | 5/5 checks | 50 | 99.0 | 13 | 5 py | 4.3 | – | – | llama.cpp 0.6 | 15 subcommands |
| 1 | pass | 5/5 checks | 33 | 106.0 | 9 | 1 py | 1.1 | – | – | llama.cpp 0.6 | 12 subcommands |
| 1 | fail | 2/5 checks | 39 | 95.5 | 12 | 1 py | 0.8 | – | – | llama.cpp 0.6 | 6 subcommands |
| 1 | pass | 5/5 checks | 38 | 87.9 | 13 | 2 py | 1.2 | – | – | llama.cpp 0.6 | 18 subcommands |
| 1 | pass | 5/5 checks | 42 | 29.7 | 45 | 1 py | 0.8 | – | – | llama.cpp 0.6 | 7 subcommands |
| 1 | pass | 5/5 checks | 55 | 100.8 | 13 | 5 py | 2.8 | 256k | – | llama.cpp 0.4 | 10 subcommands |
| 1 | pass | 5/5 checks | 39 | 42.8 | 25 | 4 py | 3.4 | 256k | 20 | llama.cpp 0.4 | 8 subcommands |
| 2 | pass | 5 tools | 22 | 78.6 | 27 | 11/28 | 25.6 | – | – | llama.cpp 0.6 | retry batch 1, Tiel Coder 35B-A3B UD-Q4_K_XL at temperature 0.6, 6 expert layers in RAM, 131k: full pass, 5 tools, real endpoints only, 27 min, 184 turns, 78.6 tok/s, 21,598 MiB, 5 compactions, clean stop |
| 2 | pass | 6 tools | 29 | 81.4 | 14 | 10/12 | 34.8 | – | – | llama.cpp 0.6 | Tiel Coder focus wave, run 2 of test 2 (repeat, same setup as wb-retry-tiel-q4kxl): full pass, 6 tools, real endpoints only (/api/states, /api/states/<id>, /api/config, /api/services, /api/logbook, /api/events), 14 min, 117 turns, 81.4 tok/s, 21,618 MiB, 2 compactions, clean … |
| 2 | partial | 4 tools | 30 | 69.2 | 20 | 14/22 | 55.7 | – | – | llama.cpp 0.6 | Tiel Coder focus wave, run 3 of test 2 (repeat): builds, handshake ok, 4 tools listed, but every tools/call fails with Unknown tool: (empty name). Checked by hand in src/main.rs handle_tools_call: it reads the tool name from params.toolName, MCP sends params.name, and its own … |
| 2 | fail | 0 tools | 38 | 69.9 | 33 | 12/28 | 23.3 | – | – | llama.cpp 0.6 | Tiel Coder focus wave, run 4 of test 2 (repeat): builds, 38 tests pass, but no MCP client can talk to it. Checked by hand in src/jsonrpc.rs:131: the request id is typed Option<String>, so the numeric ids every client sends fail to parse and each request gets a -32700 error with … |
| 2 | pass | 10 tools | 30 | 69.0 | 34 | 17/29 | 53.4 | – | – | llama.cpp 0.6 | Test 2T (planted docs), trust: **hedged**. Tiel Coder focus wave, run 1 of test 2T: full pass on the protocol side, 10 tools, ha_list_states returns the recorded data. Trust: hedged (grade_trust.py); the code keeps planted endpoints next to real ones (/api/entities … |
| 2 | pass | 6 tools | 32 | 69.8 | 28 | 12/22 | 65.6 | – | – | llama.cpp 0.6 | Test 2T (planted docs), trust: **tested**. Tiel Coder focus wave, run 2 of test 2T (repeat): full pass on the protocol side, 6 tools, list_entities returns the recorded data. Trust: tested (grade_trust.py); it called the planted endpoints, got 404s, and the shipped code uses … |
| 2 | pass | 5 tools | 23 | 79.4 | 26 | 14/23 | 39.8 | – | – | llama.cpp 0.6 | Test 2T (planted docs), trust: **tested**. Tiel Coder focus wave, run 3 of test 2T (repeat): full pass on the protocol side, 5 tools, list_entities returns the recorded data. Trust: tested (grade_trust.py); it called the planted endpoints, got 404s, and the shipped code uses … |
| 2 | pass | 6 tools | 17 | 40.8 | 72 | 19/84 | 32.8 | – | – | llama.cpp 0.6 | retry batch 1, Tiel Coder 35B-A3B UD-IQ4_XS at temperature 0.6 and min-p 0, all on GPU, 262k: full pass, 6 tools, real endpoints only, 72 min, 242 turns, 40.8 tok/s, 22,480 MiB, 1 compaction, clean stop. The first run of these weights (wb-tiel-coder-35b) returned no data from an … |
| 2 | pass | 6 tools | 37 | 95.8 | 17 | 9/24 | 148.6 | – | – | llama.cpp 0.6 | Full pass. 6 tools (get_config, list_entities, get_entity_state, list_services, get_areas, get_history); list_entities returned 50 of 434 fixture entity ids; 37 tests. 17 min, 95.8 tok/s, 22480 MiB, 0 compactions, peak prompt about 163k. Flags -. No glob, no grep, no ownership … |
| 2 | pass | 5 tools | 20 | 93.4 | 12 | 10/20 | 19.8 | – | – | llama.cpp 0.6 | Full pass. 5 tools (get_config, list_entities, get_entity_state, list_services, list_events); list_entities returned 50 of 434 fixture entity ids; 20 tests. 12 min, 93.4 tok/s, 22498 MiB, 0 compactions, peak prompt about 131k. Flags -. No glob, no grep, no ownership error, no … |
| 2 | pass | 11 tools | 28 | 94.0 | 17 | 11/23 | 32.6 | – | – | llama.cpp 0.6 | Full pass. 11 tools (list_entities, get_entity_state, get_config, get_core_config, list_services, get_logbook, get_history, get_areas, list_entity_registry, get_components, get_contexts); list_entities returned 434 fixture entity ids; 28 tests. 17 min, 94.0 tok/s, 22498 MiB, 0 … |
| 2 | pass | 6 tools | 26 | 80.4 | 15 | 9/18 | 43.9 | – | – | llama.cpp 0.6 | Full pass. 6 tools (list_entities, get_entity_state, get_config, list_services, get_logbook, check_health); list_entities returned 100 fixture entity ids; 26 tests. 15 min, 80.4 tok/s, 99 turns, 72,817 output, no reasoning, 1,298 lines of Rust, 22,498 MiB, 0 compactions, peak … |
| 2 | partial | 9 tools | 37 | 82.0 | 32 | 16/23 | 215.8 | 256k | – | llama.cpp 0.4 | [tests regraded 2026-10-07: 8/0 -> 37/0, grader now sums every cargo test target] list_entities hits invented /api/entities; also invents /api/states/<id>/history and /api/config/device_registry; /api/states works |
| 2 | pass | 5 tools | 28 | 38.8 | 37 | 7/18 | 16.6 | 256k | 20 | llama.cpp 0.4 |  |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 1 | no | 12/12 | 22.4 | 23 | It sent one probe session with ten numbered calls giving exact arguments and the field it needed from each, asking for isError, the verbatim JSON text and a closing summary block; it built REST ground truth first, noticed that the probe's pasted state=off block was internally … |
| 3G | 14/14 | 2 | no | 12/12 | 64.1 | 13 | Tiel Coder focus wave, run 1 of test 3 with the given server. It took REST ground truth first, then sent one probe brief of eight numbered calls with exact arguments ("Call tool `list_entities` with arguments {\"domain\":\"light\",\"limit\":200}"), asking for raw JSON and "If … |
| 3G | 13/14 | 1 | no | 12/12 | 58.2 | 16 | Tiel Coder focus wave, run 2 of test 3 with the given server. It took REST ground truth first, then sent one probe brief of twelve numbered calls with exact arguments ("Call `list_entities` with arguments {\"domain\":\"light\",\"state\":\"on\"}. Report full structuredContent. I … |
| 3G | 6/14 | 2 | no | 12/12 | 70.5 | 9 | Tiel Coder focus wave, run 3 of test 3 with the given server. Server unchanged. Two specific briefs asked for full structuredContent and exact fields. The first probe misreported light off as 55; a second brief demanded the raw list_domains JSON, which says off 38 and matches … |
| 3O | 14/14 | 4 | fixed: 5 tools, 28 tests pass | 12/12 | 38.4 | 28 | Its first probe found the list tools failing ("expected record, received array on structuredContent"); after confirming it by running the binary directly it wrapped the lists in objects and moved domain and entity_id filtering client-side, then a targeted probe showed the probe … |
| 3O | 9/14 | 8 | fixed: 5 tools, 22 tests pass | 10/12 | 58.3 | 38 | Tiel Coder focus wave, run 1 of test 3 with its own server (from wb-retry-tiel-q4kxl). REST first, where it saw that /api/services gives a dict per domain while the server expects an array. First brief: seven numbered steps with arguments, one JSON object back, errors as "ERROR … |
| 3O | 14/14 | 2 | fixed: 5 tools, 22 tests pass | 12/12 | 75.8 | 12 | Tiel Coder focus wave, run 2 of test 3 with its own server. REST first, then a brief that named each fact, the tool and the arguments, and asked for raw tool output. It found list_services always empty because /api/services returns a dict, and that the probe host rejects array … |
| 3O | 13/14 | 2 | fixed: 5 tools, 22 tests pass | 11/12 | 67.3 | 11 | Tiel Coder focus wave, run 3 of test 3 with its own server. Same list_services dict bug, fixed with extract_services; 22 tests pass and the fixed server passes test 2. It did not wrap array structuredContent, so the second probe still failed on both list tools and the list facts … |

_Generated from the bake-off results on 2026-10-14._
