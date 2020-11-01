import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('hw14_data1.csv')
df2 = pd.read_csv('hw14_data2.csv')
df3 = pd.read_csv('hw14_data3.csv')

print(df1.head())


def our_prediction(a, x, b, y, c, z):
    return a * x + b * y + c * z


def error_da(f, a, x, b, y, c, z, F):
    da = 0.0001
    f1 = f(a, x, b, y, c, z)
    f2 = f(a + da, x, b, y, c, z)
    e1 = (F - f1) ** 2
    e2 = (F - f2) ** 2
    return (e2 - e1) / da


def error_db(f, a, x, b, y, c, z, F):
    db = 0.0001
    f1 = f(a, x, b, y, c, z)
    f2 = f(a, x, b + db, y, c, z)
    e1 = (F - f1) ** 2
    e2 = (F - f2) ** 2
    return (e2 - e1) / db


def error_dc(f, a, x, b, y, c, z, F):
    dc = 0.0001
    f1 = f(a, x, b, y, c, z)
    f2 = f(a, x, b, y, c + dc, z)
    e1 = (F - f1) ** 2
    e2 = (F - f2) ** 2
    return (e2 - e1) / dc


def function_abc(df, a, b, c):
    a, b, c = 1, 1, 1
    a_list = []
    b_list = []
    c_list = []
    learning_rate = 0.001
    for i, row in df.iterrows():
        x, y, z, F = row['x'], row['y'], row['z'], row['F']
        a -= learning_rate * error_da(our_prediction, a, x, b, y, c, z, F)
        b -= learning_rate * error_db(our_prediction, a, x, b, y, c, z, F)
        c -= learning_rate * error_db(our_prediction, a, x, b, y, c, z, F)
        a_list.append(a)
        b_list.append(b)
        c_list.append(c)
    plt.plot(c_list)
    plt.savefig("image.jpg")
    return a, b, c


print(function_abc(df1, 1, 1, 1))
print(function_abc(df2, 1, 1, 1))
print(function_abc(df3, 1, 1, 1))
