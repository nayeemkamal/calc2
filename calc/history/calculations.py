"""Calculation history Class"""
from history import History
class history.
    history = History()
    # pylint: disable=too-few-public-methods
    # @staticmethod
    # def clear_history():
    #     history.clear()
    #     return True
    # @staticmethod
    # def count_history():
    #     return len(history)
    # @staticmethod
    # def get_last_calculation():
    #     return history[-1]
    # @staticmethod
    # def get_first_calculation():
    #     return history[-1]
    # @staticmethod
    # def get_calculation(num):
    #     """ get a specific calculation from history"""
    #     return history[num]
    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return history.add_calculation(calculation)
    @staticmethod
    def add_addition_calculation(values):
        history.add_addition_calculation(values)
        return history.get_last_calculation().get_result()
    @staticmethod
    def add_subtraction_calculation(values):
        history.add_subtraction_calculation(values)
        return history.get_last_calculation().get_result()
    @staticmethod
    def add_multiplication_calculation(values):
        history.add_multiplication_calculation(values)
        return history.get_last_calculation().get_result()
    @staticmethod
    def add_division_calculation(values):
        History.add_division_calculation(values)
        return History.get_last_calculation().get_result()