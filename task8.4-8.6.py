import time


class Warehouse:
    current_complection = {}  # то, что сейчас на хранении на складе
    free_places = 25  # свободные места на складе
    degree_of_filling = 0  # степень заполнения склада в процентах

    @classmethod
    def status(cls):
        print(f'Сейчас на хранении - {Warehouse.current_complection} \n'
              f'Количество свободных мест - {Warehouse.free_places} мест \n'
              f'Степень заполнения - {Warehouse.degree_of_filling}%')


class Office_Equipment:
    adding = False
    of_eq_count = 0  # общее количество техники
    eq_list = {}  # словарь неоприходованной техники

    @classmethod
    def of_eq_quantity(cls):
        print(f'Неоприходованная техника - {Office_Equipment.eq_list}')

    def __init__(self, brand, model, year, quantity):
        self.brand = brand
        self.model = model
        self.year = year
        self.quantity = quantity
        Office_Equipment.adding = False

    def validate(self):
        try:
            if type(self.brand) == str:
                if 2015 <= int(self.year) <= 2020:
                    if int(self.quantity) >= 1:
                        print(f'Данные введены корректно')
                        Office_Equipment.adding = True
                    else:
                        print('Количество не может быть меньше единицы')
                else:
                    print('Год выпуска должен быть в пределах 2015-2020 года')
            else:
                print('Некорректное имя брэнда!')
        except:
            print('Введены некорректные данные, попробуйте еще раз!')


class Printer(Office_Equipment):
    eq_type = 'Printer'
    size = 1  # количество мест, которое занимает данный тип


class Scaner(Office_Equipment):
    eq_type = 'Scaner'
    size = 2  # количество мест, которое занимает данный тип


class Copy_machine(Office_Equipment):
    eq_type = 'Copy_machine'
    size = 3  # количество мест, которое занимает данный тип


pos_s = 0  # текущая позиция товара на складе
pos_k = 0  # текущая позиция товара в компании

while True:
    action = input('\nВведите действие, которое надо совершить:\n'
                   '"P" - Приход товара в компанию\n'
                   '"S" - Товары на складе\n'
                   '"K" - Товары в компании (неоприходованные)\n'
                   '"RS" - Переместить товар на склад из компании\n'
                   '"RK" - Переместить товар со склада в компанию\n'
                   '"Q" - Выход\n')
    if action.upper() == "S":
        Warehouse.status()
        continue
    if action.upper() == "K":
        Office_Equipment.of_eq_quantity()
        continue
    if action.upper() == "Q":
        Warehouse.status()
        time.sleep(3)
        Office_Equipment.of_eq_quantity()
        time.sleep(3)
        print('Bye Bye')
        break
    if action.upper() == "P":
        flag = False
        while True:
            if flag:
                break
            while True:
                eq_type = input('Выберите тип: "1" - Принтер \n"2" - Сканер \n "3" - Ксерокс\n')
                if eq_type == '1' or eq_type == '2' or eq_type == '3':
                    break
                else:
                    print('Выберите из предложенных вариантов')
            eq_name = input('Введите имя устройства')
            eq_brand = input('Введите марку оборудованиия')
            eq_model = input('Введите модель')
            eq_year = input('Введите год выпуска')
            eq_quantity = input('Введите количество')
            if eq_type == '1':
                eq_name = Printer(eq_brand, eq_year, eq_quantity)
            elif eq_type == '2':
                eq_name = Scaner(eq_brand, eq_year, eq_quantity)
            elif eq_type == '3':
                eq_name = Copy_machine(eq_brand, eq_year, eq_quantity)
            eq_name.validate()
            if Office_Equipment.adding:
                pos_k += 1
                Office_Equipment.eq_list.update({pos_k: (f'Марка - {eq_brand}, Модель - {eq_model}, Год выпуска '
                                                         f'- {eq_year}, Количество - {eq_quantity}')})
                print('Товар доставлен в компанию')
                Office_Equipment.of_eq_count += int(eq_quantity)
                Office_Equipment.of_eq_quantity()
                flag = True
                break