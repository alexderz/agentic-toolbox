# Local models on Titan: which to run, and how

- Source: model bake-off on Titan, wave A (test 1), 2026-09-30 to 2026-10-02.
  Harness and raw results: `~/src/grok-bot-perm/model-bakeoff` on Pluto
  (`results-wave-a/REPORT.md`, `grades.tsv`, `matrix-wave-a.tsv`). Titan host
  config: `alexderz/house-infra` `hosts/titan/`.
- Distilled: `2026-10-03`
- Live docs win: the live `llama-swap.yaml` on Titan
  (`/home/alex.derzhi/ai/config/llama-swap.yaml`) and the bake-off report.
  When this note and a fresh measurement disagree, trust the measurement.

## What it is

What we have measured about running open-weight models on one RTX 3090
(24 GB) for agentic coding: which models produce working code, how fast each
one runs, and the exact llama.cpp settings that got there. It sorts models
into two working tiers: fast models that live entirely (or almost) in VRAM,
and smarter models that spill experts to system RAM and run 4 to 7 times
slower.

## When to read

- Choosing a local model for a coding or agent task.
- Adding a model to llama-swap, or changing context size, KV cache type or
  expert offload.
- Diagnosing a model that loads but never answers.

Hermes on Pluto does **not** use Titan. Its Titan provider is disabled on
purpose (house-infra `hosts/pluto/claw.py`, `HERMES_USE_TITAN = False`, decided
2026-10-02). Nothing here is a reason to turn it back on. That is the
operator's call.

## The machine

- Titan: RTX 3090 24 GB, 125 GB RAM, Bazzite (home is `/var/home/alex.derzhi`).
  LAN 10.69.2.62, WireGuard 10.8.0.7.
- Weights live on Saturn's NAS and reach Titan over read-only NFS at
  `~/ai/models` (mounted into containers as `/models`). New weights are
  downloaded on Saturn into `/srv/nas/models`, never on Titan.
- llama-swap serves one model at a time. LAN endpoint `:8080` (Caddy,
  `read_timeout 0`), admin `:8081`. `healthCheckTimeout: 2400`, no `ttl`.
  Asking for a different model unloads the current one; a cold load of a
  large offloaded model takes minutes.
- The bake-off edits `llama-swap.yaml` live. Its entries can carry the last
  variant tested rather than the best one. The gated row in
  `matrix-wave-a.tsv` is the setting that was measured.

## Five rules that decide everything

1. **Speed is set by how much of the model sits in VRAM.** Parameter count
   matters far less. Every model that fits on the GPU ran at 25 to 100 tok/s;
   every model that pushes experts to system RAM ran at 3 to 10 tok/s,
   whatever its size. Pick a tier first, then a model.
2. **A model with experts offloaded (`-ncmoe N`) must also have `-lm none`.**
   Without it llama.cpp memory-maps the experts, reports "loaded" in seconds,
   then page-faults tens of GB off NFS (about 180 MiB/s) during the first
   request. The process sits in state `D` with the GPU idle, the client's
   300-second stream timeout fires, and the agent retries forever. `-lm none`
   reads the weights into RAM at load time. Titan's `hosts/titan/status`
   fails if any `-ncmoe` entry lacks it (house-infra `ac93ba2`).
3. **KV cache size comes from the layers that actually cache attention.**
   Count `attn_k` tensors in the GGUF, not `block_count`. Qwen3.8 Flash-Next
   has 12 caching layers out of 48 (the rest are linear attention), so f16 KV
   costs about 28 KiB per token and the full 262,144 context fits.
4. **f16 KV costs VRAM, not speed.** At the same offload, f16 and q8_0 KV
   measured the same throughput. f16 is the better cache; use it when the VRAM
   is there, and drop to q8_0 when q8_0 is what lets more layers stay on the
   GPU. On offloaded models, VRAM spent on KV is VRAM taken from experts:
   about 1,300 MiB per expert layer at IQ4_XS.
