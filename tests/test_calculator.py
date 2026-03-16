import pytest
from src.calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_add_large():
    assert add(9999999, 3) == 10000002

def test_add_float():
    assert add(2.5, 3.5) == 6.0

def test_add_string():
    with pytest.raises(TypeError):
        add(3, "hello")

def test_add_none():
    with pytest.raises(TypeError):
        add(3, None)

def test_subtract():
    assert subtract(10, 3) == 7

def test_subtract_negative():
    assert subtract(2, 3) == -1

def test_subtract_negative_all():
    assert subtract(-2, -3) == 1

def test_subtract_to_zero():
    assert subtract(2, 2) == 0

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_multiply_all_negative():
    assert multiply(-2, -3) == 6

def test_multiply_zero():
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
