# Public red-team and blue-team agent skill packs (2026-10-18)

- Source: the GitHub REST API (repository metadata, default-branch
  commits, file trees) for every repository listed below; `openclaw
  skills search` against ClawHub; web search summaries for discovery
  only. Ticket `DER-557`.
- Distilled: `2026-10-18`
- Live docs win: each repository's GitHub page. Stars, forks, and
  commit dates move daily. This file is a dated snapshot, not a live
  ranking.

## What it is

A pointer catalog of public agent skill packs (mostly `SKILL.md`
collections for Claude Code and other agents that read Agent Skills)
that cover offensive security (red), defensive security (blue), or
both. Each row names the pack, its maintainer, and the area it
covers. Nothing here is vendored, pinned, or cleared for use. This
repo's own security skills (`security-hardening`, `golang-security`)
are first-party and are not part of this catalog.

## When to read

Read this before you look for a third-party security skill, before
you propose one for [intake](../../../docs/INTAKE.md), or when an
operator asks what public red-team or blue-team packs exist. Open the
live repository before you rely on any number here.

## How to read the tables

- **Verified signal**: stars and forks from the GitHub API on
  2026-10-18, and the date of the latest commit on the default
  branch. These are facts as of that day.
- **Maintained**: a guess from the commit date. `yes` means a commit
  within 90 days, `slowing` within 180 days, and `stale` older than
  that. A recent commit does not prove review quality.
- **Purpose**: the area the pack covers, from its README and its
  skill directory names. It is a summary, not an endorsement.
- **SKILL.md / code files**: counts from the repository file tree.
  Code files are `.sh`, `.py`, `.js`, `.ts`, and `.ps1`. Under the
  intake checklist, any script is untrusted until **security** clears
  it.

## Red team

| Name | URL | Maintainer | Side | Verified signal | Maintained | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| Claude-Red | <https://github.com/SnailSploit/Claude-Red> | SnailSploit (user) | Red | 7.6k stars, 995 forks; last commit 2026-10-12 | yes | Offensive-security methodology library (79 `SKILL.md`, 3 code files) across web, Active Directory, cloud, wireless, and reporting; README scopes it to authorized testing, bug bounty, research, and CTF |
| Claude-BugHunter | <https://github.com/elementalsouls/Claude-BugHunter> | elementalsouls (user) | Red | 5.1k stars, 785 forks; last commit 2026-10-17 | yes | Bug-bounty and external red-team bundle (83 `SKILL.md`, 53 code files, slash commands) built around disclosed-report patterns |
| communitytools | <https://github.com/transilienceai/communitytools> | transilienceai (org) | Red | 577 stars, 84 forks; last commit 2026-07-29 | yes | Skills, agents, and slash commands for penetration testing and bug bounty (50 `SKILL.md`, 187 code files) |
| awesome-skills-security | <https://github.com/Eyadkelleh/awesome-skills-security> | Eyadkelleh (user) | Red | 391 stars, 69 forks; last commit 2026-06-08 | slowing | Security-testing plugins (7 `SKILL.md`) that bundle wordlists and payload lists; no license file |
| SecSkills | <https://github.com/Arenbai/SecSkills> | Arenbai (user) | Red | 258 stars, 29 forks; last commit 2026-09-29 | stale (author says so) | Chinese-language penetration-testing module for Claude Code organized by PTES phases (1 `SKILL.md`); the description says the skill will not be updated further |

## Blue team: security operations, detection, and threat intelligence

| Name | URL | Maintainer | Side | Verified signal | Maintained | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| Google skills (SecOps subset) | <https://github.com/google/skills> | Google (org) | Blue | 21.4k stars, 1.8k forks (whole repo); last commit 2026-10-16 | yes | Product skills for Google technologies; the security subset covers Google SecOps triage, investigation, hunting, cases, and detection engineering, plus GKE and WAF security |
| Elastic agent-skills (security plugin) | <https://github.com/elastic/agent-skills> | Elastic (org) | Blue | 594 stars, 54 forks (whole repo); last commit 2026-09-10 | yes | Official Elastic skills; the security plugin covers alert triage, case management, and detection-rule management |
| splunk-agent-skills | <https://github.com/splunk/splunk-agent-skills> | Splunk (org) | Blue | 60 stars, 11 forks; last commit 2026-09-11 | yes | Official Splunk skills (32 `SKILL.md`) for Splunk search and operations use cases |
| cti-skills | <https://github.com/Liberty91LTD/cti-skills> | Liberty91LTD (org) | Blue | 27 stars, 9 forks; last commit 2026-09-30 | yes | Cyber threat intelligence skills for each stage of the CTI lifecycle, including detection-rule writing (78 `SKILL.md`, 38 code files) |

## Blue team: application security and code audit

