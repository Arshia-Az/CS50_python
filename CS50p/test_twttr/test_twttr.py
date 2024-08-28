from twttr import shorten
import pytest


def test_shorten_lower():
    assert shorten("hi how are you") == "h hw r y"


def test_shorten_captalize():
    assert shorten("HI HOW ARE YOU") == "H HW R Y"


def test_shorten_number():
    assert shorten("123456789") == "123456789"


def test_shorten_punctuation():
    assert shorten("...") == "..."
