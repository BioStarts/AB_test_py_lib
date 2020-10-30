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
# хотим проверить Корреляцию цены и площади домов в Альбукерке

df = df.replace(-9999, np.nan) # говорим что -9999 это на самом деле пропущенные данные
print(df.head()) # выводим первые 5 значений таблицы из файла

x = df[df['COR'] == 1]['PRICE']
y = df[df['COR'] == 0]['PRICE']
x.name, y.name = 'corner', 'not corner'

plt.scatter(df['PRICE'], df['SQFT'])
plt.show()

res = stats.pearsonr(df['PRICE'], df['SQFT']) # проверяем гипотезу что кореляция = 0
print('Pearson rho: ', res[0])
print('p_value: ', res[1]) # корреляция есть, гипотезу не принимаем

