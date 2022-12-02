from __future__ import annotations

import argparse
import os.path
from enum import Enum

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    1. Determine the score from the chosen rock, paper, scissor
    2. Determine the win, draw, loss
    3. Sum

    """

    class Choice(Enum):
        ROCK: int = 1
        PAPER: int = 2
        SCISSOR: int = 3

    class Result(Enum):
        LOSE: int = 0
        DRAW: int = 3
        WIN: int = 6

    elf_choices: dict[str, Choice] = {
        'A': Choice.ROCK,
        'B': Choice.PAPER,
        'C': Choice.SCISSOR,
    }
    your_choices: dict[str, Choice] = {
        'X': Choice.ROCK,
        'Y': Choice.PAPER,
        'Z': Choice.SCISSOR,
    }

    # results[you][elf]
    # 1st index is perspective
    result: dict[Choice, dict[Choice, Result]] = {
        Choice.ROCK: {
            Choice.ROCK: Result.DRAW,
            Choice.PAPER: Result.LOSE,
            Choice.SCISSOR: Result.WIN,
        },
        Choice.PAPER: {
            Choice.ROCK: Result.WIN,
            Choice.PAPER: Result.DRAW,
            Choice.SCISSOR: Result.LOSE,
        },
        Choice.SCISSOR: {
            Choice.ROCK: Result.LOSE,
            Choice.PAPER: Result.WIN,
            Choice.SCISSOR: Result.DRAW,
        },
    }

    score: int = 0
    lines: list[str] = s.splitlines()
    for line in lines:
        elf, you = line.split(' ')

        score += (
            your_choices[you].value +
            result[your_choices[you]][elf_choices[elf]].value
        )
    return score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 15


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
