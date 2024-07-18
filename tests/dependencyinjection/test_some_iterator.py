import pytest

from dependencyinjection.some_iterator import ConsumerV1, Container


@pytest.fixture
def container() -> Container:
    return Container()


def test_fib_iterator_factory(container: Container) -> None:
    it = container.fib_iterator_factory(n=5)
    assert list(it) == [0, 1, 1, 2, 3]
    assert list(it) == []

    it = container.fib_iterator_factory(n=5)
    assert list(it) == [0, 1, 1, 2, 3]
    assert list(it) == []


@pytest.mark.xfail(reason="AttributeError: '_asyncio.Future' object has no attribute 'consume'")
def test_consumer_v1_factory(container: Container) -> None:
    consumer1 = container.consumer_v1_factory(some_iterator__n=3)
    consumer2 = container.consumer_v1_factory(some_iterator__n=5)
    assert consumer1 is not consumer2
    assert consumer1.consume() == [0, 1, 1]
    assert consumer1.consume() == []
    assert consumer2.consume() == [0, 1, 1, 2, 3]
    assert consumer2.consume() == []


def test_inject_fib_iterators_manually(container: Container) -> None:
    fib1 = container.fib_iterator_factory(n=3)
    fib2 = container.fib_iterator_factory(n=5)
    consumer1 = ConsumerV1(some_iterator=fib1)
    consumer2 = ConsumerV1(some_iterator=fib2)
    assert consumer1 is not consumer2
    assert consumer1.consume() == [0, 1, 1]
    assert consumer1.consume() == []
    assert consumer2.consume() == [0, 1, 1, 2, 3]
    assert consumer2.consume() == []


def test_consumer_v2_factory(container: Container) -> None:
    consumer1 = container.consumer_v2_factory(n=3)
    consumer2 = container.consumer_v2_factory(n=5)
    assert consumer1 is not consumer2
    assert consumer1.consume() == [0, 1, 1]
    assert consumer1.consume() == [0, 1, 1]
    assert consumer2.consume() == [0, 1, 1, 2, 3]
    assert consumer2.consume() == [0, 1, 1, 2, 3]
