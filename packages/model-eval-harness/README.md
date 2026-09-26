# model-eval-harness

Runnable pieces for the [`model-eval`](../../skills/model-eval/SKILL.md)
skill: compare models on a real agentic coding task and grade the result
by running it.

The skill holds the process. This holds the code.

## Layout

```
src/model_eval/
  preflight.sh        gate 1 - tool-call round-trip, per model
  probe-variants.sh   gate 2 - every parameter set actually loads
  readonly_proxy.py   safe read-only access to a live target system
  rubric.py           execution-based grading, runs inside the container
suites/
  home-assistant-cli/ prompts (unguided + graded) and an example matrix
Containerfile         sandbox for executing generated code
tests/                tests for the proxy's refusal behaviour
```

## Runtime adapter

`probe-variants.sh` needs three shell functions for your inference
stack. Provide them in a `lib.sh` (or point `EVAL_LIB` at one):

- `set_variant <model-id> <flags>` — apply flags and restart the server
- `warm <model-id>` — load the model, echo load seconds, non-zero on failure
- `vram` — echo resident device memory in MiB

Warming matters: load time must not land inside the measured run.

## Read-only proxy

Many systems cannot issue a read-only token — a token inherits the
creating user's permissions. Enforce it in front instead:

```
HA_TOKEN_FILE=~/.config/model-eval/ha-token \
HA_UPSTREAM=http://<target>:8123 \
PROXY_PORT=8124 CLIENT_TOKEN=<placeholder> \
python3 src/model_eval/readonly_proxy.py
```

`GET`/`HEAD` only; write-shaped paths refused even on GET; rate limited;
the real credential stays in the proxy and agents get the placeholder.
Every request is logged, which gives you a behavioural metric — what
each model explored, and whether it explored at all.

Run a **second instance on another port** for grading, so the grader's
requests do not consume the rate budget of a case that is still running.

## Grading

Build the sandbox, then run `rubric.py` inside it with the work
directory mounted read-only:

```
podman build -t model-eval-grader .
podman run --rm \
  --add-host=host.containers.internal:host-gateway \
  --memory=2g --pids-limit=256 --cap-drop=ALL \
  --security-opt=no-new-privileges \
  -v <case>/work:/src:ro -v src/model_eval/rubric.py:/rubric.py:ro \
  -e HA_URL=http://host.containers.internal:8125 -e HA_TOKEN=<placeholder> \
  model-eval-grader \
  sh -c 'cp -r /src/. /app/; python3 /rubric.py'
```

Do not use `--network=host`. It would give unreviewed code every
service on the host's loopback, which is the risk the container exists
to contain.

`rubric.py` emits JSON per case: entrypoint, whether help/reads/bad
input/bad auth work, whether the model's own tests collect and pass,
and the subcommands it exposes.

## Reporting

Report LOC as a descriptive stat only. It measures verbosity, not
quality — see the skill.
