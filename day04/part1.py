from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    """
    # Part 1
    0. Determine if section falls in range of the other
    1. parse the input, determine range and check below
    2. Check if range is within other
    3. OR if the second range is in the first.
    """
    lines = s.splitlines()
    count = 0
    for line in lines:

        def _parse_input(string: str) -> list[int]:
            start, stop = sorted([int(n) for n in string.split("-")])
            return list(range(int(start), int(stop) + 1))

        first, second = (_parse_input(elf) for elf in line.split(","))

        # combined = sorted(list(set(first + second)))
        #
        #
        # if combined == first or combined == second:
        #     count += 1

        if set(first).issubset(set(second)) or set(second).issubset(set(first)):
            count += 1

    return count


INPUT_S = """\
6-8,2-4
2-3,4-5
5-7,7-9
2-8,3-7
40-60,60-60
2-6,4-8
"""
EXPECTED = 2


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
