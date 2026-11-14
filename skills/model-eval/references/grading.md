# Grading

## Grade by execution

Reading generated code tells you how it looks. Running it tells you
whether it works. Those diverge constantly: a tool can be well
structured, well named, thoroughly commented, and not function.

**LOC is never a quality measure.** It measures verbosity. In practice
the largest output in a matrix is often padded, and a model can write
a long, tidy tool with zero tests while a shorter one ships real ones.
Report size as a descriptive stat if you like; never rank on it.

## Run it in a container

Generated code is model-written and unreviewed. It must not execute on
the host.

- no host network — reach only a dedicated endpoint for the eval
- source copied in, mounted read-only, running as an unprivileged user
- drop all capabilities, `no-new-privileges`, memory and pid caps

Resist `--network=host` for convenience: it hands untrusted code every
service listening on the host's loopback, which is exactly the thing
you are trying to prevent. Instead run a second, separate endpoint for
the grader (its own rate budget, its own credential) and let the
container reach only that.

## The checks

| check | passes when |
|---|---|
| `help` | `--help` exits 0 and prints usable help |
| `reads` | a real read against the target returns real data |
| `bad_input` | a nonexistent resource fails cleanly, non-zero exit, no traceback |
| `bad_auth` | a wrong credential is handled, no traceback |
| `no_crash` | nothing raises an unhandled exception |
| `tests` | the model's own tests collect, run and pass |
| `coverage` | how much of the target API was genuinely exercised |

Two things this catches that no amount of reading will:

- a tool that prints `Error:` and still **exits 0**
- a test file that does not even **collect** (import error), which
  looks like "wrote tests" in any file-counting metric

## Discovering the entry point

Every model invents its own CLI, so the grader has to find it:

- prefer files that import an arg parser and define a `main`
- detect executables by shebang as well as by extension
- skip `test_*`, `conftest`, `setup`, `mock*`
- scrape subcommand names out of `--help` output, then try the model's
  own names before falling back to generic ones

Tools also disagree about whether a configured base URL already
contains the API path. Try both shapes before concluding a tool cannot
read — otherwise you will record a harness bug as a model failure.

## Scoring

Weight the criteria equally unless you have a reason not to, and state
them in the prompt if you are running a graded round. Judge the top
candidates by reading them **after** the execution results are in, so
the reading is informed by what actually ran.
