# Change map — `README.md`

Item: DER-337 (G47). Light pass (LLD "Behavior: rule-map format"):
changed lines only. Old = project-main 120d298. "Old L" = line in the
old file; "L" = line in the new file. No rule changes meaning; people
docs are not agent text.

| Old L | Change | Why | L |
| --- | --- | --- | --- |
| 24, 26–29 | Role jobs copied from the SDLC index `#roles` table | G47: role tables = the index's seven roles and jobs | 24, 26–29 |
| 35 (fix-forward) | Appended "Internal work skips PRs: it lands by local merge." after the CONTRIBUTING link; L34 ("PRs welcome", maintainer link) unchanged | Review: the manager row's "no PRs" read as contradicting "PRs welcome"; the role table stays word for word (G47) | 35 |
| 31–32 | "Improvise beyond predefinition when the work needs it." → "If no listed skill fits the task, do the work without one. Never create a new skill id mid-task." Remint sentence kept | Operator clarification 2026-09-27 (LLD "Behavior: work areas") | 31–32 |

## Checks

- Role table equals `docs/SDLC.md` L25–33 byte for byte.
- K3 (names that apply to people docs): no "improvise", "orchestrator",
  "official copy", "parent agent/session", "a person".
- K7: every relative link and anchor resolves.
- K10: added lines hold no hostnames, IPs, ports, paths or tokens.
