

import re

from typing import Callable

# функція для пошуку чисел в тексті

def generator_numbers(text: str):
    # перевіряємо чи текст не None і не пустий
    if text is not None and text != '':
        # розбиваємо текст на частини по пробілу і записуємо їх у список
        list_of_words_drom_text = text.split(" ")
        # створюємо шаблон для пошуку чисел і враховуємо що може бути крапка між цифрами
        pattern = r"([0-9]+\.?[0-9]?)"
        # цикл для пошуку чисел
        for str_in_list in list_of_words_drom_text:
            # якщо рядок то число
            if re.search(pattern, str_in_list) is not None:
                # повертаємо число і чекаємо наступне число
                yield str_in_list

# функція для розрахунку суми чисел у тексті
def sum_profit(text: str, func: Callable) -> float:
    # створюмо змінну для суми чисел
    all_sum = 0
    # входимо у цикл щоб пройтись генератором по всім числам
    for digit in func(text):
        # записуємо всі числа до змінної і перетводимо у float        
        all_sum += float(digit)
    # повертаємо суму чисел
    return all_sum
   
# приклад використання

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

