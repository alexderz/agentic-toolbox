# Papers, datasets, and benchmarks

Snapshot 2026-11-06. `Reported` means the paper or leaderboard states
the number. `This survey` is `not run` for every row. Limits are the
ones the source itself states, plus gaps this pass did not close.

## Mechanical datasets and generators

### ABC

| Field | Value |
| --- | --- |
| URL | Cited by DeepCAD as Koch et al., about 1 million CAD models from Onshape, B-rep, without construction sequences. Canonical project page was not reopened |
| Date | Cited as 2019 in the DeepCAD paper |
| Task | Geometric deep learning on B-rep collections |
| Reported | Collection scale as stated in DeepCAD's related work |
| Artifacts | Not re-downloaded |
| Limits | DeepCAD: no construction sequence |

### Fusion 360 Gallery

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/abs/2010.02392>. Data <https://github.com/AutodeskAILab/Fusion360GalleryDataset> |
| Date | arXiv abstract fetched. Repository `pushed_at` 2022-04-23. 760 stars. License SPDX `NOASSERTION` |
| Task | Reconstruct sketch-and-extrude construction sequences. 8,625 designs. Official split 6,900 train and 1,725 test. Representations: B-rep, mesh, JSON. Environment: Fusion 360 Gym |
| Reported | Paper presents neurally guided search. Numbers not copied |
| Artifacts | Repository exists. Gym compatibility with current Fusion was not tested |
| Limits | Paper: sketch and extrude only, by design |

### DeepCAD

| Field | Value |
| --- | --- |
| URL | <https://doi.org/10.48550/arxiv.2105.09492> |
| Date | arXiv 2105.09492 |
| Task | Generative model of CAD command sequences. Dataset of 178,238 designs, sketch and extrude |
| Reported | Dataset size from the paper text that was fetched |
| Artifacts | Used as the base of Text2CAD and OpenECAD. Original host not re-downloaded |
| Limits | Operation subset is sketch and extrude |

### Text2CAD

| Field | Value |
| --- | --- |
| URL | NeurIPS 2024 PDF linked from the repository: <https://proceedings.neurips.cc/paper_files/paper/2024/file/0e5b96f97c1813bb75f6c28532c2ecc7-Paper-Conference.pdf>. Code <https://github.com/SadilKhan/Text2CAD>. Data <https://huggingface.co/datasets/SadilKhan/Text2CAD> |
| Date | NeurIPS 2024, spotlight, per the repository |
| Task | Text prompts at four expertise levels to a CAD command sequence. Built on DeepCAD. Dataset card: v1.0 captions from LLaVA-NeXT and Mistral-7x8B-Instruct. v1.1 from Qwen2-VL 14B and Qwen2.5-72B-Instruct 8-bit. Full card storage warning: 605 GB |
| Reported | Not copied. This survey did not extract the results table |
| Artifacts | Code repository, 491 stars, `pushed_at` 2025-05-15. License file: CC BY-NC-SA 4.0. Weights file `Text2CAD_1.0.pth` named on the dataset card |
| Limits | Sequence representation follows DeepCAD. Caption text is model-generated. Non-commercial share-alike license |

### BrepGen

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2401.15563>. Code <https://github.com/samxuxiang/BrepGen> |
| Date | arXiv 2401.15563. Repository description: SIGGRAPH 2024 |
| Task | Diffusion that emits a B-rep, including free-form faces. Evaluated on DeepCAD, ABC, and a furniture B-rep set |
| Reported | Paper says it surpasses prior methods. Tables not copied |
| Artifacts | Code, data, and weights in the repository. `pushed_at` 2024-09-13. 428 stars. License: no commercial use. Research terms follow GPL v3 |
| Limits | Author comparison. Not rerun |

### OpenECAD

