from fuel import convert, gauge
import pytest


@pytest.mark.parametrize("input_format", [
    "12",
    "1-2",
    "1//2",
    "",
    "!@#$%^&*()_+]"
])
def test_convert_value_error(input_format):
    with pytest.raises(ValueError):
        convert(input_format)


@pytest.mark.parametrize("integer", [
    "0.5/0.8",
    "-1/-2"
])
def test_convert_value_error(integer):
    with pytest.raises(ValueError):
        convert(integer)


@pytest.mark.parametrize("invalid_fraction",[
    "2/1",
    "-1/-2"
])
def test_convert_value_error(invalid_fraction):
    with pytest.raises(ValueError):
        convert(invalid_fraction)


@pytest.mark.parametrize("zero_division",[
    "1/0",
])
def test_convert_zero_division_error(zero_division):
    with pytest.raises(ZeroDivisionError):
        convert(zero_division)


@pytest.mark.parametrize("valid_fraction, expected", [
    ("1/100", 1),
    ("1/2", 50),
    ("1/1", 100),
    ("0/1", 0)
])
def test_convert_expected(valid_fraction, expected):
    assert convert(valid_fraction) == expected


@pytest.mark.parametrize("percentage, expected", [
    (0, "E"),
    (1, "E"),
    (2, "2%"),
    (50, "50%"),
    (99, "F"),
    (100, "F")
])
def test_gauge_expected(percentage, expected):
    assert gauge(percentage) == expected
