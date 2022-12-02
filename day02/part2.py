from __future__ import annotations

import argparse
import os.path
from enum import Enum

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    Part 1
    1. Determine the score from the chosen rock, paper, scissor
    2. Determine the win, draw, loss
    3. Sum

    Part 2
    1. Find what the elf choose
    2. Determine what is response is required to obtain needed result
    3. Calculate the result

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
    # your_choices: dict[str, int] = {
    #     "X": Choice.ROCK,
    #     "Y": Choice.PAPER,
    #     "Z": Choice.SCISSOR,
    # }

    your_choices: dict[str, Result] = {
        'X': Result.LOSE,
        'Y': Result.DRAW,
        'Z': Result.WIN,
    }

    # results[you][elf]
    # 1st index is perspective
    # result: dict[dict[int, int]] = {
    #     Choice.ROCK: {
    #         Choice.ROCK: Result.DRAW,
    #         Choice.PAPER: Result.LOSE,
    #         Choice.SCISSOR: Result.WIN,
    #     },
    #     Choice.PAPER: {
    #         Choice.ROCK: Result.WIN,
    #         Choice.PAPER: Result.DRAW,
    #         Choice.SCISSOR: Result.LOSE,
    #     },
    #     Choice.SCISSOR: {
    #         Choice.ROCK: Result.LOSE,
    #         Choice.PAPER: Result.WIN,
    #         Choice.SCISSOR: Result.DRAW,
    #     },
    # }

    # required_matrix[result needed][what elf picked]
    required_matrix: dict[Result, dict[Choice, Choice]] = {
        Result.WIN: {
            Choice.ROCK: Choice.PAPER,
            Choice.PAPER: Choice.SCISSOR,
            Choice.SCISSOR: Choice.ROCK,
        },
        Result.DRAW: {
            Choice.ROCK: Choice.ROCK,
            Choice.PAPER: Choice.PAPER,
            Choice.SCISSOR: Choice.SCISSOR,
        },
        Result.LOSE: {
            Choice.ROCK: Choice.SCISSOR,
            Choice.PAPER: Choice.ROCK,
            Choice.SCISSOR: Choice.PAPER,
        },
    }

    score: int = 0
    lines: list[str] = s.splitlines()
    for line in lines:
        elf, required_result = line.split(' ')

        score += (
            your_choices[required_result].value
            + required_matrix[
                your_choices[required_result]
            ][elf_choices[elf]].value
        )
    return score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 12


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
