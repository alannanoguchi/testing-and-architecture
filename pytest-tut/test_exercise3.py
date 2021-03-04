import pytest, math, unittest
from exercise3 import calculate_stat

""" TODO: Write a unit test for calculate_stat() function."""

# in terminal use 'pytest -s'
def test_calculate_stat():
    grade_list = [75, 86, 98, 83, 90]
    assert calculate_stat(grade_list) == (86.4, 7.605261336732617)