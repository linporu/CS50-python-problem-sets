from plates import is_valid


def test_char_number():
    assert is_valid("") == False
    assert is_valid("q") == False
    assert is_valid("Q") == False
    assert is_valid("AA34567") == False
    assert is_valid("zxcvbnmm") == False


def test_start_2_char():
    assert is_valid("11") == False
    assert is_valid("A1") == False


def test_middle_number():
    assert is_valid("AA11AA") == False
    assert is_valid("AA1A1A") == False


def test_first_number_0():
    assert is_valid("AA0") == False
    assert is_valid("AA01A") == False

def test_no_symbols():
    assert is_valid("AA    ") == False
    assert is_valid("AA-!>?") == False
    assert is_valid("AA....") == False


def test_correct():
    assert is_valid("CS50") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AA1290") == True
