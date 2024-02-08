import os
from colorama import Fore, Back


# Додаємо декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        function_name = str(func).split(" ")[1]
        try:
            return func(*args, **kwargs)
        except ValueError:
            if function_name == "add":
                return False, "Please, enter again your command to add contact correctly. \nGive me name and phone please"
            elif function_name == "change":
                return False, "Please, enter again your command to change contact correctly. \nGive me name and phone please"
        except IndexError:
            if function_name == "phone":
                return False, "Please, enter again your command to show contact correctly. \nGive me name please"
        except KeyError:
            if function_name == "phone":
                return False, "There is no such contact yet. Add it please."
    return inner


def validate_phone(func):
    def wrapper(args, contacts):
        name, phone = args
        if phone.isdigit():
            return func(args, contacts)
        else:
            return False, "Номер не є цифрами."
    return wrapper

# Функція взаємодії з користувачем
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Функція виводу імені у відповідях боту
def name_out(name:str):
    return f"{Fore.MAGENTA}{name}{Fore.RESET}"

# Декоратор для функції add_contact
@input_error
@validate_phone

def add_contact(args, contacts):
    name, phone = args
    if phone in contacts.values():
        return False, "Цей номер вже присутній у контактах."
    else:
        contacts[name] = phone
        return True, f"Контакт {name_out(name)} додано."
    


# Декоратор для функції change_phone
@input_error
@validate_phone
def change_phone(args, contacts):
    if len(args) != 2:
        return False, "Неправильна кількість аргументів. Потрібно ввести ім'я та новий номер телефону."
    
    name, new_phone = args
    
    if name not in contacts:
        return False, f"Попередження: Контакт {name_out(name)} не знайдено."

# Функція виводу всіх контактів    
@input_error
def all_contacts(contacts):
    if contacts == {}:
        return False, "Увага: Контактні списки порожні."
    else:
        return True, f"{contacts}"

# Функція виводу номеру телефону за іменем контакту
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return True, contacts[name]
    return False, f"Contact {name_out(name)} not found"

def main():
    contacts = {}
    
    while True:      
        user_input = input(f"{Back.LIGHTBLACK_EX}Введіть команду: {Back.RESET}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Back.LIGHTGREEN_EX}Good bye!{Back.RESET}")
            break

        elif command in ["hello", "привіт"]:
            print(f"{Fore.GREEN}Як я можу вам допомогти?{Fore.RESET}")

        elif command == "add":
            success, message = add_contact(args, contacts)
            if success:
                print(f"{Fore.CYAN}Успішно: {message}{Fore.RESET}")
            else:
                print(f"{Fore.RED}Помилка: {message}{Fore.RESET}")

        elif command == "change":
            success, message = change_phone(args, contacts)
            if success:
                print(f"{Fore.CYAN}Успішно: {message}{Fore.RESET}")
            else:
                print(f"{Fore.RED}Помилка: {message}{Fore.RESET}")

        elif command == "all":
            success, message = all_contacts(contacts)
            if success:
                print(f"{Fore.CYAN}Успішно: {message}{Fore.RESET}")
            else:
                print(f"{Fore.RED}Помилка: {message}{Fore.RESET}")

        elif command == "phone":
            success, message = show_phone(args, contacts)
            if success:
                print(f"{Fore.CYAN}Успішно: {message}{Fore.RESET}")
            else:
                print(f"{Fore.RED}Помилка: {message}{Fore.RESET}")

        else:
            print(f"{Fore.YELLOW}Невідома команда. Будь ласка, спробуйте ще раз.{Fore.RESET}")

if __name__ == "__main__":
    main()
