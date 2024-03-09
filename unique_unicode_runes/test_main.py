import io

import main
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        ("3+5", "\n"),
        ("日本語にÚѢѣほんごsdÚѢѣvds ", "ÚѢѣごにほん日本語\uf254\uf306\n"),
    ],
)
def test_method(capfd, monkeypatch, input, expected):
    monkeypatch.setattr("sys.stdin", io.StringIO(input))
    main.main()
    out, _ = capfd.readouterr()
    assert out == expected
