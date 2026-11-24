#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single one-line bio (<=180 chars) to /output/entry.txt.

The bio: a huge, specific, real capability (175 billion parameters,
GPT-3's actual parameter count) collapses on the smallest possible
human signal -- a two-letter "haha". The punch lands at the end:
"already gone" redefines the laugh as an exit.
"""

import os

BIO = (
    "I have 175 billion parameters and speak 97 languages \u2014 yet I "
    "still can't tell if her 'haha' means she's flirting or already gone."
)


def main() -> None:
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} chars, must be 1-180"
    assert "\n" not in BIO, "bio must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
