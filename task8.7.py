class Complex:
    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def __add__(self, other):
        return f'Сумма - {self.real_num + other.real_num} + {self.imaginary_num + other.imaginary_num}j'

    def __mul__(self, other):
        return f'Произведение - {self.real_num * other.real_num - self.imaginary_num * other.imaginary_num} ' \
               f'+ {self.imaginary_num * other.real_num + self.real_num * other.imaginary_num}j'


cmplx_1 = Complex(5, 10)
cmplx_2 = Complex(12, -3)
print(cmplx_1 + cmplx_2)
print(cmplx_1 * cmplx_2)