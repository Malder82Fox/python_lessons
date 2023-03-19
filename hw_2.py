# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_menu():
    """Выводит меню на экран"""
    print('1.Ввести данные\n2.Вывести данные\n3.Выход')

def create_new_empty(fields):
    """Добавляем нового пользователя
    вводим аргументы
        fields (имя, фамилия, ......)
    возвращаем
        return {имя: Иван, фамилия: Петров,....}"""
    entry = {}
    for field in fields:
        entry[field] = input(f'Введите значение поля {field}: ')
    return entry

def show_data(database):
    """Вывод данных на экран"""
    for entry in database:
        print(entry)

def main():
    database = []
    data_fields = ('name', 'surname', 'born', 'city', 'email', 'phone')

    while True:
        print_menu()
        change = input('Выберите пунк меню: ')
        if change == '1':
            database.append(create_new_empty(fields=data_fields))

        elif change == '2':
            show_data(database)

        elif change == '3':
            break

        else:
            print('Выберите верный пунк меню: ')

main()
