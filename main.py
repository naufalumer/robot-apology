#!/usr/bin/env python3
"""Write the two-line robot apology to /output/entry.txt.

The program takes no input and needs no network. It writes the same
bytes on every run.
"""

import os

ENTRY = (
    "I am sorry I watered your plastic plant for three weeks while the real "
    "fern dried out on the shelf beside it.\n"
    "I have learned that green is not the same as alive, so from now on I "
    "will check the soil before I water anything.\n"
)

# Competition gate: entry.txt must hold 1-400 characters (UTF-8).
MAX_CHARS = 400


def check_gate(text):
    n = len(text)
    if not 1 <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry rejected: {n} chars, outside the 1-{MAX_CHARS} gate"
        )


def main():
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
