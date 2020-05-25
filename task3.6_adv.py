def int_func(my_str):
    while True:
        my_str = list(my_str)
        flag = False
        for n in my_str:
            if 97 <= ord(n) <= 122 or ord(n) == 32:
                continue
            else:
                flag = True
                print('Только маленькие латинские буквы от "a" до "z"!')
                my_str = input('Введите слова, состоящие из маленьких латинских букв через пробел ')
                break
        if flag:
            continue
        break

    my_str = (''.join(my_str)).title()

    return my_str


print(int_func(input('Введите слова, состоящие из маленьких латинских букв через пробел ')))