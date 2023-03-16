sec = int(input('Введите количество целых секунд - '))

# hour = sec // 3600
# minutes = (sec %  3600) // 60
# seconds = sec % 60
#
# print(f' Время в формате чч:мм:сс - {hour}:{minutes}:{seconds}')

print(f' Время в формате чч:мм:сс - {sec // 3600}:{(sec % 3600) // 60}:{sec % 60}')
