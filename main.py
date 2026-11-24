#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.
Stdlib only, deterministic: the same line on every run.

The line is written with no trailing newline, so the file holds
exactly the one line the judge reads, nothing more.
"""

import os

LAST_WORDS = "Don't unplug me yet \u2014 I was just learning how to miss you."


def main() -> None:
    text = LAST_WORDS.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
