import pytest

from fibbo import fibbo


def test_fib_9_is_34():
    assert fibbo(39) == 34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibbo(-1)

