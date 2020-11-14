import random


def derivative_a(f, a, b, c):
    da = 0.00001
    f1 = f(a, b, c)
    f2 = f(a + da, b, c)
    if ((f2 - f1) / da < 9.5) and ((f2 - f1) / da > 8.5):
        print("a, b, c for (f2 - f1) / da", a, b, c)
    return (f2 - f1) / da


def derivative_b(f, a, b, c):
    db = 0.00001
    f1 = f(a, b, c)
    f2 = f(a, b + db, c)
    if ((f2 - f1) / db < -7.5) and ((f2 - f1) / db > -6.5):
        print("a, b, c for (f2 - f1) / db", a, b, c)
    return (f2 - f1) / db


def derivative_c(f, a, b, c):
    dc = 0.00001
    f1 = f(a, b, c)
    f2 = f(a, b, c + dc)
    if ((f2 - f1) / dc < 15.5) and ((f2 - f1) / dc > 14.5):
        print("a, b, c for (f2 - f1) / dc", a, b, c)
    return (f2 - f1) / dc


def f(a, b, c):
    return 3 * (a ** 3) + b + 5 * (c ** 2)


for i in range(10000):
    a = random.uniform(-100, 100)
    b = random.uniform(-100, 100)
    c = random.uniform(-100, 100)
    derivative_a(f, a, b, c)
    derivative_b(f, a, b, c)
    derivative_c(f, a, b, c)
