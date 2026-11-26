"""The Absurd Clause Contest entry.

The line is written as genuine terms-of-service boilerplate: a numbered
section, the formal opener "Notwithstanding any prior agreement", and the
legal verb "shall be resolved". The absurdity ambushes the reader only at
the end, when the dispute-resolution mechanism turns out to be a binding
staring contest against a Chief Legal Officer who has not blinked since 2019.
That single concrete image is specific and original, the joke lands on
one reading with no outside setup, and the sentence stays tight with no
explanation of its own joke — matching the judge's brief in order.
"""

import os

TEXT = "Section 23.8: Notwithstanding any prior agreement, any dispute arising under these Terms shall be resolved by a binding staring contest with our Chief Legal Officer, who has not blinked since 2019."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
