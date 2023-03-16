# переберем все элементы списка

data = [100, 'hello', 200, 'world']
print(len(data)) # len возвращает длину (количество элементов) в объекте

i = 0
while i < len(data):
    print(data[i])
    i += 1

for i in data: # это сокращенная версия кода в строках 6-9 (цикл для переборки: кортежей, словарей, строк)
    print(i)

person = {'name': 'Tom', 'age': 56}

for key, value in person.items(): # перебираем словарь (БД) по ключам и значениям
    print(key, value)
