# python-iterators-generators-coroutines

> Iterables have an `__iter__` method that instantiates a new iterator every time. Iterators implement a `__next__` method that returns individual items, and an `__iter__` method that returns `self`. Therefore, iterators are also iterable, but iterables are not iterators.
>
> To support multiple traversals, it must be possible to obtain multiple independent iterators from the same iterable instance, and each iterator must keep its own internal state, so a proper implementation of the pattern requires each call to `iter(my_iterable)` to create a new, independent, iterator.
>
> The classic Iterator pattern can be replaced by a generator function or generator expression.
>
> Any Python function that has the `yield` keyword in its body is a generator function: a function which, when called, returns a generator object. In other words, a generator function is a generator factory.
>
> *Source: [Fluent Python, 2nd Edition](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) by Luciano Ramalho*
