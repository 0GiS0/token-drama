#!/usr/bin/env python3
"""
UserPromptSubmit hook: counts tokens in the user prompt and appends to a CSV log.

Token counting strategy:
  1. Try tiktoken (OpenAI tokenizer) for cl100k_base encoding (GPT-4 / Copilot-compatible).
  2. Fall back to character-based approximation (~4 chars per token).
"""

import csv
import json
import sys
import os
import math
from datetime import datetime, timezone

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "token-usage.csv")
LOG_FILE = os.path.abspath(LOG_FILE)

CSV_HEADERS = ["timestamp", "session_id", "tokens", "method", "chars", "cwd", "prompt"]


def count_tokens(text: str) -> tuple[int, str]:
    """Return (token_count, method_used)."""
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text)), "tiktoken/cl100k_base"
    except ImportError:
        pass
    # Fallback: ~4 chars per token (rough but safe approximation)
    approx = math.ceil(len(text) / 4)
    return approx, "approx(len/4)"


def main() -> None:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Cannot parse input; exit silently (non-blocking)
        sys.exit(0)

    prompt: str = data.get("prompt", "")
    session_id: str = data.get("session_id", data.get("sessionId", "unknown"))
    timestamp: str = data.get("timestamp", datetime.now(timezone.utc).isoformat())
    cwd: str = data.get("cwd", "")

    if not prompt:
        sys.exit(0)

    token_count, method = count_tokens(prompt)

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    write_header = not os.path.exists(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_HEADERS)
        writer.writerow([timestamp, session_id, token_count, method, len(prompt), cwd, prompt])

    # Non-blocking: let the agent continue normally
    sys.exit(0)


if __name__ == "__main__":
    main()
