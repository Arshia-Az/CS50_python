from fuel import gauge, convert
import pytest


def main():
    test_convert()
    test_value_error()
    test_zero_devison()



def test_zero_devison():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")



if __name__ == "__main__":
    main()
