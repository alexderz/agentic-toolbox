# Cyber-Tiel-Coder-35B-A3B

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Tiel Coder 35B |
| Source | Cyber-Tiel-Coder-35B-A3B UD-Q6_K_XL |
| Architecture | MoE, 35B / 3B active |

## Summary

A security-focused tune of Tiel-Coder, 6-bit, 20 expert layers in RAM.

## Verdict

Test-2 full pass (6 tools, 35 tests) at 24.5 tok/s. llama.cpp 0.6 gave no speed gain on it.

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Cyber-Tiel-Coder-35B 6-bit · llama.cpp, 20 expert layers in RAM | llama.cpp 0.4 | Q6_K_XL | 256k | 20 | 44.3 |
| Cyber-Tiel-Coder-35B 6-bit · llama.cpp 0.6, 20 expert layers in RAM | llama.cpp 0.6 | Q6_K_XL | not run yet | | |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 53 | 44.3 | 14 | 1 py | 0.8 | 256k | 20 | llama.cpp 0.4 | 6 subcommands |
| 2 | pass | 6 tools | 35 | 24.5 | 82 | 12/24 | 29.9 | 256k | 20 | llama.cpp 0.4 |  |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 6 | no | 12/12 | 24.9 | 21 | It built REST ground truth first, then sent six probe sessions: a wiring check, four parallel one-tool probes with exact arguments asking for the verbatim structuredContent and errors, and a re-probe with limit 1 after the server's 24,000-character text cap cut off the 124-row … |
| 3O | 14/14 | 5 | fixed: 6 tools, 38 tests pass | 12/12 | 34.4 | 21 | Running its own binary directly showed list_services failing on this installation's array-shaped /api/services; two parallel probes then found list_entities rejected ("expected record, received array" on structuredContent) and version missing from the get_config text. It wrapped … |

_Generated from the bake-off results on 2026-10-10._
