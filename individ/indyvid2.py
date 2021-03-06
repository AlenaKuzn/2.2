#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вариант 7

from math import sqrt

if __name__ == '__main__':
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))

    d = b * b - 4 * a * c

    if d > 0:
        t1 = (-b - sqrt(d)) / (2 * a)
        t2 = (-b + sqrt(d)) / (2 * a)
        if t1 >= 0:
            x1 = sqrt(t1)
            x2 = -sqrt(t1)
        if t2 >= 0:
            x3 = sqrt(t2)
            x4 = -sqrt(t2)
        print("Корни уравнения: ", x1, x2, x3, x4)

    if d == 0:
        x1 = sqrt(-b / 2 * a)
        x2 = -sqrt(-b / 2 * a)
        print("Корни уравнения: ", x1, x2)

    if d < 0:
        print("Корней нет")