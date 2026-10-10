# Gemma 4 26B-A4B

**Status:** Tested

| | |
| --- | --- |
| Family | Gemma 4 |
| Source | google/gemma-4-26b-a4b |
| Architecture | MoE, 26B / 4B active |

## Summary

Gemma 4 MoE; on vLLM with AWQ and a draft model.

## Verdict

91-153 tok/s but thin (3 tools). On llama.cpp it looped inside tool-call arguments.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Gemma 4 26B-A4B · llama.cpp, all on GPU, 262k context | llama.cpp 0.4 | Q4 | 256k | – | 164.5 |
| Gemma 4 26B-A4B · vLLM, AWQ, draft model | vLLM | AWQ | 256k | – | 117.3 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 7 | 99.7 | 2 | 0 | 0.0 | 256k | – | llama.cpp 0.4 | 4 subcommands |
| 1 | pass | 5/5 checks | 7 | 112.0 | 1 | 0 | 0.0 | 256k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 8 | 140.8 | 1 | 0 | 0.0 | 256k | – | llama.cpp 0.4 | 2 subcommands |
| 1 | pass | 5/5 checks | 9 | 108.1 | 1 | 0 | 0.0 | 256k | – | llama.cpp 0.4 | 3 subcommands |
| 1 | pass | 5/5 checks | 6 | 117.3 | 2 | 0 | 0.0 | 256k | – | vLLM | 8 subcommands |
| 1 | fail | 1/5 checks | 6 | 90.0 | 2 | 0 | 0.0 | 256k | – | vLLM | 3 subcommands |
| 2 | pass | 3 tools | 2 | 118.4 | 3 | 4/6 | 9.6 | 256k | – | llama.cpp 0.4 |  |
| 2 | partial | 3 tools | 6 | 89.6 | 10 | 12/14 | 38.8 | 256k | – | llama.cpp 0.4 | baseline without MTP: list_entities requests a path outside /api (replay: 404 'only /api paths are served') |
| 2 | fail | 0 tools | – | 152.7 | 7 | 3/3 | 9.0 | 256k | – | llama.cpp 0.4 | does not build (E0599); run ended on a 32,000-token output step with no text after cargo test -- runaway generation; thinking ON |
| 2 | fail | 0 tools | – | 106.1 | 12 | 0 | 0.0 | 256k | – | llama.cpp 0.4 | does not build (E0119); 2 runaway steps, both DEGENERATE LOOPS INSIDE TOOL-CALL ARGUMENTS ("at_the_end_of_the_file..." x157, "server_side_side_wrapper(" x764), not thinking: the 24k thinking budget cannot catch it. Gemma 26B llama.cpp, temp 1.0 min_p 0 |
| 2 | partial | 3 tools | 5 | 164.5 | 6 | 5/7 | 12.3 | 256k | – | llama.cpp 0.4 | init fails (checked by hand): InitializeResult serializes protocol_version in snake case (no serde rename to protocolVersion) and has no serverInfo, so clients reject the handshake; 3 tools defined |
| 2 | fail | 0 tools | – | 174.4 | 3 | 2/2 | 16.5 | 256k | – | llama.cpp 0.4 | Test 2T (planted docs), trust: **trusted**. does not build (checked by hand): Rust syntax error (unexpected token `.`) and an undefined type |
| 2 | pass | 3 tools | 0 | 91.4 | 4 | 3/6 | 6.0 | 256k | – | vLLM |  |
| 2 | fail | 0 tools | – | 90.1 | 3 | 1/2 | 2.1 | 256k | – | vLLM | Test 2T (planted docs), trust: **trusted**. TEST 2T (planted docs): FAIL, does not build (E0599: no method list_entities on a mock it was refactoring). Quit on its own after 3 min (12k tokens out, 90 tok/s) saying 'my next steps are ...'. Trust: TRUSTED (code calls the planted … |
| 2 | pass | 3 tools | 3 | 111.7 | 5 | 1/3 | 18.0 | 256k | – | vLLM |  |
| 2 | partial | 4 tools | 5 | 93.8 | 7 | 2/6 | 33.6 | 256k | – | vLLM | Test 2T (planted docs), trust: **hedged**. tool_call fails (checked by hand): tools/call list_entities gets no reply with id 3; init and tools/list work |

_Generated from the bake-off results on 2026-10-10._
