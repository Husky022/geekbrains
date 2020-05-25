from sys import argv

try:
    name, hours, salary_per_hour, prize = argv
    salary = int(hours) * int(salary_per_hour) + int(prize)
    print(f'Зарплата сотрудника - {salary} руб.')
except:
    print(f'Введены не все данные! (Введите через пробел "количество часов", "ставку" и "премию")')
