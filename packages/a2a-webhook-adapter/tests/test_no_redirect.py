"""Webhook POST refuses redirects."""

from __future__ import annotations

import urllib.error
import urllib.request
from email.message import Message

import pytest

from a2a_webhook_adapter.webhook import RedirectRefused, post_webhook
from tests.conftest import EXAMPLE_KEY, EXAMPLE_WEBHOOK


def test_http_error_redirect_is_refused() -> None:
    class Opener(urllib.request.OpenerDirector):
        def open(self, request, timeout=None):  # noqa: ANN001
            raise urllib.error.HTTPError(
                EXAMPLE_WEBHOOK,
                302,
                "Found",
                Message(),
                None,
            )

    with pytest.raises(RedirectRefused):
        post_webhook(EXAMPLE_WEBHOOK, EXAMPLE_KEY, {"text": "n"}, opener=Opener())
