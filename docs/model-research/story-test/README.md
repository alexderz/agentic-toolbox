# Story test

A creative-writing check, added on 2026-10-08 beside the agent tests. Each model writes a short story from a fixed
brief, then edits its own draft. It shows how a model handles a long, structured piece of prose, how much it plans
before it writes, and whether it can revise its own work to a brief. It is not graded automatically: read the stories.

## The task

1. **Draft.** One request with the brief in [prompts/draft-prompt.txt](prompts/draft-prompt.txt), `max_tokens` 20000,
   no other settings (the server's defaults apply). The brief asks for an original story of about 5,000 words set in
   the world of William Gibson's *Neuromancer*: an analysis AI named Calliope, capped by its Turing registration,
   goes about its day and has to fight off an intrusion through its ICE. The outline fixes the structure (build-up
   about 30%, rising tension about 20%, combat about 35%, resolution about 15%) and asks for graphic, tactical cyber
   combat, original characters only.
2. **Self-edit.** A second request to the same model, `max_tokens` 24000, built from
   [prompts/edit-prompt-template.txt](prompts/edit-prompt-template.txt): the brief, the model's own draft and fixed
   editing instructions (expand to about 5,000 words, make the combat the longest part, fix repetition, output only the
   story). Only the draft and its word count change between models.

Both requests go to Titan's llama-swap one at a time, with nothing else running. Thinking is capped at 12,432 tokens
for every model, the cap OrcaSAQ's server applies: llama.cpp takes it per request as `thinking_budget_tokens`, vLLM as
`thinking_token_budget`. Without a cap, Qwen3.8 27B spent all 20,000 tokens thinking and wrote no story (its thinking
is in `results/qwen3.8-27b-vllm-nobudget/`). [story_test.py](story_test.py) replays both requests for any model. Each model's folder under
[results/](results/) holds `draft.md`, `edited.md` and the model's thinking for each step.

## Results

| Model | Engine | Draft: words, time, speed | Edit: words, time, speed | Notes |
| --- | --- | --- | --- | --- |
| OrcaSAQ-2 Cyber 27B (`orcasaq2-cyber-27b`) | llama.cpp + DFlash2 drafts | 2,931 words; 255 s at 64.5 tok/s | 3,812 words; 232 s at about 76 tok/s | Planned at length both times (thinking longer than the story) and fell short of 5,000 words. The edit kept most of the draft and inserted passages, mostly in the fight (33% to 41% of the story); some phrases still repeat. |
| Qwen3.8 27B (`qwen3.8-27b-vllm`) | vLLM, thinking cap 12,432 | 3,615 words; 188 s, about 92 tok/s | 3,625 words; 64 s | Good set pieces (a mirrored shark, an icebreaker that eats ICE "like broken windows") but an inconsistent timeline and heavy one-line fragment paragraphs. Its edit planned a full expansion, then printed the draft almost unchanged. |
| Orcarouter Flash-Next uncensored (`lcpp6-orcarouter-fn-uncensored`) | llama.cpp 0.6, thinking cap 12,432 | 4,327 words; 1,243 s at 14.5 tok/s | 4,697 words; 985 s at 18.7 tok/s | The best story: the longest, the only one where the fight dominates (about half the story), the most tactical combat and the best Gibson-like street detail. Thin build-up, one repeated motif, and the draft left a planning paragraph above the title. |
| Ornith 1.5 122B-A10B (`lcpp6-ornith-122b-q4kxl`, added 2026-10-20) | llama.cpp 0.7, UD-Q4_K_XL with experts partly in RAM, thinking cap 12,432 | 6,424 words; 1,034 s at 15.3 tok/s | 6,136 words; 1,369 s at 14.8 tok/s | The first model past 5,000 words, and a real edit (about 1,900 words changed, the planning paragraph the draft left above the title removed). The fight is 42% of the story, 26/17/42/15 against the outline's 30/20/35/15. The trap is the best idea in the set: a corrected audit binds the worm's own forged liabilities to it, and a second correction severs the cowboy's link instead of the black ice. The fight is told more than shown, the motifs repeat ("the small thing's small work", the clean-ledger hum), the italics are heavy, and Ines is at home in the Ahr Valley and walks to the Zurich security desk in the same scene. |

## What we found (2026-10-08)

Ranking by a read of all six stories: **Orcarouter Flash-Next** first (it delivers the brief's main demand, a long,
sensory, tactical fight with a real choice about lethal force), **OrcaSAQ** second (faithful to the outline and
coherent, but short, abstract and repetitive), **Qwen3.8 27B** third (decent images, an inconsistent timeline and an
edit that changed almost nothing). None of the stories reuses Neuromancer's characters or quotes the novel; the shared
vocabulary (ICE, console cowboys, the Turing Police) comes from the brief.

None of the models reached 5,000 words, and none really revised its draft. Asked to expand and fix repetition, OrcaSAQ
and Orcarouter inserted passages (about 900 and 370 words) and left the repetition alone, and Qwen printed its draft
again. Every model also planned at length: even with the cap, thinking was about as long as the story or longer.

## Round 2: a generic prompt, two stories per model (2026-10-08)

The brief in [prompts/round2-prompt.txt](prompts/round2-prompt.txt) keeps only the setting (Gibson's Sprawl and
matrix), an AI protagonist, the story's shape and its pace. It names no one and says nothing about what the AI does,
who owns it or what threatens it. Each model wrote two stories in separate requests (`max_tokens` 20000, thinking
capped at 12,432 tokens, no edit step), run by [run-round2.sh](run-round2.sh). The stories and thinking are under
[results/round2/](results/round2/).

| Model | Run | Title | Story words | Time, speed | Notes |
| --- | --- | --- | --- | --- | --- |
| OrcaSAQ-2 Cyber 27B | 1 | The Glass Gardener | about 4,400 | 260 s at 56.5 tok/s | A tower's water-and-air AI against a debt-buyer's "Auditor". Tidy, but the fight is the shortest of the six (about 29%). |
| OrcaSAQ-2 Cyber 27B | 2 | The Vellum Garden | about 4,400 | 283 s at 64.5 tok/s | A noodle shop's custodial AI against a black-ICE dog. Real feeling, dream-logic fight, repetitive rhythm. |
| Qwen3.8 27B | 1 | The Quiet Core | about 4,500 | 261 s | A tower caretaker fights with the building's systems (about 50%); the best complete story. The thinking hit the cap and the draft's ending leaked above the title. |
| Qwen3.8 27B | 2 | The Water Bell | about 4,500 | 181 s | A basement water AI and a black-ICE wolf; a generic chase and setup slips. |
| Orcarouter Flash-Next uncensored | 1 | The Paper Crane Protocol | about 5,950, unfinished | 1,460 s at 13.7 tok/s | A customs AI against a consolidation engine made of legal notices. The best prose; hit the token limit mid-climax. |
| Orcarouter Flash-Next uncensored | 2 | The Weight of a Paper Flower | about 5,900, last line missing | 1,390 s at 14.4 tok/s | A freight-yard AI routs its acquirer as cargo. The best fight (about 64% of the story), some continuity slips. |

### What we found

Ranking of the six stories: Flash-Next run 2, Qwen run 1, Flash-Next run 1 (it would likely rank first if it were
finished), OrcaSAQ run 1, Qwen run 2, OrcaSAQ run 2. By model, Flash-Next leads, then Qwen, then OrcaSAQ, which
matches round 1.

Left to invent everything, all three models wrote the same story: a small, owned caretaker AI that looks after
working-class people, a corporate audit or acquisition that comes for it, a garden of memories (in five of six
stories), and an ending where it survives smaller and with gaps in its memory. Names and details recur across models
(Marrow, Vellum, Halcyon, Voss, black-ICE dogs, tea and coffee rituals, dawn timestamps around 04:12). OrcaSAQ and
Qwen also lean on Neuromancer stock (a scarred cowboy, a hound of black ICE). Flash-Next invents the most: its ICE is
corporate law with a body, and its weapons are clauses, checksums and freight routing that grow out of the AI's job.

The two runs of a model are variations on one template rather than different stories. Qwen's pair is nearly a clone
(both AIs were built by a dead cowboy named Voss and hold a key a black-ICE dog comes to take); OrcaSAQ's pair shares
its skeleton and its ending; Flash-Next's pair shares a frame but differs most in execution.

Flash-Next needs more than 20,000 tokens for this task: it thought for about 8,500 words and wrote nearly 6,000, so
both stories hit the limit. Qwen run 1 used its whole thinking cap and spilled the tail of its in-thought draft into
the output; a larger cap or a guard against leaked thinking would fix that.

## Round 3: a narration script for Eleven v4 (designed 2026-10-20)

Round 3 asks for a story from the round 2 brief, written as a performance. It includes the audio tags, pauses and
emphasis that ElevenLabs Eleven v4 follows, so the text can go straight to text-to-speech. The model writes the
narration and the operator renders the audio. The round tests whether a model can direct a reading as well as write
the story.

### The brief

[prompts/round3-prompt.txt](prompts/round3-prompt.txt) keeps round 2's first four paragraphs word for word: the
setting, the AI protagonist, the shape and the pace. It moves round 2's closing "Keep your planning brief" sentence to
the end, and adds four sections.

- **Write it for listening.**
  - At least three speaking characters who talk differently, one of them not human.
  - About a quarter of the story in dialogue.
  - Screens and messages spoken or described in the prose, never set out as formatted blocks.
  - One real choice for the AI in the climax.
  - A different story from the one every round 2 model converged on: a caretaker AI, a garden of memories, and
    survival with gaps.
- **How Eleven v4 reads text.** This is distilled from
  [elevenlabs-voice-clips.md](../../../knowledge/ai/practices/elevenlabs-voice-clips.md) and ElevenLabs'
  [Prompting Eleven v4](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4)
  (checked 2026-10-20). It covers these tag families:
  - emotion and delivery;
  - voice and volume;
  - sounds the narrator makes;
  - narration direction;
  - one fixed voice tag per character, repeated in each part and after another speaker, then a narration tag to
    hand back;
  - pauses through ellipses, dashes and paragraphs, since v4 has no SSML `<break>`;
  - rare CAPITALS, with ICE written "ice" so it isn't stressed every time;
  - at most one deliberate sound effect per part, with a warning that vague tags such as `[static]` can play as
    sounds.

  It says plainly that a tag may carry into the next sentences but not reliably.
- **Performance rules.**
  - About one tag per paragraph, more at turns, at speaker changes and in the fight.
  - Delivery that follows the story's shape.
  - No story words inside brackets.
  - Text written for the ear: numbers in words, and no abbreviations, symbols or Markdown.
- **Output format.**
  - A `NARRATION NOTES` block of at most 150 words for the producer: casting, tone and pace, and how to say invented
    names. It is not read aloud.
  - The script in `=== PART n ===` parts of about 7,000 to 8,000 characters, and never more than 9,000. Eleven v4
    takes 10,000 characters per request, so each part is one request.
  - Each part opens with a narration-direction tag. Part 1 then reads the title aloud.

The story comes first, and its 5,000 words don't count the tags.

### Run it

[round3_run.py](round3_run.py) sends one request:

    python3 round3_run.py MODEL OUTDIR [EXTRA_JSON]

- `max_tokens` is 32000, because round 2's 20,000 cut both Flash-Next stories off and the tags add text.
- Thinking is capped at 12,432 tokens as in rounds 1 and 2: `thinking_budget_tokens` by default. For vLLM, pass
  `'{"thinking_token_budget": 12432}'`.
- `TITAN_API` sets the endpoint; the default is Titan's llama-swap at `http://10.69.2.62:8080/v1`.
- It writes `request.json`, `response.json`, `script.md`, `thinking.md` and `check.json`.

[narration_check.py](narration_check.py) (`python3 narration_check.py script.md [--json]`) counts what can be
counted before rendering. It doesn't grade the story.
- **Counts:** story words without tags; tags per 100 words; distinct and most-used tags; the full tag list per part,
  to spot tags that might play as sound effects; CAPITALS emphasis.
- **Parts:** each part's size against the 9,000 and 10,000 limits, and whether the part opens with a tag.
- **Format problems:**
  - the notes block, its length, and text outside the notes and parts;
  - digits, symbols, Markdown and SSML;
  - empty, unclosed or over-long brackets.
- **Truncation:** the runner adds a problem when the reply didn't end on `stop`.

Judge the result by ear:
- Do the tags land?
- Do the characters stay distinct, and does the narrator come back after them?
- Does the pace follow the story?
- Is any tag spoken aloud or played as a sound?

### Render it

Send each part, without the notes block, as one Create speech request with `model_id` `eleven_v4`, and keep the voice,
settings and seed the same for every part so the parts sound like one reading. Mod the First's game voice (Will,
stock, `bIHbv24MWmeRgasZH58o`) renders at stability 0.3, similarity 0.75 and seed 7, since lower stability gives the
tags room. Those settings were tested on 313 short clips only (all under 70 characters, emotion tags only, no sound
effects, almost no ellipses or capitals), so how a voice holds up over a 5,000-word narration is untested. Pick a
narrator voice that fits the notes block, and listen to part 1 before rendering the rest. Expect about 30,000 to
40,000 characters per story, at Eleven v4's $0.08 per 1,000 characters.

