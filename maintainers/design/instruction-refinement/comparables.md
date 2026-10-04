# Comparables — instruction refinement

How others write agent instructions that must work across model
strengths. **Before** locking HLD shape.

- Slug: `instruction-refinement`
- Brief / options map: confirmed brief on DER-288 (2026-09-26), options
  map from Gather
- Date: `2026-09-26`

## Required

### Anthropic, skill authoring best practices

- **Who / what** — [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- **What they did** — "Test with all models you plan to use": what
  works for the strongest model "might need more detail" for the
  smallest. One term per concept ("Choose one term and use it
  throughout"). References "one level deep from SKILL.md". Numbered
  workflows with a copyable checklist for fragile sequences ("low
  freedom"). Evaluations before docs: three scenarios, a baseline, then
  iterate. No time-sensitive text.
- **Steal** — Cross-model testing as the acceptance idea; one name per
  thing; one-hop routing; numbered steps where the sequence is fragile
  (our gates are); three eval tasks with a baseline; drop self-deleting
  text (the in-flight map).
- **Won't copy** — Their 500-line body budget (we keep 250) and
  `scripts/` for deterministic steps (our skills stay prose). Their
  "Claude is already very smart" default: our weakest target is a small
  local model, so we write for it and check that frontier models are
  not hurt.

### AGENTS.md format

- **Who / what** — [agents.md](https://agents.md/) (open format,
  stewarded under the Linux Foundation; used by many coding agents)
- **What they did** — A short "README for agents": build and test
  commands, conventions, security notes. Nested files; the nearest one
  wins. People-facing text stays in `README.md`.
- **Steal** — The split we need: agent text and people text in separate
  files. Root `AGENTS.md` as a short router, not a rulebook.
- **Won't copy** — Nearest-file-wins precedence. Our root `AGENTS.md`
  and the SDLC index own their rules; a nested file (`maintainers/`)
  adds, never overrides a gate.

### IFScale (instruction density)

- **Who / what** — Jaroslawicz et al., [How Many Instructions Can LLMs
  Follow at Once?](https://arxiv.org/abs/2507.11538) (2025)
- **What they did** — Up to 500 simultaneous keyword instructions, 20
  models. Accuracy falls as instruction count rises (best frontier model
  68% at 500). Degradation pattern depends on model size and reasoning.
  Bias toward earlier instructions.
- **Steal** — Fewer instructions in context per turn: load only the
  step in play (SDLC split). Put the most-violated rule first in each
  file (primacy).
- **Won't copy** — Its task (keyword inclusion in a report) is not ours;
  we do not treat its numbers as thresholds. We measure our own tasks.

### Chroma, Context Rot

- **Who / what** — Hong, Troynikov, Huber, [Context Rot](https://www.trychroma.com/research/context-rot)
  (Chroma, 2025)
- **What they did** — Performance falls as input grows, even on simple
  tasks. Distractors (similar but wrong text) hurt more as length grows.
- **Steal** — Duplicated or near-duplicate rules are distractors: one
  owner per rule, others route. Shorter files per turn.
- **Won't copy** — Its finding that shuffled haystacks beat coherent
  ones; we keep a logical order for people who maintain the text.

## Optional

- Looked at, not used: OpenAI's practical guide to building agents (PDF)
  could not be read in this session, so it is not cited here.
