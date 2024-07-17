import re
from typing import List


class Sentence:
    words: List[str]

    def __init__(self, text: str) -> None:
        self.words = re.findall(r"\w+", text)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __len__(self) -> int:
        return len(self.words)
