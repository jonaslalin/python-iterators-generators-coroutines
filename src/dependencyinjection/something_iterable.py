from typing import Iterable, List

from dependency_injector import containers, providers

from generators.fibonacci import FibIterable


class Consumer:
    something_iterable: Iterable[int]

    def __init__(self, something_iterable: Iterable[int]) -> None:
        self.something_iterable = something_iterable

    def consume(self) -> List[int]:
        return list(self.something_iterable)


class ConsumerOfConsumer:
    consumer: Consumer

    def __init__(self, consumer: Consumer) -> None:
        self.consumer = consumer

    def consume(self) -> List[int]:
        return self.consumer.consume()


class Container(containers.DeclarativeContainer):
    fib_iterable_factory = providers.Factory(FibIterable)

    consumer_factory = providers.Factory(Consumer, something_iterable=fib_iterable_factory)

    consumer_singleton = providers.Singleton(Consumer, something_iterable=fib_iterable_factory)

    consumer_of_consumer_singleton = providers.Singleton(ConsumerOfConsumer, consumer=consumer_factory)