5. **Fill the card.** Raise `-c` towards the model's native context until
   VRAM is nearly full, then bring expert layers back with what is left.
   Hybrid-attention models (Qwen3.6/3.8 MoE, Tiel) reach their full 262k this
   way. `tools/fill_vram.py` in the bake-off repo does the search with real
   loads; aim for 23.6 to 23.8 GB of 24.

Pre-warm weights into the page cache before a timed run:
`cat <model files> > /dev/null` on Titan.

## Tier 1: fast, full GPU (25 to 100 tok/s)

Default choice for interactive and agent work. All passed test 1 at 5/5
except where noted.

| Model (llama-swap id) | tok/s | Test 1 | Settings that were measured |
| --- | --- | --- | --- |
| `tiel-coder-35b` (UD-IQ4_XS, MoE 3B active) | **101** | 5/5, 55 tests | `-ngl 999 -c 262144 -ctk f16 -ctv f16`, 23.6 GB, nothing offloaded |
| `qwen3.6-35b-a3b` (UD-Q4_K_M, MoE 3B active) | 57 | 5/5, 52 tests | `-ngl 999 -ncmoe 12 -c 131072 -ctk f16 -ctv f16 -lm none`, 19.8 GB |
| `qwen3.8-27b` (UD-Q4_K_M, dense) | 33 | 5/5, 55 tests | `-ngl 999 -c 131072 -ctk q8_0 -ctv q8_0`, 20.7 GB |
| `qwen3.6-27b` (Q4_K_M, dense) | 31 | 5/5, 65 tests | `-ngl 999 -c 131072 -ctk q8_0 -ctv q8_0`, 21.4 GB |
| `q38-27b-cyber` (IQ4_XS, dense, uncensored) | 24 | 5/5, 39 tests | `-ngl 999 -c 131072 -ctk q8_0 -ctv q8_0` |

Notes:

- `tiel-coder-35b` is the default: the fastest model that writes working
  code, fully on the GPU at its native 262k context, 13 minutes for the
  task. The Q6 builds (`tiel-coder-35b-q6`, `cyber-tiel-coder-35b`) must
  leave 20 expert layers in RAM at 262k and run at 43 to 44 tok/s with no
  better result; use IQ4_XS.
- `qwen3.6-35b-a3b` was measured at 131k with 12 expert layers in RAM
  (57 tok/s). It has not been re-tuned with the card filled.
- The two dense 27B models are the steadiest full-GPU choices. The dense
  Qwen3.8 is the newer of the two.
- `q38-27b-cyber` is the pick for security testing of our own code, where a
  stock model refuses.
- `qwen3-coder-30b-a3b` passed 5/5 at 24 tok/s with `-ncmoe 26`, but wrote
  thin code (7 subcommands, one failing test). The 35B-A3B above is better
  on every measure.

Fast and **not** recommended:

| Model | tok/s | Why not |
| --- | --- | --- |
| `bonsai2-27b` / `bonsai2-27b-pq2` (ternary) | 41 / 47 | Invents APIs. 2/5, then 4/5 on a rerun at 254k: the core reads worked, but 11 of its 14 API paths do not exist. Fast, confident, wrong. |
| `glm-4.7-flash` | 35 to 62 | 2/5 then 5/5 at 203k. Inconsistent; left a failing test. |
| `devstral-small-2-24b` | 26 to 33 | 2/5 then 5/5 at 205k. Inconsistent; left a failing test. |
| `nemotron3-nano-30b` | 83 to 91 | 2/5 twice. Quits within minutes. Excluded. |
| `nanbeige4.2-3b` | 16 to 20 | 2/5 then 1/5. Excluded. |
| `qwen3vl-8b` | 40 | 0/5: did not import, 16 undefined names |
| `jan-nano-128k` | 48 | 1/5: wrote no files, tried to install its own harness |

## Tier 2: smartest, slow, experts in RAM (3 to 10 tok/s)

