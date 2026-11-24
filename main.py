#!/usr/bin/env python3
"""One Line of Earned Pride — writes a single earned-pride line to /output/entry.txt."""

import os

LINE = (
    "On her third try, seven-year-old Ana threaded the needle, "
    "sewed the button back onto her father's coat, "
    "and held it up like a flag she'd sewn herself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
