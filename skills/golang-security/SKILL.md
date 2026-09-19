---
name: golang-security
description: use this when writing, reviewing, or auditing Go for exploitable issues — injection, crypto, path, SSRF, cookies, secrets, PII in logs, authn/z — not nil/slice bugs (golang-safety) or test-harness design (golang-testing).
---

# Go security

Rewrite of samber/cc-skills-golang `golang-security` @ `22c58a55`. **Not** a vendor paste. **SKILL only** — no `evals/`, no `scripts/`, no `references/`. Compatible with `security-hardening`: **LLM output is untrusted**; the system prompt is not a boundary.

Pairs with `golang-testing` (race/fuzz proof) and `golang-safety` (non-exploitable panics / slice aliasing). Separate PRs OK. Do not install the samber pack.

## Iron law

**Every trust-boundary crossing gets a control in code.** Validate input, parameterize queries, encode for the sink, fail closed. Upstream validation adjusts severity; it does not dismiss the finding.

## Three questions

1. **Trust boundary** — where does untrusted data enter? (HTTP, uploads, env, other services' rows)
2. **Attacker control** — which inputs reach SQL, shell, HTML, paths, crypto, or outbound HTTP?
3. **Blast radius** — leak, RCE, auth bypass, or DoS if this layer fails?

## Always

| Rule | Go move |
| --- | --- |
| Parameterize every query | `database/sql` / `pgx` placeholders (`$1` / `?`). Allowlist identifiers (`ORDER BY`, columns). Never concat user text into SQL. |
| Exec without a shell | `exec.Command(bin, args...)`. Never `sh -c` / `bash -c` with user text. |
| Encode for the HTML sink | `html/template` (auto-escape). `html.EscapeString` if you must `Fprintf`. |
| Scope file paths | Go 1.24+: `os.Root`. Older: `filepath.IsLocal` + `filepath.Rel`. Never `Clean` + `HasPrefix` alone. |
| Authenticated crypto | AES-256-GCM or ChaCha20-Poly1305. Fresh nonce per seal. `crypto/rand`, not `math/rand`. |
| Slow password hashes | Argon2id preferred; bcrypt OK. Not MD5 / SHA-1 / bare SHA-256. |
| Constant-time secrets | `crypto/subtle.ConstantTimeCompare` or `hmac.Equal`. Not `==`. |
| TLS 1.2+ and verify certs | `MinVersion: tls.VersionTLS12`. No `InsecureSkipVerify`. SSH: `FixedHostKey`, not `InsecureIgnoreHostKey`. |
| Timeouts on HTTP servers | `ReadTimeout` / `WriteTimeout` / `IdleTimeout` / `MaxHeaderBytes`. |
| Secure session cookies | `HttpOnly`, `Secure`, `SameSite=Lax` or `Strict`. |
| Secrets from env or a manager | Fail closed if required secret is empty. |
| Generic client errors | Log details server-side. No stack traces, DSNs, or SQL text to clients. |
| Server-side authn/z | Every handler. Do not trust `X-Forwarded-For` / `X-Is-Admin`. |
| Race-sensitive shared state | `sync.Mutex` / channels. Prove with `go test -race` (`golang-testing`). |

## Ask first

| Topic | Why it is a stop |
| --- | --- |
| New auth / session shape | Trust-boundary widen — same as `security-hardening` |
| New egress or SSRF-shaped fetch | Outbound URL from user input needs an allowlist + no link-local / metadata |
| Uploads / zip extract | ZipSlip, zip bombs, special files |
| Public pprof / debug mux | `/debug/pprof` is a leak if reachable |
| `SameSite=None` or cookie `Domain` | CSRF / cross-site widening |
| Skipping `-race` or fuzz on a security-touching change | Proof belongs with `golang-testing` |
| Review/audit growing write or deploy tools | Review skills should not write — read, report |

Record the decision on the LLD or ticket. Do not self-except.

## Never

| Never | Why |
| --- | --- |
| SQL / command / HTML string-built from user or model text | Injection (CWE-89 / 78 / 79) |
| Hardcoded secrets, DSNs, or JWT keys in source | History is forever |
| `math/rand` for tokens, IDs, or nonces | Predictable |
| DES, RC4, MD5, SHA-1, AES-ECB, or reused GCM nonce | Broken or catastrophic |
| Ignoring crypto / encrypt errors (`_, _ = …`) | Fail-open |
| Rolling your own crypto | Use stdlib / `x/crypto` |
| `gob` of untrusted input | Unsafe deserialization |
| Bind `0.0.0.0` or public mesh from a one-off | Network becomes the client |
| World-writable files (`0777` / `0666`) | Data-class fail |
| PII, tokens, or passwords in logs | `security-hardening` Never |
| Personal finance, mail, password stores, or extra hosts without the operator | Host / account locks |
| Copy `evals/` or `scripts/` into this skill dir | INTAKE quarantine |
| Install the samber pack / marketplace sync | Dual routers; pin stays |

Host and personal-account locks are **Never**, not Ask first.

## Modes

- **Review** — start at the diff, then trace call sites and data flow. A vuln may live outside the hunk. **Read, report, escalate.** Do not grow write/merge tools to “finish the review.”
- **Audit** — cover five domains: (1) injection, (2) crypto and secrets, (3) web / headers / cookies, (4) authn/z, (5) races that break authz. Score DREAD; one fix = one PR. Do not dump a mixed-concern patch.
- **Coding** — write behind Always. Optionally grep new code for concat-SQL, `sh -c`, `InsecureSkipVerify`, and hardcoded keys while implementing.

## Research before reporting

Do not flag a snippet in isolation.

1. Trace the value to its origin (user, constant, internal).
2. Check upstream validation / allowlists / type parse.
3. Note remaining defenses (middleware, `os.Root`, parameterized store).
4. Report with **adjusted severity**, not a silent skip. If you downgrade, leave a short `// security:` comment naming the control.

Defense in depth: every layer still protects itself. A concat reachable only through `parseUserID() int` is medium, not dismissed.

## Severity (DREAD)

| Level | Score | Meaning |
| --- | --- | --- |
| Critical | 8–10 | RCE, full breach, credential theft — fix now |
| High | 6–7.9 | Auth bypass, broken crypto, significant leak — this PR / sprint |
| Medium | 4–5.9 | Session / timing / defense weakening — next pass |
| Low | 1–3.9 | Best-practice drift — opportunistic |

Escalate Critical/High to the operator. Do not bury them in a follow-up with no ticket ID.

## STRIDE at the boundary

For each crossing: spoofing (authn), tampering (integrity), repudiation (audit log), disclosure (encrypt / no PII logs), DoS (timeouts / rate limits), elevation (authz). Score with DREAD. Do not treat STRIDE as a substitute for the **security** LLD/PR gate.

## Compact rules

**Injection / SSRF.** Placeholders for values; allowlist for identifiers. Dynamic `IN` = generated `$n` plus bound args (`sqlx.In` + `Rebind`). Block `file:`, link-local, and metadata hosts on outbound URLs. Prefer JSON with a typed struct over `gob` / `interface{}`.

**Filesystem.** `os.Root` for user paths and zip extract. Cap decompressed size; treat limit-hit as error, not `io.EOF`. Temps via `os.CreateTemp` + `0600`. Dirs `0750`, secret files `0600`.

**HTTP.** Allowlist redirect hosts; reject `javascript:` / `data:`. No public `net/http/pprof`. Reject XML DTD / `ENTITY`. Headers as the app requires (HSTS, CSP, frame, nosniff) — same bar as `security-hardening`.

**Cookies.** Session cookies: `HttpOnly` + `Secure` + `SameSite`. Cookie-store keys from env, not literals.

**Logging.** Structured fields (`log/slog`). Never `%+v` a struct that holds a password or token.

**Not this skill.** Nil panics, typed-nil interfaces, `append` aliasing → `golang-safety`. Table-driven tests, `t.Parallel`, fuzz harness → `golang-testing`. `govulncheck` / lockfile audit → **tester** CI + dependency review, not an install step here.

## Tooling (no skill scripts)

```bash
go test -race ./...
go test -fuzz=Fuzz
```

`gosec` / `govulncheck` belong in **tester** hooks when **security** asks — do not `go install` them as this skill’s job and do not copy vendor installers.

## Roles

| Role | Owns | Does not own |
| --- | --- | --- |
| **security** | This gate at LLD/PR for Go boundaries; skill intake | Writing product tests |
| **builder** | Implementing behind Always; pairing `golang-testing` / `golang-safety` | Self-excepting “just this query” |
| **tester** | `-race` / SAST hooks when they appear | Skipping **security** because CI is green |
| **manager** | After-act | Blessing a ship that skipped the gate |

Workers do not bypass. A green `gofmt` is not a **security** clear.

## Red flags

- “The input is validated upstream, so concat is fine”
- “`filepath.Clean` + prefix is enough”
- “`InsecureSkipVerify` is only for staging”
- “`math/rand` is fine for a reset token”
- “I’ll log the whole user struct”
- “Review will just apply the fix”
- “Install the samber pack to get Go security”

Stop. Classify. Ask or never — do not ship.

## Upstream pin

Intent: samber/cc-skills-golang `skills/golang-security` @ `22c58a55a0a799b901aa251172923180bad9e010` (MIT). Body is a rewrite. See [SOURCES.md](../../SOURCES.md).
