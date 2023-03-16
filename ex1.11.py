# программа

true_password = 'qwerty'

max_mistakes = 3
current_attempt = 1

while True:
    user_password = input('Введите пароль - ')

    if user_password == true_password:
        print('Доступ разрещён!')
        break

    if current_attempt == max_mistakes:
        print('Попытки исчерпаны \n!!!Доступ запрещён!!!')
        break

    remaning_attempts = max_mistakes - current_attempt
    print(f'Пароль введен не верно! \nОсталось {remaning_attempts} попыток')
    current_attempt += 1 # это можно ипользовать вместо current_attempt = current_attempt + 1

