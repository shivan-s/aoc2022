from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    part 1
    1. parse the string
    2. keep log of chars until unique
    3. return the index where 3 unique chars are provided
    """
    for idx, char in enumerate(s):
        if idx > 3:
            packet = s[idx - 3: idx]
            if len(set(packet)) == 3 and char not in packet:
                return idx + 1

        # uniques.append(char)
        # if len(uniques) > 3:
        #     if char not in uniques:
        #         return idx + 1
        #
        #
        # if char in uniques:
        #     uniques = []


INPUT_S_1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
EXPECTED_1 = 5

INPUT_S_2 = 'nppdvjthqldpwncqszvftbrmjlhg'
EXPECTED_2 = 6

INPUT_S_3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
EXPECTED_3 = 10

INPUT_S_4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
EXPECTED_4 = 11

INPUT_S_5 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
EXPECTED_5 = 7


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S_1, EXPECTED_1),
        (INPUT_S_2, EXPECTED_2),
        (INPUT_S_3, EXPECTED_3),
        (INPUT_S_4, EXPECTED_4),
        (INPUT_S_5, EXPECTED_5),
    ),
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
