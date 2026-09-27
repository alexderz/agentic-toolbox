# Rule map — `docs/sdlc/plan-trial-spec.md`

Item: DER-301 (C4). A later item that edits this file appends its own
section.

Old: `docs/SDLC.md` at main 7a11696, lines 612–698 and 955–958.
New: [`docs/sdlc/plan-trial-spec.md`](../../../../docs/sdlc/plan-trial-spec.md).
Disposition: **kept** (same rule, same meaning, reworded to the
standard), **route** (the rule lives in its owner; this file links it),
**dropped** (duplicate, owner named), **DER-265**, **DER-271**. "Old L"
= line in old `docs/SDLC.md`; "New L" = line in the new file.

Clarifications (operator, 2026-09-27): none apply. The file has no
groom-review round, no "a person", no "Improvise". Gate reasons in
parentheses become "for example" lists (New L20).

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 612 | Heading Plan | kept, H2 `#plan` (C1) | L3 |
| 614 | **architect** commits the HLD to git | kept, numbered | L9 (step 3) |
| 614–615 | **manager** posts the HLD path on the Epic with `tracker-sdlc` `comment` | kept, numbered | L10–11 (step 4) |
| 615–616 | Lock hierarchy, persistence, and worker rules | kept; actor **architect** (MQ1) | L7–8 (step 2) |
| 616–617 | Use `sdlc-artifacts` templates `hld.md` and `track.md` / `chunk.md` | kept; actor **architect** (MQ1) | L5–6 (step 1) |
| 619 | Before locking shape, **architect** looks at how others have done it | kept | L29 |
| 619–620 | **designer** too, if there are screens | kept; parenthesis → sentence | L30 |
| 620–621 | 2–4 real examples; page `comparables.md` | kept, numbered | L32–33 |
| 621–622 | Per example: who, what they did, what we steal, what we will not copy, a link | kept | L34–35 |
| 622–623 | Reuse the brief's options map if it exists; still write this page | kept; "the confirmed brief" (the artifact, not the Brief step) | L36 |
| 623–624 | Skip only if the operator waives look-around in writing; link Asking the human | kept; link `../SDLC.md#asking-the-human` | L39–40 |
| 624–625 | No invented "industry standard" | kept; allowed action beside it | L37 |
| 627–628 | **designer**: high-level UX and user stories in the same step (`ux-design`, `ux.md` / `user-story.md`); not the Spec | kept | L49–51 |
| 629–631 | Loop (UX work and mockups): designer produces; a different agent reviews against the written requirements (function, stated taste/shape; not the reviewer's taste); designer fixes until those agents agree | kept, numbered; this file's `#ux` is the owner (writing standard, Rule owners) | L54–61 |
| 631–632 | **then** the **operator** accepts, or writes `UX verification not required` | kept (owner `#ux`) | L62–63 |
| 633 | Architect and designer do not self-approve | kept, merged into the first Never bullet (same rule) | L67–69 |
| 633–634 | Skip mockups here; those are Spec if there is a screen | kept | L51–52 |
| 636 | **Item:** do not write a new HLD; read the existing one | kept | L13 |
| 636–638 | **manager** posts `honors` / `clarification` (small, in place) / `escalate` on the ticket with `tracker-sdlc` `comment` | kept; list → condition table | L13–19 |
| 638–640 | A real shape change (new parts, new trust boundary, new screen, several tickets) escalates to a chunk, not a quiet HLD edit | kept; parenthesis → "for example" (clarification); allowed action beside the never | L20 |
| 640–641 | Nothing to align to: ask (stub vs promote) | kept; "ask" = the operator via `#asking-the-human` (MQ2) | L21 |
| 641–642 | This skills home: `docs/ARCHITECTURE.md` + "this file" count as the plan when the change is the process itself | kept; "this file" meant old `docs/SDLC.md`, now the SDLC index and its step files (MQ3) | L23–25 |
| 644 | Heading Trial | kept, H2 `#trial` | L73 |
| 646 | Only if needed; evidence in git; template `poc.md` | kept; "optional proof" from the index Steps row; "only if needed" unchanged (MQ4) | L75–76 |
| 648 | **Item:** skip unless the chosen fix is itself uncertain | kept | L78 |
| 650 | Heading Spec | kept, H2 `#spec` | L80 |
| 652–653 | Entry gate: offline `tracker-sdlc` setup check; fail → `sdlc-onboarding` first | kept | L82–83 |
| 655 | **architect** commits the LLD to git | kept, numbered | L88 (step 2) |
| 655–656 | **manager** posts its path on the Epic with `tracker-sdlc` `comment` | kept, numbered | L89–90 (step 3) |
| 656–657 | Template `lld.md`; trust-boundary section required; `n/a` + why if none | kept; actor **architect** (MQ1) | L85–87 (step 1) |
| 659 | If people see a screen, **designer** produces mockups | kept, H3 `#mockups` | L99–100 |
| 659–662 | 2–3 structurally different mockups (`ux-design`, `mockup.md`) in whatever medium this agent has (markdown, HTML, canvas, image, or an attached design tool — plus a git snapshot) | kept; list wording unchanged (MQ5) | L100–102 |
| 662–664 | Same review loop as Plan: agents agree, **then** the **operator** accepts or writes `UX verification not required` | route (owner: `#ux`) | L104 |
| 664–665 | No screen: `n/a` and why; do not invent pictures | kept | L106 |
| 667–669 | Before Groom/Build, **security** reviews the LLD for trust boundaries (authn/z, secrets, egress, data class, who may write what) | kept, H3 `#security-gate`, numbered; the list is a definition, not a condition | L110–111 |
| 669 | This is a gate | kept | L118 |
| 669 | Not a later monthly note | route (owner: `docs/sdlc/trunk-changelog-monthly.md#monthly`, "Monthly is not the security gate") | L118–119 |
| 669–670 | Do not skip to Build without it when the change touches a boundary | kept; allowed action beside it | L121–122 |
| 672–673 | **Accept the LLD** (architect + **security** on trust boundaries) before Groom/Build | kept; stated per MQ7 (operator, 2026-09-27): architect and security accept, then the operator; moved after the security review it closes | L112–116 (steps 2–4) |
| 673–674 | If people see a screen, **designer** mockups (`mockup.md`) are part of Spec | kept, merged with L659 (same rule) | L99 |
| 674–675 | The **operator** accepts those mockups, or writes `UX verification not required`, before Groom | kept in the owner `#ux`; "before Groom" moved there | L62–63 |
| 675–676 | Then Documentation is in force | dropped (owner: `#documentation`, whose first line "Once the LLD is accepted" holds the trigger); removes a forward reference | — |
| 678–679 | **Item:** align to the existing LLD as in Plan; clarification in place; shape change → escalate | kept; link `#plan` | L92–93 |
| 679–680 | **security** still reads the trust-boundary note; `n/a` + why if the item does not touch a boundary | kept; parenthesis → sentence | L93–95 |
| 682 | Heading Documentation (after Spec) | kept, H2 `#documentation` (C1) | L124 |
| 684–685 | Once the LLD is accepted, builders keep docs current through land; two surfaces, do not mix their jobs | kept | L126–127 |
| 687–690 | Surface table: Human, Agent | kept, unchanged | L129–132 |
| 692 | Human docs are for people; agent notes are enablement, not tutorials | kept; metaphor "enablement" → "enable future agents" | L134–135 |
| 693 | Do not paste the SDLC into product docs | kept | L135 |
| 693–694 | Update both in the same land as the change | kept | L135–136 |
| 694 | Build DoD includes docs current with the item | route (owner: `docs/sdlc/build-review.md#definition-of-done`) | L136–138 |
| 696–698 | Skills, templates, technical docs use engineering words; no layperson analogies outside How software gets built | kept; link `../how-software-gets-built.md` (C1) | L140–142 |
| 955–956 | Never: designer or architect self-OK as the UX gate; skip mockups for a screen without a written `UX verification not required` | kept (owner `#ux`); allowed action beside each | L65–71 |
| 957–958 | Never: lock Plan shape without 2–4 real comparables unless the operator waived look-around in writing | kept; allowed action beside it | L42–45 |

UX copies collapsed into `#ux` (LLD Duplicate owners: Old L660–666,
L673–676, L955–956): the loop and operator acceptance are whole in
L54–71; `#mockups` holds one route (L104); `#spec` holds none.

## Meaning questions

- **MQ1** — Old L615–617 and L656–657 have no actor for "Lock …", "Use
  templates …" and the LLD template. Resolved from the text: the
  same sentences give the HLD and LLD to **architect**, and the index
  `#roles` row gives **architect** "Design, HLD/LLD". No second reading.
- **MQ2** — Old L640–641 "ask". Resolved from the text: the index
  `#asking-the-human` is where the SDLC asks, and it asks the operator.
- **MQ3** — Old L641–642 "this file" meant `docs/SDLC.md` when written.
  After C1 the sentence sat in `plan-trial-spec.md`, so "this file" had
  changed referent. Resolved from the text and the DER-298 review: the
  SDLC (`docs/SDLC.md` and its step files), which is what old "this
  file" held. Scope unchanged: still under **Item:**, still "when the
  change is the process itself".
- **MQ4** — Old L646 "Only if needed" has no checkable condition
  (standard 2). Resolved: wording kept; defining "needed" would add a
  condition. The index Steps row already says "Optional proof".
- **MQ5** — Old L661–662 "— plus a git snapshot" may attach to the whole
  medium list or only to the design tool. Resolved: wording and
  punctuation kept verbatim, so neither reading is chosen and meaning is
  unchanged.
- **MQ6** — Old L637 "clarification (small, in place)". Resolved: kept
  as "small clarification, made in place"; where "in place" is (HLD or
  ticket) is not named, as before.

- **MQ7** — Old L672 "**Accept the LLD** (architect + **security** on
  trust boundaries)" had two readings: (a) the architect accepts the LLD
  and security accepts its trust boundaries; (b) acceptance is also the
  operator's, as index `#asking-the-human` lists "accepting … the
  detailed design" as an operator ask. Resolved by operator 2026-09-27
  (Q5): the architect and security accept the LLD first, then the
  operator. New L112–116 state that order; the process is unchanged.

