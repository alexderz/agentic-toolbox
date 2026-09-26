# Gates

Each of these exists because skipping it produced a confidently wrong
result. Run them in order; none is optional.

## 1. Tool-call round-trip

**Proves:** the model emits tool calls the inference server can parse
and terminate on.

Send one trivial tool-calling request per model, outside the agent
entirely:

```
POST /v1/chat/completions
{"model": "<id>", "max_tokens": 512,
 "messages": [{"role": "user", "content": "List the files in the current directory."}],
 "tools": [{"type": "function", "function": {"name": "bash", ...}}]}
```

Accept only if **all** hold:

- `finish_reason == "tool_calls"`
- exactly the expected tool name
- `arguments` parses as JSON
- no markup leaked into `arguments` (`</parameter>`, `<tool_call>`, …)

A model can fail this while being perfectly capable. Chat templates
encode a tool-call syntax, and runtimes select a parser by sniffing the
template. When the sniff misses, the parser never finds a terminator:
the model generates to the output-token limit, the agent rejects the
truncated call, and it retries forever. Symptom is many turns, a huge
event log and zero files.

A template patch usually cannot fix this — the model was *trained* to
emit that syntax, and the template only controls how history is
rendered. Exclude the model and say why. Do not score it.

## 2. Variant load

**Proves:** every parameter set in the matrix loads.

Model-level checks do not cover this. The matrix overrides the runtime
defaults with different contexts and offload splits, and an override
can OOM outright. Load each variant, record resident memory, move on.

Record the *headroom* too. A config that loads while leaving a third of
the accelerator idle is a tuning bug, not a result — see
`assets/case-matrix.md` on fill variants.

## 3. Loop iteration

**Proves:** the driver runs every case.

Test the loop shape with a stand-in body before trusting it:

```bash
n=0
while IFS=$'\t' read -r case rest; do
  n=$((n+1)); <the same command shape the real body uses>
done < <(grep -v '^#' matrix.tsv)
echo "iterations: $n"
```

The classic failure is a command in the loop body reading the loop's
stdin and draining it — `ssh` without `-n` is the usual culprit. The
loop silently ends after one iteration. Feed the loop from a process
substitution and redirect the body's stdin from `/dev/null`.

## 4. Workspace isolation

**Proves:** nothing ambient reaches the model.

Run one case, then grep the event stream for anything that could only
have come from an instruction file. If it is there, the eval is
measuring obedience, not capability.

## 5. Metric sanity

**Proves:** counters measure the model's own work.

Run one case and read the raw numbers before trusting any of them.
Things that have silently broken counters:

- a virtualenv or installed packages counted as model output
- files without a `.py` extension not counted at all, so a complete
  tool with a shebang scored zero
- token usage read from streaming deltas, which carry zeros — real
  totals arrive on terminal events

Exclude vendored and generated paths; detect language by shebang as
well as extension; sum terminal events, not deltas.
