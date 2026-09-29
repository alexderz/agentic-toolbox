# Jev (TypeSafe System One)

- Source: `alexderz/grok-bot-perm` `docs/integrations/typesafe.md` @
  `8b2cfffca35d938337f3af524187e6c998ee3e89`; live TypeSafe docs.
  Related reading (not SoT): Archer Hume,
  [Jev’s Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked/?v=3)
  (2026-09-17); X
  [status/2100555442061820286](https://x.com/4rcherhume/status/2100555442061820286)
- Distilled: `2026-09-28`
- Live docs win: [docs.typesafe.ai](https://docs.typesafe.ai)
  ([llms.txt](https://docs.typesafe.ai/llms.txt)). Hume’s essay does
  not override those pages.

## What it is

TypeSafe **System One** models are decision models for software, not
chat. **Jev** is the flagship. You send `state` plus named typed
questions (**Choice**, **Score**, **Noul**) and get structured answers
code can branch on. Questions in one request share state, run in
parallel, and are independent. No generated prose to parse.

## When to read

Calling Jev from an agent or app. Prefer this note plus live docs over
reminting a TypeSafe skill in this home. For a probe-based guess at
internals, see Related reading — live TypeSafe docs still win.

## Constraints

- **Do not train on Input.** Privacy Policy (2025-11-19) and Models
  page: TypeSafe will not train or fine-tune on customer prompts/input.
  [Privacy](https://typesafe.ai/legal/privacy-policy),
  [Models](https://docs.typesafe.ai/models).
- Public pages fetched 2026-09-19 do **not** say “Telemetry free.” Do
  not invent a telemetry or retention guarantee.
- **Do not** paste live API keys. Env: `TYPESAFE_API_KEY`.
- Access may be waitlisted. Official HTTP uses
  `Authorization: Bearer <key>`, not `x-api-key`.
- Official SDKs: **Python** and **JavaScript/TypeScript** only.
  Community Rust is not on the official SDK page.
- **No** documented sandbox host, webhooks, streaming evaluate, or
  public OpenAPI (as of that fetch). `jev-preview` is a **model alias**,
  not a second base URL.

## Auth and URLs

| Item | Value |
| --- | --- |
| Console | `https://console.typesafe.ai` |
| API root | `https://api.typesafe.ai` |
| Evaluate | `POST /v1/systemone` |
| List models | `GET /v1/models` |
| Header | `Authorization: Bearer $TYPESAFE_API_KEY` |
| Optional env | `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL`, `TYPESAFE_LOG_LEVEL` |

Mint keys from the dashboard after sign-in. `/settings/keys` is inferred,
not independently documented.

## Request

`state` (required): string, object, or array of **text**. No image/audio.
English is strongest.

`questions` (required): nonempty map. Keys are **your** IDs (not sent to
the model). Values discriminated by `type`:

| `type` | Extra | Answer |
| --- | --- | --- |
| `noul` | `instructions`; optional `criteria` `{true, false}` | `noul` ∈ [0,1] = P(yes). No `confidence` |
| `choice` | `instructions`; `criteria` option → rubric | winning `choice`, full `probabilities`, `confidence` |
| `score` | `instructions`; ordered `criteria` array (≥2 levels) | `score` (can sit between levels), `legend`, `probabilities`, `confidence` |

`model` optional. SDK default `jev-latest`. Pin `jev-1.13.0` if you
tuned thresholds.

Response: `model` (may resolve an alias), `answers` (same keys),
`usage.input_tokens`, `usage.output_tokens` (output billed free as of
Models page). SDKs expose `request_id` from `x-typesafe-request-id`.

`GET /v1/models` lists **aliases**. Versioned IDs such as `jev-1.13.0`
are still accepted on evaluate.

## Jev 1.13 limits

From [Models](https://docs.typesafe.ai/models). Limits can change.

| Item | Value |
| --- | --- |
| Versioned ID | `jev-1.13.0` |
| Aliases | `jev-latest` → `jev-1.13.0`; `jev-preview` → same until a preview ships |
| Price | $42 / billion input tokens; output tokens free |
| Rate | 250k tokens/sec **and** 1200 req/min; either excess → `429` |
| Context | 64k / request; 32k for `state` + the single longest question |

Errors: `401` bad key, `422` body, `429` rate, `529` overloaded. SDKs
retry 2 extra times on `408`/`429`/`5xx`, honor `Retry-After` /
`retry-after-ms`. Raw HTTP must retry itself.

## Official SDKs

| | Python | JS/TS |
| --- | --- | --- |
| Package | `typesafe-sdk` (PyPI) | `@typesafe-ai/sdk` |
| Runtime | Python ≥ 3.10 | Node 20+ |
| Call | `client.system_one(state=…, questions=…)` | `client.systemOne({ state, questions })` |
| Types | `Choice`, `Score`, `Noul` | `choice()`, `score()`, `noul()` |
| Changelog at extract | v0.7.0 (2026-09-18) | v0.6.0 (2026-09-15) |

Browser: blocked unless `dangerouslyAllowBrowser: true` (exposes the
key). Keep credentials server-side.

## How to write questions

- One snap judgment per question. Compose in **code**, not one fat prompt.
- Put the full question in `instructions`. IDs are for your code only.
- Structured state: backtick paths, e.g. `` `ticket.messages[0].text` ``.
- Batch every question that shares a state into **one** call. A second
  request only when the next options/state cannot be built yet.
- Gate high-stakes actions on Choice/Score `confidence`, or how close
  `noul` is to 0.5.

## Unknown

- Sandbox/staging API host
- Webhooks, outbound callbacks, streaming evaluate
- Public OpenAPI
- Exact dashboard click-path for keys
- Whether a given account is off the waitlist
- Live numeric rate limits for a given account
- Internal architecture, parameter count, and base model. TypeSafe
  has not published those. Hume’s reconstruction is a probe
  hypothesis, not a disclosure.
- Whether Hume ships reconstruction weights. None were on Hugging
  Face as of 2026-09-28.

## Do not

- Marketplace-install TypeSafe’s skill into this skills home
  (`npx skills add …`). Point at live docs / cookbooks instead.
- Remint this note as `skills/typesafe-ai/`.
- Invent legal or telemetry claims beyond the cited pages.
- Treat Hume’s essay as TypeSafe source of truth for the API,
  architecture, or weights.

## Related reading (speculative)

[Archer Hume, *Jev’s Architecture Unmasked*](https://archerhume.com/posts/jevs-architecture-unmasked/?v=3)
(2026-09-17, ~28 min; `?v=3`). Black-box probe reconstruction of
hosted `jev-1.13.0` (~10,000 API calls in the author’s account),
not TypeSafe’s published architecture. Live docs below remain the
API contract. Open weights for a Hume reconstruction were promised
on X (training takes time) and were **not** on Hugging Face as of
2026-09-28. Same stance as Drex in
[`jev-open-2026-09-27.md`](jev-open-2026-09-27.md): promised, not
shipped.

Author’s proposed picture (labeled by the essay as speculative
where evidence is thin):

- Causal transformer; sparse MoE is the **least certain** part
- Shared-state KV prefix; isolated question branches that do not
  attend to one another
- Listwise option interaction before the choice
- Direct probability readouts, not token generation
- RLCD-style training of the predictive distribution
- API `confidence` is arithmetic on that distribution (Choice:
  how far `p_max` sits above uniform), not a second learned score

Do not copy the essay’s schematic example probabilities as
measurements of Jev. Local open-weight rows that cite this essay
(for example Kev) implement a *Jev-style* interface; they are not
hosted Jev.

## Live docs

[Introduction](https://docs.typesafe.ai/introduction) ·
[Quick start](https://docs.typesafe.ai/introduction/quickstart) ·
[HTTP API](https://docs.typesafe.ai/api) ·
[Models](https://docs.typesafe.ai/models) ·
[State](https://docs.typesafe.ai/concepts/state) ·
[Primitives](https://docs.typesafe.ai/primitives) ·
[Confidence](https://docs.typesafe.ai/confidence) ·
[Python SDK](https://docs.typesafe.ai/sdk/python) ·
[JS SDK](https://docs.typesafe.ai/sdk/javascript) ·
[Legal](https://docs.typesafe.ai/legal)
