"""Fail-closed listen-address policy: loopback or private unicast only."""

from __future__ import annotations

import ipaddress

_REFUSED = frozenset(
    {
        "0.0.0.0",
        "::",
        "[::]",
        "*",
        "::0",
        "0:0:0:0:0:0:0:0",
    }
)


class BindError(ValueError):
    """Raised when the configured listen host is not allowed."""


def validate_bind_host(host: str) -> str:
    """Return a stripped host if it is loopback or private; else raise.

    Refuses unspecified addresses (``0.0.0.0``, ``::``) so the process
    never becomes a public client. Hostnames other than ``localhost``
    are refused (no DNS surprise).
    """
    candidate = (host or "").strip()
    if not candidate:
        raise BindError("bind host is empty")
    if candidate in _REFUSED:
        raise BindError(f"refusing public or unspecified bind {candidate!r}")
    if candidate.lower() == "localhost":
        return "127.0.0.1"
    try:
        ip = ipaddress.ip_address(candidate)
    except ValueError as exc:
        raise BindError(
            f"bind host must be an IP or localhost, not {candidate!r}"
        ) from exc
    if ip.is_unspecified or ip.is_multicast:
        raise BindError(f"refusing bind {candidate!r}")
    if ip.is_loopback or ip.is_private:
        return candidate
    raise BindError(f"refusing non-private bind {candidate!r}")
