# CI hooks — first cut

Thin plan for what to wire **first**. **No skill bodies.**

Owner: **tester** (tooling pick). **security** still owns intake.
**architect** owns the candidate list.

## Wire first (fmt / lint only)

Run **only** when matching files appear on the PR:

| Tool | When |
| --- | --- |
| **ruff** | Python appears |
| **gofmt** | Go appears |
| **shellcheck** | Shell scripts appear |
| markdown / prettier | **Optional skip** this cut |

Do **not** gate on third-party skill bodies yet. Empty `.gitkeep` dirs
and unpinned vendor ids are not a CI fail.

First-party `security-hardening` is already pinned. Hooks do **not**
special-case it beyond normal path globs.

## Pre-commit vs GHA

Prefer **GitHub Actions on PR** if local hooks are painful. **tester**
picks the exact action, image, and versions. Local pre-commit is
optional, not required for this cut.

## Success

A PR **fails if format is dirty** (ruff / gofmt / shellcheck as
applicable). No secret scan in this first cut — park for later
(**security** / **tester**).

## Non-goals (this cut)

- SkillSpector in CI — intake stays [INTAKE.md](INTAKE.md) /
  **security**, before a body lands
- Full test suites
- Vendor skill SHA verification in CI — stays **security** +
  [SOURCES.md](../SOURCES.md) until more pins exist
- Secret scan / dependency-audit hooks (**tester** owns those later; see
  `security-hardening`)

## Later (not this cut)

Secret scan, dep audit, a CI echo of SkillSpector only if **security**
asks, SHA-pin check once more vendor rows are pinned, prettier after the
fmt gate exists.
