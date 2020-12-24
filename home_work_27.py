import pandas as pd
import matplotlib.pyplot as plt
import math


df = pd.read_csv('data.csv')


def recall(df):
    _TP = TP(df)
    _FN = FN(df)
    if _TP == 0:
        return 0
    return _TP / (_TP + _FN)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


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


def f(a1, a2, x1, x2, t):
    return a1 * x1 + a2 * x2 - t


x1 = df.iloc[:, 0]
x2 = df.iloc[:, 1]
y = df.iloc[:, 2]
x_values = [30, 100]
y_values = [90, 30]

admitted = df.loc[y == 1]
not_admitted = df.loc[y == 0]

plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not Admitted')
plt.plot(x_values, y_values)
plt.legend()
plt.show()