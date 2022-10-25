# Создадим собственную функцию для косинуса

import math

ITERATIONS = 20

def my_cos(x):
    """
    Вычисление косинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = 1
    multiplier = 1
    partial_sum = 1
    for n in range(1, ITERATIONS):
        x_pow *= x**2  # В цикле постепенно считаем степень
        multiplier *= -1 / (2*n-1) / (2*n)  # (-1)^n и факториал
        partial_sum += x_pow * multiplier
    
    return partial_sum

help(math.cos)
help(my_cos)

print(math.cos(0.4))
print(my_cos(0.4))

# Сравниваем работу нашей функции с библиотечной

import cmath

complex_angle = cmath.acos(5)
print('"Угол", на котором косинус достигает пяти:', complex_angle)

print("Достигает ли пяти наш косинус?", my_cos(complex_angle))
print("А библиотечный?", cmath.cos(complex_angle))

# Где слабое место у нашего косинуса?

import matplotlib.pyplot as plt

# Построим и сравним графики

import matplotlib.pyplot as plt
import numpy as np

vs = np.vectorize(my_cos)
print(my_cos, vs)

angles = np.r_[-16.25:16.25:0.01]
plt.plot(angles, np.cos(angles), linewidth=3.0, color='cyan')
plt.plot(angles, vs(angles), linewidth=1.0, color='black')
plt.show()