| Name | URL | Maintainer | Side | Verified signal | Maintained | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| security-audit-skill | <https://github.com/cloudflare/security-audit-skill> | Cloudflare (org) | Blue | 30.8k stars, 1.9k forks; last commit 2026-09-14 | yes | One multi-phase security-audit skill with independently verified, machine-readable findings; no code files |
| Trail of Bits skills | <https://github.com/trailofbits/skills> | Trail of Bits (org) | Blue | 7.6k stars, 659 forks; last commit 2026-10-15 | yes | Security research and audit workflows (85 `SKILL.md`): audit context building, smart-contract vulnerability scanners, fuzzing guides, supply-chain risk, YARA authoring. Some research skills are dual-use. License CC-BY-SA-4.0 |
| Sentry skills (security subset) | <https://github.com/getsentry/skills> | Sentry (org) | Blue | 1.1k stars, 55 forks (whole repo); last commit 2026-10-15 | yes | Sentry's development skills; the security subset is security review, GitHub Actions security review, and Claude settings audit |
| Ghost Security skills | <https://github.com/ghostsecurity/skills> | Ghost Security (org) | Blue | 413 stars, 25 forks; last commit 2026-09-28 | yes | Application-security skills for coding agents (8 `SKILL.md`) |
| Semgrep skills | <https://github.com/semgrep/skills> | Semgrep (org) | Blue | 328 stars, 31 forks; last commit 2026-07-28 | yes | Skills for using Semgrep from coding agents (3 `SKILL.md`, 7 code files) |
| claude-cybersecurity | <https://github.com/AgriciDaniel/claude-cybersecurity> | AgriciDaniel (user) | Blue | 231 stars, 46 forks; last commit 2026-04-15 | slowing | Code-review skill with specialist agents mapped to OWASP, CWE Top 25, and MITRE references |
| SecOpsAgentKit | <https://github.com/AgentSecOps/SecOpsAgentKit> | AgentSecOps (org) | Blue | 224 stars, 43 forks; last commit 2026-04-15 | slowing | Security toolkit for coding agents (32 `SKILL.md`) aimed at catching vulnerabilities during development |
| security-skills-claude-code | <https://github.com/Security-Phoenix-demo/security-skills-claude-code> | Security-Phoenix-demo (org) | Blue | 80 stars, 10 forks; last commit 2026-09-11 | yes | Plugins for security review, threat modeling, and security assessment (27 `SKILL.md`) |

## Both sides

| Name | URL | Maintainer | Side | Verified signal | Maintained | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| Anthropic-Cybersecurity-Skills | <https://github.com/mukul975/Anthropic-Cybersecurity-Skills> | mukul975 (user) | Both | 34.6k stars, 4.2k forks; last commit 2026-08-31 | yes | Very large library (818 `SKILL.md`) mapped to MITRE ATT&CK, NIST CSF, and other frameworks: forensics, malware analysis, threat hunting, SOC operations, and offensive domains. A user account owns it; the name does not mean Anthropic publishes it |
| Claude-Code-CyberSecurity-Skill | <https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill> | Masriyan (user) | Both | 487 stars, 93 forks; last commit 2026-10-16 | yes | 22 skills (44 code files) across offensive planning, threat hunting, SOC automation, SIEM queries, incident response, and hardening |
| secskills | <https://github.com/trilwu/secskills> | trilwu (user) | Both | 164 stars, 18 forks; last commit 2026-08-06 | yes | Plugin marketplace split into offense, defense (DFIR, SOC, detection), and shared core plugins (94 `SKILL.md`) |

## Thin sources

These packs match the topic but have little verifiable adoption:
under about 20 stars, a few days of history, or both. Treat the
side and purpose as the author's claim.

| Name | URL | Maintainer | Side | Verified signal | Purpose |
| --- | --- | --- | --- | --- | --- |
| secops-claude-skills | <https://github.com/ftrout/secops-claude-skills> | ftrout (user) | Blue | 0 stars; one-day history, 2026-09-18 | SOC skills: triage, detection engineering, hunting, DFIR, intel |
| claude-blue-team-skills | <https://github.com/PolGs/claude-blue-team-skills> | PolGs (user) | Blue | 8 stars; last commit 2026-04-09; no license | SOC analyst and malware-analysis triage skills |
| dfir-skills | <https://github.com/Fuzzdkk/dfir-skills> | Fuzzdkk (user) | Blue | 3 stars; last commit 2026-04-10; no license | DFIR and SOC skills for a forensics workstation |
| accans-sec-skills | <https://github.com/roodlicht/accans-sec-skills> | roodlicht (user) | Both | 4 stars; last commit 2026-05-23 | Profile-selectable skills for AppSec, pentest, blue team, and GRC |
| hacking-skills | <https://github.com/securityfortech/hacking-skills> | securityfortech (org) | Red | 17 stars; last commit 2026-03-15 | Bug bounty, pentest, CTF, and code-review skills |
| audn-ai skills | <https://github.com/audn-ai/skills> | audn-ai (org) | Red (AI systems) | 8 stars; last commit 2026-04-13 | Adversarial testing of the user's own AI agents |
| red-team-agent-skills | <https://github.com/yechao-zhang/red-team-agent-skills> | yechao-zhang (user) | Red (AI systems) | 5 stars; last commit 2026-01-24 | Red teaming of AI agents |
| llm-red-teaming-skill | <https://github.com/puthtipong/llm-red-teaming-skill> | puthtipong (user) | Red (AI systems) | 1 star; last commit 2026-04-15 | Authorized red teaming of LLM applications |

