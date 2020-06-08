class Cell:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        new_cell_size = self.size + other.size
        new_cell = Cell(new_cell_size)
        return new_cell

    def __sub__(self, other):
        new_cell_size = self.size - other.size
        if new_cell_size < 0:
            return 'Действие невозможно! Вычитаемая клетка больше исходной!'
        new_cell = Cell(new_cell_size)
        return new_cell

    def __mul__(self, other):
        new_cell_size = self.size * other.size
        new_cell = Cell(new_cell_size)
        return new_cell

    def __truediv__(self, other):
        new_cell_size = self.size / other.size
        if new_cell_size < 1:
            return 'Действие невозможно! Исходная клетка должна быть больше чем делитель!'
        new_cell = Cell(round(new_cell_size))
        return new_cell

    def make_order(self, line_size):
        a = ''
        i = 0
        while True:
            j = 0
            while j < line_size:
                a += '*'
                i += 1
                j += 1
                if i == self.size:
                    return a
                    break
            a += '\n'


cell_1 = Cell(22)
cell_2 = Cell(10)
print((cell_1 + cell_2).make_order(4))
print()
print((cell_1 - cell_2).make_order(4))
print()
print((cell_1 * cell_2).make_order(4))
print()
print((cell_1 / cell_2).make_order(4))
print()