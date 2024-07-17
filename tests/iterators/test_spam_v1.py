import pytest

from iterators.spam_v1 import Spam


@pytest.fixture
def spam() -> Spam:
    return Spam()


def test_spam_iterator(spam: Spam, capsys: pytest.CaptureFixture[str]) -> None:
    it = iter(spam)
    assert list(it) == ["foo", "bar"]
    captured = capsys.readouterr()
    assert captured.out == "-> 0\n-> 1\n-> 2\n"
    assert list(it) == []
    captured = capsys.readouterr()
    assert captured.out == ""
