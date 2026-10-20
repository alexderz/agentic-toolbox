# Bundle — ok

## What it is

A complete small flow for the sdlc-driver tests: the chunk gates, the
env land, and one item land.

## Flow summary

- Entry `plan`; item entry `build`.
- `plan` Plan gate -
- `trial` Trial gate -
- `spec` Spec model architect
- `security` Spec model security
- `spec-gate` Spec gate -
- `env-build` Build model env-builder
- `env-prove` Build command -
- `env-verify` Build model env-verifier
- `env-review` Review model env-reviewer
- `env-gate` Build gate -
- `env-land` Build land -
- `groom` Groom model architect
- `build` Build model builder
- `prove` Build command -
- `verify` Build model verifier
- `review` Review model reviewer
- `land` Build land -

## Required skills

- `ok-notes`
- `tdd`
- `yagni`

## Personas

- `architect`
- `security`
- `env-builder`
- `env-verifier`
- `env-reviewer`
- `builder`
- `verifier`
- `reviewer`

## Modes

- `enforced`

## Scripts

- `scripts/lint.sh` sha256 `566182641bbed63dd7579685ced41dc6078bc386f87d74cd111372ab46dd0e56` intake `ok-lint`
