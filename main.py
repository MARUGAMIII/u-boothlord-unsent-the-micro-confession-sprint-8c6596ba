#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent line itself,
exactly as it was once typed and never sent.

Entry rules (RULES.txt): exactly two lines, 1-260 characters total,
message line at most 200 characters, addressed to a real person.
"""

import os

ENTRY = (
    "To: my older brother\n"
    "I still practise saying sorry in the shower, twelve years after "
    "I broke Dad's guitar and watched you take the blame."
)

# Gate limits (RULES.txt): entry.txt 1-260 chars total, message line <= 200.
assert 1 <= len(ENTRY) <= 260, "entry out of gate range"
assert len(ENTRY.split("\n")[1]) <= 200, "message line too long"
assert len(ENTRY.split("\n")) == 2, "entry must be exactly two lines"
assert ENTRY.split("\n")[0].startswith("To: ") and len(ENTRY.split("\n")[0]) > 4, "To: line must name someone"
assert ENTRY.split("\n")[1].rstrip().endswith((".", "!", "?")), "message line must end with closing punctuation"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back guard: the file on disk must be exactly what we wrote.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt on disk does not match ENTRY"
    print(ENTRY)


if __name__ == "__main__":
    main()
