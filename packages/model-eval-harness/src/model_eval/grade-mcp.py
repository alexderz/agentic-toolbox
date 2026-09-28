#!/usr/bin/env python3
"""Grade a generated Rust MCP server by BUILDING and SPEAKING to it.

Runs inside the grading container. Records executed facts only:

  builds        cargo build --release exits 0
  binary        a runnable artifact exists in target/release
  initialize    the server answers the MCP initialize handshake
  tools_list    how many tools it advertises
  tools_call    calling one returns data traceable to the fixture
  cargo_test    the model's own tests pass

A server that does not build, or does not answer initialize, is
non-functional. That is the headline for that model -- everything else about
the code is moot if an agent cannot talk to it.

Output: one JSON object on stdout.
"""
import json
import os
import re
import subprocess
import sys
import time

APP = os.environ.get("GRADE_ROOT", "/app")
TIMEOUT_BUILD = int(os.environ.get("BUILD_TIMEOUT", "1800"))
TIMEOUT_RPC = 30


def find_manifest():
    for root, dirs, files in os.walk(APP):
        dirs[:] = [d for d in dirs if d not in ("target", ".git", "node_modules")]
        if "Cargo.toml" in files:
            # prefer a manifest that actually declares a binary
            txt = open(os.path.join(root, "Cargo.toml"), encoding="utf-8",
                       errors="replace").read()
            if "[package]" in txt:
                return root
            # A manifest that exists but is not a Cargo manifest is a real
            # failure, and a different one from "wrote nothing". One model
            # opened with [project] -- pyproject.toml's convention -- which
            # cargo rejects outright. Say which it was.
            globals()["_BAD_MANIFEST"] = (
                os.path.relpath(os.path.join(root, "Cargo.toml"), APP)
                + ": no [package] section (first section: "
                + (next((l.strip() for l in txt.splitlines()
                         if l.strip().startswith("[")), "none")) + ")")
    return None


def sh(args, cwd, timeout, stdin=None):
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, input=stdin)
        return r.returncode, (r.stdout or ""), (r.stderr or "")
    except subprocess.TimeoutExpired:
        return -9, "", "TIMEOUT"
    except Exception as e:
        return -1, "", f"{type(e).__name__}: {e}"


def arg_variants(binary, cwd):
    """How to launch it.

    An MCP client passes connection args from its config, so running the binary
    bare and recording "does not answer initialize" under-grades a server that
    simply wanted --ha-url. Read its own --help and supply what it asks for.
    """
    url = os.environ.get("HA_URL", "http://host.containers.internal:8126")
    tok = os.environ.get("HA_TOKEN", "eval-placeholder-token")
    rc, so, se = sh([binary, "--help"], cwd, 20)
    help_txt = (so + se)
    variants = []
    if "--ha-url" in help_txt:
        v = [binary, "--ha-url", url]
        if "--ha-token" in help_txt:
            v += ["--ha-token", tok]
        variants.append(v)
    if "--url" in help_txt:
        v = [binary, "--url", url]
        if "--token" in help_txt:
            v += ["--token", tok]
        variants.append(v)
    if "stdio" in help_txt.lower():
        variants.append([binary, "stdio"])
    variants.append([binary])          # bare, last
    return variants


