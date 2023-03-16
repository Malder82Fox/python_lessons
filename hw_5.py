gain = int(input('ваши доходы - '))
cost = int(input('ваши затраты - '))

if gain - cost > 0:
    print(f' Ваша рентабильность  {(gain - cost) / gain}')
    employee = int(input('Сколько у вас сотрудников - '))
    print(f'Доход на сотрудника {(gain - cost) / employee}')

elif gain - cost == 0:
    print('Отработали в "ноль"')

else:
    print('Вы ушли в минус ((((')



