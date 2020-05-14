revenue = int(input("Укажите сумму выручки Вашей компании "))
cost = int(input("Укажите сумму издержек Вашей компании "))
profit = revenue - cost

if profit < 0:
    print(f'Ваша компания работает в убыток. \nУбыток компании равен {profit}')
elif profit == 0:
    print('Выручка Вашей компании равна издержкам')
else:
    persons = int(input("Укажите количество сотрудников в Вашей компании "))
    profitability = (profit / revenue) * 100
    prof_per_person = profit / persons
    print(f' Прибыль Вашей компании - {profit:.2f} руб.\n'
          f' Рентабельность Вашей компании - {profitability:.2f} %\n'
          f' Прибыль на одного сотрудника - {prof_per_person:.2f} руб.' )
