# Agents write and check proofs: Lauren Tan's formal verification approach

Recorded 2026-11-20. This page summarizes what Lauren Tan has published
about having coding agents write formal specifications and proofs, and
having tools check them, so that people review verification results
instead of reading every line of agent-written code. Quotes are copied
from the sources listed at the end. Times are America/Chicago.

## Who and where

| Field | Record |
| --- | --- |
| Author | Lauren Tan, X handle [@poteto](https://x.com/poteto) |
| X bio (read 2026-11-20) | "grok @bot at @SpaceXSI. react compiler core team, prev cursor, meta, netflix" |
| Talk title slide | "Lauren Tan / Principal Engineer SPACEX" |
| Main posts | X posts from 2026-10-11 to 2026-11-08, listed in [Sources](#sources) |
| Main talk | "All Code Is Slop (Except Mine)", AI Engineer Code Summit, 2026-11-11 12:10 PM CST |
| Tools she ships | `/create-formal-verification-skill` and `/statechart` in [pstack](https://github.com/cursor/plugins/tree/main/pstack) |

The `@poteto` account is the one named on the talk slides ("@poteto",
"poteto (aka lauren tan)").

## The core idea in her words

The entry point is that the agent verifies its own work and returns an
artifact a person can check faster than the diff (2026-10-11):

> "the point is to give yourself confidence in the agents' work by them
> producing some kind of artifact that proves that 1) that the work is
> correct, 2) that it matches what you intended, and 3) is easier to
> review than reading the whole PR."

Formal verification, in her description (2026-10-18):

> "if you're new to formal verification, think of it as mathematically
> proving properties and invariants (something that must always be
> true) or "laws" of your system."

> "historically formal verification never reached mainstream status
> because of the difficulty in modeling and writing proofs. it's quite
> difficult to model your business requirements and keep them in sync!
> but i expect that we will see more innovation in formal verification
> in the future as being able to formally verifiy that the code does
> what you intended gives your agents superpowers in writing correct
> software."

Spending tokens on verification instead of agent code review
(2026-11-02):

> "maybe a hot take but i now consider adversarial reviews mostly a
> waste of tokens. far better to use those tokens on empirical combined
> with formal verification. i have updated pstack to use the interrogate
> skill less, and eventually i think i may remove it altogether
>
> i have found very little value with code review in the abstract,
> agents tend to just get lost in the nitpicks and yagnis"

In a reply to that post (2026-11-02):

> "both, to clarify i mean just having agents review code without
> running it empirically or using a deterministic checker like with
> formal verification"

From the talk (2026-11-11, machine transcript):

> "our code review process has now really shrunk into looking at
> verification artifacts instead. So things like videos, screenshots,
> diagrams, formal verification."

The cost argument, from the same talk:

> "These are just good software engineering tools, but ones that might
> have been prohibitively expensive to use before as they were hard to
> understand or write or maintain. But agents drastically cut this cost
> down"

## How it works

### Two kinds of verification

She separates two pstack skills (2026-11-05, 2026-11-08):

| Skill | What she says it does |
| --- | --- |
| `/create-verification-skill` | "the empirical verification skill, the one that teaches agents how to run your app" |
| `/create-formal-verification-skill` | "uses formal languages to prove/check certain things about your code" |

> "both types work great together!"

### The talk slide

The "formal verification" slide in the talk lists two tools:

| Tool | Slide text |
| --- | --- |
| TLA+ | "Model a state machine." "Check that its rules hold." |
| Lean | "Write proofs about code." "Check every logical step." |

### Workflow as described

1. **Create a verification skill per subsystem.**
   `/create-formal-verification-skill` is "a meta-skill that creates a
   new skill and formal verification suite based on the characteristics
   you want to verify" (2026-10-18). Her suggested prompt (2026-11-08):
   "use /create-formal-verification-skill to model these state machines,
   one skill per subsystem. and use /statechart to visualize my most
   important user flows".
2. **Pick the tool by the question.** Her post names TLA+ "to model
   state machines and systems with concurrency" and "kani in rust to
   check for undefined behavior" (2026-10-18). The skill text says: "Let
   the question choose the tool", with TLA+ as "the default" for
   "whether events can happen in a bad order", a verifier that runs on
   the code for "memory safety, overflow, or a data-structure
   invariant", and "a proof" for "a property that must hold at every
   size, where a bound is not enough".
3. **Show the check can fail.** Skill text: "A check that you have never
   seen fail proves nothing. Show each property failing on a broken
   variant of the code it guards, such as a removed check or a reordered
   step."
