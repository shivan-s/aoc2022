from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    """Part 1.

    1. parse line to determine input vs output
    2. walk through directories and calculate the size of directories, with recursion.
    3. calculate the size by summing the file sizes
    """

    lines = s.splitlines()
    files: dict[tuple[str, ...], int] = {("/",): 0}
    dirs: dict[tuple[str, ...], int] = {("/",): 0}
    cd: list[str] = ["/"]

    for line in lines:
        words = line.split(" ")

        temp_cd = cd[:]
        temp_cd.append(words[1])
        if words[0] == "dir":
            if dirs.get((tuple(temp_cd))) is None:
                dirs[(tuple(temp_cd))] = 0

        elif words[0].isdigit():
            if files.get(tuple(temp_cd)) is None:
                files[tuple(temp_cd)] = int(words[0])

        elif words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    cd.pop()
                elif words[2] == "/":
                    cd = ["/"]
                else:
                    cd.append(words[2])

    for dr in sorted(list(dirs.keys()), key=lambda x: len(x), reverse=True):
        for key, size in files.items():
            if set(dr).issubset(set(key)):
                dirs[dr] += size
        print(dr, dirs[dr])

    return sum((v for _, v in dirs.items() if v <= 100_000))


INPUT_S = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
EXPECTED = 95437


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
