from typing import Iterator


class Spam:
    index = 0

    def __iter__(self) -> Iterator[str]:
        print("->", self.index)
        yield "foo"
        self.index += 1
        print("->", self.index)
        yield "bar"
        self.index += 1
        print("->", self.index)
