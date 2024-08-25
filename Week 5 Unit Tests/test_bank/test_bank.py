from bank import value


def test_start_with_hello():
    assert value("Hello, David.") == 0
    assert value("Hello") == 0
    assert value("HeLLo, David.") == 0  # case-insensitive


def test_only_h():
    assert value("h") == 20
    assert value("hADSFDSFDSF") == 20


def test_non_h():
    assert value("") == 100  # None
    assert value("qwerADSF") == 100  # case-insensitive
    assert value("1234567890!@#$%^&*()") == 100  # numbers and symbols
