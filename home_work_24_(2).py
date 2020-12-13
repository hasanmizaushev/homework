import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())


def f_score(precision, recall):
    return 2 * precision * recall / (precision + recall)


def f_score_beta(precision, recall, beta=1):
    return (1 + beta) ** 2 * precision * recall / (precision * beta ** 2 + recall)


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


def our_own_formula(precision, recall):
    return precision * recall


# a) recall must be 1.0;
# b) precision must be 1.0;
# c) precision and recall must be 1.0;


def create_dataset_a_b_c(df):
    for i in range(100):
        y_true = df["is admitted"][i]
        y_pred = y_true
        yield {'y_pred': y_pred, 'y_true': y_true}


dataset = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_dataset_a_b_c(df):
    dataset = dataset.append(i, ignore_index=True)

print(recall(dataset))
print(precision(dataset))
print(our_own_formula(precision(dataset), recall(dataset)))


# d) recall must be 0


def create_dataset(df):
    for i in range(100):
        y_true = df["is admitted"][i]
        y_pred = 0
        yield {'y_pred': y_pred, 'y_true': y_true}


dataset_2 = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_dataset(df):
    dataset_2 = dataset_2.append(i, ignore_index=True)

print(recall(dataset_2))


# precision must be 0.01
# i don't know

# f-score must be close to 0.66 (+-0.01)


def create_dataset(df):
    for i in range(100):
        y_true = df["is admitted"][i]
        if i < 46:
            y_pred = 0
        else:
            y_pred = 1
        yield {'y_pred': y_pred, 'y_true': y_true}


dataset_3 = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_dataset(df):
    dataset_3 = dataset_3.append(i, ignore_index=True)

print(f_score(precision(dataset_3), recall(dataset_3)))


# f-score with beta=2 must be close to 0.7 (+-0.02)


def create_dataset(df):
    for i in range(100):
        y_true = df["is admitted"][i]
        if i < 74:
            y_pred = 0
        else:
            y_pred = 1
        yield {'y_pred': y_pred, 'y_true': y_true}


dataset_4 = pd.DataFrame(columns=["y_pred", "y_true"])
for i in create_dataset(df):
    dataset_4 = dataset_4.append(i, ignore_index=True)

print(f_score_beta(precision(dataset_4), recall(dataset_4), beta=2))