## Adjacent: not skill packs

Often listed beside the packs above, but they ship a framework, a
server, an Action, or a scanner rather than `SKILL.md` content.

| Name | URL | Maintainer | Kind | Verified signal |
| --- | --- | --- | --- | --- |
| PentestGPT | <https://github.com/GreyDGL/PentestGPT> | GreyDGL (user) | Penetration-testing agent framework | 16.0k stars; last push 2026-07-14 |
| hexstrike-ai | <https://github.com/0x4m4/hexstrike-ai> | 0x4m4 (user) | MCP server that drives security tools | 12.9k stars; last push 2026-08-03 |
| claude-code-security-review | <https://github.com/anthropics/claude-code-security-review> | Anthropic (org) | GitHub Action for security review of pull requests | 6.4k stars; last push 2026-02-11 |
| skill-scanner | <https://github.com/cisco-ai-defense/skill-scanner> | Cisco AI Defense (org) | Scanner for agent skills; already named in [intake](../../../docs/INTAKE.md) | 2.6k stars; last push 2026-10-15 |
| pentest-ai | <https://github.com/0xSteph/pentest-ai> | 0xSteph (user) | Penetration-testing framework with agents and an MCP server; no `SKILL.md` | 1.7k stars; last commit 2026-10-07 |
| claude-skills-security-guide | <https://github.com/RationalEyes/claude-skills-security-guide> | RationalEyes (user) | Threat taxonomy for skills as a supply chain | 13 stars; last push 2026-03-30 |

## Indexes

General skill lists with security sections. Star counts are for the
whole list, not its security entries.

| Name | URL | Verified signal |
| --- | --- | --- |
| Anthropic skills (not security-specific) | <https://github.com/anthropics/skills> | 181.8k stars; last push 2026-10-09 |
| ComposioHQ awesome-claude-skills | <https://github.com/ComposioHQ/awesome-claude-skills> | 77.3k stars; last push 2026-09-18 |
| hesreallyhim awesome-claude-code | <https://github.com/hesreallyhim/awesome-claude-code> | 55.9k stars; last push 2026-10-18 |
| sickn33 agentic-awesome-skills | <https://github.com/sickn33/agentic-awesome-skills> | 47.8k stars; last push 2026-10-17 |
| VoltAgent awesome-agent-skills | <https://github.com/VoltAgent/awesome-agent-skills> | 35.9k stars; last push 2026-10-15 |
| OpenAI skills (Codex catalog) | <https://github.com/openai/skills> | 28.1k stars; last push 2026-09-08 |
| travisvn awesome-claude-skills | <https://github.com/travisvn/awesome-claude-skills> | 15.5k stars; last push 2026-04-28 |
| BehiSecc awesome-claude-skills | <https://github.com/BehiSecc/awesome-claude-skills> | 10.3k stars; last push 2026-09-21 |
| securityfortech awesome-security-skills | <https://github.com/securityfortech/awesome-security-skills> | 4 stars; last push 2026-03-29 (thin) |

## Cautions

- **Look-alike repositories.** A GitHub search for "claude skills
  security" returned several repositories named like
  `r09-<list-owner>-awesome-claude-skills-security`. Each claims to
  derive from a popular list, has 38 to 51 stars, zero or one fork,
  and the same push date. That shape suggests inflated stars. They
  are left out on purpose; do not treat them as forks of the lists
  they name.
- **ClawHub.** Searches for pentest, red team, blue team, threat
  hunting, incident response, detection engineering, and security
  audit returned mostly single skills from individual publishers,
  some in near-duplicate listings from one publisher. The CLI output
  shows no download or star counts, and several mirrored entries are
  marked "Not scanned by ClawHub". No ClawHub entry is listed here.
- **Licenses.** Some packs have no license file. Trail of Bits uses
  CC-BY-SA-4.0, which is share-alike. Check the license before any
  rewrite under intake.
- **Skill text runs as instructions.** A red-team pack loaded into a
  general agent changes what that agent will do. Load one only for
  authorized work, and read it first.

## Unknown

- **X.** A site-restricted X search failed with a provider error.
  A general search summary said that Claude-Red and Claude-BugHunter
  were the most shared security packs on X in 2026 and that blue-team
  packs drew less engagement. Post-level likes and bookmarks were not
  verified, so no X figure appears in the tables.
- Whether any pack's content is accurate, safe, or current. Nothing
  was scanned or reviewed for this note.
- Download or install counts. GitHub does not publish them, and the
  ClawHub search output did not show them.
- Packs published only on vendor marketplaces or private registries.

## Do not

- Install a pack from this list with a marketplace command, `npx`, or
  a plugin add. Intake is clone, scan, pin, and rewrite:
  [docs/INTAKE.md](../../../docs/INTAKE.md).
- Copy a `SKILL.md` body, payload list, or script from these packs
  into this repo.
- Remint a pack as a skill id here, or read a star count as a
  security clearance.
- Store tokens or credentials used to query these sources.
