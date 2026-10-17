# Stage result

Tickets: item `DER-529`, chunk `DER-421`.

A **stage** is one run of one SDLC step. Use the step names in
[Names](../SDLC.md#names). A **stage result** is the file `result.json`
in a caller-supplied absolute output directory, unique to this stage
invocation and outside the source checkout. The caller retains that
path with the invocation; retries use new directories.
A **command stage** runs a deterministic tool and records its exit code.
A **model stage** is any other stage. Both use this schema, not the
`result.json` a `grok-acp` run writes.

## Status

A **failure** means the reader rejects the stage as unsuccessful, never
accepting a claimed `pass`. Do not rewrite the submitted status.
`status` is exactly `pass`, `fail`, `blocked`, or `needs_input`. Any
other status is a failure.

| Status | Meaning |
| --- | --- |
| `pass` | The stage finished, and its evidence holds. |
| `fail` | The stage ran, and its evidence does not hold. |
| `blocked` | The stage stopped on an open blocker. |
| `needs_input` | The stage stopped for a decision from the operator, or someone the operator names in writing. |

For tracker states, see [Tracker](../SDLC.md#tracker). For decisions,
see [Asking the operator](../SDLC.md#asking-the-human).

## Schema

The file is UTF-8 JSON: one object and no trailing text. Reject duplicate
keys at every nesting level as a failure; do not keep the last value.
The four top-level fields are required. An unknown key or a null value
is a failure. An empty string or array does not meet a non-empty rule.

| Field | Type | Rule |
| --- | --- | --- |
| `step` | string | A step name in [Names](../SDLC.md#names). |
| `status` | string | One of the four statuses. |
| `evidence` | object | Stage evidence. |
| `findings` | string | The prose. It may be empty, except when `status` is `fail` or `blocked`: then it must be non-empty. |

| Evidence field | Type | Required when |
| --- | --- | --- |
| `kind` | `command` or `model` | Always. |
| `command` | non-empty string | `kind` is `command`. The command line. |
| `exit_code` | integer | `kind` is `command`. Not a string, and not a fraction. |
| `checks` | non-empty array of non-empty strings with no newline | `kind` is `model` and `status` is `pass`. Each entry names one check. |
| `blocker` | non-empty string | `status` is `blocked`. The blocker ticket id. |
| `question` | non-empty string | `status` is `needs_input`. The decision the stage waits on. |

Omit an evidence field when its required condition does not hold.

## Rules

| Condition | Record |
| --- | --- |
| The file is missing, or it is not one JSON object | Failure |
| `status` is missing, or it is not one of the four | Failure |
| `step` is not a step name, a required top-level or evidence field is missing or invalid, or a key is unknown | Failure |
| `kind` is `command`, `exit_code` is the integer `0`, and `status` is not `pass` | Failure |
| `kind` is `command`, `exit_code` is an integer other than `0`, and `status` is not `fail` | Failure |
| `status` is `fail` or `blocked`, and `findings` is empty | Failure |

A matching command row is a **disagreement** and a failure. Report a
structured validation error for invalid results or disagreements.
Disagreement alone does not authorize opening prose.

The **stage harness** is the caller that persists a stage's output.

1. **Stage harness** persists `result.json` before returning on every path.
2. **Stage harness** replaces the file; do not append a second object.
3. **Stage harness** persists model output on behalf of read-only roles;
   reviewers do not write files or modify the reviewed checkout.

| Actor and stage kind | Output authority |
| --- | --- |
| Command wrapper, command stage | Supply `step`, `evidence`, and `status`. Exit `0` means `pass`; any other integer means `fail`. Record `command` and `exit_code` from the actual invocation and process result. The wrapper can populate `findings` from CI links or error output. |
| Model, command stage | Add `findings` only; do not set `status` or change command evidence. |
| Model, model stage | Return the four fields to the harness, with `status` as one of the four. |

| Condition | Action |
| --- | --- |
| `status` is `fail` | Open `findings`. |
| `status` is `blocked` | Open `findings`. |
| A required evidence field is missing | Open `findings`. |
| None of those | Do not open `findings`. |

## Examples

### pass

Command stage:
```json
{
  "step": "Build", "status": "pass",
  "evidence": {"kind": "command", "command": "npm test", "exit_code": 0},
  "findings": ""
}
```

Model stage:
```json
{
  "step": "Spec", "status": "pass",
  "evidence": {"kind": "model", "checks": ["Schema matches acceptance"]},
  "findings": ""
}
```

### fail

```json
{
  "step": "Build", "status": "fail",
  "evidence": {"kind": "command", "command": "npm test", "exit_code": 1},
  "findings": "npm test exited 1. test/retry.js expected 3 and got 0."
}
```

### blocked

```json
{
  "step": "Build", "status": "blocked",
  "evidence": {"kind": "model", "blocker": "ABC-12"},
  "findings": "ABC-12 is an open blocker, so this stage stops."
}
```

### needs_input

```json
{
  "step": "Brief", "status": "needs_input",
  "evidence": {
    "kind": "model",
    "question": "Stop the retry after 3 attempts, or after 30 seconds?"
  },
  "findings": ""
}
```

## Out of scope

This spec does not define the flow file, the Pi command, or session
resume.
