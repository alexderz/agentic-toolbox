"""Log redaction. Never write tokens, Bearer values, or webhook keys."""

from __future__ import annotations

import logging
import re

_BEARER = re.compile(r"(Bearer\s+)(\S+)", re.IGNORECASE)
_QUERY_SECRET = re.compile(
    r"((?:token|key|secret|password|authorization)=)([^&\s]+)",
    re.IGNORECASE,
)
_CRSR = re.compile(r"\bcrsr_[A-Za-z0-9._\-]+")
_LONG_HEX = re.compile(r"\b[A-Fa-f0-9]{32,}\b")


def redact_text(text: str) -> str:
    """Return *text* with credentials replaced by ``[redacted]``."""
    out = _BEARER.sub(r"\1[redacted]", text)
    out = _QUERY_SECRET.sub(r"\1[redacted]", out)
    out = _CRSR.sub("[redacted]", out)
    out = _LONG_HEX.sub("[redacted]", out)
    return out


class RedactingFormatter(logging.Formatter):
    """Formatter that redacts secrets in the rendered log line."""

    def format(self, record: logging.LogRecord) -> str:
        rendered = super().format(record)
        return redact_text(rendered)
