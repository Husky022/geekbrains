my_str = input('Введите строку из нескольких слов через пробел ')
my_str = my_str.split(" ")
print(my_str)

i = 0
while len(my_str) > i:
    print(my_str[i][:10:])
    i += 1
