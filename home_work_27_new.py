import pandas as pd
import matplotlib.pyplot as plt
import math


data = pd.read_csv('data.csv')


X = data.iloc[:, :-1]
y = data.iloc[:, -1]

admitted = data.loc[y == 1]
not_admitted = data.loc[y == 0]

# plots
plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Admitted')
plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not Admitted')
plt.plot([30, 100], [100, 30], label='Decision Boundary')
plt.legend()
plt.show()


def sigmoid(x):
    return 1 / (1 + math.e ** -x)


def f(row):
    return sigmoid(0.2 * row["first exam"] + 0.2 * row["second exam"] - 26)


def summ(x1, x2, a1=1, a2=1):
    theta = x1 + x2
    summ = theta / 5 + a1 / 5 + a2 / 5
    return print(summ, a1, a2, theta)


def transform(val):
    if val > 0.5:
        return 1
    else:
        return 0


data["sigmoid y_pred"] = data.apply(f, axis=1)
data["transformed_pred"] = data["sigmoid y_pred"].apply(transform)
print(data.head())


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
    tmp = df[(df["transformed_pred"] == 1) & (df["is admitted"] == 1)]
    return len(tmp) / len(df)


def TN(df):
    tmp = df[(df["transformed_pred"] == 0) & (df["is admitted"] == 0)]
    return len(tmp) / len(df)


def FP(df):
    tmp = df[(df["transformed_pred"] == 1) & (df["is admitted"] == 0)]
    return len(tmp) / len(df)


def FN(df):
    tmp = df[(df["transformed_pred"] == 0) & (df["is admitted"] == 1)]
    return len(tmp) / len(df)


def f_score(precision, recall):
    return 2 * precision * recall / (precision + recall)


print(precision(data))
print(recall(data))
