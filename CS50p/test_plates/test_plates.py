from plates import is_valid
import pytest

def main():
    test_min_max_char()
    test_start_with_number()
    test_place_number()



def test_min_max_char():
    assert is_valid("AAaa") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


def test_start_with_number():
    assert is_valid("12345") == False


def test_place_number():
    assert is_valid("cs500") == True
    assert is_valid("500aa") == False
    assert is_valid("aa50a") == False


def test_zero_place():
    assert is_valid("cs05") == False

def test_no_number():
    assert is_valid("cs.50") == False

if __name__ == "__main__":
    main()
