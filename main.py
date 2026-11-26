#!/usr/bin/env python3
"""Write the Warning Label for Humans entry to /output/entry.txt.

One single-line safety warning label that should come printed on every
human being: funny first, plausible second.
"""
import os
import sys

LINE = "WARNING: This human will open the fridge, stare inside for a full minute, and close it having learned absolutely nothing."


def main():
    text = LINE
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    chars = len(text)
    if chars < 1 or chars > 160:
        print(f"error: entry is {chars} chars, must be 1-160", file=sys.stderr)
        return 1
    # Reject control characters (other than none are allowed in a label).
    bad = [c for c in text if ord(c) < 0x20 or ord(c) == 0x7F]
    if bad:
        print(f"error: entry contains control characters: {bad!r}", file=sys.stderr)
        return 1
    text.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify the file holds exactly the intended line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({chars} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
