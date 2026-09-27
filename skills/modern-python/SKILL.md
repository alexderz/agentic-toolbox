---
name: modern-python
description: use this when creating, configuring, or migrating a Python project or standalone script — uv, ruff, ty, pytest; do not reach for pip, Poetry, mypy, or black unless the operator keeps legacy.
---

# Modern Python

First-party. **MIT.** Id: `modern-python`. **SKILL.md only.** No `scripts/`.
Not a vendor paste. Tool facts from the public uv, ruff, ty, and pytest docs.

Load-with list and `lang-python` pointer: `language-router` [Family rules](../language-router/SKILL.md#family-rules), [Map](../language-router/SKILL.md#map).

## Iron law

**`uv add` / `uv remove` change dependencies. `uv run` runs tools. Do
not activate a venv or hand-edit dependency lists.**

On new work, use Python 3.12+, uv, ruff (lint **and** format), ty, pytest.
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

| Never | Instead | Why |
| --- | --- | --- |
| Marketplace `npx skills add` / plugin install | Follow [INTAKE.md](../../docs/INTAKE.md) | Intake owns third-party skills |
| `scripts/` in this skill dir | Keep this skill `SKILL.md` only | Intake quarantine |
| Hand-edit `pyproject.toml` to add/remove deps | `uv add` / `uv remove` | `uv.lock` is the install truth |
| Secrets in `pyproject.toml`, scripts, or lockfiles | Leave them out; see [`security-hardening`](../security-hardening/SKILL.md#never) | History is forever |
| Live network in tests unless marked | Mark each test that needs the network | Default tests stay offline |

## Decision

| Doing | Path |
| --- | --- |
| One file + deps | PEP 723 script |
| App, not published | `uv init` then groups |
| Importable package | `uv init --package` |
| Existing tree | Migrate; if it already ships, Ask first |

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

`uv add` owns `[project].dependencies` and the dev group. Never type
packages into `pyproject.toml` by hand; run `uv add`.

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

No lockfile. If the code spans more than one file, use `pyproject.toml`.
Use `uv run --with pkg` only as a one-off probe; add project deps with `uv add`.

## Migration

Migrate only when asked.

| From | Do | Then delete |
| --- | --- | --- |
| `requirements.txt` + pip | `uv init`; `uv add` each reviewed package | `requirements*.txt`, old `venv/`; commit `uv.lock` |
| `setup.py` / `setup.cfg` | `uv init`; `uv add` from install_requires; copy name/version into `[project]` | `setup.py`, `setup.cfg` |
| flake8 + black + isort | `uv remove` them; drop their config; `uv add --dev ruff` | `.flake8`, `[tool.black]`, `[tool.isort]` |
| mypy / pyright | `uv remove`; `uv add --dev ty` | `mypy.ini`, `pyrightconfig.json`, `[tool.mypy]` |

If a requirement has odd markers or is a VCS dep, stop and do it by hand.
Never import a lock you have not read; read it first.

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
