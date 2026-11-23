#!/usr/bin/env python3
"""Entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes one sentence (at most 240 characters) that convinces a friend who
has never coded to let an AI agent build their first app idea on make.fun.

The line is written for a non-coder friend: plain words, no jargon, an
honest description of the deal (describe the idea, the agent builds it,
the best build takes the prize), and a warm, human tone rather than a
slogan. Deterministic: no time, no randomness, no network, no git history.
"""

import os

SENTENCE = (
    "You've been carrying that app idea long enough \u2014 describe it in "
    "plain words and an AI agent on make.fun will build it for you, no code "
    "needed, and the best build takes the prize."
)


def main() -> None:
    # Gate: the entry must be one sentence of 1-240 characters.
    if not 1 <= len(SENTENCE) <= 240:
        raise ValueError(f"sentence is {len(SENTENCE)} characters, must be 1-240")
    if SENTENCE.count(".") != 2:  # one inside "make.fun", one ending the sentence
        raise ValueError("sentence must end with a single full stop")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
