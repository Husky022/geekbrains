def my_func(a, b):
    try:
        result = int(a) / int(b)
    except ValueError:
        print('Введены некорректные данные')
        return
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        return
    return result


a = input('Введите первое число "a" ')
b = input('Введите второе число "b" ')
print(my_func(a, b))
