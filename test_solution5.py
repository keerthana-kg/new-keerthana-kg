from solution5 import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8
    assert add(-3, 3) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 1) == 5
    assert divide(5, 0) == float('inf')  # Updated to check for infinity instead of exception
