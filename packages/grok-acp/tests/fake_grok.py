#!/usr/bin/env python3
"""Fake `grok agent ... stdio`: just enough ACP for the client tests.

Behaviour is switched by environment variables so one file covers every case:
FAKE_LOG          append each received method name to this file
FAKE_SLOW_NEW     seconds to sleep before answering session/new
FAKE_HANG         never finish the prompt on its own
FAKE_IGNORE_CANCEL  with FAKE_HANG: also ignore session/cancel
FAKE_ASK          send one session/request_permission before finishing
FAKE_FAIL_RESUME  answer session/resume with an error
FAKE_CHILD_PID    spawn a detached `sleep` and write its pid to this file
"""

import json
import os
import subprocess
import sys
import time
import uuid

env = os.environ


def out(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def reply(mid, result):
    out({"jsonrpc": "2.0", "id": mid, "result": result})


def finish(mid):
    chunk = {"sessionUpdate": "agent_message_chunk", "content": {"text": "done"}}
    out({"jsonrpc": "2.0", "method": "session/update", "params": {"update": chunk}})
    reply(mid, {"stopReason": "end_turn", "_meta": {"modelId": "fake"}})


prompt_id = None
for line in sys.stdin:
    msg = json.loads(line)
    method = msg.get("method")
    if env.get("FAKE_LOG"):
        with open(env["FAKE_LOG"], "a") as log:
            log.write(f"{method or 'response'}\n")
    if method == "initialize":
        caps = {"sessionCapabilities": {"resume": {}}}
        reply(msg["id"], {"protocolVersion": 1, "agentCapabilities": caps})
    elif method == "session/new":
        time.sleep(float(env.get("FAKE_SLOW_NEW", "0")))
        reply(msg["id"], {"sessionId": str(uuid.uuid4())})
    elif method == "session/resume":
        if env.get("FAKE_FAIL_RESUME"):
            error = {"code": -32603, "message": "Path not found."}
            out({"jsonrpc": "2.0", "id": msg["id"], "error": error})
        else:
            reply(msg["id"], {})
    elif method == "session/prompt":
        prompt_id = msg["id"]
        if env.get("FAKE_CHILD_PID"):
            child = subprocess.Popen(["sleep", "300"], start_new_session=True)
            with open(env["FAKE_CHILD_PID"], "w") as fh:
                fh.write(str(child.pid))
        if env.get("FAKE_ASK"):
            options = [
                {"optionId": "no", "kind": "reject_once"},
                {"optionId": "once", "kind": "allow_once"},
                {"optionId": "always", "kind": "allow_always"},
            ]
            out(
                {
                    "jsonrpc": "2.0",
                    "id": 9000,
                    "method": "session/request_permission",
                    "params": {"options": options},
                }
            )
        elif not env.get("FAKE_HANG"):
            finish(prompt_id)
    elif method == "session/cancel":
        if prompt_id is not None and not env.get("FAKE_IGNORE_CANCEL"):
            reply(prompt_id, {"stopReason": "cancelled"})
    elif method is None and msg.get("id") == 9000:
        picked = msg["result"]["outcome"]["optionId"]
        if env.get("FAKE_LOG"):
            with open(env["FAKE_LOG"], "a") as log:
                log.write(f"picked={picked}\n")
        finish(prompt_id)
