import re 
from typing import Callable
from decimal import Decimal

text = "Загальний дохід працівника складається"\
" з декількох частин: 1000.01 як основний дохід,"\
" доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text : str) :
    incomes = re.findall(r'\s\d+\.\d*\s?', text)
    for income in incomes :
        yield income
    

def sum_profit(text: str, func: Callable) -> float :
    total_income = 0
    for element in func(text) :
        total_income += Decimal(element)
    return total_income
        

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
