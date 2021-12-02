"""Calculation history Class"""
from calc.history.history import History


class Calculations:
    """ calc object"""

    # pylint: disable=too-few-public-methods


    @staticmethod
    def get_result():
        """ get a specific result from history"""

        return History.get_last_calculation()


    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return History.add_calculation(calculation)

    @staticmethod
    def add_number(values):
        """ get a specific add calculation from history"""
        History.add_addition_calculation(values)
        return History.get_last_calculation().get_result()

    @staticmethod
    def subtract_number(values):
        """ get a specific subtract calculation from history"""

        History.add_subtraction_calculation(values)
        return History.get_last_calculation().get_result()

    @staticmethod
    def multiply_numbers(values):
        """ get a specific calculation from history"""

        History.add_multiplication_calculation(values)
        return History.get_last_calculation().get_result()

    @staticmethod
    def divide_numbers(values):
        """ get a specific calculation from history"""

        History.add_division_calculation(values)
        return History.get_last_calculation().get_result()
