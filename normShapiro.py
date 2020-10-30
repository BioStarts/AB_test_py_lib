import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')

import os
os.chdir("files/Shad_Python_06_2")

df = pd.read_csv('town_1959_2.csv', encoding='cp1251')
df = df.set_index(u'номер')

plt.hist(np.log10(df[u'население']))
# plt.show() # сохраняем гистограмму в директории и сразу выводим
# plt.savefig('myfig.png' ) # сохраняем гистограмму картинкой в ди ректорию выше

res = stats.shapiro(np.log10(df[u'население']))
print('p_value: ', res[1])

# критерий шапиро отвергает гипотезу нормальности (p_value < альфа = 0.05 - по умаочанию)
# увеличим количество столбцов и увилим что есть 3 выброса

plt.hist(np.log10(df[u'население']), bins=50)
# plt.show() # сохраняем гистограмму в директории и сразу выводим




