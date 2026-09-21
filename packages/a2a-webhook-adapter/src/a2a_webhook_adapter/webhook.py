"""HTTPS webhook allowlist and one-shot POST. Redirects are refused."""

from __future__ import annotations

import ipaddress
import json
import re
import urllib.error
import urllib.parse
import urllib.request

# Public Cursor Grok Bot webhook host (not a house endpoint).
ALLOWED_WEBHOOK_HOSTS = frozenset({"api2.cursor.sh"})
_WEBHOOK_PATH = re.compile(r"^/automations/webhook/[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
_TIMEOUT_S = 10


class WebhookURLError(ValueError):
    """Raised when WEBHOOK_URL fails the HTTPS allowlist."""


class RedirectRefused(urllib.error.HTTPError):
    """Raised when the webhook host issues a redirect."""


class _FailOnRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        raise RedirectRefused(
            req.full_url,
            code,
            "webhook redirects are refused",
            headers,
            fp,
        )


def _is_ip_literal(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False


def validate_webhook_url(url: str) -> urllib.parse.ParseResult:
    """Return the parsed URL if it is an allowed HTTPS webhook.

    Always: HTTPS, exact host on the allowlist, path
    ``/automations/webhook/<id>``, no userinfo, query, or fragment.
    Never: HTTP, localhost, IP literals, other hosts, redirects (checked
    at POST time).
    """
    raw = (url or "").strip()
    if not raw:
        raise WebhookURLError("WEBHOOK_URL is empty")
    parsed = urllib.parse.urlparse(raw)
    if parsed.scheme != "https":
        raise WebhookURLError("WEBHOOK_URL must be https")
    if parsed.username is not None or parsed.password is not None:
        raise WebhookURLError("WEBHOOK_URL must not include userinfo")
    if parsed.query or parsed.fragment:
        raise WebhookURLError("WEBHOOK_URL must not include query or fragment")
    if parsed.port not in (None, 443):
        raise WebhookURLError("WEBHOOK_URL must use port 443")
    host = (parsed.hostname or "").lower()
    if not host:
        raise WebhookURLError("WEBHOOK_URL host is missing")
    if host in {"localhost", "127.0.0.1", "::1"}:
        raise WebhookURLError("WEBHOOK_URL must not target localhost")
    if _is_ip_literal(host):
        raise WebhookURLError("WEBHOOK_URL must not be an IP literal")
    if host not in ALLOWED_WEBHOOK_HOSTS:
        raise WebhookURLError("WEBHOOK_URL host is not on the HTTPS allowlist")
    if _WEBHOOK_PATH.match(parsed.path) is None:
        raise WebhookURLError("WEBHOOK_URL path is not an allowed webhook path")
    return parsed


def post_webhook(
    url: str,
    key: str,
    body: dict[str, object],
    *,
    opener: urllib.request.OpenerDirector | None = None,
) -> tuple[int, bytes]:
    """POST JSON *body* to the allowlisted webhook. No redirects.

    Returns ``(status, response_body)``. Caller must not log *key* or
    *body* if they may contain secrets.
    """
    validate_webhook_url(url)
    data = json.dumps(body, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
            "User-Agent": "a2a-webhook-adapter/0.1",
        },
    )
    director = opener or urllib.request.build_opener(_FailOnRedirect())
    try:
        with director.open(request, timeout=_TIMEOUT_S) as response:
            payload = response.read()
            return int(getattr(response, "status", 200)), payload
    except RedirectRefused:
        raise
    except urllib.error.HTTPError as exc:
        if 300 <= int(exc.code) < 400:
            raise RedirectRefused(
                url,
                exc.code,
                "webhook redirects are refused",
                exc.headers,
                exc.fp,
            ) from exc
        err_body = b""
        if exc.fp is not None:
            err_body = exc.fp.read()
        return int(exc.code), err_body
