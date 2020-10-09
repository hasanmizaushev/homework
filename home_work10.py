import math
import random


def f(x):
    return (x / 10) * 3 * math.sin(2 * x)


def f2(x):
    return x * 4 - x * 3 + x - 1


def derivative(f, x1):
    dx = 0.0001
    x2 = x1 + dx
    y1 = f(x1)
    y2 = f(x2)
    dy = y2 - y1
    return dy / dx


def find_min_1(f):
    currentX = random.randint(-50, 50)
    print("example for function number 1")
    for i in range(40):
        der = derivative(f, currentX)
        if der < 0:
            print('Oh, derivative is negative. We need to go to the right')
            currentX += 0.01
            print(currentX)
        else:
            print('Oh, derivative is positive. We need to go to the left')
            currentX -= 0.01
            print(currentX)


def find_min_2(f2):
    currentX = random.randint(-50, 50)
    print("example for function number 2")
    for i in range(40):
        der = derivative(f2, currentX)
        if der < 0:
            print('Oh, derivative is negative. We need to go to the right')
            currentX += 0.01
            print(currentX)
        else:
            print('Oh, derivative is positive. We need to go to the left')
            currentX -= 0.01
            print(currentX)


find_min_1(f)
find_min_2(f2)
