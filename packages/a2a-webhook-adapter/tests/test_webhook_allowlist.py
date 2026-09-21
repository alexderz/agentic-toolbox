"""HTTPS webhook allowlist."""

from __future__ import annotations

import pytest

from a2a_webhook_adapter.webhook import WebhookURLError, validate_webhook_url

GOOD = "https://api2.cursor.sh/automations/webhook/exampleRoutine1"


def test_accepts_cursor_webhook_path() -> None:
    parsed = validate_webhook_url(GOOD)
    assert parsed.hostname == "api2.cursor.sh"


@pytest.mark.parametrize(
    "url",
    [
        "http://api2.cursor.sh/automations/webhook/exampleRoutine1",
        "https://127.0.0.1/automations/webhook/exampleRoutine1",
        "https://localhost/automations/webhook/exampleRoutine1",
        "https://8.8.8.8/automations/webhook/exampleRoutine1",
        "https://example.com/automations/webhook/exampleRoutine1",
        "https://evil.api2.cursor.sh/automations/webhook/exampleRoutine1",
        "https://api2.cursor.sh.evil.example/automations/webhook/exampleRoutine1",
        "https://user:pass@api2.cursor.sh/automations/webhook/exampleRoutine1",
        "https://api2.cursor.sh/automations/webhook/exampleRoutine1?x=1",
        "https://api2.cursor.sh/automations/webhook/exampleRoutine1#frag",
        "https://api2.cursor.sh/other/exampleRoutine1",
        "https://api2.cursor.sh/automations/webhook/../escape",
        "https://api2.cursor.sh:8443/automations/webhook/exampleRoutine1",
        "",
    ],
)
def test_rejects_non_allowlisted_urls(url: str) -> None:
    with pytest.raises(WebhookURLError):
        validate_webhook_url(url)