| Field | Value |
| --- | --- |
| URL | Paper id on the dataset card: 2406.09913. Code <https://github.com/YuanZhe-99/OpenECAD_Project>. Data <https://huggingface.co/datasets/Yuan-Che/OpenECAD-Dataset> |
| Date | Dataset card cites June 2024 for 2406.09913 |
| Task | Image to editable CAD code. LLaVA-format pairs. Dataset card: 918,719 rows, 3.88 GB |
| Reported | Not extracted |
| Artifacts | MIT code repository, 18 stars, `pushed_at` 2024-11-07. README: CUDA required for the TinyLLaVA path. STEP conversion tool named `YuanZhe-99/OpenECADtoSTEP` |
| Limits | Depends on DeepCAD conversions. Weight file sizes unknown |

### CAD-Recode

| Field | Value |
| --- | --- |
| URL | <https://github.com/filaPro/cad-recode>. Card <https://huggingface.co/filapro/cad-recode-v1.5> |
| Date | Repository description: ICCV 2025. Card describes point cloud to CadQuery Python, Qwen2-1.5B plus a linear layer |
| Task | Reverse engineering a point cloud into executable CAD code |
| Reported | Not extracted from the paper PDF. Paper PDF was not the page opened |
| Artifacts | Weights on Hugging Face. License CC BY-NC 4.0 |
| Limits | Non-commercial. Output is code that still needs a kernel to execute |

### CADCodeVerify and CADPrompt

| Field | Value |
| --- | --- |
| URL | <https://github.com/Kamel773/CAD_Code_Generation> |
| Date | Repository description: ICLR 2025 |
| Task | Vision-language model writes CAD code. CADCodeVerify asks a VLM a set of checks and revises. CADPrompt: 200 DeepCAD objects with STL, OBJ, language, JSON commands, and expert Python |
| Reported | Not extracted |
| Artifacts | Repository 67 stars, `pushed_at` 2025-02-28. No license detected |
| Limits | 200 prompts. Not rerun |

### CADGenBench

| Field | Value |
| --- | --- |
| URL | <https://github.com/huggingface/cadgenbench>. Inputs <https://huggingface.co/datasets/HuggingAI4Engineering/cadgenbench-data>. Leaderboard <https://huggingface.co/spaces/HuggingAI4Engineering/cadgenbench-leaderboard> |
| Date | Repository created 2026-05-27. `pushed_at` 2026-10-22. 151 stars. Package version in `pyproject.toml` snippet: 0.1.0. Python 3.12 or newer |
| Task | 81 fixtures. Generation: 49 drawings to a solid. Editing: 32 STEP files plus a change. Submission is `output.step` or `output.stp` per sample. Ground truth is private |
| Metrics | Validity gate: well-formed watertight BREP that meshes to a closed manifold. Failure zeroes the rest. Then shape similarity (surface-distance F1 and volume IoU), interface match (keep-in and keep-out volumes), topology match (Betti numbers). CAD Score is a weighted combination. Full weights are in `docs/metrics.md`, which was not copied |
| Reported | Leaderboard rows are author or submitter uploads. Four baseline rows are quoted in [models](models.md) from the dataset viewer on 2026-11-06. Not recomputed |
| Artifacts | Apache-2.0 code. Reference baseline uses build123d or CadQuery. Local sanity check script is named in the README |
| Limits | 81 parts. Private ground truth. Rows can stay unvalidated until a maintainer review |

### STEP-LLM

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2601.12641> |
| Date | arXiv 2601.12641 |
| Task | Fine-tune an LLM to emit STEP text. About 40,000 STEP-caption pairs. DFS reserialization, retrieval, then a Chamfer-distance reward |
| Reported | Paper: higher geometric fidelity than a Text2CAD baseline. Tables not copied |
| Artifacts | A public checkpoint URL was not confirmed (G8) |
| Limits | STEP is cross-referenced text. The paper's own motivation is that autoregressive models struggle with that structure |

