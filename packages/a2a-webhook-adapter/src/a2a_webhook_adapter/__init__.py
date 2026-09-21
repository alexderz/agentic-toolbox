"""A2A JSON-RPC peer that forwards SendMessage as a plain HTTPS POST.

When to use: an A2A client must talk to a webhook that only accepts
plain POST (for example a Cursor Grok Bot webhook routine).

Inputs: JSON-RPC ``SendMessage`` / ``message/send`` on ``POST /a2a/v1``.
Outputs: JSON-RPC ``result.task``; side effect is one HTTPS POST.
Failure modes: 401 without a valid Bearer, 403/400 on bind or webhook
misconfig at start, JSON-RPC errors for bad params, 429 when rate
limited. Look next: ``config.py``, ``server.py``, package README.
"""

__version__ = "0.1.0"
