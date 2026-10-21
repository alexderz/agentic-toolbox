"""Story test round 3 (narration script for ElevenLabs Eleven v4), Alex 2026-10-20: one request with
prompts/round3-prompt.txt, max_tokens 32000 (round 2's 20,000 cut the longest stories off and tags add about a tenth),
thinking capped at 12,432 as in rounds 1 and 2 (llama.cpp thinking_budget_tokens; pass '{"thinking_token_budget": 12432}'
as EXTRA for vLLM instead). Writes request.json, response.json, script.md, thinking.md and check.json (narration_check.py).

  python3 round3_run.py MODEL OUTDIR [EXTRA_JSON]

TITAN_API is the OpenAI-compatible base (default http://10.69.2.62:8080/v1, Titan's llama-swap). While a GPU hold
blocks plain requests there, point it at a forwarder that adds the holder's key. The prompt is read from
prompts/round3-prompt.txt beside this script, or from round3-prompt.txt in the same folder.
"""
import json, os, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from narration_check import check

MODEL, OUT = sys.argv[1], sys.argv[2]
EXTRA = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {"thinking_budget_tokens": 12432}
BASE = os.environ.get("TITAN_API", "http://10.69.2.62:8080/v1")
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT = next(p for p in (os.path.join(HERE, "prompts", "round3-prompt.txt"), os.path.join(HERE, "round3-prompt.txt"))
              if os.path.exists(p))
prompt = open(PROMPT, encoding="utf-8").read().strip()
body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "max_tokens": 32000, **EXTRA}
json.dump(body, open(os.path.join(OUT, "request.json"), "w"), indent=1)
print(f"{time.strftime('%H:%M:%S')} start {MODEL} round 3", flush=True)
t0 = time.time()
req = urllib.request.Request(BASE + "/chat/completions", json.dumps(body).encode(), {"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=14400) as r:
    d = json.load(r)
json.dump(d, open(os.path.join(OUT, "response.json"), "w"), indent=1)
m = d["choices"][0]["message"]; script = m.get("content") or ""
think = m.get("reasoning_content") or m.get("reasoning") or ""
if not think and "</think>" in script:
    think, script = script.split("</think>", 1); think = think.replace("<think>", "")
open(os.path.join(OUT, "script.md"), "w", encoding="utf-8").write(script.strip() + "\n")
open(os.path.join(OUT, "thinking.md"), "w", encoding="utf-8").write(think.strip() + "\n")
res = check(script)
finish = d["choices"][0]["finish_reason"]
if finish != "stop":
    res["problems"].insert(0, f"finish_reason {finish}: the script may be cut off")
json.dump(res, open(os.path.join(OUT, "check.json"), "w"), indent=1)
u, t = d.get("usage", {}), d.get("timings", {})
print(f"{time.strftime('%H:%M:%S')} done: finish {finish}, story {res['words']} words, "
      f"{res['tags']} tags ({res['tags_per_100_words']}/100 words, {res['distinct_tags']} distinct), {len(res['parts'])} parts, "
      f"thinking {len(think.split())} words, completion {u.get('completion_tokens')} tokens"
      + (f", {t['predicted_ms']/1000:.0f} s at {t['predicted_per_second']:.1f} tok/s" if t else "")
      + f", wall {time.time()-t0:.0f} s; problems: {'; '.join(res['problems']) or 'none'}", flush=True)
