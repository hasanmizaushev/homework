import pandas as pd
import numpy as np
import random


def create_data_set(a=2, b=3, size=10):
    for i in range(size):
        x = np.random.uniform(-10, 10)
        y = np.random.uniform(-10, 10)
        noise = np.random.normal(loc=0, scale=0.001)
        z = a * x + b * y + noise
        yield {'x': x, 'y': y, 'z': z}


df = pd.DataFrame(columns=['x', 'y', 'z'])
for i in create_data_set(size=1000):
    df = df.append(i, ignore_index=True)

# print(df.head())

# find the average value x

mean_x = sum(list(df['x'])) / len(list(df['x']))
print(mean_x)

# find standard deviation x

std_x = np.std(list(df['x']))
print(std_x)

# find the value of the expression value = z - 2x - 3y
# and add all the values to the list_of_value

all_x = list(df['x'])
all_y = list(df['y'])
all_z = list(df['z'])

list_of_value = []

for i in range(len(all_x)):
    x1 = all_x[i]
    y1 = all_y[i]
    z1 = all_z[i]
    value = z1 - 2 * x1 - 3 * y1
    list_of_value.append(value)

# print(list_of_value)
# then find the average of the list_of_value

mean_list_of_value = sum(list_of_value) / len(list_of_value)
print(mean_list_of_value)

# find standard deviation list_of_value

std_list_of_value = np.std(list(list_of_value))
print(std_list_of_value)
