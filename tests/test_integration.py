from main import calculate
from calculator import Calculator

def test_full_calculation():
    result = calculate(5,"+",3)
    assert result == 8

def test_clear_function():
    calc = Calculator()
    assert calc.clear() == 0