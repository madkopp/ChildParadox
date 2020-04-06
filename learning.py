import numpy as np
import matplotlib.pyplot as plt
import random


max_num = 3

'''
ints = []
for n in range(100000):
    ints.append(random.randint(1, max_num+2))
'''

ints = np.random.randint(low=1, high=max_num, size=100000)

'''
ints = []
for n in range(100000):
    m=1
    while m == 1:
        m = np.random.randint(low=1, high=max_num+2)
'''

print(ints[:100])

plt.hist(ints, np.arange(.5, max_num+1.5, 1))
plt.show()
