# TODO Написать 3 класса с документацией и аннотацией типов
import random
import doctest
import math

class Right_triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    def corners(self)->list:
        """Возвращает список углов треугольника
        >>> corn = Right_triangle(3, 4, 5)
        >>> corn.corners()"""
        return [math.pi / 2, math.acos(self.a / self.c), math.acos(self.b / self.c)]
    def area(self)->float:
        """Возвращает площадь треугольника
        >>> corn = Right_triangle(3, 4, 5)
        >>> corn.area()"""
        return 0.5 * self.a * self.b
class Complex:
    def __init__(self, real: float, image: float):
        self.real = real
        self.image = image
    def module(self)->float:
        """Вычисляет длину вектора комплексного числа
        return: модуль вектора
        >>> numb = Complex(4, 4)
        >>> numb.module()
        """
        return (self.real ** 2 + self.image ** 2) ** 0.5
    def create_fi(self)->float:
        """Вычисляет и возвращает угол в радианах между вектором комплекчного
        числа и вещественной состовляющей
        >>> numb = Complex(4, 4)
        >>> numb.create_fi()"""
        return math.acos(self.real / self.module())
class Matrix:
    def __init__(self, weight: int, height: int):
        self.weight = weight
        self.height = height
        self.matrix = self.create_matrix()
    def create_matrix(self)->list:
        """Создает и возвращает структуру матрицы"""
        return [[None for j in range(self.weight)] for i in range(self.height)]
    def fill_random(self, value: int)->list:
        """Заполняет матрицу рандомными числами типа
        int в интервале от 0 до value.
        return: заполненная матрица
        >>> matr = Matrix(3, 3)
        >>> matr.fill_random(10)
        '[[6, 9, 8], [5, 8, 5], [7, 8, 0]]'
        """
        for i in range(self.weight):
            for j in range(self.weight):
                self.matrix[i][j] = random.randint(0, int(value))
        return self
    def create_naturalle(self)->list:
        """Делает матрицу единичной.
        return: единичная матрица
        >>> matr = Matrix(3, 3)
        >>> matr.create_naturalle()
        '[[1, 0, 0], [0, 1, 0], [0, 0, 1]]'"""
        for i in range(self.weight):
            for j in range(self.weight):
                if i == j:
                    self.matrix[i][j] = 1
                else:
                    self.matrix[i][j] = 0
        return self

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
