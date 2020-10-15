import math
import random


def derivative(f, x1):
    dx = 0.0001
    x2 = x1 + dx
    y1 = f(x1)
    y2 = f(x2)
    dy = y2 - y1
    return dy / dx


f = lambda x: - x ** 2 / 100 + 10 * math.sin(x)


print(
    derivative(f, 3)
)


def find_max(f):
    currentX = random.randint(-20, 20)
    for i in range(40):
        der = derivative(f, currentX)
        if der < 0:
            print('Oh, derivative is negative. We need to go to the left')
            currentX -= 0.1
            print(currentX)
        else:
            print('Oh, derivative is positive. We need to go to the right')
            currentX += 0.1
            print(currentX)


find_max(f)
