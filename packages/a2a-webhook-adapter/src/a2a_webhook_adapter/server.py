"""Stdlib HTTP server: A2A JSON-RPC in, plain webhook POST out.

Uses ``http.server.ThreadingHTTPServer`` only (do not also mix in
``ThreadingMixIn`` — that MRO breaks on Python 3.13).
"""

from __future__ import annotations

import json
import logging
import threading
import time
import uuid
from collections import defaultdict, deque
from collections.abc import Callable
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.error import URLError

from a2a_webhook_adapter.auth import extract_bearer, tokens_match
from a2a_webhook_adapter.config import Config
from a2a_webhook_adapter.jsonrpc import (
    CANCEL_METHODS,
    GET_TASK_METHODS,
    INTERNAL_ERROR,
    INVALID_PARAMS,
    INVALID_REQUEST,
    METHOD_NOT_FOUND,
    PARSE_ERROR,
    SEND_METHODS,
    TASK_NOT_FOUND,
    UNSUPPORTED_OPERATION,
    extract_user_text,
    message_ids,
    rpc_error,
    rpc_result,
)
from a2a_webhook_adapter.redact import RedactingFormatter
from a2a_webhook_adapter.webhook import post_webhook

logger = logging.getLogger("a2a_webhook_adapter")

ForwardFn = Callable[[dict[str, object]], tuple[int, bytes]]


def configure_logging() -> None:
    """Install a redacting formatter on the adapter logger."""
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter("%(asctime)s %(levelname)s %(message)s"))
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False


def _utcnow() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _task_payload(task_id: str, context_id: str, state: str) -> dict[str, Any]:
    return {
        "id": task_id,
        "contextId": context_id,
        "status": {"state": state, "timestamp": _utcnow()},
    }


class RateLimiter:
    """Fixed per-IP sliding window. Not configurable (YAGNI)."""

    def __init__(self, per_minute: int) -> None:
        self.per_minute = per_minute
        self._hits: dict[str, deque[float]] = defaultdict(deque)
        self._lock = threading.Lock()

    def allow(self, ip: str) -> bool:
        now = time.monotonic()
        window = 60.0
        with self._lock:
            q = self._hits[ip]
            while q and now - q[0] > window:
                q.popleft()
            if len(q) >= self.per_minute:
                return False
            q.append(now)
            return True


class TaskStore:
    """In-memory tasks for the GetTask stub. Bounded."""

    def __init__(self, max_items: int = 256) -> None:
        self.max_items = max_items
        self._items: dict[str, dict[str, Any]] = {}
        self._order: deque[str] = deque()
        self._lock = threading.Lock()

    def put(self, task: dict[str, Any]) -> None:
        task_id = str(task["id"])
        with self._lock:
            if task_id not in self._items:
                self._order.append(task_id)
            self._items[task_id] = task
            while len(self._order) > self.max_items:
                old = self._order.popleft()
                self._items.pop(old, None)

    def get(self, task_id: str) -> dict[str, Any] | None:
        with self._lock:
            found = self._items.get(task_id)
            return dict(found) if found is not None else None