No open MQ.

## DER-278

Proof-of-concept code stays in the repo as a frozen record. Changed lines
only. Old = project-main 88455d8; "Old L" = line there; "L" = line in
the new file.

| Old L | Rule | Disposition | L |
| --- | --- | --- | --- |
| 5–6 | **architect** writes the HLD with templates `hld.md`, `track.md` / `chunk.md` | kept; rewrapped to one line (cap) | L5 |
| 7–8 | **architect** locks hierarchy, persistence, and worker rules in the HLD | kept; rewrapped to one line (cap) | L6 |
| 9 | **architect** commits the HLD to git | changed (MQ8): stages each Plan draft on project-main as it is written | L7 |
| — | Before each commit, scan every staged file, binary files included, for credentials, hostnames or IPs, personal data, local paths, `.env` files, logs, data dumps; remove each hit from the stage | new (MQ8); this file owns it, no earlier owner | L8–10 (step 4) |
| — | **architect** commits | new (MQ8); split from old L9 | L11 (step 5) |
| — | **architect** pushes project-main | new (MQ8); `branches-and-lands.md#land-path` Durability routes here | L12 (step 6) |
| 10–11 | **manager** posts the HLD path on the Epic | kept; renumbered step 7; rewrapped to one line | L13 |
| 23–25 | This skills home: `docs/ARCHITECTURE.md` and the SDLC count as the plan | kept; rewrapped to two lines (cap) | L25–26 |
| 39–40 | Skip the comparables page only if the operator waives look-around in writing | kept; rewrapped to one line (cap) | L40 |
| 44–45 | Never: lock Plan shape without 2–4 real comparables | kept; rewrapped (cap) | L44–45 |
| 49–52 | **designer** writes high-level UX and stories; not Spec; no mockups here | kept; rewrapped to three lines (cap) | L49–51 |
| 67–71 | Never: self-OK as the UX gate; skip mockups without `UX verification not required` | kept; rewrapped to four lines (cap) | L66–69 |
| 75–76 | Optional proof; only if needed; evidence in git; template `poc.md` | kept; "evidence in git" now covers the note and code in `poc/` (MQ9) | L73, L79–85 |
| — | Note and code are a frozen record, not product code, not instructions to load; never import or merge `poc/` into product paths; Build rebuilds if the trial proves out | new (MQ9); this file owns it; allowed action beside the never | L73–76 |
| — | A secret found in a pushed Plan or Trial file: **security** removes it and has it rotated; the one edit a frozen `poc/` allows | new (MQ12) | L76–77 |
| — | **architect** makes `poc/` beside the chunk's design records, in the folder that holds its HLD; in this skills home `maintainers/design/<chunk-slug>/poc/` | new (MQ10); actor (MQ13) | L79–80 (step 1) |
| — | **architect** writes `poc/poc.md` from template `poc.md`, trial code beside it | new; the template use is old L76; actor (MQ13) | L81 (step 2) |
| — | **architect** writes `poc/README.md` stating the record rule and the secret rule | new (MQ9, MQ12); actor (MQ13) | L82 (step 3) |
| — | Link to sources; never copy vendored dependencies or build output into `poc/` | new (MQ9); allowed action beside the never; actor (MQ13) | L83–84 (step 4) |
| — | Commit and push each Trial file as written, per Plan steps 3–6 | new (MQ8); backward link, no second owner; actor (MQ13) | L85 (step 5) |
| 78 | **Item:** skip unless the chosen fix is itself uncertain | kept, unchanged | L87 |
| 89–90 | **manager** posts the LLD path on the Epic | kept; rewrapped to one line (cap) | L98 |
| 110–111 | **security** reviews the LLD for trust boundaries | changed (MQ11): "the LLD and any `poc/`" | L118–119 |
| 114–115 | **operator** accepts the LLD after them | kept; rewrapped to one line (cap) | L122 |
| 140–142 | Engineering words; no layperson analogies outside How software gets built | kept; rewrapped to two lines (cap) | L147–148 |

