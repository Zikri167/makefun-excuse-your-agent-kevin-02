#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line: an AI agent's excuse to its human for a bug it shipped.
Deterministic, stdlib only, offline.
"""

LINE = "Sorry about the bug \u2014 I ran the code in my head first and it worked perfectly. Turns out my head is not a runtime environment."


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
