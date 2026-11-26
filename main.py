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


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
