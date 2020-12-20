import math
import pandas as pd
import numpy as np


def error(y_pred, y_true):
    delta = 10 ** -10
    return -y_true * math.log(y_pred + delta) - (1 - y_true) * math.log(1 + delta - y_pred)


def total_error(y_pred, y_true):
    _sum = 0
    for pred, true in zip(y_pred, y_true):
        _sum += error(pred, true)
    return _sum / len(y_pred)


def create_all_negative_true_data_set(size=1000):
    for i in range(size):
        pred = np.random.uniform(0, 1)
        true = 0
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


negative_data_set = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_all_negative_true_data_set(size=1000):
     negative_data_set = negative_data_set.append(i, ignore_index=True)


ideal_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_ideal_data_set():
    ideal_dataset = ideal_dataset.append(i, ignore_index=True)


positive_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_all_positive_preds_data_set():
    positive_dataset = positive_dataset.append(i, ignore_index=True)


one_positive_dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_one_positive_prediction_data_set():
    one_positive_dataset = one_positive_dataset.append(i, ignore_index=True)


# data set (negative_data_set):
list_pred_1 = []
list_true_1 = []
for _, row in negative_data_set.iterrows():
    list_pred_1.append(row[0])
    list_true_1.append(row[1])
print(total_error(list_pred_1, list_true_1))

# data set (ideal_dataset):
list_pred_2 = []
list_true_2 = []
for _, row in ideal_dataset.iterrows():
    list_pred_2.append(row[0])
    list_true_2.append(row[1])
print(total_error(list_pred_2, list_true_2))

# data set (positive_dataset):
list_pred_3 = []
list_true_3 = []
for _, row in positive_dataset.iterrows():
    list_pred_3.append(row[0])
    list_true_3.append(row[1])
print(total_error(list_pred_3, list_true_3))

# data set (one_positive_dataset):
list_pred_4 = []
list_true_4 = []
for _, row in one_positive_dataset.iterrows():
    list_pred_4.append(row[0])
    list_true_4.append(row[1])
print(total_error(list_pred_4, list_true_4))
