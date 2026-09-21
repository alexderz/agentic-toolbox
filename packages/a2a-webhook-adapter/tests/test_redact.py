"""Redacting formatter never emits tokens."""

from __future__ import annotations

import logging

from a2a_webhook_adapter.redact import RedactingFormatter, redact_text
from tests.conftest import EXAMPLE_KEY


def test_redact_bearer_and_crsr() -> None:
    raw = f"Authorization: Bearer {EXAMPLE_KEY} extra"
    out = redact_text(raw)
    assert EXAMPLE_KEY not in out
    assert "Bearer [redacted]" in out


def test_formatter_redacts() -> None:
    record = logging.LogRecord(
        "a2a_webhook_adapter",
        logging.INFO,
        __file__,
        1,
        "got Bearer supersecretTOKEN1234567890abcdef",
        (),
        None,
    )
    formatted = RedactingFormatter("%(message)s").format(record)
    assert "supersecretTOKEN1234567890abcdef" not in formatted
