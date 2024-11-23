from solution2 import (
    add, subtract, multiply, divide, power, floor_division,
    modulus, is_greater, is_equal, is_lesser
)

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 3) == 0
    assert add(0, 0) == 0  # Additional test case

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 5) == -5  # Additional test case

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0
    assert multiply(-4, 5) == -20  # Additional test case

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 1) == 5
    assert divide(5, 0) == float('inf')  # Test for division by zero
    assert divide(0, 5) == 0  # Test for zero numerator

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0  # Additional test case

def test_floor_division():
    assert floor_division(10, 3) == 3
    assert floor_division(5, 0) == float('inf')  # Test for division by zero
    assert floor_division(0, 5) == 0  # Test for zero numerator

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(5, 0) != modulus(5, 0)  # NaN comparison for modulus by zero
    assert modulus(0, 5) == 0  # Test for zero numerator

def test_is_greater():
    assert is_greater(10, 5) == True
    assert is_greater(5, 10) == False
    assert is_greater(5, 5) == False  # Additional test case

def test_is_equal():
    assert is_equal(5, 5) == True
    assert is_equal(10, 5) == False
    assert is_equal(-5, -5) == True  # Additional test case

def test_is_lesser():
    assert is_lesser(5, 10) == True
    assert is_lesser(10, 5) == False
    assert is_lesser(5, 5) == False  # Additional test case
