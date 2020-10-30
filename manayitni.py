import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')

import os
os.chdir("files/Shad_Python_06_2")

df = pd.read_csv('Albuquerque/Albuquerque Home Prices_data.txt', sep='\t')
# print(df.head()) # выводим первые 5 значений таблицы из файла
# хотим проверить что цену домов на углу COR = 1 отличаются от других домов COR = 0. Хотим применить t критерий стьюдента,
# предварительно проверив 1. Нормальность данных 2. Равенство Дисперсий

df = df.replace(-9999, np.nan) # говорим что -9999 это на самом деле пропущенные данные
print(df.head()) # выводим первые 5 значений таблицы из файла

x = df[df['COR'] == 1]['PRICE']
y = df[df['COR'] == 0]['PRICE']
x.name, y.name = 'corner', 'not corner'

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

# исходя из гистограмм можем сказать что критерий стьюдента здесь не применим (убирание выбросов не поможет).
# можем попробовать непараметрические криетрии: Уилкоксона применим только для парных выборок
# (у нас же разные дома), тогда нам остается только критерий Мана Уитни
# идея сравнивать по средним арифметическим не прошла значит сравниваем медианы по Мана Уитни

res = stats.mannwhitneyu(x, y)
print('p_value', res[1])

# p value достаточно большой > альфа (0.05) => гипотезу (о равенстве) не отвергаем


# еще один тест на тех же данных (Северовосток vs все остальные)
x2 = df[df['NE'] == 1]['PRICE']
y2 = df[df['NE'] == 0]['PRICE']
x2.name, y2.name = 'NE', 'not NE'

two_histograms(x2, y2)

res2 = stats.median_test(x2, y2)
print('p_value', res2[1])

