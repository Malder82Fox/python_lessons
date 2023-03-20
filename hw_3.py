# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# 'winter':'spring':'summer':autumn'

year = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
user_mount = int(input('Введите номер месяца: '))

# for mount in year:
#     print(year[mount])

for quarter in (year.values()):  # перебераем значения словаря year (квартала)
    # print(quarter)
    for mount in quarter: # перебераем элементы значений словоря year (месяца)
        # print(mount)
        if user_mount == mount:
            res = year.items(mount)
            print(f'Ваш месяц: {res}')




# print(year)