# Ввод, вывод и преобразование типов

num_1 = input('Введите первое число - ')  # input всегда возвращает текст !!!!!
num_2 = input('Введите первое число - ')  # input всегда возвращает текст !!!!!

print(type(num_1), type(num_2)) # type функция показывающая тип данных

num_1 = int(num_1) # преобразовываем тип данных в INT
num_2 = int(num_2)

print(type(num_1), type(num_2)) # type функция показывающая тип данных

result = num_1 + num_2

# int варианты применения
# result = int(num_1) + int(num_2)
# num_1 = int(input('Введите первое число - '))
# num_2 = int(input('Введите второе число - '))

print(result)
