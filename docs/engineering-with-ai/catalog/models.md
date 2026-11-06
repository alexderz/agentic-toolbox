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

## 24 GB-class options with a source

Only these statements are sourced. No GPU is assumed to be present.

| Option | Source | What it supports | What it does not say |
| --- | --- | --- | --- |
| RTLCoder 4-bit | Paper | 4 GB memory claim, and a GGUF path with `gpu_layers=0` in the README | Measured tokens per second, context beyond the README sample, or a named 24 GB card for inference |
| RTLCoder training | Paper | Fits training on 24 GB RTX 4090 cards with the paper's batch settings | That a reader must own that GPU |
| CAD-Recode v1.5 | Model card | About 1.5B to 2B parameters | VRAM, quantization, and CPU-only status |
| FP16 RTLCoder-v1.1 shards | Hugging Face file listing | 14.48 GB of weight files | Peak VRAM. A fit in 24 GB would be an estimate and is not stated |

General coding models in the 7B to 32B range are the usual tool-drivers
for build123d and KiCad. Their file sizes and quantizations were not
looked up in this pass, so none is listed as 24 GB-capable here (G21).

## Hosted models with no local weights on the pages read

Zoo Zookeeper, the Fusion MCP session, the Onshape FeatureScript MCP,
and the atopile agent are product agents. The pages read do not publish
parameter counts or checkpoints.
