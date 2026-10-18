# Comparables — solo-dlc: the SDLC on a harness without sub-agents

How others run a multi-agent coding workflow from a fixed definition,
with separate agent processes, durable state, and human gates.
**Before** locking HLD shape. UX look-and-flow comparables are on the
designer's page: [ux.md](ux.md#comparables).

- Slug: `solo-dlc`
- Brief / options map: DER-421 brief v3, confirmed 2026-10-18 (tracker
  copy: a comment on DER-421). The brief has no options map.
- Date: `2026-10-18`

## Required

### Pi, subagent extension example

- **Who / what** — The `subagent` example extension in the Pi coding
  agent repository:
  [packages/coding-agent/examples/extensions/subagent](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/subagent).
- **What they did** — A Pi extension that runs each subagent as a
  separate `pi` process with its own system prompt, tools, and model.
  Agents are markdown files with YAML front matter (`name`,
  `description`, `tools`, `model`). Three modes: single, parallel (at
  most 8 tasks, 4 at a time), and chain, where each step gets the
  previous step's output through a `{previous}` placeholder. Chain mode
  stops at the first failing step and reports which step failed. A
  non-zero exit code, an error stop reason, or a user abort each surface
  as an error. Project-local agent files are treated as repo-controlled
  prompts and need confirmation in untrusted projects.
- **Steal** — One OS process per worker, started by an extension on the
  host harness. A persona as a markdown file with front matter for tools
  and model. Stop the flow at the first failing step and name it. Treat
  repo-supplied agent definitions as untrusted until intake.
- **Won't copy** — The model calls the subagent as a tool, so the model
  decides when to delegate; here `/sdlc` is a user command and no tool
  starts or steers the driver. Each call is a fresh process with no
  resume; here the builder, verifier, and reviewer are resumed across
  passes. Output passes as text between steps; here it passes as files
  in a run folder and a validated `result.json`. The chain is linear;
  the flow here has loops expressed as allowed exits.

### OpenCode, agents and the Task tool

- **Who / what** — OpenCode's agent configuration:
  [Agents](https://opencode.ai/docs/agents/), including
  [Task permissions](https://opencode.ai/docs/agents/#task-permissions).
- **What they did** — Primary agents and subagents, defined in JSON
  config or markdown files. Each agent sets its own model, prompt, and
  permissions; a reviewer can deny `edit` and `bash`. A primary agent
  starts subagents through the Task tool, which creates navigable child
  sessions. `permission.task` uses globs to allow, ask for, or deny
  which subagents an agent may start; a denied subagent is removed from
  the Task tool's description. A hidden `compaction` agent writes the
  summary when context runs long. The SDK's `session.create` takes an
  optional `parentID` and starts with an empty transcript (checked in
  the `@opencode-ai/sdk` 1.19.3 types; see the brief).
- **Steal** — A model per persona, so the reviewer can point at a
  different model than the builder. Deny writes to read-only personas in
  the harness's own permission system where it has one. A new session
  with an empty transcript as the clean mint for a worker.
- **Won't copy** — Delegation chosen by a primary agent: that is a
  coordinating agent that dispatches workers, which the brief rules
  out. Compaction by a
  generic summarizer agent: here the worker's own `state.md` plus
  driver facts build the summary.

### Archon, workflow engine for AI coding agents

- **Who / what** — Archon, an open-source workflow engine:
  [repository and README](https://github.com/coleam00/Archon);
  [docs](https://archon.diy/).
- **What they did** — Development processes defined as YAML workflows
  committed under `.archon/workflows/`. A workflow mixes AI nodes
  (plan, implement, review) with deterministic `bash` nodes (tests,
  git) that run without a model. Loops repeat until a completion signal
  or a shell check passes, with an iteration cap. `wait` nodes pause for
  a human approval. Runs can use their own git worktree. The README's
  framing: the workflow defines the phases, validation gates, and
  artifacts, and the AI fills in the intelligence at each step. The
  installers offer Claude, Codex, and Pi as providers.
- **Steal** — The process is data in the repo, owned by the user, not
  by a model. Proving commands run as deterministic nodes the model
  cannot skip or edit. Human approval is a node type, not a convention.
  One worktree per unit of work. A cap on repair loops.
- **Won't copy** — `fresh_context` per loop iteration: here the builder
  keeps its session across passes and compacts from `state.md`. A DAG
  of `depends_on` edges: Build, Verify, and Review loop, so this flow
  lists exits per step instead. Pull requests as the end of a run: this
  SDLC lands locally on project-main with no internal PRs. The agent
  picking a workflow from a chat request ("use archon to …"): here only
  the operator types `/sdlc`. Product telemetry.

### LangGraph, persistence and checkpointers

- **Who / what** — LangGraph's persistence layer:
  [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence).
- **What they did** — A checkpointer saves a thread's graph state as
  checkpoints keyed by a `thread_id`, so a run can continue after an
  interruption, recover from a failure, and pause for a human. A
  separate store keeps data across threads. The docs warn that in-memory
  savers lose every checkpoint on restart and that checkpoints grow
  without bound unless pruned.
- **Steal** — Durable run state outside the process, keyed by one id
  (here, the run root path), so a crash or reboot loses nothing and the
  same command resumes. Keep driver position separate from worker
  memory. Decide retention up front: here old run folders are kept on
  purpose.
- **Won't copy** — A library runtime or server with a database
  checkpointer. Here state is plain files in the run root plus git and
  the tracker, readable by the operator and by a followed-mode agent
  without the driver.
