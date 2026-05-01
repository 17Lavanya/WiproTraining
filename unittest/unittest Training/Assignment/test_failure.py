import pytest

def test_uppercase_failure():
    result = "hello".upper()
    assert result == "hello", f"Expected 'hello' but got {result}"
