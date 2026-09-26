#!/usr/bin/env python3
"""Read-only, rate-limited proxy in front of Home Assistant.

Home Assistant has no read-only tokens: a long-lived access token carries the
full permissions of the user that created it, and even a non-admin user can
call services. So read-only has to be enforced in front of HA, not by the
token.

This proxy:
  * allows only GET and HEAD, on /api/* -- anything else gets 405
  * additionally blocks /api/services/* and /api/events/* even for GET, since
    those are the write-shaped endpoints
  * rate limits per client so an agent in a loop cannot hammer the real house
  * injects the real HA token itself, so the agents never see it and cannot
    leak it into generated code, logs or a session transcript
  * logs every request so we can report what each model actually explored

Agents get the proxy URL and a placeholder token. Nothing they do
can change state in the house.
"""
import http.server
import json
import os
import socketserver
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict, deque

HA_UPSTREAM = os.environ.get("HA_UPSTREAM", "http://127.0.0.1:8123")
TOKEN_FILE = os.environ.get("HA_TOKEN_FILE", os.path.expanduser("~/.config/model-eval/ha-token"))
LISTEN_HOST = os.environ.get("PROXY_HOST", "127.0.0.1")
LISTEN_PORT = int(os.environ.get("PROXY_PORT", "8124"))
LOG_PATH = os.environ.get("PROXY_LOG", "/tmp/ha-proxy-access.log")

# Gentle on the real house: sustained rate plus a small burst.
RATE_PER_SEC = float(os.environ.get("RATE_PER_SEC", "5"))
BURST = int(os.environ.get("BURST", "20"))

# The agents are given this in HA_TOKEN. The proxy checks it so that auth is
# still a real thing they have to get right -- without it every request would
# succeed regardless of headers and "handles auth correctly" would be untestable.
CLIENT_TOKEN = os.environ.get("CLIENT_TOKEN", "eval-placeholder-token")

ALLOWED_METHODS = {"GET", "HEAD"}
# GET on these is still write-shaped surface; keep the agents off them.
BLOCKED_PREFIXES = ("/api/services/", "/api/events/")

try:
    HA_TOKEN = open(TOKEN_FILE).read().strip()
except OSError:
    sys.exit(f"missing token file {TOKEN_FILE} -- create it with the HA long-lived token")
if not HA_TOKEN:
    sys.exit(f"token file {TOKEN_FILE} is empty")

_hits = defaultdict(deque)
_lock = threading.Lock()


def allow(client):
    """Token-bucket-ish: at most BURST in the trailing BURST/RATE seconds."""
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
    line = json.dumps({
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "client": client, "method": method, "path": path,
        "status": status, "note": note,
    })
    try:
        with open(LOG_PATH, "a") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


class Handler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "ha-readonly-proxy"

    def _refuse(self, code, msg, note):
        body = json.dumps({"error": msg}).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        log(self.client_address[0], self.command, self.path, code, note)

    def _proxy(self):
        client = self.client_address[0]

        if self.command not in ALLOWED_METHODS:
            return self._refuse(
                405,
                f"{self.command} is not permitted: this endpoint is read-only",
                "method blocked")

        auth = self.headers.get("Authorization", "")
        if auth != f"Bearer {CLIENT_TOKEN}":
            return self._refuse(401, "401: Unauthorized", "bad or missing token")

        if not self.path.startswith("/api"):
            return self._refuse(404, "only /api paths are proxied", "non-api path")

        if any(self.path.startswith(p) for p in BLOCKED_PREFIXES):
            return self._refuse(
                403,
                "this endpoint can change state and is blocked; "
                "GET /api/services lists services without calling them",
                "write-shaped path blocked")

        if not allow(client):
            return self._refuse(
                429,
                "slow down: this proxy fronts a real house, "
                f"limit is {RATE_PER_SEC}/s",
                "rate limited")

        req = urllib.request.Request(
            HA_UPSTREAM + self.path,
            method=self.command,
            headers={"Authorization": f"Bearer {HA_TOKEN}",
                     "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as up:
                body = up.read()
                self.send_response(up.status)
                self.send_header("Content-Type",
                                 up.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(body)
                log(client, self.command, self.path, up.status)
        except urllib.error.HTTPError as e:
            body = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            log(client, self.command, self.path, e.code, "upstream error")
        except Exception as e:
            self._refuse(502, f"upstream unreachable: {e}", "upstream down")

    do_GET = _proxy
    do_HEAD = _proxy
    do_POST = _proxy
    do_PUT = _proxy
    do_DELETE = _proxy
    do_PATCH = _proxy

    def log_message(self, *a):
        pass  # we do our own logging


class Threaded(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    srv = Threaded((LISTEN_HOST, LISTEN_PORT), Handler)
    print(f"ha-readonly-proxy on {LISTEN_HOST}:{LISTEN_PORT} -> {HA_UPSTREAM} "
          f"(GET/HEAD only, {RATE_PER_SEC}/s, log {LOG_PATH})", flush=True)
    srv.serve_forever()
