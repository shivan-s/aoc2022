from __future__ import annotations

import argparse
import math
import os.path
from dataclasses import dataclass
from pprint import pprint

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, str]
    test: int
    is_true: int
    is_false: int
    count: int = 0


STEPS = 10_000


def compute(s: str) -> int:
    """Part 1.
    1. parse input

    Part 2

    """
    lines = s.splitlines()
    monkeys: list[Monkey] = []
    for idx, line in enumerate(lines):
        if line.startswith("Monkey"):
            m: type[Monkey] = Monkey(
                items=lines[idx + 1].split(":")[-1].split(","),
                operation=lines[idx + 2].split()[-2:],
                test=int(lines[idx + 3].split()[-1]),
                is_true=int(lines[idx + 4].split()[-1]),
                is_false=int(lines[idx + 5].split()[-1]),
            )
            monkeys.append(m)

    lcm = math.prod([_.test for _ in monkeys])

    for _ in range(STEPS):
        for m in monkeys:
            if m.items:
                for item in m.items:
                    item = int(item)
                    m.count += 1
                    operator, operand = m.operation
                    if operator == "*":
                        if operand == "old":
                            new_item = item * item
                        else:
                            new_item = item * int(operand)
                    elif operator == "+":
                        if operand == "old":
                            new_item = item + item
                        else:
                            new_item = item + int(operand)

                    new_item = new_item % lcm

                    if new_item % m.test == 0:
                        monkeys[m.is_true].items.append(new_item)
                    else:
                        monkeys[m.is_false].items.append(new_item)

                m.items = []

    second, first = sorted([m.count for m in monkeys])[-2:]
    return first * second


INPUT_S = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
EXPECTED = 2713310158


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
