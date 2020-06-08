class Matrix:
    def __init__(self, el):
        self.el = el

    def __add__(self, other):
        if len(self.el) != len(other.el) or len(self.el[0]) != len(other.el[0]):
            return 'Матрицы разного размера!'
        new_matrix = self.el
        try:
            for i in range(len(self.el)):
                for j in range(len(self.el[i])):
                    new_matrix[i][j] = self.el[i][j] + other.el[i][j]
            return Matrix(new_matrix)
        except TypeError:
            return 'Ошибка в элементах матрицы. Могут быть только числа!'

    def __str__(self):
        a = ''
        for i in range(len(self.el)):
            for j in range(len(self.el[i])):
                a += str(self.el[i][j])
                a += ' '
            a += '\n'
        return a


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
