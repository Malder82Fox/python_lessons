gain = float(input('ваши доходы - '))
cost = float(input('ваши затраты - '))

if gain - cost > 0:
    print(f' Ваша рентабильность  {(gain - cost) / gain:.3f}')
    employee = int(input('Сколько у вас сотрудников - '))
    print(f'Доход на сотрудника {(gain - cost) / employee:.3f}')

elif gain - cost == 0:
    print('Отработали в "ноль"')

else:
    print(f'Вы ушли в минус (((( {gain - cost}')



