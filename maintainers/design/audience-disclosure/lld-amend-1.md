# LLD amendment 1 — Audience procedure file; `pr-lens` route

- Slug: `audience-disclosure` · LLD: [lld.md](lld.md) · Groom:
  [groom.md](groom.md) (frozen; G1 = DER-353, G2 = DER-355, G4 = DER-354)
- Date: `2026-09-28`
- Trigger: two findings from Build on DER-353 (G1)
- Status: architect proposes. It needs a **security** re-read (rule
  text moves between files; a new first-party skill file) and an
  operator yes on the new file (writing standard 9).

## A1. `sdlc-onboarding` over its cap

### Facts

All counts wrap prose at 72 columns. Table rows and link-only lines
are not wrapped.

| File | Old | Builder draft as delivered | Honest at 72 columns | Cap |
| --- | --- | --- | --- | --- |
| `skills/sdlc-onboarding/SKILL.md` | 200 | 242 (one line per paragraph, rejected) | 274 (`_alt/`, probe already moved out) | 250 |
| `skills/security-hardening/SKILL.md` | 100 | 160 | about 207: the old text keeps its own style and stays at 100, and the new Disclosure section wraps to about 107 lines instead of 60 | 250 (LLD budget 175) |
| `docs/sdlc/branches-and-lands.md` | 69 | 119 | 119: its long lines are link-only or old table rows | 120 |

`security-hardening`'s 160 hides the same problem. Its old text uses
one line per paragraph as house style. The new Disclosure section
copied that style, and honestly wrapped it is about 47 lines longer.
It still fits the 250 cap. So the "15 spare lines" do not exist, and
the LLD budget of ≤175 was wrong.

### Options

| Option | `sdlc-onboarding` | Other files | Verdict |
| --- | --- | --- | --- |
| (a) Move Discover, Propose and Write into Disclosure | about 216 | `security-hardening` about 265, over its cap. That puts onboarding procedure in a security skill, which blurs one owner per rule. | Reject |
| (b) Move the Audience procedure into `skills/sdlc-onboarding/audience.md`; leave a short `## Audience` route in `SKILL.md`; move the probe back from Disclosure into `audience.md` | about 215 | `audience.md` about 87 (no cap); `security-hardening` about 189 | **Recommend** |
| (c) Trim existing onboarding text | Needs 24 or more lines cut from rules that are not this chunk's, and every cut risks meaning | — | Reject |
| (d) Raise the `sdlc-onboarding` cap to 280 | 274 | none | Honest, but it grows the file every Brief loads, and the cap is the operator's call. Fallback if (b) is refused. |

### Precedent for (b)

- `skills/tracker-sdlc/adapters/*.md`: first-party skill-local files,
  read by path from `sdlc-onboarding`.
- `skills/buying-researcher/references/*.md` (first-party): linked from
  its `SKILL.md` and read on demand.
- Loading: agents read `skills/<id>/SKILL.md` by path (root
  `AGENTS.md` "A skill") and follow its links. The Claude Code skill
  loader also serves extra files from a skill's directory.
- `docs/INTAKE.md` covers only third-party content and `scripts/`. A
  first-party `.md` is prose, and needs no intake. The `SOURCES.md`
  row for `sdlc-onboarding` says "prose only, no scripts/". It gains
  "Audience procedure in `audience.md`".
- Writing standard 6, one hop: every link that needs the procedure
  points at `audience.md` directly, never at the route.

### The change (replaces LLD B3's `## Audience` block)

