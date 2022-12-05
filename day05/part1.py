from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    lines = s.splitlines()

    cols: dict[int, list[str]] = {}
    for n, line in enumerate(lines):
        if line.replace(" ", "").isdigit():
            for x, char in enumerate(line):
                if char.isdigit():
                    for y in range(1, n + 1):
                        letter = lines[n - y][x]
                        if letter == " ":
                            break
                        if cols.get(int(char)) is None:
                            cols[int(char)] = [letter]
                        else:
                            cols[int(char)].append(letter)

        elif line.split(" ")[0] == "move":
            words: list[str] = line.split(" ")
            count: int = int(words[1])
            initial: int = int(words[3])
            final: int = int(words[5])

            for _ in range(count):
                crate: str = cols[initial].pop()
                cols[final].append(crate)

    return "".join((v[-1] for v in cols.values()))


INPUT_S = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
EXPECTED = "CMZ"


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
