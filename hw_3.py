# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.
# 'winter':'spring':'summer':autumn'

while True:
    user_mount = input('Введите номер месяца от 1 до 12: ')
    if user_mount.isdigit() and 0 < int(user_mount) <= 12:
        season_1 = ['winter', 'spring', 'summer', 'autumn', 'winter']
        season_2 = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
        print(f'Месяц под номером: {user_mount}\nВ списке: {season_1[int(user_mount) // 3]}\nВ словаре:{season_2[int(user_mount) //3]}')
        break
    else:
        print('Ошибка !!!')

