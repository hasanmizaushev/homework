import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data.csv')
df.head()


def recall(df):
    _TP = TP(df)
    _FN = FN(df)
    if _TP == 0:
        return 0
    return _TP / (_TP + _FN)


def precision(df):
    _TP = TP(df)
    _FP = FP(df)
    if _TP == 0:
        return 0
    return _TP / (_TP + _FP)


def TP(df):
    tmp = df[(df["y_pred"] == 1) & (df["y_true"] == 1)]
    return len(tmp) / len(df)


def TN(df):
    tmp = df[(df["y_pred"] == 0) & (df["y_true"] == 0)]
    return len(tmp) / len(df)


def FP(df):
    tmp = df[(df["y_pred"] == 1) & (df["y_true"] == 0)]
    return len(tmp) / len(df)


def FN(df):
    tmp = df[(df["y_pred"] == 0) & (df["y_true"] == 1)]
    return len(tmp) / len(df)


def f_score(precision, recall):
    return 2 * precision * recall / (precision + recall)


def accuracy(df):
    _TP = TP(df)
    _FN = FN(df)
    _TN = TN(df)
    _FP = FP(df)
    return (_TP + _TN) / (_TP + _FN + _TN + _FP)


def f(a, b, x, y):
    return a * x + b * y


def squared_error(f, a, b, x, y, y_true):
    y_pred = f(a, b, x, y)
    return (y_true - y_pred) ** 2


def der_a(f, a, b, x, y, y_true):
    e1 = squared_error(f, a, b, x, y, y_true)
    e2 = squared_error(f, a + 0.00001, b, x, y, y_true)
    return (e2 - e1) / 0.00001


def der_b(f, a, b, x, y, y_true):
    e1 = squared_error(f, a, b, x, y, y_true)
    e2 = squared_error(f, a, b + 0.00001, x, y, y_true)
    return (e2 - e1) / 0.00001


lerning_rate = 0.1
a1, b1 = 3, 3
for _, row in df.iterrows():
    da = lerning_rate * der_a(f, a1, b1, row[0], row[1], row[2])
    db = lerning_rate * der_b(f, a1, b1, row[0], row[1], row[2])
    a1 -= da * lerning_rate
    b1 -= db * lerning_rate

print(a1, b1)

lerning_rate = 0.01
a2, b2 = 3, 3
for _, row in df.iterrows():
    da = lerning_rate * der_a(f, a2, b2, row[0], row[1], row[2])
    db = lerning_rate * der_b(f, a2, b2, row[0], row[1], row[2])
    a2 -= da * lerning_rate
    b2 -= db * lerning_rate

print(a2, b2)

lerning_rate = 0.001
a3, b3 = 3, 3
for _, row in df.iterrows():
    da = lerning_rate * der_a(f, a3, b3, row[0], row[1], row[2])
    db = lerning_rate * der_b(f, a3, b3, row[0], row[1], row[2])
    a3 -= da * lerning_rate
    b3 -= db * lerning_rate

print(a3, b3)


y_pred_list = []
y_true_list = []

for _, row in df.iterrows():
    if row[0] * 0.01 > 0.5 and row[1] * 0.01 > 0.5:
        y_pred_list.append(1)
    else:
        y_pred_list.append(0)

for _, row in df.iterrows():
    y_true_list.append(row[2])

# регрессия отличается от класиффикации тем что регресии возвращает нам одно число
# например стоимость дома на донный момент по каким-то кретериям и тд
# класиффикация возвращает нам true или false, 1 или 0 и тд


def create_our_dataset(y_true_list, y_pred_list, size=100):
    for i in range(size):
        true = y_true_list[i]
        pred = y_pred_list[i]
        yield {'y_pred': pred, 'y_true': true}


dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_our_dataset(y_true_list, y_pred_list, size=100):
    dataset = dataset.append(i, ignore_index=True)
print(dataset.head())

print(recall(dataset))
print(precision(dataset))
print(accuracy(dataset))
print(f_score(precision(dataset), recall(dataset)))
