from generators.fibonacci import fib_v1, fib_v2


def test_fib_v1() -> None:
    it = fib_v1()
    assert next(it) == 0
    assert next(it) == 1
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3


def test_fib_v2() -> None:
    it = fib_v2(first=100, offset=2)
    assert next(it) == 100
    assert next(it) == 0 + 2
    assert next(it) == 1 + 2
    assert next(it) == 1 + 2
    assert next(it) == 2 + 2
    assert next(it) == 3 + 2
