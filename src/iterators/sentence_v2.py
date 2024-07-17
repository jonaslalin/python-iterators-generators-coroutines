import re
from typing import List

from typing_extensions import Self


class Sentence:
    words: List[str]

    def __init__(self, text: str) -> None:
        self.words = re.findall(r"\w+", text)

    def __iter__(self) -> "SentenceIterator":
        return SentenceIterator(self.words)


class SentenceIterator:
    words: List[str]
    index = 0

    def __init__(self, words: List[str]) -> None:
        self.words = words

    def __next__(self) -> str:
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration() from None
        self.index += 1
        return word

    def __iter__(self) -> Self:
        return self
