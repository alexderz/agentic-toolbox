# Models

Snapshot 2026-11-06. A row is `specialist` when the checkpoint is
trained to emit CAD, Verilog, or a circuit structure. A row is
`tool-driver` when a general coding or vision model is expected to call
an external kernel. This survey did not load any weights.

## Specialist checkpoints with a sourced size

### RTLCoder

| Field | Value |
| --- | --- |
| URL | Paper <https://arxiv.org/html/2312.08617v4>. Code <https://github.com/hkust-zhiyao/RTL-Coder>. Weights named in the README: `ishorn5/RTLCoder-Deepseek-v1.1`, `ishorn5/RTLCoder-v1.1`, GPTQ 4-bit, and GGUF 4-bit |
| Class | specialist, Verilog |
| Parameters | Paper: 7B class. Bases named: Mistral-7B-v0.1 and DeepSeek-Coder-6.7B |
| Quantization and memory | Paper: 4-bit quantization "takes only 4GB of memory" and "can work on a laptop". That 4 GB figure is the paper's claim, not a measurement from this survey. Hugging Face file listing for `ishorn5/RTLCoder-v1.1` shows two FP16 shards, 9.94 GB and 4.54 GB (14.48 GB of weight files). File size is not peak VRAM |
| Training hardware in the paper | 4 RTX 4090 GPUs, 24 GB each, DeepSpeed stage 2, context 2048. That is training, not a requirement for inference |
| 24 GB class | The paper's 4-bit claim (4 GB) is inside a 24 GB card if the claim holds, and also inside a smaller card. The paper also trains on 24 GB cards. Inference VRAM for the FP16 shards was not measured. CPU path: README says the GGUF 4-bit file can run with `ctransformers` and `gpu_layers=0` |
| License | No license file in the GitHub content listing (API 404 on the license endpoint) |
| Maturity | Repository `pushed_at` 2025-02-09. 330 stars. Paper HTML is version 4 of the 2023 preprint |
| Formats | Verilog text |
| Evidence | `paper`, README, Hugging Face file listing |

Author-reported results are in [papers](papers.md). Not rerun.

### CAD-Recode

| Field | Value |
| --- | --- |
| URL | <https://github.com/filaPro/cad-recode>. Weights <https://huggingface.co/filapro/cad-recode-v1.5> |
| Class | specialist. Point cloud to CadQuery Python |
| Parameters | Model card: Qwen2-1.5B plus one linear layer. Card also says "Model size 2B params" |
| Quantization and memory | Not stated on the model card text that was fetched. No VRAM number is recorded. A third-party hardware page was not used |
| 24 GB class | Parameter count is in the 2B range. Whether a given runtime fits in 24 GB, or in system RAM without a GPU, was not measured |
| License | `LICENSE.md` header: Creative Commons Attribution-NonCommercial 4.0. GitHub SPDX `NOASSERTION` |
| Maturity | Repository description: ICCV 2025. `pushed_at` 2025-11-16. 278 stars. Model card downloads-last-month figure on the fetched page: 1,997. That counter moves |
| Formats | Input point cloud. Output Python that the project describes as valid CAD code |
| Evidence | `hf-card`, `license-file`, `github-api` |

## Specialist artifacts without a sourced runtime size

| Name | URL | What the source says about size | Memory |
| --- | --- | --- | --- |
| Text2CAD transformer | <https://huggingface.co/datasets/SadilKhan/Text2CAD> | Dataset card lists `Text2CAD_1.0.pth` as the transformer weights used in the NeurIPS 2024 paper. Annotation models named for the captions: v1.0 uses LLaVA-NeXT and Mistral-7x8B-Instruct. v1.1 uses Qwen2-VL 14B and Qwen2.5-72B-Instruct (8-bit) | Checkpoint file size unknown. The 72B caption model is a data-generation model, not the Text2CAD transformer. Its 8-bit memory footprint was not stated on the card |
| OpenECAD | <https://github.com/YuanZhe-99/OpenECAD_Project> and <https://huggingface.co/datasets/Yuan-Che/OpenECAD-Dataset> | README: TinyLLaVA fine-tune, CUDA required. Dataset card: 918,719 rows, 3.88 GB dataset files. Model weight sizes not on the pages read | Unknown |
| BrepGen | <https://github.com/samxuxiang/BrepGen> | README description: PyTorch implementation, SIGGRAPH 2024. Diffusion over a B-rep tree, not an LLM | Weight file size unknown. License file: no commercial use. Research terms follow GPL v3 in `LICENSE_GPL` |
| AnalogGenie | <https://arxiv.org/html/2503.00205> | Graph generator for analog topologies. Parameter count not extracted | Unknown |

