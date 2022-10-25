#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math # импорт библиотеки math для использования sin
import numpy # импорт библиотеки numpy 
import matplotlib.pyplot as mpp # импорт библиотеки matplotlib для черчения графика

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': # __main__ это область видимости, где выполняется код. таким образом данная стррока верна, если программа запущена напрямую
    arguments=numpy.arange(0,200,0.1) #задает измененные аргументы
    mpp.plot( 
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    ) # построение графика видоизмененного синуса
    mpp.show() # показ полученного графика
