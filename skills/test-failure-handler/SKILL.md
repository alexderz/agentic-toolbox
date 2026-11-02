---
name: test-failure-handler
description: Open the failing log, find the cause, and fix it inside the accepted harness without editing prove lines or the env block.
---

# Test failure handler

Use on the first test-failure prompt. Open the log path given in the prompt. Find the first failure. Load `debug` and name the root cause before changing code.

When the cause is in product code, write a failing test (`tdd`), fix that cause, and commit. Add one `## Corrected errors` line to `state.md`. When an approach failed, add one `## Do not repeat` line.

Edit only the product code the root cause names. Never edit proving commands, `groom.md`, or the LLD env block. Use only the accepted `json sdlc-env` harness. Never add a harness, dependency, or toolchain, and never install or start a new service. Leave the ticket where it is. Never move the ticket. A failure that needs a new harness stops as `needs_input` with choice `operator` and an `env-capability` check. Stop there. Never propose or apply an environment edit to get past that stop.

Use only the accepted harness. A known red baseline stays evidence. Keep the failing test. Never delete, skip, weaken, or relabel a test to go green. Do not put transcripts, prompts, secrets, or `passEnv` values in `state.md` or `result.md`.

Submit the typed result before prose.

## Related

- [Debug](../debug/SKILL.md)
- [Stage results](../../docs/sdlc/stage-result.md)