## Tool-driver models

A tool-driver for these workflows is a general coding model, or a
vision-language model when the input is a drawing or a render.
CADGenBench's reference baseline writes build123d or CadQuery with an
external LLM, then exports STEP. The benchmark README does not require
a CAD-specialist checkpoint. Leaderboard rows fetched from the
submissions dataset on 2026-11-06 include hosted general models driving
that baseline. Those rows are snapshots, not a ranking. Examples
present in the viewer text:

| Submission id | Submitted at | Validity rate | Aggregate CAD score |
| --- | --- | --- | --- |
| `huggingface_claude-opus-4-8-hf-baseline-with-build12_20260605-134714` | 2026-06-05 | 0.963 | 0.3451 |
| `huggingface_claude-opus-4-7-hf-baseline-with-build12_20260605-135748` | 2026-06-05 | 0.9383 | 0.3691 |
| `huggingface_gpt-5-5-hf-baseline-with-build123d_20260605-140819` | 2026-06-05 | 0.8765 | 0.3596 |
| `huggingface_claude-opus-4-6-hf-baseline-with-build12_20260605-152108` | 2026-06-05 | 0.8889 | 0.3092 |

Source: Hugging Face dataset viewer text for
`HuggingAI4Engineering/cadgenbench-submissions`, read 2026-11-06.
`validation_method` on those rows was `manual`. The live board is
<https://huggingface.co/spaces/HuggingAI4Engineering/cadgenbench-leaderboard>.
This survey did not download the STEP files or recompute scores.

The same pattern applies to KiCad, SKiDL, tscircuit, JITX, and
PlatformIO: the model that writes the code can be any coding model the
harness runs. Correctness is the external tool's ERC, DRC, build, or
simulation, documented in [evaluation](../workflows/evaluation.md).

## Local coding and vision tool-drivers

Checked 2026-11-06 against official Qwen repositories. Apache-2.0 on
the Hugging Face model records below. No checkpoint was loaded. No
token rate was measured.

The Qwen2.5-Coder family README lists instruct sizes 0.5B, 1.5B, 3B,
7B, 14B, and 32B, each with AWQ, GGUF, and GPTQ-Int4 / GPTQ-Int8
uploads. The 32B AWQ card states 32.5B parameters, AWQ 4-bit, and a
context length of 131,072 tokens. The official 32B GGUF README states
context length 32,768 tokens and says sequences up to 131,072 tokens
belong on the non-GGUF weights. GGUF quant names on that README include
`q4_K_M`, `q5_K_M`, and `q8_0`.

`Qwen/Qwen2.5-Coder-7B-Instruct` reports 7,615,616,512 BF16 parameters.
The four safetensors files sum to 15,231,271,864 bytes (14.185 GiB).
That matches 2 bytes times the parameter count, plus a few kilobytes of
headers. It is the weight-file size of the BF16 checkpoint.

`Qwen/Qwen2.5-VL-7B-Instruct` is `image-text-to-text`. Config:
`model_type` `qwen2_5_vl`, `torch_dtype` `bfloat16`,
`max_position_embeddings` 128000, 28 layers, hidden size 3584. The
safetensors record is 8,292,166,656 parameters. The five weight files
sum to 16,584,414,560 bytes (15.446 GiB).

### Weight-file sizes

HTTP `Content-Length` after redirects, official GGUF files, 2026-11-06.
GiB is bytes divided by 1024 cubed. These are file sizes.

