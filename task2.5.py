my_range = [7, 5, 3, 3, 2]


while True:
    el = int(input('Введите новый элемент рейтинга '))

    i = 1
    while i <= len(my_range):
        if my_range[0] < el:
            my_range.insert(0, el)
        elif my_range[i - 1] >= el > my_range[i]:
            my_range.insert(i - 1, el)
            break
        elif my_range[len(my_range) - 1] >= el:
            my_range.append(el)
            break
        i += 1
    print(my_range)
