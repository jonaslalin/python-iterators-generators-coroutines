from typing import Iterator, Optional


def fib_v1() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_v2(first: Optional[int] = None, offset: int = 0) -> Iterator[int]:
    if first is not None:
        yield first
    gen_obj = (f + offset for f in fib_v1())
    yield from gen_obj
