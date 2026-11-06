# X chatter on red-team and blue-team agent skill packs (2026-10-18)

- Source: posts read through Grok Bot's built-in public X reads (the
  free `x` namespace: `search_posts_all`, `get_posts_by_ids`), no X
  connection or credits used. Companion to
  [security-skill-packs-2026-10-18.md](security-skill-packs-2026-10-18.md),
  which carries the GitHub-API verified signals this note leaves to X.
- Distilled: `2026-10-18`
- Live docs win: each pack's GitHub page for stars, forks, license, and
  commit dates; each post's own page for current engagement. This file
  is a dated snapshot of X chatter, not a live ranking.

## What it is

A ranking of public red-team and blue-team agent skill packs by their
signal on X: how many distinct posts named each pack in the searches
below, and the engagement on the top post. Packs are grouped Both
(red and blue in one pack), Red, and Blue. Every star and license
figure in this note is **as stated in posts**; X-reported numbers are
not GitHub-verified here (the verified figures live in the companion
file). Nothing is vendored.

## When to read

Read this when an operator asks what the X community is saying about
red-team or blue-team security skill packs, or wants the X side of the
companion catalog's signals. Open the live repository and the live
posts before relying on any number.

## How to read the signal

- **X signal** counts distinct posts that named the pack across the
  queries in [Search coverage](#search-coverage), with the top post's
  likes/reposts and handle. Counts are inflated for packs that recur
  in copy-paste "top repos" listicles.
- **As posted** marks stars and licenses taken from post text, not the
  GitHub API.
- Top post link format is `https://x.com/<handle>/status/<id>`.

## Both (red + blue in one pack)

| Pack | URL | What it is | License / stars (as posted) | X signal |
| --- | --- | --- | --- | --- |
| Anthropic-Cybersecurity-Skills (community, not Anthropic) | <https://github.com/mukul975/Anthropic-Cybersecurity-Skills> | 817 `SKILL.md` skills across 29 domains (threat hunting, IR, malware analysis, red teaming, cloud) mapped to MITRE ATT&CK/ATLAS/D3FEND, NIST CSF 2.0 and AI RMF, MITRE F3; by Mahipal Jangra; Claude Code, Codex CLI, Cursor, Copilot, Gemini CLI | Apache 2.0; ~10k (May) → ~22k (Jun) → ~27k (Jul) → ~30k (Aug) → ~33k (Sep) | 42 posts, May 19–Oct 16, most-mentioned pack. Top: @MAXdeg0 743♥/101↻ <https://x.com/MAXdeg0/status/2088509557576261965>; also @akaclandestine 165♥ <https://x.com/akaclandestine/status/2089035428795916648>, @_guillecasaus 179♥ <https://x.com/_guillecasaus/status/2079207638185701404> |
| Trail of Bits skills | <https://github.com/trailofbits/skills> | Claude Code plugin marketplace, 40+ audit skills (Semgrep/YARA rule writing, supply-chain and dependency audit, C/C++ and Rust review, smart-contract scanners, insecure-defaults, fp-check); Codex can load it | CC-BY-SA-4.0; ~6.2k (Jul) → ~6.9k (Aug) → ~7.6k (Oct) | 16 posts, Jun 1–Oct 17. Top: @sumika45379 237♥/32↻ <https://x.com/sumika45379/status/2091654222861516904>; @gideonxqt 22♥ <https://x.com/gideonxqt/status/2094111800195240177> |
| Cloudflare security-audit-skill | <https://github.com/cloudflare/security-audit-skill> | Coding-agent skill for multi-phase security audits (data isolation, auth, prompt injection, deps/CI, cloud config) with findings marked confirmed / needs-validation / ruled-out and a disprove-it verifier agent; JavaScript | ~"+20K in September" / "+22k" | 24 posts, Jul–Oct (many low-engagement repo-feed reposts). Top: @Voxyz_ai 112♥/9↻ <https://x.com/Voxyz_ai/status/2107486036314227068>; @GitTrend0x 12♥ <https://x.com/GitTrend0x/status/2100607243054194885> |
| Cyber-Frost Harness (Blackfrost AI) | <https://huggingface.co/collections/Blackfrost-AI/cyber-frost-38> | Reproducible security-agent runtime for red/blue/purple work: procedural skills, evidence ledger, isolated Docker targets; shipped with a ~180B security MoE model (Qwen3.8-Flash-Next-based) | Harness MIT; weights on Hugging Face | 26 posts, Sep–Oct (mostly about the model and quants). Top: @cybersec 1,566♥/220↻ <https://x.com/cybersec/status/2107203607624048956>; @Dinosn 219♥ <https://x.com/Dinosn/status/2107347342898667995> |
| anthropics/claude-code-security-review | <https://github.com/anthropics/claude-code-security-review> | Official Anthropic GitHub Action / `/security-review` running Claude on every PR diff (SQLi, XSS, hardcoded secrets, auth flaws) via semantic analysis | ~5,805 | 13 posts, Jun–Oct. Top: @_vmlops 24♥ <https://x.com/_vmlops/status/2063342446499758166> |
| DevOps & Security Agent Skills (bagelhole) | <https://github.com/bagelhole/DevOps-Security-Agent-Skills> | 160+ skills incl. vuln scanning, secrets management, container hardening, supply-chain, MCP security, prompt-injection, SOC2/GDPR/HIPAA/PCI, IR; Claude Code/Codex/Cursor | — | 2 posts. @DanKornas 47♥ <https://x.com/DanKornas/status/2093382869477408885>; @AI_Caffeine 35♥ <https://x.com/AI_Caffeine/status/2092205093718561135> |

## Red team

| Pack | URL | What it is | License / stars (as posted) | X signal |
| --- | --- | --- | --- | --- |
| Strix | <https://github.com/usestrix/strix> | Autonomous AI pentester for web apps/APIs; multi-step exploit chains in sandboxed Docker, validated PoCs, autofix-to-PR | Apache-2.0; ~30k (Jul) → ~58.8k (Aug) → ~65k (Sep) | 31 posts, Jul–Oct, persistent GitHub-trending chatter. Top in set: @DivyanshT91162 87♥ <https://x.com/DivyanshT91162/status/2106797730110828892> |
| Claude-BugHunter | <https://github.com/elementalsouls/Claude-BugHunter> | Drop-in Claude Code skill bundle for bug bounty / external red team; 51→71→83 skills, 15 slash commands, 681 disclosed HackerOne patterns across 24 vuln classes; red-team chains for M365/Okta/vCenter/SSL-VPN | MIT; ~3k | 39 posts, May 19–Oct 11 (2nd-most-mentioned overall); original thread cited at "1.6M views". Top: @MAXdeg0 243♥/47↻ <https://x.com/MAXdeg0/status/2089601037153808889>; @obscaries 129♥ <https://x.com/obscaries/status/2060217982421549193> |
| HexStrike AI | <https://github.com/0x4m4/hexstrike-ai> | MCP server orchestrating 150+ security tools so Claude/GPT/Copilot/Cursor run autonomous pentests (12+ agents); RED-TEAM fork adds BOAZ integration | ~13k | 37 posts, Jun–Oct. Top: @DivyanshT91162 87♥ <https://x.com/DivyanshT91162/status/2106797730110828892>; @UnTalNixon_exe 313♥ <https://x.com/UnTalNixon_exe/status/2107613763532726485> |
| Claude-Red | <https://github.com/SnailSploit/Claude-Red> | Curated library of 78 `SKILL.md` offensive-security skills in 23 categories, load-on-demand: web, AD, cloud, containers, CI/CD, wireless, EDR evasion, exploit-dev; by Kai Aizen | MIT | 22 posts, Aug–Oct, high engagement. Top: @0x0SojalSec 642♥/125↻, 164k impressions <https://x.com/0x0SojalSec/status/2099637006133518580>; @PythonHub 25♥ <https://x.com/PythonHub/status/2104303873984799215> |
| CyberStrike | <https://github.com/CyberStrikeus/CyberStrike> | Open-source AI-augmented offensive harness: "13+ autonomous agents, 7,600+ Ed25519-signed attack skills, 120+ OWASP test cases, 176+ MCP tools"; plug in Claude/GPT/any LLM; TypeScript | ~1.8–2.2k | 7 posts, high engagement. Top: @bountywriteups 1,036♥/165↻ <https://x.com/bountywriteups/status/2095142679764226142>; @NeobeePaul 592♥ <https://x.com/NeobeePaul/status/2083620181428072939> |
| Shannon | <https://github.com/KeygraphHQ/shannon> | Autonomous white-box AI pentester for web apps/APIs; reads source, maps attack paths, executes real exploits ("no exploit, no report"); TypeScript | AGPL-3.0; ~47–49k | 23 posts, Jul–Oct. Top: @aiedge_ 97♥ <https://x.com/aiedge_/status/2088807971975516270>; @KitPloit 40♥ <https://x.com/KitPloit/status/2097314446171373651> |
| PentestGPT | <https://github.com/GreyDGL/PentestGPT> | LLM-driven pentest agent (USENIX Security 2024 paper); phased recon/exploit/walkthrough; anchors large "AI security tools" listicles | ~16k | 12 posts, high engagement via listicles. Top: @MAXdeg0 1,283♥/270↻ <https://x.com/MAXdeg0/status/2097937353599832571>; @UnTalNixon_exe 313♥ <https://x.com/UnTalNixon_exe/status/2107613763532726485> |
| Cybermes | <https://github.com/Zyrexnn/Cybermes> | Autonomous offensive / bug-bounty / red-team agent framework on Hermes Agent; integrates Strix, HackTricks/HackSkills, Claude BugHunter + multi-model orchestration | — | 5 posts. Top: @Dinosn 624♥/98↻ <https://x.com/Dinosn/status/2091384639055073775> |
| REA – Reverse Engineer Anything | <https://github.com/morluto/rea> | MCP server + CLI (~139–170 tools) for reverse-engineering native binaries, .NET, Electron, APKs, firmware, live processes; bridges Ghidra/IDA/Hopper | MIT; posts claim 40 → 170k → 229k → 300k+ stars in ~2 weeks | 36 posts, concentrated Oct 7–18. Top: @mvanhorn 277♥/22↻ <https://x.com/mvanhorn/status/2110369555516407913>; @zodchiii 29♥ <https://x.com/zodchiii/status/2111805298952548704> |

Lower-signal red-team mentions: **reverse-skill** (zhaoxuya520, "36.4k stars," skill router for RE/malware/CTF) @bigaiguy 25♥ <https://x.com/bigaiguy/status/2102329454173602054>; **claude-bug-bounty** (shuvonsec, ~3.2k stars) @trybughunter 419♥ <https://x.com/trybughunter/status/2063917216668713432>; **Claude-OSINT**; **TORCH** (Claude Code + Obsidian bug-bounty harness); **hackthebox-skills** (blue0x1).

Reverse-engineering MCPs cited by name: **GhidraMCP** (<https://github.com/LaurieWired/GhidraMCP>, <https://github.com/bethington/ghidra-mcp>, ~3.4k→5k stars) 14 posts; **IDA Pro MCP** (<https://github.com/mrexodia/ida-pro-mcp>) 16 posts, @PythonHub 15♥ <https://x.com/PythonHub/status/2086139254787232156>; **Burp MCP** 27 posts, no single dominant repo (practitioner "Claude/Codex + Burp MCP + OpenCode" workflows), @zack0x01_ 39♥ <https://x.com/zack0x01_/status/2109906779979100468>.

## Blue team

Blue-team packs drew fewer and lower-engagement posts than red-team packs in these searches.

| Pack | URL | What it is | License / stars (as posted) | X signal |
| --- | --- | --- | --- | --- |
| Wazuh "Blue Team" MCP Server | <https://github.com/INFOKOM-KI/Wazuh-MCP-Server> | Defensive MCP server for Claude Desktop / MCP clients over Wazuh SIEM: "80+ SOC tools" (threat intel, alert enrichment, MITRE-based 3-Sum APT correlation, attack graphing, threat hunting, host forensics), read-only default, LangGraph playbooks | — | 7 posts. Top: @onnowpurbo 216♥/54↻ <https://x.com/onnowpurbo/status/2089504401312665703>; @DanKornas 24♥ <https://x.com/DanKornas/status/2105941862469058854> |
| AiSOC | <https://github.com/beenuar/AiSOC> | Self-hostable AI SOC, MCP for Claude/Cursor, MITRE ledger, "no API keys", alert fusion | ~2.4k | 5 posts. @0xal0ke <https://x.com/0xal0ke/status/2104220953387683909> |
| Vigil | — | Open-source agentic security operations center for investigate/respond/document | — | 5 posts. @DanKornas 5♥ <https://x.com/DanKornas/status/2099713314586517634> |
| Agentic SOC Platform / Tracecat | <https://github.com/TracecatHQ/tracecat> | Open-source security automation for agentic SOC teams (triage, enrichment, playbooks) | — | 5 posts. @sibyog13 21♥ <https://x.com/sibyog13/status/2092595522456391979>; @tracecathq 6♥ (Tracecat 1.0) |
| AnalystAIPack | — | 118 skills for malware analysis, reverse engineering, threat hunting | — | 1 post (self-announce). @sdkhere <https://x.com/sdkhere/status/2072365161944653829> |
| Gideon | — | 21 offensive & defensive security skills for Claude Code/Codex (Web/API/Cloud/AD/LLM, OWASP+MITRE mapped) | — | 1 post. @iamnoahfranklin <https://x.com/iamnoahfranklin/status/2109204103570006188> |

Blue-team adjacent mentions: **splunk-mcp-guard** (defensive proxy over Splunk MCP) @MehmetKadirCrk1 9♥ <https://x.com/MehmetKadirCrk1/status/2103502200052092969>; **Nebulock** (open-sourced detection-rule reasoning) 1 post; Sentinel/Defender XDR "25 investigation skills + KQL via Copilot Agent Mode" (concept posts, no standout repo); Microsoft Security Copilot (vendor, blue-team investigation, appears in listicles). Standalone `SKILL.md`-only blue-team packs (detection engineering, DFIR, Sigma/YARA authoring) appeared mostly folded into the large Both libraries above rather than as separate viral repos.

## Cross-cutting from X

- Several high-reach posts frame the category as `SKILL.md` re-enabling offensive capability the hosted models restrict, e.g. @diegopepe10 "Labs restrict offensive cyber in the hosted model; SKILL.md loads it back in the harness" <https://x.com/diegopepe10/status/2098478385651384798>.
- Scanner tooling for agent skills was also discussed in this period: NVIDIA **SkillSpector**, **SkillHawk**, Cisco **skill-scanner**, and an OWASP "Top 10 for agent skills".

## Search coverage

- ~30 `search_posts_all` queries plus 2 `get_posts_by_ids` full-text pulls, via the built-in free `x` namespace only; no X credits used.
- Angles: red/blue team skills; cybersecurity/security skills + Claude Code/Codex/`SKILL.md`; pentest and bug-bounty skills; threat hunting / DFIR / detection-engineering / SOC skills; and named targets (Anthropic-Cybersecurity-Skills, Claude-BugHunter, Claude-Red, CyberStrike, Cybermes, Trail of Bits, Cloudflare security-audit-skill, claude-code-security-review, HexStrike, PentestGPT, Strix, Shannon, REA, GhidraMCP, IDA MCP, Burp MCP, Wazuh/Splunk/Sentinel MCP, AiSOC, Vigil, Tracecat, Cyber-Frost).
- 675 unique posts reviewed. Date range 2026-05-19 to 2026-10-18, emphasis Jul–Oct, `-is:retweet`, relevancy sort.
- Caveats: all star/license figures are as stated in posts (not GitHub-verified in this note); "Anthropic-Cybersecurity-Skills" is a community project despite the name; listicle posts recycle identical repo sets, inflating raw counts for Strix, HexStrike, and PentestGPT.

## Unknown

- GitHub-verified stars, forks, licenses, and commit dates: see the companion [security-skill-packs-2026-10-18.md](security-skill-packs-2026-10-18.md); not re-derived here.
- Whether any pack's content is accurate, current, or safe. Nothing was scanned for this note.
- Download or install counts. X engagement is not adoption.
- Packs discussed only in replies, closed communities, or non-X channels.

## Do not

- Install a pack named here with a marketplace command, `npx`, or a plugin add. Intake is clone, scan, pin, rewrite: [docs/INTAKE.md](../../../docs/INTAKE.md).
- Copy a `SKILL.md` body, payload list, or script from these packs into this repo.
- Remint a pack as a skill id here, or read an X like count as a GitHub star count.
- Store tokens or credentials used to query these sources.
