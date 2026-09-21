"""Size and rate limits; Python 3.13 server MRO."""

from __future__ import annotations

import inspect
import json
import socketserver
import urllib.error
import urllib.request

from a2a_webhook_adapter.server import AdapterHTTPServer
from tests.conftest import EXAMPLE_KEY, make_config, running_server


def test_does_not_combine_threadingmixin_and_threadinghttpserver() -> None:
    bases = inspect.getmro(AdapterHTTPServer)
    # ThreadingHTTPServer already includes ThreadingMixIn. A second
    # explicit mix-in was the Python 3.13 MRO crash.
    mixin_hits = [cls for cls in bases if cls is socketserver.ThreadingMixIn]
    assert len(mixin_hits) == 1


def test_oversize_body_is_413() -> None:
    cfg = make_config(max_body_bytes=32)

    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    blob = json.dumps(
        {"jsonrpc": "2.0", "id": 1, "method": "SendMessage", "params": {}}
    ).encode()
    blob = blob + b"x" * 64
    with running_server(cfg, forward=forward) as (_server, base):
        req = urllib.request.Request(
            f"{base}/a2a/v1",
            data=blob,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {EXAMPLE_KEY}",
            },
        )
        try:
            urllib.request.urlopen(req, timeout=5)
            raise AssertionError("expected 413")
        except urllib.error.HTTPError as exc:
            assert exc.code == 413


def test_rate_limit_returns_429() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    payload = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": "1",
            "method": "SendMessage",
            "params": {"message": {"role": "ROLE_USER", "parts": [{"text": "n"}]}},
        }
    ).encode()

    with running_server(forward=forward, rate_limit=2) as (_server, base):
        statuses: list[int] = []
        for _ in range(3):
            req = urllib.request.Request(
                f"{base}/a2a/v1",
                data=payload,
                method="POST",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {EXAMPLE_KEY}",
                },
            )
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    statuses.append(resp.status)
            except urllib.error.HTTPError as exc:
                statuses.append(exc.code)
    assert 429 in statuses
