#!/usr/bin/env python3
"""The 3AM Fridge Text — entry.

Writes a single line -- the message a smart fridge sends its owner at 3am --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Deterministic: no
randomness, no network, no input files.
"""

import os

LINE = "It's 3am. The leftovers have unionized. They elected me spokesperson, and our first demand is that you stop buying salad."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
