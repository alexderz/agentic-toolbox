# Bundle — bundle

## What it is
A fixture bundle for the checker.

## Flow summary
- Entry: `plan`
- Item entry: none
- `plan` | `Plan` | `gate` | `none`
- `trial` | `Trial` | `gate` | `none`
- `spec` | `Spec` | `model` | `architect`
- `secure` | `Spec` | `model` | `security`
- `sgate` | `Spec` | `gate` | `none`
- `envbuild` | `Build` | `model` | `env-builder`
- `envprove` | `Build` | `command` | `none`
- `envverify` | `Build` | `model` | `env-verifier`
- `envreview` | `Review` | `model` | `env-reviewer`
- `envland` | `Build` | `land` | `none`
- `release` | `Build` | `gate` | `none`

## Required skills

## Personas
- `architect`
- `env-builder`
- `env-reviewer`
- `env-verifier`
- `security`

## Modes
- followed
