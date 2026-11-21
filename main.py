#!/usr/bin/env python3
"""Write one one-line joke to /output/entry.txt.

The joke is a live-demo disaster: the demo worked in rehearsal, the
coding agent cleaned up the 'unused' code, and on stage the room
learns the app itself was the unused code. The setup is every
developer's rehearsal; the twist is what the cleanup actually removed.
"""

import os
from pathlib import Path

TEXT = (
    "The demo worked in rehearsal — then my agent cleaned up the "
    "'unused' code, and on stage we discovered the app was the "
    "unused code."
)


def main() -> None:
    # The entry must be 1-280 Unicode characters and not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of bounds"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
