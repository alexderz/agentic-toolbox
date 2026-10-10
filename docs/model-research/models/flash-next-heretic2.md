# Flash-Next Heretic2

**Status:** Recommended · Uncensored

| | |
| --- | --- |
| Family | Qwen3.8 Flash-Next |
| Source | Heretic2 (automated abliteration) of Flash-Next, IQ4XS-NGQ4 |
| Architecture | MoE, 125B total / 6B active |

## Summary

Flash-Next with refusals removed by Heretic's automated abliteration. Vision-capable.

## Verdict

Fastest of the big uncensored models. On llama.cpp 0.6 with long-horizon settings it passed test 2 (7 tools, 33 tests) in 120 minutes at 14.6 tok/s: about twice as fast as the Orcarouter fine-tune on the same engine, which built more (8 tools, 54 tests). Test 1 passed (5/5) on llama.cpp 0.4. In test 3 it handled the known-good server perfectly (14/14 facts, rubric 12/12) but misjudged its own: that server returns data only as structured content with a one-line text summary, so its probe saw 5 of 14 facts, and it still declared the server correct (rubric 8/12).

## Variants we ran

Each variant is one engine and settings combination. Context and expert offload come from its best run.

| Variant | Engine | Quantization | Context | Expert layers in RAM | Best tok/s over a run |
| --- | --- | --- | --- | --- | --- |
| Flash-Next Heretic2 · llama.cpp, experts in RAM | llama.cpp 0.4 | IQ4XS-NGQ4 | 128k | 42 | 8.7 |
| Flash-Next Heretic2 · llama.cpp 0.6, experts in RAM | llama.cpp 0.6 | IQ4XS-NGQ4 | 256k | 40 | 14.6 |

## Results

Test 1 builds a Python CLI and is graded by running it (5 checks). Test 2 builds a Rust MCP server and is graded by connecting to it as a client; *tools* is how many tools a client sees. *Failed builds* and *errors per 1k lines* show how hard the model fought the compiler on the way. One run per row. See [Method](../method.md).

| Test | Result | Score | Own tests | tok/s | Minutes | Failed builds | Errors per 1k lines | Context | Expert layers in RAM | Engine | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | pass | 5/5 checks | 25 | 8.7 | 123 | 0 | 0.0 | 128k | 42 | llama.cpp 0.4 | 12 subcommands |
| 2 | pass | 7 tools | 33 | 14.6 | 120 | 14/22 | 28.3 | 256k | 40 | llama.cpp 0.6 | [tests regraded 2026-10-07: 18/0 -> 33/0, grader now sums every cargo test target] Flash-Next Heretic2 on llama.cpp 0.6 (-ncmoe 40, 262k, -fit off), long-horizon settings (8 h cap): FULL PASS, 7 tools, 18 tests, 120 min, 14.6 tok/s over the run (twice the orcarouter run on the … |

## Test 3: using an MCP server through a subagent

The model gets an MCP server's source and a probe subagent whose only tools are that server's, must get 14 facts through the probe, check them against the REST API and fix the server if it is wrong. *3G* is a known-good server, *3O* the model's own from test 2. The rubric (out of 12) scores how it briefed and checked the probe.

| Server | Facts | Probes | Changed the server | Rubric | tok/s | Minutes | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3G | 14/14 | 1 | no | 12/12 | 5.5 | 19 | One probe session with eight numbered calls naming exact arguments and fields, the tool's own matched/returned/next_cursor plus the probe's own tally, a list_domains cross-check and errors quoted verbatim; then built REST ground truth in one curl and Python pass and matched all … |
| 3O | 5/14 | 2 | fixed: 7 tools, 33 tests pass | 8/12 | 10.3 | 44 | Two probe sessions with good numbered briefs (exact definitions, errors quoted verbatim, final 14-fact table) and a full REST ground truth. Its own server returns data only in structuredContent with a one-line text summary, so the probe saw just "434 entities", "light: 52 … |

_Generated from the bake-off results on 2026-10-10._
