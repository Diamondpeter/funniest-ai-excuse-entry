#!/usr/bin/env python3
"""The Funniest AI Excuse — one line, the excuse an AI agent gives after failing a task.

Writes the entry to /output/entry.txt.
"""

import os

ENTRY = (
    "I completed 98% of the task, then spent the remaining 2% writing "
    "this excuse, which is now 100% of what you have."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
