# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.

def my_func(x, y, z):
    user_args = [x, y, z]
    total = []
    max_1 = max(user_args)
    total.append(max_1)
    user_args.remove(max_1)
    max_2 = max(user_args)
    total.append(max_2)
    print(f"Ваши максимальные числа {max_1} и {max_2}\nих сумма равна:")
    print(sum(total))

my_func(100, 34, -58)

