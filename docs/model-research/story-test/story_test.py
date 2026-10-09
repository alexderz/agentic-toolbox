"""Story test (operator 2026-10-08): the same draft request and self-edit request as OrcaSAQ's run, for another model.
  python3 story_test.py MODEL OUTDIR [draft|edit|both]
Prompts: ../orcasaq-neuromancer/request-draft.json (verbatim, model swapped) and request-edit.json (template: the draft
between the markers and the draft's word count, rounded to 100, swapped in). Requests run on titan with curl, one at a time."""
import json, os, re, subprocess, sys, time
MODEL, OUT = sys.argv[1], sys.argv[2]; STEP = sys.argv[3] if len(sys.argv) > 3 else "both"
EXTRA = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}   # extra request fields, e.g. a thinking budget for vLLM
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "orcasaq-neuromancer")
T = ["ssh", "-o", "HostKeyAlias=titan", "10.69.2.62"]
os.makedirs(OUT, exist_ok=True)

def run(name, body):
    req = os.path.join(OUT, f"request-{name}.json"); json.dump(body, open(req, "w"))
    rt, ot = f"/tmp/story-{MODEL}-{name}.json", f"/tmp/story-{MODEL}-{name}.out"
    subprocess.run(["scp", "-q", "-o", "HostKeyAlias=titan", req, f"10.69.2.62:{rt}"], check=True)
    print(f"{time.strftime('%H:%M:%S')} start {MODEL} {name}", flush=True)
    subprocess.run(T + [f"rm -f {ot}; curl -s -m 5400 127.0.0.1:8081/v1/chat/completions -H 'Content-Type: application/json' -d @{rt} > {ot}"], check=True)
    subprocess.run(["scp", "-q", "-o", "HostKeyAlias=titan", f"10.69.2.62:{ot}", os.path.join(OUT, f"response-{name}.json")], check=True)
    d = json.load(open(os.path.join(OUT, f"response-{name}.json")))
    m = d["choices"][0]["message"]; story = m.get("content") or ""
    think = m.get("reasoning_content") or m.get("reasoning") or ""
    if not think and "</think>" in story: think, story = story.split("</think>", 1); think = think.replace("<think>", "")
    open(os.path.join(OUT, f"{'draft' if name == 'draft' else 'edited'}.md"), "w").write(story.strip() + "\n")
    open(os.path.join(OUT, f"{'draft' if name == 'draft' else 'edited'}-thinking.md"), "w").write(think.strip() + "\n")
    u, t = d.get("usage", {}), d.get("timings", {})
    print(f"{time.strftime('%H:%M:%S')} done {name}: finish {d['choices'][0]['finish_reason']}, story {len(story.split())} words, "
          f"thinking {len(think.split())} words, completion {u.get('completion_tokens')} tokens"
          + (f", {t['predicted_ms']/1000:.0f} s at {t['predicted_per_second']:.1f} tok/s" if t else ""), flush=True)
    return story

if STEP in ("draft", "both"):
    b = json.load(open(os.path.join(BASE, "request-draft.json"))); b["model"] = MODEL; b.update(EXTRA)
    t0 = time.time(); draft = run("draft", b); print(f"wall {time.time()-t0:.0f} s", flush=True)
else:
    draft = open(os.path.join(OUT, "draft.md")).read()
if STEP in ("edit", "both"):
    b = json.load(open(os.path.join(BASE, "request-edit.json"))); b["model"] = MODEL; b.update(EXTRA)
    c = b["messages"][-1]["content"]
    m = re.search(r"(=== YOUR DRAFT ===\n)(.*)(\n=== END OF DRAFT ===)", c, re.S); assert m, "draft markers"
    c = c[:m.start(2)] + draft.strip() + c[m.end(2):]
    n = round(len(draft.split()), -2)
    c, k = re.subn(r"The draft is about [\d,]+ words", f"The draft is about {n:,} words", c); assert k == 1
    b["messages"][-1]["content"] = c
    t0 = time.time(); run("edit", b); print(f"wall {time.time()-t0:.0f} s", flush=True)
