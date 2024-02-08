
import os
from colorama import Fore, Back


# додаємо декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        function_name = str(func).split(" ")[1]
        try:
            return func(*args, **kwargs)
        # якщо помилка при введення команди add
        except ValueError:
            if function_name == "add_contact":
                return  f"{Fore.RED}Неправильно введена команда.\
                    \nPlease type {Fore.LIGHTGREEN_EX} add name phone.{Fore.RESET}\n"
            elif function_name == "change_phone":
                return  f"{Fore.YELLOW}Неправильно введена команда.\
                    \nПотрібно ввести {Fore.LIGHTGREEN_EX}change name new_phone.{Fore.RESET}\n"
            
        except IndexError:
            if function_name == "show_phone":
                return f"{Fore.YELLOW}Неправильно введена команда.\
                    \nПотрібно ввести {Fore.LIGHTGREEN_EX}phone name{Fore.RESET}\n"
                    
        except KeyError:
            # виводить помилку, якщо немає такого контакту
            if function_name == "show_phone":
                return f"Контакту {name_out(name)} не існує. Add it please.\n"
            
    return inner

# функція взаємодії з користувачем
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# функція виводу іʼмя у відповідях боту
def name_out (name:str):
    return f"{Fore.MAGENTA}{name}{Fore.RESET}"


@input_error
# функція додавання контактів
def add_contact(args, contacts):
    name, phone = args
    if phone.isdigit():
        # перевіряємо чи вже існує такий номер або імя
        if phone in contacts.values() or name in contacts.keys():
                        
            return f"{Fore.RED}Цей номер або ім'я вже присутній у контактах.{Fore.RESET}"
        else:
            contacts[name] = phone
            return f"{Fore.GREEN}Контакт{Fore.RESET} {name_out(name)} {Fore.GREEN}додано.{Fore.RESET}"
    else:
        return f"{Fore.LIGHTRED_EX}Номер не є цифрами.{Fore.RESET}"

        
# функція виводу всіх контактів    

@input_error
def all_contacts(contacts):
    if contacts == {}:
        return f"{Fore.LIGHTRED_EX}Warning:{Fore.RESET}Contacts list is empty."
    else:
        return f"{contacts}"


# функція зміни номеру у словнику
@input_error
def change_phone(args, contacts):
       
    name, new_phone = args
    # перевіряємо чи новий телефон скдадається з цифр
    if not new_phone.isdigit():
        return  f"{Fore.RED}Новий номер телефону повинен містити лише цифри.{Fore.RESET}"
    # перевіряємо чи існує такий контакт
    if name not in contacts:
        return f"{Fore.YELLOW}Попередження: Контакт{Fore.RESET} {name_out(name)} {Fore.YELLOW}не знайдено.{Fore.RESET}"
    
    contacts[name] = new_phone
    return f"{Fore.LIGHTGREEN_EX}Номер телефону контакту{Fore.RESET} {name_out(name)} {Fore.LIGHTGREEN_EX}змінено на {Fore.RESET} {Fore.LIGHTBLUE_EX}{new_phone}{Fore.RESET}"
    
 

# функція виводу номеру телефону за імʼям контакту
@input_error

def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return f"{Fore.GREEN}Телефон контакту{Fore.RESET} {name_out(name)} {Fore.GREEN}є{Fore.RESET} {Fore.LIGHTBLUE_EX}{contacts[name]}{Fore.RESET}"
    else:
        return f"{Fore.RED}Contact{Fore.RESET} {name_out(name)} {Fore.RED}not found{Fore.RESET}"

# головна функція
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

        elif command in ["add", "додати"]:
            print(add_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))           
            
        elif command == "all":
            print(f"{Fore.CYAN}{all_contacts(contacts)}{Fore.RESET}")
        
        elif command == "change":
            print(change_phone(args, contacts))
        
        else:
            print(f"{Fore.LIGHTRED_EX}Невірна команда.{Fore.RESET}")

if __name__ == "__main__":
    main()


