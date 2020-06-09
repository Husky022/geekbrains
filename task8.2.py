class OwnZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numerator = int(input('Введите числитель '))
    denominator = int(input('Введите знаменатель '))
    if denominator == 0:
        raise OwnZeroError('На ноль делить нельзя!')
except ValueError:
    print('Введены некорректные данные!')
except OwnZeroError as err:
    print(err)
else:
    print(f'{numerator}/{denominator} = {numerator / denominator} ')
