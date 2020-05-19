product = []
i = 1
title = input('Введите название продукта ')
price = input('Введите цену продукта ')
quantity = input('Введите количество ')
unit = input('Введите единицы измерения ')

product.append((i, {'название': title, 'цена': price, 'количество': quantity, 'ед.измерения': unit}))

while True:
    user_ask = input('Продолжить ввод? Для выхода - ответьте "нет"')
    if user_ask.lower() == 'нет':
        break
    i += 1
    title = input('Введите название продукта ')
    price = input('Введите цену продукта ')
    quantity = input('Введите количество ')
    unit = input('Введите единицы измерения ')
    product.append((i, {'название': title, 'цена': price, 'количество': quantity, 'ед.измерения': unit}))


def print_result(value):
    result = []
    i = 0
    while i < len(product):
        result.append(product[i][1].get(value))
        i += 1
    print(f"{value} - {result}")


print_result('название')
print_result('цена')
print_result('количество')
print_result('ед.измерения')
