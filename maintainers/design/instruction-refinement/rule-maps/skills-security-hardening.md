# Rule map — `skills/security-hardening/SKILL.md`

Item: DER-316 (E5).

Old: `skills/security-hardening/SKILL.md` at main 7a11696, lines 1–101.
New: [`skills/security-hardening/SKILL.md`](../../../../skills/security-hardening/SKILL.md).
Disposition: **kept** (same rule, this file), **route** (the rule lives in
its owner; this file links it), **dropped** (duplicate, owner named),
**DER-265**, **DER-271**. "Old L" = line in the old file; "L" = line in
the new file.

Protected rows touched: `security-hardening` Never and Ask first. Every
table row in both sections is kept byte-identical; row counts are equal
(Never 11, Ask first 10, header and separator included). **security**
reads this item at Review. Operator clarifications (2026-09-27): only
"gate reasons in parentheses are examples" has a subject here (MQ3).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1–4 | Front matter: name, description | kept verbatim | L1–4 |
| 6 | Title | kept | L6 |
| 8 | First-party Always / Ask first / Never; table shape from Osmani's boundary pattern; not a vendor copy | kept; "rules" added after "Never" | L8 |
| 10 | **security** owns this gate at LLD (trust boundaries) and at PR | kept; now also defines the name "the gate" (standard 3), used everywhere after | L10 |
| 10 | Escalate vulns to the operator | dropped (duplicate; owner in this file: old L78, new L77) | — |
| 10 | **tester** owns CI secret-scan and dependency-audit hooks; do not remint those jobs here | kept; moved beside the Roles table, which holds the tester row | L77 |
| 12 | Heading "Prompts are not a boundary" | kept | L12 |
| 14 | System prompt is not a security boundary; LLM output is untrusted | kept, imperative | L14 |
| 16 | Enforce controls in code, policy, infrastructure; prompt text, "be careful", model self-report are not controls; treat tool calls, generated SQL/HTML/shell, agent plans as untrusted client input | kept; second sentence imperative | L16 |
| 18 | Heading "Always" | kept | L18 |
| 20 | Summary: validate, parameterize, encode, HTTPS, hash, headers and cookies, audit | dropped (duplicate; owner: the Always table in this file, L20–29, one row per item) | — |
| 22–31 | Always table | kept byte-identical | L20–29 |
| 33 | Change touching a boundary and skipping a row fails the security LLD/PR gate | kept; "the **security** LLD/PR gate" → "the gate" (defined L10) | L31 |
| 35 | Heading "Ask first" (protected) | kept | L33 |
| 37 | Stop and get a decision (the operator, or **security** on the LLD) before adding or widening any topic | kept, as steps 1–2; the parenthesis becomes a stated condition (standard 8) (MQ2) | L46–47 |
| 39–48 | Ask first table (protected) | kept byte-identical | L35–44 |
| 50 | Do not implement the widening in the same pass as an unrelated ticket; record the decision on the LLD or ticket | kept, as steps 4 and 3; "“Ask first” means" dropped, the steps now say it | L48–49 |
| 52 | Heading "Never" (protected) | kept | L51 |
| 54–64 | Never table (protected) | kept byte-identical (MQ1) | L53–63 |
| 66 | Host and personal-account locks are Never, not Ask first; no "supervised exception" | kept verbatim | L65 |
| 68 | Heading "Roles" | kept | L67 |
| 70–71 | Roles table header | kept | L69–70 |
| 72 | **security** owns this gate at LLD and PR and skill intake (`docs/INTAKE.md`); not Monthly vuln cadence (Monthly is not this gate) | kept; "This gate at LLD (trust boundaries) and PR" → "The gate" (defined L10); intake → route link to owner `docs/INTAKE.md`; Monthly → route link to owner `docs/sdlc/trunk-changelog-monthly.md#monthly` | L71 |
| 73–75 | operator, tester, builder rows | kept verbatim | L72–74 |
| 76 | **manager**: SDLC after-act; not blessing a ship that skipped security | kept; "Blessing" → "Approving" (no metaphor, standard 8) | L75 |
| 78 | Escalate vulns to the operator; do not bury them in a "follow-up" with no ticket ID | kept; "Never … ; name the ticket ID" names the allowed action (standard 7), from the old condition | L77 |
| 80 | Workers (remote agents, local CLIs, mirrors) do not bypass this gate | route (owner: `docs/SDLC.md#roles`, "They do not bypass **security**"); examples kept (MQ4) | L79 |
| 80 | A green CI hook is not a security clear | kept | L77 |
| 82 | Heading "Review-skill discipline" | kept | L81 |
| 84 | Least privilege; review skills should not write | kept, imperative (MQ5) | L83 |
| 86 | A reviewing, intake, audit or hardening skill must not grow write, deploy or credential tools "to finish the review"; read, report, escalate; a write needs a different skill and a different security ask | kept; "Never … Read, report, and escalate instead" puts the allowed action beside the never (standard 7) | L85 |
| 88 | Same rule for this file: a gate, not a pentest kit, credentials broker, or reason to open bank, mail, password stores | kept, imperative | L87 |
| 90 | Heading "Red flags" | kept | L89 |
| 92–99 | Eight red-flag quotes | kept verbatim | L91–98 |
| 101 | All of these fail the gate. Stop. Ask or never; do not ship | kept; "Ask or never" names both sections (MQ6) | L100 |

## Meaning questions

- **MQ1** — Standard 7 wants an allowed action beside every never; the
  protected Never rows must stay kept. Resolved from the text: the rows
  stay byte-identical and no allowed action is added, because the item
  adds no rule. Rows 3, 4, 5, 7 and 8 already name one, in the row or in
  the Always or Ask first tables; rows 1, 2, 6 and 9 stay as they were.
- **MQ2** — Old L37 "(the operator, or **security** on the LLD)" can read
  as "either one decides anywhere" or "the operator decides, and
  **security** can also decide on the LLD". Resolved from the text: the
  parenthesis names **security** only for the LLD, so step 2 says: on the
  LLD, the operator or **security** decides; elsewhere, the operator
  decides. Both readings give that result.
- **MQ3** — "LLD (trust boundaries) and PR" differs from the SDLC index,
  which names **security**'s gates "Spec (trust boundaries) and Review".
  Renaming a gate is an MQ trigger. Resolved from the text: kept
  verbatim, no reading chosen; the parenthesis is a gate reason, so it
  is an example (operator clarification, 2026-09-27).
- **MQ4** — The owner's examples are "(agents, CI bots)"; this file's are
  "(remote agents, local CLIs, mirrors)". Dropping them could narrow who
  the rule covers. Resolved from the text: the route keeps this file's
  examples, adds no condition, and links the owner.
- **MQ5** — Old L84 "should not write" could read as advice. Resolved
  from the text: old L86 says "must not grow write … tools", so the rule
  is a requirement; "Keep review skills read-only" says the same.
- **MQ6** — Old L101 "Ask or never". Resolved from the text: the two
  choices are the file's Ask first and Never sections, named as such.