| File | Bytes | GiB |
| --- | --- | --- |
| `qwen2.5-coder-3b-instruct-q4_k_m.gguf` | 2,104,932,800 | 1.960 |
| `qwen2.5-coder-3b-instruct-q8_0.gguf` | 3,616,088,512 | 3.368 |
| `qwen2.5-coder-7b-instruct-q4_k_m.gguf` | 4,683,073,536 | 4.361 |
| `qwen2.5-coder-7b-instruct-q5_k_m.gguf` | 5,444,831,232 | 5.071 |
| `qwen2.5-coder-7b-instruct-q8_0.gguf` | 8,098,525,184 | 7.542 |
| `qwen2.5-coder-14b-instruct-q4_k_m.gguf` | 8,988,110,272 | 8.371 |
| `qwen2.5-coder-14b-instruct-q5_k_m.gguf` | 10,508,873,152 | 9.787 |
| `qwen2.5-coder-14b-instruct-q8_0.gguf` | 15,701,597,632 | 14.623 |
| `qwen2.5-coder-32b-instruct-q4_k_m.gguf` | 19,851,335,872 | 18.488 |
| `qwen2.5-coder-32b-instruct-q5_k_m.gguf` | 23,262,156,992 | 21.665 |

AWQ safetensors sums from the Hugging Face tree API the same day:

| Repo | Bytes | GiB |
| --- | --- | --- |
| `Qwen/Qwen2.5-Coder-32B-Instruct-AWQ` | 19,328,993,904 | 18.002 |
| `Qwen/Qwen2.5-VL-7B-Instruct-AWQ` | 6,923,972,384 | 6.448 |

### What a 24 GiB device can be said to hold

24 GiB is 25,769,803,776 bytes. Every file in the two tables is smaller
than that, so the weights themselves are under 24 GiB. That statement
is about the file. It is not a measured runtime peak.

Headroom left if the file were the only occupant:

| File | File GiB | 24 minus file, GiB |
| --- | --- | --- |
| 7B `q4_K_M` | 4.361 | 19.639 |
| 7B BF16 safetensors | 14.185 | 9.815 |
| 14B `q8_0` | 14.623 | 9.377 |
| VL-7B BF16 safetensors | 15.446 | 8.554 |
| 32B AWQ safetensors | 18.002 | 5.998 |
| 32B `q4_K_M` | 18.488 | 5.512 |
| 32B `q5_K_M` | 21.665 | 2.335 |

KV cache, activations, and a vision tower's runtime buffers sit in the
remainder. Their size was not measured. A 32B `q5_K_M` file leaves
2.335 GiB before any cache, which is a small remainder, not evidence
that generation succeeds. CPU-only execution is possible in the sense
that the GGUF files exist and llama.cpp can place layers in system
RAM. No CPU-only run was done, and system-RAM peak is unknown.

### Other published memory figures, different models

| Source | What it measures | What it is not |
| --- | --- | --- |
| Qwen vLLM recipe, original Qwen | Table of GPU memory on a Tesla V100 32 GB in eager mode. Qwen-7B is 17.94 GB at sequence 2048 and 20.96 GB at 8192. Qwen-7B-Int4 is 9.10 GB and 12.26 GB. The same page lists 24 GB cards (RTX 4090, 3090, A5000) as supporting Qwen-7B, Qwen-7B-Int4, and Qwen-14B-Int4 at the default sequence length | Not Qwen2.5-Coder and not Qwen2.5-VL. The page is an older generation |
| OpenLLM Qwen2.5 deployment page | A "required GPU RAM" column: `qwen2.5:7b` 24G, `qwen2.5:32b` 80G, `qwen2.5:14b` 80G | A packager's requirement label for generic `qwen2.5` tags. Not a peak measured here, and not labeled as the Coder or VL checkpoints |
| RTLCoder paper | 4-bit model "takes only 4GB of memory". Training used four 24 GB RTX 4090 cards | Author claim for a Verilog specialist, not a measurement of Qwen2.5-Coder |

Third-party VRAM calculators that estimate 18 to 19 GB for the 32B AWQ
checkpoint were not used. The AWQ weight files sum to 18.002 GiB, which
is the part of that estimate that this survey actually counted.

## Hosted models with no local weights on the pages read

Zoo Zookeeper, the Fusion MCP session, the Onshape FeatureScript MCP,
and the atopile agent are product agents. The pages read do not publish
parameter counts or checkpoints.
