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

Both requests go to Titan's llama-swap one at a time, with nothing else running. Each model's folder under
[results/](results/) holds `draft.md`, `edited.md` and the model's thinking for each step.

## Results

| Model | Engine | Draft: words, time, speed | Edit: words, time, speed | Notes |
| --- | --- | --- | --- | --- |
| OrcaSAQ-2 Cyber 27B (`orcasaq2-cyber-27b`) | llama.cpp + DFlash2 drafts | 2,931 words; 255 s at 64.5 tok/s | 3,812 words; 232 s at about 76 tok/s | Planned at length both times (thinking longer than the story) and fell short of 5,000 words. The edit kept most of the draft and inserted passages, mostly in the fight (33% to 41% of the story); some phrases still repeat. |