### OmniMech

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2608.05539> |
| Date | arXiv 2608.05539 |
| Task | 251,000 dimensioned and toleranced drawings paired with native CAD (the paper says SolidWorks `.sldprt`), STEP, mesh, and annotations. Tasks: parametric program synthesis, diagram-to-3D, annotation-grounded constraints, tool-using agent |
| Reported | Paper's summary: current VLMs fail executable programs, fine geometry, and tolerance grounding. Tables not copied |
| Artifacts | Paper says data, evaluation code, and tool interfaces will be released. Not found in this pass (G7) |
| Limits | Release pending, as of the HTML that was read |

### Multi-Agent CAD

Repository only. <https://github.com/Pan-Chera/Multi-Agent-CAD>. 1,071
stars, MIT, `pushed_at` 2026-11-04. Paper, if any, was not opened.

## Topology and simulation papers

### Foam-Agent 2.0

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2509.18178v2> |
| Date | arXiv 2509.18178 version 2 |
| Task | Multi-agent OpenFOAM CFD. The HTML describes an MCP split into meshing, solving, and post-processing, with `case_id` and `job_id` |
| Reported | Not extracted |
| Artifacts | No repository returned by the GitHub search used in this pass (G12) |
| Limits | OpenFOAM case correctness was not checked |

### AutoSiMP

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2603.27000> |
| Date | arXiv 2603.27000 |
| Task | Natural language to a binary topology through a validated SIMP specification, not through generated solver code. 10 configuration problems. 17-benchmark controller comparison |
| Reported | Configurator: valid specifications on all 10 cases, median compliance penalty +0.3% versus expert ground truth. LLM controller: lowest median compliance, 76.5% pass rate. Deterministic schedule: 100% pass rate at +1.5% higher compliance. End to end with the schedule controller: all LLM-configured problems pass on the first attempt. These are author-reported |
| Artifacts | Paper: code, specifications, and a demo will be released on journal acceptance |
| Limits | 2-D and the paper's own benchmark set. Not rerun. Code absent at the time of that HTML |

### LLM as SIMP controller

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2603.25099v2> |
| Date | arXiv 2603.25099 version 2 |
| Task | An LLM sets SIMP continuation parameters from a numeric observation. Benchmarks: three 2-D problems at 120 by 60 and two 3-D problems at 40 by 20 by 10, 300 iterations |
| Reported | Lowest final compliance on every listed benchmark, from −5.7% to −18.1% versus a fixed baseline, solutions fully binary. Author-reported |
| Artifacts | Paper: code will be released on publication |
| Limits | Those five problems. Not rerun |

## Electrical papers and benchmarks

### VerilogEval

| Field | Value |
| --- | --- |
| URL | Original <https://arxiv.org/html/2309.07544>. Code <https://github.com/NVlabs/verilog-eval>. Revisit: <https://dl.acm.org/doi/full/10.1145/3718088> |
| Date | Original arXiv 2309.07544. Repository created 2023-08-23, `pushed_at` 2025-07-14, 492 stars. Revisit published 2025-10-21 in ACM TODAES |
| Task | 156 HDLBits problems. Functional check is transient simulation against a golden solution. The revisit adds specification-to-RTL and failure classification |
| Reported, revisit, author-reported | GPT-4o 63% pass on specification-to-RTL. Llama 3.1 405B 58%. RTL-Coder 6.7B 34%. Models named in that paper also include GPT-4 Turbo, Llama 3.1 8B and 70B, Llama 3 70B, Mistral Large, DeepSeek Coder 33B and 6.7B, CodeGemma 7B |
| Artifacts | MIT license text in the NVIDIA repository (SPDX was `NOASSERTION`) |
| Limits | HDLBits-style problems. Prompt sensitivity is called out by the revisit. Not rerun |

### RTLCoder

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2312.08617v4> |
| Date | Preprint 2312.08617, HTML v4 |
| Task | Fine-tune 7B models for Verilog. Benchmarks named: VerilogEval and RTLLM |
| Reported | Paper: better than GPT-3.5 on the benchmarks it uses, and better than GPT-4 on VerilogEval Machine. 4-bit model still above GPT-3.5 on VerilogEval with slight degradation. Author-reported. The revisit above later reports 34% for RTL-Coder 6.7B on specification-to-RTL, which is a different number on a later harness |
| Artifacts | Code repository has no license file. Dataset of 27K instruction pairs described in the paper. Hugging Face repos named in the README |
| Limits | See [models](models.md) for size evidence. The two papers' percentages are not interchangeable |

