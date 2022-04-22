#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать абстрактный базовый класс Function (функция) с виртуальными методами
вычисления значения функции y = f(x) в заданной точке и вывода результата на экран.
Определить производные классы Ellipse (эллипс), Hyperbola (гипербола) с
собственными функциями вычисления у в зависимости от входного параметра.
Уравнение эллипса x^2/a^2 + y^2/b^2 = 1; гиперболы: x^2/a^2 - y^2/b^2 = 1
"""

from abc import ABC, abstractmethod
from math import sqrt


class Function(ABC):

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def display(self):
        pass


class Ellipse(Function):

    def __init__(self, a, b, x):
        self.__a = a
        self.__b = b
        self.__x = x
        self.__y = None

    def solve(self):
        if self.__a == 0:
            raise ValueError()

        self.__y = sqrt(1 + (self.__x ** 2 / self.__a ** 2) * self.__b ** 2)

    def display(self):
        return self.__y


class Hyperbola(Function):

    def __init__(self, a, b, x):
        self.__a = a
        self.__b = b
        self.__x = x
        self.__y = None

    def solve(self):
        if self.__a == 0:
            raise ValueError()

        y = 1 - (self.__x ** 2 / self.__a ** 2) * self.__b ** 2
        if y >= 0:
            self.__y = sqrt(y)
        else:
            raise ArithmeticError("При данных значениях функция не имеет решения")

    def display(self):
        return self.__y


if __name__ == "__main__":
    e1 = Ellipse(1, 2, 7)
    h1 = Hyperbola(22, 7, 2)
    e1.solve()
    print(e1.display())
    h1.solve()
    print(h1.display())
