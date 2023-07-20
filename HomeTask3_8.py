import numpy as np
import scipy.stats as stats

x = 174.2
z = stats.norm.ppf(0.975)
s = np.sqrt(25)
n = 27
print(x - z * (s / np.sqrt(n)), x + z * (s / np.sqrt(n)))
