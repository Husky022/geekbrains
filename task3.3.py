def my_func(a, b, c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        if a >= c and b >= c:
            result = a + b
        elif a >= b and c >= b:
            result = a + c
        elif b >= a and c >= a:
            result = b + c
    except ValueError:
        print('Введены некорректные данные!')
        return
    return result

a = input('Введите первое число "a" ')
b = input('Введите второе число "b" ')
c = input('Введите третье число "с" ')
print(f'Сумма наибольших двух чисел - {my_func(a, b, c)}')