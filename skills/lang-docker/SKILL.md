---
name: lang-docker
description: use this when writing or reviewing Dockerfiles, *.dockerfile, or compose files. do not use as a substitute for shell-safety on a real .sh file.
---

# Dockerfile

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. No `scripts/`. Real `.sh` files still
load `shell-safety`.

## Iron law

**Non-root. Pinned bases. No secrets in layers.**

## Tooling / verify

```bash
docker build -t tmp-check .
docker compose config    # when compose changed
# hadolint if the repo already has it
```

Grep the Dockerfile for `curl |`, `latest`, and `ENV`/`ARG` that look
like keys.

## Idioms a linter misses

- Multi-stage so compilers die in the builder stage.
- `COPY --from` with explicit paths.
- `.dockerignore` covers `.git` and secrets.
- `ARG` for build-only; `ENV` for runtime. Neither holds secrets.
- One process per container. Do not add a supervisor "to run two things"
  unless compose already defines that pattern.
- `HEALTHCHECK` only if the project already uses them.
- `RUN` apt: update + install + clean in one layer if that is the
  file's style. No `|| true` on apt.

## Errors

- A failed `RUN` must fail the build.

## Testing

- Build the image.
- If `CMD`/`ENTRYPOINT` changed, run a throwaway container far enough
  to prove the binary starts.
- `docker compose config` must parse.

## PR review

- Base pin: digest preferred when the project already pins digests.
- `USER` set?
- Secrets in any layer (including deleted files — layers keep history)?
- `COPY` scope. Privileged flags in compose.

## Security

- No `curl | sh`.
- No `privileged: true` as a default.
- No publish on `0.0.0.0` without asking.
- Secrets via BuildKit secret mounts, not `ENV`.

## Always

- Pin. Non-root. `.dockerignore`.

## Ask first

- Running as root to "make it work."
- Publishing ports on all interfaces.
- Adding a second process manager.

## Never

- Secrets in `ENV` or baked files.
- `latest` as the only pin.
- Privileged mode as a default.
- `curl | sh` in a `RUN`.

## Red flags

- "Need root for apt"
- "We'll put the key in ENV for now"
- "latest is fine for CI"
- `COPY . .` with no `.dockerignore`
