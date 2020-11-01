import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('hw15.csv').set_index('Unnamed: 0')
# print(df.head())

# a, b, c - koefs
# x, y, z - variables/vars


def f(koefs, variables):
    s = 0
    for i in range(len(koefs)):
        s += koefs[i] * variables[i]
    return s


def error(f, koefs, variables, F_true):
    F_pred = f(koefs, variables)
    # print(f_pred)
    return (F_pred - F_true) ** 2
# print(error(f, [1, 2, 3], [3, 2, 1], 12))

# d_error:
# koefs, variables, function, F_true
# return:
# list of ders


def d_error(f, koefs, variables, F_true):
    derivatives = []
    delta = 0.001
    f1 = error(f, koefs, variables, F_true)
    for i in range(len(koefs)):
        new_koefs = list(koefs)
        new_koefs[i] += delta
        f2 = error(f, new_koefs, variables, F_true)
        derivatives.append((f2 - f1) / delta)
        # print(new_koefs, variables, f2, f1)
    return derivatives


X = np.array(df.drop(['F'], axis=1))
y = np.array(df['F'])


def gradient_descent(f, X, y, lr=0.00001):
    koefs = [1] * X.shape[1]
    for i in range(X.shape[0]):
        derivatives = d_error(f, koefs, X[i, :], y[i])
        for j in range(len(koefs)):
            koefs[j] -= lr * derivatives[j]
        # print(koefs)
    return koefs


print(gradient_descent(f, X[:], y[:]))
