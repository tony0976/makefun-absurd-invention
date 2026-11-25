# The laugh is in the invention itself: the machine does the worrying for
# you, and delivers the bad news in the words of a relationship talk.
"""Writes one absurd invention pitch to /output/entry.txt."""
import os

TEXT = "A washing machine that texts you 'we need to talk' the moment it finds a single red sock hiding in the whites."

# Rule: the pitch must be exactly one sentence of 1 to 220 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 220 and TEXT.count(".") == 1, f"entry must be one sentence, 1-220 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
