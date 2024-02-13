

from typing import Callable
import re
# функція для пошуку чисел в тексті
def generator_numbers(text: str):
    # створюємо шаблон для пошуку чисел і враховуємо що може бути крапка між цифрами
    # pattern = r'\s{1}\d+\.{0,1}\d*\s{1}' # нарешті правильно, тут ми вказали що один пробіл, але воно працює коли пробілів більше
    pattern = r'\s+\d+\.{0,1}\d*\s+'  # так теж правильно, \.{0,1} вказує що крапки може не бути

    for match in re.finditer(pattern, text):
        yield float(match.group())
# функція для розрахунку суми чисел у тексті
def sum_profit(text: str, func: Callable):
    numbers = func(text)
    total_sum = sum(numbers)
    return total_sum

text = "Загальний дохід працівника складається з декількох  частин: 1000.01 як основний o19 дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
