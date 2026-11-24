"""Two days of quiet dread.

Writes a single-line code review comment to $MAKEFUN_OUTPUT_DIR/entry.txt:
an approval ("LGTM. The tests pass") that quietly admits the repo is the
only proof any of us were ever here. Deterministic — the same line, every run.
"""

import os


def main():
    line = "LGTM. The tests pass, and one day this repo will be the only proof any of us were here."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # open() directly: a deterministic single write, no temp file or rename.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
