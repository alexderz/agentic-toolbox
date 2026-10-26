#!/usr/bin/env python3
"""Serve a recorded Home Assistant fixture.

Replaces the live read-only proxy for evals. Same contract -- GET/HEAD only,
bearer token required -- but every response comes from the recording, so:

  * the run is byte-for-byte reproducible, forever
  * there is no rate limit to work around and no load on a real installation
  * anyone can run the suite without owning the target system

Rate limiting is off by default here. Set RATE_PER_SEC to re-enable it if the
suite is specifically testing whether generated clients handle 429.
"""
import http.server
import json
import os
import socketserver
import sys
import threading
import time
from collections import defaultdict, deque
from urllib.parse import urlsplit

FIXTURE = os.environ.get("FIXTURE", "fixtures/ha-fixture.json")
LISTEN_HOST = os.environ.get("PROXY_HOST", "127.0.0.1")
LISTEN_PORT = int(os.environ.get("PROXY_PORT", "8126"))
CLIENT_TOKEN = os.environ.get("CLIENT_TOKEN", "eval-placeholder-token")
LOG_PATH = os.environ.get("PROXY_LOG", "/tmp/ha-replay-access.log")
RATE_PER_SEC = float(os.environ.get("RATE_PER_SEC", "0"))  # 0 = unlimited
BURST = int(os.environ.get("BURST", "20"))

ALLOWED_METHODS = {"GET", "HEAD"}
BLOCKED_PREFIXES = ("/api/services/", "/api/events/")

try:
    with open(FIXTURE) as fh:
        FX = json.load(fh)
except OSError as e:
    sys.exit(f"cannot read fixture {FIXTURE}: {e}")

RESP = FX.get("responses", {})
FP = FX.get("fingerprint", {})
if not RESP:
    sys.exit(f"fixture {FIXTURE} has no responses")

_hits = defaultdict(deque)
_lock = threading.Lock()


def allow(client):
    if RATE_PER_SEC <= 0:
        return True
    now = time.time()
    window = BURST / RATE_PER_SEC
    with _lock:
        q = _hits[client]
        while q and now - q[0] > window:
            q.popleft()
        if len(q) >= BURST:
            return False
        q.append(now)
        return True


def log(client, method, path, status, note=""):
    try:
        with open(LOG_PATH, "a") as fh:
            fh.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                 "client": client, "method": method, "path": path,
                                 "status": status, "note": note}) + "\n")
    except OSError:
        pass


def lookup(path):
    """Exact match, then ignoring the query string, then a 404 that says so."""
    if path in RESP:
        return RESP[path], "exact"
    bare = urlsplit(path).path
    if bare in RESP:
        return RESP[bare], "query-stripped"
    # tolerate a missing or extra trailing slash
    alt = bare.rstrip("/") if bare.endswith("/") else bare + "/"
    if alt in RESP:
        return RESP[alt], "slash-normalised"
    return None, "not-recorded"


class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "ha-replay"

    def _send(self, code, body, ctype="application/json", note=""):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)
        log(self.client_address[0], self.command, self.path, code, note)

    def _serve(self):
        # Order matters. Checking the method FIRST makes every non-GET return
        # 405, including for paths that do not exist -- and models read 405 as
        # "this endpoint exists but needs another method". Ternary Bonsai built
        # a whole phantom API map that way, spending turns on endpoints that
        # were never real. Resolve the path first so a bogus path 404s for any
        # method, and 405 only ever means "real path, wrong method".
        if self.headers.get("Authorization", "") != f"Bearer {CLIENT_TOKEN}":
            return self._send(401, json.dumps({"error": "401: Unauthorized"}),
                              note="bad or missing token")

        if not self.path.startswith("/api"):
            return self._send(404, json.dumps({"error": "only /api paths are served"}),
                              note="non-api path")

        rec, how = lookup(self.path)
        is_write_shaped = any(self.path.startswith(p) for p in BLOCKED_PREFIXES)

        if rec is None and not is_write_shaped:
            return self._send(404, json.dumps(
                {"error": "not in the recorded fixture",
                 "hint": "this eval replays a recording; only recorded paths exist"}),
                note=f"{how} ({self.command})")

        if is_write_shaped:
            return self._send(403, json.dumps(
                {"error": "this endpoint can change state and is blocked; "
                          "GET /api/services lists services without calling them"}),
                note="write-shaped path blocked")

        if self.command not in ALLOWED_METHODS:
            return self._send(405, json.dumps(
                {"error": f"{self.command} is not permitted: this endpoint is read-only"}),
                note="method blocked on a real path")

        if not allow(self.client_address[0]):
            return self._send(429, json.dumps(
                {"error": f"slow down: limit is {RATE_PER_SEC}/s"}), note="rate limited")

        if rec is None:
            return self._send(404, json.dumps(
                {"error": "not in the recorded fixture",
                 "hint": "this eval replays a recording; only recorded paths exist"}),
                note=how)
        self._send(rec["status"], rec["body"],
                   rec.get("content_type", "application/json"), note=how)

    do_GET = _serve
    do_HEAD = _serve
    do_POST = _serve
    do_PUT = _serve
    do_DELETE = _serve
    do_PATCH = _serve

    def log_message(self, *a):
        pass


class Threaded(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    srv = Threaded((LISTEN_HOST, LISTEN_PORT), Handler)
    print(f"ha-replay on {LISTEN_HOST}:{LISTEN_PORT} from {FIXTURE} "
          f"({FP.get('paths_recorded')} paths, {FP.get('entity_count')} entities, "
          f"recorded {FX.get('recorded_at')}, "
          f"rate {'unlimited' if RATE_PER_SEC <= 0 else str(RATE_PER_SEC) + '/s'})",
          flush=True)
    srv.serve_forever()
