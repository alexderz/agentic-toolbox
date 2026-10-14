# Engines

The engine moves a model within its speed tier by 2 to 5 times. This page
says which engine to use for which kind of model, and the settings that
matter for each.

## Rule of thumb

- If the model fits on the GPU, use **vLLM**.
- If a mixture-of-experts model must keep experts in system RAM, use
  **llama.cpp 0.6**, or **Strata** or **SGLang** for Qwen3.8-Flash-Next.
- Speculative decoding (MTP or a draft model) pays off only when the model
  is GPU-resident. With experts in RAM it gave nothing.

## vLLM

We use the HyperQwen build of vLLM for Qwen3.8-27B. It ran 2-4x faster
than llama.cpp over whole agent runs, thanks to prefix caching and MTP
drafting.

| Setup | Context | Result |
| --- | --- | --- |
| MTP drafts, FP8 KV | 150k | The default. About 70 tok/s over a run, full passes on both tests. |
| DFlash2 drafts, 4/2-bit KV | 240k | Same quality at 240k, about half the speed under load. Use it only when a job needs more than about 150k. |
| DFlash2 drafts | 64k | About 97 tok/s, but the agent compacts constantly and one test overflowed the context. |
| DFlash2 15-token drafts | 57k | About 95 tok/s; one test compacted 55 times and took 6x as long. |

vLLM needs a per-request thinking budget (`thinking_token_budget`) and
`--reasoning-config` on the server.

## llama.cpp

llama.cpp runs anything with a GGUF, including models whose experts sit in
system RAM.

| Setting | Why |
| --- | --- |
| `-ncmoe N` with `-lm none` | Experts of `N` layers in RAM, loaded eagerly. Without `-lm none` the first request page-faults the weights and stalls. |
| `-fit off` (0.6) | The automatic fit keeps 1 GiB spare and aborts when `-ngl` is set by hand. |
| `--reasoning-budget` | Caps thinking; set it inside the reply cap. |
| `--chat-template-kwargs '{"enable_thinking":true}'` | Gemma-style templates think only when asked. |
| `--spec-type draft-mtp` | MTP drafting for models that ship MTP layers (0.6). |

### llama.cpp 0.6 against 0.4

A short-prompt probe at 49k context, thinking off, temperature 0. Real agent
runs average lower.

| Model | 0.4 decode | 0.6 decode | 0.6 with drafting | Prefill 0.4 → 0.6 |
| --- | --- | --- | --- | --- |
| Qwen3.8-Flash-Next (experts in RAM) | 2.2 tok/s | 8.9 tok/s | – | 136 → 569 tok/s |
| Orcarouter Flash-Next Uncensored (experts in RAM) | 5.3 tok/s | 13.1 tok/s | – | 295 → 486 tok/s |
| Qwen3.8-27B Cyber (all on GPU) | 44.9 tok/s | 45.1 tok/s | 82.2 tok/s with MTP | about the same |
| OrcaSAQ-2-Cyber-27B (all on GPU) | 85.5 tok/s | 83.2 tok/s | 412 tok/s on copy-heavy output with n-gram drafts | about the same |
| Cyber-Tiel-Coder-35B (20 expert layers in RAM) | 52.3 tok/s | 50.5 tok/s | – | about the same |

In a real 8-hour agent run, the Orcarouter model on 0.6 averaged 7.6 tok/s:
much better than 0.4 (which could not finish) but far below the probe.
Measure on your own workload.

## SGLang

SGLang with an EXL3 3-bit quant and a GPU expert cache ran
Qwen3.8-Flash-Next at 36 tok/s over a run and built the best test-2 server
of all runs. It handles one session at a time; it crashed under several.

## Strata

Strata runs the Qwen3.8-Flash-Next family (GSQ-RCO quants) with a hot-expert
cache in VRAM: 30-45 tok/s decode, 21-24 tok/s over a whole run.

- Set `reasoning_budget_tokens` in its model config. It is off by default,
  and the 1.6-bit coder looped without it.
- Add the host name your proxy uses to `allowed_hosts`. Its DNS-rebinding
  guard returns 403 to any other name.
- On 0.1.42, set `STRATA_PCIE_FRAC_DEFAULT=old`. With the release default,
  long answers decoded at about 48 tok/s and large prompts were read at
  about 1,200 tok/s; with the older PCIe share, 95 and 2,000 (two rounds in
  opposite orders after a warm-up). Turning tail skip off helps decode as
  much but not reading; turning the prefill CPU share off reads fastest and
  decodes slowest.
- Warm it up before timing anything. The first request after a start is
  many times slower.

## ExLlamaV3 (TabbyAPI)

ExLlamaV3 1.6.1 behind TabbyAPI runs Qwen3.8-27B from EXL3 4.00 bpw weights, unpatched, with the model's own
MTP head or with the DFlash2 drafter. Short prompts, thinking off, temperature 0, three rounds on the 3090
at a 16k window (2026-10-13; the no-drafting row is one round):

| Setup | Code | Prose | Structured | Window that fits, 8-bit cache |
| --- | --- | --- | --- | --- |
| DFlash2 drafter | 158 tok/s | 73 | 181 | 98k |
| Own MTP head | 116 tok/s | 70 | 128 | 196k |
| No drafting | 42 tok/s | 42 | 42 | – |

Served at a 196k window with MTP (a later run) it is slower than vLLM with MTP at 150k on every point we
measured (115 against 127 tok/s on
short code, 72 against 85 at 141k of context, and it reads prompts at about the same 650-740 tok/s). Its
advantage is the larger window at 8 bits. Set `reasoning_budget_tokens` in the model section; TabbyAPI
reads any config key from `TABBY_<SECTION>_<KEY>` environment variables, so one config file serves several
windows and drafting modes.

## TensorFold

TensorFold 0.6.6 (the Python engine) with the DFlash2 drafter was the fastest writer we have measured for
Qwen3.8-27B on the 3090: 167-170 tok/s on short code, 81-84 on prose, 209-211 on structured output, against
158 / 73 / 181 for ExLlamaV3 with the same drafter (in the side-by-side sitting 170 / 84 / 211, ahead by 7 %,
15 % and 17 %). It needed a local patch to run below compute capability
8.9, keeps the cache in bf16 only (42k window with the default memory reserve, 73k at the edge), and its
Python line is frozen upstream. The maintained engine is the native one, which supports the RTX 30 series
for other model families so far. Not in use here.

## Running engines as containers behind a router

When an engine runs as a container behind llama-swap, restarting
llama-swap does not stop the container. Stop the container first, or the
orphan keeps the GPU and the next load fails.
