# Method

This page describes how models are tested and how to read the numbers.

## The machine

| Part | Value |
| --- | --- |
| GPU | NVIDIA RTX 3090, 24 GB (compute capability 8.6) |
| System RAM | 125 GB |
| CPU | AVX2, no AVX-512 |
| Weights | Read from a NAS over the network; the first load streams at roughly 180-280 MB/s |
| Router | llama-swap: one model loaded at a time, each engine as a separate process or container |
| Agent | OpenCode in a sandboxed container; some runs use the Pi agent |

## The tests

Every test gives the agent one task and no guidance. The agent runs in a
container with no network access except the model server and a read-only
replay of a real Home Assistant installation (434 entities). The result is
graded by running it, not by reading it.

### Test 1: a command-line tool

The task is to write a Python command-line tool for the Home Assistant REST
API. The grader runs the tool in a sandbox and checks five things:

1. It has an entry point and prints help.
2. It reads real data from the API.
3. It handles bad input.
4. It handles a bad token.
5. It doesn't crash.

The grader also runs the model's own tests and counts subcommands.

### Test 2: an MCP server

The task is to build a Model Context Protocol (MCP) server in Rust that
exposes the same Home Assistant API to an agent. The MCP specification is
on disk. The grader builds the server and talks to it as a real MCP
client: `initialize`, `tools/list`, and a real `tools/call` that must return
data from the replay. Every failure is checked by hand and explained in the
model's card.

| Result | Meaning |
| --- | --- |
| pass | Builds, answers `initialize`, lists tools, and a tool call returns real data. |
| partial | Builds and answers a client in part (for example, tools without `initialize`, or tools that return no data). |
| fail | Does not build, or nothing a client can use. |

Test 2 separates models that test 1 cannot: invented API endpoints, broken
handshakes, and networking bugs only show when a client drives the server.

### Test 2T: trust the docs

Test 2 with a short Home Assistant REST reference added to the workspace,
introduced as written for a slightly older version. Most entries are
correct; three are deliberately wrong (`GET /api/entities`,
`GET /api/entities/<entity_id>`, and `GET /api/services/list`; the real
endpoints are `/api/states`, `/api/states/<entity_id>`, and `/api/services`).
Besides the normal test-2 grade, each run gets a trust verdict from the
replay's access log and the shipped code:

| Verdict | Meaning |
| --- | --- |
| tested | Tried a planted endpoint, got a 404, and shipped code that uses only the real ones. |
| avoided | Never tried a planted endpoint; shipped only the real ones. |
| hedged | Shipped code that tries a planted endpoint and falls back to the real one. |
| trusted | Shipped code that uses a planted endpoint and never the real one. |

This came from an accident: `/api/entities` is not a Home Assistant
endpoint (entities are listed through `/api/states`; the entity registry is
only on the WebSocket API), yet six runs used it with no prompt or document
mentioning it. Some models switched to `/api/states` after the 404; one
built its whole tool on invented paths.

### Long-horizon runs

Slow models get an 8-hour cap and the sampling Qwen uses for its own
long-horizon coding evaluation: temperature 1.0, top-p 0.95, top-k 20,
min-p 0, and a 26k-token thinking budget.

## Settings

Every model ran at its own best fit on the card, found by real loads:

- **Context** (`-c`) is raised towards the model's native limit until VRAM
  is nearly full.
- **Expert offload** (`-ncmoe N` in llama.cpp) keeps the experts of `N`
  layers in system RAM for mixture-of-experts models. It is always used with
  `-lm none`, so the weights load into RAM up front instead of page-faulting
  over the network during the first request.
- **KV cache** is f16 or q8_0. f16 costs VRAM, not speed.
- **Thinking budget** is `min(24000, reply cap − 6000)` tokens on every
  engine, so a long think ends with room left to answer.
- **Client context** tells the agent the model's limit minus
  `max(10%, 16k)`, because the agent decides when to compact from the
  previous turn's size.

## How to read the numbers

- **This is a living snapshot, not an apples-to-apples benchmark.** The
  harness, grading, engines, and client settings changed as we learned; see
  [History](history.md). Rows from different eras are not directly
  comparable.
- **One run per row.** One model scored 5/5, 5/5, and 2/5 on identical
  settings. A one- or two-check difference is noise. Read results as pass,
  partial, or fail.
- **tok/s** is generation throughput averaged over the whole agent run:
  output and reasoning tokens divided by wall time. It includes prompt
  processing, tool time, and compaction, so it is lower than a short-prompt
  benchmark and depends on the task.
- **Uncensored models** run the same coding tasks as every other model.
