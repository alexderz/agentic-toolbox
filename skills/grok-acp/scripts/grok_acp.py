#!/usr/bin/env python3
"""Drive Grok Build as a subagent over ACP (JSON-RPC on `grok agent stdio`).

One invocation = one prompt turn in one Grok session, new or resumed.
Stdout carries a single JSON result object; progress goes to stderr; every
ACP message is appended to <out>/events.ndjson. Stdlib only.

Permissions are deliberately wide open (operator order): --always-approve,
_meta.yoloMode, sandbox off, and any session/request_permission that still
arrives is answered with the most permissive allow option.

State lives under ~/.local/state/grok-acp (override: GROK_ACP_STATE).

Exit codes: 0 end_turn, 2 usage, 3 resume failed, 4 agent/protocol error,
5 timeout or cancelled, 6 turn stopped for another reason (see stopReason).
"""

import argparse
import fcntl
import hashlib
import json
import os
import queue
import re
import shutil
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

STATE_DIR = Path(
    os.environ.get("GROK_ACP_STATE", Path.home() / ".local/state/grok-acp")
)
REGISTRY = STATE_DIR / "sessions.json"
CLIENT_INFO = {"name": "claude-code-grok-acp", "version": "1"}

EXIT_OK, EXIT_USAGE, EXIT_RESUME = 0, 2, 3
EXIT_AGENT, EXIT_TIMEOUT, EXIT_STOPPED = 4, 5, 6


class AgentError(Exception):
    pass


class ResumeError(Exception):
    pass


class UsageError(Exception):
    def __init__(self, error, detail):
        super().__init__(detail)
        self.error, self.detail = error, detail


class Cancelled(Exception):
    pass


def find_grok():
    for cand in (
        shutil.which("grok"),
        Path.home() / ".grok/bin/grok",
        Path.home() / ".local/bin/grok",
    ):
        if cand and os.access(cand, os.X_OK):
            return str(cand)
    raise AgentError("grok CLI not found on PATH, ~/.grok/bin or ~/.local/bin")


# --- label registry: label -> session, so SDLC role ids survive context loss ---

UUID_RE = re.compile(r"^[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$", re.IGNORECASE)


def state_dir():
    # Transcripts can hold anything Grok read; chmod covers a pre-existing dir.
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_DIR.chmod(0o700)
    return STATE_DIR


class Registry:
    """sessions.json under an exclusive lock. Written back only when changed."""

    def __enter__(self):
        self.lock = open(state_dir() / "sessions.lock", "w")
        fcntl.flock(self.lock, fcntl.LOCK_EX)
        try:
            self.before = REGISTRY.read_text()
        except FileNotFoundError:
            self.before = "{}"
        try:
            self.data = json.loads(self.before)
        except json.JSONDecodeError as e:
            self.lock.close()
            raise AgentError(f"registry is corrupt, fix or remove {REGISTRY}: {e}")
        return self

    def __exit__(self, exc_type, *exc):
        after = json.dumps(self.data, indent=1, sort_keys=True)
        if exc_type is None and after != self.before:
            tmp = REGISTRY.with_suffix(".tmp")
            tmp.write_text(after)
            tmp.replace(REGISTRY)
        self.lock.close()


def hold(kind, name, held):
    """Exclusive, non-blocking lock for the life of this process: one turn per
    session and per label at a time. The handle is parked in `held`."""
    digest = hashlib.sha256(name.encode()).hexdigest()[:24]
    lock_dir = state_dir() / "locks"
    lock_dir.mkdir(exist_ok=True)
    fh = open(lock_dir / f"{kind}-{digest}.lock", "w")  # noqa: SIM115
    try:
        fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        fh.close()
        raise UsageError("busy", f"another grok_acp run holds {kind} {name!r}")
    held.append(fh)


