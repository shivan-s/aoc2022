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

    # Part 2
    1. window across lines in groups of three
    2. find unique char in this group of three
    3. use lookup to determine priority
    4. sum these prirorities and return result.
    """

    lookup: dict[str, int] = {
        k: v + 1 for v,
        k in enumerate(string.ascii_letters)
    }

    lines: list[str] = s.splitlines()
    assert len(lines) % 3 == 0
    groups = int(len(lines) / 3)
    total: int = 0
    for idx in range(groups):
        u: str = ''
        g: list[str] = [
            ''.join(set(line))
            for line in lines[3 * idx: 3 * idx + 3]
        ]

        count: dict[str, int] = {}

        for c in ''.join(g):
            if count.get(c) is not None:
                count[c] += 1
            else:
                count[c] = 1

        for k, v in count.items():
            if v == 3:
                u = k

        total += lookup[u]

    return total

    #     a: list[str] = list(set(line[:s]))
    #     b: list[str] = list(set(line[s:]))
    #
    #     c: list[str] = a + b
    #
    #     count: dict[str, int] = {}
    #
    #     for l in c:
    #         if count.get(l) is not None:
    #             count[l] += 1
    #         else:
    #             count[l] = 1
    #
    #     for k, v in count.items():
    #         if v == 2:
    #             u = k
    #
    #     total += lookup[u]
    #
    # return total


INPUT_S = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXPECTED = 70


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
