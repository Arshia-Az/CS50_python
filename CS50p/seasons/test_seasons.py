from seasons import main, check_time
import pytest
def main():
    test_time()

def test_time():
    assert check_time("2001-10-10") == ("2001", "10", "10")
    assert check_time("2001-1-1") == None
    

if __name__ == "__main__":
    main()


