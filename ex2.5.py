
def print_menu(): # """ такими ковычками вуделяют документацию к функции """. ФУНКЦИЯ должна делать только то что в
    # ней написано, и не должна быть больше 30 строчек
    """Выводит меню на экран"""
    print('1.Ввести данные\n2.Вывести данные\n3.Выход')

def create_new_entry(fields):
    """Создает новую запись
    input args:
        fields - ('name', 'age', ...) - список полей в записи
        return - {'name': 'Tom', 'age': 56, ...} - dict - новая запись"""
    entry = {} # пустой словарь это
    for field in fields:
        entry[field] = input(f'Введите значение поля {field} - ')
    return entry

def show_data(database):
    """Выводит данные на экран"""
    for entry in database:
        print(entry)

def main():
    """Главная функция которая вызывает другие функции """
    database = []
    data_fields = ('name', 'age', 'income')

    while True:
        print_menu()
        change = input('Выберите пункт меню - ')
        if change == '1':
            database.append(create_new_entry(fields=data_fields))

        elif change == '2':
            show_data(database)

        elif change == '3':
            break

        else:
            print('Выберете верный пункт меню')

main()
