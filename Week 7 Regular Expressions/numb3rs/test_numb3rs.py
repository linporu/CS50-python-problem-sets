import pytest
from numb3rs import validate


@pytest.mark.parametrize("valid_input, expected", [

("127.0.0.1", True),

("0.0.0.0", True),

("255.255.255.255", True),

("512.512.521.512", False),

("1.2.3.1000", False),

("1.2000.3.1", False),

("1.2.3000.1", False),

("0.256.256.256", False),

("cat", False)

])


def test_validate(valid_input, expected):

	assert validate(valid_input) == expected
