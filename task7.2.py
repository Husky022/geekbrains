from abc import ABC, abstractmethod


def expense_info():
    return f'Общий расход ткани - {Clothes.total_expense}'


class Clothes(ABC):
    total_expense = 0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def expense(self):
        expense = round((self.size / 6.5 + 0.5), 2)
        Clothes.total_expense += expense
        return f'Расход ткани - {expense}'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 44:
            self.__size = 44
            print('Взят минимально возможный размер - 44')
        elif size > 58:
            self.__size = 58
            print('Взят максимально возможный размер - 58')
        else:
            self.__size = size
            print(f'Взят размер - {self.__size}')


class Suit(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def expense(self):
        expense = round((2 * self.height + 0.3), 2)
        Clothes.total_expense += expense
        return f'Расход ткани - {expense}'

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1.45:
            self.__height = 1.45
            print('Взят минимально возможный рост - 1.45')
        elif height > 2.15:
            self.__height = 2.15
            print('Взят максимально возможный рост - 2.15')
        else:
            self.__height = height
            print(f'Взят рост - {self.__height}')


coat1 = Coat('chester', 40)
print(coat1.expense())
print(expense_info())
suit1 = Suit('cowboy', 1.8)
print(suit1.expense())
print(expense_info())
