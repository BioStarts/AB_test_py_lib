# coding=utf-8
# This is a sample Python script.

from scipy.stats import norm, chi2_contingency
import statsmodels.api as sm
import numpy as np

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = 135
    n1 = 1781
    s2 = 47
    n2 = 1443
    p1 = s1/n1
    p2 = s2/n2
    p = (s1 + s2) / (n1 + n2)
    z = (p2 - p1) / ((p * (1 - p) * ((1 / n1) + (1 / n2))) ** 0.5)

    p_value = norm.cdf(z)

    print(['{:.12f}'.format(a) for a in (abs(z), p_value * 2)])

    z1, p_value1 = sm.stats.proportions_ztest([s1, s2], [n1, n2])
    print(['{:.12f}'.format(b) for b in (z1, p_value1)])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
