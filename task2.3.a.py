# list

months = ['Январь', 'Февраль', 'Март', 'Апрель','Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
while True:
    months_number = int(input('Выберите номер месяца от 1 до 12 '))
    if 1 <= months_number <= 12:
        break
print(f'Выбранный месяц - {months[months_number - 1]}')
