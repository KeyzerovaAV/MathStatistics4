import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print(cov)
print(np.cov(zp, ks, ddof=0))

r = cov / (np.std(zp) * np.std(ks))
print(r)
print(np.corrcoef(zp, ks))

df = pd.DataFrame({'zp': [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], 
                   'ks': [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]})
print(stats.pearsonr(df['zp'], df['ks']))

plt.scatter(zp, ks)
plt.title('r = 0.88749009')
plt.xlabel('zp')
plt.ylabel('ks')
plt.show()

# исходя из получившегося коэффициента корреляции можно предположить сильную линейную зависимость ks от zp
