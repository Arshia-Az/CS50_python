from bank import value
import pytest

def test_incorrect_value():
    assert value("hi boss") == 20
    assert value("hello boss") == 0
    assert value("boss what's up") == 100


def test_value_case_insensitivity():
    assert value("HI BOSS") == 20
    assert value("Hello BOSS") == 0
    assert value("BOSS WHAT'S UP") == 100
