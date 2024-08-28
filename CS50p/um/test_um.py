from um import count


def test_upper_lower_case():
    assert count("Um, thanks, um, regular expressions make sense now") == 2
    assert count("um, thanks, um, regular expressions make sense now") == 2


def test_with_word():
    assert count("yummi") == 0


def test_with_space():
    assert count("helo um ") == 1
