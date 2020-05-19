sp = []
i = 0
while True:
    el = input(f'Введите {i + 1}й элемент списка. Если элементов больше нет, введите "Cтоп" ')
    if el.lower() == 'стоп':
        break
    sp.append(el)
    i += 1
print(f'Введенный список из {len(sp)} элементов - {sp}')

i = 1
while i < len(sp):
    b = sp[i - 1]  # промежуточная переменная
    sp[i - 1] = sp[i]
    sp[i] = b
    i += 2
print(f'Измененный список из {len(sp)} элементов - {sp}')
