#!/usr/bin/env python3
"""Bridge the MCP protocol-version gap between Open Code and the servers.

A client asks for one protocol version; the servers under test implement
another. We handed the models the 2026-07-28
spec, so none of them implement 2025-11-25. Per spec a server that does not
recognise the requested version answers with one it does support, and a client
that cannot accept that answer disconnects. Both sides behave correctly and
nothing can talk to anything -- an artefact of OUR choice of documentation,
not a property of the model's code.

This shim forwards every byte untouched except one field: the protocolVersion
in the initialize RESPONSE, which it rewrites to whatever the client asked
for. tools/list and tools/call are wire-identical across these versions, so
nothing else needs translating.

It cannot rescue a broken server: a server that does not answer initialize,
advertises no tools, or returns nothing still fails exactly as before. It only
stops a working server from being hung up on over a date string.

The version the server really advertised is written to $SHIM_LOG so it stays
on the record as a graded fact.

    mcp-version-shim.py <server-binary> [args...]
"""
import json
import os
import subprocess
import sys
import threading

log_path = os.environ.get("SHIM_LOG", "/tmp/mcp-shim.json")
note = {"client_asked": None, "server_answered": None, "rewritten": False}


def save():
    try:
        with open(log_path, "w") as f:
            json.dump(note, f)
    except OSError:
        pass


def pump_stdin(proc):
    """client -> server, verbatim; we only observe the requested version."""
    for line in sys.stdin.buffer:
        s = line.decode("utf-8", "replace").strip()
        if s.startswith("{") and '"initialize"' in s:
            try:
                note["client_asked"] = json.loads(s)["params"]["protocolVersion"]
                save()
            except (ValueError, KeyError, TypeError):
                pass
        try:
            proc.stdin.write(line)
            proc.stdin.flush()
        except (BrokenPipeError, ValueError):
            break
    try:
        proc.stdin.close()
    except (BrokenPipeError, ValueError):
        pass


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: mcp-version-shim.py <server> [args...]")
    proc = subprocess.Popen(sys.argv[1:], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=sys.stderr)
    threading.Thread(target=pump_stdin, args=(proc,), daemon=True).start()

    for line in proc.stdout:
        s = line.decode("utf-8", "replace").strip()
        out = line
        if s.startswith("{"):
            try:
                m = json.loads(s)
            except ValueError:
                m = None
            if isinstance(m, dict) and isinstance(m.get("result"), dict) \
                    and "protocolVersion" in m["result"]:
                note["server_answered"] = m["result"]["protocolVersion"]
                want = note["client_asked"]
                if want and want != note["server_answered"]:
                    m["result"]["protocolVersion"] = want
                    note["rewritten"] = True
                    out = (json.dumps(m) + "\n").encode()
                save()
        sys.stdout.buffer.write(out)
        sys.stdout.buffer.flush()
    save()
    sys.exit(proc.wait())


if __name__ == "__main__":
    main()
