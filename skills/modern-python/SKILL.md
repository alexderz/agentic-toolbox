---
name: modern-python
description: use this when creating, configuring, or migrating a Python project or standalone script — uv, ruff, ty, pytest; do not reach for pip, Poetry, mypy, or black unless the operator keeps legacy.
---

# Modern Python

First-party. **MIT.** Id: `modern-python`. **SKILL.md only.** No
`scripts/`. Not a vendor paste. Tool facts from the public uv, ruff, ty,
and pytest docs.

Compatible with `tdd`, `verify-before-done`, `pr-review`,
`security-hardening`. Optional pointer: `lang-python`.

## Iron law

**`uv add` / `uv remove` change dependencies. `uv run` runs tools. Do
not activate a venv or hand-edit dependency lists.**

New work: Python 3.12+, uv, ruff (lint **and** format), ty, pytest.
Keep pip / Poetry / mypy / black only when the operator says so.

## Always

| Rule | Why |
| --- | --- |
| `uv add` / `uv remove` / `uv sync` | `uv.lock` is the install truth |
| `uv run <cmd>` | Project env without `source .venv/bin/activate` |
| Commit `uv.lock` | Reproducible installs |
| ruff for lint and format | One tool, not flake8 + black + isort |
| ty for types | Replaces mypy / pyright on new work |
| pytest for tests | Not `unittest` as the default |
| PEP 723 metadata for a one-file script | No `requirements.txt` for a script |
| Pair with `security-hardening` on untrusted input | `eval`, `pickle`, `yaml.load`, `shell=True` |

## Ask first

| Topic | Why |
| --- | --- |
| Keep pip / Poetry / mypy / black / pyright | They may own that workflow |
| Python older than 3.12 on **new** work | Pin is 3.12+ |
| Migrate a shipping tree | Confirm before deleting `requirements.txt` / `setup.py` |
| `uv pip install` | Bypasses the lockfile |
| Publish, extra indexes, private registries | Trust and credentials |
| pre-commit / hook installers | **tester** owns CI; do not add hook packs here |

## Never

| Never | Why |
| --- | --- |
| Marketplace `npx skills add` / plugin install | [INTAKE.md](../../docs/INTAKE.md) |
| `scripts/` in this skill dir | Intake quarantine |
| Hand-edit `pyproject.toml` to add/remove deps | `uv add` / `uv remove` |
| Secrets in `pyproject.toml`, scripts, or lockfiles | History is forever |
| Live network in tests unless marked | Default tests stay offline |

## Decision

| Doing | Path |
| --- | --- |
| One file + deps | PEP 723 (below) |
| App, not published | `uv init` then groups |
| Importable package | `uv init --package` |
| Existing tree | Migration — Ask first if it already ships |

## Tools

| Tool | Purpose | Replaces |
| --- | --- | --- |
| **uv** | Deps, venv, run, lock, build | pip, virtualenv, pip-tools, pipx, Poetry |
| **ruff** | Lint + format | flake8, black, isort, pyupgrade |
| **ty** | Types | mypy, pyright |
| **pytest** | Tests | unittest as the default |

Scanners and CI hooks are **tester / security**, not this skill.

## New project

```bash
uv init myproject
cd myproject
uv add httpx
uv add --dev pytest ruff ty
uv sync
uv run pytest
uv run ruff check .
uv run ruff format --check
uv run ty check .
```

Package:

```bash
uv init --package myproject
cd myproject
uv sync
uv build
```

`uv add` owns `[project].dependencies` and the dev group. Do not type
packages into `pyproject.toml` by hand.

## PEP 723 scripts

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx

print(httpx.get("https://example.com").status_code)
```

```bash
uv init --script myscript.py
uv add --script myscript.py httpx
uv run myscript.py
```

No lockfile. Multi-file? Use `pyproject.toml`. `uv run --with pkg` is a
one-off probe, not a project dep.

## Migration (only when asked)

| From | Do | Then delete |
| --- | --- | --- |
| `requirements.txt` + pip | `uv init`; `uv add` each reviewed package | `requirements*.txt`, old `venv/`; commit `uv.lock` |
| `setup.py` / `setup.cfg` | `uv init`; `uv add` from install_requires; copy name/version into `[project]` | `setup.py`, `setup.cfg` |
| flake8 + black + isort | `uv remove` them; drop their config; `uv add --dev ruff` | `.flake8`, `[tool.black]`, `[tool.isort]` |
| mypy / pyright | `uv remove`; `uv add --dev ty` | `mypy.ini`, `pyrightconfig.json`, `[tool.mypy]` |

Odd markers or VCS deps: stop and do them by hand. Do not import a lock
you have not read.

## uv (short)

| Command | Use |
| --- | --- |
| `uv init` / `uv init --package` | App vs package |
| `uv add <pkg>` / `uv add --dev <pkg>` | Deps |
| `uv remove <pkg>` | Drop a dep |
| `uv sync` | Install from the lock |
| `uv run <cmd>` | Run in the project env |
| `uv run --with <pkg>` | Temporary extra |
| `uv build` | Wheel/sdist; publish is Ask first |

## Verify

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check
uv run ty check .
```

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **builder** | This toolchain on product work | Adding `scripts/` to this skill |
| **tester** | ruff/fmt hooks when `.py` appears | A second Python skill |
| **security** | Intake | Day-to-day `uv add` |
| **manager** | After-act | Blessing a marketplace Python pack |

## Red flags

- “I’ll pip install just this once”
- “source the venv”
- “hand-edit pyproject to add the package”
- “keep requirements.txt and uv”
- “copy a vendor Python skill pack”

Stop. Use uv. Or Ask first.

## License

MIT. First-party. See repo `LICENSE` and [SOURCES.md](../../SOURCES.md).
