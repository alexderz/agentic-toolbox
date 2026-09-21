"""Timing-safe Bearer matching; 401 bodies must not echo the token."""

from __future__ import annotations

import json
import urllib.error
import urllib.request

from a2a_webhook_adapter.auth import extract_bearer, tokens_match
from tests.conftest import EXAMPLE_KEY, running_server


def test_extract_bearer() -> None:
    assert extract_bearer("Bearer abc") == "abc"
    assert extract_bearer("bearer abc") == "abc"
    assert extract_bearer("Basic abc") is None
    assert extract_bearer(None) is None


def test_tokens_match_accepts_equal() -> None:
    assert tokens_match("secret", "secret") is True
    assert tokens_match("secret", "other") is False


def test_no_auth_is_401_without_token_text() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        req = urllib.request.Request(
            f"{base}/a2a/v1",
            data=b"{}",
            method="POST",
            headers={"Content-Type": "application/json", "Content-Length": "2"},
        )
        try:
            urllib.request.urlopen(req, timeout=5)
            raise AssertionError("expected 401")
        except urllib.error.HTTPError as exc:
            assert exc.code == 401
            body = exc.read().decode("utf-8")
            assert EXAMPLE_KEY not in body
            assert "crsr_" not in body


def test_wrong_token_is_401() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        req = urllib.request.Request(
            f"{base}/a2a/v1",
            data=b"{}",
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer definitely-wrong-token",
            },
        )
        try:
            urllib.request.urlopen(req, timeout=5)
            raise AssertionError("expected 401")
        except urllib.error.HTTPError as exc:
            assert exc.code == 401
            body = exc.read().decode("utf-8")
            assert "definitely-wrong-token" not in body


def test_matching_token_reaches_handler() -> None:
    captured: list[dict] = []

    def forward(body: dict) -> tuple[int, bytes]:
        captured.append(body)
        return 200, b"{}"

    payload = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "SendMessage",
        "params": {
            "message": {
                "messageId": "m1",
                "role": "ROLE_USER",
                "parts": [{"text": "hi"}],
            }
        },
    }
    data = json.dumps(payload).encode()
    with running_server(forward=forward) as (_server, base):
        req = urllib.request.Request(
            f"{base}/a2a/v1",
            data=data,
            method="POST",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {EXAMPLE_KEY}",
            },
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            assert resp.status == 200
            result = json.loads(resp.read().decode())
        assert "task" in result["result"]
        assert captured[0]["text"] == "hi"
