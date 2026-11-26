#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes a single funny one-liner to /output/entry.txt.
Deterministic, no network, no dependencies, Python 3.13 stdlib only.
"""

import os

LINE = (
    "I joined a gym to get fit, but the treadmill filed a restraining "
    "order after I used it as a coat rack for six months."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(text: str) -> str:
    """One-liners must be a single line of 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("line must not contain a newline")
    return text


def write_entry(path: str, text: str) -> int:
    """Write the validated line to path, return characters written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return len(text)


def main() -> None:
    line = validate_line(LINE)
    count = write_entry(OUTPUT_PATH, line)
    print(f"Wrote {count} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
