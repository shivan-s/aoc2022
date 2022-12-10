from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    """
    1. parse the input
    2. `x` is an array that stores register over cycles
    3. append register onto the array
    4. if noop append current x
    5. if addx append the current and v

     0
    [1]   0   0 1
    noop [1] [1,1]
                  0 1 2 3
    addx 3 [1,4] [1,1,1,4]
                      0 1 2 3 4
    addx -5 [4,4,-1] [1,1,1,1,4, 4, -1]
    """

    lines: list[str] = s.splitlines()
    x: list[int] = [1]
    CYCLES = [20, 60, 100, 140, 180, 220]

    for line in lines:

        if line.split()[0] == "addx":
            v: int = int(line.split()[1])
            x.extend([x[-1], x[-1] + v])

        elif line.split()[0] == "noop":
            x.append(x[-1])

        else:
            raise Exception("Unknown instruction")

    # print(x)
    # for cycle in CYCLES:
    #     print(cycle, x[cycle], cycle * x[cycle])

    return sum([x[cycle - 1] * cycle for cycle in CYCLES])


INPUT_S = """\
addx 15
addx -11 
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
EXPECTED = 13140


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
