# History

The tests changed as we learned. Most changes came from a failure that
turned out to be the harness, not the model. This page lists each change
and the reason for it.

| Date | Change | Why |
| --- | --- | --- |
| 2026-09-23 | **Round 1.** One prompt (a Python CLI for the Home Assistant API), the Pi agent, llama.cpp only, 17 setups. Scored by API endpoints touched and whether the code compiled. | A first look at which local models write working code at all. |
| 2026-09-27 | **Tests 2, 3A, and 3B.** OpenCode in a container against a recorded Home Assistant. Test 2 builds a Rust MCP server; test 3A and 3B describe the house through your own server or someone else's. | Separate building a tool from using one. |
| 2026-09-29 | **Uncensored cohort.** Three uncensored Flash-Next variants and the stock model through the MCP test. | Security testing of our own software needs models that don't refuse. |
| 2026-09-30 | **Harness fixes.** Experts offloaded to RAM were memory-mapped and page-faulted off the network during the first request, so offloaded models produced no output. Fixed with eager loading (`-lm none`); also a 3-hour case cap, longer client timeouts, and guaranteed result records. | Several early failures were the harness. |
| 2026-10-01 | **Wave A.** Test 1 graded by running the tool (five checks plus the model's own tests). Context and offload tuned per model with real loads. | Counting endpoints in the source credited help text and invented APIs. |
| 2026-10-03 | **Wave B.** Test 2 graded by driving the server as a real MCP client; every failure verified by hand. | Test 1 no longer separated the models. |
| 2026-10-04 | **Client settings.** Context margin of `max(10%, 16k)` and a thinking budget on every engine. | Runs died on context overflow, and on single thinks that used the whole reply. |
| 2026-10-04 | **New engines.** vLLM for the dense 27B; SGLang and Strata for Flash-Next. | The same weights ran 2-5x faster on a better-suited engine. |
| 2026-10-05 | **llama.cpp 0.6, long-horizon runs, small-window setups.** An A/B of llama.cpp 0.6 against 0.4; 8-hour runs with Qwen's long-horizon sampling; 57-64k vLLM setups with OpenCode and Pi. | llama.cpp 0.6 is 2.5-4x faster on Flash-Next; the uncensored Flash-Next finished test 2 for the first time. |
| 2026-10-06 | **Uncensored round.** A new uncensored 27B, and 8-hour test-2 runs for the slower uncensored Flash-Next variants. | Find the smartest uncensored model, not only the fastest. |
