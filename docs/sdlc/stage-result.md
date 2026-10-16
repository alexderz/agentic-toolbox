# Stage result

Tickets: item `DER-529`, chunk `DER-421`.

A **stage** is one run of one SDLC step. The step names are the ones in
[Steps](../SDLC.md#steps). A **stage result** is the file `result.json`
in the stage's working directory. A **command stage** runs a
deterministic tool and records that process exit code. A **model stage**
is any other stage. Deterministic tools and model stages use this same
schema. This file is not the `result.json` a `grok-acp` run writes.

## Status

`status` is exactly `pass`, `fail`, `blocked`, or `needs_input`. Any
other status is a failure. Do not map an unknown status onto one of the
four.

| Status | Meaning |
| --- | --- |
| `pass` | The stage finished, and its evidence holds. |
| `fail` | The stage ran, and its evidence does not hold. |
| `blocked` | The stage stopped on an open blocker. |
| `needs_input` | The stage stopped for a decision from the operator. |

`blocked` and `needs_input` are stage results, not tracker states.
Tracker states stay the six in [Tracker](../SDLC.md#tracker). Sending an
ask still follows [Asking the operator](../SDLC.md#asking-the-human).

## Schema

The file is UTF-8 JSON: one object and no trailing text. The four
fields are required. An unknown key is a failure. A null value is a
failure. Omit an evidence key the evidence table does not require. An
empty string or an empty array does not meet a non-empty rule.

| Field | Type | Rule |
| --- | --- | --- |
| `step` | string | A step name in [Steps](../SDLC.md#steps). |
| `status` | string | One of the four statuses. |
| `evidence` | object | The evidence keys in the evidence table. |
| `findings` | string | The prose. It may be empty, except when `status` is `fail` or `blocked`: then it must be non-empty. |

| Evidence key | Type | Required when |
| --- | --- | --- |
| `kind` | `command` or `model` | Always. |
| `command` | non-empty string | `kind` is `command`. The command line. |
| `exit_code` | integer | `kind` is `command`. Not a string, and not a fraction. |
| `checks` | non-empty array of non-empty strings with no newline | `kind` is `model` and `status` is `pass`. Each entry names one check. |
| `blocker` | non-empty string | `status` is `blocked`. The blocker ticket id. |
| `question` | non-empty string | `status` is `needs_input`. The decision the stage waits on. |

## Rules

Apply the failure table and the prose table. A file can match a row in each.

| Condition | Record |
| --- | --- |
| The file is missing, or it is not one JSON object | Failure |
| `status` is missing, or it is not one of the four | Failure |
| `step` is not a step name, a required field is missing or the wrong type, or a key is unknown | Failure |
| `kind` is `command`, `exit_code` is the integer `0`, and `status` is not `pass` | Failure |
| `kind` is `command`, `exit_code` is an integer other than `0`, and `status` is not `fail` | Failure |
| `status` is `fail` or `blocked`, and `findings` is empty | Failure |

A matching command row is a **disagreement**. A disagreement is a failure, including when the file says `pass`.

Write `result.json` on every path:

1. Write the file before the stage returns.
2. Write it for `pass`, `fail`, `blocked`, and `needs_input`.
3. Replace the file. Do not append a second object.
4. On a command stage, the command wrapper writes `status` from the process exit code so that neither command row matches.
5. On a command stage, the model may write `findings`.
6. On a command stage, the model must not write `status`.
7. On a model stage, the model writes `status` as one of the four.

Open the prose in `findings` only when a row here matches. Otherwise do not open `findings`.

| Condition | Action |
| --- | --- |
| `status` is `fail` | Open `findings`. |
| `status` is `blocked` | Open `findings`. |
| A required evidence field is missing | Open `findings`. |
| None of those | Do not open `findings`. |

## Examples

### pass

```json
{
  "step": "Build",
  "status": "pass",
  "evidence": {
    "kind": "command",
    "command": "npm test",
    "exit_code": 0
  },
  "findings": ""
}
```

### fail

```json
{
  "step": "Build",
  "status": "fail",
  "evidence": {
    "kind": "command",
    "command": "npm test",
    "exit_code": 1
  },
  "findings": "npm test exited 1. test/retry.js expected 3 and got 0."
}
```

### blocked

```json
{
  "step": "Build",
  "status": "blocked",
  "evidence": {
    "kind": "model",
    "blocker": "ABC-12"
  },
  "findings": "ABC-12 is an open blocker, so this stage stops."
}
```

### needs_input

```json
{
  "step": "Brief",
  "status": "needs_input",
  "evidence": {
    "kind": "model",
    "question": "Stop the retry after 3 attempts, or after 30 seconds?"
  },
  "findings": ""
}
```

## Out of scope

This spec does not define the flow file, the Pi command, or session resume.
