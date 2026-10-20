# sdlc-driver

Core of the solo SDLC driver. It checks a bundle and reads a stage
result. Node built-ins only: no runtime dependency and no harness import.
Later items add the run loop, land, and toolbox copy in this same package.

Node `>=22.18`. `npm run check` is `tsc -p . && node --test`.

## Commands

```text
sdlc-driver check BUNDLE_DIR [--at COMMIT]
sdlc-driver validate RESULT --flow F --node N [--ticket TICKET] [--authored worker|driver]
```

`check` reads the working tree, or one commit with `--at`. One error per
line, then exit `0` when clean and `1` when not:

```text
<file>: node <id> exit <name>: <code>: <message>
<file>: <field>: <code>: <message>
```

The field form is used when no node applies. A usage error exits `2`.

`validate` checks `result.json` against stage-result v1 and the node's
exits. It prints the same line shape and uses the same exit codes. It
takes the node's step, evidence kind, and exits from the flow. It treats
the result path as `RUN_ROOT/<scope>/run-N/result.json`. `--ticket` is
the invocation ticket; a different value is `result.ticket-mismatch`.
Without it, only the ticket pattern is checked. `--authored` defaults to
`worker`. A reserved exit with `fail` is `flow.reserved-status` unless
`--authored driver`.

## What this item checks

- Strict JSON: one value, no duplicate keys, no nulls, no trailing text.
  A fraction or an exponent is not an integer.
- Stage result v1, including the candidate rules a worker result must
  meet once the run folder is known.
- Persona front matter, the YAML subset with no library: one `key: value`
  per line, body at the first `#` line. No `---` fence.
- Bundle rules B1–B14, including every `gate.*` row.

Shared fixtures under `docs/sdlc/fixtures/results/`, `flows/`, and
`bundles/` are tests. Each result uses its context file. Each flow
directory is one phase (`bundle`, `candidate`, or `env-block`) and an
exact code set. The suite does not skip a landed fixture.

## Driver-only formats

Only the driver writes and reads these. This item names them. Later
items fill the types in; they are not a schema yet.

| File | What it holds |
| --- | --- |
| `driver.json` | Run progress the driver keeps off the product repo: pin, chunk and item state, sessions, the in-flight stage |
| `driver/state.json` | Local tip record of the state branch: `seq`, `tip`, `genesis`, `pushedTip`, `restore`. Never mirrored |
| `driver/ledger.json` | Hash ledger of driver files, so the driver's own writes are not mistaken for a worker's |
| `index.jsonl` | Append-only history of stage events for people. Resume does not read it |
| `plan/items.json` | Snapshot of the groomed item plan for people and dispatch order. Proving commands are not read from it |

## Install

`typescript` is the only dependency, exact-pinned, dev-only, through
`docs/INTAKE.md`. No network at runtime.

```sh
npm --prefix packages/sdlc-driver ci
npm --prefix packages/sdlc-driver run check
```
