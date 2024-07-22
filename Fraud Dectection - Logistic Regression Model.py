# -*- coding: utf-8 -*-
"""CodeSoft Task 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qF7X1kBzzHuCx5uOgEYa3gATNJCdROEM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler , LabelEncoder

fraud_data = pd.read_csv('/content/fraud_train.csv')

fraud_data.head()

fraud_data.shape

fraud_data.isnull().sum()

fraud_data.describe()

X = fraud_data.drop(columns='Class', axis=1)
Y = fraud_data['Class']

standardScaler = StandardScaler()

standardScaler.fit(X)

standardScaler_data = standardScaler.transform(X)

print(standardScaler_data)

X = standardScaler_data
Y = fraud_data['Class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

model = LogisticRegression()

model.fit(X_train, Y_train)

train_prediction = model.predict(X_train)
test_prediction = model.predict(X_test)

score_train = accuracy_score(Y_train, train_prediction)
score_test = accuracy_score(Y_test, test_prediction)

print(score_train)
print(score_test)

input=(8365.0,-0.6550932346466539,1.10228328336999,1.61091369534439,2.54244016040913,0.928295331124692,0.344426736595771,0.3408310541008969,-0.0041300220965452,-0.0393246461073465,0.2450177793449129,0.0769723350061413,-3.040577574944629,1.8063944413176,1.65503728786487,0.375913126976771,-0.0246519325350989,0.566769329751559,0.0792675879574908,-0.289508406509825,-0.0360406561066014,0.0257102669375876,0.297263170395489,-0.195074280789403,-0.476353241537347,-0.269339144085593,0.154727916384427,-0.0040280729781211,0.155043678042639,16.93)
input_data = np.asarray(input)
input_data_reshaped = input_data.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if prediction == 0.0:
  print('Not Fraud')
else:
  print('Fraud')

