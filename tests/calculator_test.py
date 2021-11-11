"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.history.history import History

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    History.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0
def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    my_tuple = (1.0,2.0,3.0)
    assert History.add_subtraction_calculation(my_tuple) == -6.0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculations()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.get_result() == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    assert calc.get_result() == 0

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1
def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.multiply_numbers(1,2)
    assert result == 2
def test_calculator_divide():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result  = calc.divide_numbers(1,2)
    assert result == 2
