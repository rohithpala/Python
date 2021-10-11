# importing dependencies
# import inline as inline
# import matplotlib
# import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# storing
data = pd.read_csv("mnist_train.csv")

# viewing column heads
data.head()

# extracting data and viewing it
a = data.iloc[4, 1:].values
a = a.reshape(28, 28).astype('uint8')

# reshaping the extracted data
plt.imshow(a)

# separating labels and pixel/data values
x = data.iloc[:, 1:]
y = data.iloc[:, 0]

# Creating test and train batches.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
# test_size = 0.2 -> means the test data contains 20% of the original data and the reamaining is to train the rf clasifier
# random_state means randomness of picking the data

# checking the data
x_train.head()  # Has data except labels

y_train.head()  # Has only Labels

# calling rf classifier
rf = RandomForestClassifier(n_estimators=100)

# fitting the data
rf.fit(x_train, y_train)  # training the model with x_train and y_train

# prediction of test data
predictor = rf.predict(x_test)
print(predictor)  # this is the data predicted by the rf classifier and this is checked with the actual labels present in y_test

# comparing the predicted data with the labels of them present in y_test and also finding the accuracy
s = y_test.values
count = 0
l = len(predictor)

# calculating the accuracy
for i in range(l):
    if s[i] == predictor[i]:
        count += 1
print(count)
print("Accuracy =", count / l)  # our classifier is 96.841% accurate
