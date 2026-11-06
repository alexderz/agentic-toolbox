# Method

Survey date: 2026-11-06. The working method is progressive and
breadth-first.

## Passes

| Pass | Name | Exit test |
| --- | --- | --- |
| 0 | Landscape | Every requested facet has a row, an inclusion rule, and at least one open question |
| 1 | Primary-source survey | Each facet has at least one primary URL that was opened, or an explicit gap |
| 2 | Deepen | High-traffic workflows have a documented check (validity, ERC, DRC, simulation, or HDL test) taken from that tool's own docs |

Pass 2 stopped at documented checks. No candidate was installed. No
score in [papers](catalog/papers.md) was recomputed.

## Evidence grades

| Grade | Meaning |
| --- | --- |
| `github-api` | GitHub REST API fields for that repository on 2026-11-06 |
| `git-tree` | `SKILL.md` paths from `git/trees/HEAD?recursive=1` the same day |
| `license-file` | Opening lines of the repository license file |
| `official-doc` | Vendor or project documentation page fetched the same day |
| `readme` | Repository README text fetched the same day |
| `paper` | arXiv HTML, proceedings page, or abstract fetched the same day |
| `hf-card` | Hugging Face dataset or model page text fetched the same day |
| `unread` | Named during search. Body not opened. Capabilities unknown |

A search snippet is not a grade. If a later sentence depends on a
snippet, the sentence says so.

## Candidate fields

Each concrete candidate uses these fields when the source has them.
Missing fields stay `unknown`.

| Field | What is recorded |
| --- | --- |
| URL | Official repository, doc, or paper URL |
| Capabilities | Actions the README or doc states |
| Maturity | Release tag and date, or `pushed_at`, or paper date |
| License | SPDX id, or license-file text |
| Dependencies | Programs or accounts the doc names |
| Formats | File types the doc names |
| Read/write | Whether the interface reads state, writes a design, or both |
| Mode | Local process, local app plus bridge, or vendor-hosted |
| Evidence | Grade from the table above |
| Class | `tool-driver` (a general agent calls a kernel or EDA tool) or `specialist` (a model emits geometry, a mesh, a sequence, or a circuit) |

## Counts

Star counts are adoption signals from GitHub, not quality scores.
`SKILL.md` counts include templates and per-agent copies when the tree
says so. The KiCad MCP Pro tree is the example: 39 files, 7 names under
`skills/`.

## Results

Author-reported benchmark numbers are labeled `author-reported`. This
survey's own runs are labeled `not run`. No number was estimated to
fill a gap.

## Hardware

Model file sizes and memory figures appear only next to the source that
states them. Three different numbers stay in separate columns:

| Kind | What it is |
| --- | --- |
| Weight-file size | Bytes of a GGUF or safetensors object, from an HTTP `Content-Length` or the Hugging Face tree API |
| Parameter storage | Published parameter count times the bytes per element the checkpoint declares (`BF16` is 2) |
| Runtime peak | Memory a process actually reached while generating tokens, including the KV cache |

A file size is not a runtime peak. A fit on a 24 GB GPU is recorded
only when a source states that fit for that checkpoint and context.
This survey does not assume a GPU is present and did not load weights.
