import math
import numpy as np
import matplotlib.pyplot as plt

# первая часть домашнего задания


def f1(x):
    return math.sin(x)


def f2(x):
    return math.log(x)


def derivative(f, x1):
    y1 = f(x1)
    y2 = f(x1 + 0.0001)
    return y2 - y1 / 0.0001


def list_xs(f):
    list_of_xs = []
    for x in np.arange(0.001, 10, 0.01):
        list_of_xs.append(derivative(f, x))
    plt.plot(list_of_xs)
    return plt.savefig("charts.jpg")


list_xs(f1)
list_xs(f2)


# вторая часть домашнего задания


def f3(x, y):
    return math.cos(x) ** 2 - (y - 3) ** 2


def function_list():
    list_xy = []
    for y in np.arange(-10, 11, 0.01):
        for x in np.arange(-10, 11, 0.01):
            list_xy.append([x, y])
    return list_xy


def find_max(f, list_):
    list_values = []
    max_x_y = f(list_[0][0], list_[0][1])
    for x, y in list_:
        if f(x, y) > max_x_y:
            max_x_y = f(x, y)
            max_x = x
            max_y = y
            list_values.append([max_x, max_y])
    print(list_values[-10:])


find_max(f3, function_list())