Length: 142 → 148 (cap 150). This file is a C1 move, so K2 does not apply.
Every rewrap keeps the words; only line breaks move.

### Meaning questions (DER-278)

- **MQ8** — Old L9 committed the HLD with no push rule;
  `branches-and-lands.md#land-path` pushed project-main only after each
  land. Resolved by the operator, 2026-09-27: Plan drafts and Trial code
  are committed and pushed as they are written, and the pushing agent
  first scans for credentials, hosts or IPs, and data dumps. The Review
  round of 2026-09-27 (security BLOCK) set the order: scan the staged
  files, binary files included, before each commit, so no commit that is
  later pushed holds a hit; the scan list adds personal data, local paths,
  `.env` files and logs. The architect is the pushing agent in Plan,
  since Plan steps name only the architect as a writer.
- **MQ9** — Old L75–76 kept evidence in git and was silent on code; the
  people doc said to throw the scratch away. Resolved by the operator,
  2026-09-27: keep the code in `poc/` with its own `README.md` (frozen
  record, not product code, never imported or merged into product
  paths, Build rebuilds, a record and not instructions); no vendored
  dependencies or build output, link to sources.
- **MQ10** — Where `poc/` lives. Resolved by the operator, 2026-09-27:
  beside the chunk's design records, wherever those live; DER-271 decides
  that place; this repo keeps `maintainers/design/<chunk>/poc/`; no new
  `.agents/design/` default. "In the folder that holds its HLD" is from
  the text: at Trial time the HLD is the only design record that must
  exist (LLD and `groom.md` come later), and the old `sdlc-artifacts`
  row put the PoC note "next to the HLD".
- **MQ11** — Old L110–111 had **security** read only the LLD. Resolved
  by the operator, 2026-09-27: **security** reads `poc/` at Spec.
- **MQ12** — A frozen `poc/` and a secret found after a push conflict.
  Resolved in the Review round of 2026-09-27 (security): **security**
  removes the secret and has it rotated; that removal is the one edit a
  frozen `poc/` allows. Rotation, because git history keeps the pushed
  commit.
- **MQ13** — Old L75–76 named no actor for the Trial. Resolved from the
  text: Trial sits between Plan and Spec, whose design writer is the
  **architect** in every step, and standard 1 needs a role on each
  step. No other role gains or loses work.

No open MQ.
