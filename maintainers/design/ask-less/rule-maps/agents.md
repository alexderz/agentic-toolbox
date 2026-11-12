# Rule map — root `AGENTS.md`

Item: DER-735 (A3).

Old: `AGENTS.md` at main c26f424, lines 1–76.
New: [`AGENTS.md`](../../../../AGENTS.md) (76 lines).
Key: **kept**, **route**, **replaced**, **dropped**, **new**. "Old L" is a line at main c26f424.

A0 retargeted SDLC links in this file. A row marked **kept** is the same rule. A3 changes the Refine row only. Procedure: [A3](../lld.md#a3--brief-step-and-discover-the-idea).

Protected rows (writing standard, Public-repo rule): old L16, L18, L20–32. Every one of those rows is **kept**, unchanged, at the same lines. Check: `diff <(git show c26f424:AGENTS.md | sed -n 16,32p) <(sed -n 16,32p AGENTS.md)` → empty. **security** reads them at Review.

Operator clarifications (2026-09-27): "Improvise" and "a person" do not occur in this file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3–5 | Shared skills home; Claude Code stays on this file | kept | L3–5 |
| 7–8 | Git is the source of truth; no skill body only on a mirror | kept | L7–8 |
| 10–14 | Toolbox users skip `maintainers/`; repo work reads `maintainers/AGENTS.md` | kept | L10–14 |
| 16 | Heading Public repo | kept, protected | L16 |
| 18 | Public, open-source repo | kept, protected | L18 |
| 20–27 | Deliverables: outside readers; no names, private URLs, hostnames, credentials, or session leftovers; bare ticket ids are fine | kept, protected | L20–27 |
| 28–30 | Agent context may be informal: civil and credential-free | kept, protected | L28–30 |
| 31–32 | Commit messages, PR descriptions, and tags are public | kept, protected | L31–32 |
| 34 | Heading How to load | kept | L34 |
| 36–38 | Do not paste bodies; read the path or pack it | kept | L36–38 |
| 40–45 | Load table through the Requirements row (`discover-the-idea`) | kept | L40–45 |
| 46 | Refine row: read `skills/yagni/SKILL.md` | route (R4): read [`discover-the-idea` Refine](../../../../skills/discover-the-idea/SKILL.md#refine). Do not load `yagni`. The owner states the same prohibition (`It loads no yagni`); this line adds no further condition | L46 |
| 47–63 | The other load-table rows | kept | L47–63 |
| 65 | Heading Intake | kept | L65 |
| 67–68 | Complete security intake before third-party content | kept | L67–68 |
| 70 | Heading Related | kept | L70 |
| 72–76 | Related links | kept | L72–76 |

## Meaning questions

None open. The Refine row is a route to the refiner section, not a second copy of the checklist.
