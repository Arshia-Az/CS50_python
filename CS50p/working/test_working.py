from working import convert
import pytest


def main():
    test_wrong_format()
    test_time()
    test_wrong_hour()
    test_wrong_minute()


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_time():
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"



def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 17 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("8:60 PM to 8:60 AM")

if __name__ == "__main__":
    main()
