def numbers():
    summary = 0
    while True:
        user_numbers = input('Введите числа через пробел. Для завершения программы введите "q" ')
        user_numbers = user_numbers.split(' ')
        flag = False
        for n in user_numbers:
            if n.lower() == 'q':
                flag = True
                break
            summary = summary + int(n)
        print(f'Сумма - {summary}')
        if flag:
            break
    return summary


print(f'Конечная сумма введенных элементов - {numbers()}')
