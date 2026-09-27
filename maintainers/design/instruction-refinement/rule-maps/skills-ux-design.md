# Change map: skills/ux-design/SKILL.md

Old: `skills/ux-design/SKILL.md` at main 7a11696, lines 1–109 (the same
at project-main 120d298). New: `skills/ux-design/SKILL.md`, 109 lines.

Light pass (vendor-derived, LLD area F): naming, dedupe, real defects.
Changed lines only. Upstream attribution (old L12–14) is unchanged. No
upstream text is added. `SOURCES.md` changes only the `ux-design` Notes
cell, which gets the LLD note appended.

Key: **renamed**: a banned or non-index name is replaced with the index
name. **route**: the copy is replaced with a link to its owner.
**kept**: the rule stays in this file with new wording. **fixed**: a
real defect.

| Old L | Rule | Disposition | New L |
| --- | --- | --- | --- |
| 3 | Description: "then human", "skip the human gate" | renamed: `operator` (index `#roles`) | 3 |
| 9–10 | Templates list | fixed: names the owning skill `sdlc-artifacts`, which holds the templates | 9–10 |
| 19–21 | Iron law: "the human accepts" | renamed: `operator`; rewrapped | 19–21 |
| 25–26 | Deliverable "the human can look at" | renamed: `operator`; rewrapped | 25–27 |
| 45 | Keep variants "until the human has picked" | renamed: `operator` | 46 |
| 62 | Resume the same designer | route: [subagents `#step-agents`](../../../../docs/sdlc/subagents.md#step-agents), which owns the `designer_id` and `ux_reviewer_id` resume | 63–64 |
| 64 | Heading "agents, then human" | renamed: `operator` | 66 |
| 66–67 | Step 1: designer produces | route: [plan-trial-spec `#ux`](../../../../docs/sdlc/plan-trial-spec.md#ux) owns the loop | 68–69 |
| 68–69 | UX reviewer is a different subagent; resume `ux_reviewer_id` | route: plan-trial-spec `#ux` ("a different agent") and subagents `#step-agents` (id, resume) | 63–64, 68–69 |
| 69–70 | Reviewer reads brief, stories, and taste/shape that is a requirement | kept, now step 1 | 71–72 |
| 71 | "Can the person finish the job" | renamed: "the user" (the product's user, not the approver) | 73 |
| 77–78 | Designer fixes; loop until the reviewer agrees on the requirements | route: plan-trial-spec `#ux` | 68–69 |
| 78 | "or they disagree and need the human" | kept, now step 2; `operator` | 79–80 |
| 79–82 | Then ask the operator: show variants, recommend by requirement | kept, now step 3; link text fixed to the heading "Asking the operator" (anchor unchanged) | 81–83 |
| 82–83 | "what to reply"; do not continue until they answer | route: `docs/SDLC.md#asking-the-human` step 6 and template `ask-human.md` ("What to reply") | 81–83 |
| 83 | Unless the operator wrote `UX verification not required` | route: plan-trial-spec `#ux` owns operator acceptance and the waiver | 68–69 |
| 89 | Agent review before human | renamed: `operator` | 89 |
| 103 | Never show the human before agents agree | renamed: `operator` | 103 |
| 107 | Red flag "show the human" | renamed: `operator` | 107 |

## Not changed, for the owner

- Variants (old L42): "default **3** … (cap 5)". Plan-trial-spec
  `#mockups` says "2–3 structurally different" mockups. The two caps
  differ. Changing either changes a rule, so this pass leaves both.

## Meaning questions

None. Every route target holds the whole routed rule; no rule changes.
