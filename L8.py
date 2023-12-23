# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1.Создаем файл
# -Открываем файл на дозапись
# 2.Добавление контактов
# запросить/получить у пользователя данные
# -подготовить форматирование данных к записи
# -открыть файл на дозапись
# -добавить новый контакт в файл
# 3.Вывод данных на экран
# -открыть файл на чтение
# -вывод на экран
# 4.Поиск контактов
# -запросить/получить у пользователя данные
# -открыть файл на чтение
# -произвести поиск контакта
# -вывести на экран
# 5.Интерфейс
# -вывод на экран меню пользователя
# -окно для ввода данных
# -запросить/получить у пользователя вариант режима работы(1,2,3,4)
# -вызов соотвествующей функции
# -осуществление выхода из программы

# -----------------------------------------

import os


def print_data():
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()
        
        
def input_name():
    return input("Vvedite imya kontakta ").title()

def input_surname():
    return input("Vvedite familiu kontakta ").title()

def input_patronymic():
    return input("Vvedite otchestvo kontakta ").title()    

def input_phone():
    return input("Vvedite nomer telefona kontakta ")

def input_address():
    return input("Vvedite address kontakta ").title()


def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = " "
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n {address}\n\n"
    
    
def add_contact():
    new_contact = input_data()
    with open("phonebook.txt", "a", encoding="utf-8") as file:
        file.write(new_contact)


def search_contact():
    print("Menu polzovatelya:\n"
            "1. Familiya \n"
            "2. Imya\n"
            "3. Otchestvo \n"
            "4. Telefon \n"
            "5. Address \n")
    command = input("Viberite punkt menu ")
        
    while command not in ("1", "2", "3", "4", "5"):
            print("Nekorrektiy vvod dannix ")
            command = input("Viberite punkt menu ")
            
    i_search = int(command) - 1
    
    search = input("Vveite dannie dlya poiska ").lower()
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        print(contacts_list)
    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        print(lst_contact)
        
        if search in lst_contact[i_search]:
            print(contact_str)
            print()
            check_cont = True
    if not check_cont:
        print("Takogo kontakta net")
        

def copy_line(source_file, destination_file, line_number):
    try:
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines()

            if 1 <= line_number <= len(lines):
                with open(destination_file, 'a', encoding='utf-8') as destination:
                    destination.write(lines[line_number - 1])

                print(f"Строка {line_number} скопирована из {source_file} в {destination_file}")
            else:
                print(f"Ошибка: Номер строки {line_number} вне диапазона.")

    except FileNotFoundError:
        print("Ошибка: Один из файлов не найден.")
        
        
        
def interface():
    with open("phonebook.txt", "a", encoding="utf-8"):
        pass
    command = None
    os.system("cls")
    while command != "5":
        print("Меню пользователя:\n"
              "1. Вывод на экран \n"
              "2. Добавить контакт\n"
              "3. Поиск контакта \n"
              "4. Копировать строку\n" 
              "5. Выход \n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод данных ")
            command = input("Выберите пункт меню: ")

        if command == "1":
            print_data()
        elif command == "2":
            add_contact()
        elif command == "3":
            search_contact()
        elif command == "4":
            line_to_copy = int(input("Введите номер строки для копирования: "))
            copy_line("phonebook.txt", "new_phonebook.txt", line_to_copy)
        elif command == "5":
            print("Завершение программы ")
        print()

if __name__ == "__main__":
    interface()
    
    
    
    








# def interface():
#     with open("phonebook.txt", "a", encoding="utf-8"):
#         pass
#     command = None
#     os.system("cls")
#     while command != "4": 
#         print("Menu polzovatelya:\n"
#             "1. Vivod na ekran \n"
#             "2. Dobavit kontakt\n"
#             "3. Poisk kontakta \n"
#             "4. Vixod \n"
#             "5. Izmenenie \n")
#         command = input("Viberite punkt menu ")
        
#         while command not in ("1", "2", "3", "4", "5"):
#             print("Nekorrektiy vvod dannix ")
#             command = input("Viberite punkt menu ")
            
#         match command:
#             case "1":
#                 print_data()
#             case "2":
#                 add_contact()
#             case "3":
#                 search_contact()
#             case "4":
#                 print("Zavershenie programi ")
#             case "5":
#                 copy_line()
#         print()

# if __name__ == "__main__":
#     interface()
    