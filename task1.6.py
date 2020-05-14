while True:
    start = int(input('Введите результат спортсмена за 1-й день в км '))
    if start > 0:
        break

while True:
    finish = int(input('Введите конечный результат спортсмена в км '))
    if finish > 0:
        break
    else:
        print('Конечный результат должен быть больше стартового!')

day = 1
result = start
print(f'Результат за {day}-й день: {result:.2f} км')

while True:
    day += 1
    result = result * 1.1
    print(f'Результат за {day}-й день: {result:.2f} км')
    if result >= finish:
        print(f'Конечный результат - {finish} км достигнут на {day}-й день')
        break