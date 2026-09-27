# Case matrix

One line per case, tab separated:

```
case-name	model-id	runtime-flags	note
```

Comment lines start with `#`. Keep excluded cases in the file, commented,
with the reason — a matrix is a record of what you decided not to run as
well as what you ran.

## Variants

A case is a **model plus a parameter set**. The same model appears many
times under different settings, and the delta between them is often
more interesting than the difference between models.

Common axes:

- **speed vs context** — more resident weight and a smaller window,
  against a larger window and more offload
- **reasoning budget** — unlimited / generous / tight / disabled
- **fill** — the same context, but parameters that actually use the
  whole accelerator

## Fill variants

Tuning for context alone reliably leaves memory idle. Measure it:
record resident memory per case and subtract from capacity. If a case
runs with a large fraction of the device unused, that is a tuning bug,
and any conclusion drawn from its speed is partly about your config.

Find the limit by stepping the offload parameter until it fails, then
backing off — do not guess. Step coarsely and you will miss the real
boundary and conclude there is no headroom; bisect between the last
success and the first failure.

Add fill results as **new cases**, never as edits to existing ones.

## Ordering

Order fastest expected to slowest. You get most of the signal early,
and a single pathological case at the end cannot block everything else.

## Naming

`<model-short>-<variant>` — `foo30-speed`, `foo30-max`, `foo30-fill`.
Derive the fill name from its base case so the pairing is obvious.
