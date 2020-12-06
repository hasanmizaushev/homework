import pandas as pd


def create_dataset(size=10):
    for i in range(size):
        y_pred = 1
        y_true = 1
        yield {"y_pred": y_pred, "y_true": y_true}


def data_precision():
    precision = lambda TP, FP: TP / (TP + FP)
    df_p = pd.DataFrame(columns=["y_pred", "y_true"])
    for i in create_dataset(size=100):
        df_p = df_p.append(i, ignore_index=True)
    df_p["y_true"][-5:] = 0
    TP_p = len(df_p[(df_p["y_pred"] == 1) & (df_p["y_true"] == 1)])
    FP_p = len(df_p[(df_p["y_pred"] == 1) & (df_p["y_true"] == 0)])
    print(precision(TP_p, FP_p))


def data_recall():
    recall = lambda TP, FN: TP / (TP + FN)
    df_r = pd.DataFrame(columns=["y_pred", "y_true"])
    for i in create_dataset(size=100):
        df_r = df_r.append(i, ignore_index=True)
    df_r["y_pred"][-3:] = 0
    TP_r = len(df_r[(df_r["y_pred"] == 1) & (df_r["y_true"] == 1)])
    FN_r = len(df_r[(df_r["y_pred"] == 0) & (df_r["y_true"] == 1)])
    print(recall(TP_r, FN_r))


data_recall()
data_precision()
