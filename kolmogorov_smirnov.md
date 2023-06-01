Так как у биоинформатиков не экспериментальных данных, то было бы очень увлекательно узнать правда ли, что среди соревнований по спидкуберству, где записывается время сборки кубика Рубика, имеет место быть равномерное распределение!

Данные брались здесь "https://galileo24.ru/mirovie-rekordy-po-sborke-kubika-rubika". Всего 32 рекорда

```
import matplotlib.pyplot as plt

ntries = 32
experiments = [3.47,4.22,4.59,4.59,4.69,4.73,4.74,4.90,5.09,5.25,5.55,5.66,6.18,6.24,6.65,6.65,7.03,7.08,8.72,8.72,9.18,10.36,10.48,11.13,11.75,12.11,13.93,14.76,15.07,16.53,16.71,22.95]

plt.bar(list(range(ntries)), experiments)
plt.title('Experimental data')
plt.show()
```
Мы получили график. Не удивительно, что он плавный... А теперь запишем все в формат csv

```
import pandas

df = pandas.DataFrame(data={
    'experiments': experiments
})

df.to_csv("experiments.csv")
```
А как выглядит распределение?
```
df1 = pandas.DataFrame(data={
    'df': df['experiments']
})

df1.plot.kde()
plt.show()

from scipy import stats

d = df1['df']
```
Немного криво, но рисунок же похож?

```
print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=5000))
print()

print(stats.kstest(d, 'norm', (d.mean(), d.std()), N=5000))
```
В итоге получаем результат "KstestResult(statistic=0.20110589767938003, pvalue=0.1305316807447675)", первое маленькое и второе значение меньше первое. Значит это сложно наззвать нормальным распределением

