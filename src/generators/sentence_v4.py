import re
from typing import Iterator, List


class Sentence:
    words: List[str]

    def __init__(self, text: str) -> None:
        self.text = text

    def __iter__(self) -> Iterator[str]:
        gen_obj = (match.group() for match in re.finditer(r"\w+", self.text))
        return gen_obj
