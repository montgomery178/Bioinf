import matplotlib.pyplot as plt
import random
import numpy as np
from math import sin
from matplotlib.pyplot import MultipleLocator


def func(x):
    return 2*x**3+2*x**2-x

rpoint=0
bpoint=0
gpoint=0

for i in range(7000):
    xi = np.random.uniform(-2,2) # выбраны значения для подсчета неопределенного интеграла
    yi = np.random.uniform(-10,26) # такие значения из-за того что func(min)=-6, func(max)=22

    if yi>=0 and yi<=(func(xi)):
        plt.plot(xi, yi, 'ro')
        rpoint += 1
    elif yi<=0 and yi>=(func(xi)):
        plt.plot(xi, yi, 'go')
        gpoint += 1
    else:
        plt.plot(xi, yi, 'bo')
        bpoint += 1

a=-2
b=2

for j in range(100):
    plt.plot([a+j*(b-a)/100, a+(j+1)*(b-a)/100], [func(a+j*(b-a)/100), func(a+(j+1)*(b-a)/100)],linewidth=3.0, color='cyan')
    

res1=144*rpoint/(rpoint+bpoint+gpoint) # 144 - площадь нашего квадрата
res2=144*gpoint/(gpoint+bpoint+rpoint)

plt.xlabel(f'Ось х \n Результат: {res1-res2}')
plt.ylabel('Ось y')
plt.grid()

ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

plt.xlim(-2,2)
plt.ylim(-10,26)
plt.show()


print(144*rpoint/(rpoint+bpoint+gpoint))
print(144*gpoint/(gpoint+bpoint+rpoint))

print(rpoint, gpoint, bpoint)

# Неопределенный интеграл искомой функции равен 10,(6). Подсчет по нашему способу выдает значения, достаточно близкие
# к нашему интегралу: 11,01; 10,56; 11,8; 10,77



