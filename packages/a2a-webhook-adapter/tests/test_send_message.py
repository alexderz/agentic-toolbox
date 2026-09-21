"""SendMessage golden path: ROLE_USER, bare {text}, result.task."""

from __future__ import annotations

import json
import urllib.request

from a2a_webhook_adapter.jsonrpc import extract_user_text
from tests.conftest import EXAMPLE_KEY, FIXTURES, running_server


def _rpc(base: str, payload: dict) -> dict:
    data = json.dumps(payload).encode()
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
        return json.loads(resp.read().decode())


def test_golden_send_message_returns_result_task() -> None:
    raw = (FIXTURES / "golden_send_message.json").read_text(encoding="utf-8")
    payload = json.loads(raw)
    captured: list[dict] = []

    def forward(body: dict) -> tuple[int, bytes]:
        captured.append(body)
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        result = _rpc(base, payload)
    assert result["id"] == "req-1"
    assert "task" in result["result"]
    assert result["result"]["task"]["id"]
    assert captured == [{"text": "hello from peer", "messageId": "m1"}]


def test_ok_true_is_not_a_send_result() -> None:
    """OpenClaw-style clients reject a bare {ok: true} envelope."""
    payload = json.loads(
        (FIXTURES / "golden_send_message.json").read_text(encoding="utf-8")
    )

    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        result = _rpc(base, payload)
    assert result.get("result") != {"ok": True}
    assert "task" in result["result"]


def test_message_send_alias() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    payload = {
        "jsonrpc": "2.0",
        "id": 7,
        "method": "message/send",
        "params": {
            "message": {"role": "user", "parts": [{"kind": "text", "text": "alias"}]}
        },
    }
    with running_server(forward=forward) as (_server, base):
        result = _rpc(base, payload)
    assert "task" in result["result"]
    assert result["id"] == 7


def test_cancel_task_is_unsupported() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        raise AssertionError("must not forward")

    payload = {
        "jsonrpc": "2.0",
        "id": "c1",
        "method": "CancelTask",
        "params": {"id": "task-1"},
    }
    with running_server(forward=forward) as (_server, base):
        result = _rpc(base, payload)
    assert result["error"]["code"] == -32004


def test_get_task_stub_after_send() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    send = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "SendMessage",
        "params": {"message": {"role": "ROLE_USER", "parts": [{"text": "n"}]}},
    }
    with running_server(forward=forward) as (_server, base):
        created = _rpc(base, send)
        task_id = created["result"]["task"]["id"]
        got = _rpc(
            base,
            {
                "jsonrpc": "2.0",
                "id": "2",
                "method": "GetTask",
                "params": {"id": task_id},
            },
        )
        missing = _rpc(
            base,
            {
                "jsonrpc": "2.0",
                "id": "3",
                "method": "GetTask",
                "params": {"id": "does-not-exist"},
            },
        )
    assert got["result"]["id"] == task_id
    assert missing["error"]["code"] == -32001


def test_extract_requires_text() -> None:
    assert extract_user_text({"message": {"role": "ROLE_USER", "parts": []}}) is None
    assert (
        extract_user_text(
            {"message": {"role": "ROLE_AGENT", "parts": [{"text": "nope"}]}}
        )
        is None
    )


def test_unknown_method() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        result = _rpc(
            base,
            {"jsonrpc": "2.0", "id": "x", "method": "Nope", "params": {}},
        )
    assert result["error"]["code"] == -32601


def test_webhook_failure_is_internal_error() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 500, b"nope"

    payload = json.loads(
        (FIXTURES / "golden_send_message.json").read_text(encoding="utf-8")
    )
    with running_server(forward=forward) as (_server, base):
        result = _rpc(base, payload)
    assert result["error"]["code"] == -32603
