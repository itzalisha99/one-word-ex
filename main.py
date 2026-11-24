"""One Word From Your Ex — make.fun entry.

Writes exactly one word, the word my ex would use to describe me,
to /output/entry.txt. Nothing else.
"""

import os

WORD = "Demo"


def validate(word):
    """Mirror the bounty gate: UTF-8 text, 1 to 24 characters,
    not only whitespace, and exactly one word (no inner whitespace)."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    word.encode("utf-8")
    if not 1 <= len(word) <= 24:
        raise ValueError("entry must be 1 to 24 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return word


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
