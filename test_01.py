import pytest


def add(a: int, b: int) -> int:
    return a + b


def test_add():
    assert add(1, 2) == 3