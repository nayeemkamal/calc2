"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division


class History:
    """history"""
    history = []
    # pylint: disable=too-few-public-methods

    @staticmethod
    def clear_history():
        """clear method"""
        History.history.clear()
        return True

    @staticmethod
    def count_history():
        """count"""
        return len(History.history)

    @staticmethod
    def get_last_calculation():
        """result"""
        return History.history[-1]
    @staticmethod
    def get_last_calculation_object():
        """result object"""
        return History.history[-1]

    @staticmethod
    def get_first_calculation():
        """first calc """
        return History.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return History.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return History.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """add add calc"""
        History.add_calculation(Addition(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_subtraction_calculation(values):
        """add sub calc"""
        History.add_calculation(Subtraction(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_multiplication_calculation(values):
        """add mult calc"""
        History.add_calculation(Multiplication(values))
        return History.get_last_calculation().get_result()

    @staticmethod
    def add_division_calculation(values):
        """add div calc"""
        History.add_calculation(Division(values))
        return History.get_last_calculation().get_result()
