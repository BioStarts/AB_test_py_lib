import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')

import os
os.chdir("files/Shad_Python_06_2")

# Хотим проверить что скорость чтения названий цветов в зависимости от цвета шрифта которым напсиано слово (1935 исследование)

df = pd.read_csv('interference.csv')
print(df.head()) # выводим первые 5 значений таблицы из файла

x = df['DiffCol']
y = df['Black']
x.name, y.name = 'DiffCol', 'Black'

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
#    plt.show()

two_histograms(x,y)

# данные условно нормальны. Поскольку в выборках содержатся одни и те же люди, которые читали различные шрифты
# значит выборки у нас связные, а занчит используем ttest_rel

res = stats.ttest_rel(x, y)
print('p_value', res[1])

# 0.01 < p_value < 0.05 - спорный момент. Считаю что можем утвержадать что разница в реакции есть.
