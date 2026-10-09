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
