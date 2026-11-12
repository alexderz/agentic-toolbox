# Rule map — `skills/sdlc/references/plan-trial-spec.md`

Item: DER-739 (A7 of DER-712). Procedure:
[A7](../lld.md#a7--design-gate-and-hld-touchpoint).

Old: `docs/sdlc/plan-trial-spec.md` at main c26f424, lines 1–148.
New: `skills/sdlc/references/plan-trial-spec.md`, 150 lines.

A0 moved this file and rewrote links. Line numbers did not change in
that move, so Old L is a c26f424 line and the same line after A0,
before A7. A7 adds Plan step 8 and rewrites two acceptance lines.
Rows below cover every non-blank old line.

Key: **kept**, **route**, **dropped** (owner named), **DER-265**,
**DER-271**. No row uses DER-265 or DER-271.

Clarifications (operator, 2026-09-27): none apply. This file has no
groom-review round and no frontmatter. The verdict row already says
"for example".

This item edits no protected-rules row. The UX review loop stays the
owner at `#ux`.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3 | Heading Plan | kept | L3 |
| 5 | **architect** writes the HLD with the `hld.md` and `track.md` / `chunk.md` templates | kept | L5 |
| 6 | **architect** locks hierarchy, persistence, and worker rules | kept | L6 |
| 7 | **architect** stages each Plan draft on project-main as it is written | kept | L7 |
| 8–10 | Before each commit, **architect** scans staged files for credentials, hostnames or IPs, personal data, local paths, `.env` files, logs, and dumps, and deletes each | kept | L8–10 |
| 11 | **architect** commits | kept | L11 |
| 12 | **architect** pushes project-main | kept | L12 |
| 13 | **manager** posts the HLD path on the Epic with `tracker-sdlc` `comment` | kept | L13 |
| — | HLD review chosen at touchpoint 1 → **manager** sends touchpoint 2; Spec waits for the answer | added (A7). The touchpoint list is owned by `skills/sdlc/SKILL.md#touchpoints` (A1). This step is the Plan action | L14–15 |
| 15–16 | **Item:** do not write a new HLD; **manager** posts one verdict with `tracker-sdlc` `comment` | kept | L17–18 |
| 18–22 | Verdict rows: `honors`, `clarification`, `escalate` (for example a shape change; never edit the HLD quietly) | kept | L20–24 |
| 23 | No HLD to align to: ask the operator, stub or promote | kept. A0 rewrote the link `../SDLC.md` to `../SKILL.md` | L25 |
| 25–26 | In this skills home, `docs/ARCHITECTURE.md` and the SDLC count as the plan | kept. A0 rewrote the path text and the link | L27–28 |
| 28 | Heading Comparables | kept | L30 |
| 30–31 | Before locking shape, **architect** looks; **designer** looks too if there are screens | kept | L32–33 |
| 33–37 | Comparables steps 1–4: 2–4 real examples, the page, the per-example fields, reuse an options map | kept | L35–39 |
| 38 | Cite only real examples. Never invent an "industry standard" | kept | L40 |
| 40 | Skip this page only if the operator waives look-around in writing | kept. A0 rewrote the link | L42 |
| 42 | Never | kept | L44 |
| 44–45 | Never lock Plan shape without 2–4 real comparables unless the operator waived look-around; write the page first | kept | L46–47 |
| 47 | Heading UX. Owner of the review loop and operator acceptance | kept | L49 `#ux` |
| 49–51 | **designer** writes high-level UX and stories in this step; this is not the Spec; no mockups here; mockups are Spec if there is a screen | kept | L51–53 |
| 53 | UX work and mockups both pass this review loop | kept | L55 |
| 55 | **designer** produces the work | kept | L57 |
| 56–58 | A different agent reviews against the written requirements; the reviewer's own taste is not a requirement | kept | L58–60 |
| 59–60 | **designer** fixes; repeat until both agree the work meets the requirements | kept | L61–62 |
| 61–62 | **operator** accepts the work, or writes `UX verification not required`. For mockups, this happens before Groom | kept, retimed (A7). Acceptance of the work (UX and mockups, old L53) is at the design gate. The waiver phrase stays. The link names `#touchpoints` | L63–64 |
| 64 | Never | kept | L66 |
| 66–67 | Never treat designer or architect self-OK as the UX gate. The gate is step 4 | kept. Step 4 is now the design-gate acceptance | L68–69 |
| 68–69 | Never skip mockups for a screen without a written `UX verification not required` | kept | L70–71 |
| 71 | Heading Trial | kept | L73 |
| 73–77 | The Trial is optional proof. `poc/` is a frozen record, never imported into product paths. **security** removes a pushed secret and has it rotated | kept | L75–79 |
| 79–84 | Trial steps 1–4: `poc/` beside the design records, `poc.md`, `README.md`, no vendored copies | kept | L81–86 |
| 85 | **architect** commits and pushes each Trial file as it is written: Plan steps 3–6 | kept | L87 |
| 87 | **Item:** skip the Trial unless the chosen fix is itself uncertain | kept | L89 |
| 89 | Heading Spec | kept | L91 |
| 91–92 | Entry gate: offline `tracker-sdlc` setup check; if it fails, run `sdlc-onboarding` first | kept | L93–94 |
| 94–96 | **architect** writes the LLD; the trust-boundary section is required; `n/a` and why if there is none | kept | L96–98 |
| 97 | **architect** commits the LLD | kept | L99 |
| 98 | **manager** posts the LLD path on the Epic | kept | L100 |
| 100–103 | **Item:** align to the existing LLD as in Plan. **security** still reads the trust-boundary note | kept | L102–105 |
| 105 | Heading Mockups | kept | L107 |
| 107–110 | If people see a screen, **designer** produces 2–3 structurally different mockups | kept | L109–112 |
| 112 | Review and operator acceptance use the UX review loop | route to `#ux` | L114 |
| 114 | No screen: write `n/a` and why. Do not invent pictures | kept | L116 |
| 116 | Heading Security gate | kept | L118 |
| 118–119 | Before Groom or Build, **security** reviews the LLD and any `poc/` for trust boundaries | kept | L120–121 |
| 120–121 | **architect** accepts the LLD, and **security** accepts it on trust boundaries | kept | L122–123 |
| 122 | **operator** accepts the LLD after architect and security | kept, widened (A7): the operator accepts the LLD, UX and mockups at the design gate. Steps 1–2 still precede step 3. The link moves from `#asking-the-human` to `#touchpoints`. A0 had rewritten the old link target | L124 |
| 123 | Start Groom or Build only after step 3 | kept | L125 |
| 125–126 | This review is a gate at Spec. Monthly is not the security gate | kept. The Monthly sentence routes to `trunk-changelog-monthly.md#monthly` | L127–128 |
| 128–129 | If the change touches a boundary, run this review before Build | kept | L130–131 |
| 131 | Heading Documentation | kept | L133 |
| 133–134 | Once the LLD is accepted, builders keep docs current through land. Two surfaces; do not mix their jobs | kept | L135–136 |
| 136–139 | Human and Agent surface table | kept | L138–141 |
| 141–145 | Human docs are for people; agent notes are not tutorials; do not paste the SDLC; update both in the same land; the Build definition of done includes docs | kept. The definition of done routes to `build-review.md#definition-of-done` | L143–147 |
| 147–148 | Skills and technical docs use engineering words. Do not reuse the layperson analogies outside How software gets built | kept. A0 rewrote the link | L149–150 |

## Meaning questions

No open question.

- **MQ1** — Old L61–62 said mockup acceptance happens before Groom. The
  new sentence says the operator accepts the work at the design gate.
  Resolved from the accepted A7 text: the loop already covers UX work
  and mockups (old L53), and Groom still starts only after security-gate
  step 3 (old L123).
- **MQ2** — Old L122 said the operator accepts the LLD "after them".
  The new sentence does not repeat those words. Resolved from the
  accepted A7 text: the new line replaces the old one, and steps 1–2
  still come before step 3.
