import pytest
from string_calculator import add

def test_empty_string():
    assert add("") == 0
    
def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,5") == 6
