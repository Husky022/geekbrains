with open("text_3.txt", "r", encoding="utf-8") as workers_salary:
    salary = workers_salary.readlines()
    salary_list = []
    workers_list = []
    for el in salary:
        salary_list.append(float(el.split()[1]))
        workers_list.append(el.split()[0])
    low_salary_list = []
    low_salary_workers = []
    i = 0
    while i < len(salary_list):
        if salary_list[i] <= 20000.0:
            low_salary_list.append(salary_list[i])
            low_salary_workers.append(workers_list[i])
        i += 1
    print('Список сотрудников с окладом менее 20000.0 руб.')
    i = 0
    while i < len(low_salary_workers):
        print(f'{i + 1}: {low_salary_workers[i]} - {low_salary_list[i]} руб.')
        i += 1
    salary_sum = 0
    for el in salary_list:
        salary_sum += el
    mid_salary = salary_sum / len(salary_list)
    print(f'\nСредняя зарплата в компании - {mid_salary} руб.')
