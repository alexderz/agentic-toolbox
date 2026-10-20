# Bundle — bundle

## What it is
A fixture bundle for the checker.

## Flow summary
- Entry: `plan`
- Item entry: `build`
- `plan` | `Plan` | `gate` | `none`
- `trial` | `Trial` | `gate` | `none`
- `spec` | `Spec` | `model` | `architect`
- `secure` | `Spec` | `model` | `security`
- `sgate` | `Spec` | `gate` | `none`
- `envgate` | `Build` | `gate` | `none`
- `envbuild` | `Build` | `model` | `env-builder`
- `envprove` | `Build` | `command` | `none`
- `envverify` | `Build` | `model` | `env-verifier`
- `envreview` | `Review` | `model` | `env-reviewer`
- `envland` | `Build` | `land` | `none`
- `release` | `Build` | `gate` | `none`
- `build` | `Build` | `model` | `builder`
- `prove` | `Build` | `command` | `none`
- `verify` | `Build` | `model` | `verifier`
- `review` | `Review` | `model` | `reviewer`
- `land` | `Build` | `land` | `none`

## Required skills

## Personas
- `architect`
- `builder`
- `env-builder`
- `env-reviewer`
- `env-verifier`
- `reviewer`
- `security`
- `verifier`

## Modes
- followed
