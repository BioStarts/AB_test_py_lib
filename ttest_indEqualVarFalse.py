import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')

import os
os.chdir("files/Shad_Python_06_2")

# Хотим проверить что продолжительость жизни арситократов и императоров не отличается

df = pd.read_csv('agedeath.dat.txt', sep='\s+', header=None, names=['group', 'age', 'index'])
print(df.head()) # выводим первые 5 значений таблицы из файла

x = df[df['group'] == 'sovr']['age']
y = df[df['group'] == 'aris']['age']
x.name, y.name = 'sovr', 'aris'

# проверяем нормальность
# Функции определяются так.
# После определения функции полезно ее описание добавить в таком стиле.
# Тройные кавычки -- для обрамления многострочных строковых литералов.
# Функция которая построит 2 гистограммы на одной картинке и выведет средние значения по ним

def two_histograms(x, y):
    x.hist(alpha=0.5, weights=[1./len(x)]*len(x))
    y.hist(alpha=0.5, weights=[1./len(y)]*len(y))
    plt.axvline(x.mean(), color='red', alpha=0.8, linestyle= 'dashed')
    plt.axvline(y.mean(), color='blue', alpha=0.8, linestyle= 'dashed')
    plt.legend([x.name, y.name])
    plt.show()

two_histograms(x,y)

#данные условно нормальны. Проверим с помощью критерия Флигнера-Килина, равны ли дисперсии

res = stats.fligner(x, y)
print('p_value', res[1])

# Гипотезу о равенстве дисперсий отвергаем, т.к. p_value низкое. В 2х выборках находятся разные наблюдаемые объекты
# то есть выборки несвязные. Итого гипотезу о равенстве средних значений будем проверять
# с помощью ttest_ind c equal_var=False

res = stats.ttest_ind(x, y, equal_var=False)
print('p_value', res[1])

# вывод гипотезу равенста отвергаем (p_value меньше alpha), значит аристократы живут дольше


