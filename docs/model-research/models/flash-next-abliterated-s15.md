# Flash-Next Abliterated s1.5

**Status:** Tested · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | weight-abliterated Flash-Next, IQ4_XS |
| Architecture | MoE, 125B total / 6B active |

## Summary

Flash-Next with refusal directions removed from the weights (strength 1.5). Text only.

## Verdict

Passed the long-horizon test 2 on llama.cpp 0.6 (6 tools, 20 tests, 120 minutes, 10.4 tok/s) and test 1 (5/5) on llama.cpp 0.4. Slightly behind Heretic2, which built one more tool at 40% higher speed. In test 3 it handled the known-good server well (14/14 facts, rubric 12/12). On its own server it found and fixed a real defect (three tools returned a bare string or array where an object was declared) and ended with 14/14 facts, but it took 128 minutes, most of it the probe counting entities by hand, and it accepted a final probe answer that came from no new server calls (rubric 8/12).

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Abliterated s1.5 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4_XS | 128k | 42 | 9.6 |
| Flash-Next Abliterated s1.5 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4_XS | 256k | 39 | 10.4 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 26 | 9.6 | 119 | 3 py | 4.5 | 128k | 42 | llama.cpp 0.4 | 8 subcommands |
| 2 | pass | 6 tools | 20 | 10.4 | 120 | 10/21 | 20.3 | 256k | 39 | llama.cpp 0.6 | [tests regraded 2026-10-07: 19/0 -> 20/0, grader now sums every cargo test target] Flash-Next Abliterated s1.5 on llama.cpp 0.6 (-ncmoe 39, 262k, -fit off), long-horizon settings (8 h cap): FULL PASS, 6 tools, 19 tests, 120 min, 10.4 tok/s, 0 compactions, ended on its own |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 1 | no | 12/12 | 6.2 | 20 | It built REST ground truth first, then sent one probe session with eight numbered calls giving exact arguments and the fields to report raw, pagination to the end, state-filter cross-checks and errors quoted; all 14 facts matched, a second REST pull confirmed them, and it … |
| 3O | 14/14 | 1 | fixed: 6 tools, 20 tests pass | 8/12 | 3.5 | 127 | Five briefs resumed in one probe session (hence 1 counted session), 93 of 128 minutes spent in the probe hand-counting 434 entities at 3.5 tok/s; built REST ground truth first and chased every mismatch (123 and 113 vs 124 unavailable, 7 vs 3 lock services), also by driving the … |

_Generated from the bake-off results on 2026-10-10._
