class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": [15000, 35000, 50000], "bonus": [15000, 25000, 40000]}


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник - {self.surname} {self.name}')

    def get_total_income(self):
        while True:
            if self.position.lower() == 'секретарь':
                total_salary = (self._income.setdefault("wage"))[0] + (self._income.setdefault("bonus"))[0]
                break
            elif self.position.lower() == 'проектировщик':
                total_salary = (self._income.setdefault("wage"))[1] + (self._income.setdefault("bonus"))[1]
                break
            elif self.position.lower() == 'руководитель':
                total_salary = (self._income.setdefault("wage"))[2] + (self._income.setdefault("bonus"))[2]
                break
            else:
                print('В компании только 3 должности: Секретарь, Проектировщик, Руководитель')
                self.position = input('Введите должность ')
                continue
        print(f'Позиция - {self.position}, суммарный доход в месяц - {total_salary}')


worker1 = Position(input('Введите имя '), input('Введите фамилию '), input('Введите должность '))
worker1.get_full_name()
worker1.get_total_income()
