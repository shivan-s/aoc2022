from __future__ import annotations

import argparse
import os.path
import string

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    # Part 1
    1. split in half
    2. find unique letter
    3. create look up with unique letter to priority number
    4. sum this and return result.

    """

    lookup: dict[str, int] = {
        k: v + 1 for v,
        k in enumerate(string.ascii_letters)
    }
    lines = s.splitlines()
    total: int = 0
    for line in lines:
        u: str = ''
        half: int = int(len(line) / 2)

        a: list[str] = list(set(line[:half]))
        b: list[str] = list(set(line[half:]))

        c: list[str] = a + b

        count: dict[str, int] = {}

        for item in c:
            if count.get(item) is not None:
                count[item] += 1
            else:
                count[item] = 1

        for k, v in count.items():
            if v == 2:
                u = k

        total += lookup[u]

    return total


INPUT_S = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXPECTED = 157


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
