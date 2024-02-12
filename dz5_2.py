import re
from typing import Callable

def generator_numbers(text: str):
    # визначення дійсних чисел
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    matches = pattern.finditer(text)
    # проходио по знайдених числах та повертаємо генератор
    for match in matches:
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # підсумовуємо числа
    total_sum = sum(func(text))
    return total_sum


text = "Загальний дохід працівника  складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")