"""PuddleWatch — The Worst App Idea Ever Pitched.

Deterministically writes a single-sentence pitch for the worst, most
useless app imaginable to /output/entry.txt. Pure standard library,
no network, no randomness, no model calls: the pitch is a fixed string.

The pitch is exactly one sentence, 236 characters, with no trailing
newline, so the written file satisfies the gate (UTF-8, 1-240 chars).
"""

import os

PITCH = (
    "PuddleWatch is the app that tracks every puddle within one mile of "
    "you in real time and sends you a push notification the instant each "
    "one fully evaporates, so you never again miss the exact moment wet "
    "pavement becomes regular pavement."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
