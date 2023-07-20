import numpy as np
import scipy.stats as stats

students_IQ = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
x = np.mean(students_IQ)
t = stats.t.ppf(0.975, len(students_IQ) - 1)
s = np.std(students_IQ, ddof=1)
print(x - t * (s / np.sqrt(len(students_IQ))), x + t * (s / np.sqrt(len(students_IQ))))
