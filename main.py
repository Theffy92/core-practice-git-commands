import pytest


def always_returns_true():
    return False
    print("This is false")


def test_always_returns_true():
    assert always_returns_true() == False
    print(False)
