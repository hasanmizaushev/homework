import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


def create_all_negative_true_data_set(size=1000):
    for i in range(size):
        pred = np.random.uniform(0, 1)
        true = 0
        yield {"y_pred": pred, "y_true": true}


def create_data_set(size=1000):
    for i in range(size):
        pred = np.random.uniform(0, 1)
        true = np.random.uniform(0, 1)
        yield {"y_pred": pred, "y_true": true}


def create_ideal_data_set(size=1000):
    for i in range(size):
        true = np.random.randint(2)
        pred = true
        yield {'y_pred': pred, 'y_true': true}


def create_all_positive_preds_data_set(size=1000):
    for i in range(size):
        true = np.random.randint(2)
        pred = 1
        yield {'y_pred': pred, 'y_true': true}


def create_one_positive_prediction_data_set(size=1000):
    yield {'y_pred': 1, 'y_true': 1}
    for i in range(size):
        true = np.random.randint(2)
        pred = 0
        yield {'y_pred': pred, 'y_true': true}


def create_unbalance_data_set(size=1000):
    yield {'y_pred': 0, 'y_true': 1}
    for i in range(size):
        true = 0
        pred = 0
        yield {'y_pred': pred, 'y_true': true}


def harmonic_mean(x):
    a = 0
    for i in x:
        a += i**(-1)
    return (a / len(x))**(-1)


def TP(df):
    tmp = df[(df['y_pred'] == 1) & (df['y_true'] == 1)]
    return len(tmp) / len(df)


def TN(df):
    tmp = df[(df['y_pred'] == 0) & (df['y_true'] == 0)]
    return len(tmp) / len(df)


def FP(df):
    tmp = df[(df['y_pred'] == 1) & (df['y_true'] == 0)]
    return len(tmp) / len(df)


def FN(df):
    tmp = df[(df['y_pred'] == 0) & (df['y_true'] == 1)]
    return len(tmp) / len(df)


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


def function_min(precision, recall):
    return min(recall, precision)


def mean(x):
    return sum(x) / len(x)


def function_mean(precision, recall):
    return mean([precision, recall])


def function_multiply(precision, recall):
    return precision * recall


positive_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_all_positive_preds_data_set():
    positive_dataset = positive_dataset.append(i, ignore_index=True)

unbalanced_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_unbalance_data_set():
    unbalanced_dataset = unbalanced_dataset.append(i, ignore_index=True)

ideal_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_ideal_data_set():
    ideal_dataset = ideal_dataset.append(i, ignore_index=True)

one_positive_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_one_positive_prediction_data_set():
    one_positive_dataset = one_positive_dataset.append(i, ignore_index=True)

data_set = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_data_set(size=1000):
    data_set = data_set.append(i, ignore_index=True)

negative_data_set = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_all_negative_true_data_set(size=1000):
     negative_data_set = negative_data_set.append(i, ignore_index=True)


# print(function_min(precision(positive_dataset), recall(positive_dataset)))
# print(function_min(precision(unbalanced_dataset), recall(unbalanced_dataset)))
# print(function_min(precision(ideal_dataset), recall(ideal_dataset)))
# print(function_min(precision(one_positive_dataset), recall(one_positive_dataset)))
# print(function_min(precision(data_set), recall(data_set)))
# print(function_min(precision(negative_data_set), recall(negative_data_set)))

# print(function_mean(precision(positive_dataset), recall(positive_dataset)))
# print(function_mean(precision(unbalanced_dataset), recall(unbalanced_dataset)))
# print(function_mean(precision(ideal_dataset), recall(ideal_dataset)))
# print(function_mean(precision(one_positive_dataset), recall(one_positive_dataset)))
# print(function_mean(precision(data_set), recall(data_set)))
# print(function_mean(precision(negative_data_set), recall(negative_data_set)))

# print(function_multiply(precision(positive_dataset), recall(positive_dataset)))
# print(function_multiply(precision(unbalanced_dataset), recall(unbalanced_dataset)))
# print(function_multiply(precision(ideal_dataset), recall(ideal_dataset)))
# print(function_multiply(precision(one_positive_dataset), recall(one_positive_dataset)))
# print(function_multiply(precision(data_set), recall(data_set)))
# print(function_multiply(precision(negative_data_set), recall(negative_data_set)))

# Data set             # metrics # Result # Comment
# positive_dataset     # min()       # 0.48  # Correct on 50%, dataset isn't ideal
# unbalanced_dataset   # min()       # 0     # Not correct, dataset isn't ideal
# ideal_dataset        # min()       # 1     # Correct, dataset is ideal
# one_positive_dataset # min()       # 0.002 # Not correct, dataset isn't ideal
# data_set             # min()       # 0     # Not correct, dataset isn't ideal
# negative_data_set    # min()       # 0     # Not correct, dataset isn't ideal

# positive_dataset     # mean()      # 0.755 # Correct on 75%, dataset is normal
# unbalanced_dataset   # mean()      # 0.0   # Not correct, dataset isn't ideal
# ideal_dataset        # mean()      # 1.0   # Correct, dataset is ideal
# one_positive_dataset # mean()      # 0.501 # Correct on 50%, dataset isn't ideal
# data_set             # mean()      # 0     # Not correct, dataset isn't ideal
# negative_data_set    # mean()      # 0     # Not correct, dataset isn't ideal

# positive_dataset     # multiply()  # 0.493 # Correct on 50%, dataset isn't ideal
# unbalanced_dataset   # multiply()  # 0     # Not correct, dataset isn't ideal
# ideal_dataset        # multiply()  # 1.0   # Correct, dataset is ideal
# one_positive_dataset # multiply()  # 0.001 # Not correct, dataset isn't ideal
# data_set             # multiply()  # 0     # Not correct, dataset isn't ideal
# negative_data_set    # multiply()  # 0     # Not correct, dataset isn't ideal
