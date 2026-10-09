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
