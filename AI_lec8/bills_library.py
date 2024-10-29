import csv
import random


from sklearn.model_selection import train_test_split

from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

#model = Perceptron()
#model = KNeighborsClassifier(n_neighbors=1)
#model = svm.SVC()
model = GaussianNB()

# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({"evidence": [float(cell) for cell in row[:4]],"label": "real" if row[4] == "0" else "fake"})
        
# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]

X_training, X_testing, y_training, y_testing = train_test_split(evidence, labels, test_size=0.2)

# Train the model
model.fit(X_training, y_training)

# Make predictions on the testing set
predictions = model.predict(X_testing)

# Compute how well we performed
correct = sum([y == p for y, p in zip(y_testing, predictions)])
incorrect = sum([y != p for y, p in zip(y_testing, predictions)])
total = len(predictions)

# Make a list of all the cases model got wrong
missed_bills = [(X,y) for X, y, p in zip(X_testing, y_testing, predictions) if y != p]

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total}%")

# check specific case with model, predict the value of the last bill from the missed_bills list
print(missed_bills[-1][0])

print(model.predict([missed_bills[-1][0]]))




