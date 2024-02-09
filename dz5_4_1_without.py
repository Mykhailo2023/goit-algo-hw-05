
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
                return  f"Неправильно введена команда.\
                    \nPlease type  add name phone."
            elif function_name == "change_phone":
                return  f"Неправильно введена команда.\
                    \nПотрібно ввести change name new_phone."
            
        except IndexError:
            if function_name == "show_phone":
                return f"Неправильно введена команда.\
                    \nПотрібно ввести phone name"
        
       
       
        # ''' не можу розібратися з цим куском коду  '''
        
        # except KeyError:                                   
        #     # виводить помилку, якщо немає такого контакту
        #     if function_name == "show_phone":
        #         return f"Контакту не існує. Add it please.\n"
        
    #    ''' не можу розібратися з цим куском коду  '''  
    return inner




# функція взаємодії з користувачем
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# функція виводу іʼмя у відповідях боту
def name_out (name:str):
    return f"{name}"

@input_error
# функція додавання контактів
def add_contact(args, contacts):
    name, phone = args
    if phone.isdigit():
        # перевіряємо чи вже існує такий номер
        if phone in contacts.values():
            return "Цей номер вже присутній у контактах."
        # перевіряємо чи вже існує таке ім'я
        elif name in contacts.keys():               
            return f"Контакт {name_out(name)} вже існує."
        # якщо все правильно додаємо контакт
        else:
            contacts[name] = phone
            return f"Контакт {name_out(name)} додано."
    else:
        return "Номер не є цифрами."


@input_error
# функція додавання контактів
def change_phone(args, contacts):
       
    name, new_phone = args
    # перевіряємо чи новий телефон скдадається з цифр
    if not new_phone.isdigit():
        return  "Новий номер телефону повинен містити лише цифри."
    # перевіряємо чи існує такий контакт
    if name not in contacts:
        return f"Попередження: Контакт {name_out(name)} не знайдено."
    
    contacts[name] = new_phone
    return f"Номер телефону контакту {name_out(name)} змінено на {new_phone}"

        
# функція виводу всіх контактів    

@input_error
def all_contacts(contacts):
    if contacts == {}:
        return "Warning: Contacts list is empty."
    else:
        return f"{contacts}"


# функція зміни номеру у словнику
@input_error
def change_phone(args, contacts):
       
    name, new_phone = args
    # перевіряємо чи новий телефон скдадається з цифр
    if not new_phone.isdigit():
        return  "Новий номер телефону повинен містити лише цифри."
    # перевіряємо чи існує такий контакт
    if name not in contacts:
        return f"Попередження: Контакт {name_out(name)} не знайдено."
    
    contacts[name] = new_phone
    return f"Номер телефону контакту {name_out(name)} змінено на {new_phone}"
    
 

# функція виводу номеру телефону за імʼям контакту
@input_error

def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return f"Телефон контакту {name_out(name)} є {contacts[name]}"
    else:
        return "Контакту не існує. Додайте його."
    
# головна функція
def main():
    contacts = {}
    
    while True:      

        user_input = input(f"Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command in ["hello", "привіт"]:
            print("Як я можу вам допомогти?")

        elif command in ["add", "додати"]:
            print(add_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))           
            
        elif command == "all":
            print(f"{all_contacts(contacts)}")
        
        elif command == "change":
            print(change_phone(args, contacts))
        
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()


