# test_exception.py
import pytest

def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

# Returns TypeError because input is not a string
# palindrome(44)

# this unit test tests that the function verifies the function raises TypeError exception in case somebody passed a non-string value to it
def test_palindrome():
    with pytest.raises(TypeError):
        palindrome(44)