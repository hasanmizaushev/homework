import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data.csv')


def recall(df):
    _TP = TP(df)
    _FN = FN(df)
    if _TP == 0:
        return 0
    return _TP / (_TP + _FN)


def accuracy(df):
    _TP = TP(df)
    _FN = FN(df)
    _TN = TN(df)
    _FP = FP(df)
    return (_TP + _TN) / (_TP + _FN + _TN + _FP)


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


def f(a, b, x, y):
    return a + x + b + y


def error(f, a, b, x, y, y_true):
    y_pred = f(a, b, x, y)
    return (y_true - y_pred) ** 2


def der_a(f, a, b, x, y, y_true):
    e1 = error(f, a, b, x, y, y_true)
    e2 = error(f, a + 0.00001, b, x, y, y_true)
    return (e2 - e1) / 0.00001


def der_b(f, a, b, x, y, y_true):
    e1 = error(f, a, b, x, y, y_true)
    e2 = error(f, a, b + 0.00001, x, y, y_true)
    return (e2 - e1) / 0.00001


l_r = 0.01
a, b = 2, 2
for _, row in df.iterrows():
    da = l_r * der_a(f, a, b, row[0], row[1], row[2])
    db = l_r * der_b(f, a, b, row[0], row[1], row[2])
    a -= da * l_r
    b -= db * l_r
print(a, b)


l_r = 0.001
a2, b2 = 2, 2
for _, row in df.iterrows():
    da = l_r * der_a(f, a2, b2, row[0], row[1], row[2])
    db = l_r * der_b(f, a2, b2, row[0], row[1], row[2])
    a2 -= da * l_r
    b2 -= db * l_r
print(a2, b2)


l_r = 0.0001
a3, b3 = 2, 2
for _, row in df.iterrows():
    da = l_r * der_a(f, a3, b3, row[0], row[1], row[2])
    db = l_r * der_b(f, a3, b3, row[0], row[1], row[2])
    a3 -= da * l_r
    b3 -= db * l_r
print(a, b)


y_true_list = []
y_pred_list = []
for _, row in df.iterrows():
    y_pred_list.append(f(a, b, row[0], row[1]))


for i, row in df.iterrows():
    if y_pred_list[i] > 0.5:
        y_pred_list[i] = 1
    else:
        y_pred_list[i] = 0

df["y_pred"] = y_pred_list
df.rename(columns={"is admitted": "y_true"}, inplace=True)
print(df.head(10))


print(recall(df))
print(precision(df))
print(accuracy(df))
print(f_score(precision(df), recall(df)))