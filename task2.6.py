product = []
i = 1
title = input('Введите название продукта ')
price = input('Введите цену продукта ')
quantity = input('Введите количество ')
unit = input('Введите единицы измерения ')

product.append((i, {'название': title, "цена": price, 'количество': quantity, 'ед.измерения': unit}))

print(product)

while True:
    user_ask = input('Продолжить ввод? ')
    if user_ask.lower() == 'нет':
        print(f'Название - {(product[i - 1][1]).get(title)}')
        print(f'Цена - {(product[i - 1][1]).get(price)}')
        print(f'Количество - {(product[i - 1][1]).get(quantity)}')
        print(f'Ед.измерения - {(product[i - 1][1]).get(unit)}')
        break
