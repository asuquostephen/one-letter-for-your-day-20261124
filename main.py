#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character — the letter D — to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate allows exactly one
character: a single letter A to Z, standing for the word that
describes the day. Behind this D sits "deadline": the day is the
thing that has to be finished by tonight, and everything else in
the day arranges itself around it.
Python 3 standard library only. No network.
"""
import os
import sys

LETTER = "D"


def main() -> int:
    data = LETTER.encode("utf-8")
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print(f"entry must be exactly one letter A-Z, got {LETTER!r}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
