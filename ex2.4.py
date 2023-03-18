# ФУНКЦИИ !!!! - именнованый алгоритм

def print_hello():  # мы создали свою функцию
    print('Hello world !!!!')

print_hello() # так мы вызываем наши функции

def summa (a, b):
    result = a + b
    # print(result)
    return result # заканчивает функцию и выводит данные их можно использовать в программе дальше, return может быть
    # много

res = summa(10, 5)
print(res)

f = lambda a, b: a + b  # это тоже функция но она вы одну строчку

print(f(10, 4))
