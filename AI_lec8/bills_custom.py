import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

# model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
model = GaussianNB()

print(type(model))
print(type(model).__name__)
print(model.__dict__)

# read data from csv file, store as dict of evidence list and label list
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        evidence = []
        label = ''
        for i in range(4):
            evidence.append(float(row[i]))
            
        if row[4] == '0':
            label = 'real'
        else:
            label = 'fake'
            
        
        data.append({"evidence": evidence,"label": label })

# Separate data into training and testing groups
split = int(0.2 * len(data))
random.shuffle(data)
testing = data[:split]
training = data[split:]

print('training data size:', len(training))
print('testing data size:', len(testing))

# Train model on training set
X_training = [row["evidence"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)

# Make predictions on the testing set
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

print(type(predictions))
print(predictions.shape)

print(predictions[:10])
print(y_testing[:10])

# Model test
correct = 0
incorrect = 0
total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total}%")