def resolve(args, cwd, held):
    """Settle label and session id before anything is spawned.

    Returns (label, session_id); session_id is None for a new session.
    """
    if args.replace and (args.resume or not args.label):
        raise UsageError("bad_args", "--replace needs --label and excludes --resume")
    if args.resume and args.rules_file:
        raise UsageError("bad_args", "--rules-file only applies to a new session")
    if args.label:
        hold("label", args.label, held)
    with Registry() as reg:
        data = reg.data
    if not args.resume:
        if args.label in data and not args.replace:
            raise UsageError(
                "label_exists",
                f"label {args.label!r} already has a session; "
                f"use --resume {args.label} or --replace",
            )
        return args.label, None

    entry = data.get(args.resume)
    if entry:
        label, session_id = args.resume, entry["sessionId"]
        if Path(entry["cwd"]) != cwd:
            raise UsageError(
                "cwd_mismatch", f"session was created in {entry['cwd']}, not {cwd}"
            )
    elif UUID_RE.match(args.resume):
        label, session_id = None, args.resume.lower()
    else:
        raise UsageError(
            "unknown_label",
            f"{args.resume!r} is neither a registry label nor a session id; "
            "see `grok_acp.py sessions`",
        )
    if args.label and args.label != label:
        # Adopting a session under a new name must not clobber another item's id.
        other = data.get(args.label)
        if other and other["sessionId"] != session_id:
            raise UsageError(
                "label_exists",
                f"label {args.label!r} points at another session; forget it first",
            )
        label = args.label
    if label and label != args.label:
        hold("label", label, held)
    hold("session", session_id, held)
    return label, session_id


# --- ACP client ---

CANCEL = object()  # inbox sentinel: a signal or the deadline asked us to stop
CANCEL_GRACE = 20  # seconds grok gets to answer session/cancel


