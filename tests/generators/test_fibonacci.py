from typing import List

import pytest

from generators.fibonacci import FibIterable, fib


def test_fib_forever() -> None:
    it = fib()
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (-1, []),
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 1]),
        (4, [0, 1, 1, 2]),
        (5, [0, 1, 1, 2, 3]),
    ],
)
def test_fib(n: int, expected: List[int]) -> None:
    assert list(fib(n)) == expected


def test_fib_iterable() -> None:
    fib_iterable = FibIterable(n=5)
    assert list(fib_iterable) == [0, 1, 1, 2, 3]
    assert list(fib_iterable) == [0, 1, 1, 2, 3]
