# Rule map — `docs/sdlc/trunk-changelog-monthly.md`

Item: DER-304 (C7). A later item that edits this file appends its own section.

Old: `docs/SDLC.md` at main 7a11696, lines 870–900.
New: [`docs/sdlc/trunk-changelog-monthly.md`](../../../../docs/sdlc/trunk-changelog-monthly.md).
C1 (DER-298) moved these lines word for word; the only C1 change was the
Conventions link. Disposition: **kept** (same rule, this file),
**route** (the rule lives in its owner; this file links it), **dropped**
(duplicate, owner named), **DER-265**, **DER-271**. "Old L" = line in
old `docs/SDLC.md`; "L" = line in the new file.

| Old L | Rule | Disposition | New location |
| --- | --- | --- | --- |
| 870 | Heading Trunk | kept; H3 → H2 at C1; anchor `#trunk` | L3 |
| 872–874 | After the chunk's items are on project-main, merge project-main to trunk | kept; precondition line, then step 1 | L8, L10 |
| 873 | **trunk** = the repo's protected default, usually `main` | kept as a one-line definition at first use | L10–11 |
| 874 | That merge is the coherent integrate | kept; name defined in step 1 | L11 |
| 874 | CHANGELOG may wait for the Changelog step | kept | L15 |
| 875 | **manager** transitions the Epic to `done` with `tracker-sdlc` | kept; same actor, own step | L12 |
| 875–876 | Delete project-main after it is on trunk | kept; step 3, after the merge in step 1 | L13 |
| 876 | Delete project-main if **manager** cancels the chunk | kept; parenthesis → if/then (standard 8) | L15–16 |
| 878–879 | Incoming item with no project-main: already on trunk after Review; step `n/a` | kept; if/then, placed first so the steps follow "Otherwise" | L5–6 |
| 881 | Heading Changelog | kept; anchor `#changelog` | L18 |
| 883–885 | Coherent chunk on trunk: promote `CHANGELOG.md` Unreleased into a dated chunk heading; template `changelog.md`; see Conventions | kept; condition → action row. Link retargeted from `conventions.md#name-formats` (C1) to `conventions.md#changelog-and-connection`, the section that holds the dated heading format | L22 |
| 887 | Incoming item already on trunk: keep the Unreleased line from Build | kept; condition → action row | L23 |
| 888–889 | Promote it with the next Changelog pass: a later chunk, or a dated heading that lists that ticket and the trunk SHA | kept; parenthesis → colon, both forms and the "or" word for word (MQ2) | L23 |
| 889–890 | Do not invent a chunk heading just to close a lone item | kept as "Never write a chunk heading only to close a lone item"; allowed action named beside it: leave the line under Unreleased (standard 7) | L23 |
| 892 | Heading Monthly | kept; anchor `#monthly` | L25 |
| 894 | Vuln / updates / new solutions review | kept; merged with L899–900 "cadence review of vulns/updates/new solutions" into one sentence | L32 |
| 894 | Template `monthly.md` | kept as "Write it from template `monthly.md`" | L32–33 |
| 894–895 | Recurrence note only until **manager** / **operator** cut a Task | kept word for word (MQ1) | L33–34 |
| 895–896 | No watcher, no cron required | kept as "Monthly needs no watcher and no cron" | L34 |
| 898 | Monthly is **not** the security gate | kept; owner of this rule (writing standard, Rule owners); placed first in the section (standard 7) | L27 |
| 898–899 | **security** already gated trust boundaries at Spec and Review | kept | L27–28 |
| 899–900 | Monthly is not a substitute for those gates | kept; the allowed action is named beside it: "Never defer a Spec or Review security check to Monthly; **security** runs it at that gate" (MQ3) | L28–30 |

Clarifications (operator, 2026-09-27): none of the five occurs in old
L870–900; nothing to apply.

Old L878–879 depends on the incoming-item branch and land rule. That
rule is owned by
[`branches-and-lands.md#branches`](../../../../docs/sdlc/branches-and-lands.md#branches)
(C8) and is mapped there. This file does not restate it.

## Meaning questions

- **MQ1** — Old L894–895 "Recurrence note only until **manager** /
  **operator** cut a Task" has two readings: the Monthly recurs as a
  note until a Task is cut for it; or a Monthly's findings stay a note
  until a Task is cut. "/" can also mean either role or both.
  Resolved from the text: the sentence is kept word for word, so the
  rewrite picks no reading and the meaning cannot shift. Filing a Task
  is a tracker write, which only the manager does
  (`docs/SDLC.md#tracker`), under either reading. Making the fragment
  an imperative (standard 8) needs the operator to pick a reading.
- **MQ2** — Old L888–889 lists the next Changelog pass in parentheses
  ("a later chunk, or a dated heading …"). Resolved from the text: the
  two forms and the "or" are kept word for word after a colon; no "for
  example" and no "only" is added. The parentheses clarification (gate
  reasons are examples) does not apply: this is not a gate reason.
- **MQ3** — Is "Never defer a Spec or Review security check to Monthly;
  **security** runs it at that gate" a new condition? Resolved from the
  text: it restates old L900 "not a substitute for those gates" in the
  words of the Spec copy ("a gate, not a later monthly note",
  `plan-trial-spec.md#security-gate`) and the Review copy ("not deferred
  to Monthly", `build-review.md#review`, old L867). The owner now holds
  the whole rule, so those copies can become routes that add no
  condition (standard 5). **security** already gates at Spec and Review
  (`docs/SDLC.md#roles`); no actor, gate or approval changes.
- **MQ4** — Old L875–876 gives no order between the Epic transition and
  deleting project-main. Resolved from the text: steps 2 and 3 follow the
  old sentence order; the only old constraint, delete after project-main
  is on trunk, holds because step 3 follows step 1. Neither is a gate.

No open MQ.
