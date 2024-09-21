import pytest
from working import convert


@pytest.mark.parametrize("valid_input, expected", [

("9 AM to 5 PM", "09:00 to 17:00"),

("9:00 AM to 5:00 PM", "09:00 to 17:00"),

("10 AM to 8:50 PM", "10:00 to 20:50"),

("10:30 PM to 8 AM", "22:30 to 08:00")

])


def test_convert_expected(valid_input, expected):

	assert convert(valid_input) == expected


@pytest.mark.parametrize("invalid_input",[

"9:60 AM to 5:60 PM",

"9 AM - 5 PM",

"09:00 AM - 17:00 PM",

])


def test_convert_ValueError(invalid_input):

	with pytest.raises(ValueError):

		convert(invalid_input)