4. **Keep findings as findings.** Skill text: "Do not weaken the property
   or the model until it passes, and do not change product code unless
   the user asks."
5. **Record scope and sync.** Skill text: "Say what is verified, under
   which bounds and assumptions, and what is left out." The generated
   skill records "which files and functions each check covers, and the
   commit at which you last confirmed that the verification describes
   them."
6. **Let agents maintain it.** "in my game, every subsystem has its own
   formal verification skill and the agents do a good job of keeping it
   up to date" (2026-11-05).
7. **Read results as a statechart.** `/statechart` checks a TLA+ model
   and draws it as a Mermaid statechart. Skill text: "The report gives
   the shortest path to each state that breaks a rule." She says it
   "contains a mini tlc compiler that parses, lowers to a small IR, and
   has a backend that outputs mmd syntax" (2026-10-29), and that it "draws
   you a diagram based on your TLA+ specs from your user's pov"
   (2026-11-04).
8. **Confirm against the running code.** "i tend to pair it with
   empirical verification (running the code) also to confirm it's real"
   (2026-11-05).

### Where formal checks sit in her layering

From her 2026-10-16 post, as an "inverse pyramid" with most effort at
the top:

1. "codebase improvements": architecture, types, invariants, boundaries.
2. "static analysis: lint rules, tests, CI, verification (eg TLA+). very
   token efficient ways to catch issues ahead of time."
3. "prose: comments, rules, AGENTS.md, skills".
4. "human review: the hardest to scale."

From 2026-11-05:

> "so i think in the near-medium term you'll still need to layer your
> codebase: constraints and guardrails (types, lint rules, api design,
> refactoring), empirical verification (tests, evals, real usage), and
> formal verification for the parts that really need it. none of these
> catch everything on their own, but layered together, they catch a lot
> more and shrink what's left for you to review"

## Examples and tools cited

