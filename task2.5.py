my_range = [7, 7, 5, 5, 3, 3, 2, 2]
print(my_range)

while True:
    el = int(input('Введите новый элемент рейтинга '))
    i = 1
    while i <= len(my_range):
        if el > my_range[i-1]:
            break
        i += 1
    my_range.insert(i - 1, float(el))

    print(my_range)
