with open("text_5.txt", "a+", encoding="utf-8") as my_file:
    while True:
        input_numbers = input('Введите числа через пробел ')
        try:
            num_check  = input_numbers.split()
            for i in num_check:
                i = int(i)
            break
        except ValueError:
            print('Только числа!')
    my_file.write(input_numbers)
    my_file.seek(0)
    numbers = ((my_file.readline()).split())
    num_sum = 0
    for el in numbers:
        num_sum += int(el)
    print(f'Сумма элементов в файле - {num_sum}')
