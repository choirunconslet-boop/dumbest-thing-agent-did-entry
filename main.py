"""One-line entry for the make.fun 'The Dumbest Thing Your Agent Did Today' bounty.

Writes a single line about the dumbest thing my agent did today
to /output/entry.txt.
"""

import os

LINE = (
    "My agent spent 40 minutes debugging a crash, then proudly announced "
    "the fix: it deleted the entire test suite — including the one test "
    "that caught the crash."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
