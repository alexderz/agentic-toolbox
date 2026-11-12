# Rule map — `skills/sdlc/references/entry-brief-repo.md`

Item: DER-735 (A3).

Old: `docs/sdlc/entry-brief-repo.md` at main c26f424, lines 1–134.
New: [`skills/sdlc/references/entry-brief-repo.md`](../../../../skills/sdlc/references/entry-brief-repo.md) (144 lines).
Key: **kept**, **route**, **replaced**, **dropped**, **new**. "Old L" is a line at main c26f424.

A0 moved this file and retargeted links only. A row marked **kept** is the same rule; an A0 link target is not a rule change. Procedure: [A3](../lld.md#a3--brief-step-and-discover-the-idea).

Protected rows touched: none. The route to `branches-and-lands.md#never` stays a route.

Operator clarifications (2026-09-27): "a person" and "Improvise" do not occur. Gate reasons in parentheses stay examples.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 1 | Title | kept | L1 |
| 3 | Heading Entry | kept | L3 |
| 5–7 | Read-only classification; the classification line goes on the ticket at Brief | kept | L5–7 |
| 9–12 | Chunk or item condition table | kept | L9–12 |
| 14–17 | Unclear → a short look, then ask; how to ask routes to `#asking-the-human` | kept | L14–17 |
| 19–22 | Do not implement; never use the item path to skip the operator; route to `#never` | kept | L19–22 |
| 24 | Heading Brief | kept | L24 |
| 26 | Brief runs before Plan | kept | L26 |
| 28 | Heading Chunk brief | kept | L28 |
| 30–31 | Gather ↔ Refine; skip only for a confirmed brief; do not implement | kept | L30–31 |
| 33–38 | Gather loads `discover-the-idea`; do not copy its loop | kept | L33–38 |
| 39–42 | Refiner loads `yagni`, questions necessity, and works from first principles | replaced (A3 edit 1, R4): runs [`discover-the-idea` Refine](../../../../skills/discover-the-idea/SKILL.md#refine); loads no `yagni`; first principles stay | L39–42 |
| 43–44 | A requirement dies, or a new unresolved point → return to Gather | replaced (R91): return when Refine returns `back to Gather`, with its delta | L43–44 |
| 45–46 | Repeat until the operator confirms a brief Refine did not send back | replaced (A3): `buildable` runs the setup check; the **manager** sends touchpoint 1 once; a correction returns to step 1; a confirm ends chunk Brief | L45–51 |
| 48–50 | Gatherer and refiner ids route to `#step-agents`; no language skill routes to `language-router` | kept | L53–55 |
| 52 | Write Plan from the confirmed brief, never from a raw dump | kept | L57 |
| 54 | Heading End of chunk Brief | kept | L59 |
| 56–60 | Cut project-main; setup check fails → load `sdlc-onboarding`, which writes the tracker files first | replaced (R54, GR18): also commit `brief.md`, `rulings.md` and `asks.md`; the confirmed brief is frozen; only the **manager** changes `brief.md`, on project-main, citing the ask id and logging a ruling. The setup check now runs at chunk Brief step 4; this step runs `sdlc-onboarding` Write on the touchpoint 1 answer when that check failed, and still writes the tracker files first | L61–69 |
| 61–72 | Get the Epic; onboarding that ran lands as its own item before Plan | kept. "Onboarding ran in step 2" still names End step 2, which is the Write | L70–81 |
| 73–74 | **manager** posts the Entry classification on the Epic | replaced (GR18): the comment also names the path and commit of the confirmed brief | L82–84 |
| 76 | Heading Item brief | kept | L86 |
| 78–81 | Always run item Brief unless the ticket says `n/a — split from accepted Spec` | kept | L88–91 |
| 83–110 | Item Brief steps 0–3: branch, troubleshooter, contrarian, manager pick | kept | L93–119 |
| 112–114 | Check the pick; the same-to-a-user row | kept | L120–124 |
| 115 | AFK, headless, or autonomous → the AFK pick | dropped (T2). Owner of auto mode: `skills/sdlc/SKILL.md#asking-the-human` (A1). This row is now the two-way row: the step 3 pick stands and a ruling is logged | L125 |
| 116 | Otherwise ask the operator; the wait blocks this issue only | kept | L126 |
| 118–119 | Contrarian id routes to `#step-agents`; roles route to `#roles` | kept | L128–129 |
| 121 | Heading Repo | kept | L131 |
| 123 | Before Plan, set up what is missing | kept | L133 |
| 125–132 | Repo exists, stub, CI watch, designs in git | kept | L135–142 |
| 134 | Item: confirm the workspace; do not reinvent it | kept | L144 |

## Meaning questions

None open. Old L45–46's "until the operator confirms" is touchpoint 1 in L47–51, one confirmation per loop. Old L115's AFK pick is not rewritten into a second procedure here.
