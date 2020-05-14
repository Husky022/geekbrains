while True:
    number = int(input('Введите любое положительное число '))
    if number >= 0:
        break

max_figure = 0

while (number // 10) != 0:
    n = number % 10
    number = number // 10
    if n == 9:
        max_figure = n
        break
    if n >= max_figure:
        max_figure = n

print(f"Наибольшая цифра в введенном числе - {max_figure}")