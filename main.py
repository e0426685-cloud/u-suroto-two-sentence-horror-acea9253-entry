"""Two-Sentence Horror: the locked door.

A parent locks a child's bedroom door every night to keep her safe.
The second sentence turns that protection inside out: the thing the
lock was meant to keep out is already inside, and it has learned how
the lock works. Writes the story to /output/entry.txt.
Python standard library only, fully deterministic.
"""

import os

MAX_CHARS = 400

STORY = (
    "For a year I have tucked my daughter in and locked her bedroom door "
    "from the hallway, to keep her safe. "
    "Last night she begged me to stop, because the thing that lives under "
    "her bed has learned to turn the key."
)


def main() -> None:
    assert "\n" not in STORY and "\r" not in STORY, "entry must be a single line"
    assert STORY.strip(), "entry must not be only whitespace"
    assert STORY == STORY.strip(), "entry must not start or end with whitespace"
    assert STORY.endswith("."), "entry must end with a full stop"
    sentence_parts = [s for s in STORY.split(". ") if s]
    assert len(sentence_parts) == 2, f"entry must be exactly two sentences, got {len(sentence_parts)}"
    assert 1 <= len(STORY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(STORY)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == STORY, "written entry does not match"
    assert 1 <= len(written) <= 400
    print(f"Wrote /output/entry.txt ({len(written)} characters, 2 sentences)")


if __name__ == "__main__":
    main()
