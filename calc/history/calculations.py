"""Calculation history Class"""
from history import History
class Calculations:
    # pylint: disable=too-few-public-methods

    def __init__(self) -> None:
        self.history=History()
    # 
    # def clear_history():
    #     self.history.clear()
    #     return True
    # 
    # def count_history():
    #     return len(history)
    
    def get_result(self):
        return self.history.get_last_calculation()
    # 
    # def get_first_calculation():
    #     return history[-1]
    # 
    # def get_calculation(num):
    #     """ get a specific calculation from history"""
    #     return history[num]
    
    def add_calculation(self,calculation):
        """ get a specific calculation from history"""
        return self.history.add_calculation(calculation)
    
    def add_number(self,values):
        self.history.add_addition_calculation(values)
        return self.history.get_last_calculation().get_result()
    
    def subtract_number(self,values):
        self.history.add_subtraction_calculation(values)
        return self.history.get_last_calculation().get_result()
    
    def multiply_numbers(self,values):
        self.history.add_multiplication_calculation(values)
        return self.history.get_last_calculation().get_result()
    
    def divide_numbers(self,values):
        self.history.add_division_calculation(values)
        return self.history.get_last_calculation().get_result()