#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
вычисления углов, вычисления периметра. Создать производный класс RightAngled
(прямоугольный), имеющий поле площади. Определить метод вычисления площади.
"""

from math import acos, degrees


class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def side_a(self):
        return self.__a

    @side_a.setter
    def side_a(self, a):
        if a > 0:
            self.__a = a
        else:
            raise ValueError

    @property
    def side_b(self):
        return self.__b

    @side_b.setter
    def side_b(self, b):
        if b > 0:
            self.__b = b
        else:
            raise ValueError()

    @property
    def side_c(self):
        return self.__c

    @side_c.setter
    def side_c(self, c):
        if c > 0:
            self.__c = c
        else:
            raise ValueError()

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def angle(self):
        ab = acos((self.__c ** 2 - self.__a ** 2 - self.__b ** 2) / (-2 * self.__a * self.__b))
        bc = acos((self.__a ** 2 - self.__b ** 2 - self.__c ** 2) / (-2 * self.__b * self.__c))
        ac = acos((self.__b ** 2 - self.__a ** 2 - self.__c ** 2) / (-2 * self.__a * self.__c))
        return degrees(ab), degrees(bc), degrees(ac)


class RightAngled(Triangle):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.__s = 0

    def square(self):
        self.__s = 0.5 * self.side_a * self.side_b
        return self.__s


if __name__ == "__main__":
    tr1 = Triangle(3, 4, 5)
    tr2 = RightAngled(4, 6, 3)
    print(f"Периметр: {tr1.perimeter()}")
    angles = tr1.angle()
    print(f"Углы треугольника:\nAB = {angles[0]:.1f}\n"
          f"BC = {angles[1]:.1f}\nAC = {angles[2]:.1f} ")
    print(f"Площадь: {tr2.square()}")