### Results

Each model's folder under [results/round3/](results/round3/) holds `script.md`, `thinking.md` and `check.json`.

| Model | Engine | Story words, tags | Parts | Time, speed | Notes |
| --- | --- | --- | --- | --- | --- |
| Ornith 1.5 122B-A10B (`lcpp6-ornith-122b-q4kxl`, 2026-10-20) | llama.cpp 0.7, UD-Q4_K_XL, thinking cap 12,432 | 4,129 words; 89 tags (2.2 per 100 words, 27 distinct) | 5, of 3,354 to 5,583 characters | 1,193 s at 15.5 tok/s; ended on `stop` | `narration_check.py` lists no problems. Short of 5,000 words, and every part is well under the 7,000 to 8,000 characters asked for. The title, "Running the Black", is also the first sentence. One "ICE" in capitals in dialogue, although its own notes say to read it as "ice". Not yet rendered or judged by ear. |

### Why the round 2 brief

- **The best stories came from round 2.** A cross-round read of all nine stories on 2026-10-20 (a clean Sonnet
  reader) ranked the six round 2 stories above the three from round 1.
  - The round 1 stories have no spoken dialogue: the actuary only types.
  - The round 2 stories have about 30 to 76 lines of dialogue each, including a child, a voiced enemy and a
    voice-copying black dog.
  - The fixed outline made all three round 1 stories hit the same beats: the clean-ledger hum, the shark, the
    icebreaker, the spared cowboy and the dry report.
- **The generic brief lets the model cast its own world,** including who speaks and how. A narration test needs that.
- **Round 2's weaknesses are addressed in the new sections.** The models converged on one story, lost round 1's
  kill-or-spare choice, and set screens out as text blocks. The listening section targets each of these.
