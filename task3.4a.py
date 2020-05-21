# operator - **

def my_func(x, y):
    while True:
        try:
            x = int(x)
            if x > 0:
                break
        except ValueError:
            try:
                x = float(x)
                if x > 0:
                    break
            except ValueError:
                continue
    while True:
        try:
            y = int(y)
            if y < 0 and y % 1 == 0:
                break
        except ValueError:
            continue
    result = x ** y
    return result


x = input('Введите любое положительное число ')
y = input('Введите целое отрицательное число ')
print(my_func(x, y))