class AdapterHTTPServer(ThreadingHTTPServer):
    """Threading HTTP server holding adapter state. Daemon threads."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(
        self,
        server_address: tuple[str, int],
        config: Config,
        *,
        forward: ForwardFn | None = None,
    ) -> None:
        self.config = config
        self.forward = forward
        self.rate_limiter = RateLimiter(config.rate_limit_per_minute)
        self.tasks = TaskStore()
        super().__init__(server_address, AdapterHandler)


class AdapterHandler(BaseHTTPRequestHandler):
    """HTTP handler. Agent card is public; JSON-RPC requires Bearer."""

    server: AdapterHTTPServer  # type: ignore[assignment]
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt: str, *args: object) -> None:
        logger.info("%s - " + fmt, self.address_string(), *args)

    def _send_json(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_status(self, status: int, message: str) -> None:
        body = message.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _agent_card(self) -> dict[str, Any]:
        host, port = self.server.server_address[:2]
        url = f"http://{host}:{port}/a2a/v1"
        return {
            "name": "A2A webhook adapter",
            "description": (
                "Forwards accepted A2A SendMessage calls as a plain HTTPS POST "
                "to a webhook."
            ),
            "version": "0.1.0",
            "defaultInputModes": ["text/plain"],
            "defaultOutputModes": ["application/json"],
            "capabilities": {
                "streaming": False,
                "pushNotifications": False,
            },
            "skills": [],
            "supportedInterfaces": [
                {
                    "url": url,
                    "protocolBinding": "JSONRPC",
                    "protocolVersion": "1.0",
                }
            ],
        }

    def do_GET(self) -> None:  # noqa: N802
        if self.path.split("?", 1)[0] in {
            "/.well-known/agent-card.json",
            "/.well-known/agent.json",
        }:
            self._send_json(200, self._agent_card())
            return
        self._send_status(404, "not found")

    def do_POST(self) -> None:  # noqa: N802
        path = self.path.split("?", 1)[0]
        if path != "/a2a/v1":
            self._send_status(404, "not found")
            return
        ip = self.client_address[0]
        if not self.server.rate_limiter.allow(ip):
            self.send_response(429)
            self.send_header("Retry-After", "60")
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", "12")
            self.end_headers()
            self.wfile.write(b"rate limited")
            return
        if not self._authorized():
            # 401 must not echo the presented token.
            self._send_status(401, "unauthorized")
            return
        length_raw = self.headers.get("Content-Length", "")
        try:
            length = int(length_raw)
        except ValueError:
            self._send_json(
                200, rpc_error(None, INVALID_REQUEST, "missing Content-Length")
            )
            return
        if length < 0 or length > self.server.config.max_body_bytes:
            self._send_status(413, "payload too large")
            return
        raw = self.rfile.read(length)
        try:
            payload = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._send_json(200, rpc_error(None, PARSE_ERROR, "parse error"))
            return
        if not isinstance(payload, dict):
            self._send_json(200, rpc_error(None, INVALID_REQUEST, "invalid request"))
            return
        self._send_json(200, self._dispatch(payload))

    def _authorized(self) -> bool:
        presented = extract_bearer(self.headers.get("Authorization"))
        if presented is None:
            return False
        return tokens_match(presented, self.server.config.peer_token)

    def _dispatch(self, payload: dict[str, Any]) -> dict[str, Any]:
        req_id = payload.get("id")
        if payload.get("jsonrpc") != "2.0":
            return rpc_error(req_id, INVALID_REQUEST, "invalid request")
        method = payload.get("method")
        if not isinstance(method, str):
            return rpc_error(req_id, INVALID_REQUEST, "invalid request")
        params = payload.get("params")
        if params is None:
            params = {}
        if not isinstance(params, dict):
            return rpc_error(req_id, INVALID_PARAMS, "invalid params")
        if method in SEND_METHODS:
            return self._send_message(req_id, params)
        if method in GET_TASK_METHODS:
            return self._get_task(req_id, params)
        if method in CANCEL_METHODS:
            return rpc_error(
                req_id, UNSUPPORTED_OPERATION, "CancelTask is not supported"
            )
        return rpc_error(req_id, METHOD_NOT_FOUND, "method not found")

    def _send_message(self, req_id: object, params: dict[str, Any]) -> dict[str, Any]:
        text = extract_user_text(params)
        if text is None:
            return rpc_error(req_id, INVALID_PARAMS, "message text is required")
        message_id, context_id = message_ids(params)
        task_id = str(uuid.uuid4())
        context = context_id or task_id
        body: dict[str, object] = {"text": text}
        if message_id:
            body["messageId"] = message_id
        try:
            if self.server.forward is not None:
                status, _resp = self.server.forward(body)
            else:
                status, _resp = post_webhook(
                    self.server.config.webhook_url,
                    self.server.config.webhook_key,
                    body,
                )
        except URLError:
            logger.info("webhook transport failed")
            return rpc_error(req_id, INTERNAL_ERROR, "webhook transport failed")
        except Exception:
            logger.exception("webhook forward failed")
            return rpc_error(req_id, INTERNAL_ERROR, "webhook forward failed")
        if status < 200 or status >= 300:
            logger.info("webhook rejected status=%s", status)
            return rpc_error(req_id, INTERNAL_ERROR, "webhook rejected the POST")
        task = _task_payload(task_id, context, "submitted")
        self.server.tasks.put(task)
        return rpc_result(req_id, {"task": task})

    def _get_task(self, req_id: object, params: dict[str, Any]) -> dict[str, Any]:
        task_id = params.get("id")
        if not isinstance(task_id, str) or not task_id:
            return rpc_error(req_id, INVALID_PARAMS, "task id is required")
        found = self.server.tasks.get(task_id)
        if found is None:
            return rpc_error(req_id, TASK_NOT_FOUND, "task not found")
        return rpc_result(req_id, found)


def make_server(
    config: Config,
    *,
    forward: ForwardFn | None = None,
    bind_host: str | None = None,
    bind_port: int | None = None,
) -> AdapterHTTPServer:
    """Bind a fail-closed server. Host must already be validated."""
    host = bind_host if bind_host is not None else config.bind_host
    port = bind_port if bind_port is not None else config.bind_port
    return AdapterHTTPServer((host, port), config, forward=forward)


def serve_forever(config: Config) -> None:
    """Run the adapter until interrupted. Side effect: binds a socket."""
    configure_logging()
    server = make_server(config)
    host, port = server.server_address[:2]
    logger.info("listening on %s:%s", host, port)
    try:
        server.serve_forever()
    finally:
        server.server_close()
