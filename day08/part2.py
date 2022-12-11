from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    """
    1. Determine the trees on the edge
    2. create a dict for each coordinate - a dict with T,L,R,B as lists
    3. if the list is descending then seen.

    # part 2

    """
    mat = [[int(_) for _ in line] for line in s.splitlines()]

    # for y, line in enumerate(mat):
    #     if y != 0 and y != len(mat) - 1:
    #         for x, tree in enumerate(line):
    #             if x != 0 and x != len(line) - 1:
    #                 if (
    #                     max([mat[y_i][x] for y_i in range(y)]) < tree  # top
    #                     or max(mat[y][x_i] for x_i in range(x)) < tree  # left
    #                     or max(mat[y_i][x] for y_i in range(y + 1, len(mat)))
    #                     < tree  # bottom
    #                     or max(mat[y][x_i] for x_i in range(x + 1, len(line)))
    #                     < tree  # right
    #                 ):
    #                     seen += 1

    def _traverse(lst: list[int], tree: int) -> int:
        """Test."""
        new_l = []
        for t in lst:
            new_l.append(t)
            if t >= tree:
                break
        return len(new_l)

    scores: list[int] = []
    for y, line in enumerate(mat):
        if y != 0 and y != len(mat) - 1:
            for x, tree in enumerate(line):
                if x != 0 and x != len(line) - 1:
                    top = reversed([mat[y_i][x] for y_i in range(y)])
                    left = reversed([mat[y][x_i] for x_i in range(x)])
                    right = [mat[y_i][x] for y_i in range(y + 1, len(mat))]
                    bottom = [mat[y][x_i] for x_i in range(x + 1, len(line))]
                    scores.append(
                        _traverse(top, tree)
                        * _traverse(left, tree)
                        * _traverse(right, tree)
                        * _traverse(bottom, tree),
                    )

    return max(scores)


INPUT_S = """\
30373
25512
65332
33549
35390
"""
EXPECTED = 8


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