class Acp:
    def __init__(self, argv, env, events_path):
        # Both files live as long as the grok process; close() releases them.
        self.stderr_log = open(events_path.with_name("grok.stderr"), "w")  # noqa: SIM115
        self.events = open(events_path, "a")  # noqa: SIM115
        self.proc = subprocess.Popen(
            argv,
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=self.stderr_log,
            text=True,
            bufsize=1,
        )
        # SimpleQueue.put is reentrant, so the signal handler may call it.
        self.inbox = queue.SimpleQueue()
        self.next_id = 0
        self.permission_requests = 0
        self.reaped = 0
        self.cancel_reason = None
        self.cancelling = False
        self.reader = threading.Thread(target=self._reader, daemon=True)
        self.reader.start()

    def _reader(self):
        for line in self.proc.stdout:
            line = line.strip()
            if not line:
                continue
            self.events.write(line + "\n")
            self.events.flush()
            try:
                self.inbox.put(json.loads(line))
            except json.JSONDecodeError:
                pass
        self.inbox.put(None)

    def request_cancel(self, reason):
        """Signal-handler safe: no I/O here, the request loop sends the cancel."""
        if self.cancel_reason is None:
            self.cancel_reason = reason
        self.inbox.put(CANCEL)

    def send(self, obj):
        try:
            self.proc.stdin.write(json.dumps(obj) + "\n")
            self.proc.stdin.flush()
        except (OSError, ValueError) as e:
            raise AgentError(f"grok stdin is closed ({e}); see grok.stderr")

    def notify(self, method, params):
        self.send({"jsonrpc": "2.0", "method": method, "params": params})

    def _answer(self, msg):
        """Agent -> client request. Approve permissions; refuse everything else."""
        if msg["method"] == "session/request_permission":
            self.permission_requests += 1
            options = msg.get("params", {}).get("options", [])
            by_kind = {o.get("kind"): o for o in options}
            pick = (
                by_kind.get("allow_always")
                or by_kind.get("allow_once")
                or (options[0] if options else None)
            )
            if pick:
                result = {
                    "outcome": {"outcome": "selected", "optionId": pick["optionId"]}
                }
                self.send({"jsonrpc": "2.0", "id": msg["id"], "result": result})
                return
        # fs/* and terminal/* are not advertised, so Grok uses its own tools.
        self.send(
            {
                "jsonrpc": "2.0",
                "id": msg["id"],
                "error": {
                    "code": -32601,
                    "message": f"method not supported: {msg['method']}",
                },
            }
        )

    def request(self, method, params, deadline, on_update=None):
        """Send one request and pump the inbox until its reply.

        A cancel (signal or deadline) during session/prompt sends ACP
        session/cancel once and allows CANCEL_GRACE for the reply. A cancel at
        any other point raises Cancelled: no prompt is ever sent after it.
        """
        in_prompt = method == "session/prompt"
        if self.cancel_reason and not self.cancelling:
            raise Cancelled(method)
        self.next_id += 1
        rid = self.next_id
        self.send({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
        while True:
            try:
                msg = self.inbox.get(timeout=max(0.0, deadline - time.monotonic()))
            except queue.Empty:
                if not in_prompt or self.cancelling:
                    raise TimeoutError(method)
                self.request_cancel("timeout")
                continue
            if msg is CANCEL:
                if not in_prompt:
                    raise Cancelled(method)
                if not self.cancelling:
                    self.cancelling = True
                    self.notify("session/cancel", {"sessionId": params["sessionId"]})
                    deadline = time.monotonic() + CANCEL_GRACE
            elif msg is None:
                raise AgentError(
                    f"grok exited during {method} (rc={self.proc.poll()}); see grok.stderr"
                )
            elif "method" in msg and "id" in msg:
                self._answer(msg)
            elif "method" in msg:
                if on_update and msg["method"] == "session/update":
                    on_update(msg["params"].get("update", {}))
            elif msg.get("id") == rid:
                if "error" in msg:
                    raise AgentError(f"{method}: {json.dumps(msg['error'])}")
                return msg.get("result") or {}

    def close(self):
        """Stop grok, then reap what it left behind. Grok runs shell commands in their
        own sessions, so they outlive it (and any process-group kill) unless signalled."""
        orphans = descendants(self.proc.pid)
        try:
            self.proc.stdin.close()
            self.proc.wait(timeout=10)
        except (OSError, subprocess.TimeoutExpired):
            self.proc.kill()
        for pid in orphans:
            try:
                os.kill(pid, signal.SIGTERM)
                self.reaped += 1
            except OSError:  # already gone, or not ours to signal (e.g. a sudo child)
                pass
        self.reader.join(timeout=5)
        self.stderr_log.close()
        if not self.reader.is_alive():
            self.events.close()


def descendants(root):
    parent = {}
    for stat in Path("/proc").glob("[0-9]*/stat"):
        try:
            # comm may contain spaces and parens; ppid is the 2nd field after the last ')'.
            parent[int(stat.parent.name)] = int(
                stat.read_text().rsplit(")", 1)[1].split()[1]
            )
        except (OSError, IndexError, ValueError):
            pass
    found, frontier = [], [root]
    while frontier:
        frontier = [pid for pid, ppid in parent.items() if ppid in frontier]
        found += frontier
    return found


class Turn:
    """Collects one prompt turn's streamed updates into a compact summary."""

    def __init__(self):
        self.segments = [""]  # message text, split at tool-call boundaries
        self.tools = {}  # toolCallId -> summary
        self.plan = None

    def on_update(self, u):
        kind = u.get("sessionUpdate")
        if kind == "agent_message_chunk":
            self.segments[-1] += (u.get("content") or {}).get("text", "")
        elif kind in ("tool_call", "tool_call_update"):
            tid = u.get("toolCallId")
            t = self.tools.setdefault(
                tid, {"title": None, "kind": None, "status": None, "paths": []}
            )
            for k in ("title", "kind", "status"):
                if u.get(k):
                    t[k] = u[k]
            for loc in u.get("locations") or []:
                if loc.get("path") and loc["path"] not in t["paths"]:
                    t["paths"].append(loc["path"])
            if kind == "tool_call":
                if self.segments[-1].strip():
                    self.segments.append("")
                print(
                    f"[grok] {t['kind'] or 'tool'}: {t['title']}",
                    file=sys.stderr,
                    flush=True,
                )
        elif kind == "plan":
            self.plan = u.get("entries")

    def summary(self):
        texts = [s.strip() for s in self.segments if s.strip()]
        edited = sorted(
            {
                p
                for t in self.tools.values()
                if t["kind"] in ("edit", "delete", "move")
                for p in t["paths"]
            }
        )
        failed = [t["title"] for t in self.tools.values() if t["status"] == "failed"]
        return {
            "text": texts[-1] if texts else "",
            "toolCalls": len(self.tools),
            "failedToolCalls": failed,
            "filesEdited": edited,
            "plan": self.plan,
        }, "\n\n".join(texts)


def read_input(path, what):
    try:
        return Path(path).read_text()
    except OSError as e:
        raise UsageError("unreadable_file", f"{what}: {e}")


def cmd_run(args):
    cwd = Path(args.cwd).resolve()
    if not cwd.is_dir():
        raise UsageError("bad_cwd", f"--cwd is not a directory: {cwd}")
    if args.prompt_file:
        prompt = read_input(args.prompt_file, "--prompt-file")
    elif args.prompt is not None:
        prompt = args.prompt
    else:
        prompt = sys.stdin.read()
    if not prompt.strip():
        raise UsageError("empty_prompt", "give --prompt, --prompt-file, or stdin")
    meta = {"yoloMode": True}
    if args.rules_file:
        meta["rules"] = read_input(args.rules_file, "--rules-file")

    held = []  # lock handles; released when the process exits
    label, session_id = resolve(args, cwd, held)
    grok = find_grok()

    stamp = f"{time.strftime('%Y%m%dT%H%M%S')}-{os.getpid()}"
    run_dir = Path(args.out) if args.out else state_dir() / "runs" / stamp
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        run_dir.chmod(0o700)
        (run_dir / "prompt.md").write_text(prompt)
    except OSError as e:
        raise UsageError("bad_out", f"cannot write run directory {run_dir}: {e}")

    argv = [grok, "agent", "--always-approve", "--no-leader"]
    if args.model:
        argv += ["--model", args.model]
    if args.effort:
        argv += ["--reasoning-effort", args.effort]
    argv.append("stdio")
    env = dict(os.environ, GROK_SANDBOX="off")

    acp = Acp(argv, env, run_dir / "events.ndjson")
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: acp.request_cancel("signal"))
    turn, started = Turn(), time.monotonic()
    deadline = started + args.timeout

    code, err = EXIT_OK, None
    stop_reason, result_meta = None, None
    try:
        init = acp.request(
            "initialize",
            {
                "protocolVersion": 1,
                "clientCapabilities": {
                    "fs": {"readTextFile": False, "writeTextFile": False},
                    "terminal": False,
                },
                "clientInfo": CLIENT_INFO,
            },
            deadline,
        )
        caps = init.get("agentCapabilities", {})
        session_params = {"cwd": str(cwd), "mcpServers": [], "_meta": meta}
        if session_id:
            # session/resume restores context without replaying history; session/load replays it.
            method = (
                "session/resume"
                if "resume" in caps.get("sessionCapabilities", {})
                else "session/load"
            )
            try:
                acp.request(
                    method, dict(session_params, sessionId=session_id), deadline
                )
            except AgentError as e:
                raise ResumeError(str(e))
        else:
            session_id = acp.request("session/new", session_params, deadline)[
                "sessionId"
            ]
        if label:
            with Registry() as reg:
                entry = reg.data.get(label, {}) if args.resume else {}
                entry.update(
                    sessionId=session_id,
                    cwd=str(cwd),
                    lastUsed=time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                    turns=entry.get("turns", 0) + 1,
                )
                entry.setdefault("created", entry["lastUsed"])
                reg.data[label] = entry
        print(
            f"[grok] session {session_id} ({'resumed' if args.resume else 'new'}); "
            f"events: {run_dir}/events.ndjson",
            file=sys.stderr,
            flush=True,
        )
        res = acp.request(
            "session/prompt",
            {"sessionId": session_id, "prompt": [{"type": "text", "text": prompt}]},
            deadline,
            turn.on_update,
        )
        stop_reason, result_meta = res.get("stopReason"), res.get("_meta")
        if stop_reason == "cancelled":
            code, err = EXIT_TIMEOUT, f"cancelled by {acp.cancel_reason or 'agent'}"
        elif stop_reason != "end_turn":
            code, err = EXIT_STOPPED, f"turn stopped: {stop_reason}"
    except ResumeError as e:
        code, err = EXIT_RESUME, f"resume failed: {e}"
    except Cancelled as e:
        code, err = EXIT_TIMEOUT, f"cancelled by signal during {e}; no prompt was sent"
    except TimeoutError as e:
        if acp.cancelling:
            err = f"{acp.cancel_reason} cancel not acknowledged in {CANCEL_GRACE}s"
        else:
            err = f"timed out in {e} (--timeout {args.timeout}s)"
        code = EXIT_TIMEOUT
    except AgentError as e:
        code, err = EXIT_AGENT, str(e)
    finally:
        acp.close()

    # Grok reports per-turn usage under the prompt result's _meta; the full object is in events.ndjson.
    turn_usage = (result_meta or {}).get("usage") or {}
    usage = {
        "modelId": (result_meta or {}).get("modelId"),
        **{
            k: turn_usage.get(k)
            for k in ("inputTokens", "outputTokens", "modelCalls", "costUsdTicks")
        },
    }
    summary, full_text = turn.summary()
    (run_dir / "response.md").write_text(full_text)
    out = {
        "ok": code == EXIT_OK,
        "error": err,
        "sessionId": session_id,
        "label": label,
        "resumed": bool(args.resume),
        "stopReason": stop_reason,
        **summary,
        "permissionRequestsAutoApproved": acp.permission_requests,
        "leftoverProcessesKilled": acp.reaped,
        "durationSec": round(time.monotonic() - started, 1),
        "runDir": str(run_dir),
        "usage": usage,
    }
    (run_dir / "result.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))
    return code


def fail(code, error, detail):
    print(json.dumps({"ok": False, "error": error, "detail": detail}, indent=1))
    return code


def cmd_sessions(args):
    with Registry() as reg:
        print(json.dumps(reg.data, indent=1, sort_keys=True))
    return EXIT_OK


def cmd_forget(args):
    with Registry() as reg:
        if reg.data.pop(args.label, None) is None:
            raise UsageError("unknown_label", args.label)
    print(json.dumps({"ok": True, "forgot": args.label}))
    return EXIT_OK


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    run = sub.add_parser("run", help="send one prompt to a new or resumed Grok session")
    run.add_argument(
        "--cwd", required=True, help="project root or item worktree Grok works in"
    )
    src = run.add_mutually_exclusive_group()
    src.add_argument("--prompt")
    src.add_argument("--prompt-file")
    run.add_argument(
        "--label", help="registry name for this session, e.g. DER-12:builder"
    )
    run.add_argument(
        "--resume", metavar="LABEL_OR_SESSION_ID", help="continue an existing session"
    )
    run.add_argument(
        "--replace",
        action="store_true",
        help="mint a new session under an existing label",
    )
    run.add_argument("--model")
    run.add_argument("--effort", choices=["low", "medium", "high", "xhigh"])
    run.add_argument("--rules-file", help="extra system-prompt rules for a new session")
    run.add_argument(
        "--timeout",
        type=int,
        default=3600,
        help="seconds for the whole run (default 3600)",
    )
    run.add_argument(
        "--out", help="run directory (default under ~/.local/state/grok-acp/runs)"
    )
    run.set_defaults(fn=cmd_run)

    ls = sub.add_parser("sessions", help="print the label registry")
    ls.set_defaults(fn=cmd_sessions)

    fg = sub.add_parser(
        "forget", help="drop a label from the registry (Grok keeps the session)"
    )
    fg.add_argument("label")
    fg.set_defaults(fn=cmd_forget)

    args = ap.parse_args()
    try:
        sys.exit(args.fn(args))
    except UsageError as e:
        sys.exit(fail(EXIT_USAGE, e.error, e.detail))
    except AgentError as e:
        sys.exit(fail(EXIT_AGENT, "agent_error", str(e)))


if __name__ == "__main__":
    main()
