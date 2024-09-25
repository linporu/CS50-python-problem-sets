import pytest
from um import count


@pytest.mark.parametrize("valid_input, expected", [

("um", 1),

("um?", 1),

("Um, thanks for the album.", 1),

("Um, thanks, um...", 2),

("Yummy", 0)


])


def test_um_expected(valid_input, expected):

	assert count(valid_input) == expected
