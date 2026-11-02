# Bundle — sdlc

## What it is

A complete, role-separated development run from a gathered brief to
verified item lands. The operator's worker stays out of the driver loop.
Use the pinned toolbox copy and the run's accepted design, not mutable
external instructions. Chunk work starts at refine. An item starts at
build only after the accepted LLD, the env land, and Groom. Routing,
claims, stops, and public-git limits are in
[Bundle runs](../../docs/sdlc/bundle-runs.md).

## Flow summary

- Entry: `refine`
- Item entry: `build`
- `refine` | `Brief` | `model` | `refiner`
- `brief-gate` | `Brief` | `gate` | `none`
- `comparables` | `Plan` | `model` | `architect`
- `hld` | `Plan` | `model` | `architect`
- `ux` | `Plan` | `model` | `designer`
- `ux-review` | `Plan` | `model` | `ux-reviewer`
- `ux-gate` | `Plan` | `gate` | `none`
- `plan-gate` | `Plan` | `gate` | `none`
- `trial-gate` | `Trial` | `gate` | `none`
- `trial-done` | `Trial` | `gate` | `none`
- `spec` | `Spec` | `model` | `architect`
- `mockups` | `Spec` | `model` | `designer`
- `mockup-review` | `Spec` | `model` | `ux-reviewer`
- `mockup-gate` | `Spec` | `gate` | `none`
- `security` | `Spec` | `model` | `security`
- `spec-gate` | `Spec` | `gate` | `none`
- `env-prep` | `Build` | `model` | `env-builder`
- `respec-gate` | `Spec` | `gate` | `none`
- `env-prove` | `Build` | `command` | `none`
- `env-baseline` | `Build` | `command` | `none`
- `env-verify` | `Build` | `model` | `env-verifier`
- `env-review` | `Review` | `model` | `env-reviewer`
- `env-gate` | `Build` | `gate` | `none`
- `env-land` | `Build` | `land` | `none`
- `groom` | `Groom` | `model` | `architect`
- `groom-review` | `Groom` | `model` | `groom-reviewer`
- `file-tickets` | `Groom` | `model` | `manager`
- `build` | `Build` | `model` | `builder`
- `prove` | `Build` | `command` | `none`
- `verify` | `Build` | `model` | `verifier`
- `review` | `Review` | `model` | `reviewer`
- `land` | `Build` | `land` | `none`

## Required skills

- test-failure-handler
- yagni
- sdlc-artifacts
- docs-google-style
- security-hardening
- ux-design
- tdd
- debug
- verify-before-done
- pr-review

## Personas

- refiner
- architect
- designer
- ux-reviewer
- security
- groom-reviewer
- manager
- env-builder
- env-verifier
- env-reviewer
- builder
- verifier
- reviewer

## Modes

- enforced
- followed
