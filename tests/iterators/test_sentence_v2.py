from collections.abc import Generator, Iterable, Iterator

import pytest

from iterators.sentence_v2 import Sentence, SentenceIterator


@pytest.fixture
def sentence() -> Sentence:
    return Sentence("Luke, I am your father.")


def test_sentence_iterator_independence(sentence: Sentence) -> None:
    assert list(sentence) == ["Luke", "I", "am", "your", "father"]
    assert list(sentence) == ["Luke", "I", "am", "your", "father"]


def test_sentence_iterator_independence_in_a_different_way(sentence: Sentence) -> None:
    it1 = iter(sentence)
    it2 = iter(sentence)
    assert it1 is not it2


def test_sentence_iterator_type(sentence: Sentence) -> None:
    it = iter(sentence)
    assert isinstance(it, Iterator)
    assert isinstance(it, Iterable)
    assert isinstance(it, SentenceIterator)
    assert not isinstance(it, Generator)


def test_sentence_iterator_manually_using_next(sentence: Sentence) -> None:
    it = iter(sentence)
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
