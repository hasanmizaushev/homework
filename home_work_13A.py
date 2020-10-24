def derivative_a(f, a, b, c):
    da = 0.00001
    f1 = f(a, b, c)
    f2 = f(a + da, b, c)
    return (f2 - f1) / da


def derivative_b(f, a, b, c):
    db = 0.00001
    f1 = f(a, b, c)
    f2 = f(a, b + db, c)
    return (f2 - f1) / db


def derivative_c(f, a, b, c):
    dc = 0.00001
    f1 = f(a, b, c)
    f2 = f(a, b, c + dc)
    return (f2 - f1) / dc


def f(a, b, c):
    return 3 * (a ** 3) + b + 5 * (c ** 2)


print(derivative_a(f, 9, -7, 15))
print(derivative_b(f, 9, -7, 15))
print(derivative_c(f, 9, -7, 15))
