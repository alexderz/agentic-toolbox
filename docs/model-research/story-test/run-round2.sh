#!/bin/bash
# Story test round 2 (operator 2026-10-08): a generic prompt (setting, an AI protagonist, story shape and pace only),
# two independent stories per model, no edit step. Thinking capped at 12,432 tokens as in round 1.
# Kept as it ran on Saturn from ~/stories/round2, beside ../tools/story_test.py (the story_test.py in this folder) and
# a request-draft.json that wraps prompts/round2-prompt.txt as the single user message with max_tokens 20000.
cd "$(dirname "$0")"
T="ssh -o HostKeyAlias=titan 10.69.2.62"
$T '~/bin/gpu-lease acquire bakeoff "story test round 2 (operator): orcasaq, qwen3.8-27b-vllm, orcarouter flash-next, two stories each"' || exit 1
run() {  # model extra-json
  for i in 1 2; do STORY_BASE=$PWD python3 -u ../tools/story_test.py "$1" "$1/run$i" draft "$2"; done
}
run orcasaq2-cyber-27b '{"thinking_budget_tokens": 12432}'
run qwen3.8-27b-vllm '{"thinking_token_budget": 12432}'
run lcpp6-orcarouter-fn-uncensored '{"thinking_budget_tokens": 12432}'
$T 'curl -s -m 120 127.0.0.1:8081/unload; echo; ~/bin/gpu-lease release bakeoff'
echo "=== ROUND 2 DONE $(date -Is)"
