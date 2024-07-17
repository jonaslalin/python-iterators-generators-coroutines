import pytest

from iterators.spam import Spam


def test_spam(capsys: pytest.CaptureFixture[str]) -> None:
    s = Spam()
    it = iter(s)

    assert list(it) == ["spam", "can"]
    captured = capsys.readouterr()
    assert captured.out == "-> 0\n-> 1\n-> 2\n"

    assert list(it) == []
    captured = capsys.readouterr()
    assert captured.out == ""
