import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
matplotlib.style.use('ggplot')

# В регионе ожидаются выборы. В городе в поддержку кандидата высказалось 28% из 100 опрошеных и
# 20% из 100 опрошеных в селе. Хотим выснить является ли эта разница стат значимой. И нужно ли разворачивать
# доп рекламную кампанию на селе. Проверять будем через хи-квадрат. Для начала строим таблицу сопряженности

contingency_table = pd.DataFrame([[28,72],[20,80]], index=['city', 'country'], columns=['for', 'against'])
print(contingency_table)

res = stats.chi2_contingency(contingency_table)
print('p_value', res[1])

# p_value получился достаточно большим поэтому оснований отвергнуть гипотезу об однородности(равенсте долей) нет
