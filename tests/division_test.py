"""Testing Addition"""
import pytest

from calc.calculations.division import Division

def test_calculation_division():
    """test division"""
    mynumbers = (4.0,2.0)
    division = Division(mynumbers)
    assert division.get_result() == 0.5
def test_calculation_division_zero():
    """test division"""
    with pytest.raises(ZeroDivisionError):
        mynumbers = (0,2)
        Division(mynumbers).get_result()
