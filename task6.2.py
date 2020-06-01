class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        result = self._length * self._width * 25 * 5
        print(f'Вес дорожного полотна - {result / 1000} т')


highway1 = Road(8000, 20)
highway1.mass()
