import numpy as np
import math

f = lambda x: (x-0.1) * (x-0.1) / 10 + math.sin(3 * x)
l = np.arange(-10, 10, 0.0001)


def find_min(f, l):
    min_x = l[0]
    _min = f(l[0])
    for val in l:
        if f(val) < _min:
            _min = f(val)
            min_x = val
    print(min_x, _min)


find_min(f, l)


f2 = lambda x: math.sin(x) + math.sqrt(math.fabs(x-5))
l2 = np.arange(-20, 15, 0.0001)


def find_max(f, l):
    max_x = l[0]
    _max = f(l[0])
    for val in l:
        if f(val) > _max:
            _max = f(val)
            max_x = val
    print(max_x, _max)


find_max(f2, l2)