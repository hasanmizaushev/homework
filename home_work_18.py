import pandas as pd
import random
import math


df = pd.read_csv('yandex_data.csv')
# print(df.head())


def f(a, b, c, x):
    ea = random.uniform(-0.001, 0.001)
    eb = random.uniform(-0.001, 0.001)
    ec = random.uniform(-0.001, 0.001)
    return ((a + ea) * math.sin(x) + (b + eb) * math.log(x)) ** 2 + (c + ec) * (x ** 2)


def error(f, a, b, c, x, y_true):
    y_pred = f(a, b, c, x)
    return abs(y_pred - y_true)


def der_a(f, a, b, c, x, y_true):
    e1 = error(f, a, b, c, x, y_true)
    e2 = error(f, a + 0.00001, b, c, x, y_true)
    return (e2 - e1) / 0.00001


def der_b(f, a, b, c, x, y_true):
    e1 = error(f, a, b, c, x, y_true)
    e2 = error(f, a, b + 0.00001, c, x, y_true)
    return (e2 - e1) / 0.00001


def der_c(f, a, b, c, x, y_true):
    e1 = error(f, a, b, c, x, y_true)
    e2 = error(f, a, b, c + 0.00001, x, y_true)
    return (e2 - e1) / 0.00001


a, b, c = 2, 3, 1
lr = 0.001
for i in range(1):
    for _, row in df.iterrows():
        da = der_a(f, a, b, c, row[0], row[1])
        db = der_b(f, a, b, c, row[0], row[1])
        dc = der_c(f, a, b, c, row[0], row[1])
        a -= lr * da
        b -= lr * db
        c -= lr * dc
print(a, b, c)


# Error function # Learning rate # a, b, c (after one data frame iteration)
# squared        # 0.1           # -5.287798479258273e+17; 6.065815069654868e+18; 1.5161261817854886e+18
# squared        # 0.01          # -19646341115836.65; 597125437463505.5; 604614265827139.5
# squared        # 0.001         # 1.5474250491067252e+29; -6.969457350078336e+28; 5.548969512031147e+28
# absolute       # 0.1           # 5507533748044283.0; -23890353749029.5; -6579655098395.413
# absolute       # 0.01          # 1.7887972643369886e+16; -8821812245320.598; 355794569991560.9
# absolute       # 0.001         # -11663035650.824463; 5427250150.7102585; -558922385224.5458
