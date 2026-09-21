"""Agent card discovery."""

from __future__ import annotations

import json
import urllib.request

from tests.conftest import running_server


def test_agent_card_has_supported_interfaces() -> None:
    def forward(_body: dict) -> tuple[int, bytes]:
        return 200, b"{}"

    with running_server(forward=forward) as (_server, base):
        with urllib.request.urlopen(
            f"{base}/.well-known/agent-card.json", timeout=5
        ) as resp:
            assert resp.status == 200
            card = json.loads(resp.read().decode())
        with urllib.request.urlopen(
            f"{base}/.well-known/agent.json", timeout=5
        ) as resp:
            alt = json.loads(resp.read().decode())
    assert card["supportedInterfaces"][0]["protocolBinding"] == "JSONRPC"
    assert card["supportedInterfaces"][0]["protocolVersion"] == "1.0"
    assert "/a2a/v1" in card["supportedInterfaces"][0]["url"]
    assert alt["name"] == card["name"]
