# Knowledge distillations

Compressed facts about a model, vendor, API, or platform. **Not skills.**
Skills are procedures under `skills/<id>/SKILL.md` and load by id.
These notes are what to believe about a thing. Live vendor docs win
when they disagree. Notes are MIT unless a file says otherwise.

## Path

```
knowledge/<domain>/<kind>/<slug>.md
```

Do not dump notes in this directory. Do not invent a fourth path
segment until a kind folder already has enough files to hurt.

## Taxonomy

**Domain** (add a row here when you need a new one; do not freehand):

| Domain | For |
| --- | --- |
| `ai` | Models, model vendors, AI APIs |
| `cloud` | Cloud platforms and their services |
| `saas` | Hosted products (Linear, GitHub, …) |
| `lang` | Language/runtime notes that are **not** a language skill |
| `ops` | Shared infra/ops facts (not a product-repo host inventory) |

**Kind** (same rule):

| Kind | For |
| --- | --- |
| `models` | One named model |
| `vendors` | A company or product when the note is not one model |
| `apis` | HTTP/SDK contracts that span models |
| `platforms` | A cloud or SaaS surface |
| `practices` | How we use a thing, not the thing itself |

One topic per file. A second topic gets a new slug.

## Required fields

Every note:

- **Source** — repo path and/or URLs
- **Distilled** — `YYYY-MM-DD`
- **Live docs win** — where to re-fetch
- **What it is** / **When to read**
- **Unknown** — say unknown; do not guess
- **Do not** — secrets, marketplace install, reminting as a skill

## Index

| Note | Path |
| --- | --- |
| Jev (TypeSafe System One) | [`ai/models/jev.md`](ai/models/jev.md) |

## Never

- A second process pack or a `SKILL.md` under `knowledge/`.
- Marketplace `npx skills add` from a distillation.
- Secrets, live API keys, or “telemetry free” claims you did not cite.
- Copying a 400-line vendor extract verbatim. Compress.
