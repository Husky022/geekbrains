import time
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Скорость автомобиля - {self.name} ({self.color} цвет) - {self.speed} км/ч')

    def go(self):
        print(f'Автомобиль {self.name} ({self.color} цвет) завелся и поехал')

    def stop(self):
        print(f'Автомобиль {self.name} ({self.color} цвет) остановился и заглушил мотор')

    def turn(self, direction):
        print(f'{self.name} ({self.color} цвет) движется в направлении - {direction}')

class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Автомобиль - {self.name} ({self.color} цвет) движется с превышением скорости'
                  f' на ({int(self.speed) - 60} км/ч) при разрешенных 60 км/ч')
        else:
            print(f'Скорость автомобиля - {self.name} ({self.color} цвет) - {self.speed} км/ч')


class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Автомобиль - {self.name} ({self.color} цвет) движется с превышением скорости'
                  f' на ({int(self.speed) - 40} км/ч) при разрешенных 40 км/ч')
        else:
            print(f'Скорость автомобиля - {self.name} ({self.color} цвет) - {self.speed} км/ч')

class PoliceCar(Car):

    def siren(self):
        print('UUUUIIIIIIUUUUUUUIIIIIIUUUIIIIIII ("Звук сирены")')


auto1 = TownCar(input('Введите скорость '), input('Введите цвет '),
                  input('Введите имя авто '), input('Это полицейская машина? '))
auto1.go()
time.sleep(2)
auto1.turn(input('Куда едем '))
time.sleep(2)
try:
    auto1.siren()
except AttributeError:
    pass
time.sleep(2)
auto1.show_speed()
time.sleep(2)
auto1.stop()

auto2 = PoliceCar(input('Введите скорость '), input('Введите цвет '),
                  input('Введите имя авто '), input('Это полицейская машина? '))
auto2.go()
time.sleep(2)
auto2.turn(input('Куда едем '))
time.sleep(2)
try:
    auto2.siren()
except AttributeError:
    pass
time.sleep(2)
auto2.show_speed()
time.sleep(2)
auto2.stop()

auto3 = WorkCar(input('Введите скорость '), input('Введите цвет '),
                  input('Введите имя авто '), input('Это полицейская машина? '))
auto3.go()
time.sleep(2)
auto3.turn(input('Куда едем '))
time.sleep(2)
try:
    auto3.siren()
except AttributeError:
    pass
time.sleep(2)
auto3.show_speed()
time.sleep(2)
auto3.stop()
