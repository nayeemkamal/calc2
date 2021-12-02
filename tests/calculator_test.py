"""Testing the Calculator"""
<<<<<<< Updated upstream
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0
=======
import pytest
from calc.calculator import Calculator
from calc.history.history import History


@pytest.fixture()
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    History.clear_history()


def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 2.0, 5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0


def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 2.0, 3.0)
    assert History.add_subtraction_calculation(my_tuple) == -6.0
>>>>>>> Stashed changes


def test_calculator_add(clear_history_fixture):
    """Testing the Add function of the calculator"""
<<<<<<< Updated upstream
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
=======
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
    calc.add_numbers((4, 0))
    assert calc.get_last_result_value() == 4


def test_calculator_get_result(clear_history_fixture):
>>>>>>> Stashed changes
    """Testing the Get result method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
    calc.add_numbers((0, 0))
    assert calc.get_last_result_value() == 0


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract method of the calculator"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
    calc.subtract_numbers((0,1))
    assert calc.get_last_result_value() == -1


def test_calculator_multiply(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
    calc.multiply_numbers((1, 2))
    assert calc.get_last_result_value() == 2


def test_calculator_divide(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
    calc.divide_numbers((4, 2))
    assert calc.get_last_result_value() == 0.5

def test_calculator_count(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()
<<<<<<< Updated upstream
    result  = calc.multiply_numbers(1,2)
    assert result == 2
=======

    assert calc.count_history() == 0

def test_calculator_clear(clear_history_fixture):
    """ tests multiplication of two numbers"""
    # pylint: disable=unused-argument,redefined-outer-name

    calc = Calculator()

    assert calc.clear_history()
>>>>>>> Stashed changes
