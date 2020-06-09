class NotNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        new_element = input('Введите новый элемент или команду "stop" для остановки ')
        if new_element.lower() == 'stop':
            break
        if not (new_element.lstrip('-')).isdigit():
            raise NotNumberError('Вы ввели не число!')
    except NotNumberError as err:
        print(err)
    else:
        my_list.append(int(new_element))
print(f'Итоговый список - {my_list}')