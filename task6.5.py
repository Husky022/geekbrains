class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Ручка {self.title} - Запуск отрисовки')

class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} - Запуск отрисовки')

class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} - Запуск отрисовки')


Pen1 = Pen('Гелевая')
Pen1.draw()
Pencil1 = Pencil('Kohinoor')
Pencil1.draw()
Handle1 = Handle('Черный')
Handle1.draw()