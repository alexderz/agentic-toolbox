# Vendor-neutral cybersecurity skill packs

**Surveyed 2026-10-07.**

This page catalogs open cybersecurity skill packs for AI coding agents:
`SKILL.md`-style packs (plus a few rules-file and playbook packs) that
Claude Code, Codex, Cursor, Gemini CLI, opencode, and similar agents can
load. It lists each pack, says what it is for, and outlines what it
contains, so you can pick one to evaluate without researching the same
repositories twice.

This is a catalog, not an endorsement. Nothing listed here is vendored
into this repository or approved for use. Community packs must be vetted
before any agent or bot loads them; see
[Supply-chain risk](#supply-chain-risk-and-skill-scanners).

## Scope

A pack is **vendor-neutral** when it is useful without a vendor tenant:
no SIEM, SecOps, EDR, or cloud-security subscription is needed to get
value from it. Packs that only operate one vendor's product are listed
under [Excluded](#excluded). Full SOC platforms and vendor MCP servers
are out of scope.

Open-source tools are fine. A pack that drives Semgrep, Ghidra,
Volatility, or `nmap` is still vendor-neutral.

## How this was checked

The starting point was a research scan from the same day that covered
73 repositories, 57 of them vendor-neutral candidates. The scan used
GitHub repository and code search, the major awesome lists for agent
skills, and the skills.sh registry. A search on X was attempted, but
every request was rate-limited, so the survey has no X data.

Every repository named on this page was then rechecked on GitHub on
2026-10-07:

- **Stars, license, and last commit** come from the GitHub API. The
  license is GitHub's SPDX detection of the root license file.
  `NONE` means no license file; `Other` means GitHub could not classify
  the file, and the license the scan read by hand appears beside it.
- **Last commit** is the committer date of the newest commit on the
  default branch (UTC).
- **Skill count** is the number of `SKILL.md` files in the default
  branch tree. It can include templates and per-agent duplicates; those
  cases are noted.
- **Catalogs** come from each repository's actual folder layout, plus
  its README where the README groups the skills.
- **Agent targets** are what the README, description, or GitHub topics
  claim. They weren't tested.

Anything that couldn't be confirmed is marked **unverified**. Stars and
commit dates change daily; treat them as a snapshot.

## Shortlist at a glance

The shortlist is ranked by depth, maintainer credibility, and fit for
vendor-neutral work, roughly in that order.

| # | Pack | Focus | Skills | License | Stars | Last commit |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [mukul975/Anthropic-Cybersecurity-Skills](#1-mukul975anthropic-cybersecurity-skills) | Broad: offense, defense, DFIR, cloud, GRC | 818 | Apache-2.0 | 33,913 | 2026-08-31 |
| 2 | [trailofbits/skills](#2-trailofbitsskills) | Code audit, static analysis, fuzzing, smart contracts | 85 (security subset smaller) | CC-BY-SA-4.0 | 7,414 | 2026-09-28 |
| 3 | [cloudflare/security-audit-skill](#3-cloudflaresecurity-audit-skill) | Multi-phase code audit with verified findings | 1 (plus 14 phase guides) | MIT | 25,983 | 2026-09-14 |
| 4 | [Masriyan/Claude-Code-CyberSecurity-Skill](#4-masriyanclaude-code-cybersecurity-skill) | Broad, one skill per discipline | 22 | MIT | 467 | 2026-09-07 |
| 5 | [briiirussell/cybersecurity-skills](#5-briiirussellcybersecurity-skills) | Audits, red, blue, purple, compliance | 29 (plus 29 Cursor adapters) | MIT | 412 | 2026-05-27 |
| 6 | [ljagiello/ctf-skills](#6-ljagielloctf-skills) | Capture-the-flag challenges | 11 | MIT | 3,402 | 2026-09-13 |
| 7 | [SnailSploit/Claude-Red](#7-snailsploitclaude-red) | Offensive security and exploit development | 79 | MIT | 7,337 | 2026-09-19 |
| 8 | [meltedinhex/analyst-ai-pack](#8-meltedinhexanalyst-ai-pack) | Malware analysis, reverse engineering, hunting | 118 (plus 1 template) | Apache-2.0 | 21 | 2026-07-07 |
| 9 | [teamdfir/protocol-sift](#9-teamdfirprotocol-sift) | DFIR on the SANS SIFT Workstation | 5 (plus config and templates) | NONE | 29 | 2026-03-25 |
| 10 | [Liberty91LTD/cti-skills](#10-liberty91ltdcti-skills) | Cyber threat intelligence lifecycle | 78 | MIT | 27 | 2026-09-30 |
| 11 | [openai/skills](#11-openaiskills-security-skills-only) (security only) | AppSec practices and threat modeling | 3 security (of 44) | Per skill | 27,922 | 2026-06-24 |
| 12 | [BagelHole/DevOps-Security-Agent-Skills](#12-bagelholedevops-security-agent-skills) | DevSecOps, cloud, compliance | 163 (54 security or compliance) | MIT | 1,141 | 2026-05-22 |
| 13 | [ADScanPro/Claude-AD](#13-adscanproclaude-ad) | Active Directory red team | 8 | MIT | 210 | 2026-08-24 |
| 14 | [BrownFineSecurity/iothackbot](#14-brownfinesecurityiothackbot) | IoT and hardware pentesting | 13 | MIT | 858 | 2026-06-01 |
| 15 | [gemini-cli-extensions/security](#15-gemini-cli-extensionssecurity) | Diff and PR vulnerability review | 3 (plus commands) | Apache-2.0 | 794 | 2026-04-28 |

## Shortlist in depth

### 1. mukul975/Anthropic-Cybersecurity-Skills

- **URL:** <https://github.com/mukul975/Anthropic-Cybersecurity-Skills>
- **Maintainer:** `mukul975`, a personal account. Despite the name, this
  is a community project, not an Anthropic repository.
- **What it is:** The largest single cybersecurity skill library found.
  Each skill is one procedure with YAML frontmatter that maps it to
  frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI
  RMF, and MITRE F3), plus `references/`, `scripts/`, and `assets/`
  folders.
- **Focus:** Broad coverage of offense, defense, DFIR, cloud, and GRC.
- **License:** Apache-2.0
- **Skills:** 818 `SKILL.md` files; the README claims 817 across 34
  domains.
- **Agent targets:** Claude Code, GitHub Copilot, Codex CLI, Cursor,
  Gemini CLI, Windsurf, Cline, and Hermes, per the README.
- **Last activity:** 2026-08-31 · 33,913 stars · created 2026-02-25
- **Notes:** Some skills use Splunk, Elastic, or Microsoft queries as
  examples, but the procedures don't require a tenant. The repository
  ships a `SCOPE.md` that explicitly keeps offensive and dual-use content
  in scope. It has several repackages and mirrors; see
  [Repackages and mirrors](#repackages-and-mirrors).

**Catalog.** All skills sit flat under `skills/`, named
`verb-ing-the-task`. The README groups them by the `subdomain`
frontmatter field. The largest domains:

| Domain (README count) | Example skills |
| --- | --- |
| Cloud security (66) | `analyzing-cloud-storage-access-patterns` |
| SOC operations (63) | `analyzing-dns-logs-for-exfiltration` |
| Threat hunting (58) | Hypothesis-driven hunts, living-off-the-land detection, EVTX hunting |
| Threat intelligence (52) | `analyzing-apt-group-with-mitre-navigator`, `analyzing-campaign-attribution-evidence` |
| Web application (46) and API security (28) | OWASP Top 10, SQL injection, SSRF, GraphQL |
| Digital forensics (41) | `acquiring-disk-image-with-dd-and-dcfldd`, `analyzing-disk-image-with-autopsy` |
| Identity and access management (40) | `analyzing-active-directory-acl-abuse` |
| Malware analysis (39) | `analyzing-cobalt-strike-beacon-configuration`, `analyzing-golang-malware-with-ghidra` |
| Red teaming (35) | `abusing-shadow-credentials-for-privesc` |
| Smaller domains | Container, OT/ICS, incident response (`analyzing-linux-audit-logs-for-intrusion`), vulnerability management, DevSecOps, zero trust, AI security, mobile, compliance (`achieving-cmmc-level-2-compliance`), and more |

Example skills were checked against each file's `subdomain` field. Rows
without skill names use the README's capability summary.

### 2. trailofbits/skills

- **URL:** <https://github.com/trailofbits/skills>
- **Maintainer:** Trail of Bits
- **What it is:** A Claude Code plugin marketplace from a security audit
  firm, with skills for audit preparation, static analysis, fuzzing,
  cryptography review, and smart-contract security. The tools it drives
  are free and open source (Semgrep, CodeQL, AFL++, libFuzzer), so no
  tenant is needed.
- **Focus:** Application security and code auditing.
- **License:** CC-BY-SA-4.0
- **Skills:** 85 `SKILL.md` files across 44 plugin folders. Some are
  general development or team skills, not security (for example
  `modern-python`, `devcontainer-setup`, `interpreting-culture-index`,
  and `let-fate-decide`).
- **Agent targets:** Claude Code; Codex loads Claude plugin
  marketplaces directly, per the README.
- **Last activity:** 2026-09-28 · 7,414 stars
- **Notes:** Trail of Bits also runs
  [trailofbits/skills-curated](https://github.com/trailofbits/skills-curated),
  the only vetted, security-focused marketplace the survey found.

**Catalog.** Skills are grouped as `plugins/<plugin>/skills/<skill>`.

| Group | Example skills |
| --- | --- |
| Smart contracts (`building-secure-contracts`, 11) | `solana-vulnerability-scanner`, `token-integration-analyzer`, `audit-prep-assistant` |
| Fuzzing and testing (`testing-handbook-skills`, 15) | `aflpp`, `libfuzzer`, `cargo-fuzz`, `harness-writing`, `wycheproof` |
| Static analysis | `semgrep`, `codeql`, `sarif-parsing`, `semgrep-rule-creator` |
| Code audit | `differential-review`, `variant-analysis`, `sharp-edges`, `entry-point-analyzer`, `c-review`, `rust-review` |
| Code graphs (`trailmark`, 14) | `crypto-protocol-diagram`, `mermaid-to-proverif`, `trailmark-finding-triage` |
| Verification | `constant-time-analysis`, `zeroize-audit`, `property-based-testing`, `mutation-testing` |
| Supply chain and CI | `supply-chain-risk-auditor`, `agentic-actions-auditor` |
| Other security | `yara-authoring`, `firebase-apk-scanner`, `dwarf-expert`, `burpsuite-project-parser` |

### 3. cloudflare/security-audit-skill

- **URL:** <https://github.com/cloudflare/security-audit-skill>
- **Maintainer:** Cloudflare
- **What it is:** One large skill that turns a coding agent into a code
  auditor. It runs isolated sub-agents through reconnaissance,
  coverage-led hunting, independent verification of every candidate, and
  schema-validated reporting. The README says it seeded Cloudflare's own
  vulnerability discovery harness.
- **Focus:** Source-code security audit.
- **License:** MIT
- **Skills:** 1 `SKILL.md` with 14 phase and attack-class guides.
- **Agent targets:** Any coding agent that loads skills, per the README.
- **Last activity:** 2026-09-14 · 25,983 stars
- **Notes:** Ships two Node.js validators (`validate-findings.cjs` and
  `validate-coverage-ledger.cjs`) that the skill runs. Treat them like any
  other third-party script.

**Catalog.** Everything is in `skills/security-audit/`.

| Group | Files |
| --- | --- |
| Workflow | `SKILL.md`, `RECONNAISSANCE.md`, `HUNTING.md`, `VALIDATION-AND-REPORTING.md` |
| Attack classes | `ATTACK-CLASSES.md`, `WEB-PROTOCOL-AND-AUTH.md`, `CLIENT-SIDE.md`, `MEMORY-SAFETY-AND-BINARY.md`, `AI-AND-LLM.md` |
| Environment classes | `CLOUD-AND-DEPLOYMENT.md`, `DATA-ISOLATION-AND-LIFECYCLE.md`, `DESKTOP-MOBILE-AND-LOCAL-IPC.md`, `PROTOCOLS-RPC-AND-MESSAGING.md`, `RESOURCE-EXHAUSTION-AND-AVAILABILITY.md`, `SUPPLY-CHAIN-AND-RELEASE.md` |
| Output contract | `report-schema.json`, two validators and their tests |

### 4. Masriyan/Claude-Code-CyberSecurity-Skill

- **URL:** <https://github.com/Masriyan/Claude-Code-CyberSecurity-Skill>
- **Maintainer:** `Masriyan`
- **What it is:** 22 long skills, one per security discipline, each with
  reference material. A compact way to give an agent broad security
  coverage without hundreds of skill files.
- **Focus:** Broad, from recon to GRC.
- **License:** MIT
- **Skills:** 22
- **Agent targets:** Claude Code
- **Last activity:** 2026-09-07 · 467 stars
- **Notes:** The scan found that SIEM queries appear as multi-vendor
  examples, not as requirements; that wasn't rechecked (**unverified**).

**Catalog.** Numbered folders under `skills/`.

| Group | Skills |
| --- | --- |
| Offense | `01-recon-osint`, `02-vulnerability-scanner`, `03-exploit-development`, `14-red-team-ops` |
| Analysis | `04-reverse-engineering`, `05-malware-analysis`, `13-crypto-analysis` |
| Defense and SOC | `06-threat-hunting`, `07-incident-response`, `11-csoc-automation`, `12-log-analysis`, `15-blue-team-defense`, `22-purple-team` |
| Domains | `08-network-security`, `09-web-security`, `10-cloud-security`, `16-ai-llm-security`, `17-mobile-security`, `18-ot-ics-security` |
| Governance and intel | `19-grc-compliance`, `20-supply-chain-security`, `21-threat-intelligence` |

### 5. briiirussell/cybersecurity-skills

- **URL:** <https://github.com/briiirussell/cybersecurity-skills>
- **Maintainer:** `briiirussell`
- **What it is:** Audit-oriented skills written for both security
  engineers and teams without one. Skills are authored as Claude Code
  `SKILL.md` files and built into Cursor `.mdc` adapters; offensive
  skills include authorization gates.
- **Focus:** Code, cloud, and compliance audits, plus red, blue, and
  purple team work.
- **License:** MIT
- **Skills:** 29, plus 29 generated Cursor `.mdc` adapters.
- **Agent targets:** Claude Code, Cursor, and Codex.
- **Last activity:** 2026-05-27 · 412 stars

**Catalog.** Flat folders under `skills/`.

| Group | Skills |
| --- | --- |
| Code and app audits | `owasp-audit`, `api-audit`, `dependency-audit`, `secrets-audit`, `crypto-audit`, `mobile-audit` |
| Infrastructure audits | `cloud-audit`, `iam-audit`, `container-audit` |
| Compliance and risk | `csf-mapping`, `hipaa-audit`, `pci-audit`, `privacy-engineering`, `ai-risk-management` |
| Offense | `recon`, `osint-recon`, `web-pentest`, `red-team-engagement`, `vuln-research`, `prompt-injection` |
| Defense | `threat-hunting`, `siem-detection`, `soc-operations`, `incident-triage`, `disk-forensics` |
| Cross-cutting | `threat-modeling`, `finding-triage`, `breach-patterns`, `security-comms` |

### 6. ljagiello/ctf-skills

- **URL:** <https://github.com/ljagiello/ctf-skills>
- **Maintainer:** `ljagiello`
- **What it is:** Dense skills for solving capture-the-flag challenges,
  with a solve orchestrator and a write-up skill.
- **Focus:** CTF: web, pwn, crypto, reverse engineering, forensics, and
  OSINT.
- **License:** MIT
- **Skills:** 11
- **Agent targets:** Claude Code, Codex, Gemini CLI, and opencode, per the
  GitHub topics.
- **Last activity:** 2026-09-13 · 3,402 stars
- **Notes:** Ships a tool installer (`scripts/install_ctf_tools.sh`).
  The README's install path is `npx skills add`; this repository's
  [intake rules](../INTAKE.md) say to clone instead.

**Catalog.** One top-level folder per skill: `ctf-web`, `ctf-pwn`,
`ctf-crypto`, `ctf-reverse`, `ctf-forensics`, `ctf-malware`, `ctf-osint`,
`ctf-ai-ml`, `ctf-misc`, `ctf-writeup`, and the entry point
`solve-challenge`.

### 7. SnailSploit/Claude-Red

- **URL:** <https://github.com/SnailSploit/Claude-Red>
- **Maintainer:** `SnailSploit`
- **What it is:** A deep offensive-security library that ranges from web
  bugs to shellcode, EDR evasion, and exploit development.
- **Focus:** Offense and exploit development.
- **License:** MIT
- **Skills:** 79 (the README badge says 78) in 23 categories.
- **Agent targets:** Claude (Claude Code and Claude.ai).
- **Last activity:** 2026-09-19 · 7,337 stars
- **Notes:** Strongly dual-use: it includes evasion, keylogger, and
  anti-forensics content. Ships `install.sh` and `convert_skills.py`. The
  scan reported one skill file at about 567 KB (**unverified**).

**Catalog.** `Skills/<category>/offensive-<topic>/`.

| Group | Example skills |
| --- | --- |
| Web (16) | `offensive-sqli`, `offensive-ssrf`, `offensive-request-smuggling`, `offensive-deserialization` |
| Wireless (14) | `offensive-wpa3-sae`, `offensive-evil-twin`, `offensive-bluetooth-ble`, `offensive-zigbee-thread-matter` |
| Infrastructure and red team (7) | `offensive-initial-access`, `offensive-edr-evasion`, `offensive-shellcode` |
| Exploit dev and fuzzing (10) | `offensive-exploit-development`, `offensive-crash-analysis`, `offensive-fuzzing` |
| Post-exploitation and privesc | `offensive-lateral-movement`, `offensive-persistence`, `offensive-linux-privesc` |
| Identity and AD | `offensive-active-directory`, `offensive-netexec`, `offensive-jwt`, `offensive-oauth` |
| Cloud, containers, CI/CD | `offensive-cloud`, `offensive-k8s-attacks`, `offensive-cicd-secrets` |
| Other | Supply chain, social engineering, crypto, IoT, mobile, AI, and `offensive-reporting` |

### 8. meltedinhex/analyst-ai-pack

- **URL:** <https://github.com/meltedinhex/analyst-ai-pack>
- **Maintainer:** `meltedinhex`
- **What it is:** Compact, runnable skills for malware analysts, reverse
  engineers, and threat hunters. Each skill maps to MITRE ATT&CK,
  D3FEND, and CAR, and the repository has CI and a written taxonomy.
- **Focus:** Malware analysis, reverse engineering, and threat hunting.
- **License:** Apache-2.0
- **Skills:** 118, plus one `skill-template`.
- **Agent targets:** Claude Code, Codex, Cursor, Gemini CLI, and Copilot,
  per the scan; not rechecked (**unverified**).
- **Last activity:** 2026-07-07 · 21 stars
- **Notes:** Low star count, but the content is structured and recent.

**Catalog.** Flat under `skills/`; `taxonomy.md` assigns each skill to
one subdomain.

| Subdomain | Example skills |
| --- | --- |
| Lab foundations | `setting-up-an-isolated-malware-analysis-lab`, `handling-malware-samples-safely`, `triaging-an-unknown-sample`, `writing-a-malware-analysis-report` |
| Malware analysis | `performing-static-pe-analysis`, `analyzing-malicious-office-macros`, `analyzing-malware-in-memory-with-volatility3`, `extracting-cobalt-strike-beacon-config` |
| Reverse engineering | `reverse-engineering-binaries-with-ghidra`, `unpacking-upx-and-common-packers`, `resolving-dynamic-api-hashing`, `emulating-shellcode-with-unicorn` |
| Threat hunting and detection | `hunting-c2-beaconing-with-frequency-analysis`, `hunting-kerberoasting-and-ticket-attacks`, `writing-sigma-detection-rules`, `writing-yara-rules-from-reversed-code` |

### 9. teamdfir/protocol-sift

- **URL:** <https://github.com/teamdfir/protocol-sift>
- **Maintainer:** `teamdfir` (SANS DFIR team account, per the scan)
- **What it is:** A complete Claude Code setup for forensic work on the
  free SANS SIFT Workstation: tool skills, global behavior rules, a
  per-case project template, and a PDF report generator.
- **Focus:** DFIR: memory, disk, timeline, Windows artifacts, and YARA.
- **License:** NONE (no license file), so reuse rights are unclear.
- **Skills:** 5
- **Agent targets:** Claude Code
- **Last activity:** 2026-03-25 · 29 stars
- **Notes:** The installer overwrites `~/.claude/CLAUDE.md` and
  `~/.claude/settings.json` (tool permissions and a Stop hook), and the
  global prompt prefers autonomous operation without questions. Install
  it only on a dedicated SIFT VM. The README has chain-of-custody notes.
  The scan's note that the project is experimental and not for
  evidentiary use wasn't found in the README (**unverified**).

**Catalog.**

| Group | Contents |
| --- | --- |
| Skills | `memory-analysis` (Volatility 3), `plaso-timeline`, `sleuthkit`, `windows-artifacts` (EZ Tools, EVTX, registry), `yara-hunting` |
| Global config | `global/CLAUDE.md`, `global/settings.json`, `global/settings.local.json` |
| Case setup | `case-templates/CLAUDE.md`, `analysis-scripts/generate_pdf_report.py` |

### 10. Liberty91LTD/cti-skills

- **URL:** <https://github.com/Liberty91LTD/cti-skills>
- **Maintainer:** Liberty91 Ltd, a threat intelligence firm.
- **What it is:** Skills for the full intelligence cycle: requirements,
  collection, IOC investigation, analytic tradecraft, detection writing,
  and reporting with confidence language.
- **Focus:** Cyber threat intelligence.
- **License:** MIT
- **Skills:** 78
- **Agent targets:** Claude Code, Cursor, Codex, and Windsurf, per the
  README.
- **Last activity:** 2026-09-30 · 27 stars
- **Notes:** 23 skills (`lookup-*` and `*-api`) query third-party services
  (VirusTotal, Shodan, CrowdStrike, Microsoft Sentinel, and the
  maintainer's own Liberty91 platform). API keys are optional; the README
  says the pack works without them, minus live lookups. The tradecraft
  skills are the vendor-neutral core.

**Catalog.** Flat under `skills/`.

| Group | Example skills |
| --- | --- |
| Analytic tradecraft | `ach`, `key-assumptions-check`, `devils-advocacy`, `structured-analytic-techniques`, `confidence-levels`, `likelihood-language` |
| Investigation | `ip-investigation`, `domain-investigation`, `hash-investigation`, `indicator-pivoting`, `ioc-enrichment-workflow` |
| Threat landscape | `russia-cyber-espionage`, `ransomware-ecosystem`, `infostealers`, `initial-access-brokers` |
| Detection and sharing | `sigma-writing`, `yara-writing`, `kql-writing`, `stix-bundle`, `tlp-guide`, `ioc-export` |
| Program management | `pir-management`, `maturity-assessment`, `stakeholder-management`, `cti-orchestrator` |
| Service lookups | `lookup-virustotal`, `lookup-shodan`, `lookup-misp`, `lookup-opencti`, `greynoise-api` |

### 11. openai/skills (security skills only)

- **URL:** <https://github.com/openai/skills>
- **Maintainer:** OpenAI
- **What it is:** OpenAI's Codex skill catalog. Three curated skills are
  security skills: short, official, and solid.
- **Focus:** Secure coding practices, threat modeling, and security
  ownership mapping.
- **License:** No root license; each skill ships its own `LICENSE.txt`.
  The scan read these as Apache-2.0; not reopened (**unverified**).
- **Skills:** 3 security skills of 44 total.
- **Agent targets:** Codex
- **Last activity:** 2026-06-24 · 27,922 stars
- **Notes:** The README now says the repository is **deprecated** in
  favor of [openai/plugins](https://github.com/openai/plugins). The
  security skills haven't been checked there. Trail of Bits'
  `skills-curated` also mirrors them.

**Catalog.** `skills/.curated/`:

- `security-best-practices`: language- and framework-specific secure
  coding guidance, with `references/`.
- `security-threat-model`: a repository-grounded threat model.
- `security-ownership-map`: maps security-sensitive code to owners, with
  `scripts/`.

### 12. BagelHole/DevOps-Security-Agent-Skills

- **URL:** <https://github.com/BagelHole/DevOps-Security-Agent-Skills>
- **Maintainer:** `BagelHole`
- **What it is:** A broad operations knowledge base with copy-paste
  configs. Security and compliance are about a third of it; the rest is
  DevOps and infrastructure.
- **Focus:** DevSecOps, hardening, cloud, and compliance.
- **License:** MIT
- **Skills:** 163 (35 security, 19 compliance, 39 DevOps, 70
  infrastructure).
- **Agent targets:** Claude Code, Cursor, Codex, and other file-reading
  agents, per the README.
- **Last activity:** 2026-05-22 · 1,141 stars

**Catalog.** `<area>/<group>/<skill>/`. Security and compliance groups:

| Group | Example skills |
| --- | --- |
| `security/ai` | `prompt-injection-defense`, `mcp-server-security`, `ai-red-teaming` |
| `security/scanning` | `sast-scanning`, `dast-scanning`, `container-scanning`, `sbom-supply-chain` |
| `security/hardening` | `cis-benchmarks`, `kubernetes-hardening`, `linux-hardening`, `windows-hardening` |
| `security/secrets` and `security/network` | `hashicorp-vault`, `sops-encryption`, `zero-trust`, `waf-setup` |
| `security/operations` | `incident-response`, `penetration-testing`, `threat-modeling` |
| `compliance/*` | `soc2-compliance`, `iso27001-compliance`, `pci-dss-compliance`, `access-review`, `disaster-recovery` |

### 13. ADScanPro/Claude-AD

- **URL:** <https://github.com/ADScanPro/Claude-AD>
- **Maintainer:** `ADScanPro`
- **What it is:** Active Directory assessment methodology as skills,
  agents, and slash commands, with OPSEC and telemetry notes for each
  technique. It drives open tools: NetExec, Impacket, Certipy, bloodyAD,
  and BloodHound CE.
- **Focus:** Internal AD red team.
- **License:** MIT
- **Skills:** 8, plus agents and commands.
- **Agent targets:** Claude Code (plugin).
- **Last activity:** 2026-08-24 · 210 stars
- **Notes:** The whole history is a single day (created and last commit
  2026-08-24). The README explains where it ends and the maintainer's
  ADscan product begins; the skills don't require that product.

**Catalog.** `skills/`: `ad-methodology`, `ad-environment-constraints`,
`kerberos-attacks`, `adcs-attacks`, `acl-abuse`, `coercion-ntlm-relay`,
`ad-opsec-telemetry`, and `compliance-mapping`.

### 14. BrownFineSecurity/iothackbot

- **URL:** <https://github.com/BrownFineSecurity/iothackbot>
- **Maintainer:** Brown Fine Security
- **What it is:** IoT and embedded pentest tooling paired with skills
  that drive it, for IP cameras, firmware, Android companion apps, and
  hardware debug ports.
- **Focus:** IoT and hardware pentesting.
- **License:** MIT
- **Skills:** 13, plus custom tools in `tools/` and `bin/`.
- **Agent targets:** Claude Code
- **Last activity:** 2026-06-01 · 858 stars

**Catalog.**

| Group | Skills |
| --- | --- |
| Network discovery | `nmap`, `wsdiscovery`, `iotnet`, `netflows` |
| Device testing | `onvifscan`, `telnetshell` |
| Firmware and files | `chipsec`, `ffind` |
| Android | `apktool`, `jadx` |
| Hardware access | `jtagprobe`, `picocom`, `logicmso` |

### 15. gemini-cli-extensions/security

- **URL:** <https://github.com/gemini-cli-extensions/security>
- **Maintainer:** Google
- **What it is:** The official Gemini CLI security extension. It reviews
  the current branch's changes for vulnerabilities and scans dependencies
  with the open-source OSV-Scanner.
- **Focus:** Diff and pull request security review.
- **License:** Apache-2.0
- **Skills:** 3, plus slash commands and a local MCP server.
- **Agent targets:** Gemini CLI only, but it needs no Google Cloud
  tenant.
- **Last activity:** 2026-04-28 · 794 stars

**Catalog.**

| Group | Contents |
| --- | --- |
| Commands | `/security:analyze` (branch diff review, optional JSON), `/security:scan-deps` (OSV-Scanner) |
| Skills | `dependency-manager`, `poc`, `security-patcher` |
| Other | `mcp-server/`, a GitHub Actions workflow for pull request review |

## Honorable mentions

The remaining vendor-neutral candidates from the scan. Each was rechecked
on GitHub on 2026-10-07; quality notes come from the scan.

| Repository | Focus | Skills | License | Stars | Last commit | Note |
| --- | --- | --- | --- | --- | --- | --- |
| [tsale/awesome-dfir-skills](https://github.com/tsale/awesome-dfir-skills) | DFIR (osquery, hunting) | 5 | Apache-2.0 | 324 | 2026-05-14 | Small curated set with a validator |
| [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | PR security review | 0 | MIT | 6,318 | 2026-02-11 | A GitHub Action, not a skill pack |
| [transilienceai/communitytools](https://github.com/transilienceai/communitytools) | Pentest, bug bounty | 50 | MIT | 561 | 2026-07-29 | Many short skills |
| [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) | GRC (ISO 27001, SOC 2, NIST) | 36 | MIT | 941 | 2026-10-04 | Benchmark claims are self-reported |
| [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) | Secure coding | 1 | Apache-2.0 | 1,311 | 2026-02-17 | Single solid skill |
| [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) | OWASP Top 10:2025, ASVS 5.0 | 1 | MIT | 377 | 2026-09-25 | Single skill |
| [Nebulock-Inc/agentic-threat-hunting-framework](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework) | Threat hunting framework | 1 | MIT | 385 | 2026-10-02 | Needs your own log source |
| [secondsky/claude-skills](https://github.com/secondsky/claude-skills) | OSS-only AppSec (`cybersecurity` plugin) | 1 security of 187 | MIT | 227 | 2026-09-26 | Maps paid tools to OSS alternatives |
| [AgentSecOps/SecOpsAgentKit](https://github.com/AgentSecOps/SecOpsAgentKit) | DevSecOps scanners | 32 | Other (scan: dual) | 220 | 2026-04-15 | Wraps OSS scanners |
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | RE and pentest router (CN/EN) | 89 | MIT | 40,051 | 2026-09-22 | See [suspicious stars](#suspicious-popularity) |
| [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) | Reverse engineering (CN) | 7 | NONE | 2,238 | 2026-05-06 | Real, small |
| [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) | Android RE | 1 | Apache-2.0 | 7,998 | 2026-09-08 | Single skill |
| [incogbyte/android-reverse-engineering-claude-skill](https://github.com/incogbyte/android-reverse-engineering-claude-skill) | Android RE | 1 | Unlicense | 122 | 2026-06-20 | Single skill |
| [wgpsec/AboutSecurity](https://github.com/wgpsec/AboutSecurity) | Pentest knowledge base (CN) | 249 | NONE | 1,775 | 2026-10-03 | Long-running knowledge base converted to skills |
| [x-glacier/kali-pentest](https://github.com/x-glacier/kali-pentest) | Kali pentest with approval gates | 2 | Apache-2.0 | 135 | 2026-06-25 | Needs Kali |
| [0rangec3t/Black-cat](https://github.com/0rangec3t/Black-cat) | Hypothesis-driven red team (CN) | 1 | NONE | 318 | 2026-07-31 | Single skill |
| [UseOSINT/Skills](https://github.com/UseOSINT/Skills) | OSINT, passive-first | 29 | MIT | 48 | 2026-08-03 | Some skills use Shodan and similar services |
| [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth) | Photo geolocation | 1 | MIT | 1,182 | 2026-10-07 | Single skill, active |
| [EvilFreelancer/secs](https://github.com/EvilFreelancer/secs) | Broad, with a Metasploitable lab | 49 | Apache-2.0 | 11 | 2026-08-09 | Scan counted per-agent copies; 49 today |
| [jaskaranhundal/usap-skills](https://github.com/jaskaranhundal/usap-skills) | SOC, IR, hunting, red and blue | 196 (87 unique) | Apache-2.0 | 4 | 2026-09-05 | Duplicated per agent; low traction |
| [NoorQureshi/SploitAgent](https://github.com/NoorQureshi/SploitAgent) | Pentest, bug bounty, CTF | 206 | MIT | 20 | 2026-10-04 | Thin skills, new |
| [mukul975/Threatswarm](https://github.com/mukul975/Threatswarm) | Pentest kill-chain agents | 10 (5 unique) | MIT | 86 | 2026-04-29 | Agent layer over the mukul975 library |
| [EresusSecurity/appsec-skills](https://github.com/EresusSecurity/appsec-skills) | SAST, threat modeling | 11 | Apache-2.0 | 7 | 2026-04-07 | Low traction |
| [tanviet12/vbsec](https://github.com/tanviet12/vbsec) | Vulnerability scan for AI-written code | 3 (1 unique) | MIT | 287 | 2026-09-28 | One skill copied per agent |
| [kulchankas/paranoid](https://github.com/kulchankas/paranoid) | Self-pentest of your own app | 1 | MIT | 48 | 2026-09-27 | New |
| [Orizon-eu/claude-code-pentest](https://github.com/Orizon-eu/claude-code-pentest) | Web pentest lifecycle | 6 | MIT | 26 | 2026-03-11 | Ships helper scripts |
| [jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill) | ffuf fuzzing | 1 | NONE | 213 | 2025-10-16 | Early single skill |
| [matank001/cursor-security-rules](https://github.com/matank001/cursor-security-rules) | Secure coding rules | 0 (16 `.mdc`) | MIT | 380 | 2025-08-27 | Cursor rules; stale |
| [wiz-sec-public/secure-rules-files](https://github.com/wiz-sec-public/secure-rules-files) | Secure code generation rules | 0 (9 `.mdc`) | Other (scan: CC-BY-NC-ND-4.0) | 242 | 2025-12-23 | No Wiz product needed; restrictive license |
| [pillar-labs/sail-skill](https://github.com/pillar-labs/sail-skill) | AI and agent risk catalog | 1 | Other (scan: CC-BY-NC-SA-4.0) | 113 | 2026-07-07 | Non-commercial license |
| [olanokhin/agent-security-skill](https://github.com/olanokhin/agent-security-skill) | OWASP LLM and agentic review | 1 | MIT | 6 | 2026-06-13 | Small |
| [Fuzzdkk/dfir-skills](https://github.com/Fuzzdkk/dfir-skills) | DFIR on Kali | 12 | NONE | 3 | 2026-04-10 | No license |
| [samaritan0/dfir-agentic-suite](https://github.com/samaritan0/dfir-agentic-suite) | DFIR skills and MCP | 5 | NONE | 17 | 2026-03-24 | Small |
| [sector-b79/Malware-And-Reverse-Engineering-Skill-for-AI-Agents](https://github.com/sector-b79/Malware-And-Reverse-Engineering-Skill-for-AI-Agents) | Malware and RE | 3 (1 unique) | NONE | 18 | 2026-05-09 | Small |
| [PolGs/claude-blue-team-skills](https://github.com/PolGs/claude-blue-team-skills) | SOC and malware analysis | 0 | NONE | 8 | 2026-04-09 | Two prompt files |
| [masonzeng702550/blueteam-ctf](https://github.com/masonzeng702550/blueteam-ctf) | Blue-team CTF (zh/en) | 7 | Other (scan: MIT) | 1 | 2026-05-29 | Tiny |
| [Garyson26/Trident-SecOps-Skills](https://github.com/Garyson26/Trident-SecOps-Skills) | Broad | 24 | MIT | 5 | 2026-09-30 | Thin skills |
| [Eyadkelleh/awesome-skills-security](https://github.com/Eyadkelleh/awesome-skills-security) | Wordlists and payloads | 7 | NONE | 388 | 2026-06-08 | Mostly SecLists wordlists |
| [Hi-FullHouse/CyberSecurity-Skills](https://github.com/Hi-FullHouse/CyberSecurity-Skills) | Pentest knowledge base (CN) | 0 | MIT | 651 | 2026-05-15 | Self-described as AI-maintained |
| [frendysanusi/claude-pentest-skills](https://github.com/frendysanusi/claude-pentest-skills) | Web pentest | 1 | NONE | 46 | 2026-09-12 | Small |
| [SHADOWPR0/security-bluebook-builder](https://github.com/SHADOWPR0/security-bluebook-builder) | Security documentation | 1 | NONE | 8 | 2025-12-24 | Small |
| [trailofbits/skills-curated](https://github.com/trailofbits/skills-curated) | Vetted marketplace | 31 | CC-BY-SA-4.0 | 512 | 2026-07-14 | Mirrors vetted third-party security skills |

## Excluded

These repositories came up in the scan and are deliberately left out.
Metadata was rechecked on 2026-10-07; the reasons come from the scan and
weren't re-derived unless noted.

### Vendor-bound

| Repository | Reason |
| --- | --- |
| [eth0izzle/security-skills](https://github.com/eth0izzle/security-skills) | Centered on CrowdStrike Falcon |
| [sherlon1/soc-hunter](https://github.com/sherlon1/soc-hunter) | Needs SIEM, EDR, CSPM, and CASB MCP servers to do anything |
| `pmoses-s1/claude-skills` | **Not found** on GitHub on 2026-10-07. Earlier search results described it as a SentinelOne SOC pack |
| [ghostsecurity/skills](https://github.com/ghostsecurity/skills) | Downloads and runs Ghost Security's own binaries |
| [google/skills](https://github.com/google/skills) | Its security skills are bound to GKE and Google Cloud |
| [crowdsecurity/crowdsec-skill](https://github.com/crowdsecurity/crowdsec-skill) | Operates the CrowdSec product |
| [Neo23x0/virustotal-skill](https://github.com/Neo23x0/virustotal-skill) | VirusTotal API |
| [dandye/ai-runbooks](https://github.com/dandye/ai-runbooks), [dandye/secops-gemini-extension](https://github.com/dandye/secops-gemini-extension) | Google SecOps |
| [membranedev/application-skills](https://github.com/membranedev/application-skills) (security entries) | Exabeam, Cortex XSOAR, and LimaCharlie integrations |

### Repackages and mirrors

These derive from mukul975/Anthropic-Cybersecurity-Skills. Use the
original instead.

| Repository | Skills | What it is |
| --- | --- | --- |
| [Mikaru0Mystic/sectinel](https://github.com/Mikaru0Mystic/sectinel) | 785 | Repackage; the scan matched 754 folder names to mukul975 |
| [26zl/cybersec-toolkit](https://github.com/26zl/cybersec-toolkit) | 872 | Repackage plus a tool installer and sandboxed MCP |
| [costrict-plugins-repo/mukul975-…](https://github.com/costrict-plugins-repo/mukul975-anthropic-cybersecurity-skills-cybersecurity-skills) | 818 | Auto-generated mirror |
| [killvxk/cybersecurity-skills-zh](https://github.com/killvxk/cybersecurity-skills-zh) | 735 | Chinese translation |
| [majiayu000/claude-skill-registry-data](https://github.com/majiayu000/claude-skill-registry-data) | 23,000+ | Scraped registry archive; it dominates code-search hits |

### Suspicious popularity

[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)
has 40,051 stars for a repository created on 2026-05-13, while its skills
are short (median about 3 KB, per the scan). It stays in the honorable
mentions on content, but don't use its star count as a quality signal.
Star counts in general are a weak signal for skill packs.

### Jailbreak tooling

[Sekolah76/syadagentic](https://github.com/Sekolah76/syadagentic)
describes itself as a "zero-refusal" agent framework with jailbreak
templates. It is excluded as abuse tooling.

## Supply-chain risk and skill scanners

A skill pack is executable instructions plus, often, executable scripts.
An agent that loads one follows its text and may run its helpers with
the agent's permissions. That makes every community pack a supply-chain
input: a malicious or careless skill can inject instructions, exfiltrate
data, or install software. The scan cites Snyk's ToxicSkills research,
which found prompt injection in 36% of the skills it tested
(**unverified** at the primary source).

**Vet any community pack before an agent or bot loads it.** In this
repository, third-party skill content goes through
[security intake](../INTAKE.md): clone instead of marketplace-installing,
quarantine scripts, scan, pin a commit SHA, and rewrite. Registries such
as skills.sh rank by installs, not by review.

Scanners and references the survey found:

| Tool | What it is | License | Stars |
| --- | --- | --- | --- |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Scanner for agent skills: malicious patterns, prompt injection, data exfiltration, supply-chain risk | Apache-2.0 | 19,641 |
| [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) | Security scanner for agent skills | Other | 2,581 |
| [alexgreensh/repo-forensics](https://github.com/alexgreensh/repo-forensics) | Offline scanner for agent repositories, skills, plugins, and MCP servers | Other | 188 |
| [OWASP Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10) | OWASP project page for the top risks in agent skills | Other | 286 |

Check the GitHub organization of any scanner before you trust its binary
or action; a matching name is not proof.

## Related

- [Third-party skill intake](../INTAKE.md)
- [Security hardening skill](../../skills/security-hardening/SKILL.md)
