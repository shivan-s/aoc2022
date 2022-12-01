from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    """Compute.
        From part 1:
        1. Turn input into list of numbers e.g. ("1000", "2000", "3000", "")
        2. Loop through list and group together numbers with an empty element \
                separate elves.
        3. Calculate total calories
        4. Return the max calories

        Part 2:
        1. Sort the list
        2. Find top 3
        3. Sum the top 3
    """

    # part 1
    elves_calories = []
    total = 0
    for elem in s.split("\n"):
        if elem == "":
            elves_calories.append(total)
            total = 0
        else:
            total += int(elem)

    # part 2
    return sum(sorted(elves_calories, reverse=True)[:3])


INPUT_S = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
EXPECTED = 45000


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
