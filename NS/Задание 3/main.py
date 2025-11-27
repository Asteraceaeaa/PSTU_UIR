import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


class Point:

    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def coords(self):
        return [self.x, self.y, self.z]


x1_0, x2_0, x3_0 = 0, 0, 0
O = Point(x1_0, x2_0, x3_0) #Инициализируем начало координат


""" Параметры модели """

v0 = 4e6 #м/с
B = 0.15 #Тл
q = 3.2e-19 #Кл
m = 6.7e-27 #Кг
alpha = 60 #Градусов

#Начальные координаты частицы
x1 = x2 = x3 = 0
R = Point(x1, x2, x3)