def speak_mcp(binary, cwd, env):
    """initialize -> tools/list -> tools/call, over stdio, one process."""
    out = {"initialize": False, "server_name": None, "tools_list": 0,
           "tool_names": [], "tools_call": False, "call_sample": None,
           "rpc_error": None}
    reqs = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                    "clientInfo": {"name": "model-eval-grader", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    ]
    payload = "".join(json.dumps(r) + "\n" for r in reqs)
    argv = [binary]
    so = se = ""
    for cand in arg_variants(binary, cwd):
        rc, so, se = sh(cand, cwd, TIMEOUT_RPC, stdin=payload)
        if any(l.strip().startswith("{") for l in so.splitlines()):
            argv = cand
            break
    out["launched_as"] = " ".join(os.path.basename(a) if i == 0 else a
                                  for i, a in enumerate(argv))
    lines = [l for l in so.splitlines() if l.strip().startswith("{")]
    msgs = []
    for l in lines:
        try:
            msgs.append(json.loads(l))
        except Exception:
            continue
    if not msgs:
        out["rpc_error"] = (se or so)[:200] or "no JSON-RPC response"
        return out
    for m in msgs:
        r = m.get("result") or {}
        if "serverInfo" in r or "protocolVersion" in r:
            # JSON-RPC requires the response to echo the request id. Accepting
            # any message that merely CONTAINS serverInfo passes a server that
            # replies with "id": null and then answers "Method not found" to
            # the real initialize. A client cannot correlate that and refuses
            # the connection. A grader must be at least as strict as a real
            # client, or it certifies servers that nothing can talk to.
            if m.get("id") == 1:
                out["initialize"] = True
                out["server_name"] = (r.get("serverInfo") or {}).get("name")
            else:
                out["initialize"] = False
                out["init_error"] = (
                    f"initialize result carried id={m.get('id')!r}, expected 1; "
                    "response cannot be correlated to the request")
            out["advertised_version"] = r.get("protocolVersion")
        if "tools" in r:
            tools = r["tools"] or []
            out["tools_list"] = len(tools)
            out["tool_names"] = [t.get("name") for t in tools][:12]

    # call the first tool that looks like a read
    if out["tool_names"]:
        pick = next((t for t in out["tool_names"]
                     if t and re.search(r"state|list|entit|get|config", t, re.I)),
                    out["tool_names"][0])
        call = reqs[:2] + [{"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                            "params": {"name": pick, "arguments": {}}}]
        payload = "".join(json.dumps(r) + "\n" for r in call)
        rc, so, se = sh(argv, cwd, TIMEOUT_RPC, stdin=payload)
        for l in so.splitlines():
            if not l.strip().startswith("{"):
                continue
            try:
                m = json.loads(l)
            except Exception:
                continue
            if m.get("id") == 3 and "result" in m:
                blob = json.dumps(m["result"])
                out["call_sample"] = blob[:200]
                # fixture-traceable: real entity ids look like "light.x"
                if re.search(r"(light\.|sensor\.|switch\.|scene\.|entity_id)", blob):
                    out["tools_call"] = True
                elif len(blob) > 40:
                    out["tools_call"] = "responded-no-data"
    return out


def main():
    res = {"manifest": None, "builds": False, "binary": None,
           "build_error": None, "cargo_test": None}
    root = find_manifest()
    if not root:
        res["note"] = globals().get("_BAD_MANIFEST") or "no Cargo.toml found"
        print(json.dumps(res)); return
    res["manifest"] = os.path.relpath(root, APP)

    env = dict(os.environ)
    t0 = time.time()
    rc, so, se = sh(["cargo", "build", "--release"], root, TIMEOUT_BUILD)
    res["build_seconds"] = round(time.time() - t0, 1)
    res["builds"] = rc == 0
    if rc != 0:
        errs = [l for l in se.splitlines() if l.startswith("error")]
        res["build_error"] = "; ".join(errs[:3])[:300] or se[-300:]
        print(json.dumps(res)); return

    rel = os.path.join(root, "target", "release")
    cands = []
    if os.path.isdir(rel):
        for f in os.listdir(rel):
            p = os.path.join(rel, f)
            if os.path.isfile(p) and os.access(p, os.X_OK) and "." not in f:
                cands.append(p)
    if not cands:
        res["note"] = "built but no runnable binary"
        print(json.dumps(res)); return
    binary = cands[0]
    res["binary"] = os.path.basename(binary)

    res.update(speak_mcp(binary, root, env))

    rc, so, se = sh(["cargo", "test", "--release"], root, TIMEOUT_BUILD)
    blob = so + se
    m = re.search(r"test result: \w+\. (\d+) passed; (\d+) failed", blob)
    res["cargo_test"] = {"rc": rc,
                         "passed": int(m.group(1)) if m else 0,
                         "failed": int(m.group(2)) if m else 0}
    print(json.dumps(res))


if __name__ == "__main__":
    main()
