sec = int(input('Введите количество целых секунд - '))

# hour = sec // 3600
# minutes = (sec %  3600) // 60
# seconds = sec % 60
#
# print(f"{hour:02}:{minutes:02}:{seconds:02}")

print(f' Время в формате чч:мм:сс - {sec // 3600:02}:{(sec % 3600) // 60:02}:{sec % 60:02}')
