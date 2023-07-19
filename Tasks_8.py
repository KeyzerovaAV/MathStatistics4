import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

a = np.array([12, 10, 11, 19, 13, 11, 17, 15, 19, 14, 21, 18, 21, 11, 17, 14, 15, 17, 20, 19])
b = np.array([11, 13, 18, 15, 17, 18, 10, 21, 26, 15, 11, 12, 15, 17, 10, 18, 18, 12, 21, 20])
print(stats.ttest_ind(a, b, equal_var = True))

s1 = np.std(a, ddof=1)
s2 = np.std(b, ddof=1)
x1 = np.mean(a)
x2 = np.mean(b)
t1_calculated = (x1 - x2) / np.sqrt(s1 ** 2 / len(a) + s2 ** 2 / len(b))
print(t1_calculated)

print(stats.ttest_ind(a, b, alternative = 'greater'))
print(stats.ttest_ind(a, b, alternative = 'less'))
print(stats.ttest_ind(a, b, alternative = 'two-sided'))

t_calculated = stats.t.ppf(1 - 0.8737549039369696 / 2, len(a) + len(b) - 2)
print(t_calculated)
t_tabulated = stats.t.ppf(1 - 0.05 / 2, len(a) + len(b) - 2)
print(t_tabulated)

# print(np.corrcoef(a, b))
# plt.scatter(a, b)
# plt.title('r = 0.01847613')
# plt.xlabel('a')
# plt.ylabel('b')
# plt.show()
