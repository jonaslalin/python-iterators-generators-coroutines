import re
from typing import Iterator, List


class Sentence:
    words: List[str]

    def __init__(self, text: str) -> None:
        self.words = re.findall(r"\w+", text)

    def __iter__(self) -> Iterator[str]:
        for word in self.words:  # noqa: UP028
            yield word