For long unattended jobs where quality matters more than wall time. Expect a
multi-hour run for a task Tier 1 finishes in under an hour.

| Model (llama-swap id) | tok/s | Test 1 | Settings that were measured |
| --- | --- | --- | --- |
| `qwen3.8-flash-next-unpruned` (GSQ-RCO IQ3_S) | 8.3 | 5/5, 89 tests | `-ngl 999 -ncmoe 42 -c 131072 -ctk f16 -ctv f16 -lm none` |
| `swift15-flash-next` (GSQ-RCO IQ3_XXS) | 7.1 | 5/5, 96 tests | `-ngl 999 -ncmoe 42 -c 131072 -ctk f16 -ctv f16 -lm none`, 16.4 GB |
| `orcarouter-fn-uncensored` (Flash-Next, uncensored) | 8.8 | 5/5, 54 tests | offloaded, f16 KV |
| `qwen3.8-flash-next-coder` | 9.9 | 5/5, 24 tests | `-ngl 999 -ncmoe 26 -c 131072 -ctk f16 -ctv f16 -lm none`, 20.9 GB |
| `nemotron3-super-120b` (UD-Q4_K_M) | 8.5 | 5/5, no tests written, 5 subcommands | `-ngl 999 -ncmoe 77 -c 131072 -ctk f16 -ctv f16 -lm none`, 20.5 GB |

- `qwen3.8-flash-next-unpruned` wrote the best code of the whole run in a
  blind review (8/10; next best 7/10 for `swift15`). It is the model to keep
  current.
- Flash-Next at f16 fits the full 262,144 context at `-ncmoe 40`
  (22.4 GB, 19 tok/s on a short prompt). Use 131,072 unless the task needs
  more; the freed VRAM keeps more experts on the GPU.
- `glm-4.5-air` (3 tok/s at `-ncmoe 55`) is too slow to be worth it here.
- `qwen3-235b-a22b` does not run: Q4_K_M is 132 GiB against 125 GB of RAM,
  and offloaded models must load eagerly (rule 2).

### In between: Flash-Next on SGLang

`flashnext` runs Qwen3.8 Flash-Next as EXL3 3.05 bpw under SGLang (Strata
image) with a GPU expert cache, as a podman container behind llama-swap. It
ran at 44 tok/s, scored 4/5, and produced the largest submission of the run
(242 tests, 25 subcommands). It gives near-Tier-1 speed on a Tier-2 model.
It is a different engine with its own failure modes; see the Titan config
for the image tag (`localhost/strata:v0.1.30-sm86` is built).

## How models were graded

- One task: a Python command-line tool for the Home Assistant REST API,
  built by OpenCode in a sandboxed container against a read-only replay of
  Pluto's Home Assistant. Five checks run by executing the result: entry
  point and help, real reads, bad input, bad auth, no crash; plus the
  model's own tests.
- **n=1 per model.** One model has swung 5/5, 5/5, 2/5 on identical
  settings. A one- or two-check difference is noise. Read the scores as
  works / partly works / does not work.
- tok/s is decode throughput averaged over the whole agent run, from event
  timestamps. It includes prompt processing and is lower than a short-prompt
  benchmark.
- Tests 2 (build an MCP server) and 3 (use one) have not run yet.

## Unknown

- Whether Tier 1 rankings hold on tests 2 and 3.
- How the wave A models (run at 131k) score and run with the card filled.
- Whether more context changes quality at all: batch 2 reruns changed both
  context and run, so the two effects cannot be separated.
- Quality cost of q8_0 KV against f16 on long contexts: not measured.

## Do not

- Do not point Hermes at Titan. The operator disabled it.
- Do not download weights on Titan; `~/ai/models` is read-only NFS.
- Do not offload experts without `-lm none`.
- Do not hand-edit Titan's host config outside house-infra `hosts/titan/`;
  Titan's own agent owns it.
- Do not treat a single test-1 score as a ranking.
