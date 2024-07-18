from typing import Callable, Iterator, List

from dependency_injector import containers, providers

from generators.fibonacci import fib


class ConsumerV1:
    some_iterator: Iterator[int]

    def __init__(self, some_iterator: Iterator[int]) -> None:
        self.some_iterator = some_iterator

    def consume(self) -> List[int]:
        return list(self.some_iterator)


class ConsumerV2:
    some_iterator_factory: Callable[..., Iterator[int]]
    n: int

    def __init__(self, some_iterator_factory: Callable[..., Iterator[int]], n: int) -> None:
        self.some_iterator_factory = some_iterator_factory
        self.n = n

    def consume(self) -> List[int]:
        return list(self.some_iterator_factory(self.n))


class Container(containers.DeclarativeContainer):
    fib_iterator_factory = providers.Factory(fib)

    consumer_v1_factory = providers.Factory(ConsumerV1, some_iterator=fib_iterator_factory)

    consumer_v2_factory = providers.Factory(ConsumerV2, some_iterator_factory=fib_iterator_factory.provider)
