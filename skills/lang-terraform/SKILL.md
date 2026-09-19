---
name: lang-terraform
description: use this when writing or reviewing Terraform / HCL — *.tf, *.hcl. do not use for general YAML or for Docker.
---

# Terraform

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. No `scripts/`.

## Iron law

**State is sensitive. Plans are read. Secrets stay out of VCS.**

## Tooling / verify

```bash
terraform fmt -check
terraform validate
terraform plan
```

Read the plan. Do not apply in this skill.

## Idioms a linter misses

- Remote state with locking when the project already has it.
- Pin `required_providers` and Terraform version as the root module
  already does.
- `for_each` over `count` for sets.
- Variables for anything that changes by env. No copied prod IDs in a
  public file.
- Expand-contract for destructive destroys.
- `ignore_changes` only with a named reason.

## Errors

- Failed plan is a stop. Do not `-auto-approve` to hide it.

## Testing

- `terraform plan` against the real backend is the default test.
  `terraform plan -lock=false` is not a substitute.
- `terraform test` / terratest only if the repo already has it.

## PR review

- Plan attached or reproducible from the module.
- IAM not widened (`*` actions).
- No secrets in `.tf` / committed `.tfvars`.
- State backend unchanged unless the ticket says so.

## Security

- Least-privilege IAM. Do not widen `*`.
- No access keys in the tree.
- State contains secrets — treat backends as sensitive.

## Always

- `fmt` + `validate` + a plan you read.

## Ask first

- State migration.
- New cloud account or region.
- Destroy of existing resources.

## Never

- Secrets in VCS.
- `apply` without a plan you read.
- Force-unlock as a habit.
- `-auto-approve` as the default path.

## Red flags

- "I'll apply -auto-approve"
- "The secret is just a variable"
- "force-unlock, it's stuck"