| Example or tool | What she reports | Source |
| --- | --- | --- |
| Team code modeled in TLA+ | "have already found several bugs with the skill created by /create-formal-verification-skill" | 2026-10-18 post |
| TLA+ for major user flows | "model checking of major user flows, such as, notifications across multiple devices and platforms" | 2026-11-11 talk |
| Lean for an algorithm | Used on "our own custom virtualization library" "to check that we don't have, you know, flickering or jittering problems" | 2026-11-11 talk |
| Her game, [tibo.dog](https://tibo.dog) | "used TLA+ heavily to find bugs in the game's various state machines: the story, cutscenes, the game's systems. there are many formal verification skills, one for each major system" | 2026-11-01 post |
| `/statechart` | "here's a chart of the /statechart skill and 2 real bugs i just found" | 2026-10-29 post |
| Kani (Rust) | Named for checking undefined behavior | 2026-10-18 post |
| Bend | "newer approaches like with kani and @bendlang take a different approach where there is no separate language" | 2026-10-18 post |
| Rust plus Verus | "the closest thing you might have for a strict and somewhat verifiable language for agents is rust + something like verus, but that's also not complete" | 2026-10-26 reply |
| [Pele](https://pele.run/) | Renderer the statechart skill uses for charts | 2026-10-22 and 2026-10-29 posts |
| [Bombadil](https://github.com/antithesishq/bombadil) | Property-based UI testing, listed next to formal verification. "has also caught a few UI bugs for us already" | 2026-11-11 talk |

## Stated limits and open questions

- **Spec, not intent.** "it cannot guarantee your code is bug free, only
  that it matches the spec under certain assumptions, and the specs come
  from what people want, not math. as long as we build software for
  humans, nothing can prove that your spec is right, only you can
  judge." (2026-11-05)
- **Drift.** "the spec isn't your actual code so there's always a risk
  of drift" (2026-11-05)
- **Proof cost.** "proofs cover every possible input, but only for the
  properties specified, and it takes a lot more code/work." (2026-11-05)
- **Bounded model checking.** "bounded model checking can run on your
  actual code, which avoids drift, but it only checks up to a certain
  number of steps, so it's better at finding bugs than proving there
  aren't any" (2026-11-05)
- **Not a silver bullet.** "Not a silver bullet, and we're treating it as
  another tool, another layer in our agents' environment." (2026-11-11
  talk)
- **Early tooling.** "i think we're still really early and some of these
  new languages need time to mature and an ecosystem built around them
  to succeed." (2026-10-26)
- **Code and spec sync.** "very hard problem but hopefully we will see
  more innovation in formal verification (+ keeping code/spec in sync,
  ideally in same lang like @bendlang)" (2026-10-22)
- **Verification is approximate.** "not all domains can be verified
  easily yet, and that verification is just approximation and can still
  be wrong." (2026-10-11)
- **Own expertise.** "disclaimer: i am not an expert in it" (2026-11-05)
- **Long run.** "maybe in the limit, the bitter lesson will prevail and
  flawless code will just be printed out perfectly every time with no
  bugs. even in that scenario, /statechart still seems very helpful in
  confirming that the agent understood your intent correctly."
  (2026-11-05)

## Related references she cited

- [pstack](https://github.com/cursor/plugins/tree/main/pstack), her
  plugin, which holds both skills.
- [`create-formal-verification-skill`](https://github.com/cursor/plugins/tree/main/pstack/skills/create-formal-verification-skill)
  and [`statechart`](https://github.com/cursor/plugins/tree/main/pstack/skills/statechart).
- Cindy Sridharan (`@copyconstruct`), quoted in the talk: "70% of her
  daily tokens go into verification". Tan: "I'd say that that tracks with
  what I see as well".
- Bend (`@bendlang`), Kani, Verus, Lean, Dafny, CBMC, TLA+ with TLC,
  named in her posts.

## Notes on the record

- The talk quotes come from a machine transcript published by
  agents.conffab.com. Wording can differ from the recording.
- Her X posts are lower-case in the original. Quotes keep that.
- Search found her posts and talk on agents writing and checking
  proofs. No long-form blog essay by her on this topic was found.
- Secondary write-ups of the talk exist (teamday.ai, pjfp.com,
  testsprite.com, mindpattern.ai). This page does not quote them.

## Sources

Opened 2026-11-20.

| Date and time (America/Chicago) | Source | Topic |
| --- | --- | --- |
| 2026-10-11 7:09 PM CDT | [X post](https://x.com/poteto/status/2109436202554372476) | Verification as the base agent loop |
| 2026-10-16 11:32 AM CDT | [X post](https://x.com/poteto/status/2111133080526495985) | Inverse pyramid of trust |
| 2026-10-18 4:05 PM CDT | [X post](https://x.com/poteto/status/2111926622278521253) | `/create-formal-verification-skill` launch (pstack v0.15.27) |
| 2026-10-20 9:44 PM CDT | [X post](https://x.com/poteto/status/2112736749281759566) | Statechart plus TLA+ to find bugs |
| 2026-10-22 5:33 PM CDT | [X post](https://x.com/poteto/status/2113398433977659654) | Statechart companion skill preview |
| 2026-10-26 2:02 AM CDT | [X reply](https://x.com/poteto/status/2114613597515190666) | Early tooling, Bend, Rust plus Verus |
| 2026-10-29 1:55 PM CDT | [X post](https://x.com/poteto/status/2115880102601101414) | `/statechart` stable (pstack v0.15.36) |
| 2026-11-01 5:57 PM CST | [X post](https://x.com/poteto/status/2117043478140276847) | Game built with TLA+ skills per system |
| 2026-11-02 8:04 PM CST | [X post](https://x.com/poteto/status/2117437607940681849) | Adversarial review versus verification |
| 2026-11-02 8:16 PM CST | [X reply](https://x.com/poteto/status/2117440753551204735) | Clarifies review without a checker |
| 2026-11-04 2:10 PM CST | [X reply](https://x.com/poteto/status/2118073519515025804) | Statechart from TLA+ specs |
| 2026-11-05 12:52 PM CST | [X post](https://x.com/poteto/status/2118416074601545968) | Limits and layering of formal methods |
| 2026-11-05 1:05 PM CST | [X reply](https://x.com/poteto/status/2118419507685544058) | One verification skill per subsystem |
| 2026-11-05 1:29 PM CST | [X reply](https://x.com/poteto/status/2118425409276801121) | Empirical versus formal skills |
| 2026-11-08 2:02 PM CST | [X post](https://x.com/poteto/status/2119521036660314339) | Suggested prompt |
| 2026-11-11 12:10 PM CST | [Talk transcript, "All Code Is Slop (Except Mine)"](https://agents.conffab.com/aie-code-26/live/keynotes/sessions/1794420600.md) | Review shrinks to verification artifacts; TLA+ and Lean use |
| Read 2026-11-20 | [`create-formal-verification-skill/SKILL.md`](https://github.com/cursor/plugins/blob/main/pstack/skills/create-formal-verification-skill/SKILL.md) | Skill rules quoted in the workflow |
| Read 2026-11-20 | [`statechart/SKILL.md`](https://github.com/cursor/plugins/blob/main/pstack/skills/statechart/SKILL.md) | Statechart skill |
