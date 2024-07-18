from itertools import takewhile
from typing import Iterator, Optional


def fib_forever() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n: Optional[int] = None) -> Iterator[int]:
    if n is None:
        return fib_forever()
    gen_obj = (x for i, x in takewhile(lambda i_x: i_x[0] < n, enumerate(fib_forever())))
    return gen_obj


class FibIterable:
    n: Optional[int]

    def __init__(self, n: Optional[int] = None) -> None:
        self.n = n

    def __iter__(self) -> Iterator[int]:
        return fib(self.n)
