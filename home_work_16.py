import pandas as pd
import math


df = pd.read_csv('hw16.csv').set_index('Unnamed: 0')
print(df.head())


def f(a, b, x):
    return a * math.sin(b * x)


def error(f, a, b, x, y_true):
    y_pred = f(a, b, x)
    return abs(y_pred - y_true)


def der_a(f, a, b, x, y_true):
    e1 = error(f, a, b, x, y_true)
    e2 = error(f, a + 0.00001, b, x, y_true)
    return (e2 - e1) / 0.00001


def der_b(f, a, b, x, y_true):
    e1 = error(f, a, b, x, y_true)
    e2 = error(f, a, b + 0.00001, x, y_true)
    return (e2 - e1) / 0.00001


a, b = 20, 1
lr = 0.0001
for i in range(1):
    for _, row in df.iterrows():
        da = der_a(f, a, b, row[0], row[1])
        db = der_b(f, a, b, row[0], row[1])
        a -= lr * da
        b -= lr * db
print(a, b)


# learning rate # Start random point (a, b) # Result point (x, y)
# 0.0001        # 1, 1                      # 0.04786395651887093, 1.025372843098677
# 0.0001        # 9, 6                      # 7.095707975176135, 7.291706119773459
# 0.0001        # 2, 4                      # 0.12901172483495008, 4.151179741892127
# 0.0001        # 5, 11                     # 3.101187486203238, 11.095886548148446
# 0.0001        # 20, 1                     # 18.12502483072319, 2.0082924436665017
