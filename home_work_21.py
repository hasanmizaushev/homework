import pandas as pd
import math


df = pd.read_csv('tp_data.csv')
# print(df.head())


list_y_pred = []
for _, row in df.iterrows():
    list_y_pred.append(row[0])


list_y_true = []
for _, row in df.iterrows():
    list_y_true.append(row[1])


def standard_deviation(list_y_pred):
    counter = 0
    mean_number = sum(list_y_pred) / len(list_y_pred)
    for i in list_y_pred:
        counter += (i-mean_number)**2
    return math.sqrt(counter / (len(list_y_pred)-1))


mean_answer = sum(list_y_pred) / len(list_y_pred)
print(mean_answer)

print(standard_deviation(list_y_pred))


TP = 0
FP = 0
for i, j in zip(list_y_pred, list_y_true):
    if i == j:
        TP += 1
    else:
        FP += 1
# print(TP, FP)
# так ка в нашей таблице нет отрицательных значений то наш TN = 0
TN = 0
# так ка в нашей таблице нет отрицательных значений то наш FN = 0
FN = 0


def precision(tp, fp):
    pr = tp / (tp + fp)
    return pr


def recall(tp, fn):
    rc = tp / (tp + fn)
    return rc


print(precision(TP, FP))
print(recall(TP, FN))
