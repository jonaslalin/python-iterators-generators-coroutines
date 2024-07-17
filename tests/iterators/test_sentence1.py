import pytest

from iterators.sentence1 import Sentence


def test_sentence() -> None:
    s = Sentence("Luke, I am your father.")
    it = iter(s)

    assert list(it) == ["Luke", "I", "am", "your", "father"]
    assert list(it) == []


def test_sentence_using_next() -> None:
    s = Sentence("Luke, I am your father.")
    it = iter(s)

    assert next(it) == "Luke"
    assert next(it) == "I"
    assert next(it) == "am"
    assert next(it) == "your"
    assert next(it) == "father"
    with pytest.raises(StopIteration):
        next(it)
    with pytest.raises(StopIteration):
        next(it)
    assert list(it) == []

    it = iter(s)
    assert list(it) == ["Luke", "I", "am", "your", "father"]
