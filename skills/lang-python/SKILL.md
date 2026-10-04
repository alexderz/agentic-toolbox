---
name: lang-python
description: use this when the change is Python and you need the toolchain pointer — routes to modern-python. do not use as a second Python body. do not use for other languages.
---

# Python (router)

**This id routes.** Load `modern-python`. Do not remint uv/ruff/ty/pytest
advice. No `scripts/`. `modern-python` is first-party MIT.
Python row and the process skills that may load with it: `language-router` [Map](../language-router/SKILL.md#map), [Load-with list](../language-router/SKILL.md#load-with-list).

## Iron law

**`modern-python` is the Python skill.** Do not invent a parallel guide.

## Combined verify (after modern-python)

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check
uv run ty check .
```

If the tree is still pip/poetry/mypy, **Ask first** before migrating. That
stop lives in `modern-python`.

## Combined PR checklist

- Deps changed only via `uv add` / `uv remove` (lockfile in the diff).
- No `pickle` / `yaml.load` / `eval` / `subprocess` with `shell=True` on untrusted input.
- Tests cover the new branch; no live network unless the test is marked so.
- Types: no new `# type: ignore` without a named reason.

## Never

- A second Python skill that restates `modern-python`.
- `pip install` / activating venvs / hand-editing dep lists.
- Marketplace-installing a vendor Python pack into this home.