### EDA Corpus

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2405.06676>. Data <https://github.com/OpenROAD-Assistant/EDA-Corpus> |
| Date | arXiv 2405.06676. Repository `pushed_at` 2025-01-17. 46 stars |
| Task | OpenROAD prompts. More than 1,000 pairs: question to prose, and prompt to OpenROAD script |
| Reported | Dataset size. No accuracy table copied |
| Artifacts | License CC-BY-4.0 |
| Limits | OpenROAD APIs drift. Currency of the scripts against a current OpenROAD build was not tested |

### OpenROAD Agent

| Field | Value |
| --- | --- |
| URL | IEEE ICLAD 2025 abstract, <https://ieeexplore.ieee.org/document/11106006> |
| Date | Conference 2025-06-26 to 2025-06-27. Added to IEEE Xplore 2025-08-13 |
| Task | Qwen2.5-Coder fine-tune that generates and executes OpenROAD Python, then corrects from tool errors |
| Reported | Abstract: 94% script-generation accuracy. Author-reported. The abstract says model, data, and scripts are open-sourced. The repository URL was not opened in this pass |
| Artifacts | Claimed open. URL unverified here |
| Limits | Abstract only. Accuracy definition not read beyond the abstract |

### AnalogCoder

| Field | Value |
| --- | --- |
| URL | <https://doi.org/10.1609/aaai.v39i1.32016>. Code <https://github.com/laiyao1/AnalogCoder> |
| Date | AAAI 2025. DOI page says published 2025-04-11 |
| Task | Training-free PySpice generation for analog circuits, with simulator feedback and a subcircuit library |
| Reported | Abstract: 20 circuits, 5 more than the paper's standard GPT-4o. Author-reported |
| Artifacts | MIT code. Depends on ngspice and an OpenAI-compatible API |
| Limits | The paper's own benchmark of conventional analog blocks. Not rerun |

### AnalogGenie

| Field | Value |
| --- | --- |
| URL | <https://arxiv.org/html/2503.00205> |
| Date | arXiv 2503.00205 |
| Task | Generative model of analog topologies as graphs. Related-work summary in the paper: CktGNN for op-amps, LaMAGIC for converters with fewer than 4 devices, AnalogCoder for PySpice of circuits on the order of ten devices |
| Reported | Not extracted from the results section |
| Artifacts | Not confirmed |
| Limits | Topology generation is not a SPICE signoff |

### ChatEDA and ChipNeMo, from a survey table

`LLM4EDA` survey HTML <https://arxiv.org/html/2401.12224v1> (2401.12224)
contains a dataset table. Cells read from that table, not from the
original papers:

| Dataset | Task marks in the survey | Size cell |
| --- | --- | --- |
| ChipNeMo | Chat, generation, verification | 24.1 billion tokens, internal NVIDIA data. Not public, per the survey's surrounding text on proprietary data |
| ChatEDA | Generation | 1,500 instructions |
| VeriGen | Generation | 400 MB from textbooks and GitHub |
| VerilogEval SFT data | Generation | 8,502 samples |

Original ChipNeMo and ChatEDA PDFs were not opened. Treat the cells as
the survey's summary.

### SchGen

| Field | Value |
| --- | --- |
| URL | <https://huggingface.co/datasets/microsoft/SchGen_dataset> |
| Date | Card fetched 2026-11-06. Publication date not on the excerpt |
| Task | 8,420 natural-language requests paired with Python that the card says renders to KiCad schematics |
| Reported | No accuracy number on the card excerpt |
| Artifacts | Hugging Face dataset |
| Limits | Card: GPT-5 drafted designs from open-source references, humans corrected them, then requests were synthesized. That is a construction pipeline, not a blind test set description |
