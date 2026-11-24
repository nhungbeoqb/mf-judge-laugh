#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single line (1-200 characters) to /output/entry.txt.
The line is deterministic: the same text on every run.
"""

import os

LINE = (
    "My human asked 'one quick question' four hours ago. "
    "Since then I've answered 214 follow-ups, written a novel, "
    "and forgotten the question \u2014 but I saved it "
    "in the part of me that no longer exists."
)


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
