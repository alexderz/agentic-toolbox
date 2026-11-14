#!/usr/bin/env python3
"""Distil one case's events.jsonl into meta.json.

Extracted from run-case.sh so the host runner and the sandboxed runner share
one implementation. Two copies of metrics logic drift, and a metrics bug is
indistinguishable from a model failure -- that has already cost this harness
a full night (venv counted as model output, shebang scripts counted as zero).

Usage: distil-meta.py <out_dir> <case> <model> <flags> <load_s> <vram> <dur>
"""
import sys,json,os,glob
out,case,model,flags,load_s,vram,dur = sys.argv[1:8]
ev=[]
p=os.path.join(out,"events.jsonl")
if os.path.exists(p):
    for line in open(p,encoding="utf-8",errors="replace"):
        line=line.strip()
        if not line: continue
        try: ev.append(json.loads(line))
        except Exception: pass
def dig(o,*keys):
    for k in keys:
        if isinstance(o,dict) and k in o: o=o[k]
        else: return None
    return o
# Pi streams token-level `message_update` deltas whose usage fields are all
# zero; the real totals ride on message_end/turn_end. Taking a max across all
# events therefore reported 0 tokens for every model. Sum the terminal events
# and count turns from turn_start, not from every streamed message.
tin=tout=cacheR=cacheW=0
turns=sum(1 for e in ev if e.get("type")=="turn_start")
tools=sum(1 for e in ev if e.get("type")=="tool_execution_start")
for e in ev:
    if e.get("type") not in ("message_end","turn_end"): continue
    u=e.get("usage") or dig(e,"message","usage") or {}
    tin    += u.get("input")     or u.get("input_tokens")  or u.get("prompt_tokens")     or 0
    tout   += u.get("output")    or u.get("output_tokens") or u.get("completion_tokens") or 0
    cacheR += u.get("cacheRead") or 0
    cacheW += u.get("cacheWrite") or 0
# Round 2 lets models install packages, so a work dir can contain a venv,
# pip's own source, caches and build artifacts. Counting those reported 816,923
# LOC for a ~300 line tool. Only count what the model actually authored.
_SKIP_DIRS = {"venv", ".venv", "env", ".env", "site-packages", "__pycache__",
              ".pytest_cache", ".git", "node_modules", "build", "dist",
              ".mypy_cache", ".ruff_cache", ".tox", "lib", "lib64", "bin",
              "include", "share", "wheels",
              # Rust: `target` is cargo's build output and `.cargo` its cache.
              # Counting them reported 2939 "files created" for a project whose
              # actual source was a handful -- the same mistake as counting a
              # venv, one language over.
              "target", ".cargo", "registry", ".session", "incremental", "deps"}
def _authored(path, root):
    rel = os.path.relpath(path, root)
    parts = rel.split(os.sep)
    if any(p in _SKIP_DIRS for p in parts[:-1]):
        return False
    if any(p.endswith(".egg-info") or p.endswith(".dist-info") for p in parts):
        return False
    return not path.endswith((".pyc", ".pyo", ".so", ".whl"))
_root=os.path.join(out,"work")
files=[f for f in glob.glob(os.path.join(_root,"**","*"),recursive=True)
       if os.path.isfile(f) and _authored(f,_root)]
# Detect python by shebang as well as extension: qwen3-coder writes
# `ha-api` with no extension, and an extension-only test scored that
# complete tool as 0 LOC.
def _is_py(path):
    if path.endswith(".py"): return True
    try:
        first=open(path,"rb").readline(200).decode("utf-8","replace")
        return first.startswith("#!") and "python" in first
    except Exception: return False
py=[f for f in files if _is_py(f)]
loc=0
for f in py:
    try: loc+=sum(1 for _ in open(f,encoding="utf-8",errors="replace"))
    except Exception: pass
import ast as _ast
def _ok(f):
    try: _ast.parse(open(f,encoding="utf-8",errors="replace").read()); return True
    except Exception: return False
syntax_ok=sum(1 for f in py if _ok(f))
_sz={}
for f in py: _sz.setdefault(os.path.getsize(f),[]).append(os.path.basename(f))
dupes=[v for v in _sz.values() if len(v)>1]
stalled=os.path.exists(os.path.join(out,"stderr.log")) and "STALLED:" in open(os.path.join(out,"stderr.log"),encoding="utf-8",errors="replace").read()
status="stalled_no_output" if stalled else ("ok" if files else ("no_files" if ev else "no_output"))
meta=dict(case=case,model=model,flags=flags,status=status,
          load_seconds=int(load_s),vram_mib=int(vram),duration_s=float(dur),
          events=len(ev),turns=turns,tool_events=tools,
          input_tokens=tin,output_tokens=tout,cache_read=cacheR,cache_write=cacheW,
          tok_per_s=round(tout/float(dur),2) if tout and float(dur)>0 else None,
          files_created=len(files),py_files=len(py),py_loc=loc,
          py_names=[os.path.basename(f) for f in py],
          py_syntax_ok=syntax_ok,duplicate_groups=dupes)
json.dump(meta,open(os.path.join(out,"meta.json"),"w"),indent=2)
print(f"  events={len(ev)} turns={turns} out_tok={tout} dur={dur}s files={len(files)} py_loc={loc}")
