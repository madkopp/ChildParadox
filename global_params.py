import numpy as np


num_names = 5
names = {'female': list(range(1, num_names+1)),
         'male':   list(range(num_names+1, 2*num_names+1))}

num_kids_per_family = 2

num_families = 10000


def rand_wrapper(low, high, size=None):
    result = np.random.randint(low=low, high=high+1, size=size)

    return result