1. New `skills/sdlc-onboarding/audience.md`:
   - H1 `# Audience`, then one line: "The `## Audience` area of
     [`sdlc-onboarding`](SKILL.md). When it runs: its
     [When](SKILL.md#when) table."
   - H2 `## Check`, `## Discover`, `## Probe`, `## Propose` and
     `## Write`, with LLD B3 text word for word. The probe text is
     LLD B3's, moved back from Disclosure.
   - Its links resolve from its own directory: `SKILL.md#branch`,
     `../security-hardening/SKILL.md#disclosure` and
     `#before-a-repo-goes-public`, and its own `#probe`.
2. `SKILL.md` keeps everything else from B3: the `description` clause,
   Names, the When row, the Propose step 6 clause and the Never
   change. Its `## Audience` becomes:

   ```markdown
   ## Audience

   Records whether this repo's pushes are public, in `## Audience` of
   the governing `AGENTS.md`. Its Check, Discover, Propose and Write:
   [audience.md](audience.md). Read that file whenever the When table
   runs Audience.
   ```

   The anchor `#audience` stays, so the G3 and V2 lists do not change.
3. `security-hardening`: delete `### Probe`. The Disclosure intro
   links `../sdlc-onboarding/audience.md` for "whether a repo's pushes
   are public".
4. Links retargeted to `audience.md`, for one hop:
   - `branches-and-lands` Before a push step 1 → `../../skills/sdlc-onboarding/audience.md`
     (G1).
   - `entry-brief-repo` Audience Check → `../../skills/sdlc-onboarding/audience.md#check`
     (G2).
   - `writing-standard` Rule-owners row "`## Audience` record and
     companion location" → `skills/sdlc-onboarding/audience.md` (G2).
5. Every file is wrapped at 72 columns, prose included, in new text.
   Old `security-hardening` text keeps its style; only lines this
   chunk adds are wrapped. No one-line paragraphs in new text.

### New budgets (at 72 columns)

| File | Budget | Cap |
| --- | --- | --- |
| `skills/sdlc-onboarding/SKILL.md` | ≤220 | 250 |
| `skills/sdlc-onboarding/audience.md` (new) | ≤95 | none; new file |
| `skills/security-hardening/SKILL.md` | ≤195 | 250 |
| `docs/sdlc/branches-and-lands.md` | ≤120 | 120 |

V1 counts honest lines: new prose at no more than 72 columns. A rule
map records `audience.md` as moved text (B3 → new path), not new rules.

## A2. Unowned V4 hit: `skills/pr-lens/SKILL.md:245`

Old: "Labels, summaries, or titles built from anything but this
repository's diff or code: no internal hostnames, URLs, credentials,
personal data, or other repositories' names. On a public repository an
attached diagram is public."

It restates list A and B categories, so it is a second owner (V4). Its
"URLs" (all of them) and "other repositories' names" are narrower
pr-lens rules. They stay, so the meaning does not change.

New: one bullet, the same four lines. `pr-lens` is at its 250-line cap,
so the count must not grow.

```markdown
- Labels, summaries, or titles built from anything but this
  repository's diff or code: no URLs, no other repositories' names, and
  nothing on [Disclosure](../security-hardening/SKILL.md#disclosure)
  list A or B. On a public repository an attached diagram is public.
```

Meaning check: the old text banned internal hosts, credentials and
personal data in every repo, public or private. The new text keeps
that: it names lists A and B with no audience condition.

- Owner: G2 (DER-355), the routes item. It links to G1's
  `#disclosure`, and G2 ← G1 already holds. No new blocker.
- `pr-lens` is vendor-derived: a light pass with a change map
  (writing standard, Rule maps 6), and the `SOURCES.md` row gains
  "Wording edit DER-286, pins unchanged". **security** reads it at
  G2's Review.
- V4's pattern then matches only `security-hardening` Disclosure.

## Tracker and gates

- `groom.md` stays frozen. No new item and no new blocker, so this is
  not a late insertion. It is **two ticket edits**: the **manager**
  posts `comment`s with the changed Outcome, Acceptance and Verify.
  - On DER-353 (G1): A1 items 1–5, the new budgets, V2 adds
    `audience.md#check` and `#probe`, and `SOURCES.md` gains the
    `sdlc-onboarding` note.
  - On DER-355 (G2): A1 item 4's two retargets, A2 (the `pr-lens`
    route, the change map, the `SOURCES.md` note), and the gate reason
    "vendor-derived `pr-lens`".
- **security**: re-reads this amendment before DER-353 resumes
  (probe and procedure move files; new skill file), then reads both
  items at Review as planned.
- **operator**: yes to the new file `audience.md` (writing standard 9),
  or picks (d). Until then, DER-353 waits (a wait on that issue).
