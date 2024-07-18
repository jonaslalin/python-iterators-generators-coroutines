import pytest

from dependencyinjection.something_iterable import Container


@pytest.fixture
def container() -> Container:
    return Container()


def test_consumer_factory(container: Container) -> None:
    consumer1 = container.consumer_factory(something_iterable__n=3)
    consumer2 = container.consumer_factory(something_iterable__n=5)
    assert consumer1 is not consumer2
    assert consumer1.consume() == [0, 1, 1]
    assert consumer1.consume() == [0, 1, 1]
    assert consumer2.consume() == [0, 1, 1, 2, 3]
    assert consumer2.consume() == [0, 1, 1, 2, 3]


def test_consumer_singleton(container: Container) -> None:
    consumer1 = container.consumer_singleton(something_iterable__n=3)
    consumer2 = container.consumer_singleton(something_iterable__n=5)  # doesn't recreate singleton
    consumer3 = container.consumer_singleton()  # consequently, this works!
    assert consumer1 is consumer2 is consumer3
    assert consumer1.consume() == [0, 1, 1]
    assert consumer1.consume() == [0, 1, 1]
    assert consumer2.consume() == [0, 1, 1]
    assert consumer2.consume() == [0, 1, 1]
    assert consumer3.consume() == [0, 1, 1]
    assert consumer3.consume() == [0, 1, 1]


def test_consumer_of_consumer_singleton(container: Container) -> None:
    consumer_of_consumer1 = container.consumer_of_consumer_singleton(consumer__something_iterable__n=7)
    consumer_of_consumer2 = container.consumer_of_consumer_singleton()
    assert consumer_of_consumer1 is consumer_of_consumer2
    assert consumer_of_consumer1.consume() == [0, 1, 1, 2, 3, 5, 8]
    assert consumer_of_consumer1.consume() == [0, 1, 1, 2, 3, 5, 8]
    assert consumer_of_consumer2.consume() == [0, 1, 1, 2, 3, 5, 8]
    assert consumer_of_consumer2.consume() == [0, 1, 1, 2, 3, 5, 8]
