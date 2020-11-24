import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import csv


df = pd.read_csv('heart.csv')

# initial columns feture and target data
X_Data = df[df.columns[:13]]
Y_Data = df[["target"]]

# minMax scaler function
scaler = MinMaxScaler()
scaler.fit(X_Data)
Data_Norm = scaler.transform(X_Data)

# list for data normalization
data_norm = []

# normalization process
for row in Data_Norm:
    row_data = []
    for cell in row:
        cell = round(cell, 3)
        row_data.append(cell)
    data_norm.append(row_data)

# initial directory file, name file, dan initialization file csv
f = open('data.csv', 'w')
w = csv.writer(f)
w.writerow(('age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
            ))

# targer/class data
kelas = Y_Data.values.tolist()

# write file csv
for index, data in enumerate(data_norm):
    rows = data + kelas[index]
    w.writerow(rows)

# close csv process
f.close()
