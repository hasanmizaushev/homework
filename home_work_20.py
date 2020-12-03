import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1 / (1 + math.e ** -x)


def derivative(f, x1):
    y1 = f(x1)
    y2 = f(x1 + 0.0001)
    return (y2 - y1) / 0.0001


Xs = np.arange(-10, 10, 0.01)
Ys = [derivative(f, i) for i in Xs]
plt.plot(Xs, Ys)
plt.savefig("sigmoid_der.jpg")

print(derivative(f, 0.5))


def transform(x):
    if x == 0:
        return 0.5
    if x < 0:
        return 0.5 - (x * 0.003)
    else:
        return 0.5 + (x * 0.003)


print(transform(3))

x = 0
while True:
    if round(f(x), 2) == 0.75:
        break
    else:
        x += 0.1
print(x)
