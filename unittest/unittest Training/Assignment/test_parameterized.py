
import pytest

def square(x):
    return x * x
@pytest.mark.parametrize("input_val, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_square(input_val, expected):
    result = square(input_val)
    assert result == expected, f"Expected {expected} but got {result}"


