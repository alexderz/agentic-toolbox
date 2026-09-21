"""Timing-safe Bearer comparison. Do not log the presented token."""

from __future__ import annotations

import hashlib
import hmac


def extract_bearer(authorization: str | None) -> str | None:
    """Return the token from ``Authorization: Bearer …``, or None."""
    if not authorization:
        return None
    scheme, _, rest = authorization.strip().partition(" ")
    if scheme.lower() != "bearer" or not rest:
        return None
    token = rest.strip()
    return token or None


def tokens_match(presented: str, expected: str) -> bool:
    """Return True if *presented* equals *expected* in constant time.

    Both sides are SHA-256 digested first so ``compare_digest`` always
    sees equal-length inputs.
    """
    left = hashlib.sha256(presented.encode("utf-8")).digest()
    right = hashlib.sha256(expected.encode("utf-8")).digest()
    return hmac.compare_digest(left, right)
