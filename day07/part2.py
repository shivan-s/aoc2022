from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), "input.txt")


def compute(s: str) -> int:
    """Part 1.

    1. parse line to determine input vs output
    2. dict with files, abs path as a key and
    3. calculate the size by summing the file sizes

    Part 2
    """

    lines = s.splitlines()
    files: dict[str, int] = {"/": 0}
    dirs: dict[str, int] = {"/": 0}
    cd: list[str] = []

    for line in lines:
        words = line.split(" ")

        if words[0] == "dir":
            temp_cd = cd + [words[1]]
            if dirs.get("/".join(temp_cd)) is None:
                dirs["/".join(temp_cd)] = 0

        elif words[0].isdigit():
            temp_cd = cd + [words[1]]
            if files.get("/".join(temp_cd)) is None:
                files["/".join(temp_cd)] = int(words[0])

        elif words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    cd.pop()
                elif words[2] == "/":
                    cd = [""]
                else:
                    cd.append(words[2])

    for dr in dirs:
        for key, size in files.items():
            # dealing with root files
            if dr == "/" and "/".join(key.split("/")[:-1]) == "":
                dirs[dr] += size
            elif dr in "/".join(key.split("/")[:-1]):
                dirs[dr] += size

    curr_unused = 70_000_000 - dirs["/"]
    candidate_dirs = {k: v for k, v in dirs.items() if (v + curr_unused) > 30_000_000}
    return min(candidate_dirs.values())


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
EXPECTED = 24933642


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
