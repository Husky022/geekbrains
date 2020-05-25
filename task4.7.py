from math import factorial

def fact(n):
    for i in range(0, n + 1):
        yield factorial(i)


for el in fact(int(input('Введите число - '))):
    print(el)

