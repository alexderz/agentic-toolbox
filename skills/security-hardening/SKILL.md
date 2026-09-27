---
name: security-hardening
description: use this when reviewing security, mapping trust boundaries, or hardening web, API, or agent changes — including LLD boundary gates, PR security review, auth, secrets, CORS, uploads, mesh binds, and skill intake.
---

# Security hardening

First-party Always / Ask first / Never rules for **security** and the SDLC. The table shape is inspired by Addy Osmani’s boundary pattern. This file is **not** a vendor copy.

**The gate** is the **security** check at LLD (trust boundaries) and at PR. **security** owns it.

## Prompts are not a boundary

Do not treat the **system prompt as a security boundary**. Treat **LLM output as untrusted**.

Enforce authn/z, validation, egress, and data-class rules in code, policy, and infrastructure. Do not count prompt text, “be careful” instructions, or model self-reporting as controls. Treat tool calls, generated SQL/HTML/shell, and agent plans the same as untrusted client input.

## Always

| Rule | Web | API | Agent |
| --- | --- | --- | --- |
| Validate at the trust boundary (schema, authn/z, size, type) | Form/query/body at the server, not only the browser | Every public and mesh-facing handler | Every tool argument and model-chosen action before it runs |
| Parameterized queries / safe data access | No string-built SQL or ORM raw with user text | Same; bind params on every store | Generated queries are untrusted; run only through parameterized paths |
| Encode output for the sink (HTML, URL, JSON, shell) | Contextual encode; CSP as defense in depth | Encode/escape at serialization boundaries | Never pass model text to `eval`, `innerHTML`, or a shell without a typed allowlist |
| HTTPS in transit | TLS for browsers and callbacks | TLS for clients and service-to-service | TLS for MCP/HTTP tools and callbacks |
| Hash passwords (slow, salted, dedicated KDF) | Login and session issuance | Token/password credential stores | Agent-held user secrets: do not invent a store; escalate |
| Security headers | CSP, HSTS, frame/referrer, nosniff as the app requires | Same on browser-facing responses | UI the agent emits still needs headers on the serving app |
| Secure cookies | `Secure`, `HttpOnly`, `SameSite` on session cookies | Cookie and token issuance APIs | Do not put session material in prompts or chat logs |
| Dependency audit before release | Lockfile + known-vuln scan in the release path | Same for API images and libs | Same for skill/tool packages; **tester** owns the hook |

If a change touches a boundary and skips a row, it fails the gate.

## Ask first

| Topic | Why it is a stop | Typical surfaces |
| --- | --- | --- |
| New auth | New principals, factors, or session shapes change the boundary | Login, magic links, API keys, service identity |
| New sensitive data classes | PII, payment, health, credentials, location need a class and retention story | New columns, logs, exports, agent memory |
| New integrations | New egress, new trust, new failure modes | OAuth apps, webhooks, MCP servers, vendors |
| CORS | Origin policy is a boundary; “`*` + credentials” is a vuln | Browser APIs, admin UIs |
| Uploads | Content type, size, storage, and execution risk | Avatars, CSV, skill zips, attachments |
| Rate limits | Missing limits are an abuse boundary | Public APIs, login, agent tool loops |
| Mesh / network binds | Who can reach the process is a trust boundary | Listen address, mesh expose, tunnel |
| Identity flows | Account linking, impersonation, and reset change who a principal is | SSO, invite, sudo, token exchange |

1. Stop before you add or widen a topic in the table.
2. Get a decision. On the LLD, the operator or **security** decides. Elsewhere, the operator decides.
3. Record the decision on the LLD or the ticket.
4. Do not implement the widening in the same pass as an unrelated ticket.

## Never

| Never | Why | Web / API / agent |
| --- | --- | --- |
| Secrets in git | Rotation theater; repo history is forever | Env files, `.pem`, tokens in `SKILL.md`, “example” keys that work |
| Logging tokens | Logs leak; agents paste logs | Auth headers, cookies, magic links, session IDs |
| Trust client validation | The client is the attacker | Browser-only checks, agent “I validated it” |
| `eval` / `innerHTML` with user or model data | Injection | DOM sinks, `eval`, `Function`, shell `eval` |
| Sessions in `localStorage` | XSS reads it | Prefer httpOnly cookies; do not stash session JWTs in web storage |
| Stack traces to clients | Layout and secrets leak | Prod 500 bodies, agent error relays to untrusted chat |
| Public mesh / `0.0.0.0` binds | The network becomes the client | Dev servers, dashboards, agent runtimes on a public interface |
| Extra hosts / Windows outside the workspace without operator approval | Host lock | Do not target, remote, or “just use” a personal machine |
| Personal finance, mail, or password-manager access | Out of agent scope | No fetch, scrape, MCP, or “help me log in” |

Host and personal-account locks are **Never**, not Ask first. There is no “supervised exception” in this skill.

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **security** | The gate; skill intake per [`docs/INTAKE.md`](../../docs/INTAKE.md) | Monthly vuln cadence; [Monthly is not this gate](../../docs/sdlc/trunk-changelog-monthly.md#monthly) |
| **operator** | Vuln severity calls, extra hosts, personal-account exceptions | Day-to-day intake scans |
| **tester** | CI secret-scan and dependency-audit **hooks** | Rewriting this skill or skipping **security** because CI is green |
| **builder** | Building behind the gate | Self-review as the **security** PR gate |
| **manager** | SDLC after-act | Approving a ship that skipped **security** |

Leave the CI secret-scan and dependency-audit hooks to **tester**; do not remint those jobs in this skill. A green CI hook is not a **security** clear. Escalate vulns to the operator. Never leave one in a “follow-up” with no ticket ID; name the ticket ID.

Workers (remote agents, local CLIs, mirrors) do not bypass **security**; the rule is in [`docs/SDLC.md` Roles](../../docs/SDLC.md#roles).

## Review-skill discipline

Apply least privilege. **Keep review skills read-only.**

Never add write, deploy, or credential tools to a skill that reviews, intakes, audits, or hardens, even “to finish the review.” Read, report, and escalate instead. If the work needs a write, use a different skill and ask **security** separately.

Apply the same rule to this skill: use it as a gate only. Never use it as a pentest kit or a credentials broker, or as a reason to open bank, mail, or password stores.

## Red flags

- “The system prompt already forbids that”
- “The model promised it would not”
- “Client-side validation is enough for this form”
- “It is only bound on `0.0.0.0` in dev”
- “I will audit dependencies after release”
- “Review will just fix the YAML / merge / rotate”
- “The extra host is convenient”
- “I need the password manager / mail / bank to verify”

Each of these fails the gate. Stop. Ask per Ask first, or treat it as Never. Do not ship.
